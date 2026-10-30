---
title: 'Module: csrc/ops/embedding/embedding.cc'
type: catalog
provenance: extracted
module: csrc/ops/embedding/embedding.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  BuildEmbeddingBagShlo: BuildEmbeddingBagShlo(5e8b6cc97c7a60a5).
  BuildEmbeddingBagBackwardShlo: BuildEmbeddingBagBackwardShlo(cc11ad052759fb3d).
  BuildEmbeddingDenseBackwardShlo: BuildEmbeddingDenseBackwardShlo(151a8fd2ea3db64a).
  BuildRenormRow: '`$anonymous_namespace_csrc/ops/embedding/embedding.cc`/BuildRenormRow(4beeacacf8c2d68d).'
  BuildEmbeddingBagSparseBackwardIndexGradShlo: BuildEmbeddingBagSparseBackwardIndexGradShlo(a7dfd1574123fe7d).
  BuildOffset2Bag: '`$anonymous_namespace_csrc/ops/embedding/embedding.cc`/BuildOffset2Bag(697437a9d4607d83).'
  BuildEmbeddingSparseBackwardPadShlo: BuildEmbeddingSparseBackwardPadShlo(d6612fc6847a1c6f).
  ScaleGradByFrequency: '`$anonymous_namespace_csrc/ops/embedding/embedding.cc`/ScaleGradByFrequency(d8cecbbdc9c65274).'
  BuildMaxAggregation: '`$anonymous_namespace_csrc/ops/embedding/embedding.cc`/BuildMaxAggregation(dedb5cfee9955816).'
  BuildBagSize: '`$anonymous_namespace_csrc/ops/embedding/embedding.cc`/BuildBagSize(225d212cfce54c94).'
  BuildEmbeddingShlo: BuildEmbeddingShlo(9dd408ac7de815bd).
  MaskPaddingIndices: '`$anonymous_namespace_csrc/ops/embedding/embedding.cc`/MaskPaddingIndices(4216c53f64f59484).'
  ResolveMeanBagSize: '`$anonymous_namespace_csrc/ops/embedding/embedding.cc`/ResolveMeanBagSize(87acb123d3108c2).'
  BuildEmbeddingRenormShlo: BuildEmbeddingRenormShlo(35fdf0071c625b4b).
  BuildMeanBagBackward: '`$anonymous_namespace_csrc/ops/embedding/embedding.cc`/BuildMeanBagBackward(4c390e1df8421d87).'
  ZeroOutPaddingGradIndices: '`$anonymous_namespace_csrc/ops/embedding/embedding.cc`/ZeroOutPaddingGradIndices(c4a63dc770aa1368).'
  BuildMaxBagBackward: '`$anonymous_namespace_csrc/ops/embedding/embedding.cc`/BuildMaxBagBackward(d8cecbbdc9c65274).'
  ApplyPerSampleWeights: '`$anonymous_namespace_csrc/ops/embedding/embedding.cc`/ApplyPerSampleWeights(a3fda1f5f6db7d54).'
  ScaleByBagSize: '`$anonymous_namespace_csrc/ops/embedding/embedding.cc`/ScaleByBagSize(6fb228fd2a36be37).'
  BuildEmbeddingSparseBackwardNoPadShlo: BuildEmbeddingSparseBackwardNoPadShlo(c7e03db390d43621).
  BuildSimpleScatter: '`$anonymous_namespace_csrc/ops/embedding/embedding.cc`/BuildSimpleScatter(f60984abbdb1ed3f).'
  BuildEmbeddingGather: '`$anonymous_namespace_csrc/ops/embedding/embedding.cc`/BuildEmbeddingGather(e0a93cd238e2957e).'
  HasWindow: '`$anonymous_namespace_csrc/ops/embedding/embedding.cc`/HasWindow#'
  HasWindow.kYes: '`$anonymous_namespace_csrc/ops/embedding/embedding.cc`/HasWindow#kYes.'
  BuildSparseMaskDescIotaAscComparator: '`$anonymous_namespace_csrc/ops/embedding/embedding.cc`/BuildSparseMaskDescIotaAscComparator(fb903c4b9d45beef).'
  MaxAggregationResult.max_indices: '`$anonymous_namespace_csrc/ops/embedding/embedding.cc`/MaxAggregationResult#max_indices.'
  MaskedPaddingResult: '`$anonymous_namespace_csrc/ops/embedding/embedding.cc`/MaskedPaddingResult#'
  MaskedPaddingResult.is_padding: '`$anonymous_namespace_csrc/ops/embedding/embedding.cc`/MaskedPaddingResult#is_padding.'
  MaxAggregationResult: '`$anonymous_namespace_csrc/ops/embedding/embedding.cc`/MaxAggregationResult#'
  HasWindow.kNo: '`$anonymous_namespace_csrc/ops/embedding/embedding.cc`/HasWindow#kNo.'
  MaxAggregationResult.output: '`$anonymous_namespace_csrc/ops/embedding/embedding.cc`/MaxAggregationResult#output.'
  MaskedPaddingResult.gathered: '`$anonymous_namespace_csrc/ops/embedding/embedding.cc`/MaskedPaddingResult#gathered.'
---
# Module: [`csrc/ops/embedding/embedding.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/embedding/embedding.cc)

## Classes
### <a id="HasWindow"></a>`HasWindow`
- def: [`csrc/ops/embedding/embedding.cc:77`](../../../../../../../raw/code/torch_tpu/csrc/ops/embedding/embedding.cc#L77)
- doc: Builds a simple scatter operation.
- signature: `enum class HasWindow`
- members:
  - <a id="HasWindow.kNo"></a>`kNo` — [`L78`](../../../../../../../raw/code/torch_tpu/csrc/ops/embedding/embedding.cc#L78)
  - <a id="HasWindow.kYes"></a>`kYes` — [`L79`](../../../../../../../raw/code/torch_tpu/csrc/ops/embedding/embedding.cc#L79)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`BuildEmbeddingBagShlo`](embedding.cc.md#BuildEmbeddingBagShlo), [`BuildEmbeddingBagBackwardShlo`](embedding.cc.md#BuildEmbeddingBagBackwardShlo), [`BuildEmbeddingDenseBackwardShlo`](embedding.cc.md#BuildEmbeddingDenseBackwardShlo), [`BuildOffset2Bag`](embedding.cc.md#BuildOffset2Bag), [`ScaleGradByFrequency`](embedding.cc.md#ScaleGradByFrequency), [`BuildBagSize`](embedding.cc.md#BuildBagSize), [`BuildSimpleScatter`](embedding.cc.md#BuildSimpleScatter)

### <a id="MaskedPaddingResult"></a>`MaskedPaddingResult`
- def: [`csrc/ops/embedding/embedding.cc:316`](../../../../../../../raw/code/torch_tpu/csrc/ops/embedding/embedding.cc#L316)
- signature: `struct MaskedPaddingResult`
- members:
  - <a id="MaskedPaddingResult.gathered"></a>`gathered` — [`L317`](../../../../../../../raw/code/torch_tpu/csrc/ops/embedding/embedding.cc#L317)
  - <a id="MaskedPaddingResult.is_padding"></a>`is_padding` — [`L318`](../../../../../../../raw/code/torch_tpu/csrc/ops/embedding/embedding.cc#L318)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`MaskPaddingIndices`](embedding.cc.md#MaskPaddingIndices)

### <a id="MaxAggregationResult"></a>`MaxAggregationResult`
- def: [`csrc/ops/embedding/embedding.cc:50`](../../../../../../../raw/code/torch_tpu/csrc/ops/embedding/embedding.cc#L50)
- signature: `struct MaxAggregationResult`
- members:
  - <a id="MaxAggregationResult.max_indices"></a>`max_indices` — [`L52`](../../../../../../../raw/code/torch_tpu/csrc/ops/embedding/embedding.cc#L52)
  - <a id="MaxAggregationResult.output"></a>`output` — [`L51`](../../../../../../../raw/code/torch_tpu/csrc/ops/embedding/embedding.cc#L51)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`BuildEmbeddingBagShlo`](embedding.cc.md#BuildEmbeddingBagShlo), [`BuildOffset2Bag`](embedding.cc.md#BuildOffset2Bag), [`BuildMaxAggregation`](embedding.cc.md#BuildMaxAggregation)

## Functions
- <a id="ApplyPerSampleWeights"></a>`ApplyPerSampleWeights(mlir::MlirOp tensor, const std::optional<mlir::MlirOp>& per_sample_weights, bool needs_upcast)` — [`L298`](../../../../../../../raw/code/torch_tpu/csrc/ops/embedding/embedding.cc#L298)
- <a id="BuildBagSize"></a>`BuildBagSize(mlir::MlirBuilder& builder, mlir::MlirOp bag_size_init, mlir::MlirOp scatter_indices, int64_t num_indices, int64_t padding_idx, mlir::MlirOp is_padding, mlir::Type i64_type)` — [`L345`](../../../../../../../raw/code/torch_tpu/csrc/ops/embedding/embedding.cc#L345)
- <a id="BuildEmbeddingBagBackwardShlo"></a>`BuildEmbeddingBagBackwardShlo(mlir::MlirOp grad, mlir::MlirOp indices, mlir::MlirOp offsets, mlir::MlirOp offset2bag, mlir::MlirOp bag_size, mlir::MlirOp max_indices, at::SymInt num_weights, bool scale_grad_by_freq, int64_t mode, bool sparse, std::optional<mlir::MlirOp> per_sample_weights, int64_t padding_idx)` — [`L680`](../../../../../../../raw/code/torch_tpu/csrc/ops/embedding/embedding.cc#L680)
- <a id="BuildEmbeddingBagShlo"></a>`BuildEmbeddingBagShlo(mlir::MlirOp weight, mlir::MlirOp indices, mlir::MlirOp offsets, bool scale_grad_by_freq, int64_t mode, bool sparse, std::optional<mlir::MlirOp> per_sample_weights, bool include_last_offset, int64_t padding_idx)` — [`L555`](../../../../../../../raw/code/torch_tpu/csrc/ops/embedding/embedding.cc#L555)
- `BuildEmbeddingBagShlo(mlir::MlirOp weight, mlir::MlirOp indices, mlir::MlirOp offsets, bool scale_grad_by_freq, int64_t mode, bool sparse, std::optional<mlir::MlirOp> per_sample_weights, bool include_last_offset, int64_t padding_idx)` — [`L555`](../../../../../../../raw/code/torch_tpu/csrc/ops/embedding/embedding.cc#L555)
- <a id="BuildEmbeddingBagSparseBackwardIndexGradShlo"></a>`BuildEmbeddingBagSparseBackwardIndexGradShlo(mlir::MlirOp grad, mlir::MlirOp indices, mlir::MlirOp offsets, mlir::MlirOp offset2bag, mlir::MlirOp bag_size, int64_t mode, std::optional<mlir::MlirOp> per_sample_weights, int64_t padding_idx)` — [`L777`](../../../../../../../raw/code/torch_tpu/csrc/ops/embedding/embedding.cc#L777)
- <a id="BuildEmbeddingDenseBackwardShlo"></a>`BuildEmbeddingDenseBackwardShlo(mlir::MlirOp grad_output, mlir::MlirOp indices, at::SymInt num_weights, at::SymInt padding_idx, bool scale_grad_by_freq)` — [`L836`](../../../../../../../raw/code/torch_tpu/csrc/ops/embedding/embedding.cc#L836)
- <a id="BuildEmbeddingGather"></a>`BuildEmbeddingGather(mlir::MlirBuilder& builder, mlir::MlirOp weight, mlir::MlirOp indices)` — [`L56`](../../../../../../../raw/code/torch_tpu/csrc/ops/embedding/embedding.cc#L56) — Gathers embedding rows from `weight` based on `indices`.
- <a id="BuildEmbeddingRenormShlo"></a>`BuildEmbeddingRenormShlo(mlir::MlirOp weight, mlir::MlirOp indices, double max_norm, double norm_type)` — [`L957`](../../../../../../../raw/code/torch_tpu/csrc/ops/embedding/embedding.cc#L957)
- <a id="BuildEmbeddingShlo"></a>`BuildEmbeddingShlo(mlir::MlirOp weight, mlir::MlirOp indices)` — [`L522`](../../../../../../../raw/code/torch_tpu/csrc/ops/embedding/embedding.cc#L522)
- <a id="BuildEmbeddingSparseBackwardNoPadShlo"></a>`BuildEmbeddingSparseBackwardNoPadShlo(mlir::MlirOp grad_output, mlir::MlirOp indices)` — [`L1015`](../../../../../../../raw/code/torch_tpu/csrc/ops/embedding/embedding.cc#L1015)
- <a id="BuildEmbeddingSparseBackwardPadShlo"></a>`BuildEmbeddingSparseBackwardPadShlo(mlir::MlirOp grad_output, mlir::MlirOp indices, const int64_t padding_idx)` — [`L1027`](../../../../../../../raw/code/torch_tpu/csrc/ops/embedding/embedding.cc#L1027)
- <a id="BuildMaxAggregation"></a>`BuildMaxAggregation(mlir::MlirBuilder& builder, mlir::MlirOp updates, mlir::MlirOp indices, mlir::MlirOp val_init, mlir::MlirOp idx_init, mlir::Type i64_type, mlir::Type val_type, mlir::MlirOp offset2bag)` — [`L140`](../../../../../../../raw/code/torch_tpu/csrc/ops/embedding/embedding.cc#L140) — Builds the scatter operation for MAX mode, which aggregates both the
- <a id="BuildMaxBagBackward"></a>`BuildMaxBagBackward(mlir::MlirBuilder& builder, mlir::MlirOp acc_grad, mlir::MlirOp max_indices, int64_t num_indices, int64_t emb_dim, mlir::MlirOp zeros_float, mlir::Type acc_elem_type, mlir::Type i64_type)` — [`L403`](../../../../../../../raw/code/torch_tpu/csrc/ops/embedding/embedding.cc#L403)
- <a id="BuildMeanBagBackward"></a>`BuildMeanBagBackward(mlir::MlirBuilder& builder, mlir::MlirOp grad_indices, mlir::MlirOp bag_size, mlir::MlirOp offset2bag, mlir::MlirOp zeros_float, mlir::Type acc_elem_type)` — [`L382`](../../../../../../../raw/code/torch_tpu/csrc/ops/embedding/embedding.cc#L382)
- <a id="BuildOffset2Bag"></a>`BuildOffset2Bag(mlir::MlirBuilder& builder, mlir::MlirOp indices, mlir::MlirOp offsets, mlir::Type i64_type, int64_t batch_size)` — [`L106`](../../../../../../../raw/code/torch_tpu/csrc/ops/embedding/embedding.cc#L106) — Builds a tensor of shape [num_indices] where result[i] is the bag ID for
- <a id="BuildRenormRow"></a>`BuildRenormRow(mlir::MlirBuilder& builder, mlir::MlirOp row, double max_norm, double norm_type)` — [`L221`](../../../../../../../raw/code/torch_tpu/csrc/ops/embedding/embedding.cc#L221)
- <a id="BuildSimpleScatter"></a>`BuildSimpleScatter(mlir::MlirBuilder& builder, mlir::MlirOp operand, mlir::MlirOp indices, mlir::MlirOp updates, HasWindow has_window)` — [`L82`](../../../../../../../raw/code/torch_tpu/csrc/ops/embedding/embedding.cc#L82)
- <a id="BuildSparseMaskDescIotaAscComparator"></a>`BuildSparseMaskDescIotaAscComparator(mlir::RegionBuilder& rb)` — [`L982`](../../../../../../../raw/code/torch_tpu/csrc/ops/embedding/embedding.cc#L982)
- <a id="MaskPaddingIndices"></a>`MaskPaddingIndices(mlir::MlirBuilder& builder, mlir::MlirOp gathered, mlir::MlirOp flattened_indices, int64_t padding_idx, int64_t mode, mlir::Type acc_elem_type)` — [`L321`](../../../../../../../raw/code/torch_tpu/csrc/ops/embedding/embedding.cc#L321)
- <a id="ResolveMeanBagSize"></a>`ResolveMeanBagSize(mlir::MlirBuilder& builder, mlir::MlirOp bag_size, mlir::MlirOp active_offset2bag, mlir::MlirOp flattened_indices, int64_t batch_size, int64_t num_indices, int64_t padding_idx, mlir::Type i64_type)` — [`L493`](../../../../../../../raw/code/torch_tpu/csrc/ops/embedding/embedding.cc#L493)
- <a id="ScaleByBagSize"></a>`ScaleByBagSize(mlir::MlirBuilder& builder, mlir::MlirOp output, mlir::MlirOp bag_size, mlir::Type acc_elem_type)` — [`L364`](../../../../../../../raw/code/torch_tpu/csrc/ops/embedding/embedding.cc#L364)
- <a id="ScaleGradByFrequency"></a>`ScaleGradByFrequency(mlir::MlirBuilder& builder, mlir::MlirOp grad_indices, mlir::MlirOp flattened_indices, int64_t num_indices, int64_t nw, mlir::MlirOp zeros_float, mlir::Type acc_elem_type, mlir::Type i64_type)` — [`L464`](../../../../../../../raw/code/torch_tpu/csrc/ops/embedding/embedding.cc#L464)
- <a id="ZeroOutPaddingGradIndices"></a>`ZeroOutPaddingGradIndices(mlir::MlirBuilder& builder, mlir::MlirOp grad_indices, mlir::MlirOp flattened_indices, int64_t padding_idx, mlir::MlirOp zeros_float)` — [`L443`](../../../../../../../raw/code/torch_tpu/csrc/ops/embedding/embedding.cc#L443)

