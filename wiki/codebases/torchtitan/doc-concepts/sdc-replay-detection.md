---
title: Silent data corruption detection by deterministic replay
type: doc-concept
provenance: doc
source: torchtitan/observability/silent_data_corruption.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T06:34:20Z}
---
# Silent data corruption detection by deterministic replay

## Definition
TorchTitan can detect silent data corruption (SDC) by re-executing a deterministic forward/backward
and comparing all of its observable effects against the reference execution. It trades extra
forward/backward time on checked steps for an in-training, hardware-agnostic check, and it requires
fully deterministic execution. Disabled by default.

## In torchtitan (grounded)
- Component: [`SDCReplayer`](../catalog/torchtitan/observability/sdc_replayer.md#SDCReplayer "torchtitan/observability/sdc_replayer.py:L318") with
  [`SDCReplayer.Config`](../catalog/torchtitan/observability/sdc_replayer.md#SDCReplayer.Config "torchtitan/observability/sdc_replayer.py:L331"):
  [`num_steps`](../catalog/torchtitan/observability/sdc_replayer.md#SDCReplayer.Config.num_steps)
  (optimizer steps checked after each (re)start; -1 = every step) and
  [`num_replays`](../catalog/torchtitan/observability/sdc_replayer.md#SDCReplayer.Config.num_replays "torchtitan/observability/sdc_replayer.py:L340")
  (re-executions compared to the reference, >= 1). The replay boundary is
  [`run_fwd_bwd`](../catalog/torchtitan/observability/sdc_replayer.md#SDCReplayer.run_fwd_bwd "torchtitan/observability/sdc_replayer.py:L392"); the
  schedule restarts via [`reset_schedule`](../catalog/torchtitan/observability/sdc_replayer.md#SDCReplayer.reset_schedule)
  after every checkpoint load.
- Enabled only programmatically through [`Trainer.Config.sdc_replayer`](../catalog/torchtitan/trainer.md#Trainer.Config.sdc_replayer)
  (CLI-suppressed, `None` disables) together with
  [`DebugConfig.deterministic`](../catalog/torchtitan/config/configs.md#DebugConfig.deterministic)
  `=True` and [`DebugConfig.deterministic_warn_only`](../catalog/torchtitan/config/configs.md#DebugConfig.deterministic_warn_only)
  `=False`; [`Trainer.Config.__post_init__`](../catalog/torchtitan/trainer.md#Trainer.Config.__post_init__)
  enforces these.
- Failure: [`SDCReplayMismatch`](../catalog/torchtitan/observability/sdc_replayer.md#SDCReplayMismatch)
  carrying [`step`](../catalog/torchtitan/observability/sdc_replayer.md#SDCReplayMismatch.step),
  [`local_step`](../catalog/torchtitan/observability/sdc_replayer.md#SDCReplayMismatch.local_step),
  [`replay`](../catalog/torchtitan/observability/sdc_replayer.md#SDCReplayMismatch.replay),
  [`rank`](../catalog/torchtitan/observability/sdc_replayer.md#SDCReplayMismatch.rank), and the first
  differing [`signature_mismatch`](../catalog/torchtitan/observability/sdc_replayer.md#SDCReplayMismatch.signature_mismatch).
- Test recipe: [`deepseek_v3_debugmodel_sdc_replay_mismatch`](../catalog/torchtitan_recipes/tests/features.md#deepseek_v3_debugmodel_sdc_replay_mismatch)
  with [`SDCReplayMismatchTrainer`](../catalog/torchtitan_recipes/tests/features.md#SDCReplayMismatchTrainer).

## Why it matters / when it applies
- **Cost model:** a checked step costs `1 + num_replays` forward/backward executions; unchecked steps
  compute no signatures. The default (`num_steps=1`) checks the first step after every (re)start,
  where a bad restore or initialization is most likely. Benchmark/profiling runs must keep it off,
  or exclude checked steps from step-time statistics.
- **What is replayed:** only the first forward/backward of a checked optimizer step - one
  gradient-accumulation group, which under PP is one whole pipeline schedule. Later accumulation
  groups run unchecked (a cost choice; they exercise the same paths).
- **State handling:** gradients are never snapshotted; the checked call must start from the
  post-`zero_grad` state, and restore rebuilds it in place (preserving storage addresses for CUDA
  graphs). Only the final execution's gradients, buffers, RNG advance, token counter, and loss are
  committed. Signature = loss, local parameter gradients, registered buffers, Python/torch RNG
  state, token counter, hashed with `torch.hash_tensor`.
- **Determinism is a prerequisite**, which itself can cost throughput (deterministic kernels).
- **Participating backends:** eager, `torch.compile`, CUDA graphs, symmetric-memory FSDP,
  distributed GEMM, async TP, DeepEP v2, HybridEP, MinimalAsyncEP, and GraphTrainer.
- **Limitations:** CUDA graphs require `num_replays=1`; the XOR-based hash is order-insensitive, so
  permutations and some repeated-value corruptions can collide.
- **Failure semantics:** a mismatch raises on every rank before grad clipping, optimizer, LR
  scheduler, or checkpoint save, so corrupted state is never committed.
- TPU relevance: the doc lists only GPU execution backends, and no TPU recipe enables
  `sdc_replayer` at this commit; on TPU the determinism and `torch.hash_tensor` requirements would
  need to be validated first.

## Connections
- Code concepts: [observability](../concepts/observability.md),
  [trainer-and-train-loop](../concepts/trainer-and-train-loop.md),
  [debug-and-profiling-tools](../concepts/debug-and-profiling-tools.md),
  [checkpointing](../concepts/checkpointing.md).
- Module catalogs: [torchtitan/observability/sdc_replayer](../catalog/torchtitan/observability/sdc_replayer.md),
  [torchtitan/trainer](../catalog/torchtitan/trainer.md).
- Related doc-concepts: [structured-trace-logging](structured-trace-logging.md).

## Source
Extracted from `torchtitan/observability/silent_data_corruption.md` (kept in place).
