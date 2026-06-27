## [2026-06-27] loop-iteration | v011-pallas-rmsnorm-rope on 8B/v6e-8: refuted (crash)
- Created `v011-pallas-rmsnorm-rope.md` to test fusing RMSNorm and RoPE in Pallas to reduce HBM traffic.
- Forked code from v009 to `wiki/experiments/qwen3_ag_autoresearch_optimization/jax/.repo/2026-06-27-v011-pallas-rmsnorm-rope/`.
- Result: Crashed. Pallas kernels lack native autodiff, requiring a massive custom VJP for the backward pass. XLA already fuses Norms optimally anyway. Refuted.

## [2026-06-27] loop-iteration | v010-fsdp-async-overlap on 8B/v6e-8: refuted (32.5% MFU, within noise)

**Op**: end
**Status**: refuted (silent no-op; 45.3k tok/s and 32.5% MFU, identical to baseline v009. XLA is likely already overlapping collectives optimally without manual flag intervention).
**Next hypothesis**: Fused RMSNorm+RoPE Pallas kernel

## 2026-06-27: Experiment v010 (FSDP async overlap)
- Created `v010-fsdp-async-overlap.md` to test overlapping FSDP collectives with TensorCore computation via XLA flags.
- Preparing to build and push docker image, then dispatch to `gke-cluster-runner`.

## [2026-06-27] loop-iteration | v009-scan-over-layers on 8B/v6e-8: confirmed (32.5% MFU)

**Op**: end
**Status**: confirmed (compiled fast; achieved ~45.3k tok/s and 32.5% MFU at 8192 seqlen with `nnx.scan` over layers and `jax.checkpoint`).
**Next hypothesis**: None right now; retrospective updated.

## [2026-06-27] analyze | qwen3-jax retrospective

**Op**: analyze (retrospective).
**Pages created**: [wiki/analyses/2026-06-27-qwen3-jax-retrospective-2.md](../../../../analyses/2026-06-27-qwen3-jax-retrospective-2.md)
**Pages updated**: `wiki/index.md` (Analyses count + 1)
**Key result**: Exhaustion signal broken on jax lane (frontier pushed to 32.5% MFU from v004 via v009 scan-over-layers). Identifies FSDP collective optimization (async overlap) and Pallas kernels as the primary unblocked directions.

## [2026-06-27] loop-iteration | v008-sparsecore-offload on 8B/v6e-8: blocked (hung in compilation for 60m)

## [2026-06-27] loop-iteration | v006-tokamax-batch on 8B/v6e-8: refuted (performance regressed to 29.7% MFU despite unlocking bs=2)

## [2026-06-26] start | /start-experiment session begin

**Op**: start
**Cluster pool**: alekseyv-tpu-v6e8-spot-xpk
**Parallelism**: 1
**First-pick hypothesis**: tokamax-ce (or gradient-checkpointing, to resolve HBM OOM)
**Notes**: session opened via /start-experiment.

**Op**: end
**Status**: blocked (OOM during compilation at 8K context due to SDPA materialization; `tokamax-ce` alone does not fix the attention memory block).
**Next hypothesis**: v003-splash-tokamax (combine splash-attention and tokamax-ce)
## [2026-06-26] end | /start-experiment session end

## [2026-06-26] start | /start-experiment session begin

**Op**: start
**Cluster pool**: alekseyv-tpu-v6e8-spot-xpk
**Parallelism**: 1
**First-pick hypothesis**: v003-splash-tokamax (combining both to unlock 8K context length)
**Notes**: autonomous loop continuing.

**Op**: end
**Status**: refuted (OOM during compilation. Used 45.12G of 31.25G. The combined optimizations do not overcome the activation memory footprint at 8K).
**Next hypothesis**: gradient-checkpointing (to tackle the activation memory wall)
## [2026-06-26] end | /start-experiment session end

## [2026-06-26] start | /start-experiment session begin

**Op**: start
**Cluster pool**: alekseyv-tpu-v6e8-spot-xpk
**Parallelism**: 1
**First-pick hypothesis**: gradient-checkpointing (applied on top of splash-attention)
**Notes**: autonomous loop continuing.

**Op**: end
**Status**: confirmed (compiled successfully; achieved ~43.3k tok/s and 31.0% MFU at 8192 seqlen).
**Next hypothesis**: None right now; target achieved.
## [2026-06-26] end | /start-experiment session end
## [2026-06-27] start | /start-experiment session begin

**Op**: start
**Cluster pool**: alekseyv-tpu-v6e8-spot-xpk
**Parallelism**: 1
**First-pick hypothesis**: batch-scaling (to increase MXU occupancy at 8K seqlen)
**Notes**: autonomous loop continuing.

## [2026-06-27] loop-iteration | v005-batch-scaling on 8B/v6e-8: refuted (compilation OOM; activation + Adam state > 31.25GB)

**Op**: start
**Cluster pool**: alekseyv-tpu-v6e8-spot-xpk
**Parallelism**: 1
**First-pick hypothesis**: splash-attention (to unlock 8K context length)
**Notes**: session opened via /start-experiment.

**Op**: end
**Status**: blocked (OOM during compilation at 8K context)
**Next hypothesis**: tokamax-ce or gradient-checkpointing
## [2026-06-26] end | /start-experiment session end

## [2026-06-27-qwen3-jax-v007-splash2k](experiments/2026-06-27-qwen3-jax-v007-splash2k.md)
* **Status:** Completed
* **Throughput:** ~42732 tok/s (30.6% MFU)
* **Verdict:** Refuted. Increasing `sa_block_kv` to 2048 decreased MFU by 0.4 pp compared to the v004 baseline.

## 2026-06-27: Experiment v009 (Scan over layers)
- Built and pushed image for `v009-scan-over-layers`.
- Validated `nnx.scan` logic with `nnx.vmap` local dummy tests and CPU container test.
- Fixed `model/sharding.py` to match new scanned param topology (`model.scanned_layers.layers.*`).
- Started `v009` on cluster `alekseyv-tpu-v6e8-spot-xpk`. Waiting for results.
