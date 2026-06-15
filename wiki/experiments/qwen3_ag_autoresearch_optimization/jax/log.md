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

## [2026-06-15] loop-iteration | v054-c fused-qknorm-rope crashed

**Op**: loop-iteration
**Experiment**: [2026-06-15-qwen3-jax-v054-fused-qknorm-rope-c.md](file:///mnt/disks/persist/torch-tpu/tpu_performance_autoresearch_wiki_ag/wiki/experiments/qwen3_ag_autoresearch_optimization/jax/experiments/2026-06-15-qwen3-jax-v054-fused-qknorm-rope-c.md)
**Verdict**: invalid
**Notes**: The workload crashed during JAX compilation because the `fused_qknorm_rope` Pallas kernel was not wrapped in a `shard_map`. We will wrap the kernel call in a `shard_map` using `_SPLASH_MESH` and retry.
