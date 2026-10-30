---
title: Global vs local knobs (env vars, properties, flags, context managers)
type: doc-concept
provenance: doc
source: docs/developers/api_design_guide.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T02:38:46Z}
---
# Global vs local knobs (env vars, properties, flags, context managers)

## Definition
The API design guide sorts every TorchTPU behavior control into **global** knobs (process-wide) and **local** knobs (a region of one thread), and fixes how each is exposed, named, read and overridden. First preference is always to reuse an existing PyTorch API (and `torch.accelerator` over `torch.tpu`), so users pay no migration cost. This is the rule set that explains why the perf-relevant TorchTPU controls look the way they do.

## In torch_tpu (grounded)
**Global knobs** must have a Python API, preferably a property; the latest assignment wins.
- Examples: [`allow_excess_precision`](../catalog/src/torch_tpu/_internal/device/_device_module.md#_DeviceModuleMeta.allow_excess_precision) (a `torch.tpu` property that sets XLA's `--allow_excess_precision` for all future compilations via [`SetAllowExcessPrecision`](../catalog/csrc/common/excess_precision.cc.md#SetAllowExcessPrecision "csrc/common/excess_precision.cc:L54"); changing it often forces recompiles) and [`eager_mode`](../catalog/src/torch_tpu/_internal/device/_device_module.md#_DeviceModuleMeta.eager_mode) (the execution-mode property).
- An env var may set the knob's default when ops teams need to change it without touching model code. TorchTPU-introduced vars start with `TORCH_TPU_INTERNAL_` until they are user-facing, then `TORCH_TPU_`. Well-known PyTorch vars (`TORCH_TRACE`, `TORCH_SHOW_CPP_STACKTRACES`) are reused. **When both the env var and the Python API are set, the Python API wins.**
- Env vars are read **once and memoized**: [`GetEnvOnce`](../catalog/csrc/common/env_vars.h.md#GetEnvOnce) (plus typed wrappers [`GetBooleanEnvOnce`](../catalog/csrc/common/env_vars.h.md#GetBooleanEnvOnce) / [`GetIntegerEnvOnce`](../catalog/csrc/common/env_vars.h.md#GetIntegerEnvOnce)). In v0.2.0 it is a template over the variable's name and `static_assert`s that the name is registered in [`kEnvVarToStage`](../catalog/csrc/common/env_vars.h.md#kEnvVarToStage), so an unregistered env var does not compile. Setting a var after its first read does nothing.
- C++ absl flags are only for Google-internal experiments and must be named `torch_tpu_internal_*`. The guide also names a `ReadFlagOnce()` helper for them, but there is no such symbol in the v0.2.0 tree. Python `flags.DEFINE_*` is banned: it crashes client programs that never parse flags.

**Local knobs** are Python context managers scoped to the current thread, and a local knob overrides the matching global one.
- The guide's example is MLIR tracebacks: the internal flag `torch_tpu_internal_mlir_tracebacks` is the global knob, and the [`enable_tracebacks`](../catalog/src/torch_tpu/_internal/export/export.md#enable_tracebacks) context manager (push/pop around the region) overrides it.
- [`custom_compiler_options`](../catalog/src/torch_tpu/_internal/compiler_options/__init__.md#custom_compiler_options) (`torch.tpu.compiler`) is the same pattern for XLA compiler options.

## Why it matters / when it applies
- **Perf experiments:** an env var is snapshotted at its first read. Set `TORCH_TPU_*` vars before the first TPU op (in practice before `import torch` in the launcher), not halfway through a script. A Python property set at run time takes effect for later compilations and overrides the env default.
- **Precedence to remember:** context manager > Python global API > env var default > built-in default.
- Global knobs that feed compilation (precision, compiler options) also feed the compilation cache key, so flipping them causes recompiles ([compilation-cache-key](../concepts/compilation-cache-key.md)).
- Local knobs must follow TorchTPU's context-manager pattern (the C++ side keeps thread-local context states carried in c10's `ThreadLocalDebugInfo`, which background worker threads are barred from touching - see [context-states-and-execution-modes](../concepts/context-states-and-execution-modes.md)). An ad hoc implementation can leak state across threads or exceptions.

## Connections
- Code concepts: [context-states-and-execution-modes](../concepts/context-states-and-execution-modes.md), [dtype-and-precision](../concepts/dtype-and-precision.md), [compilation-pipeline](../concepts/compilation-pipeline.md), [compilation-cache-key](../concepts/compilation-cache-key.md), [error-handling](../concepts/error-handling.md), [op-names-and-python-context](../concepts/op-names-and-python-context.md)
- Module catalogs: [csrc/common/env_vars.h](../catalog/csrc/common/env_vars.h.md), [src/torch_tpu/_internal/device/_device_module](../catalog/src/torch_tpu/_internal/device/_device_module.md), [src/torch_tpu/_internal/compiler_options/__init__](../catalog/src/torch_tpu/_internal/compiler_options/__init__.md), [src/torch_tpu/_internal/export/export](../catalog/src/torch_tpu/_internal/export/export.md)
- Related doc-concepts: [api-lifecycle-stages](api-lifecycle-stages.md), [public-api-paths-and-module-structure](public-api-paths-and-module-structure.md), [gke-single-device-workload-topology](gke-single-device-workload-topology.md), [excess-precision](excess-precision.md), [matmul-precision-modes](matmul-precision-modes.md), [eager-execution-modes](eager-execution-modes.md)

## Source
Extracted from `docs/developers/api_design_guide.md` (the Principles section), which `docs/developers/README.md` lists as a design guideline (both kept in place).
