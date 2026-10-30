---
title: 'Module: csrc/ops/stride/stride_helper.cc'
type: catalog
provenance: extracted
module: csrc/ops/stride/stride_helper.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  ValidateProvidedLayoutDataFitsInStorage: ValidateProvidedLayoutDataFitsInStorage(fcd175771e1705a0).
  IsOverlapping: IsOverlapping(c6b593a6685c21d).
  CalculateStridesContiguous: CalculateStridesContiguous(1001e5ee919908dd).
  SizeAndStride.stride: '`$anonymous_namespace_csrc/ops/stride/stride_helper.cc`/SizeAndStride#stride.'
  SizeAndStride: '`$anonymous_namespace_csrc/ops/stride/stride_helper.cc`/SizeAndStride#'
  SizeAndStride.size: '`$anonymous_namespace_csrc/ops/stride/stride_helper.cc`/SizeAndStride#size.'
---
# Module: [`csrc/ops/stride/stride_helper.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/stride/stride_helper.cc)

## Classes
### <a id="SizeAndStride"></a>`SizeAndStride`
- def: [`csrc/ops/stride/stride_helper.cc:54`](../../../../../../../raw/code/torch_tpu/csrc/ops/stride/stride_helper.cc#L54)
- doc: Size and stride pair for one dimension of a tensor. Used by IsOverlapping
- signature: `struct SizeAndStride`
- members:
  - <a id="SizeAndStride.size"></a>`size` — [`L55`](../../../../../../../raw/code/torch_tpu/csrc/ops/stride/stride_helper.cc#L55)
  - <a id="SizeAndStride.stride"></a>`stride` — [`L56`](../../../../../../../raw/code/torch_tpu/csrc/ops/stride/stride_helper.cc#L56)
- used by: [`IsOverlapping`](stride_helper.cc.md#IsOverlapping)

## Functions
- <a id="CalculateStridesContiguous"></a>`CalculateStridesContiguous(absl::Span<const int64_t> shape)` — [`L34`](../../../../../../../raw/code/torch_tpu/csrc/ops/stride/stride_helper.cc#L34) — Calculates the memory strides for a tensor of a given shape, assuming a
- <a id="IsOverlapping"></a>`IsOverlapping(absl::Span<const int64_t> sizes, absl::Span<const int64_t> strides, bool allow_expanded)` — [`L61`](../../../../../../../raw/code/torch_tpu/csrc/ops/stride/stride_helper.cc#L61) — Checks if the given set of sizes and strides is overlapping.
- <a id="ValidateProvidedLayoutDataFitsInStorage"></a>`ValidateProvidedLayoutDataFitsInStorage(int64_t storage_numel, mlir::ElementType storage_element_type, Dimensions sizes, Strides strides, int64_t storage_offset, mlir::ElementType layout_element_type)` — [`L117`](../../../../../../../raw/code/torch_tpu/csrc/ops/stride/stride_helper.cc#L117) — Checks that the provided sizes, strides, and storage offset fit within the

