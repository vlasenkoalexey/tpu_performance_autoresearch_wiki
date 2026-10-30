---
title: 'Module: csrc/ops/embedding/embedding.h'
type: catalog
provenance: extracted
module: csrc/ops/embedding/embedding.h
status: fresh
symbol_base: cxx . . $ torch_tpu/EmbeddingBagMode#
symbols:
  EmbeddingBagMode.kMax: kMax.
  EmbeddingBagMode: ''
  EmbeddingBagMode.kMean: kMean.
  EmbeddingBagMode.kSum: kSum.
---
# Module: [`csrc/ops/embedding/embedding.h`](../../../../../../../raw/code/torch_tpu/csrc/ops/embedding/embedding.h)

## Classes
### <a id="EmbeddingBagMode"></a>`EmbeddingBagMode`
- def: [`csrc/ops/embedding/embedding.h:30`](../../../../../../../raw/code/torch_tpu/csrc/ops/embedding/embedding.h#L30)
- signature: `enum class EmbeddingBagMode`
- members:
  - <a id="EmbeddingBagMode.kMax"></a>`kMax` — [`L30`](../../../../../../../raw/code/torch_tpu/csrc/ops/embedding/embedding.h#L30)
  - <a id="EmbeddingBagMode.kMean"></a>`kMean` — [`L30`](../../../../../../../raw/code/torch_tpu/csrc/ops/embedding/embedding.h#L30)
  - <a id="EmbeddingBagMode.kSum"></a>`kSum` — [`L30`](../../../../../../../raw/code/torch_tpu/csrc/ops/embedding/embedding.h#L30)
- uses (calls/refs, reference-scoped): [`MlirOpResults`](../op_builder_utils.h.md#MlirOpResults), [`BuildEmbeddingBagShlo`](embedding.cc.md#BuildEmbeddingBagShlo), [`BuildEmbeddingBagBackwardShlo`](embedding.cc.md#BuildEmbeddingBagBackwardShlo), [`BuildEmbeddingDenseBackwardShlo`](embedding.cc.md#BuildEmbeddingDenseBackwardShlo), [`BuildEmbeddingBagSparseBackwardIndexGradShlo`](embedding.cc.md#BuildEmbeddingBagSparseBackwardIndexGradShlo), [`BuildEmbeddingSparseBackwardPadShlo`](embedding.cc.md#BuildEmbeddingSparseBackwardPadShlo), [`BuildEmbeddingShlo`](embedding.cc.md#BuildEmbeddingShlo), [`BuildEmbeddingRenormShlo`](embedding.cc.md#BuildEmbeddingRenormShlo), [`BuildEmbeddingSparseBackwardNoPadShlo`](embedding.cc.md#BuildEmbeddingSparseBackwardNoPadShlo), [`BuildEmbeddingBagShlo`](embedding.cc.md#BuildEmbeddingBagShlo)
- used by: [`AtenEmbeddingBag`](embedding_aten_kernels.cc.md#AtenEmbeddingBag), [`BuildEmbeddingBagShlo`](embedding.cc.md#BuildEmbeddingBagShlo), [`BuildEmbeddingBagBackwardShlo`](embedding.cc.md#BuildEmbeddingBagBackwardShlo), [`BuildEmbeddingBagSparseBackwardIndexGradShlo`](embedding.cc.md#BuildEmbeddingBagSparseBackwardIndexGradShlo), [`ValidateEmbeddingBagSparseBackwardArgs`](embedding_aten_kernels.cc.md#ValidateEmbeddingBagSparseBackwardArgs)

