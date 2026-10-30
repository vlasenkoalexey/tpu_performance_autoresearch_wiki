---
title: 'Module: csrc/ops/view_decomposition/bitcast_primitive.cc'
type: catalog
provenance: extracted
module: csrc/ops/view_decomposition/bitcast_primitive.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  operator: '`operator<<`(606f24749e46772).'
  ViewPrimitiveShlo: ViewPrimitiveShlo(caa8c0574e137584).
  UpdateLayout: UpdateLayout(f1b5a3cc32e84977).
  CheckStridesAreDivisible: '`$anonymous_namespace_csrc/ops/view_decomposition/bitcast_primitive.cc`/CheckStridesAreDivisible(ca1e36730278ef8e).'
  GetShapeAfterRealToRealBitcast: '`$anonymous_namespace_csrc/ops/view_decomposition/bitcast_primitive.cc`/GetShapeAfterRealToRealBitcast(93b7ced78989a330).'
  ToString: ToString(435822571a801be9).
  GetStorageOffsetAfterRealToRealBitcast: '`$anonymous_namespace_csrc/ops/view_decomposition/bitcast_primitive.cc`/GetStorageOffsetAfterRealToRealBitcast(507af7fcff374d18).'
  GetStridesAfterRealToRealBitcast: '`$anonymous_namespace_csrc/ops/view_decomposition/bitcast_primitive.cc`/GetStridesAfterRealToRealBitcast(dd1816c685b9b384).'
  CheckConversionBitwidthsAreDivisible: '`$anonymous_namespace_csrc/ops/view_decomposition/bitcast_primitive.cc`/CheckConversionBitwidthsAreDivisible(7fab7076b820a08e).'
  CheckBitcastTypesAreNotComplex: '`$anonymous_namespace_csrc/ops/view_decomposition/bitcast_primitive.cc`/CheckBitcastTypesAreNotComplex(5a1282a4a1907afc).'
  BitcastBitwidth.to: '`$anonymous_namespace_csrc/ops/view_decomposition/bitcast_primitive.cc`/BitcastBitwidth#to.'
  ViewAsRealShlo: '`$anonymous_namespace_csrc/ops/view_decomposition/bitcast_primitive.cc`/ViewAsRealShlo(a7867b6222e713f9).'
  BitcastBitwidth.from: '`$anonymous_namespace_csrc/ops/view_decomposition/bitcast_primitive.cc`/BitcastBitwidth#from.'
  GetBitcastBitwidth: '`$anonymous_namespace_csrc/ops/view_decomposition/bitcast_primitive.cc`/GetBitcastBitwidth(19327530f9300f2c).'
  BitcastBitwidth: '`$anonymous_namespace_csrc/ops/view_decomposition/bitcast_primitive.cc`/BitcastBitwidth#'
---
# Module: [`csrc/ops/view_decomposition/bitcast_primitive.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/bitcast_primitive.cc)

## Classes
### <a id="BitcastBitwidth"></a>`BitcastBitwidth`
- def: [`csrc/ops/view_decomposition/bitcast_primitive.cc:45`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/bitcast_primitive.cc#L45)
- doc: Bitwidth of bitcast types.
- signature: `struct BitcastBitwidth`
- members:
  - <a id="BitcastBitwidth.from"></a>`from` — [`L46`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/bitcast_primitive.cc#L46)
  - <a id="BitcastBitwidth.to"></a>`to` — [`L47`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/bitcast_primitive.cc#L47)
- used by: [`ViewPrimitiveShlo`](bitcast_primitive.cc.md#ViewPrimitiveShlo), [`UpdateLayout`](bitcast_primitive.cc.md#UpdateLayout), [`GetShapeAfterRealToRealBitcast`](bitcast_primitive.cc.md#GetShapeAfterRealToRealBitcast), [`GetStorageOffsetAfterRealToRealBitcast`](bitcast_primitive.cc.md#GetStorageOffsetAfterRealToRealBitcast), [`GetStridesAfterRealToRealBitcast`](bitcast_primitive.cc.md#GetStridesAfterRealToRealBitcast), [`CheckConversionBitwidthsAreDivisible`](bitcast_primitive.cc.md#CheckConversionBitwidthsAreDivisible), [`GetBitcastBitwidth`](bitcast_primitive.cc.md#GetBitcastBitwidth)

## Functions
- <a id="CheckBitcastTypesAreNotComplex"></a>`CheckBitcastTypesAreNotComplex(const RealToRealBitcast& bitcast)` — [`L278`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/bitcast_primitive.cc#L278)
- <a id="CheckConversionBitwidthsAreDivisible"></a>`CheckConversionBitwidthsAreDivisible(const RealToRealBitcast& bitcast, const BitcastBitwidth& bitwidth, const std::string_view error_message_suffix)` — [`L61`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/bitcast_primitive.cc#L61)
- <a id="CheckStridesAreDivisible"></a>`CheckStridesAreDivisible(const StridedLayout& layout, const RealToRealBitcast& bitcast, const int64_t size_ratio)` — [`L85`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/bitcast_primitive.cc#L85)
- <a id="GetBitcastBitwidth"></a>`GetBitcastBitwidth(const RealToRealBitcast& bitcast)` — [`L54`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/bitcast_primitive.cc#L54) — Convenient constructor of `BitcastBitwidth`, taking a `bitcast` as parameter.
- <a id="GetShapeAfterRealToRealBitcast"></a>`GetShapeAfterRealToRealBitcast(const RealToRealBitcast& bitcast, const BitcastBitwidth& bitwidth, absl::Span<const int64_t> shape, const std::string_view error_message_suffix)` — [`L120`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/bitcast_primitive.cc#L120) — Computes the shape of the tensor after a real-to-real bitcast.
- <a id="GetStorageOffsetAfterRealToRealBitcast"></a>`GetStorageOffsetAfterRealToRealBitcast(const RealToRealBitcast& bitcast, const BitcastBitwidth& bitwidth, const StridedLayout& layout)` — [`L225`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/bitcast_primitive.cc#L225) — Computes the storage offset of the tensor after a real-to-real bitcast.
- <a id="GetStridesAfterRealToRealBitcast"></a>`GetStridesAfterRealToRealBitcast(const RealToRealBitcast& bitcast, const BitcastBitwidth& bitwidth, const StridedLayout& layout)` — [`L165`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/bitcast_primitive.cc#L165) — Computes the strides of the tensor after a real-to-real bitcast.
- `ToString(ComplexToRealBitcastType bitcast)` — [`L302`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/bitcast_primitive.cc#L302)
- <a id="ToString"></a>`ToString(ComplexElementType complex_element_type)` — [`L324`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/bitcast_primitive.cc#L324)
- `UpdateLayout(StridedLayout& layout, const ViewAsComplex& bitcast)` — [`L419`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/bitcast_primitive.cc#L419) — Updates the layout to reflect the effect of applying the given
- <a id="UpdateLayout"></a>`UpdateLayout(StridedLayout& layout, const RealToRealBitcast& bitcast)` — [`L346`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/bitcast_primitive.cc#L346) — Updates the layout to reflect the effect of applying the given real-to-real
- `UpdateLayout(StridedLayout& layout, const ComplexToRealBitcast& bitcast)` — [`L391`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/bitcast_primitive.cc#L391) — Updates the layout to reflect the effect of applying the given
- <a id="ViewAsRealShlo"></a>`ViewAsRealShlo(mlir::MlirOp input)` — [`L262`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/bitcast_primitive.cc#L262) — Returns the logical equivalent of torch.view_as_real().
- `ViewPrimitiveShlo(mlir::MlirOp input, const ComplexToRealBitcast& bitcast)` — [`L523`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/bitcast_primitive.cc#L523) — Returns the logical equivalent of torch.view_as_real(), torch.real(), or
- `ViewPrimitiveShlo(mlir::MlirOp input, const ViewAsComplex& bitcast)` — [`L538`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/bitcast_primitive.cc#L538) — Returns the logical equivalent of torch.view_as_complex().
- <a id="ViewPrimitiveShlo"></a>`ViewPrimitiveShlo(mlir::MlirOp input, const RealToRealBitcast& bitcast)` — [`L469`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/bitcast_primitive.cc#L469) — Applies a real-to-real bitcast to the given tensor, following PyTorch's — documented in [view-decomposition](../../../../concepts/view-decomposition.md)
- <a id="operator"></a>`operator<<(std::ostream& os, const RealToRealBitcast& bitcast)` — [`L296`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/bitcast_primitive.cc#L296) — Formats the bitcast like "bitcast(from_type=f32, to_type=bf16)".
- `operator<<(std::ostream& os, const ComplexToRealBitcast& bitcast)` — [`L318`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/bitcast_primitive.cc#L318) — Formats the bitcast as one of:
- `operator<<(std::ostream& os, const ComplexElementType complex_element_type)` — [`L333`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/bitcast_primitive.cc#L333)
- `operator<<(std::ostream& os, const ViewAsComplex& bitcast)` — [`L338`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/bitcast_primitive.cc#L338) — Formats the bitcast like "view_as_complex(cfloat)".
- `operator<<(std::ostream& os, const ComplexToRealBitcastType bitcast)` — [`L313`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/bitcast_primitive.cc#L313)
- `operator==(const RealToRealBitcast& lhs, const RealToRealBitcast& rhs)` — [`L573`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/bitcast_primitive.cc#L573)
- `operator==(const ViewAsComplex& lhs, const ViewAsComplex& rhs)` — [`L583`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/bitcast_primitive.cc#L583)
- `operator==(const ComplexToRealBitcast& lhs, const ComplexToRealBitcast& rhs)` — [`L577`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/bitcast_primitive.cc#L577)

