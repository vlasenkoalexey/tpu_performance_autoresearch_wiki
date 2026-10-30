---
title: API lifecycle stages (internal / experimental / stable / deprecated)
type: doc-concept
provenance: doc
source: docs/developers/api_policy.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T02:38:46Z}
---
# API lifecycle stages (internal / experimental / stable / deprecated)

## Definition
TorchTPU's API policy extends PyTorch's: "the best API is no API". Implement the existing PyTorch API for TPU whenever one fits, and when a new one is unavoidable, start it **internal** (unstable, users told not to touch it), possibly promote it to **experimental** (usable, may change or vanish, migration guide only), then **stable** (backward-incompatible changes need deprecation). **Deprecated** APIs keep their stable names but warn, and may be removed no earlier than 2 minor releases later. The design principle is that moving between experimental, stable and deprecated never requires user code to change; only the warnings do.

## In torch_tpu (grounded)
Each kind of symbol carries its stage in a machine-readable way:

| Symbol kind | Internal | Experimental / stable / deprecated |
|---|---|---|
| Env var | `TORCH_TPU_INTERNAL_*` | `TORCH_TPU_*` registered in [`kEnvVarToStage`](../catalog/csrc/common/env_vars.h.md#kEnvVarToStage) with a [`SymbolStage`](../catalog/csrc/common/symbol_stage.h.md#SymbolStage) |
| C++ flag | always internal, `torch_tpu_internal_*` | not allowed |
| Python function / class | leading `_` | [`experimental`](../catalog/src/torch_tpu/_internal/utils/annotations.md#experimental "src/torch_tpu/_internal/utils/annotations.py:L339") / [`stable`](../catalog/src/torch_tpu/_internal/utils/annotations.md#stable "src/torch_tpu/_internal/utils/annotations.py:L362") / [`deprecated`](../catalog/src/torch_tpu/_internal/utils/annotations.md#deprecated "src/torch_tpu/_internal/utils/annotations.py:L380") decorators |
| Python attribute / enum constant | leading `_` | entry in the module's `__tt_api_stages__` |
| Custom op in `torch.ops.tpu` | leading `_` + [`ImplInternal`](../catalog/csrc/eager/tpu_aten_kernels.cc.md#ImplInternal) | [`ImplExperimental`](../catalog/csrc/eager/tpu_aten_kernels.cc.md#ImplExperimental) / [`ImplStable`](../catalog/csrc/eager/tpu_aten_kernels.cc.md#ImplStable "csrc/eager/tpu_aten_kernels.cc:L249") / [`ImplDeprecated`](../catalog/csrc/eager/tpu_aten_kernels.cc.md#ImplDeprecated) |

How it is enforced in v0.2.0:
- [`GetEnvOnce`](../catalog/csrc/common/env_vars.h.md#GetEnvOnce) `static_assert`s registration and warns once when an experimental or deprecated env var is set. The C++ stage also splits "internal" into `InternalImplementation` (vars TorchTPU only *writes*, e.g. ones exported for libtpu - reading them is a compile error) and `InternalApi` (internal control knobs). Some upstream vars (`WORLD_SIZE`, `RANK`, `LIBTPU_INIT_ARGS`, `TPU_VISIBLE_DEVICES`) are deliberately marked `Stable`; `XLA_FLAGS` is `Experimental`, so setting it triggers the one-time warning.
- `ImplStable` is a plain `m.impl`. `ImplInternal` `static_assert`s a leading `_`. `ImplExperimental` / `ImplDeprecated` wrap the kernel with an on-entry `TT_WARN_ONCE`, templated on the op name so each op warns once (not once per program).
- The Python decorators route through [`_annotate_target`](../catalog/src/torch_tpu/_internal/utils/annotations.md#_annotate_target "src/torch_tpu/_internal/utils/annotations.py:L277"), attaching stage metadata ([`Stage`](../catalog/src/torch_tpu/_internal/utils/annotations.md#Stage "src/torch_tpu/_internal/utils/annotations.py:L104")) and a once-per-process warning wrapper; calls from inside the framework are recognized ([`_is_framework_caller_frame`](../catalog/src/torch_tpu/_internal/utils/annotations.md#_is_framework_caller_frame "src/torch_tpu/_internal/utils/annotations.py:L80")) so only user calls warn. Example: [`allow_excess_precision`](../catalog/src/torch_tpu/_internal/device/_device_module.md#_DeviceModuleMeta.allow_excess_precision) is `@experimental`.
- `docs/markdown/public_apis.md` is generated from these annotations and a test fails when it is stale. User docs must not mention internal APIs.

## Why it matters / when it applies
- **Reading warnings in a perf run:** an "is experimental" or "is deprecated" warning is a stage notice, not a fault. But many of the strongest perf levers (`eager_mode`, `allow_excess_precision`, `custom_compiler_options`, ragged ops) are experimental and may change between releases. Pin the torch_tpu version in experiment pages.
- **`TORCH_TPU_INTERNAL_*` knobs** (e.g. `TORCH_TPU_INTERNAL_XLA_OPTIONS`, `TORCH_TPU_INTERNAL_SKINNY_SC_OFFLOAD`, `TORCH_TPU_INTERNAL_TIER3_COMPILATION_CACHE_LOCAL_BACKUP_TASK`) are unsupported by policy: fine for experiments, but a win that depends on one is fragile until the knob graduates.
- Promotions keep the name (only the warning changes), so an experiment's flags stay valid when a knob goes experimental -> stable.

## Connections
- Code concepts: [aten-kernel-authoring](../concepts/aten-kernel-authoring.md), [eager-op-dispatch](../concepts/eager-op-dispatch.md), [error-handling](../concepts/error-handling.md), [python-ops](../concepts/python-ops.md), [dtype-and-precision](../concepts/dtype-and-precision.md)
- Module catalogs: [csrc/common/env_vars.h](../catalog/csrc/common/env_vars.h.md), [csrc/common/symbol_stage.h](../catalog/csrc/common/symbol_stage.h.md), [csrc/eager/tpu_aten_kernels.cc](../catalog/csrc/eager/tpu_aten_kernels.cc.md), [src/torch_tpu/_internal/utils/annotations](../catalog/src/torch_tpu/_internal/utils/annotations.md)
- Related doc-concepts: [global-and-local-knobs](global-and-local-knobs.md), [public-api-paths-and-module-structure](public-api-paths-and-module-structure.md)

## Source
Extracted from `docs/developers/api_policy.md`, which `docs/developers/README.md` lists as a design guideline (both kept in place).
