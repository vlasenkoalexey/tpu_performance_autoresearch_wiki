---
title: Token padding buckets (compile_sizes) and bucket knobs
type: doc-concept
provenance: doc
source: docs/reference/env_vars.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-11-03T02:35:38Z}
---
# Token padding buckets (compile_sizes) and bucket knobs

## Definition
TPU programs are static-shape, so vllm-torchtpu pads every engine step's token count up
to one of a fixed set of **token buckets** and compiles one executable per bucket during
warmup. The docs expose this set through `--compilation-config '{"compile_sizes": [...]}'`
(supported-models page, "Compilation & warmup cache") and two env vars from the
reference: `TPU_TOKEN_BUCKET_EXTRA` (extra sizes) and `TPU_TOKEN_BUCKET_LINEAR`.

## In vllm-torchtpu (grounded)
- [`TpuPlatform.check_and_update_config`](../catalog/src/vllm_torchtpu/platforms/tpu_platform.md#TpuPlatform.check_and_update_config)
  fills `compile_sizes` when the user did not: [`_get_token_paddings`](../catalog/src/vllm_torchtpu/platforms/tpu_platform.md#_get_token_paddings)
  starts from [`_get_exponential_token_paddings`](../catalog/src/vllm_torchtpu/platforms/tpu_platform.md#_get_exponential_token_paddings)
  (16, 32, 64, ... doubling, with the last bucket capped at exactly
  `--max-num-batched-tokens`, e.g. `[..., 4096, 5000]` rather than 8192) and merges any
  [`TPU_TOKEN_BUCKET_EXTRA`](../catalog/src/vllm_torchtpu/envs.md#TPU_TOKEN_BUCKET_EXTRA)
  sizes that are `<= budget`.
- [`TPU_TOKEN_BUCKET_LINEAR`](../catalog/src/vllm_torchtpu/envs.md#TPU_TOKEN_BUCKET_LINEAR)
  adds [`_get_linear_token_paddings`](../catalog/src/vllm_torchtpu/platforms/tpu_platform.md#_get_linear_token_paddings):
  evenly spaced buckets above budget/4 up to `max_model_len + max_num_seqs` (capped
  count), because padding a prompt-sized pass to the next power of two can waste up to
  half of it. **Doc-vs-code:** the env reference says linear buckets replace the
  exponential ones; the code merges them into the exponential set.
- User-supplied `compile_sizes` must be integers (vLLM's `cudagraph_capture_sizes`
  placeholder strings are rejected) and are sorted.
- `TPU_MOE_SEQUENCE_PARALLEL` may drop sizes that do not split evenly over TP
  ([`_configure_sequence_parallel_moe`](../catalog/src/vllm_torchtpu/platforms/tpu_platform.md#_configure_sequence_parallel_moe)),
  after which [`_validate_token_budget_fits_compile_sizes`](../catalog/src/vllm_torchtpu/platforms/tpu_platform.md#_validate_token_budget_fits_compile_sizes)
  fails startup if the per-step token budget exceeds the largest bucket (under PCP,
  measured on rank 0's share).
- vLLM's `compile_ranges_split_points` are cleared: TPU always pads to an exact
  compile size, so catch-all ranges are never used.
- The FP8 small-bucket knob [`TPU_FP8_LINEAR_W8A16_MAX_ROWS`](../catalog/src/vllm_torchtpu/envs.md#TPU_FP8_LINEAR_W8A16_MAX_ROWS)
  is expressed in these padded bucket rows (see [load-time-requantization](load-time-requantization.md)).

## Why it matters / when it applies
- Bucket count trades warmup time and resident program HBM against padding waste:
  every bucket is a compiled program kept on device.
- `--max-num-batched-tokens` sets the largest bucket and is part of the compile cache
  key; changing it recompiles everything.
- Long-prompt prefill-heavy workloads benefit from linear buckets (less padding on big
  chunks); decode-heavy workloads mostly hit the small exponential buckets.
- A shape outside the set triggers a runtime compile; detect it with
  `VLLM_XLA_CHECK_RECOMPILATION=1` (see [compilation-cache-and-warmup](compilation-cache-and-warmup.md)).

## Connections
- Code concepts: [tpu-platform](../concepts/tpu-platform.md), [compilation-and-graph-capture](../concepts/compilation-and-graph-capture.md), [tpu-model-runner](../concepts/tpu-model-runner.md)
- Module catalogs: [tpu_platform](../catalog/src/vllm_torchtpu/platforms/tpu_platform.md), [envs](../catalog/src/vllm_torchtpu/envs.md)
- Related doc-concepts: [compilation-cache-and-warmup](compilation-cache-and-warmup.md), [env-var-reference-by-subsystem](env-var-reference-by-subsystem.md), [dp-ep-moe-layouts](dp-ep-moe-layouts.md)

## Source
Extracted from `docs/reference/env_vars.md` (section 2, bucket knobs) and the
"Compilation & warmup cache" / "Chunked prefill" rows of
`docs/user_guide/supported_models.md` (kept in place).
