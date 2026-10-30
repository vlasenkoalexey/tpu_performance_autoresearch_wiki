---
title: 'Module: torchtitan/experiments/rl/examples/alphabet_sort/config_registry.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/rl/examples/alphabet_sort/config_registry.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.rl.examples.alphabet_sort.config_registry`/
symbols:
  rl_grpo_qwen3_moe_debug_varlen_batch_invariant: rl_grpo_qwen3_moe_debug_varlen_batch_invariant().
  rl_grpo_qwen3_0_6b_varlen_batch_invariant: rl_grpo_qwen3_0_6b_varlen_batch_invariant().
  rl_grpo_qwen3_0_6b_varlen: rl_grpo_qwen3_0_6b_varlen().
  rl_grpo_gpt_oss_debug_varlen_batch_invariant: rl_grpo_gpt_oss_debug_varlen_batch_invariant().
  rl_grpo_gpt_oss_20b_varlen: rl_grpo_gpt_oss_20b_varlen().
  rl_grpo_qwen3_moe_debug_varlen: rl_grpo_qwen3_moe_debug_varlen().
  rl_grpo_qwen3_30b_a3b_varlen: rl_grpo_qwen3_30b_a3b_varlen().
  rl_grpo_qwen3_5_debug_varlen: rl_grpo_qwen3_5_debug_varlen().
  rl_grpo_qwen3_5_9b_varlen: rl_grpo_qwen3_5_9b_varlen().
  rl_grpo_qwen3_0_6b_flex: rl_grpo_qwen3_0_6b_flex().
  rl_grpo_gpt_oss_debug_varlen: rl_grpo_gpt_oss_debug_varlen().
  rl_grpo_qwen3_14b: rl_grpo_qwen3_14b().
  rl_grpo_qwen3_1_7b: rl_grpo_qwen3_1_7b().
  rl_grpo_qwen3_0_6b_flex_batch_invariant: rl_grpo_qwen3_0_6b_flex_batch_invariant().
  rl_grpo_qwen3_moe_debug_deepep: rl_grpo_qwen3_moe_debug_deepep().
  rl_grpo_qwen3_6_27b_varlen_perf: rl_grpo_qwen3_6_27b_varlen_perf().
  rl_grpo_qwen3_5_9b_varlen_batch_invariant: rl_grpo_qwen3_5_9b_varlen_batch_invariant().
  rl_grpo_qwen3_5_debug_varlen_batch_invariant: rl_grpo_qwen3_5_debug_varlen_batch_invariant().
  _qwen3_rl_model_registry: _qwen3_rl_model_registry().
  _qwen3_5_rl_model_registry: _qwen3_5_rl_model_registry().
  rl_grpo_qwen3_30b_a3b_varlen_perf: rl_grpo_qwen3_30b_a3b_varlen_perf().
  _BATCH_INVARIANT_DEBUG: _BATCH_INVARIANT_DEBUG.
---
# Module: [`torchtitan/experiments/rl/examples/alphabet_sort/config_registry.py`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/alphabet_sort/config_registry.py)

## Functions
- <a id="_qwen3_5_rl_model_registry"></a>`_qwen3_5_rl_model_registry(flavor: str, *, seq_len: int, attn_backend: str = "varlen", converters: list[ModelConfigConverter.Config] | None = None)` — [`L963`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/alphabet_sort/config_registry.py#L963) — ``qwen3_5.model_registry`` for RL, with the lm_head fp32 cast always on.
- <a id="_qwen3_rl_model_registry"></a>`_qwen3_rl_model_registry(flavor: str, *, seq_len: int, attn_backend: str, converters: list[ModelConfigConverter.Config] | None = None)` — [`L66`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/alphabet_sort/config_registry.py#L66) — ``qwen3.model_registry`` for RL, with the lm_head fp32 cast always on.
- <a id="rl_grpo_gpt_oss_20b_varlen"></a>`rl_grpo_gpt_oss_20b_varlen()` — [`L249`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/alphabet_sort/config_registry.py#L249) — GRPO training config for GPT-OSS-20B with varlen attention.
- <a id="rl_grpo_gpt_oss_debug_varlen"></a>`rl_grpo_gpt_oss_debug_varlen()` — [`L318`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/alphabet_sort/config_registry.py#L318) — Small GPT-OSS debug config (random init) to exercise the full RL loop.
- <a id="rl_grpo_gpt_oss_debug_varlen_batch_invariant"></a>`rl_grpo_gpt_oss_debug_varlen_batch_invariant()` — [`L378`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/alphabet_sort/config_registry.py#L378) — Small GPT-OSS debug config in deterministic + batch-invariant mode.
- <a id="rl_grpo_qwen3_0_6b_flex"></a>`rl_grpo_qwen3_0_6b_flex()` — [`L150`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/alphabet_sort/config_registry.py#L150) — GRPO training config for Qwen3-0.6B with flex attention (4 GPUs: 2 gen + 2 train).
- <a id="rl_grpo_qwen3_0_6b_flex_batch_invariant"></a>`rl_grpo_qwen3_0_6b_flex_batch_invariant()` — [`L210`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/alphabet_sort/config_registry.py#L210) — GRPO training config for Qwen3-0.6B with flex attention and batch invariance
- <a id="rl_grpo_qwen3_0_6b_varlen"></a>`rl_grpo_qwen3_0_6b_varlen()` — [`L86`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/alphabet_sort/config_registry.py#L86) — GRPO training config for Qwen3-0.6B (6 GPUs: 4 gen + 2 train). — documented in [rl-training](../../../../../../concepts/rl-training.md)
- <a id="rl_grpo_qwen3_0_6b_varlen_batch_invariant"></a>`rl_grpo_qwen3_0_6b_varlen_batch_invariant()` — [`L886`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/alphabet_sort/config_registry.py#L886) — On-policy GRPO config for Qwen3-0.6B (8 GPUs: trainer TP=2 + 3 generators TP=2). — documented in [rl-training](../../../../../../concepts/rl-training.md)
- <a id="rl_grpo_qwen3_14b"></a>`rl_grpo_qwen3_14b()` — [`L515`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/alphabet_sort/config_registry.py#L515) — GRPO training config for Qwen3-14B (16 GPUs: 8 gen + 8 train).
- <a id="rl_grpo_qwen3_1_7b"></a>`rl_grpo_qwen3_1_7b()` — [`L456`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/alphabet_sort/config_registry.py#L456) — GRPO training config for Qwen3-1.7B (6 GPUs: 4 gen + 2 train).
- <a id="rl_grpo_qwen3_30b_a3b_varlen"></a>`rl_grpo_qwen3_30b_a3b_varlen()` — [`L785`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/alphabet_sort/config_registry.py#L785) — GRPO training config for Qwen3-30B-A3B MoE (8 GPUs: 4 gen + 4 train). — documented in [rl-training](../../../../../../concepts/rl-training.md)
- <a id="rl_grpo_qwen3_30b_a3b_varlen_perf"></a>`rl_grpo_qwen3_30b_a3b_varlen_perf()` — [`L852`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/alphabet_sort/config_registry.py#L852) — Qwen3-30B-A3B GRPO with throughput overrides (8 GPUs: 4 gen + 4 train).
- <a id="rl_grpo_qwen3_5_9b_varlen"></a>`rl_grpo_qwen3_5_9b_varlen()` — [`L982`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/alphabet_sort/config_registry.py#L982) — Qwen3.5-9B GRPO with trainer and generator TP=2 (6 GPUs).
- <a id="rl_grpo_qwen3_5_9b_varlen_batch_invariant"></a>`rl_grpo_qwen3_5_9b_varlen_batch_invariant()` — [`L1044`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/alphabet_sort/config_registry.py#L1044) — On-policy, batch-invariant Qwen3.5-9B GRPO with matching TP=2.
- <a id="rl_grpo_qwen3_5_debug_varlen"></a>`rl_grpo_qwen3_5_debug_varlen()` — [`L1068`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/alphabet_sort/config_registry.py#L1068) — Random-init Qwen3.5 GRPO config for CI.
- <a id="rl_grpo_qwen3_5_debug_varlen_batch_invariant"></a>`rl_grpo_qwen3_5_debug_varlen_batch_invariant()` — [`L1127`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/alphabet_sort/config_registry.py#L1127) — On-policy, batch-invariant Qwen3.5 GRPO config for CI.
- <a id="rl_grpo_qwen3_6_27b_varlen_perf"></a>`rl_grpo_qwen3_6_27b_varlen_perf()` — [`L1149`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/alphabet_sort/config_registry.py#L1149) — Qwen3.6-27B GRPO with fused OffsetRMSNorm on trainer and generator.
- <a id="rl_grpo_qwen3_moe_debug_deepep"></a>`rl_grpo_qwen3_moe_debug_deepep()` — [`L649`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/alphabet_sort/config_registry.py#L649) — Debug MoE config on the DeepEP v2 backend with a cudagraph-capturable generator
- <a id="rl_grpo_qwen3_moe_debug_varlen"></a>`rl_grpo_qwen3_moe_debug_varlen()` — [`L575`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/alphabet_sort/config_registry.py#L575) — Debug MoE config with EP+TP on generator (8 GPUs: 4 gen + 4 train).
- <a id="rl_grpo_qwen3_moe_debug_varlen_batch_invariant"></a>`rl_grpo_qwen3_moe_debug_varlen_batch_invariant()` — [`L693`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/alphabet_sort/config_registry.py#L693) — Batch-invariant MoE EP config for bitwise parity testing (8 GPUs). — documented in [rl-training](../../../../../../concepts/rl-training.md)

## Module values
- <a id="_BATCH_INVARIANT_DEBUG"></a>`_BATCH_INVARIANT_DEBUG` — [`L63`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/alphabet_sort/config_registry.py#L63)

