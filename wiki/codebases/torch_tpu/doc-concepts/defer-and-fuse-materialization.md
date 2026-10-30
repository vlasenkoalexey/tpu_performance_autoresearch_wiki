---
title: DeferAndFuse - deferred queueing, multi-op fusion and materialization triggers
type: doc-concept
provenance: doc
source: docs/markdown/eager_mode.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T02:38:46Z}
---
# DeferAndFuse - deferred queueing, multi-op fusion and materialization triggers

## Definition
In fused eager mode (`TORCH_TPU_DEFER_AND_FUSE=1`) TorchTPU does not launch a device kernel per ATen op. The doc describes three steps: (1) **deferred queueing** - element-wise and arithmetic ops are recorded in an internal deferred execution buffer; (2) **multi-op fusion** - when a **materialization trigger** forces execution, XLA compiles the accumulated ops into one fused program; (3) **hardware efficiency** - intermediates stay in on-chip VMEM / vector registers instead of round-tripping through HBM. Timing the doc's example shows near-zero "deferred queue time" for the ops themselves and the whole compile+execute cost landing on the `.cpu()` call.

Materialization triggers the doc lists:
- host transfers: `.cpu()`, `.item()`, `.tolist()`, `.numpy()`;
- explicit `torch.accelerator.synchronize()`;
- value inspection: `print(tensor)` / `repr(tensor)`;
- data-dependent Python control flow, e.g. `if (tensor > 0).all():`;
- buffer thresholds - "TorchTPU automatically flushes and compiles when operation queues reach internal memory or node limits".

## In torch_tpu (grounded)
- Entry: the deferred op graph lives in `csrc/eager`; [`Materialize`](../catalog/csrc/eager/materialize.h.md#Materialize) plus [`MaterializeStream`](../catalog/csrc/eager/materialize.cc.md#MaterializeStream), [`MaterializeCurrentStream`](../catalog/csrc/eager/materialize.cc.md#MaterializeCurrentStream) and [`MaterializeDevice`](../catalog/csrc/eager/materialize.cc.md#MaterializeDevice) flush the queue at the granularity of a buffer, a stream, or a whole device (the last is what a device-wide synchronize needs). Work is handed to a [`MaterializationWorker`](../catalog/csrc/eager/materialize.cc.md#MaterializationWorker) whose separate materialize and execute loops ([`MaterializationWorker.MaterializeLoop`](../catalog/csrc/eager/materialize.cc.md#MaterializationWorker.MaterializeLoop), [`MaterializationWorker.ExecuteLoop`](../catalog/csrc/eager/materialize.cc.md#MaterializationWorker.ExecuteLoop)) let compilation of one cluster overlap execution of the previous one. [`MaterializationBlockMode`](../catalog/csrc/eager/materialize.h.md#MaterializationBlockMode) picks between `kNonBlocking` and `kBlockUntilStarted`.
- A stream flush is a snapshot: [`EventSnapshot.Record`](../catalog/csrc/eager/events_queue.cc.md#EventSnapshot.Record) / [`RecordDeviceSnapshots`](../catalog/csrc/eager/events_queue.cc.md#RecordDeviceSnapshots) freeze a [`MaterializationSettings`](../catalog/csrc/eager/events_queue.h.md#MaterializationSettings) (reason, graph mode, compile mode) at request time.
- The doc's trigger list maps onto [`MaterializationReason`](../catalog/csrc/eager/structured_log_buffer.h.md#MaterializationReason): `kCpuTransfer` (`.cpu()` / `.numpy()`), `kScalarConversion` (`.item()`, Python `bool()` in control flow), `kExplicitSync`, plus reasons the doc does not mention - `kDistributedOp` (collectives), `kAutogradSync`, `kCompileModeExecution`, `kDebugMode`, and `kRepeatedOpDetection`.
- The "buffer threshold" trigger, as implemented in this tree, is the **repeated-ops heuristic**: [`RecordDeferredOpAndDetectRepetition`](../catalog/csrc/eager/events_queue.cc.md#RecordDeferredOpAndDetectRepetition) records each new deferred op and returns true when the stream should be materialized because the tail of the queue repeats (per `events_queue.cc`, a subsequence of 2-128 deferred-op hashes seen at least twice - e.g. the body of a Python loop), so the queue is cut at loop boundaries into a cluster that is reused every iteration instead of growing without bound; [`ResetRepeatedOpsHeuristicState`](../catalog/csrc/eager/events_queue.cc.md#ResetRepeatedOpsHeuristicState) clears it. The internal env var [`kTorchTpuInternalDetectRepeatedOpsEnvVar`](../catalog/csrc/common/env_vars.h.md#kTorchTpuInternalDetectRepeatedOpsEnvVar) selects `safe` (flush with [`MaterializationMode`](../catalog/csrc/eager/events_queue.h.md#MaterializationMode) `kSplitGraph`) or `aggressive` (`kFullGraph`). The doc's wording ("memory or node limits") is looser than this; no separate node-count cap was found in `csrc/eager`.
- Collectives force their own flush by default ([`kTorchTpuInternalMaterializeCollectiveTensorsEnvVar`](../catalog/csrc/common/env_vars.h.md#kTorchTpuInternalMaterializeCollectiveTensorsEnvVar), "forcing graph breaks for collective ops"; can be disabled for SPMD workloads whose ranks build identical graphs).
- Python-side sync entry points: [`SynchronizeTensors`](../catalog/csrc/internal/sync/sync.cc.md#SynchronizeTensors) and [`PyIsMaterialized`](../catalog/csrc/internal/sync/sync_py.cc.md#PyIsMaterialized).
- Each flushed cluster is compiled with `kFastRuntime` effort (see [eager-execution-modes.md](eager-execution-modes.md)) and looked up in the [multi-tier compilation cache](multi-tier-compilation-cache.md) by a graph fingerprint, so a steady-state training loop that flushes the same cluster every step pays compile once.

## Why it matters / when it applies
- Fusion is the point: a chain of element-wise ops that costs N HBM round-trips in Strict eager becomes one kernel (the same effect `torch.compile` gets from XLA fusion - [op-fusion-and-hbm-traffic.md](op-fusion-and-hbm-traffic.md)).
- Every unplanned trigger cuts the cluster: stray `.item()` / `print` / `if tensor:` in a training step fragments the graph, shrinks fusion scope, and adds a host round-trip. Profiling with materialization reasons is how to find them.
- Fragmented or shape-varying clusters each get a distinct fingerprint and therefore their own cold compile ([graph-fingerprint-and-recompilation.md](graph-fingerprint-and-recompilation.md)).
- Fused eager fuses "on the fly" within the window between triggers; it does not see across triggers the way whole-graph `torch.compile` does.

## Connections
- Code concepts: [deferred-execution-and-materialization](../concepts/deferred-execution-and-materialization.md), [tensor-synchronization](../concepts/tensor-synchronization.md), [eager-op-dispatch](../concepts/eager-op-dispatch.md), [host-device-copy](../concepts/host-device-copy.md), [compilation-pipeline](../concepts/compilation-pipeline.md), [compilation-cache](../concepts/compilation-cache.md), [process-group-and-collectives](../concepts/process-group-and-collectives.md), [context-states-and-execution-modes](../concepts/context-states-and-execution-modes.md)
- Module catalogs: [csrc/eager/materialize.cc](../catalog/csrc/eager/materialize.cc.md), [csrc/eager/materialize.h](../catalog/csrc/eager/materialize.h.md), [csrc/eager/events_queue.cc](../catalog/csrc/eager/events_queue.cc.md), [csrc/eager/events_queue.h](../catalog/csrc/eager/events_queue.h.md), [csrc/eager/structured_log_buffer.h](../catalog/csrc/eager/structured_log_buffer.h.md), [csrc/internal/sync/sync.cc](../catalog/csrc/internal/sync/sync.cc.md)
- Related doc-concepts: [eager-execution-modes.md](eager-execution-modes.md), [op-fusion-and-hbm-traffic.md](op-fusion-and-hbm-traffic.md), [graph-fingerprint-and-recompilation.md](graph-fingerprint-and-recompilation.md), [multi-tier-compilation-cache.md](multi-tier-compilation-cache.md)

## Source
Extracted from `docs/markdown/eager_mode.md` (sections 3 and 5) and the DeferAndFuse bullet of `docs/markdown/intro_to_torchtpu.md` (= `docs/markdown/1_basics_1_intro_to_torchtpu.md`) (kept in place).
