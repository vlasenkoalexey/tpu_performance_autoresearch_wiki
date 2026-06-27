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
**Op**: start
**Cluster pool**: alekseyv-tpu-v6e8-spot-xpk
**Parallelism**: 1
**First-pick hypothesis**: splash-attention (to unlock 8K context length)
**Notes**: session opened via /start-experiment.

**Op**: end
**Status**: blocked (OOM during compilation at 8K context)
**Next hypothesis**: tokamax-ce or gradient-checkpointing
## [2026-06-26] end | /start-experiment session end
