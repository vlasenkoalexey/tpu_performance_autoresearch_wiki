---
title: 'Module: csrc/internal/sync/sync_py.cc'
type: catalog
provenance: extracted
module: csrc/internal/sync/sync_py.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  TrySyncSingleTensorFast: '`$anonymous_namespace_csrc/internal/sync/sync_py.cc`/TrySyncSingleTensorFast(124256bd5c1b3ac9).'
  TrySyncTensorArrayFast: '`$anonymous_namespace_csrc/internal/sync/sync_py.cc`/TrySyncTensorArrayFast(74695259b9bd8b66).'
  PySyncSpanNoWait: '`$anonymous_namespace_csrc/internal/sync/sync_py.cc`/PySyncSpanNoWait(5f9ed022cae69262).'
  PyIsMaterialized: '`$anonymous_namespace_csrc/internal/sync/sync_py.cc`/PyIsMaterialized(a100227fc274154c).'
  PyIsMaterializing: '`$anonymous_namespace_csrc/internal/sync/sync_py.cc`/PyIsMaterializing(a100227fc274154c).'
  PySyncSpan: '`$anonymous_namespace_csrc/internal/sync/sync_py.cc`/PySyncSpan(99568ea3285cdb43).'
  TorchTpuPyBindInitModule__tpu_torch_sync: TorchTpuPyBindInitModule__tpu_torch_sync(d5b68cea704bb038).
  PyGetComputationGraphviz: '`$anonymous_namespace_csrc/internal/sync/sync_py.cc`/PyGetComputationGraphviz(6662052fc345a2aa).'
  PyGetComputationMlir: '`$anonymous_namespace_csrc/internal/sync/sync_py.cc`/PyGetComputationMlir(87b5e875a5dc1a2b).'
  PySynchronizeDevice: '`$anonymous_namespace_csrc/internal/sync/sync_py.cc`/PySynchronizeDevice(b45ddcbc8423892c).'
  GetComputationBuffers: '`$anonymous_namespace_csrc/internal/sync/sync_py.cc`/GetComputationBuffers(d1184c7e660e2e25).'
  PySynchronize: '`$anonymous_namespace_csrc/internal/sync/sync_py.cc`/PySynchronize(1c88272df8318556).'
  UnwrapTensor: '`$anonymous_namespace_csrc/internal/sync/sync_py.cc`/UnwrapTensor(5ab30da59d95c0f0).'
  PySynchronizeSequence: '`$anonymous_namespace_csrc/internal/sync/sync_py.cc`/PySynchronizeSequence(9791f61ad17becff).'
  GetComputationGraph: '`$anonymous_namespace_csrc/internal/sync/sync_py.cc`/GetComputationGraph(5ee1e24e6473c5df).'
  AllTensorsAreDenseOnDevice: '`$anonymous_namespace_csrc/internal/sync/sync_py.cc`/AllTensorsAreDenseOnDevice(e2e57961db7696a9).'
  BufferRefToVarMap: BufferRefToVarMap#
  pybind11_exec__tpu_torch_sync: pybind11_exec__tpu_torch_sync(6642082b04e1bfd8).
  pybind11_init__tpu_torch_sync: pybind11_init__tpu_torch_sync(85901dfccbeca8c6).
  PySync: '`$anonymous_namespace_csrc/internal/sync/sync_py.cc`/PySync(4052d139d6cf6382).'
---
# Module: [`csrc/internal/sync/sync_py.cc`](../../../../../../../raw/code/torch_tpu/csrc/internal/sync/sync_py.cc)

## Classes
### <a id="BufferRefToVarMap"></a>`BufferRefToVarMap`
- def: [`csrc/internal/sync/sync_py.cc:47`](../../../../../../../raw/code/torch_tpu/csrc/internal/sync/sync_py.cc#L47) — documented in [tensor-synchronization](../../../../concepts/tensor-synchronization.md)
- signature: `using BufferRefToVarMap = absl::flat_hash_map<DeviceBufferRef, std::string>`
- uses (calls/refs, reference-scoped): [`DeviceBufferRef`](../../eager/device_buffer.h.md#DeviceBufferRef)
- used by: [`GetComputationGraphviz`](sync.cc.md#GetComputationGraphviz), [`GetComputationBuffers`](sync_py.cc.md#GetComputationBuffers)

## Functions
- <a id="AllTensorsAreDenseOnDevice"></a>`AllTensorsAreDenseOnDevice(absl::Span<const at::Tensor> tensors)` — [`L67`](../../../../../../../raw/code/torch_tpu/csrc/internal/sync/sync_py.cc#L67) — documented in [tensor-synchronization](../../../../concepts/tensor-synchronization.md)
- <a id="GetComputationBuffers"></a>`GetComputationBuffers(const std::vector<at::Tensor>& tensors)` — [`L415`](../../../../../../../raw/code/torch_tpu/csrc/internal/sync/sync_py.cc#L415) — documented in [tensor-synchronization](../../../../concepts/tensor-synchronization.md)
- <a id="GetComputationGraph"></a>`GetComputationGraph(py::dict capture_names_from)` — [`L426`](../../../../../../../raw/code/torch_tpu/csrc/internal/sync/sync_py.cc#L426) — documented in [tensor-synchronization](../../../../concepts/tensor-synchronization.md)
- <a id="PyGetComputationGraphviz"></a>`PyGetComputationGraphviz(const std::vector<at::Tensor>& tensors, py::dict capture_names_from)` — [`L443`](../../../../../../../raw/code/torch_tpu/csrc/internal/sync/sync_py.cc#L443) — Returns a graphviz compatible representation of the computation graph of the — documented in [tensor-synchronization](../../../../concepts/tensor-synchronization.md)
- <a id="PyGetComputationMlir"></a>`PyGetComputationMlir(const std::vector<at::Tensor>& tensors)` — [`L456`](../../../../../../../raw/code/torch_tpu/csrc/internal/sync/sync_py.cc#L456) — Returns a MLIR representation of the computation graph of the given tensors. — documented in [tensor-synchronization](../../../../concepts/tensor-synchronization.md)
- <a id="PyIsMaterialized"></a>`PyIsMaterialized(py::handle tensor_obj)` — [`L402`](../../../../../../../raw/code/torch_tpu/csrc/internal/sync/sync_py.cc#L402) — documented in [tensor-synchronization](../../../../concepts/tensor-synchronization.md)
- <a id="PyIsMaterializing"></a>`PyIsMaterializing(py::handle tensor_obj)` — [`L393`](../../../../../../../raw/code/torch_tpu/csrc/internal/sync/sync_py.cc#L393) — documented in [tensor-synchronization](../../../../concepts/tensor-synchronization.md)
- <a id="PySync"></a>`PySync(const std::vector<at::Tensor>& tensors, bool wait)` — [`L159`](../../../../../../../raw/code/torch_tpu/csrc/internal/sync/sync_py.cc#L159) — documented in [tensor-synchronization](../../../../concepts/tensor-synchronization.md)
- <a id="PySyncSpan"></a>`PySyncSpan(absl::Span<const at::Tensor> tensors, bool wait)` — [`L123`](../../../../../../../raw/code/torch_tpu/csrc/internal/sync/sync_py.cc#L123) — documented in [tensor-synchronization](../../../../concepts/tensor-synchronization.md)
- <a id="PySyncSpanNoWait"></a>`PySyncSpanNoWait(absl::Span<const at::Tensor> tensors_span)` — [`L77`](../../../../../../../raw/code/torch_tpu/csrc/internal/sync/sync_py.cc#L77) — documented in [tensor-synchronization](../../../../concepts/tensor-synchronization.md)
- <a id="PySynchronize"></a>`PySynchronize(py::handle tensors, bool wait)` — [`L367`](../../../../../../../raw/code/torch_tpu/csrc/internal/sync/sync_py.cc#L367) — Unified C++ entry point for `torch_tpu.sync.synchronize(tensors, wait)`. — documented in [tensor-synchronization](../../../../concepts/tensor-synchronization.md)
- <a id="PySynchronizeDevice"></a>`PySynchronizeDevice(bool wait)` — [`L305`](../../../../../../../raw/code/torch_tpu/csrc/internal/sync/sync_py.cc#L305) — Synchronizes the entire active TPU device when `synchronize(None, wait=...)` — documented in [tensor-synchronization](../../../../concepts/tensor-synchronization.md)
- <a id="PySynchronizeSequence"></a>`PySynchronizeSequence(PyObject* ptr, bool wait)` — [`L330`](../../../../../../../raw/code/torch_tpu/csrc/internal/sync/sync_py.cc#L330) — documented in [tensor-synchronization](../../../../concepts/tensor-synchronization.md)
- <a id="TorchTpuPyBindInitModule__tpu_torch_sync"></a>`TorchTpuPyBindInitModule__tpu_torch_sync(_tpu_torch_sync, m)` — [`L467`](../../../../../../../raw/code/torch_tpu/csrc/internal/sync/sync_py.cc#L467) — documented in [tensor-synchronization](../../../../concepts/tensor-synchronization.md)
- <a id="TrySyncSingleTensorFast"></a>`TrySyncSingleTensorFast(PyObject* ptr, bool wait)` — [`L180`](../../../../../../../raw/code/torch_tpu/csrc/internal/sync/sync_py.cc#L180) — Fast-path C++ synchronization for a single PyObject* representing a standard — documented in [tensor-synchronization](../../../../concepts/tensor-synchronization.md)
- <a id="TrySyncTensorArrayFast"></a>`TrySyncTensorArrayFast(PyObject* const* items, Py_ssize_t size, bool wait)` — [`L235`](../../../../../../../raw/code/torch_tpu/csrc/internal/sync/sync_py.cc#L235) — Fast-path C++ synchronization for a contiguous `PyObject* const*` array — documented in [tensor-synchronization](../../../../concepts/tensor-synchronization.md)
- <a id="UnwrapTensor"></a>`UnwrapTensor(py::handle obj)` — [`L51`](../../../../../../../raw/code/torch_tpu/csrc/internal/sync/sync_py.cc#L51) — documented in [tensor-synchronization](../../../../concepts/tensor-synchronization.md)
- <a id="pybind11_exec__tpu_torch_sync"></a>`pybind11_exec__tpu_torch_sync(_tpu_torch_sync, m)` — [`L467`](../../../../../../../raw/code/torch_tpu/csrc/internal/sync/sync_py.cc#L467)
- <a id="pybind11_init__tpu_torch_sync"></a>`pybind11_init__tpu_torch_sync(_tpu_torch_sync, m)` — [`L467`](../../../../../../../raw/code/torch_tpu/csrc/internal/sync/sync_py.cc#L467)

