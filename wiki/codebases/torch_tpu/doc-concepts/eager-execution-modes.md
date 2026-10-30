---
title: Eager execution modes (Strict / DeferAndFuse / Debug)
type: doc-concept
provenance: doc
source: docs/markdown/eager_mode.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T02:38:46Z}
---
# Eager execution modes (Strict / DeferAndFuse / Debug)

## Definition
TorchTPU runs un-compiled PyTorch code in one of three eager modes, chosen by environment variables before the first TPU tensor is touched:

| Mode (doc name) | Env var | Dispatch behavior | Doc's recommended use |
|---|---|---|---|
| Strict eager (default) | neither var set, or `"0"` | one ATen op at a time, launched asynchronously on the device stream | interactive prototyping, CPU/GPU drop-in parity |
| Fused eager / DeferAndFuse | `TORCH_TPU_DEFER_AND_FUSE=1` | ops are recorded and compiled as fused multi-op XLA clusters at the next materialization point | high-throughput eager training and inference |
| Debug eager | `TORCH_TPU_LAUNCH_BLOCKING=1` | one op at a time, host synchronizes after every op, bounds checking on | pinpointing NaNs / runtime crashes (the TPU analogue of `CUDA_LAUNCH_BLOCKING=1`) |

The docs add a fourth rung above eager: `torch.compile(model, backend="tpu")` for whole-graph production serving and peak throughput (see [torch-compile-static-shapes-and-bounded-dynamism.md](torch-compile-static-shapes-and-bounded-dynamism.md)).

## In torch_tpu (grounded)
- The env-var names are the constants [`kTorchTpuDeferAndFuseEnvVar`](../catalog/csrc/common/env_vars.h.md#kTorchTpuDeferAndFuseEnvVar) and [`kTorchTpuLaunchBlockingEnvVar`](../catalog/csrc/common/env_vars.h.md#kTorchTpuLaunchBlockingEnvVar). Debug mode also turns on the expensive checks controlled by [`kTorchTpuEnableDebugChecksEnvVar`](../catalog/csrc/common/env_vars.h.md#kTorchTpuEnableDebugChecksEnvVar) (`TORCH_TPU_ENABLE_DEBUG_CHECKS`), which can be set to `"0"` to keep debug-mode synchronization without the checks.
- [`GetDefaultEagerMode`](../catalog/csrc/eager/eager_mode.cc.md#GetDefaultEagerMode) reads the two variables once and memoizes the result. `TORCH_TPU_LAUNCH_BLOCKING` is checked first, so it **wins** if both are set; otherwise `TORCH_TPU_DEFER_AND_FUSE` selects `kDeferAndFuse`, else `kDeferNever` (the doc's "Strict"). This memoization is why the doc insists the variables be set before device initialization.
- The global mode is held by [`SetEagerMode`](../catalog/csrc/eager/eager_mode.cc.md#SetEagerMode) / [`GetEagerMode`](../catalog/csrc/eager/eager_mode.cc.md#GetEagerMode); `GetEagerMode` first consults a scoped [`EagerModeContextState`](../catalog/csrc/common/context_states.h.md#EagerModeContextState), so a context manager can override the process-wide mode. [`IsDeferNeverMode`](../catalog/csrc/eager/eager_mode.h.md#IsDeferNeverMode) groups Strict and Debug together.
- Python exposes the same switch beyond what the doc shows: the experimental enum [`EagerMode`](../catalog/src/torch_tpu/_internal/execution_mode/__init__.md#EagerMode) (`DEFER_AND_FUSE`, `DEFER_NEVER`, `DEFER_NEVER_AND_LAUNCH_BLOCKING`) and the module property on [`_ExecutionModeModule`](../catalog/src/torch_tpu/_internal/execution_mode/__init__.md#_ExecutionModeModule), which also carries `enable_cpu_fallback` and [`disable_inplace_buffer_donation`](../catalog/src/torch_tpu/_internal/execution_mode/__init__.md#_ExecutionModeModule.disable_inplace_buffer_donation).
- **Mode -> XLA compile effort (not in the doc).** [`GetCompilationMode`](../catalog/csrc/eager/events_queue.cc.md#GetCompilationMode) maps DeferAndFuse (and the compiled-FX-graph mode) to [`CompilationMode`](../catalog/csrc/common/compilation_spec.h.md#CompilationMode) `kFastRuntime` ("more optimized executables, but with longer compile"), and Strict/Debug to `kFastCompile` ("reduces compile time, but may result in slower execution"). So switching modes changes not only the size of each compiled program but also how hard XLA optimizes it.

## Why it matters / when it applies
- Strict eager pays one dispatch + one (cached) single-op executable per ATen op, with every intermediate written to HBM; DeferAndFuse amortizes dispatch and lets XLA fuse across ops (mechanism in [defer-and-fuse-materialization.md](defer-and-fuse-materialization.md)).
- Debug eager serializes the host with the device after every op - useful for exact stack traces, but never a perf configuration.
- The doc's benchmark compares a 10x `(y + 1) * 2 - 0.5` chain under DeferAndFuse vs `torch.compile(backend="tpu")` and reports the ratio as "x of compiled peak": fused eager narrows the gap to compiled mode without changing the eager workflow, while `torch.compile` remains the recommended path for whole forward+backward optimization.
- Because the default is memoized at first use, setting the env var after any TPU work has started is a silent no-op for the default mode (use the Python `eager_mode` property instead).

## Connections
- Code concepts: [context-states-and-execution-modes](../concepts/context-states-and-execution-modes.md), [deferred-execution-and-materialization](../concepts/deferred-execution-and-materialization.md), [eager-op-dispatch](../concepts/eager-op-dispatch.md), [compilation-pipeline](../concepts/compilation-pipeline.md), [compiled-mode](../concepts/compiled-mode.md), [error-handling](../concepts/error-handling.md)
- Module catalogs: [csrc/eager/eager_mode.cc](../catalog/csrc/eager/eager_mode.cc.md), [csrc/common/env_vars.h](../catalog/csrc/common/env_vars.h.md), [csrc/eager/events_queue.cc](../catalog/csrc/eager/events_queue.cc.md), [src/torch_tpu/_internal/execution_mode/__init__](../catalog/src/torch_tpu/_internal/execution_mode/__init__.md)
- Related doc-concepts: [defer-and-fuse-materialization.md](defer-and-fuse-materialization.md), [torch-tpu-architecture-and-lowering-stack.md](torch-tpu-architecture-and-lowering-stack.md), [op-fusion-and-hbm-traffic.md](op-fusion-and-hbm-traffic.md), [torch-compile-static-shapes-and-bounded-dynamism.md](torch-compile-static-shapes-and-bounded-dynamism.md)

## Source
Extracted from `docs/markdown/eager_mode.md` and the "Three eager execution modes" section of `docs/markdown/intro_to_torchtpu.md` (byte-identical copy: `docs/markdown/1_basics_1_intro_to_torchtpu.md`) (kept in place).
