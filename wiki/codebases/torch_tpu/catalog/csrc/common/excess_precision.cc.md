---
title: 'Module: csrc/common/excess_precision.cc'
type: catalog
provenance: extracted
module: csrc/common/excess_precision.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  GetAllowExcessPrecision: GetAllowExcessPrecision(c9857a73d68e59ba).
  GetDefaultExecutableBuildOptions: GetDefaultExecutableBuildOptions(d338352e4681dfa9).
  SetAllowExcessPrecision: SetAllowExcessPrecision(b45ddcbc8423892c).
  g_allow_excess_precision: '`$anonymous_namespace_csrc/common/excess_precision.cc`/g_allow_excess_precision.'
  ExcessPrecisionState: '`$anonymous_namespace_csrc/common/excess_precision.cc`/ExcessPrecisionState#'
  ExcessPrecisionState.kDisallow: '`$anonymous_namespace_csrc/common/excess_precision.cc`/ExcessPrecisionState#kDisallow.'
  ExcessPrecisionState.kUnset: '`$anonymous_namespace_csrc/common/excess_precision.cc`/ExcessPrecisionState#kUnset.'
  ExcessPrecisionState.kAllow: '`$anonymous_namespace_csrc/common/excess_precision.cc`/ExcessPrecisionState#kAllow.'
---
# Module: [`csrc/common/excess_precision.cc`](../../../../../../raw/code/torch_tpu/csrc/common/excess_precision.cc)

## Classes
### <a id="ExcessPrecisionState"></a>`ExcessPrecisionState`
- def: [`csrc/common/excess_precision.cc:29`](../../../../../../raw/code/torch_tpu/csrc/common/excess_precision.cc#L29)
- signature: `enum class ExcessPrecisionState`
- members:
  - <a id="ExcessPrecisionState.kAllow"></a>`kAllow` — [`L33`](../../../../../../raw/code/torch_tpu/csrc/common/excess_precision.cc#L33) — Explicitly allow excess precision.
  - <a id="ExcessPrecisionState.kDisallow"></a>`kDisallow` — [`L35`](../../../../../../raw/code/torch_tpu/csrc/common/excess_precision.cc#L35) — Explicitly disallow excess precision.
  - <a id="ExcessPrecisionState.kUnset"></a>`kUnset` — [`L31`](../../../../../../raw/code/torch_tpu/csrc/common/excess_precision.cc#L31) — Use XLA_FLAGS or fall back to the default.
- used by: [`GetAllowExcessPrecision`](excess_precision.cc.md#GetAllowExcessPrecision), [`SetAllowExcessPrecision`](excess_precision.cc.md#SetAllowExcessPrecision), [`g_allow_excess_precision`](excess_precision.cc.md#g_allow_excess_precision)

## Functions
- <a id="GetAllowExcessPrecision"></a>`GetAllowExcessPrecision()` — [`L59`](../../../../../../raw/code/torch_tpu/csrc/common/excess_precision.cc#L59) — Returns whether XLA is allowed to use excess precision for all compilations.
- <a id="GetDefaultExecutableBuildOptions"></a>`GetDefaultExecutableBuildOptions()` — [`L43`](../../../../../../raw/code/torch_tpu/csrc/common/excess_precision.cc#L43) — Returns the cached default `xla::ExecutableBuildOptions` instance.
- <a id="SetAllowExcessPrecision"></a>`SetAllowExcessPrecision(bool allow)` — [`L54`](../../../../../../raw/code/torch_tpu/csrc/common/excess_precision.cc#L54) — Sets whether XLA is allowed to use excess precision for all compilations. — documented in [dtype-and-precision](../../../concepts/dtype-and-precision.md)

## Module values
- <a id="g_allow_excess_precision"></a>`g_allow_excess_precision` — [`L38`](../../../../../../raw/code/torch_tpu/csrc/common/excess_precision.cc#L38)

