---
title: Common TorchTPU failure patterns (glossary)
type: doc-concept
provenance: doc
source: docs/markdown/error_glossary.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T02:38:46Z}
---
# Common TorchTPU failure patterns (glossary)

## Definition
The error-glossary doc catalogs four recurring failure shapes with live repro cells: shape mismatch
and dtype mismatch (both reported when the deferred op is lowered / materialized), the
`torch.compile` + `@torch.inference_mode` crash, and the silent `DataLoader(num_workers > 0)` hang
after the PJRT client is initialized.

## In torch_tpu (grounded)
| Pattern | Symptom | Cause (doc) | Fix (doc) | Code anchor |
|---|---|---|---|---|
| Shape mismatch | `RuntimeError` at `c.cpu()`, not at `a @ b` | StableHLO lowering rejects incompatible dims; the op was recorded, the error surfaces at materialization | match inner dims | lowering through the [StableHLO op builder](../concepts/stablehlo-op-builder.md); delivery via [`SyncAndCheckStickyError`](../catalog/csrc/common/error_utils.cc.md#SyncAndCheckStickyError "csrc/common/error_utils.cc:L972") for async errors |
| dtype mismatch | `torch.mm(float32, int64)` fails | mm needs matching dtypes | cast first (`.to(torch.float32)`) | [dtype-and-precision](../concepts/dtype-and-precision.md) |
| `inference_mode` + `torch.compile` | crash / INTERNAL ASSERT; can corrupt the dispatcher for the process | inference tensors lack the version counters AOTAutograd/Dynamo need | use `@torch.no_grad()` | [torch-compile-backend](../concepts/torch-compile-backend.md) |
| DataLoader fork deadlock | workers hang before step 0, no exception | default `fork` after PJRT init duplicates multithreaded runtime state and the `/tmp/libtpu_lockfile` handle | `num_workers=0`, or Grain for async multi-worker input | PJRT init in [`PjrtBackend::EnsureInitialized`](../catalog/csrc/pjrt/pjrt_state.cc.md#PjrtBackend.EnsureInitialized) |

## Why it matters / when it applies
- **Deferred error location.** Because ops are recorded and executed asynchronously, the Python line
  in the traceback is the sync point. Use debug eager to move it to the culprit
  ([tpu-debugging-ladder](tpu-debugging-ladder.md)).
- **Perf lens - input pipeline.** The `num_workers=0` workaround puts data loading on the training
  thread, which shows up as large gaps between TPU ops in xprof
  ([trace-red-flags](trace-red-flags.md)). For throughput work, the doc's recommendation is Grain
  (or a pipeline started before / outside the PJRT-owning process), not forking workers.
- **Perf lens - inference.** Replacing `inference_mode` with `no_grad` is required to compile at all
  under the TPU backend; it is not a perf regression in itself.

## Connections
- Code concepts: [error-handling](../concepts/error-handling.md),
  [deferred-execution-and-materialization](../concepts/deferred-execution-and-materialization.md),
  [pjrt-client](../concepts/pjrt-client.md),
  [torch-compile-backend](../concepts/torch-compile-backend.md),
  [stablehlo-op-builder](../concepts/stablehlo-op-builder.md)
- Module catalogs: [csrc/common/error_utils.cc](../catalog/csrc/common/error_utils.cc.md),
  [csrc/pjrt/pjrt_state.cc](../catalog/csrc/pjrt/pjrt_state.cc.md)
- Related doc-concepts: [graph-breaks-on-tpu](graph-breaks-on-tpu.md), [eager-execution-modes](eager-execution-modes.md), [tpu-error-anatomy](tpu-error-anatomy.md),
  [tpu-debugging-ladder](tpu-debugging-ladder.md), [trace-red-flags](trace-red-flags.md)

## Source
Extracted from `docs/markdown/error_glossary.md` and its byte-identical duplicate
`docs/markdown/4_debugging_and_performance_analysis_3_getting_better_error_information.md` (both kept in place).
