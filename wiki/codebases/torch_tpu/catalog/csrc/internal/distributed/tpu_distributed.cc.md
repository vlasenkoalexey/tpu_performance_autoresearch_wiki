---
title: 'Module: csrc/internal/distributed/tpu_distributed.cc'
type: catalog
provenance: extracted
module: csrc/internal/distributed/tpu_distributed.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  TorchTpuPyBindInitModule_tpu_distributed: TorchTpuPyBindInitModule_tpu_distributed(d5b68cea704bb038).
  GetGlobalDeviceId: '`$anonymous_namespace_csrc/internal/distributed/tpu_distributed.cc`/GetGlobalDeviceId(b126dc7c1de90089).'
  GetLocalDeviceCoords: '`$anonymous_namespace_csrc/internal/distributed/tpu_distributed.cc`/GetLocalDeviceCoords(1fb450f42081f91b).'
  GetAllGlobalDeviceIds: '`$anonymous_namespace_csrc/internal/distributed/tpu_distributed.cc`/GetAllGlobalDeviceIds(95cc8889724c44b9).'
  DeviceDebugString: '`$anonymous_namespace_csrc/internal/distributed/tpu_distributed.cc`/DeviceDebugString(efd28698952f529a).'
  pybind11_init_tpu_distributed: pybind11_init_tpu_distributed(85901dfccbeca8c6).
  pybind11_exec_tpu_distributed: pybind11_exec_tpu_distributed(6642082b04e1bfd8).
  GetRankToDeviceId: '`$anonymous_namespace_csrc/internal/distributed/tpu_distributed.cc`/GetRankToDeviceId(6f63495200e65d10).'
  MakeProcessGroup: '`$anonymous_namespace_csrc/internal/distributed/tpu_distributed.cc`/MakeProcessGroup(15bd278ca9640a16).'
---
# Module: [`csrc/internal/distributed/tpu_distributed.cc`](../../../../../../../raw/code/torch_tpu/csrc/internal/distributed/tpu_distributed.cc)

## Functions
- <a id="DeviceDebugString"></a>`DeviceDebugString()` — [`L86`](../../../../../../../raw/code/torch_tpu/csrc/internal/distributed/tpu_distributed.cc#L86)
- <a id="GetAllGlobalDeviceIds"></a>`GetAllGlobalDeviceIds()` — [`L72`](../../../../../../../raw/code/torch_tpu/csrc/internal/distributed/tpu_distributed.cc#L72)
- <a id="GetGlobalDeviceId"></a>`GetGlobalDeviceId()` — [`L65`](../../../../../../../raw/code/torch_tpu/csrc/internal/distributed/tpu_distributed.cc#L65) — Global device id of the (single) addressable device this process is using.
- <a id="GetLocalDeviceCoords"></a>`GetLocalDeviceCoords()` — [`L95`](../../../../../../../raw/code/torch_tpu/csrc/internal/distributed/tpu_distributed.cc#L95) — Returns physical grid coordinates (e.g. [x, y, z]) of the local PJRT device
- <a id="GetRankToDeviceId"></a>`GetRankToDeviceId(c10::intrusive_ptr<c10d::Backend> backend)` — [`L55`](../../../../../../../raw/code/torch_tpu/csrc/internal/distributed/tpu_distributed.cc#L55)
- <a id="MakeProcessGroup"></a>`MakeProcessGroup(c10::intrusive_ptr<c10d::Store> store, int rank, int size, std::chrono::duration<float>& timeout)` — [`L49`](../../../../../../../raw/code/torch_tpu/csrc/internal/distributed/tpu_distributed.cc#L49) — This function will be registered as the TPU distributed backend init
- <a id="TorchTpuPyBindInitModule_tpu_distributed"></a>`TorchTpuPyBindInitModule_tpu_distributed(tpu_distributed, m)` — [`L111`](../../../../../../../raw/code/torch_tpu/csrc/internal/distributed/tpu_distributed.cc#L111)
- <a id="pybind11_exec_tpu_distributed"></a>`pybind11_exec_tpu_distributed(tpu_distributed, m)` — [`L111`](../../../../../../../raw/code/torch_tpu/csrc/internal/distributed/tpu_distributed.cc#L111)
- <a id="pybind11_init_tpu_distributed"></a>`pybind11_init_tpu_distributed(tpu_distributed, m)` — [`L111`](../../../../../../../raw/code/torch_tpu/csrc/internal/distributed/tpu_distributed.cc#L111)

