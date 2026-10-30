---
title: 'Module: csrc/ops/copy_from/copy_from_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/copy_from/copy_from_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  CopyTensor: CopyTensor(ad529a7346dded39).
  AtenLocalScalarDense: AtenLocalScalarDense(8e947ca21decbfd7).
  AtenCopy_: AtenCopy_(325b165a1335c5db).
  AtenCopyFromAndResize: AtenCopyFromAndResize(91c7cc726c97ea99).
  AtenCopyFrom: AtenCopyFrom(ad529a7346dded39).
  GetCopyType: '`$anonymous_namespace_csrc/ops/copy_from/copy_from_aten_kernels.cc`/GetCopyType(e89603c510fbf94c).'
  CopyTensorGrad: '`$anonymous_namespace_csrc/ops/copy_from/copy_from_aten_kernels.cc`/CopyTensorGrad(1fed79d2bdf41e88).'
  CopySparseBuffers: '`$anonymous_namespace_csrc/ops/copy_from/copy_from_aten_kernels.cc`/CopySparseBuffers(a739d8591fe47d73).'
  CopyType: '`$anonymous_namespace_csrc/ops/copy_from/copy_from_aten_kernels.cc`/CopyType#'
  CopySparseTensor: '`$anonymous_namespace_csrc/ops/copy_from/copy_from_aten_kernels.cc`/CopySparseTensor(6c13d6b8a5a72092).'
  CopyType.kTpuToCpu: '`$anonymous_namespace_csrc/ops/copy_from/copy_from_aten_kernels.cc`/CopyType#kTpuToCpu.'
  CopyType.kCpuToTpu: '`$anonymous_namespace_csrc/ops/copy_from/copy_from_aten_kernels.cc`/CopyType#kCpuToTpu.'
  CopyType.kTpuToTpu: '`$anonymous_namespace_csrc/ops/copy_from/copy_from_aten_kernels.cc`/CopyType#kTpuToTpu.'
  SparseBuffers: '`$anonymous_namespace_csrc/ops/copy_from/copy_from_aten_kernels.cc`/SparseBuffers#'
  TpuSparseTensorImpl: '`$anonymous_namespace_csrc/ops/copy_from/copy_from_aten_kernels.cc`/TpuSparseTensorImpl#'
  TpuSparseTensorImpl.TpuSparseTensorImpl: '`$anonymous_namespace_csrc/ops/copy_from/copy_from_aten_kernels.cc`/TpuSparseTensorImpl#TpuSparseTensorImpl(33f7962f2f76c766).'
  SparseBuffers.values: '`$anonymous_namespace_csrc/ops/copy_from/copy_from_aten_kernels.cc`/SparseBuffers#values.'
  SparseBuffers.indices: '`$anonymous_namespace_csrc/ops/copy_from/copy_from_aten_kernels.cc`/SparseBuffers#indices.'
---
# Module: [`csrc/ops/copy_from/copy_from_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/copy_from/copy_from_aten_kernels.cc)

## Classes
### <a id="CopyType"></a>`CopyType`
- def: [`csrc/ops/copy_from/copy_from_aten_kernels.cc:55`](../../../../../../../raw/code/torch_tpu/csrc/ops/copy_from/copy_from_aten_kernels.cc#L55) — documented in [host-device-copy](../../../../concepts/host-device-copy.md)
- signature: `enum class CopyType`
- members:
  - <a id="CopyType.kCpuToTpu"></a>`kCpuToTpu` — [`L56`](../../../../../../../raw/code/torch_tpu/csrc/ops/copy_from/copy_from_aten_kernels.cc#L56) — documented in [host-device-copy](../../../../concepts/host-device-copy.md)
  - <a id="CopyType.kTpuToCpu"></a>`kTpuToCpu` — [`L58`](../../../../../../../raw/code/torch_tpu/csrc/ops/copy_from/copy_from_aten_kernels.cc#L58) — documented in [host-device-copy](../../../../concepts/host-device-copy.md)
  - <a id="CopyType.kTpuToTpu"></a>`kTpuToTpu` — [`L57`](../../../../../../../raw/code/torch_tpu/csrc/ops/copy_from/copy_from_aten_kernels.cc#L57) — documented in [host-device-copy](../../../../concepts/host-device-copy.md)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`CopyTensor`](copy_from_aten_kernels.cc.md#CopyTensor), [`GetCopyType`](copy_from_aten_kernels.cc.md#GetCopyType), [`CopyTensorGrad`](copy_from_aten_kernels.cc.md#CopyTensorGrad), [`CopySparseBuffers`](copy_from_aten_kernels.cc.md#CopySparseBuffers), [`CopySparseTensor`](copy_from_aten_kernels.cc.md#CopySparseTensor)

### <a id="SparseBuffers"></a>`SparseBuffers`
- def: [`csrc/ops/copy_from/copy_from_aten_kernels.cc:85`](../../../../../../../raw/code/torch_tpu/csrc/ops/copy_from/copy_from_aten_kernels.cc#L85) — documented in [host-device-copy](../../../../concepts/host-device-copy.md)
- signature: `struct SparseBuffers`
- members:
  - <a id="SparseBuffers.indices"></a>`indices` — [`L86`](../../../../../../../raw/code/torch_tpu/csrc/ops/copy_from/copy_from_aten_kernels.cc#L86) — UNINITIALIZED_TENSOR_OK=Struct field initialized by — documented in [host-device-copy](../../../../concepts/host-device-copy.md)
  - <a id="SparseBuffers.values"></a>`values` — [`L88`](../../../../../../../raw/code/torch_tpu/csrc/ops/copy_from/copy_from_aten_kernels.cc#L88) — UNINITIALIZED_TENSOR_OK=Struct field initialized by — documented in [host-device-copy](../../../../concepts/host-device-copy.md)
- uses (calls/refs, reference-scoped): (none in-repo)

### <a id="TpuSparseTensorImpl"></a>`TpuSparseTensorImpl`  ·  implements/extends SparseTensorImpl, TensorImpl, intrusive_ptr_target
- def: [`csrc/ops/copy_from/copy_from_aten_kernels.cc:123`](../../../../../../../raw/code/torch_tpu/csrc/ops/copy_from/copy_from_aten_kernels.cc#L123) — documented in [host-device-copy](../../../../concepts/host-device-copy.md)
- signature: `struct TpuSparseTensorImpl final : public at::SparseTensorImpl`
- members:
  - <a id="TpuSparseTensorImpl.TpuSparseTensorImpl"></a>`TpuSparseTensorImpl(const at::DispatchKeySet key_set, const caffe2::TypeMeta data_type, const c10::Device device)` — [`L124`](../../../../../../../raw/code/torch_tpu/csrc/ops/copy_from/copy_from_aten_kernels.cc#L124) — documented in [host-device-copy](../../../../concepts/host-device-copy.md)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`CopySparseTensor`](copy_from_aten_kernels.cc.md#CopySparseTensor)

## Functions
- <a id="AtenCopyFrom"></a>`AtenCopyFrom(const at::Tensor& src, const at::Tensor& self_dest, bool non_blocking)` — [`L232`](../../../../../../../raw/code/torch_tpu/csrc/ops/copy_from/copy_from_aten_kernels.cc#L232) — Updates the c10::Storage of self_dest to point to a new c10::StorageImpl — documented in [host-device-copy](../../../../concepts/host-device-copy.md)
- <a id="AtenCopyFromAndResize"></a>`AtenCopyFromAndResize(const at::Tensor& self, const at::Tensor& dst)` — [`L241`](../../../../../../../raw/code/torch_tpu/csrc/ops/copy_from/copy_from_aten_kernels.cc#L241) — By going through its usage in ATen/native/CPUFallback.cpp. This function is — documented in [host-device-copy](../../../../concepts/host-device-copy.md)
- <a id="AtenCopy_"></a>`AtenCopy_(at::Tensor& self, const at::Tensor& src, bool non_blocking)` — [`L268`](../../../../../../../raw/code/torch_tpu/csrc/ops/copy_from/copy_from_aten_kernels.cc#L268) — Identical to _copy_from, only registered to avoid a dispatch error in torch. — documented in [host-device-copy](../../../../concepts/host-device-copy.md)
- <a id="AtenLocalScalarDense"></a>`AtenLocalScalarDense(const at::Tensor& self)` — [`L254`](../../../../../../../raw/code/torch_tpu/csrc/ops/copy_from/copy_from_aten_kernels.cc#L254) — Copies a 1-element tensor from TPU to CPU and converts it to a scalar. — documented in [host-device-copy](../../../../concepts/host-device-copy.md)
- <a id="CopySparseBuffers"></a>`CopySparseBuffers(const at::Tensor& src_sparse, const at::Tensor& target_ref, CopyType to_copy_type, bool non_blocking)` — [`L92`](../../../../../../../raw/code/torch_tpu/csrc/ops/copy_from/copy_from_aten_kernels.cc#L92) — documented in [host-device-copy](../../../../concepts/host-device-copy.md)
- <a id="CopySparseTensor"></a>`CopySparseTensor(const at::Tensor& src_sparse, const at::Tensor& target_ref, CopyType to_copy_type, bool non_blocking)` — [`L134`](../../../../../../../raw/code/torch_tpu/csrc/ops/copy_from/copy_from_aten_kernels.cc#L134) — documented in [host-device-copy](../../../../concepts/host-device-copy.md)
- <a id="CopyTensor"></a>`CopyTensor(const at::Tensor& src, const at::Tensor& self_dest, bool non_blocking)` — [`L189`](../../../../../../../raw/code/torch_tpu/csrc/ops/copy_from/copy_from_aten_kernels.cc#L189) — Copies `src` tensor contents to `self_dest` tensor. — documented in [host-device-copy](../../../../concepts/host-device-copy.md)
- <a id="CopyTensorGrad"></a>`CopyTensorGrad(const at::Tensor& src, const at::Tensor& self_dest, CopyType to_copy_type, bool non_blocking)` — [`L157`](../../../../../../../raw/code/torch_tpu/csrc/ops/copy_from/copy_from_aten_kernels.cc#L157) — documented in [host-device-copy](../../../../concepts/host-device-copy.md)
- <a id="GetCopyType"></a>`GetCopyType(const at::Tensor& src, const at::Tensor& dest)` — [`L61`](../../../../../../../raw/code/torch_tpu/csrc/ops/copy_from/copy_from_aten_kernels.cc#L61) — documented in [host-device-copy](../../../../concepts/host-device-copy.md)

