---
title: TorchTPU debugging ladder and debug eager (TORCH_TPU_LAUNCH_BLOCKING)
type: doc-concept
provenance: doc
source: docs/markdown/error_glossary.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T02:38:46Z}
---
# TorchTPU debugging ladder and debug eager (TORCH_TPU_LAUNCH_BLOCKING)

## Definition
The error-glossary doc orders TorchTPU's diagnostics into five escalating levels, each costing more
runtime than the last:

| Level | Add | How |
|---|---|---|
| 1 | Python traceback | always on |
| 2 | C++ error trace + captured traceback | `TORCH_SHOW_CPP_STACKTRACES=1` |
| 3 | ATen op audit (CPU fallbacks) | `torch.profiler` with `ProfilerActivity.CPU` |
| 4 | HLO / LLO dumps | `XLA_FLAGS`, `LIBTPU_INIT_ARGS` |
| 5 | Synchronous "debug eager" | `TORCH_TPU_LAUNCH_BLOCKING=1` (or `torch.accelerator.synchronize()` after each op) |

Level 5 exists because ops are dispatched asynchronously: an error (shape mismatch at lowering, a
device assertion, OOM) is reported at the next materialization point such as `.cpu()`, not on the
line that caused it. Debug eager makes each op complete before the next is dispatched, so the
error lands on the culprit line - useful for OOM attribution and NaN/Inf hunting, and much slower.

## In torch_tpu (grounded)
- **Eager modes.** [`EagerMode`](../catalog/csrc/common/context_states.h.md#EagerMode) (owning
  module `csrc/common/context_states.h`) defines `kDeferAndFuse` (defer and fuse; the fast eager
  mode), `kDeferNever` (execute each op immediately, like CUDA eager), `kDeferNeverAndLaunchBlocking`
  (execute immediately **and** wait for each op's compilation before dispatching the next, with
  extra runtime checks - "worst execution performance") plus two internal modes.
- **Env selection, once.** The startup default is computed and memoized in `GetDefaultEagerMode`
  (`csrc/eager/eager_mode.cc`): [`kTorchTpuLaunchBlockingEnvVar`](../catalog/csrc/common/env_vars.h.md#kTorchTpuLaunchBlockingEnvVar)
  true -> `kDeferNeverAndLaunchBlocking`; else
  [`kTorchTpuDeferAndFuseEnvVar`](../catalog/csrc/common/env_vars.h.md#kTorchTpuDeferAndFuseEnvVar)
  true -> `kDeferAndFuse`; else `kDeferNever`. At runtime
  [`SetEagerMode`](../catalog/csrc/eager/eager_mode.cc.md#SetEagerMode) /
  [`GetEagerMode`](../catalog/csrc/eager/eager_mode.cc.md#GetEagerMode) (Python:
  `torch.tpu.eager_mode`) override it, and a context-manager state takes precedence over the global.
- **Debug checks ride along.** [`GetEnableDebugChecks`](../catalog/csrc/common/error_utils.cc.md#GetEnableDebugChecks)
  honours `TORCH_TPU_ENABLE_DEBUG_CHECKS` when set, and otherwise turns the expensive checks on
  exactly when the mode is `kDeferNeverAndLaunchBlocking` - so level 5 also enables e.g. index
  bounds validation. Set `TORCH_TPU_ENABLE_DEBUG_CHECKS=0` to get blocking without the checks.
- **Deferred error delivery.** Asynchronously detected errors are latched by
  [`SetStickyError`](../catalog/csrc/common/error_utils.cc.md#SetStickyError "csrc/common/error_utils.cc:L935")
  and thrown at the next [`SyncAndCheckStickyError`](../catalog/csrc/common/error_utils.cc.md#SyncAndCheckStickyError "csrc/common/error_utils.cc:L972").

## Why it matters / when it applies
- Never benchmark with level 4 or 5 enabled: dumps add compile-time I/O, debug eager serializes
  compile and execution, and debug checks add host-device syncs.
- Conversely, a perf regression that disappears under `TORCH_TPU_LAUNCH_BLOCKING=1` is a hint the
  original issue is overlap/async related, not a kernel cost.
- The eager mode is a first-order perf knob: `kDeferAndFuse` (`TORCH_TPU_DEFER_AND_FUSE=1` or
  `torch.tpu.eager_mode`) batches ops into larger compiled graphs, while `kDeferNever` compiles and
  runs per op.
- Graph breaks: `torch._dynamo.explain(model)(input)` and `TORCH_LOGS="+dynamo"`.

## Connections
- Code concepts: [context-states-and-execution-modes](../concepts/context-states-and-execution-modes.md),
  [deferred-execution-and-materialization](../concepts/deferred-execution-and-materialization.md),
  [error-handling](../concepts/error-handling.md),
  [tensor-synchronization](../concepts/tensor-synchronization.md),
  [profiler](../concepts/profiler.md)
- Module catalogs: [csrc/common/context_states.h](../catalog/csrc/common/context_states.h.md),
  [csrc/eager/eager_mode.cc](../catalog/csrc/eager/eager_mode.cc.md),
  [csrc/common/error_utils.cc](../catalog/csrc/common/error_utils.cc.md),
  [csrc/common/env_vars.h](../catalog/csrc/common/env_vars.h.md)
- Related doc-concepts: [eager-execution-modes](eager-execution-modes.md), [defer-and-fuse-materialization](defer-and-fuse-materialization.md), [graph-breaks-on-tpu](graph-breaks-on-tpu.md), [tpu-error-anatomy](tpu-error-anatomy.md),
  [tpu-common-failure-patterns](tpu-common-failure-patterns.md),
  [hlo-and-llo-compilation-dumps](hlo-and-llo-compilation-dumps.md), [trace-red-flags](trace-red-flags.md),
  [environment-variables](environment-variables.md)

## Source
Extracted from `docs/markdown/error_glossary.md` and its byte-identical duplicate
`docs/markdown/4_debugging_and_performance_analysis_3_getting_better_error_information.md` (both kept in place).
