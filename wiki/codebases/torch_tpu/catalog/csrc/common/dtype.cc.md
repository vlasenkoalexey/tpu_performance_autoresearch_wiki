---
title: 'Module: csrc/common/dtype.cc'
type: catalog
provenance: extracted
module: csrc/common/dtype.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  ToString: ToString(7bd5834298611050).
  ToShortString: ToShortString(7bd5834298611050).
  XlaEquivalentBitwidth: XlaEquivalentBitwidth(313708f09c862f0).
  ToElementType: internal/ToElementType(70f5cf4e07743b5e).
  ToAccumulateType: ToAccumulateType(379c77322858ec4d).
  ValidateTensorByteSize: ValidateTensorByteSize(5acd224945c07724).
  ToScalarType: internal/ToScalarType(7b148b3513bf91f9).
  TorchEquivalentBitwidth: TorchEquivalentBitwidth(313708f09c862f0).
  ToXlaType: internal/ToXlaType(102ba69f2f1a81ef).
  RealComponentOf: RealComponentOf(d1dc85090a11d7e3).
  ToScalarType.ToScalarType: internal/ToScalarType(89fa12ff8220c05a).ToScalarType(7b148b3513bf91f9).
  IsSupportedBufferType: '`$anonymous_namespace_csrc/common/dtype.cc`/IsSupportedBufferType(5cf2926bc1ae4759).'
  ToIntegerElementType: internal/ToIntegerElementType(16659b9218b61cd5).
  GetNegativeValuesIn: '`$anonymous_namespace_csrc/common/dtype.cc`/GetNegativeValuesIn(a4b78b46af57e1b1).'
  JoinBySerialComma: '`$anonymous_namespace_csrc/common/dtype.cc`/JoinBySerialComma(23b83986b497e4d5).'
---
# Module: [`csrc/common/dtype.cc`](../../../../../../raw/code/torch_tpu/csrc/common/dtype.cc)

## Functions
- <a id="GetNegativeValuesIn"></a>`GetNegativeValuesIn(const at::IntArrayRef ints)` — [`L620`](../../../../../../raw/code/torch_tpu/csrc/common/dtype.cc#L620)
- <a id="IsSupportedBufferType"></a>`IsSupportedBufferType(mlir::ElementType type)` — [`L590`](../../../../../../raw/code/torch_tpu/csrc/common/dtype.cc#L590)
- <a id="JoinBySerialComma"></a>`JoinBySerialComma(const Container& container)` — [`L631`](../../../../../../raw/code/torch_tpu/csrc/common/dtype.cc#L631)
- <a id="RealComponentOf"></a>`RealComponentOf(const mlir::ElementType element_type)` — [`L738`](../../../../../../raw/code/torch_tpu/csrc/common/dtype.cc#L738) — Returns the real component type of the input type. — documented in [dtype-and-precision](../../../concepts/dtype-and-precision.md)
- <a id="ToAccumulateType"></a>`ToAccumulateType(at::ScalarType type)` — [`L777`](../../../../../../raw/code/torch_tpu/csrc/common/dtype.cc#L777) — PyTorch uses `at::toAccumulateType` AT_TO_ACCUMULATE_TYPE_OK=doc
- <a id="ToElementType"></a>`ToElementType(const at::ScalarType scalar_type)` — [`L123`](../../../../../../raw/code/torch_tpu/csrc/common/dtype.cc#L123) — Converts to mlir::ElementType. — documented in [dtype-and-precision](../../../concepts/dtype-and-precision.md)
- `ToElementType(mlir::Type type)` — [`L333`](../../../../../../raw/code/torch_tpu/csrc/common/dtype.cc#L333)
- `ToElementType(const xla::PrimitiveType xla_type)` — [`L218`](../../../../../../raw/code/torch_tpu/csrc/common/dtype.cc#L218)
- <a id="ToIntegerElementType"></a>`ToIntegerElementType(mlir::IntegerType int_type)` — [`L311`](../../../../../../raw/code/torch_tpu/csrc/common/dtype.cc#L311)
- `ToScalarType` — [`L483`](../../../../../../raw/code/torch_tpu/csrc/common/dtype.cc#L483)
- `ToScalarType(const mlir::IntegerType int_type)` — [`L445`](../../../../../../raw/code/torch_tpu/csrc/common/dtype.cc#L445)
- <a id="ToScalarType.ToScalarType"></a>`ToScalarType` — [`L483`](../../../../../../raw/code/torch_tpu/csrc/common/dtype.cc#L483)
- `ToScalarType` — [`L483`](../../../../../../raw/code/torch_tpu/csrc/common/dtype.cc#L483)
- `ToScalarType(mlir::Type type)` — [`L482`](../../../../../../raw/code/torch_tpu/csrc/common/dtype.cc#L482)
- `ToScalarType(const mlir::ComplexType complex_type)` — [`L469`](../../../../../../raw/code/torch_tpu/csrc/common/dtype.cc#L469)
- `ToScalarType(const mlir::ComplexType complex_type)` — [`L469`](../../../../../../raw/code/torch_tpu/csrc/common/dtype.cc#L469)
- <a id="ToScalarType"></a>`ToScalarType(const mlir::ElementType element_type)` — [`L378`](../../../../../../raw/code/torch_tpu/csrc/common/dtype.cc#L378) — Converts from mlir::ElementType and mlir::Type. These should never
- `ToScalarType` — [`L483`](../../../../../../raw/code/torch_tpu/csrc/common/dtype.cc#L483)
- <a id="ToShortString"></a>`ToShortString(const mlir::ElementType element_type)` — [`L521`](../../../../../../raw/code/torch_tpu/csrc/common/dtype.cc#L521) — Returns a string representation of the given MLIR element type.
- <a id="ToString"></a>`ToString(const mlir::ElementType element_type)` — [`L517`](../../../../../../raw/code/torch_tpu/csrc/common/dtype.cc#L517) — Returns a string representation of the given type as a PyTorch
- <a id="ToXlaType"></a>`ToXlaType(const mlir::ElementType element_type)` — [`L48`](../../../../../../raw/code/torch_tpu/csrc/common/dtype.cc#L48)
- <a id="TorchEquivalentBitwidth"></a>`TorchEquivalentBitwidth(mlir::ElementType element_type)` — [`L674`](../../../../../../raw/code/torch_tpu/csrc/common/dtype.cc#L674) — Returns the number of bits used to represent the given element type in torch.
- <a id="ValidateTensorByteSize"></a>`ValidateTensorByteSize(at::IntArrayRef size, mlir::ElementType element_type)` — [`L648`](../../../../../../raw/code/torch_tpu/csrc/common/dtype.cc#L648) — Validates that `size` is a valid tensor size, and returns that size in bytes.
- <a id="XlaEquivalentBitwidth"></a>`XlaEquivalentBitwidth(const mlir::ElementType element_type)` — [`L731`](../../../../../../raw/code/torch_tpu/csrc/common/dtype.cc#L731) — Returns the number of bits used to represent the given element type in XLA.

