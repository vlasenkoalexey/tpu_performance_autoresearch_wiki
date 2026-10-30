---
title: 'Module: csrc/common/dtype.h'
type: catalog
provenance: extracted
module: csrc/common/dtype.h
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  ConvertTo: ConvertTo(75a19c6c3d0e5b5d).
  IsValidElemType.value: internal/IsValidElemType#value.
  Fingerprint64Impl.Compute: internal/Fingerprint64Impl#Compute(e8cf76919fb10dbb).
  IsValidElemType: internal/IsValidElemType#
---
# Module: [`csrc/common/dtype.h`](../../../../../../raw/code/torch_tpu/csrc/common/dtype.h)

## Classes
### <a id="IsValidElemType"></a>`IsValidElemType`
- def: [`csrc/common/dtype.h:68`](../../../../../../raw/code/torch_tpu/csrc/common/dtype.h#L68) — documented in [dtype-and-precision](../../../concepts/dtype-and-precision.md)
- doc: Trait for checking whether a type is one of the supported types for
- signature: `template <typename ToType> struct IsValidElemType`
- members:
  - <a id="IsValidElemType.value"></a>`value` — [`L69`](../../../../../../raw/code/torch_tpu/csrc/common/dtype.h#L69)
- uses (calls/refs, reference-scoped): [`ToElementType`](dtype.cc.md#ToElementType), [`ToElementType`](dtype.cc.md#ToElementType), [`ToElementType`](dtype.cc.md#ToElementType), [`ToScalarType`](dtype.cc.md#ToScalarType), [`ToXlaType`](dtype.cc.md#ToXlaType), [`ToScalarType`](dtype.cc.md#ToScalarType)
- used by: [`ConvertTo`](dtype.h.md#ConvertTo), [`ConvertTo`](dtype.h.md#ConvertTo), [`ConvertTo`](dtype.h.md#ConvertTo)

## Functions
- `ConvertTo(xla::PrimitiveType xla_type)` — [`L112`](../../../../../../raw/code/torch_tpu/csrc/common/dtype.h#L112)
- `ConvertTo(mlir::Type mlir_type)` — [`L118`](../../../../../../raw/code/torch_tpu/csrc/common/dtype.h#L118)
- <a id="ConvertTo"></a>`ConvertTo(at::ScalarType scalar_type)` — [`L106`](../../../../../../raw/code/torch_tpu/csrc/common/dtype.h#L106) — documented in [dtype-and-precision](../../../concepts/dtype-and-precision.md)
- `ConvertTo(mlir::ElementType element_type)` — [`L95`](../../../../../../raw/code/torch_tpu/csrc/common/dtype.h#L95) — Converts an arbitrary element type to another arbitrary element type.

## Other members
- <a id="Fingerprint64Impl.Compute"></a>`Fingerprint64Impl.Compute` — [`L159`](../../../../../../raw/code/torch_tpu/csrc/common/dtype.h#L159)

