---
title: SPMD lock-step rules and collective fusion (golden rules, spmd_safe)
type: doc-concept
provenance: doc
source: docs/markdown/distributed_training_101.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T02:38:46Z}
---
# SPMD lock-step rules and collective fusion (golden rules, spmd_safe)

## Definition
The distributed doc's "Golden Rules of Distributed TPU" encode the constraint that every rank must issue the same device work in the same order: (1) **never diverge** - no `if rank == 0` around operations that trigger materialization such as `.item()`, because "if one rank runs ahead, the mesh deadlocks"; (2) **shared seeds**, so all ranks start from identical weights; (3) **flush at exit** - the doc says to call `torch.tpu.manual_seed_all(0)` after the loop so the final weight update is actually executed. Its training step ends with `loss.item()` as a deliberate materialization point that keeps ranks in lock-step.

## In torch_tpu (grounded)
- **Why divergence deadlocks.** Eager TPU ops are deferred and fused into graphs that are compiled and executed at materialization points ([deferred-execution-and-materialization](../concepts/deferred-execution-and-materialization.md)). A collective inside such a graph only completes when every participating rank executes a matching graph. If ranks fuse different work around a collective, or one rank materializes while others do not, the programs no longer match.
- **The default guard: collectives in their own graph.** [`GetCollectiveSplitMode`](../catalog/csrc/distributed/process_group_tpu.cc.md#GetCollectiveSplitMode "csrc/distributed/process_group_tpu.cc:L530") returns a split-both mode by default, so each eager collective (e.g. [`ProcessGroupTpu.allreduce`](../catalog/csrc/distributed/process_group_tpu.cc.md#ProcessGroupTpu.allreduce "csrc/distributed/process_group_tpu.cc:L1785")) is cut out of the surrounding graph - safe against rank-dependent fusion, at the cost of extra graph boundaries.
- **Opting into fusion: `torch.tpu.distributed.spmd_safe`.** The experimental decorator [`spmd_safe`](../catalog/src/torch_tpu/_internal/distributed/spmd_util.md#spmd_safe) marks a function as issuing identical TPU ops, collectives and shapes on every rank. Eagerly it synchronizes inputs, enters the region ([`EnterSpmdSafeRegion`](../catalog/csrc/distributed/utils.cc.md#EnterSpmdSafeRegion) pushes a context state read by [`IsSpmdSafe`](../catalog/csrc/distributed/utils.cc.md#IsSpmdSafe)), and inside it the split mode becomes "none" so collectives fuse with neighboring ops. Under `torch.compile` it annotates the traced FX nodes instead ([fx-graph-passes](../concepts/fx-graph-passes.md)).
- **Seeding.** `torch.tpu.manual_seed_all` is [`_DeviceModule.manual_seed_all`](../catalog/src/torch_tpu/_internal/device/_device_module.md#_DeviceModule.manual_seed_all), a no-op without a TPU, otherwise forwarding to the C++ per-device generators ([device-streams-generators-and-rng](../concepts/device-streams-generators-and-rng.md)). The doc's "flush at exit" use of it relies on it touching device state; the general-purpose flush is a materialization (`.item()`, `.cpu()`) or `torch.accelerator.synchronize()` ([tensor-synchronization](../concepts/tensor-synchronization.md)).

## Why it matters / when it applies
- **Rank-dependent host logic is the classic hang.** Logging or checkpointing guarded by `rank == 0` must not call `.item()`/`.cpu()` on device tensors unless every rank does the same. Do the materialization on all ranks, then branch on the host value.
- **Perf lever:** wrapping a rank-uniform region (e.g. a fused all-reduce-plus-scale, an optimizer step) in `spmd_safe` removes the per-collective graph splits and lets XLA overlap/fuse communication with compute. Do not use it on code with rank-dependent control flow - it trades the safety guard for speed.
- **Materialization cadence is a trade-off.** The doc's per-step `.item()` keeps ranks aligned but adds a host sync each step; see [host-sync-avoidance-in-training-loops](host-sync-avoidance-in-training-loops.md) for accumulating on device instead.
- Identical seeds are also a correctness prerequisite for DDP, which assumes replicas start equal.

## Connections
- Code concepts: [process-group-and-collectives](../concepts/process-group-and-collectives.md), [deferred-execution-and-materialization](../concepts/deferred-execution-and-materialization.md), [context-states-and-execution-modes](../concepts/context-states-and-execution-modes.md), [distributed-launchers-and-spmd](../concepts/distributed-launchers-and-spmd.md), [device-streams-generators-and-rng](../concepts/device-streams-generators-and-rng.md), [tensor-synchronization](../concepts/tensor-synchronization.md), [fx-graph-passes](../concepts/fx-graph-passes.md)
- Module catalogs: [src/torch_tpu/_internal/distributed/spmd_util](../catalog/src/torch_tpu/_internal/distributed/spmd_util.md), [csrc/distributed/utils.cc](../catalog/csrc/distributed/utils.cc.md), [csrc/distributed/process_group_tpu.cc](../catalog/csrc/distributed/process_group_tpu.cc.md), [src/torch_tpu/_internal/device/_device_module](../catalog/src/torch_tpu/_internal/device/_device_module.md)
- Related doc-concepts: [torchrun-launch-and-tpu-dist-ddp](torchrun-launch-and-tpu-dist-ddp.md), [host-sync-avoidance-in-training-loops](host-sync-avoidance-in-training-loops.md), [defer-and-fuse-materialization](defer-and-fuse-materialization.md), [eager-execution-modes](eager-execution-modes.md)

## Source
Extracted from `docs/markdown/distributed_training_101.md` (Golden Rules section, kept in place). The `spmd_safe` and split-mode grounding was checked against `src/torch_tpu/_internal/distributed/spmd_util.py` and `csrc/distributed/process_group_tpu.cc` at v0.2.0.
