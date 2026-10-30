---
title: Graph breaks on TPU - cost, detection, and the backward/optimizer.step trap
type: doc-concept
provenance: doc
source: docs/markdown/advanced_compile.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T02:38:46Z}
---
# Graph breaks on TPU - cost, detection, and the backward/optimizer.step trap

## Definition
A **graph break** happens when TorchDynamo meets Python code, control flow, or a library call it cannot trace into an FX graph; execution falls back to the interpreter and the compiled region is split. The doc gives two TPU-specific costs: (1) **no fusion across the boundary** - XLA cannot fuse ops on either side, so intermediates are written to and re-read from HBM instead of staying on-chip; (2) **dispatch and launch overhead** - each fragment is a separate XLA executable that the host must schedule and dispatch independently.

Detection, per the doc:
1. `torch._dynamo.explain(fn)(*args)` - graph-break count, reasons, and stack traces.
2. `torch.compile(fn, fullgraph=True)` - fail fast with `torch._dynamo.exc.Unsupported` on the first break.
3. `TORCH_LOGS="graph_breaks"` - stream break notifications to stderr.

The common trap: compiling a standard training step (`zero_grad`, forward, loss, `loss.backward()`, `optimizer.step()`) breaks the graph, because Dynamo traces the forward but cannot inline the eager autograd engine or the mutating optimizer update. The doc's fix is to fuse the whole step functionally with [SingleTraceTrainer](single-trace-trainer.md). It also notes that stateful optimizers on TPU should be created with `capturable=True`.

## In torch_tpu (grounded)
- Dynamo hands each fragment to [`TpuBackend.__call__`](../catalog/src/torch_tpu/_internal/compile/_backend.md#TpuBackend.__call__) separately, so N breaks = N+1 compiled programs, each with its own cache entry and launch.
- The backend can also split a graph *itself*: [`SplitCompiler`](../catalog/src/torch_tpu/_internal/compile/split_compiler.md#SplitCompiler) cuts the graph at collectives unless ranks agree (via a [`Handshake`](../catalog/src/torch_tpu/_internal/compile/split_compiler.md#Handshake)) that they produced identical graphs - controlled by [`kTorchTpuSpmdHandshakeStageEnvVar`](../catalog/csrc/common/env_vars.h.md#kTorchTpuSpmdHandshakeStageEnvVar) (`TORCH_TPU_SPMD_HANDSHAKE_STAGE`, default `OFF`), or disabled outright with [`kTorchTpuInternalMaterializeCollectiveTensorsEnvVar`](../catalog/csrc/common/env_vars.h.md#kTorchTpuInternalMaterializeCollectiveTensorsEnvVar) = `0` for SPMD code whose ranks are known to trace identical graphs. These backend splits are not reported by `torch._dynamo.explain`; they show up as separate `_split<N>` modules (named by [`_get_module_name`](../catalog/src/torch_tpu/_internal/compile/_backend.md#_get_module_name)).
- The eager-mode analogue of a graph break is a materialization trigger ([defer-and-fuse-materialization.md](defer-and-fuse-materialization.md)); both cut the fusion window and add a host round-trip.

## Why it matters / when it applies
- Breaks in the hot loop are the first thing to check when compiled step time disappoints: `explain` the step, then drive the count to zero with `fullgraph=True` as the guard.
- Data-dependent Python branches (`if loss.item() > x`) cause a break *and* a device->host sync.
- When a break is unavoidable, place it where the live tensor set is small so the HBM round-trip is cheap.
- Collective-heavy SPMD code can lose fusion to backend-level splits even with zero Dynamo breaks; the handshake env var is the knob.

## Connections
- Code concepts: [torch-compile-backend](../concepts/torch-compile-backend.md), [fx-graph-passes](../concepts/fx-graph-passes.md), [compiled-mode](../concepts/compiled-mode.md), [python-optimizers](../concepts/python-optimizers.md), [process-group-and-collectives](../concepts/process-group-and-collectives.md), [distributed-launchers-and-spmd](../concepts/distributed-launchers-and-spmd.md)
- Module catalogs: [src/torch_tpu/_internal/compile/_backend](../catalog/src/torch_tpu/_internal/compile/_backend.md), [src/torch_tpu/_internal/compile/split_compiler](../catalog/src/torch_tpu/_internal/compile/split_compiler.md), [csrc/common/env_vars.h](../catalog/csrc/common/env_vars.h.md)
- Related doc-concepts: [single-trace-trainer.md](single-trace-trainer.md), [torch-compile-static-shapes-and-bounded-dynamism.md](torch-compile-static-shapes-and-bounded-dynamism.md), [op-fusion-and-hbm-traffic.md](op-fusion-and-hbm-traffic.md), [defer-and-fuse-materialization.md](defer-and-fuse-materialization.md), [host-sync-avoidance-in-training-loops.md](host-sync-avoidance-in-training-loops.md)

## Source
Extracted from `docs/markdown/advanced_compile.md` (sections 2-3) (kept in place).
