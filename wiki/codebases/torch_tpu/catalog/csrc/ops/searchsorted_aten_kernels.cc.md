---
title: 'Module: csrc/ops/searchsorted_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/searchsorted_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenSearchsortedScalarOut: AtenSearchsortedScalarOut(431f17ea061e34e2).
  AtenSearchsortedTensorOut: AtenSearchsortedTensorOut(e6f7207872561f36).
  AtenSearchsortedScalar: AtenSearchsortedScalar(b7418771b1c1d399).
  AtenSearchsortedTensor: AtenSearchsortedTensor(a2c1efd50b3bfe5d).
  SearchsortedTensorCommon: '`$anonymous_namespace_csrc/ops/searchsorted_aten_kernels.cc`/SearchsortedTensorCommon(6a83486d14f22a6a).'
  SearchsortedTensorOut: '`$anonymous_namespace_csrc/ops/searchsorted_aten_kernels.cc`/SearchsortedTensorOut(f09ce13f69da4939).'
  ValidateSearchsortedInputs: '`$anonymous_namespace_csrc/ops/searchsorted_aten_kernels.cc`/ValidateSearchsortedInputs(8e75183d475eaae2).'
  ResolveSearchsortedIsRight: '`$anonymous_namespace_csrc/ops/searchsorted_aten_kernels.cc`/ResolveSearchsortedIsRight(d0279496130bfaa9).'
  ResolveAuxiliaryTensorDevice: '`$anonymous_namespace_csrc/ops/searchsorted_aten_kernels.cc`/ResolveAuxiliaryTensorDevice(cd958efedc17238).'
  ApplySorterIfPresent: '`$anonymous_namespace_csrc/ops/searchsorted_aten_kernels.cc`/ApplySorterIfPresent(c176abad8c12df56).'
  BuildSearchsortedLoopShlo: '`$anonymous_namespace_csrc/ops/searchsorted_aten_kernels.cc`/BuildSearchsortedLoopShlo(a928f418b79eafc5).'
  SearchsortedTensorInternal: '`$anonymous_namespace_csrc/ops/searchsorted_aten_kernels.cc`/SearchsortedTensorInternal(36daf2d02c00f5d5).'
  Broadcast1DSequenceToQueryDims: '`$anonymous_namespace_csrc/ops/searchsorted_aten_kernels.cc`/Broadcast1DSequenceToQueryDims(bf8a7731760e7007).'
---
# Module: [`csrc/ops/searchsorted_aten_kernels.cc`](../../../../../../raw/code/torch_tpu/csrc/ops/searchsorted_aten_kernels.cc)

## Functions
- <a id="ApplySorterIfPresent"></a>`ApplySorterIfPresent(mlir::MlirOp sorted, std::optional<mlir::MlirOp> sorter_op, mlir::RankedTensorType query_type, int64_t seq_len, mlir::ElementType sorted_seq_elem_type)` — [`L170`](../../../../../../raw/code/torch_tpu/csrc/ops/searchsorted_aten_kernels.cc#L170)
- <a id="AtenSearchsortedScalar"></a>`AtenSearchsortedScalar(const at::Tensor& sorted_sequence, const at::Scalar& value, bool out_int32, bool right, c10::optional<c10::string_view> side, const c10::optional<at::Tensor>& sorter)` — [`L435`](../../../../../../raw/code/torch_tpu/csrc/ops/searchsorted_aten_kernels.cc#L435)
- <a id="AtenSearchsortedScalarOut"></a>`AtenSearchsortedScalarOut(const at::Tensor& sorted_sequence, const at::Scalar& value, bool out_int32, bool right, c10::optional<c10::string_view> side, const c10::optional<at::Tensor>& sorter, at::Tensor& out)` — [`L452`](../../../../../../raw/code/torch_tpu/csrc/ops/searchsorted_aten_kernels.cc#L452)
- <a id="AtenSearchsortedTensor"></a>`AtenSearchsortedTensor(const at::Tensor& sorted_sequence, const at::Tensor& values, bool out_int32, bool right, c10::optional<c10::string_view> side, const c10::optional<at::Tensor>& sorter)` — [`L405`](../../../../../../raw/code/torch_tpu/csrc/ops/searchsorted_aten_kernels.cc#L405)
- <a id="AtenSearchsortedTensorOut"></a>`AtenSearchsortedTensorOut(const at::Tensor& sorted_sequence, const at::Tensor& values, bool out_int32, bool right, c10::optional<c10::string_view> side, const c10::optional<at::Tensor>& sorter, at::Tensor& out)` — [`L420`](../../../../../../raw/code/torch_tpu/csrc/ops/searchsorted_aten_kernels.cc#L420)
- <a id="Broadcast1DSequenceToQueryDims"></a>`Broadcast1DSequenceToQueryDims(mlir::MlirOp seq_op, mlir::RankedTensorType query_type, int64_t seq_len)` — [`L155`](../../../../../../raw/code/torch_tpu/csrc/ops/searchsorted_aten_kernels.cc#L155)
- <a id="BuildSearchsortedLoopShlo"></a>`BuildSearchsortedLoopShlo(mlir::MlirOp sorted, mlir::MlirOp query, bool is_right, bool is_float, int64_t seq_len, int64_t num_iters, mlir::ElementType out_mlir_type, mlir::ElementType sorted_seq_elem_type, mlir::MlirBuilder& builder)` — [`L189`](../../../../../../raw/code/torch_tpu/csrc/ops/searchsorted_aten_kernels.cc#L189)
- <a id="ResolveAuxiliaryTensorDevice"></a>`ResolveAuxiliaryTensorDevice(const at::Tensor& tensor)` — [`L69`](../../../../../../raw/code/torch_tpu/csrc/ops/searchsorted_aten_kernels.cc#L69) — PyTorch's dispatcher bypasses backend device guards for auxiliary keyword
- `ResolveAuxiliaryTensorDevice(const c10::optional<at::Tensor>& tensor)` — [`L80`](../../../../../../raw/code/torch_tpu/csrc/ops/searchsorted_aten_kernels.cc#L80)
- <a id="ResolveSearchsortedIsRight"></a>`ResolveSearchsortedIsRight(bool right, c10::optional<c10::string_view> side)` — [`L137`](../../../../../../raw/code/torch_tpu/csrc/ops/searchsorted_aten_kernels.cc#L137)
- <a id="SearchsortedTensorCommon"></a>`SearchsortedTensorCommon(const at::Tensor& sorted_sequence, const at::Tensor& values, bool out_int32, bool right, c10::optional<c10::string_view> side, const c10::optional<at::Tensor>& sorter, OpParamCacheKeys&& param_keys, DispatchFn&& dispatch_fn)` — [`L270`](../../../../../../raw/code/torch_tpu/csrc/ops/searchsorted_aten_kernels.cc#L270)
- <a id="SearchsortedTensorInternal"></a>`SearchsortedTensorInternal(const at::Tensor& sorted_sequence, const at::Tensor& values, bool out_int32, bool right, c10::optional<c10::string_view> side, const c10::optional<at::Tensor>& sorter, OpParamCacheKeys&& param_keys)` — [`L351`](../../../../../../raw/code/torch_tpu/csrc/ops/searchsorted_aten_kernels.cc#L351)
- <a id="SearchsortedTensorOut"></a>`SearchsortedTensorOut(const at::Tensor& sorted_sequence, const at::Tensor& values, bool out_int32, bool right, c10::optional<c10::string_view> side, const c10::optional<at::Tensor>& sorter, at::Tensor& out, OpParamCacheKeys&& param_keys)` — [`L372`](../../../../../../raw/code/torch_tpu/csrc/ops/searchsorted_aten_kernels.cc#L372)
- <a id="ValidateSearchsortedInputs"></a>`ValidateSearchsortedInputs(const at::Tensor& sorted, const at::Tensor& values, const c10::optional<at::Tensor>& sorter)` — [`L90`](../../../../../../raw/code/torch_tpu/csrc/ops/searchsorted_aten_kernels.cc#L90)

