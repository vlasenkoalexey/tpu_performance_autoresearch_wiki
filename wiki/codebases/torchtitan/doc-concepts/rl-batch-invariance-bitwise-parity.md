---
title: RL batch invariance and trainer/generator bitwise parity
type: doc-concept
provenance: doc
source: torchtitan/experiments/rl/docs/bitwise_parity.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T06:34:20Z}
---
# RL batch invariance and trainer/generator bitwise parity

## Definition
In RL the generator scores completions in one batch composition (e.g. 8 completions) and the trainer recomputes log-probs in another (e.g. 2 after DP sharding). Floating-point accumulation order in GEMM, softmax, reductions and collectives depends on shapes, so the same input yields different log-probs - and tiny drift can flip MoE top-k routing. **Batch-invariant mode** forces both sides to run the same ops with the same accumulation order, giving bitwise-identical log-probs (`kl_div = logprob_diff = 0`) under supported layouts.

## In torchtitan (grounded)
- Gate: [`DebugConfig.batch_invariant`](../catalog/torchtitan/config/configs.md#DebugConfig.batch_invariant) plus [`DebugConfig.deterministic`](../catalog/torchtitan/config/configs.md#DebugConfig.deterministic) on both the trainer and generator configs.
- Shared toggle: [`set_batch_invariance`](../catalog/torchtitan/distributed/utils.md#set_batch_invariance), called by [`PolicyTrainer`](../catalog/torchtitan/experiments/rl/actors/trainer.md#PolicyTrainer), [`VLLMGenerator`](../catalog/torchtitan/experiments/rl/actors/generator.md#VLLMGenerator) and standalone `generate.py`. It (a) registers the upstream `batch_invariant_ops` Triton overrides for `mm`, `addmm`, `_log_softmax`, `mean.dim` (fixed tile iteration order); (b) sets NCCL env vars for single-channel tree all-reduce, Simple protocol, no SHARP/NVLS (must precede `init_process_group`); (c) disables TF32 and reduced-precision bf16/fp16 reductions.
- Flash-attention split-k: [`VarlenInnerAttention.forward`](../catalog/torchtitan/models/common/attention.md#VarlenInnerAttention.forward) forces `num_splits=1` for FA3 when [`is_in_batch_invariant_mode`](../catalog/torchtitan/distributed/utils.md#is_in_batch_invariant_mode) is true.
- Generator-only patches (`batch_invariance.py`): varlen attention runs TorchTitan's own `VarlenInnerAttention` through vLLM's custom backend; flex attention uses [`BatchInvariantFlexConverter`](../catalog/torchtitan/experiments/rl/batch_invariance.md#BatchInvariantFlexConverter) (a model-config converter pinning `BLOCK_M = BLOCK_N = 16` and the Triton backend, avoiding `flex_decode`); [`force_logprobs_fn_for_batch_invariance`](../catalog/torchtitan/experiments/rl/batch_invariance.md#force_logprobs_fn_for_batch_invariance) replaces vLLM's fused sampler log-prob kernel with the trainer's [`compute_logprobs`](../catalog/torchtitan/components/loss.md#compute_logprobs). GPT-OSS attention sinks use the same post-softmax rescale ([`apply_attention_sink_rescale`](../catalog/torchtitan/models/gpt_oss/model.md#apply_attention_sink_rescale)) on both sides; the vLLM wrapper installs it as the attention `out_transform`.
- Precision: both sides compute in bf16. The generator runs `model_dtype="bfloat16"`; the trainer keeps fp32 master weights and relies on FSDP mixed precision to cast to bf16 before forward. `parallelize_qwen3` ([`parallelize_qwen3`](../catalog/torchtitan/models/qwen3/parallelize.md#parallelize_qwen3)) always applies [`apply_fsdp_to_decoder`](../catalog/torchtitan/distributed/fsdp.md#apply_fsdp_to_decoder), so the cast happens even at `data_parallel_shard_degree=1`. RoPE handling is covered in [fsdp-cast-forward-inputs-fp32-rope](fsdp-cast-forward-inputs-fp32-rope.md).
- Configs: e.g. [`rl_grpo_qwen3_0_6b_varlen_batch_invariant`](../catalog/torchtitan/experiments/rl/examples/alphabet_sort/config_registry.md#rl_grpo_qwen3_0_6b_varlen_batch_invariant), [`rl_grpo_qwen3_0_6b_flex_batch_invariant`](../catalog/torchtitan/experiments/rl/examples/alphabet_sort/config_registry.md#rl_grpo_qwen3_0_6b_flex_batch_invariant).

## Why it matters / when it applies
- **Measured cost** (doc; Qwen3-8B Search-R1, 8xH100, trainer TP2 / generator TP2, on-policy, 30 steps, medians):

  | metric | BI off | BI on | effect |
  |---|---|---|---|
  | wall-clock / step | 136.4 s | 133.6 s | ~1.0x |
  | generator inter-token latency | 9.6 ms | 22.8 ms | 2.4x slower |
  | generator decode time | 177 ms | 460 ms | 2.6x slower |
  | trainer fwd/bwd throughput | 370 tok/s | 127 tok/s | 2.9x slower |
  | trainer full-step throughput | 11.1 tok/s | 9.2 tok/s | 1.2x slower |
  | kl_div max / logprob_diff max | 0.0084 / 1.56 | 0 / 0 | bitwise parity |

  Raw compute is ~2.4-2.9x slower; Search-R1 hides it because the step is dominated by multi-turn orchestration, CPU retrieval and straggler waits. A compute-bound workload would show the ~2.5x in wall-clock. Use BI for debugging and controlled on-policy studies, not throughput.
- Limitations: trainer and generator must use the same TP degree; sequence parallelism is unsupported (reduce-scatter has no tree implementation, ring is non-deterministic).
- **TPU relevance.** Every mechanism here is CUDA/NCCL/Triton-specific (cuBLAS tiles, FA3 split-k, NCCL algorithms, TF32). The general lesson for TPU parity work is the checklist itself: match kernels, tile sizes, reduction order, collective algorithm and precision boundaries on both sides.

**Doc vs code at this commit:** the doc says FA2 is already batch-invariant. The code forces `num_splits=1` for FA2 unconditionally, as a workaround for intermittent NaNs in FA2's auto split heuristic with paged KV, so FA2 gets the same treatment regardless of mode. The doc also names the canonical FSDP helper `apply_fsdp` in `distributed/fsdp.py`; the function there is `apply_fsdp_to_decoder`.

## Connections
- Code concepts: [rl-training](../concepts/rl-training.md), [parallel-dims-and-parallelization](../concepts/parallel-dims-and-parallelization.md), [model-building-blocks](../concepts/model-building-blocks.md), [qwen3-model](../concepts/qwen3-model.md), [gpt-oss-model](../concepts/gpt-oss-model.md)
- Module catalogs: [distributed/utils](../catalog/torchtitan/distributed/utils.md), [rl/batch_invariance](../catalog/torchtitan/experiments/rl/batch_invariance.md), [models/common/attention](../catalog/torchtitan/models/common/attention.md), [distributed/fsdp](../catalog/torchtitan/distributed/fsdp.md)
- Related doc-concepts: [fsdp-cast-forward-inputs-fp32-rope](fsdp-cast-forward-inputs-fp32-rope.md), [titanrl-architecture](titanrl-architecture.md), [rl-search-r1-multiturn-tool-use](rl-search-r1-multiturn-tool-use.md)

## Source
Extracted from `torchtitan/experiments/rl/docs/bitwise_parity.md` and the "Trainer/generator consistency" section of `torchtitan/experiments/rl/README.md` (kept in place).
