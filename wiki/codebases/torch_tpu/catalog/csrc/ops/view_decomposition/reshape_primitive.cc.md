---
title: 'Module: csrc/ops/view_decomposition/reshape_primitive.cc'
type: catalog
provenance: extracted
module: csrc/ops/view_decomposition/reshape_primitive.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  operator: '`operator<<`(464979026a3914c).'
  UpdateLayout: UpdateLayout(975d16341c2d5c29).
  ViewPrimitiveShlo: ViewPrimitiveShlo(710e6dff53d60953).
  Merge: Merge(6c687807910807d5).
  CheckNumberOfElements: '`$anonymous_namespace_csrc/ops/view_decomposition/reshape_primitive.cc`/CheckNumberOfElements(766f4d7f4e7104d9).'
  GetContiguityBlocks: '`$anonymous_namespace_csrc/ops/view_decomposition/reshape_primitive.cc`/GetContiguityBlocks(d0b85c1b4416cfa3).'
  IsNoOpReshape: '`$anonymous_namespace_csrc/ops/view_decomposition/reshape_primitive.cc`/IsNoOpReshape(fd3d279884a1fef8).'
  ContiguityBlock.num_elements: '`$anonymous_namespace_csrc/ops/view_decomposition/reshape_primitive.cc`/ContiguityBlock#num_elements.'
  ContiguityBlock.minor_stride: '`$anonymous_namespace_csrc/ops/view_decomposition/reshape_primitive.cc`/ContiguityBlock#minor_stride.'
  ContiguityBlock: '`$anonymous_namespace_csrc/ops/view_decomposition/reshape_primitive.cc`/ContiguityBlock#'
---
# Module: [`csrc/ops/view_decomposition/reshape_primitive.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/reshape_primitive.cc)

## Classes
### <a id="ContiguityBlock"></a>`ContiguityBlock`
- def: [`csrc/ops/view_decomposition/reshape_primitive.cc:47`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/reshape_primitive.cc#L47)
- doc: A maximally-contiguous block of dimensions in a strided layout.
- signature: `struct ContiguityBlock`
- members:
  - <a id="ContiguityBlock.minor_stride"></a>`minor_stride` — [`L49`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/reshape_primitive.cc#L49)
  - <a id="ContiguityBlock.num_elements"></a>`num_elements` — [`L48`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/reshape_primitive.cc#L48)
- used by: [`UpdateLayout`](reshape_primitive.cc.md#UpdateLayout), [`GetContiguityBlocks`](reshape_primitive.cc.md#GetContiguityBlocks)

## Functions
- <a id="CheckNumberOfElements"></a>`CheckNumberOfElements(const ReshapePrimitive& reshape, const StridedLayout& layout)` — [`L112`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/reshape_primitive.cc#L112)
- <a id="GetContiguityBlocks"></a>`GetContiguityBlocks(const StridedLayout& layout)` — [`L55`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/reshape_primitive.cc#L55) — Returns the sequence of contiguity blocks in the given strided layout.
- `GetContiguityBlocks(const StridedLayout& layout)` — [`L55`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/reshape_primitive.cc#L55) — Returns the sequence of contiguity blocks in the given strided layout.
- <a id="IsNoOpReshape"></a>`IsNoOpReshape(const ReshapePrimitive& reshape, const StridedLayout& layout)` — [`L99`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/reshape_primitive.cc#L99)
- <a id="Merge"></a>`Merge(ReshapePrimitive first, ReshapePrimitive second)` — [`L236`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/reshape_primitive.cc#L236) — Merges two sequential reshapes into a single reshape.
- <a id="UpdateLayout"></a>`UpdateLayout(StridedLayout& layout, const ReshapePrimitive& reshape)` — [`L156`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/reshape_primitive.cc#L156) — Updates the layout to reflect the effect of applying the given reshape — documented in [view-decomposition](../../../../concepts/view-decomposition.md)
- <a id="ViewPrimitiveShlo"></a>`ViewPrimitiveShlo(mlir::MlirOp input, const ReshapePrimitive& reshape)` — [`L259`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/reshape_primitive.cc#L259) — An overload for the ViewPrimitiveShlo function that handles reshape
- <a id="operator"></a>`operator<<(std::ostream& os, const ReshapePrimitive& reshape)` — [`L150`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/reshape_primitive.cc#L150) — Formats the reshape like "reshape[1, 2, 3]".

