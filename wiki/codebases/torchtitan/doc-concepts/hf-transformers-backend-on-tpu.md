---
title: HF transformers modeling backend on TPU (zero-port bring-up lane)
type: doc-concept
provenance: doc
source: torchtitan/experiments/tpu/transformers_modeling_backend/README.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T06:34:20Z}
---
# HF transformers modeling backend on TPU (zero-port bring-up lane)

## Definition
The TPU lane of the HF transformers modeling backend trains decoder-only Hub models on Cloud TPU
**without porting them**: the model is built from the checkpoint's `config.json` (random init),
sharded with SimpleFSDP, and runs HF's modeling code with TPU kernels swapped in underneath
(splash attention via HF's attention interface, fused Pallas CE, per-layer compile, and for MoE
TorchTitan's grouped experts + TPU dispatcher). It is explicitly **experimental backend coverage**
for bring-up and finding where TPU perf work would pay - not tuned production recipes (use a native
recipe under `recipes/` for that).

## In torchtitan (grounded)
- Job config: [`TPUTransformersBackendConfig`](../catalog/torchtitan/experiments/tpu/transformers_modeling_backend/job_config.md#TPUTransformersBackendConfig)
  subclasses `TPUTrainerConfig` and adds [`hf_model`](../catalog/torchtitan/experiments/tpu/transformers_modeling_backend/job_config.md#TPUTransformersBackendConfig.hf_model)
  (Hub id or local dir; only `config.json` is read) and
  [`hf_config_overrides`](../catalog/torchtitan/experiments/tpu/transformers_modeling_backend/job_config.md#TPUTransformersBackendConfig.hf_config_overrides)
  (JSON edits applied after the flavor).
- All configs come from [`_tpu_hf_config`](../catalog/torchtitan/experiments/tpu/transformers_modeling_backend/config_registry.md#_tpu_hf_config):
  SimpleFSDP (`spmd_backend="spmd_types"`), `compile.mode="layer"`, splash tiles at 1024, Grain c4_test
  loader, `block_causal` (document) masking so a packed 16k stream is not one giant causal problem.
- Model wrapper: [`TPUHFTransformerModel`](../catalog/torchtitan/experiments/tpu/transformers_modeling_backend/model.md#TPUHFTransformerModel);
  MoE swap [`substitute_tpu_experts`](../catalog/torchtitan/experiments/tpu/transformers_modeling_backend/model.md#substitute_tpu_experts);
  splash adapter [`splash_attention_forward`](../catalog/torchtitan/experiments/tpu/transformers_modeling_backend/attention.md#splash_attention_forward)
  (falls back to SDPA, logged once per reason); parallelizer
  [`parallelize_hf_transformers_tpu`](../catalog/torchtitan/experiments/tpu/transformers_modeling_backend/parallelize.md#parallelize_hf_transformers_tpu).

| Config | Attention | Loss | Compile | AC | MoE experts |
|---|---|---|---|---|---|
| [`hf_full_max`](../catalog/torchtitan/experiments/tpu/transformers_modeling_backend/config_registry.md#hf_full_max) | splash | fused CE (b=2048) | per layer | selective, keeps attention output | - |
| [`hf_full_max_plain_ce`](../catalog/torchtitan/experiments/tpu/transformers_modeling_backend/config_registry.md#hf_full_max_plain_ce) | splash | model head + plain CE | per layer | selective, keeps attention | - |
| [`hf_moe_auto`](../catalog/torchtitan/experiments/tpu/transformers_modeling_backend/config_registry.md#hf_moe_auto) | splash | plain CE | per layer | selective (default) | Pallas grouped mm |
| [`hf_moe_auto_compile`](../catalog/torchtitan/experiments/tpu/transformers_modeling_backend/config_registry.md#hf_moe_auto_compile) | splash | plain CE | per layer | selective | `torch._grouped_mm` (A/B reference) |
| [`hf_moe_auto_eager`](../catalog/torchtitan/experiments/tpu/transformers_modeling_backend/config_registry.md#hf_moe_auto_eager) | splash | plain CE | off | selective | `torch._grouped_mm` |
| [`hf_debugmodel`](../catalog/torchtitan/experiments/tpu/transformers_modeling_backend/config_registry.md#hf_debugmodel) / [`hf_debugmodel_max`](../catalog/torchtitan/experiments/tpu/transformers_modeling_backend/config_registry.md#hf_debugmodel_max) / `hf_debugmodel_kernels_{sdpa,splash}` | two-layer debug sizes for smoke / parity tests | | | | |

Attention-saving AC is [`AttentionSavingSelectiveAC`](../catalog/torchtitan/experiments/tpu/activation_checkpoint.md#AttentionSavingSelectiveAC).

### Knobs (README "Common flags")
- **Batch = token budget**: per-chip sequences = `num_tokens_per_microbatch_per_dp_rank /
  max_context_length`; global batch above `microbatch x chips` means gradient accumulation
  (`--training.max_context_length`, `--training.num_tokens_per_microbatch_per_dp_rank`,
  `--training.num_tokens_per_train_step`). Raise until throughput stops improving or HBM runs out.
- **Splash tiles** `--splash_attention_kernel.sa_block_{q,kv,kv_compute,q_dkv,kv_dkv,kv_dkv_compute}`
  (default 1024, stepped down to the largest size dividing the sequence; other `sa_*` fields ignored
  and reported); `--splash_attention_kernel.no-sa_use_document_aware_block_skipping` masks instead of
  skipping documents.
- **Fused-CE token tile** `--loss.b_block_size=...` must divide the per-rank token count.
- Toggles: `--compile.no-enable` (eager; shows attention fallbacks), `--hf_config_overrides='{...}'`,
  trailing `activation-checkpoint:full|selective|none`.

## Why it matters / when it applies
- Fastest way to get a new HF architecture training on TPU and to locate perf gaps; tested on 500+
  popular text-generation checkpoints (Llama, Qwen, Mistral/Mixtral, Gemma, Phi, OLMo/OLMoE, Granite,
  DeepSeek, Falcon-H1, LFM2, Mamba, ...); full size up to 10B on v6e-8, 10-35B on v6e-32.
- Limits: no expert parallelism; MoE models are bound by expert-weight communication; some
  architectures fall back to slower paths - check loss parity before trusting a new one.
- README claims the TPU token dispatcher's whole-row-gathering backward is 3.6x to 65x faster than the
  standard dispatcher at equal batch (DeepSeek-V2-Lite, Qwen3-30B-A3B, OLMoE).
- Measured tile choices in code: splash 1024 best on packed 2048-token sequences (512 worse, 2048 does
  not compile); fused CE b=2048 best (see [tpu-fused-linear-cross-entropy](tpu-fused-linear-cross-entropy.md)).

**Doc vs code:** the README says `hf_moe_auto` gets the same out-of-the-box set as `hf_full_max`
"with no flags needed", including the fused Pallas CE and attention-saving selective AC. At this
commit `hf_moe_auto` calls `_tpu_hf_config(..., attn="splash_tpu", compile=True,
use_pallas_grouped_mm=True)` without `fused_loss=True` or `save_attention=True`, so MoE runs use
**plain CE** and the default `SelectiveAC`. Also, the README's "`hf_full_*`" family has only two
members (`hf_full_max`, `hf_full_max_plain_ce`), and its example `--loss.b_block_size=256` is a
small-batch override (the config default is 2048).

## Connections
- Code concepts: [tpu-trainer-and-job-config](../concepts/tpu-trainer-and-job-config.md),
  [tpu-moe-dispatch-and-grouped-experts](../concepts/tpu-moe-dispatch-and-grouped-experts.md),
  [tpu-pallas-kernels](../concepts/tpu-pallas-kernels.md),
  [data-loading](../concepts/data-loading.md),
  [parallel-dims-and-parallelization](../concepts/parallel-dims-and-parallelization.md)
- Module catalogs: [transformers_modeling_backend/config_registry](../catalog/torchtitan/experiments/tpu/transformers_modeling_backend/config_registry.md),
  [transformers_modeling_backend/job_config](../catalog/torchtitan/experiments/tpu/transformers_modeling_backend/job_config.md),
  [transformers_modeling_backend/model](../catalog/torchtitan/experiments/tpu/transformers_modeling_backend/model.md),
  [transformers_modeling_backend/attention](../catalog/torchtitan/experiments/tpu/transformers_modeling_backend/attention.md),
  [activation_checkpoint (tpu)](../catalog/torchtitan/experiments/tpu/activation_checkpoint.md)
- Related doc-concepts: [tpu-splash-attention-tiles-and-vmem](tpu-splash-attention-tiles-and-vmem.md),
  [tpu-fused-linear-cross-entropy](tpu-fused-linear-cross-entropy.md),
  [tpu-moe-kernel-switches](tpu-moe-kernel-switches.md),
  [tpu-simplefsdp-and-mixed-precision](tpu-simplefsdp-and-mixed-precision.md),
  [tpu-launch-and-profiling-workflow](tpu-launch-and-profiling-workflow.md)

## Source
Extracted from `torchtitan/experiments/tpu/transformers_modeling_backend/README.md` (kept in place),
cross-checked against `transformers_modeling_backend/config_registry.py`.
