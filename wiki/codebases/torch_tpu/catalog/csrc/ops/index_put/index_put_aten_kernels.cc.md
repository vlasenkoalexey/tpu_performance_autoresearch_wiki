---
title: 'Module: csrc/ops/index_put/index_put_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/index_put/index_put_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  IndexPut: '`$anonymous_namespace_csrc/ops/index_put/index_put_aten_kernels.cc`/IndexPut(e42ab2b752f9b412).'
  TpuAtenIndexPutImpl_: TpuAtenIndexPutImpl_(ebe15a99ad8c0822).
  IndexPutWithBooleanMask: '`$anonymous_namespace_csrc/ops/index_put/index_put_aten_kernels.cc`/IndexPutWithBooleanMask(c3048f53c0b130c2).'
  IndexPutHelper: '`$anonymous_namespace_csrc/ops/index_put/index_put_aten_kernels.cc`/IndexPutHelper(e42ab2b752f9b412).'
  GetIndexBroadcastShape: '`$anonymous_namespace_csrc/ops/index_put/index_put_aten_kernels.cc`/GetIndexBroadcastShape(5d23fa4ee320ac78).'
  ConvertBooleanIndicesToPositional: '`$anonymous_namespace_csrc/ops/index_put/index_put_aten_kernels.cc`/ConvertBooleanIndicesToPositional(ad28fb4a56989085).'
  ValidateIndicesType: '`$anonymous_namespace_csrc/ops/index_put/index_put_aten_kernels.cc`/ValidateIndicesType(1cc5d988ef3b9d0).'
  GetValuesBroadcastShape: '`$anonymous_namespace_csrc/ops/index_put/index_put_aten_kernels.cc`/GetValuesBroadcastShape(9458d5ab49d94f42).'
  MoveIndicesToFront: '`$anonymous_namespace_csrc/ops/index_put/index_put_aten_kernels.cc`/MoveIndicesToFront(e143bef23f76a1de).'
  CanUseSelectWithValues: '`$anonymous_namespace_csrc/ops/index_put/index_put_aten_kernels.cc`/CanUseSelectWithValues(6d281b1aa85f6031).'
  AreIndicesContiguous: '`$anonymous_namespace_csrc/ops/index_put/index_put_aten_kernels.cc`/AreIndicesContiguous(3af0d499e8ef0de).'
  GetSingleBooleanMaskInfo: '`$anonymous_namespace_csrc/ops/index_put/index_put_aten_kernels.cc`/GetSingleBooleanMaskInfo(3051e14e3babfe12).'
  BooleanMaskInfo.mask_dim: '`$anonymous_namespace_csrc/ops/index_put/index_put_aten_kernels.cc`/BooleanMaskInfo#mask_dim.'
  BooleanMaskInfo.index_start_dim: '`$anonymous_namespace_csrc/ops/index_put/index_put_aten_kernels.cc`/BooleanMaskInfo#index_start_dim.'
  BooleanMaskInfo: '`$anonymous_namespace_csrc/ops/index_put/index_put_aten_kernels.cc`/BooleanMaskInfo#'
---
# Module: [`csrc/ops/index_put/index_put_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/index_put/index_put_aten_kernels.cc)

## Classes
### <a id="BooleanMaskInfo"></a>`BooleanMaskInfo`
- def: [`csrc/ops/index_put/index_put_aten_kernels.cc:302`](../../../../../../../raw/code/torch_tpu/csrc/ops/index_put/index_put_aten_kernels.cc#L302)
- signature: `struct BooleanMaskInfo`
- members:
  - <a id="BooleanMaskInfo.index_start_dim"></a>`index_start_dim` — [`L303`](../../../../../../../raw/code/torch_tpu/csrc/ops/index_put/index_put_aten_kernels.cc#L303)
  - <a id="BooleanMaskInfo.mask_dim"></a>`mask_dim` — [`L304`](../../../../../../../raw/code/torch_tpu/csrc/ops/index_put/index_put_aten_kernels.cc#L304)
- used by: [`IndexPutHelper`](index_put_aten_kernels.cc.md#IndexPutHelper), [`GetSingleBooleanMaskInfo`](index_put_aten_kernels.cc.md#GetSingleBooleanMaskInfo)

## Functions
- <a id="AreIndicesContiguous"></a>`AreIndicesContiguous(const Indices& indexed_dims)` — [`L159`](../../../../../../../raw/code/torch_tpu/csrc/ops/index_put/index_put_aten_kernels.cc#L159)
- <a id="CanUseSelectWithValues"></a>`CanUseSelectWithValues(const at::Tensor& self, const at::Tensor& values, int64_t index_start_dim, int64_t mask_dim)` — [`L342`](../../../../../../../raw/code/torch_tpu/csrc/ops/index_put/index_put_aten_kernels.cc#L342) — Returns true if the values tensor can be broadcast into self for a boolean
- `ConvertBooleanIndicesToPositional(const at::Tensor& self, const c10::List<std::optional<at::Tensor>>& indices_list_opt, Indices& indexed_dims)` — [`L109`](../../../../../../../raw/code/torch_tpu/csrc/ops/index_put/index_put_aten_kernels.cc#L109) — Preprocesses indices tensor list by converting boolean tensor masks into
- <a id="ConvertBooleanIndicesToPositional"></a>`ConvertBooleanIndicesToPositional(const at::Tensor& self, const c10::List<std::optional<at::Tensor>>& indices_list_opt, Indices& indexed_dims)` — [`L109`](../../../../../../../raw/code/torch_tpu/csrc/ops/index_put/index_put_aten_kernels.cc#L109) — Preprocesses indices tensor list by converting boolean tensor masks into
- `GetIndexBroadcastShape(const std::vector<at::Tensor>& index_tensors)` — [`L222`](../../../../../../../raw/code/torch_tpu/csrc/ops/index_put/index_put_aten_kernels.cc#L222) — Computes the common broadcast shape of the tensors in the 'indices' list.
- <a id="GetIndexBroadcastShape"></a>`GetIndexBroadcastShape(const std::vector<at::Tensor>& index_tensors)` — [`L222`](../../../../../../../raw/code/torch_tpu/csrc/ops/index_put/index_put_aten_kernels.cc#L222) — Computes the common broadcast shape of the tensors in the 'indices' list.
- <a id="GetSingleBooleanMaskInfo"></a>`GetSingleBooleanMaskInfo(const c10::List<std::optional<at::Tensor>>& indices_list_opt)` — [`L308`](../../../../../../../raw/code/torch_tpu/csrc/ops/index_put/index_put_aten_kernels.cc#L308) — Returns mask info if the indices list contains a single boolean index tensor.
- <a id="GetValuesBroadcastShape"></a>`GetValuesBroadcastShape(const at::Tensor& self, const at::Tensor& values, const Dimensions& index_broadcast_shape, int64_t index_start_dim, int64_t index_end_dim)` — [`L262`](../../../../../../../raw/code/torch_tpu/csrc/ops/index_put/index_put_aten_kernels.cc#L262) — Computes the shape that the values tensor is broadcastable to.
- <a id="IndexPut"></a>`IndexPut(at::Tensor& self, const c10::List<std::optional<at::Tensor>>& indices_list_opt, const at::Tensor& values, const bool accumulate, at::Tensor& out)` — [`L399`](../../../../../../../raw/code/torch_tpu/csrc/ops/index_put/index_put_aten_kernels.cc#L399)
- <a id="IndexPutHelper"></a>`IndexPutHelper(at::Tensor& self, const c10::List<std::optional<at::Tensor>>& indices_list_opt, const at::Tensor& values, const bool accumulate, at::Tensor& out)` — [`L484`](../../../../../../../raw/code/torch_tpu/csrc/ops/index_put/index_put_aten_kernels.cc#L484)
- <a id="IndexPutWithBooleanMask"></a>`IndexPutWithBooleanMask(const at::Tensor& self, const at::Tensor& mask, int64_t index_start_dim, const at::Tensor& values, const bool accumulate, at::Tensor& out)` — [`L363`](../../../../../../../raw/code/torch_tpu/csrc/ops/index_put/index_put_aten_kernels.cc#L363) — When the indices contain a boolean mask and the values tensor does not vary
- `MoveIndicesToFront(const at::Tensor& self, std::vector<at::Tensor>& index_tensors, const Indices& indexed_dims)` — [`L180`](../../../../../../../raw/code/torch_tpu/csrc/ops/index_put/index_put_aten_kernels.cc#L180) — Moves the indexed dimensions of 'self' to the front of the tensor.
- <a id="MoveIndicesToFront"></a>`MoveIndicesToFront(const at::Tensor& self, std::vector<at::Tensor>& index_tensors, const Indices& indexed_dims)` — [`L180`](../../../../../../../raw/code/torch_tpu/csrc/ops/index_put/index_put_aten_kernels.cc#L180) — Moves the indexed dimensions of 'self' to the front of the tensor.
- <a id="TpuAtenIndexPutImpl_"></a>`TpuAtenIndexPutImpl_(at::Tensor& self, const c10::List<std::optional<at::Tensor>>& indices, const at::Tensor& values, bool accumulate, bool unsafe)` — [`L525`](../../../../../../../raw/code/torch_tpu/csrc/ops/index_put/index_put_aten_kernels.cc#L525) — These function implements the behavior of torch.index_put for the TPU backend
- <a id="ValidateIndicesType"></a>`ValidateIndicesType(const c10::List<std::optional<at::Tensor>>& indices_list_opt)` — [`L56`](../../../../../../../raw/code/torch_tpu/csrc/ops/index_put/index_put_aten_kernels.cc#L56)

