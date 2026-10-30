---
title: 'Module: csrc/internal/mosaic/op_builders.h'
type: catalog
provenance: extracted
module: csrc/internal/mosaic/op_builders.h
status: fresh
symbol_base: cxx . . $ mlir/torch_tpu/
symbols:
  MatmulOptions.precision: MatmulOptions#precision.
  DimensionSemantics: DimensionSemantics#
  MatmulOptions: MatmulOptions#
  DimensionSemantics.kArbitrary: DimensionSemantics#kArbitrary.
  DimensionSemantics.kParallel: DimensionSemantics#kParallel.
  kDefaultSerializationVersion: kDefaultSerializationVersion.
  MatmulOptions.transpose_rhs: MatmulOptions#transpose_rhs.
  MatmulOptions.transpose_lhs: MatmulOptions#transpose_lhs.
---
# Module: [`csrc/internal/mosaic/op_builders.h`](../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/op_builders.h)

## Classes
### <a id="DimensionSemantics"></a>`DimensionSemantics`
- def: [`csrc/internal/mosaic/op_builders.h:39`](../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/op_builders.h#L39) — documented in [mosaic-matmul](../../../../concepts/mosaic-matmul.md)
- signature: `enum class DimensionSemantics`
- members:
  - <a id="DimensionSemantics.kArbitrary"></a>`kArbitrary` — [`L41`](../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/op_builders.h#L41)
  - `kArbitrary` — [`L41`](../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/op_builders.h#L41)
  - <a id="DimensionSemantics.kParallel"></a>`kParallel` — [`L40`](../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/op_builders.h#L40)
  - `kParallel` — [`L40`](../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/op_builders.h#L40)
- used by: [`SetBackwardDkvKernelAttributes`](../../ops/scaled_dot_product_attention/flash_attention_backward_kernel.cc.md#SetBackwardDkvKernelAttributes), [`precision`](op_builders.h.md#MatmulOptions.precision), [`SetBackwardDqKernelAttributes`](../../ops/scaled_dot_product_attention/flash_attention_backward_kernel.cc.md#SetBackwardDqKernelAttributes), [`GetDimensionSemanticsAttr`](op_builders.cc.md#GetDimensionSemanticsAttr), [`SetKernelAttributes`](../../ops/scaled_dot_product_attention/flash_attention_kernel.cc.md#SetKernelAttributes), [`BlockType`](kiln/core/kernel.cc.md#BlockType), [`ToMlirDimensionSemantics`](kiln/core/kernel.cc.md#ToMlirDimensionSemantics)

### <a id="MatmulOptions"></a>`MatmulOptions`
- def: [`csrc/internal/mosaic/op_builders.h:44`](../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/op_builders.h#L44) — documented in [mosaic-matmul](../../../../concepts/mosaic-matmul.md)
- signature: `struct MatmulOptions`
- members:
  - `precision` — [`L48`](../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/op_builders.h#L48) — MXU contraction precision (`nullopt` defaults to 1-pass kBF16).
  - <a id="MatmulOptions.precision"></a>`precision` — [`L48`](../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/op_builders.h#L48) — MXU contraction precision (`nullopt` defaults to 1-pass kBF16). — documented in [mosaic-matmul](../../../../concepts/mosaic-matmul.md)
  - `transpose_lhs` — [`L45`](../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/op_builders.h#L45)
  - <a id="MatmulOptions.transpose_lhs"></a>`transpose_lhs` — [`L45`](../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/op_builders.h#L45) — documented in [mosaic-matmul](../../../../concepts/mosaic-matmul.md)
  - `transpose_rhs` — [`L46`](../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/op_builders.h#L46)
  - <a id="MatmulOptions.transpose_rhs"></a>`transpose_rhs` — [`L46`](../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/op_builders.h#L46) — documented in [mosaic-matmul](../../../../concepts/mosaic-matmul.md)
- uses (calls/refs, reference-scoped): [`GetVmemMemRefType`](op_builders.cc.md#GetVmemMemRefType), [`CreateMatmul`](op_builders.cc.md#CreateMatmul), [`GetDimensionSemanticsAttr`](op_builders.cc.md#GetDimensionSemanticsAttr), [`CreateIotaOp`](op_builders.cc.md#CreateIotaOp), [`CreateRepeatOp`](op_builders.cc.md#CreateRepeatOp), [`GetSmemMemRefType`](op_builders.cc.md#GetSmemMemRefType), [`CreateMlirContextWithDialects`](op_builders.cc.md#CreateMlirContextWithDialects), [`SerializeMosaicKernel`](op_builders.cc.md#SerializeMosaicKernel), [`DimensionSemantics`](op_builders.h.md#DimensionSemantics), [`CreateReciprocal`](op_builders.cc.md#CreateReciprocal), [`SetTcCoreTypeAttr`](op_builders.cc.md#SetTcCoreTypeAttr), [`SetTcCoreTypeAttr`](op_builders.cc.md#SetTcCoreTypeAttr), [`CreateMlirContextWithDialects`](op_builders.cc.md#CreateMlirContextWithDialects), [`MatmulOptions`](op_builders.h.md#MatmulOptions), [`kDefaultSerializationVersion`](op_builders.h.md#kDefaultSerializationVersion), [`DimensionSemantics`](op_builders.h.md#DimensionSemantics), [`kDefaultSerializationVersion`](op_builders.h.md#kDefaultSerializationVersion)
- used by: [`buildBackwardDkvModule`](../../ops/scaled_dot_product_attention/flash_attention_backward_kernel.cc.md#buildBackwardDkvModule), [`buildBackwardDqModule`](../../ops/scaled_dot_product_attention/flash_attention_backward_kernel.cc.md#buildBackwardDqModule), [`UpdateSoftmaxState`](../../ops/scaled_dot_product_attention/flash_attention_kernel.cc.md#UpdateSoftmaxState), [`Dot`](kiln/core/tile.cc.md#Dot), [`ComputeSharedBackwardLogic`](../../ops/scaled_dot_product_attention/flash_attention_backward_kernel.cc.md#ComputeSharedBackwardLogic), [`CreateMatmul`](op_builders.cc.md#CreateMatmul)

## Module values
- <a id="kDefaultSerializationVersion"></a>`kDefaultSerializationVersion` — [`L37`](../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/op_builders.h#L37)
- `kDefaultSerializationVersion` — [`L37`](../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/op_builders.h#L37)

