---
title: TPU v7x serving recipe matrix (CI-validated configs)
type: doc-concept
provenance: doc
source: docs/deployment/v7x_recipes.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-11-03T02:35:38Z}
---
# TPU v7x serving recipe matrix (CI-validated configs)

## Definition
The v7x recipe doc is a set of `vllm serve` configurations "extracted directly from the
repository's active PR and nightly CI performance benchmark configurations" in
`scripts/vllm/benchmarking/configs/`. Each recipe is therefore a (model x slice) point that
CI benchmarks and regression-gates, not a hand-tuned suggestion. The doc's framing of the
hardware: one v7x chip exposes 2 logical TensorCore devices (96 GB HBM each), so a 4-chip
`tpu7x-8` host is 8 devices / 768 GB, `v7x-16` is 2 hosts and `v7x-32` is 4 hosts.

This page condenses the doc into a matrix, adds the measured CI baseline numbers that sit
next to each config in `scripts/vllm/benchmarking/baselines/perf/` (the doc itself states no
throughput), and records where the doc's commands differ from the configs at this commit.

## Recipe matrix

Parallelism, flags and env vars below are taken from the CI config script (the source of
truth), cross-checked with the doc. "Dev" = logical devices.

| Model | Slice (dev) | Layout | Weights / KV | Batch knobs (max-len / MBT / max-seqs / gmu) | Other key flags | Env vars |
|---|---|---|---|---|---|---|
| Qwen3.5-397B-A17B-FP8 | v7x-8 (8) | TP1 DP8 + EP | fp8 / fp8 | 10240 / 1024 / 64 / 0.92 | block 256, `--language-model-only`, mm limit 0 | `USE_MOE_SPARSE_CORE=1`, `ONEHOT_MOE_PERMUTE_THRESHOLD=32768` |
| Qwen3.5-397B-A17B-FP8 (alt) | v7x-8 (8) | TP2 DP4 + EP | fp8 / fp8 | 10240 / 2048 / 128 / 0.92 | same | same |
| Qwen3.5-397B-A17B-FP8 (alt) | v7x-8 (8) | TP8 DP1 + EP | fp8 / fp8 | 10240 / 8192 / 512 / 0.92 | same | same |
| Qwen3-Coder-480B-A35B-FP8 | v7x-8 (8) | TP8 + EP | fp8 / fp8 | 10240 / 8192 / 128 / 0.95 | - | - |
| Qwen3-Coder-30B-A3B-FP8 | v7x-8 (8) | TP8 + EP | fp8 / fp8 | 16384 / 8192 / 128 / 0.95 (harness defaults except max-seqs) | - | `LIBTPU_INIT_ARGS=--xla_tpu_alternate_memory_benefit_scaling_factor_for_large_buffers=0` |
| Qwen3.5-35B-A3B-FP8 | v7x-8 (8) | TP8 + EP | fp8 / fp8 | 16384 / 8192 / 128 / 0.9 | block 256, mm limit 0 | `USE_MOE_SPARSE_CORE=1` |
| gemma-4-31B-it-FP8-Dynamic | v7x-8 (8) | TP2 DP4 | compressed-tensors FP8 (from checkpoint) / fp8 | 16384 / 8192 / 128 / 0.90 | block 256, `mm-encoder-tp-mode: data` (via `--additional_config`, see below), `cudagraph_mm_encoder: true` (8 vision items / 8 frames per batch), `--disable-chunked-mm-input` | `VLLM_ENGINE_READY_TIMEOUT_S=1800` |
| GLM-5.2-FP8 | v7x-16 (16) | TP1 DP16 + EP | fp8 (from checkpoint) / fp8 | 9216 / 1024 / 64 / 0.90 | `--enable-ep-weight-filter`, `--safetensors-load-strategy prefetch`, gs:// streaming | - |
| DeepSeek-V4-Pro-0813 | v7x-16 (16) | TP1 DP16 (8 local) + EP | `deepseek_v4_fp8` (W4A8 MoE) / `fp8_e4m3` | 9216 / 1024 / 256 / 0.90 | `--enable-ep-weight-filter`, prefetch, loader `memory_limit` 4 GiB x concurrency 8 | fused-EP MoE stack (see below) + collective-offload `LIBTPU_INIT_ARGS` |
| Kimi-K3 | v7x-32 (32) | TP32 + EP | compressed-tensors FP8 (from checkpoint) / fp8 | 10240 / 8192 / 8 / 0.82 | block 256, `compile_sizes [1,8,8192]`, loader `memory_limit` 16 GiB, `--language-model-only` | - |

Every CI config is launched by `run_benchmarks.sh`, which adds flags the doc's commands only
partly show: `--attention-backend CUSTOM` (default for every config), `--async-scheduling`,
`--no-enable-prefix-caching`, `--kv-cache-dtype fp8` (default), `--api-server-count=1`
whenever DP > 1, and `--load-format runai_streamer --served-model-name ...` whenever the
config sets a `MODEL_URI` (GLM-5.2, DeepSeek-V4-Pro, Kimi-K3 stream from `gs://`).

## Measured CI baselines (not in the doc)

From `scripts/vllm/benchmarking/baselines/perf/<config>.baseline.json`. Workload is random
ISL/OSL at the stated concurrency (Qwen configs use range ratio 0.8; GLM/DSv4/Kimi use fixed
lengths). out = output tok/s, total = input+output tok/s, TPOT = median ms per output token.

| Config | ISL/OSL @ conc | out tok/s | total tok/s | TPOT ms | Note |
|---|---|---|---|---|---|
| 397B TP1 DP8 | 1k/8k @ 64 | 2418 | 2719 | 25.3 | |
| 397B TP1 DP8 | 1k/8k @ 512 | 8112 | 9123 | 47.1 | best high-concurrency decode |
| 397B TP1 DP8 | 8k/1k @ 512 | 3272 | 29351 | 111.2 | best high-concurrency prefill-heavy |
| 397B TP2 DP4 | 1k/8k @ 64 | 2643 | 2972 | 23.3 | |
| 397B TP2 DP4 | 1k/8k @ 512 | 8147 | 9162 | 48.0 | |
| 397B TP2 DP4 | 8k/1k @ 64 | 1042 | 9349 | 61.8 | |
| 397B TP8 DP1 | 1k/8k @ 64 | 3039 | 3417 | 22.1 | best low-concurrency latency |
| 397B TP8 DP1 | 1k/8k @ 512 | 5998 | 6746 | 61.8 | falls behind DP at high conc |
| 397B TP8 DP1 | 8k/1k @ 64 | 1724 | 15461 | 39.0 | |
| Coder-480B TP8 | 1k/1k @ 64 | 2111 | 4220 | 28.6 | |
| Coder-480B TP8 | 8k/1k @ 64 | 1134 | 10194 | 53.4 | |
| Coder-30B TP8 | 1k/1k @ 64 | 5957 | 11891 | 9.4 | median TTFT 63 ms |
| gemma-4-31B TP2 DP4 | 1k/1k @ 128 | 6477 | 12930 | 15.0 | multimodal config, text load |
| GLM-5.2 DP16 | 8k/1k @ 1024 | 2537 | 22837 | 277.0 | |
| DeepSeek-V4-Pro DP16 | 8k/1k @ 1024 | 4301 | 38709 | 215.5 | |
| Kimi-K3 TP32 | 8k/1k @ 1 | 48 | 434 | 19.2 | median TTFT 1573 ms; lowered on purpose (see below) |

Read-outs for the optimization loop:
- **TP vs DP on one host (397B).** TP8 wins at concurrency 64 (TPOT 22.1 vs 25.3 ms, and
  8k/1k total 15.5k vs 7.4k tok/s); DP8 wins at 512 (8.1k vs 6.0k out tok/s on 1k/8k). This is
  the doc's "use TP2/TP8 for lower per-request latency at smaller concurrencies" tip, quantified.
- **Kimi-K3 baseline is deliberately regressed.** The baseline's `_source` note says Kimi-K3
  now runs on the unified KV pool by default and the pooled KDA path is slower until optimized
  (TTFT 995 -> 1573 ms, 452 -> 434 tok/s); `TPU_VLLM_ENABLE_UNIFIED_BLOCK_POOL=0` restores the
  old numbers but excludes prefix caching. That is open headroom, not a ceiling.
- **Regression gate.** `check_regression.py` gates median TTFT (only when the baseline
  carries it), median TPOT, total and output throughput at `PERF_TOLERANCE` (default 0.05;
  0.08 for the 397B TP2 DP4 config), plus a 0.95 completed-requests floor.

## In vllm-torchtpu (grounded)
What the recurring recipe knobs do in the plugin:

- `--attention-backend CUSTOM` selects
  [`PallasBatchedRPAAttentionBackend`](../catalog/src/vllm_torchtpu/layers/adapter/attention.md#PallasBatchedRPAAttentionBackend)
  (a subclass of [`PallasAttentionBackend`](../catalog/src/vllm_torchtpu/layers/adapter/attention.md#PallasAttentionBackend)),
  which routes attention to the batched ragged-paged-attention kernel and keeps the
  auto-selected page size at 256. The harness comment says that without it vLLM falls back to
  FLASH_ATTN with block size 16 and benchmarks regress ~12%. Under `VLLM_KV_CACHE_LAYOUT=HND`
  the non-PCP kernel accepts only page size 128. For MLA models,
  [`TpuPlatform.get_attn_backend_cls`](../catalog/src/vllm_torchtpu/platforms/tpu_platform.md#TpuPlatform.get_attn_backend_cls)
  substitutes `FLASH_ATTN_MLA` whatever was requested, so the harness-default CUSTOM is
  effectively a no-op on MLA checkpoints.
- `--block-size 256` is the KV page size the batched kernel prefers (any multiple of 128 is
  legal for it).
- `--gpu-memory-utilization` feeds
  [`TPUWorker.determine_available_memory`](../catalog/src/vllm_torchtpu/worker/tpu_worker.md#TPUWorker.determine_available_memory):
  a profile run, then [`compute_hbm_budget`](../catalog/src/vllm_torchtpu/utils.md#compute_hbm_budget),
  minus [`post_profile_hbm_reserves`](../catalog/src/vllm_torchtpu/runner/tpu_runner.md#TPUModelRunner.post_profile_hbm_reserves)
  (KV-connector, LoRA slot-write, PP hand-off buffers), reduced to the minimum across EP/DP
  ranks by [`min_across_ep_dp`](../catalog/src/vllm_torchtpu/utils.md#min_across_ep_dp).
  Kimi-K3's low 0.82 and DSv4's loader `memory_limit` leave room for exactly these.
- `USE_MOE_SPARSE_CORE` ([env](../catalog/src/vllm_torchtpu/envs.md#USE_MOE_SPARSE_CORE))
  picks the SparseCore variant of the fused-MoE custom op in
  [`_build_fused_moe_custom_op`](../catalog/src/vllm_torchtpu/layers/adapter/fused_moe.md#_build_fused_moe_custom_op).
  It already defaults to 1 in code, so the recipes' `export USE_MOE_SPARSE_CORE=1` is a no-op
  kept for explicitness.
- `ONEHOT_MOE_PERMUTE_THRESHOLD` ([env](../catalog/src/vllm_torchtpu/envs.md#ONEHOT_MOE_PERMUTE_THRESHOLD)),
  resolved by [`resolve_onehot_permute_threshold`](../catalog/src/vllm_torchtpu/layers/core/fused_moe_gmm.md#resolve_onehot_permute_threshold):
  routed-row count (tokens x top-k) at or below which MoE permute/combine run as TensorCore
  one-hot matmuls instead of SparseCore gather/reduce. Auto (unset) is derived from SparseCore
  geometry; the 397B recipes force 32768. For the DP8 and TP2-DP4 configs (1024-2048 batched
  tokens per engine) that keeps every step with top-k <= 16 on the one-hot path; the TP8 config
  (8192 batched tokens) crosses back to SparseCore on large prefill steps.
- `--enable-ep-weight-filter` + gs:// streaming: [`patch_runai_sharded_expert_streaming`](../catalog/src/vllm_torchtpu/model_loader_patches.md#patch_runai_sharded_expert_streaming)
  makes the runai streamer fetch only this rank's experts (via
  [`_compute_local_expert_ids`](../catalog/src/vllm_torchtpu/model_loader_patches.md#_compute_local_expert_ids));
  it is inert unless both `--enable-expert-parallel` and the filter are on, and disabled under
  EPLB. [`patch_default_loader_ep_weight_filter`](../catalog/src/vllm_torchtpu/model_loader_patches.md#patch_default_loader_ep_weight_filter)
  widens the same filter to MXFP4 tensor names for the non-streaming loader.
- DeepSeek-V4-Pro's env stack: [`USE_MOE_FUSED_EP_KERNEL`](../catalog/src/vllm_torchtpu/envs.md#USE_MOE_FUSED_EP_KERNEL)
  + [`MOE_FUSED_EP_ENABLE_W4A8`](../catalog/src/vllm_torchtpu/envs.md#MOE_FUSED_EP_ENABLE_W4A8)
  (fused expert-parallel MoE with W4A8), [`MOE_REQUANTIZE_WEIGHT_DTYPE`](../catalog/src/vllm_torchtpu/envs.md#MOE_REQUANTIZE_WEIGHT_DTYPE)`=fp4`
  with block 512, [`TPU_MOE_SKIP_PADDED_TOKENS`](../catalog/src/vllm_torchtpu/envs.md#TPU_MOE_SKIP_PADDED_TOKENS)
  (padded tokens no longer route to experts), [`RAGGED_GATHER_REDUCE_VERSION`](../catalog/src/vllm_torchtpu/envs.md#RAGGED_GATHER_REDUCE_VERSION)`=v3`
  (destination-major SparseCore combine prototype; default v2), row-major RoPE cache and MoE
  hash table, plus XLA flags enabling SparseCore all-gather offload and async all-gather.
- Kimi-K3's unified KV pool default comes from
  [`unified_kv_layout_enabled`](../catalog/src/vllm_torchtpu/platforms/tpu_block_size_utils.md#unified_kv_layout_enabled),
  overridable by [`TPU_VLLM_ENABLE_UNIFIED_BLOCK_POOL`](../catalog/src/vllm_torchtpu/envs.md#TPU_VLLM_ENABLE_UNIFIED_BLOCK_POOL).

Owning modules: `layers/adapter/attention.py`, `layers/adapter/fused_moe.py`,
`layers/core/fused_moe_gmm.py`, `model_loader_patches.py`, `worker/tpu_worker.py`, `envs.py`.

## Doc vs code at this commit
- **Qwen3-Coder-480B**: the doc's command uses `--max-model-len 16384 --max-num-seqs 512`; the
  CI config it cites uses 10240 and 128.
- **Qwen3-Coder-30B**: the doc shows `--max-num-seqs 512`; the config sets 128 and also exports
  a `LIBTPU_INIT_ARGS` XLA flag the doc omits (the other doc values match harness defaults).
- **GLM-5.2 / Kimi-K3 commands** omit the `--attention-backend CUSTOM`,
  `--no-enable-prefix-caching`, `--api-server-count=1` (DP16) and runai-streamer flags the
  harness actually passes. The harness explains `--api-server-count=1`: with one frontend per
  DP rank the frontends race to resolve the model into the loader cache and the loser dies.
- **DeepSeek-V4-Pro and gemma-4-31B** appear in the doc's summary table but have no command; the
  configs carry a large env/flag stack (above). DSv4's config also exports `NEW_MODEL_DESIGN`
  and `MODEL_IMPL_TYPE`, which no module under `src/vllm_torchtpu` reads at this commit.
- **gemma-4-31B** passes `mm-encoder-tp-mode` inside `--additional_config`, which no module under
  `src/vllm_torchtpu` reads; the gemma-4-26B config uses the real `--mm-encoder-tp-mode data` flag
  (see [multimodal-encoder-inference](multimodal-encoder-inference.md)).
- **Qwen3.5-35B-A3B TP8** has no perf baseline file (baselines exist for its TP4, DP8 and
  DP4-TP2 variants), so it is benchmarked but not throughput-gated.

## Why it matters / when it applies
These are the only configs whose throughput is continuously measured, so they are the right
starting frontier for a serving-perf experiment on v7x: copy the config, not the doc command,
and diff against the baseline JSON. The TP-vs-DP crossover and the Kimi-K3 unified-pool
regression are the two explicit tuning signals in the data.

## Connections
- Code concepts: [batched-ragged-paged-attention-kernel](../concepts/batched-ragged-paged-attention-kernel.md),
  [ragged-paged-attention-kernel](../concepts/ragged-paged-attention-kernel.md),
  [kv-cache-layout-and-hbm-budget](../concepts/kv-cache-layout-and-hbm-budget.md),
  [fused-moe-kernels](../concepts/fused-moe-kernels.md),
  [adaptive-fused-moe-kernel](../concepts/adaptive-fused-moe-kernel.md),
  [sparsecore-ragged-gather-scatter](../concepts/sparsecore-ragged-gather-scatter.md),
  [quantization-methods](../concepts/quantization-methods.md),
  [distributed-parallelism-and-meshes](../concepts/distributed-parallelism-and-meshes.md),
  [compilation-and-graph-capture](../concepts/compilation-and-graph-capture.md),
  [tpu-schedulers](../concepts/tpu-schedulers.md),
  [deepseek-v4-model](../concepts/deepseek-v4-model.md),
  [kimi-k3-model](../concepts/kimi-k3-model.md),
  [tpu-platform](../concepts/tpu-platform.md).
- Module catalogs: [layers/adapter/attention](../catalog/src/vllm_torchtpu/layers/adapter/attention.md),
  [layers/adapter/fused_moe](../catalog/src/vllm_torchtpu/layers/adapter/fused_moe.md),
  [layers/core/fused_moe_gmm](../catalog/src/vllm_torchtpu/layers/core/fused_moe_gmm.md),
  [model_loader_patches](../catalog/src/vllm_torchtpu/model_loader_patches.md),
  [worker/tpu_worker](../catalog/src/vllm_torchtpu/worker/tpu_worker.md),
  [envs](../catalog/src/vllm_torchtpu/envs.md).
- Related doc-concepts: [benchmark-harness-and-regression-gates](benchmark-harness-and-regression-gates.md)
  (how the configs are run and gated), [dp-ep-moe-layouts](dp-ep-moe-layouts.md) (why DP attention +
  EP MoE), [v6e-serving-recipe-matrix](v6e-serving-recipe-matrix.md),
  [tpu-generations-and-logical-devices](tpu-generations-and-logical-devices.md),
  [gke-multihost-jobset-deployment](gke-multihost-jobset-deployment.md),
  [profile-cache-and-free-hbm-probe](profile-cache-and-free-hbm-probe.md),
  [multimodal-encoder-inference](multimodal-encoder-inference.md).

## Source
Extracted from `docs/deployment/v7x_recipes.md` (kept in place); configs and baselines read
from `scripts/vllm/benchmarking/configs/`, `scripts/vllm/benchmarking/baselines/perf/`,
`scripts/vllm/benchmarking/run_benchmarks.sh` and `check_regression.py`.
