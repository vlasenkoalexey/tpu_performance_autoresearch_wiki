---
title: Recipe precision variants and throughput accounting (token budgets, per-core MFU, FLOP conventions, float8)
type: doc-concept
provenance: doc
source: torchtitan/experiments/tpu/recipes/
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T06:34:20Z}
---
# Recipe precision variants and throughput accounting (token budgets, per-core MFU, FLOP conventions, float8)

## Definition
The TPU recipe READMEs share a set of conventions that must be understood before comparing their numbers:
batch is a **token budget** per data-parallel rank, not a sequence count; on TPU7x every metric is **per device =
per TensorCore** (two per chip); MFU depends on which **FLOP count** the run uses (torchtitan vs MaxText); and
precision comes in a canonical form (float32 master weights, bf16 compute, FP32 gradient reductions) plus
deliberately different variants - pure bf16, float8 linears, and "MaxText parity" (BF16 reductions + BF16 RoPE) -
whose results the READMEs say to keep separate.

## In torchtitan (grounded)
- Token budgets: [`TrainingConfig.num_tokens_per_microbatch_per_dp_rank`](../catalog/torchtitan/config/configs.md#TrainingConfig.num_tokens_per_microbatch_per_dp_rank),
  [`max_context_length`](../catalog/torchtitan/config/configs.md#TrainingConfig.max_context_length) and the global
  [`num_tokens_per_train_step`](../catalog/torchtitan/config/configs.md#TrainingConfig.num_tokens_per_train_step)
  (e.g. [`qwen3_32b`](../catalog/torchtitan/experiments/tpu/qwen3/config_registry.md#qwen3_32b) sets 8 x 4096 per rank and 1024 x 4096 per step).
  For FLUX, [`FluxConfig.img_size`](../catalog/torchtitan/experiments/tpu/tpu_job_config.md#FluxConfig.img_size) is applied by
  [`_apply_flux_img_size`](../catalog/torchtitan/experiments/tpu/train.md#_apply_flux_img_size), which also derives `max_context_length`.
- Peak FLOPs: [`get_peak_flops`](../catalog/torchtitan/tools/utils.md#get_peak_flops) returns 2307e12 / 2 for TPU7x (per TensorCore) and 918e12 for v6e.
- MaxText FLOP accounting: [`_use_maxtext_flops`](../catalog/torchtitan/experiments/tpu/qwen3/config_registry.md#_use_maxtext_flops)
  (called only by `*maxtext*` recipes), carried onto GraphTrainer by
  [`maybe_use_maxtext_flops`](../catalog/torchtitan/experiments/tpu/graph_trainer/config.md#maybe_use_maxtext_flops), counted by
  [`get_maxtext_decoder_nparams_and_flops`](../catalog/torchtitan/experiments/tpu/mfu_flops.md#get_maxtext_decoder_nparams_and_flops).
- Benchmark windows: [`TPUConfig.enable_mfu_benchmark`](../catalog/torchtitan/experiments/tpu/tpu_job_config.md#TPUConfig.enable_mfu_benchmark) /
  [`mfu_benchmark_start_step`](../catalog/torchtitan/experiments/tpu/tpu_job_config.md#TPUConfig.mfu_benchmark_start_step)
  (the Qwen3-30B-A3B benchmark config sets start step 10 over 30 steps).
- Precision: [`TrainingConfig.dtype`](../catalog/torchtitan/config/configs.md#TrainingConfig.dtype) (default float32),
  [`mixed_precision_param`](../catalog/torchtitan/config/configs.md#TrainingConfig.mixed_precision_param) (default bfloat16),
  [`mixed_precision_reduce`](../catalog/torchtitan/config/configs.md#TrainingConfig.mixed_precision_reduce) (default float32).
  Parity variants: [`qwen3_8b_maxtext_parity`](../catalog/torchtitan/experiments/tpu/qwen3/config_registry.md#qwen3_8b_maxtext_parity),
  [`qwen3_32b_maxtext_parity`](../catalog/torchtitan/experiments/tpu/qwen3/config_registry.md#qwen3_32b_maxtext_parity)
  (BF16 reduce + the `_BF16_ROPE_OVERRIDE` import + MaxText FLOPs).
- Float8: [`llama3_70b_float8`](../catalog/torchtitan/experiments/tpu/llama3/config_registry.md#llama3_70b_float8) ->
  [`_with_float8`](../catalog/torchtitan/experiments/tpu/llama3/config_registry.md#_with_float8) ->
  [`TpuFloat8LinearConverter`](../catalog/torchtitan/experiments/tpu/float8_converter.md#TpuFloat8LinearConverter)
  (rowwise recipe, `filter_fqns=["lm_head", "output"]`).

### Accounting conventions

| Topic | Convention in the READMEs |
|---|---|
| Batch | `num_tokens_per_microbatch_per_dp_rank = sequences x context`, e.g. 6 x 2048 = 12288 (Qwen3-8B), 4 x 8192 = 32768 (Llama3); upstream d771abb0 removed `--training.local_batch_size` / `seq_len` |
| FLUX batch | `--flux.img_size=1024` sets image size and `max_context_length` = 64 x 64 image patches + 512 T5 tokens = 4608; budget = images x 4608 (`--dataloader.img_size` no longer exists; `flux_dev` defaults to 256 px). "Step time / PDB" = step time / images per device |
| Devices | TPU7x: one process per TensorCore, so `tpu7x-128` = 128 devices on 64 chips (16 hosts x 8). v6e: one device per chip (4 per host) |
| Peak for MFU | TPU7x: 1,153.5 TFLOP/s per device (half the 2,307 TFLOP/s chip peak); v6e: per-chip peak (918 TFLOP/s in code) |
| FLOP count | Default torchtitan count; `*maxtext*` recipes use MaxText's, which halves attention FLOPs for the causal mask. Qwen3-30B-A3B: torchtitan's count is 11.7% higher at seq 2048 (18.02% vs 20.12% MFU for the same run). Step time, TPS and memory do not depend on it |
| Float8 MFU | Logged as `mfu: N/A` (no single peak for mixed float8/bf16 matmuls); compare step time and TFLOP/s/device |
| Window | "mean of steps 10-30" (Muse Glimmer, Qwen3-32B, Qwen3-30B-A3B), "around step 30" (Qwen3-8B tpu7x), steps 2-30 / 2-15 (Qwen3-8B v6e), "steady state" (Llama3) |
| Data | Default `c4_test` + test tokenizer; Qwen3-32B: streamed C4 gave ~11.95 s vs ~12.52 s on c4_test, so compare only runs with the same data and tokenizer |

### Precision variants and what they bought

| Variant | Where | Result |
|---|---|---|
| fp32 master + bf16 compute, FP32 reductions (canonical) | Llama3, Qwen3, Muse Glimmer, FLUX "float32 + MixedPrecision bfloat16" | baseline rows of [tpu-recipe-matrix](tpu-recipe-matrix.md) |
| Pure bf16 (`--training.dtype=bfloat16`) | FLUX tpu7x / v6e | fits more images per device (5 vs 3 on tpu7x, 3 vs 2 on v6e); per-image step time 0.86 -> 0.81 s (tpu7x), 1.41 -> 1.20 s (v6e-8), 1.44 -> 1.35 s (v6e-256); MFU 20.47% -> 21.64% (tpu7x) |
| torchao rowwise float8 linears, lm_head in bf16 | Llama3-70B tpu7x-128 | step 13.27 -> 10.02 s (~24.5% lower), 1,235 -> 1,636 TPS/device, 594 -> 787 TFLOP/s/device; peak memory 7.37 -> 8.67 GiB |
| MaxText parity: BF16 FSDP reductions + BF16 RoPE + MaxText FLOPs | `qwen3_32b_maxtext_parity`, `qwen3_8b_maxtext_parity` | Qwen3-32B: ~11.83 s, ~49.2% MFU, 35.10 GiB vs canonical ~11.95 s, ~48.7%, 36.46 GiB (streamed C4, 9/25/2026) |

Float8 notes from the README: `use_fast_accum` is a no-op on TPU because TPU matmuls accumulate in float32
(the converter's code comment says the same), and the float8 config needs torchao in the image (the TPU
Dockerfile installs it).

## Why it matters / when it applies
- Per-core vs per-chip: a TPU7x "TPS/device" is half a chip; multiply by two before comparing with a v6e TPS/chip.
- The MaxText-parity rows change reduction precision and RoPE arithmetic; the READMEs explicitly say to keep them
  separate from canonical FP32-reduction results. They are not numerics-preserving optimizations, and the
  all-reduce+slice rewrite at 512 devices requires FP32 reductions, so no parity variant exists there.
- MFU across READMEs is only comparable when FLOP convention, device definition and data match; step time and
  TPS are the convention-free metrics.

### Doc vs code at this commit
- The Qwen3-30B-A3B README's headline MFU / TFLOPS (18.02%, 207.82) were logged with MaxText FLOPs. Its config
  [`qwen3_moe_30b_fsdp_only_full_ac_benchmark`](../catalog/torchtitan/experiments/tpu/qwen3/config_registry.md#qwen3_moe_30b_fsdp_only_full_ac_benchmark)
  does not call `_use_maxtext_flops`, so a run at this commit logs the torchtitan count (~20.12% / 232.12 TFLOPS);
  the README says as much, citing the commit that made torchtitan's count the default for non-`*maxtext*` recipes.
  MaxText-comparable MFU comes from [`qwen3_moe_30b_fsdp_only_maxtext_benchmark`](../catalog/torchtitan/experiments/tpu/qwen3/config_registry.md#qwen3_moe_30b_fsdp_only_maxtext_benchmark),
  which also switches to BF16 reductions and BF16 RoPE.
- The Mamba-3 README commands still pass `--training.local_batch_size` and `--training.seq_len`;
  [`TrainingConfig`](../catalog/torchtitan/config/configs.md#TrainingConfig) at this commit has neither (token budgets only), so those
  commands need `--training.num_tokens_per_microbatch_per_dp_rank` / `--training.max_context_length` as in the Mamba-2 README.

## Connections
- Code concepts: [quantization](../concepts/quantization.md), [observability](../concepts/observability.md),
  [job-config](../concepts/job-config.md), [data-loading](../concepts/data-loading.md),
  [tpu-trainer-and-job-config](../concepts/tpu-trainer-and-job-config.md), [config-overrides](../concepts/config-overrides.md),
  [flux-diffusion-model](../concepts/flux-diffusion-model.md), [llama3-model](../concepts/llama3-model.md)
- Module catalogs: [config/configs](../catalog/torchtitan/config/configs.md),
  [float8_converter](../catalog/torchtitan/experiments/tpu/float8_converter.md),
  [mfu_flops](../catalog/torchtitan/experiments/tpu/mfu_flops.md), [tools/utils](../catalog/torchtitan/tools/utils.md),
  [qwen3/config_registry](../catalog/torchtitan/experiments/tpu/qwen3/config_registry.md),
  [llama3/config_registry](../catalog/torchtitan/experiments/tpu/llama3/config_registry.md),
  [train](../catalog/torchtitan/experiments/tpu/train.md)
- Related doc-concepts: [tpu-recipe-matrix](tpu-recipe-matrix.md),
  [tpu-recipe-simplefsdp-schedules](tpu-recipe-simplefsdp-schedules.md),
  [tpu-recipe-mamba-256k-long-context](tpu-recipe-mamba-256k-long-context.md),
  [float8-training](float8-training.md),
  [tpu-simplefsdp-and-mixed-precision](tpu-simplefsdp-and-mixed-precision.md)

## Source
Extracted from (kept in place):
- `torchtitan/experiments/tpu/recipes/ironwood/llama3-70b/tpu7x-128/README.md`
- `torchtitan/experiments/tpu/recipes/ironwood/llama3-70b/tpu7x-2x2x4/README.md`
- `torchtitan/experiments/tpu/recipes/ironwood/qwen3-30b-a3b/tpu7x-4x4x4/README.md`
- `torchtitan/experiments/tpu/recipes/ironwood/qwen3-32b/tpu7x-4x4x4/README.md`
- `torchtitan/experiments/tpu/recipes/ironwood/qwen3-8b/tpu7x-4x4x4/README.md`
- `torchtitan/experiments/tpu/recipes/ironwood/flux1/tpu7x-4x4x4/README.md`
- `torchtitan/experiments/tpu/recipes/trillium/flux1/v6e-8/README.md`
- `torchtitan/experiments/tpu/recipes/trillium/flux1/v6e-256/README.md`
- `torchtitan/experiments/tpu/recipes/trillium/qwen3-8b/v6e-8/README.md`
- `torchtitan/experiments/tpu/examples/mamba3/recipes/ironwood/mamba3-2.7b-256k/2x2x1/README.md`

Cross-checked against `torchtitan/config/configs.py`, `torchtitan/tools/utils.py`,
`torchtitan/experiments/tpu/float8_converter.py` and the config registries at commit 2ad96c939.
