---
title: Excess precision (torch.tpu.allow_excess_precision)
type: doc-concept
provenance: doc
source: docs/markdown/precision_management.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T02:38:46Z}
---
# Excess precision (torch.tpu.allow_excess_precision)

## Definition
Because the MXU accumulates bf16 matmuls in `float32`, XLA can keep intermediate values of a fused
computation in `float32` instead of rounding them to `bfloat16` between steps. Retaining those extra
bits is *excess precision*. TorchTPU exposes it as the process-global, experimental property
`torch.tpu.allow_excess_precision`, which drives XLA's `xla_allow_excess_precision` debug option.
**TorchTPU's default is `False`** (keep the intermediate downcasts), unlike XLA's own default of
`True`.

## In torch_tpu (grounded)
- **Python property.** [`_DeviceModuleMeta.allow_excess_precision`](../catalog/src/torch_tpu/_internal/device/_device_module.md#_DeviceModuleMeta.allow_excess_precision)
  (owning module `src/torch_tpu/_internal/device/_device_module.py`) forwards to the C++ getter /
  setter bound in `csrc/internal/device/device_rt.cc`.
- **State.** [`SetAllowExcessPrecision`](../catalog/csrc/common/excess_precision.cc.md#SetAllowExcessPrecision "csrc/common/excess_precision.cc:L54")
  stores an explicit allow/disallow; [`GetAllowExcessPrecision`](../catalog/csrc/common/excess_precision.cc.md#GetAllowExcessPrecision)
  returns it, or - when never set - checks whether the literal string `xla_allow_excess_precision`
  appears in `XLA_FLAGS` (memoized) and only then honours XLA's parsed value; otherwise `false`.
  The string check exists because `xla::DebugOptions` always reports a value (default `true`), so a
  user-set flag cannot be distinguished from XLA's default.
- **Applied at compile time.** `UpdateFromXlaFlags` in `csrc/common/compilation.cc` writes
  `GetAllowExcessPrecision()` into every compile's `debug_options`, and the value is folded into the
  executable-build-options fingerprint that feeds
  [`MakeCompileOptionsKey`](../catalog/csrc/common/compilation.cc.md#MakeCompileOptionsKey "csrc/common/compilation.cc:L441").
  Flipping the property therefore changes the compile-options key and forces recompilation of
  every subsequent graph.

## Why it matters / when it applies
- Set it **once, at the start of the script**, before any op runs or compiles. The doc warns that
  changing it mid-session forces recompiles, and that the TPU XLA runtime can latch the option on
  the first compilation of the session and ignore later changes (the doc's bitwise test prints a
  WARNING for exactly this case).
- Eager single-op execution never benefits: each op's output is materialized in its declared dtype.
  Excess precision only shows up inside fused graphs, i.e. under `torch.compile(backend="tpu")` or
  deferred/fused eager.
- Perf lens: `True` lets XLA elide `convert` round-trips between fused ops (fewer VPU ops, possibly
  better fusion); `False` gives bitwise-closer parity with a bf16 reference. When comparing a
  torch_tpu run to a JAX/MaxText run on the same model, remember the two stacks default this flag
  differently. A setting in `XLA_FLAGS` is also part of the compile cache key (the whole `XLA_FLAGS`
  string is fingerprinted).

## Connections
- Code concepts: [dtype-and-precision](../concepts/dtype-and-precision.md),
  [compilation-pipeline](../concepts/compilation-pipeline.md),
  [compilation-cache-key](../concepts/compilation-cache-key.md),
  [torch-compile-backend](../concepts/torch-compile-backend.md)
- Module catalogs: [csrc/common/excess_precision.cc](../catalog/csrc/common/excess_precision.cc.md),
  [csrc/common/compilation.cc](../catalog/csrc/common/compilation.cc.md),
  [src/torch_tpu/_internal/device/_device_module](../catalog/src/torch_tpu/_internal/device/_device_module.md)
- Related doc-concepts: [global-and-local-knobs](global-and-local-knobs.md), [graph-fingerprint-and-recompilation](graph-fingerprint-and-recompilation.md), [mxu-bf16-arithmetic](mxu-bf16-arithmetic.md),
  [matmul-precision-modes](matmul-precision-modes.md),
  [environment-variables](environment-variables.md)

## Source
Extracted from `docs/markdown/precision_management.md` (kept in place).
