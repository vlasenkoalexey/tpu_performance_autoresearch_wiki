## [2026-06-05] loop-iteration | v044 bs24 scaling

**Op**: loop-iteration
**Experiment**: [2026-06-05-qwen3-jax-v044-bs24.md](file:///mnt/disks/persist/torch-tpu/tpu_performance_autoresearch_wiki_ag/wiki/experiments/qwen3_ag_autoresearch_optimization/jax/experiments/2026-06-05-qwen3-jax-v044-bs24.md)
**Verdict**: refuted
**Notes**: Scaling to `bs=24` per-chip OOMs during XLA compilation (`38.06G of 31.25G`). `bs=16` is the limit.

## [2026-06-05] loop-iteration | v043 bs32 scaling OOM

**Op**: loop-iteration
**Experiment**: [2026-06-05-qwen3-jax-v043-bs32.md](file:///mnt/disks/persist/torch-tpu/tpu_performance_autoresearch_wiki_ag/wiki/experiments/qwen3_ag_autoresearch_optimization/jax/experiments/2026-06-05-qwen3-jax-v043-bs32.md)
**Verdict**: refuted
**Notes**: Scaling to `bs=32` per-chip resulted in `RESOURCE_EXHAUSTED` (33.07G required vs 31.25G available) during XLA compilation.

## [2026-06-05] loop-iteration | v042 gate_up_proj fusion supported

**Op**: loop-iteration
**Experiment**: [2026-06-05-qwen3-jax-v042-gate-up-fusion.md](file:///mnt/disks/persist/torch-tpu/tpu_performance_autoresearch_wiki_ag/wiki/experiments/qwen3_ag_autoresearch_optimization/jax/experiments/2026-06-05-qwen3-jax-v042-gate-up-fusion.md)
**Verdict**: supported
**Notes**: Fusing `gate_proj` and `up_proj` increased throughput from 49,944 tok/s to 51,287 tok/s (MFU 33.0%). Fixed device-init OOMs using `jax.jit`.

## [2026-06-04] stop | /stop-experiment session end

**Op**: stop
**Pages created**: 0
**Pages updated**: wiki/experiments/qwen3_ag_autoresearch_optimization/jax/log.md
**Notes**: Clean shutdown via /stop-experiment. Reaped orphan workloads: alekseyv-qwen3-jax-v040-run1, alekseyv-qwen3-jax-v042-tokamax, av-qwen3-jax-v040-tokamax. Outstanding lint items: 0.
Session metrics: 7 experiments run (v034-v040), 0 supported, 7 refuted/invalid. Frontier shifted to 34.6% MFU at v036.

## [2026-06-03] stop | /stop-experiment session end

**Op**: stop
**Pages created**: 0
**Pages updated**: wiki/experiments/qwen3_ag_autoresearch_optimization/jax/log.md
**Notes**: Clean shutdown via /stop-experiment. Reaped orphan workloads: none. Outstanding lint items: 0.
Session metrics: 8 experiments run (v026-v033), 2 supported, 5 refuted, 1 invalid. Frontier shift to 32.8% MFU.
## [2026-06-02] start | /start-experiment session begin

**Op**: start
**Cluster pool**: alekseyv-tpu-v6e8-spot-xpk
**Parallelism**: 1
**First-pick hypothesis**: Selective SparseCore offload (reduce-scatter offload only) to minimize host transfer overhead and PCIe bottleneck.
**Notes**: session opened/re-grounded via /start-experiment.

## [2026-06-02] loop-iteration | v002 selective SparseCore offload crashed

**Op**: loop-iteration
**Experiment**: [2026-06-02-qwen3-jax-v002-selective-sc-offload.md](file:///mnt/disks/persist/torch-tpu/tpu_performance_autoresearch_wiki_ag/wiki/experiments/qwen3_ag_autoresearch_optimization/jax/experiments/2026-06-02-qwen3-jax-v002-selective-sc-offload.md)
**Verdict**: invalid
**Notes**: The GKE workload crashed immediately on startup with `Unknown flag in XLA_FLAGS: --xla_tpu_enable_sparse_core_collective_offload_reduce_scatter=true`. This flag is not supported by the current image's libtpu/XLA version.

## [2026-06-02] loop-iteration | v003 selective rematerialization crashed

**Op**: loop-iteration
**Experiment**: [2026-06-02-qwen3-jax-v003-selective-remat.md](file:///mnt/disks/persist/torch-tpu/tpu_performance_autoresearch_wiki_ag/wiki/experiments/qwen3_ag_autoresearch_optimization/jax/experiments/2026-06-02-qwen3-jax-v003-selective-remat.md)
**Verdict**: refuted
**Notes**: The selective rematerialization policy `checkpoint_dots_with_no_batch_dims` reduced compilation-time HBM usage by 9.38 GB (from 42.99 GB to 33.61 GB), but still exceeded the physical 31.25 GB limit by 2.36 GB, resulting in a compilation HBM OOM.
## [2026-06-05] loop-iteration | v045 nsa bs=24

| Date | ID | Hypothesis | Step Time | MFU | Verdict |
|---|---|---|---|---|---|
| 2026-06-05 | [v045](experiments/2026-06-05-qwen3-jax-v045-nsa.md) | Native Sparse Attention XLA fallback will reduce memory and allow bs=24 | N/A | N/A | **FAILED**. OOM. XLA fallback (dense or sparse) materializes too much memory. Pallas kernel required. |

**Op**: loop-iteration
**Experiment**: [2026-06-05-qwen3-jax-v045-nsa.md](file:///mnt/disks/persist/torch-tpu/tpu_performance_autoresearch_wiki_ag/wiki/experiments/qwen3_ag_autoresearch_optimization/jax/experiments/2026-06-05-qwen3-jax-v045-nsa.md)
**Verdict**: closed
**Notes**: JAX scaling to bs=24 blocked by HBM limits at seq=2048 without custom Pallas kernels.
## [2026-06-05] loop-iteration | v046 nsa pallas fix

| Date | ID | Hypothesis | Step Time | MFU | Verdict |
|---|---|---|---|---|---|
| 2026-06-05 | [v046](experiments/2026-06-05-qwen3-jax-v046-nsa-pallas.md) | Pallas NSA fix for `ConcretizationTypeError` | N/A | N/A | **FAILED**. The `math.sqrt` fix worked, but the underlying Pallas kernel implementation is not fully ported to TPU yet (only CPU). |

**Op**: loop-iteration
**Experiment**: [2026-06-05-qwen3-jax-v046-nsa-pallas.md](file:///mnt/disks/persist/torch-tpu/tpu_performance_autoresearch_wiki_ag/wiki/experiments/qwen3_ag_autoresearch_optimization/jax/experiments/2026-06-05-qwen3-jax-v046-nsa-pallas.md)
**Verdict**: closed
**Notes**: Pallas kernel support for TPU is required.
