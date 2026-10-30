---
title: 'Module: csrc/ops/jagged/jagged_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/jagged/jagged_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenPaddedDenseToJaggedForward: AtenPaddedDenseToJaggedForward(78724e44e02c949c).
  AtenJaggedToPaddedDenseForward: AtenJaggedToPaddedDenseForward(2195bd993b0ba82b).
  AtenNestedViewFromJagged: AtenNestedViewFromJagged(ed68d586f406ed27).
  JaggedToPaddedDense: '`$anonymous_namespace_csrc/ops/jagged/jagged_aten_kernels.cc`/JaggedToPaddedDense(b5b2828c063e10d).'
  AtenNestedGetMinSeqlen: AtenNestedGetMinSeqlen(28959186f7a4bda8).
  AtenNestedGetMaxSeqlen: AtenNestedGetMaxSeqlen(28959186f7a4bda8).
  AtenNestedGetOffsets: AtenNestedGetOffsets(28959186f7a4bda8).
  AtenNestedGetValues: AtenNestedGetValues(28959186f7a4bda8).
  AtenNestedGetLengths: AtenNestedGetLengths(28959186f7a4bda8).
  AtenNestedGetJaggedDummy: AtenNestedGetJaggedDummy(28959186f7a4bda8).
  AtenNestedGetRaggedIdx: AtenNestedGetRaggedIdx(df301f5ba5d34600).
  PaddedDenseToJagged: '`$anonymous_namespace_csrc/ops/jagged/jagged_aten_kernels.cc`/PaddedDenseToJagged(6bff6b6d7d10e4c2).'
  ValidateAndGetOffsets: '`$anonymous_namespace_csrc/ops/jagged/jagged_aten_kernels.cc`/ValidateAndGetOffsets(e4f8a11eb1b338d7).'
  BuildJaggedToPaddedDenseHlo: '`$anonymous_namespace_csrc/ops/jagged/jagged_aten_kernels.cc`/BuildJaggedToPaddedDenseHlo(4f3588f9cbd59b41).'
  ComputePaddedToJaggedIndices: '`$anonymous_namespace_csrc/ops/jagged/jagged_aten_kernels.cc`/ComputePaddedToJaggedIndices(6fc5ff64153af80e).'
  GetCpuOffsets: '`$anonymous_namespace_csrc/ops/jagged/jagged_aten_kernels.cc`/GetCpuOffsets(ea29114dcc2e8e48).'
  BuildPaddedToJaggedHlo: '`$anonymous_namespace_csrc/ops/jagged/jagged_aten_kernels.cc`/BuildPaddedToJaggedHlo(ac83a6ad0c0501f).'
  ComputeJaggedToPaddedIndices: '`$anonymous_namespace_csrc/ops/jagged/jagged_aten_kernels.cc`/ComputeJaggedToPaddedIndices(27958839f7143faf).'
  AtenNestedFromPaddedTensor: AtenNestedFromPaddedTensor(84381030fac34dea).
  JaggedToPaddedIndices.num_valid: '`$anonymous_namespace_csrc/ops/jagged/jagged_aten_kernels.cc`/JaggedToPaddedIndices#num_valid.'
  CreateI64Constant: '`$anonymous_namespace_csrc/ops/jagged/jagged_aten_kernels.cc`/CreateI64Constant(c5a083f849ab3357).'
  JaggedToPaddedIndices.needs_truncation: '`$anonymous_namespace_csrc/ops/jagged/jagged_aten_kernels.cc`/JaggedToPaddedIndices#needs_truncation.'
  NormalizePaddingValue: '`$anonymous_namespace_csrc/ops/jagged/jagged_aten_kernels.cc`/NormalizePaddingValue(fc4e64391d6b2927).'
  JaggedToPaddedIndices.scatter_indices: '`$anonymous_namespace_csrc/ops/jagged/jagged_aten_kernels.cc`/JaggedToPaddedIndices#scatter_indices.'
  JaggedToPaddedIndices: '`$anonymous_namespace_csrc/ops/jagged/jagged_aten_kernels.cc`/JaggedToPaddedIndices#'
  GetInfinitePaddingScalar: '`$anonymous_namespace_csrc/ops/jagged/jagged_aten_kernels.cc`/GetInfinitePaddingScalar(69630280a1d8ae2c).'
  JaggedToPaddedIndices.gather_indices: '`$anonymous_namespace_csrc/ops/jagged/jagged_aten_kernels.cc`/JaggedToPaddedIndices#gather_indices.'
---
# Module: [`csrc/ops/jagged/jagged_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/jagged/jagged_aten_kernels.cc)

## Classes
### <a id="JaggedToPaddedIndices"></a>`JaggedToPaddedIndices`
- def: [`csrc/ops/jagged/jagged_aten_kernels.cc:188`](../../../../../../../raw/code/torch_tpu/csrc/ops/jagged/jagged_aten_kernels.cc#L188)
- doc: Helper struct holding calculated index mappings for JaggedToPaddedDense.
- signature: `struct JaggedToPaddedIndices`
- members:
  - <a id="JaggedToPaddedIndices.gather_indices"></a>`gather_indices` — [`L191`](../../../../../../../raw/code/torch_tpu/csrc/ops/jagged/jagged_aten_kernels.cc#L191)
  - <a id="JaggedToPaddedIndices.needs_truncation"></a>`needs_truncation` — [`L192`](../../../../../../../raw/code/torch_tpu/csrc/ops/jagged/jagged_aten_kernels.cc#L192)
  - <a id="JaggedToPaddedIndices.num_valid"></a>`num_valid` — [`L189`](../../../../../../../raw/code/torch_tpu/csrc/ops/jagged/jagged_aten_kernels.cc#L189)
  - <a id="JaggedToPaddedIndices.scatter_indices"></a>`scatter_indices` — [`L190`](../../../../../../../raw/code/torch_tpu/csrc/ops/jagged/jagged_aten_kernels.cc#L190)
- uses (calls/refs, reference-scoped): [`Indices`](../../common/dimension_types.h.md#Indices)
- used by: [`JaggedToPaddedDense`](jagged_aten_kernels.cc.md#JaggedToPaddedDense), [`BuildJaggedToPaddedDenseHlo`](jagged_aten_kernels.cc.md#BuildJaggedToPaddedDenseHlo), [`ComputeJaggedToPaddedIndices`](jagged_aten_kernels.cc.md#ComputeJaggedToPaddedIndices)

## Functions
- <a id="AtenJaggedToPaddedDenseForward"></a>`AtenJaggedToPaddedDenseForward(const at::Tensor& values, at::TensorList offsets, c10::SymIntArrayRef max_lengths, double padding_value)` — [`L540`](../../../../../../../raw/code/torch_tpu/csrc/ops/jagged/jagged_aten_kernels.cc#L540) — Converts a jagged nested tensor's flat values buffer into a padded dense
- <a id="AtenNestedFromPaddedTensor"></a>`AtenNestedFromPaddedTensor(const at::Tensor& padded, const at::Tensor& offsets, const at::Tensor& dummy, int64_t ragged_idx, const std::optional<at::Tensor>& min_seqlen, const std::optional<at::Tensor>& max_seqlen, std::optional<c10::SymInt> sum_S)` — [`L605`](../../../../../../../raw/code/torch_tpu/csrc/ops/jagged/jagged_aten_kernels.cc#L605) — Converts a padded dense tensor into a nested jagged view tensor.
- <a id="AtenNestedGetJaggedDummy"></a>`AtenNestedGetJaggedDummy(const at::Tensor& any)` — [`L641`](../../../../../../../raw/code/torch_tpu/csrc/ops/jagged/jagged_aten_kernels.cc#L641) — Returns a jagged dummy tensor for dispatching nested operations.
- <a id="AtenNestedGetLengths"></a>`AtenNestedGetLengths(const at::Tensor& self)` — [`L625`](../../../../../../../raw/code/torch_tpu/csrc/ops/jagged/jagged_aten_kernels.cc#L625) — Extracts the lengths tensor from a nested jagged tensor.
- <a id="AtenNestedGetMaxSeqlen"></a>`AtenNestedGetMaxSeqlen(const at::Tensor& self)` — [`L637`](../../../../../../../raw/code/torch_tpu/csrc/ops/jagged/jagged_aten_kernels.cc#L637) — Extracts the max sequence length tensor from a nested jagged tensor.
- <a id="AtenNestedGetMinSeqlen"></a>`AtenNestedGetMinSeqlen(const at::Tensor& self)` — [`L633`](../../../../../../../raw/code/torch_tpu/csrc/ops/jagged/jagged_aten_kernels.cc#L633) — Extracts the min sequence length tensor from a nested jagged tensor.
- <a id="AtenNestedGetOffsets"></a>`AtenNestedGetOffsets(const at::Tensor& self)` — [`L621`](../../../../../../../raw/code/torch_tpu/csrc/ops/jagged/jagged_aten_kernels.cc#L621) — Extracts the offsets tensor from a nested jagged tensor.
- <a id="AtenNestedGetRaggedIdx"></a>`AtenNestedGetRaggedIdx(const at::Tensor& self)` — [`L629`](../../../../../../../raw/code/torch_tpu/csrc/ops/jagged/jagged_aten_kernels.cc#L629) — Extracts the ragged index from a nested jagged tensor.
- <a id="AtenNestedGetValues"></a>`AtenNestedGetValues(const at::Tensor& self)` — [`L617`](../../../../../../../raw/code/torch_tpu/csrc/ops/jagged/jagged_aten_kernels.cc#L617) — Extracts the underlying values buffer from a nested jagged tensor.
- <a id="AtenNestedViewFromJagged"></a>`AtenNestedViewFromJagged(const at::Tensor& self, const at::Tensor& offsets, const at::Tensor& dummy, const std::optional<at::Tensor>& lengths, int64_t ragged_idx, const std::optional<at::Tensor>& min_seqlen, const std::optional<at::Tensor>& max_seqlen)` — [`L591`](../../../../../../../raw/code/torch_tpu/csrc/ops/jagged/jagged_aten_kernels.cc#L591) — =============================================================================
- <a id="AtenPaddedDenseToJaggedForward"></a>`AtenPaddedDenseToJaggedForward(const at::Tensor& dense, at::TensorList offsets, std::optional<c10::SymInt> total_L)` — [`L554`](../../../../../../../raw/code/torch_tpu/csrc/ops/jagged/jagged_aten_kernels.cc#L554) — Converts a padded dense tensor back into a flat jagged values buffer on TPU.
- <a id="BuildJaggedToPaddedDenseHlo"></a>`BuildJaggedToPaddedDenseHlo(mlir::MlirOp values_op, const Dimensions& values_shape, const Dimensions& padded_shape, const Dimensions& flat_padded_shape, mlir::ElementType output_dtype, at::Scalar fill_scalar, const JaggedToPaddedIndices& indices)` — [`L230`](../../../../../../../raw/code/torch_tpu/csrc/ops/jagged/jagged_aten_kernels.cc#L230) — Lowers JaggedToPaddedDense StableHLO graph.
- <a id="BuildPaddedToJaggedHlo"></a>`BuildPaddedToJaggedHlo(mlir::MlirOp dense_op, int64_t dense_rank, const Dimensions& dense_shape, const Dimensions& flat_dense_shape, int64_t total_L_computed, absl::Span<const int64_t> gather_indices)` — [`L420`](../../../../../../../raw/code/torch_tpu/csrc/ops/jagged/jagged_aten_kernels.cc#L420) — Lowers PaddedDenseToJagged StableHLO graph.
- <a id="ComputeJaggedToPaddedIndices"></a>`ComputeJaggedToPaddedIndices(absl::Span<const int64_t> offsets_vec, int64_t batch_size, int64_t max_length, int64_t total_values)` — [`L196`](../../../../../../../raw/code/torch_tpu/csrc/ops/jagged/jagged_aten_kernels.cc#L196) — Computes 1D linear scatter/gather index arrays for JaggedToPaddedDense.
- <a id="ComputePaddedToJaggedIndices"></a>`ComputePaddedToJaggedIndices(absl::Span<const int64_t> offsets_vec, int64_t batch_size, int64_t max_length, int64_t total_L_computed)` — [`L383`](../../../../../../../raw/code/torch_tpu/csrc/ops/jagged/jagged_aten_kernels.cc#L383) — Computes 1D linear gather indices for PaddedDenseToJagged.
- <a id="CreateI64Constant"></a>`CreateI64Constant(mlir::MlirBuilder& builder, llvm::ArrayRef<int64_t> data, llvm::ArrayRef<int64_t> shape)` — [`L133`](../../../../../../../raw/code/torch_tpu/csrc/ops/jagged/jagged_aten_kernels.cc#L133) — Helper to construct an int64 StableHLO constant tensor from an ArrayRef.
- <a id="GetCpuOffsets"></a>`GetCpuOffsets(const at::Tensor& offsets_tensor)` — [`L71`](../../../../../../../raw/code/torch_tpu/csrc/ops/jagged/jagged_aten_kernels.cc#L71) — Reads offsets tensor values into host Indices.
- <a id="GetInfinitePaddingScalar"></a>`GetInfinitePaddingScalar(at::ScalarType dtype, bool is_positive)` — [`L143`](../../../../../../../raw/code/torch_tpu/csrc/ops/jagged/jagged_aten_kernels.cc#L143) — Helper returning the extreme value scalar for infinite padding on
- <a id="JaggedToPaddedDense"></a>`JaggedToPaddedDense(const at::Tensor& values, at::TensorList offsets, c10::SymIntArrayRef max_lengths, double padding_value, OpParamCacheKeys param_keys)` — [`L307`](../../../../../../../raw/code/torch_tpu/csrc/ops/jagged/jagged_aten_kernels.cc#L307) — Lowers aten._jagged_to_padded_dense_forward to efficient StableHLO:
- <a id="NormalizePaddingValue"></a>`NormalizePaddingValue(const at::Tensor& values, double padding_value)` — [`L173`](../../../../../../../raw/code/torch_tpu/csrc/ops/jagged/jagged_aten_kernels.cc#L173) — Normalizes the padding value. For integral and boolean types, non-finite
- <a id="PaddedDenseToJagged"></a>`PaddedDenseToJagged(const at::Tensor& dense, at::TensorList offsets, int64_t total_L_val, OpParamCacheKeys param_keys)` — [`L458`](../../../../../../../raw/code/torch_tpu/csrc/ops/jagged/jagged_aten_kernels.cc#L458) — Lowers aten._padded_dense_to_jagged_forward to efficient StableHLO:
- <a id="ValidateAndGetOffsets"></a>`ValidateAndGetOffsets(at::TensorList offsets, OpParamCacheKeys& param_keys)` — [`L97`](../../../../../../../raw/code/torch_tpu/csrc/ops/jagged/jagged_aten_kernels.cc#L97) — Validates the offsets TensorList, retrieves host-side offset coordinates, and

