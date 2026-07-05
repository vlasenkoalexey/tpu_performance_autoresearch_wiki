## 2026-07-05 stop | /stop-experiment session end

**Op**: stop
**Pages created**: none
**Pages updated**: wiki/experiments/qwen3_ag_autoresearch_optimization/jax/log.md
**Notes**: Clean shutdown via user request. Reaped orphan workloads: none.
Session metrics: 0 experiments completed in this session.
## 2026-07-05 stop | /stop-experiment session end

**Op**: stop
**Pages created**: none
**Pages updated**: wiki/experiments/qwen3_ag_autoresearch_optimization/jax/log.md
**Notes**: Clean shutdown via user request. Reaped orphan workloads: none.
Session metrics: 0 experiments completed in this session (v059f deleted due to Kueue mismatch).
## [2026-07-04] start | /start-experiment session begin

**Op**: start
**Cluster pool**: alekseyv-tpu-v6e8-spot-xpk
**Parallelism**: 1
**First-pick hypothesis**: Tensor Parallelism (TP=2) batch scaling.
**Notes**: session opened via /start-experiment.

## [2026-07-03] stop | /stop-experiment session end

**Op**: stop
**Pages created**: None
**Pages updated**: wiki/experiments/qwen3_ag_autoresearch_optimization/jax/log.md
**Notes**: Clean shutdown via /stop-experiment. Reaped orphan workloads: none.
Outstanding lint items: 0.
Session metrics: 9 experiments run, 1 supported, 8 failed/invalid.

## [2026-06-27] start | /start-experiment session begin

## [2026-06-27] loop-iteration | v015-ring-attn-seq16k-bs2 on 8B/v6e-8: invalid (OOM during XLA compile, HLO temp 46.60G)

## [2026-06-27] loop-iteration | v014-ring-attn-seq16k on 8B/v6e-8: invalid (crashed with OOM during compile due to 40GB logits tensor)

**Op**: start
**Cluster pool**: alekseyv-tpu-v6e8-spot-xpk
**Parallelism**: 1
**First-pick hypothesis**: Ring attention seqlen=16384 scaling to amortize sp=2 comm overhead.
**Notes**: session opened via /start-experiment.

## [2026-06-02] start | /start-experiment session begin

**Op**: start
**Cluster pool**: <your-cluster>
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

## [2026-06-15] loop-iteration | v054-d fused-qknorm-rope crashed

**Op**: loop-iteration
**Experiment**: [2026-06-15-qwen3-jax-v054-fused-qknorm-rope-d.md](file:///mnt/disks/persist/torch-tpu/tpu_performance_autoresearch_wiki_ag/wiki/experiments/qwen3_ag_autoresearch_optimization/jax/experiments/2026-06-15-qwen3-jax-v054-fused-qknorm-rope-d.md)
**Verdict**: invalid
**Notes**: The workload crashed during setup with `ValueError: fused_qknorm_rope requires a registered mesh via set_splash_mesh` because `set_splash_mesh()` was only called when `use_splash=True`. I have fixed `train.py` to call it unconditionally and will retry.

## [2026-06-15] loop-iteration | v054-e fused-qknorm-rope crashed (OOM)

**Op**: loop-iteration
**Experiment**: [2026-06-15-qwen3-jax-v054-fused-qknorm-rope-e.md](file:///mnt/disks/persist/torch-tpu/tpu_performance_autoresearch_wiki_ag/wiki/experiments/qwen3_ag_autoresearch_optimization/jax/experiments/2026-06-15-qwen3-jax-v054-fused-qknorm-rope-e.md)
**Verdict**: invalid
**Notes**: The workload crashed with an OOM error during the first jitted_step: `RESOURCE_EXHAUSTED: Allocation (size=34359738368) would exceed memory`. The shape mentioned is `f32[4,32,8192,8192]`, which is a materialized attention matrix. The fusion must be allocating too much memory or disabling an optimization that saves memory.

## [2026-06-15] formulate-hypothesis | v055 selective-remat

**Op**: formulate-hypothesis
**Experiment**: [2026-06-15-qwen3-jax-v055-ac-selective-remat.md](file:///mnt/disks/persist/torch-tpu/tpu_performance_autoresearch_wiki_ag/wiki/experiments/qwen3_ag_autoresearch_optimization/jax/experiments/2026-06-15-qwen3-jax-v055-ac-selective-remat.md)
**Status**: in_progress
**Notes**: Formulated hypothesis to address HBM limits via Activation Checkpointing.
## [2026-06-15] loop-iteration | v055 selective activation checkpointing crashed

**Op**: loop-iteration
**Experiment**: [2026-06-15-qwen3-jax-v055-ac-selective-remat.md](file:///mnt/disks/persist/torch-tpu/tpu_performance_autoresearch_wiki_ag/wiki/experiments/qwen3_ag_autoresearch_optimization/jax/experiments/2026-06-15-qwen3-jax-v055-ac-selective-remat.md)
**Verdict**: refuted
**Notes**: The run failed during compilation. However, it was not an HBM OOM (as in previous runs), but rather a VMEM (Vector Memory) OOM inside the Pallas `splash_mha_dkv_no_residuals` backward kernel. Scoped allocation of 35.63M exceeded the 32.00M limit.

## [2026-06-27] loop-iteration | v012-ring-attention on 8B/v6e-8: confirmed (22.8% MFU)
- Created `v012-ring-attention.md` to test Ring Attention for sequence parallelism at 8K context.
- Result: Compiled and trained successfully at seqlen=8192 with bs=8 after fixing 2D FSDP cross-entropy and Pallas block sizes. MFU dropped to 22.8% due to sp=2 communication overhead and tile size inefficiency. Confirmed.

## [2026-06-27] loop-iteration | v013-fused-glu on 8B/v6e-8: refuted (30.6% MFU)
- Created `v013-fused-glu.md` to test a custom Pallas kernel for Fused GLU.
- Result: MFU regressed to 30.6%. `jax.custom_vjp` usage with standard `jnp.dot` in the backward pass forced materialization of massive intermediate tensors to HBM, negating bandwidth savings. XLA redundantly computed forward matmuls three times. Refuted.

2026-06-27-qwen3-jax-v016-fused-glu-bwd.md | Falsified | 11.9% MFU | Backward kernel exceeded VMEM limit and silently fell back to unrolled JAX reference ops.
2026-06-27-qwen3-jax-v017-fused-glu-tiled-bwd.md | Falsified | 0.0% MFU | Compile OOM (166GB). Pallas grid reduction materialized massive HBM buffers.
2026-06-27-qwen3-jax-v018-fused-glu-fori-bwd.md | Pending | N/A | Testing in-kernel fori_loop reduction for backward pass.

## [2026-06-27] loop-iteration | v020-splash-attn-only-scan3 on 8B/v6e-8: confirmed (32.3% MFU)
- Created `v020-splash-attn-only-scan3.md` to recover the baseline by falling back to standard XLA compilation with scan and per-layer remat.
- Result: Compiled and trained successfully at seqlen=8192 with bs=8. MFU recovered to 32.3%. Confirmed.
| v021-tp2 | Enable Tensor Parallelism (TP=2) with FSDP=4 to unblock global batch size 32 | 22.9% | MFU regression. Chunked cross entropy needed for HBM. |
