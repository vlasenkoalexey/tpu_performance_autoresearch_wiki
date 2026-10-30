---
title: 'Module: csrc/internal/batch_transfer/batch_transfer_impl.cc'
type: catalog
provenance: extracted
module: csrc/internal/batch_transfer/batch_transfer_impl.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  TorchTpuPyBindInitModule_batch_transfer_impl: TorchTpuPyBindInitModule_batch_transfer_impl(d5b68cea704bb038).
  PyBatchTransferH2DSync: PyBatchTransferH2DSync(baa530870c63c94).
  PyBatchTransferD2HSync: PyBatchTransferD2HSync(baa530870c63c94).
  PyBatchTransferD2H: PyBatchTransferD2H(666fac275f453526).
  PyBatchTransferH2D: PyBatchTransferH2D(666fac275f453526).
  pybind11_init_batch_transfer_impl: pybind11_init_batch_transfer_impl(85901dfccbeca8c6).
  pybind11_exec_batch_transfer_impl: pybind11_exec_batch_transfer_impl(6642082b04e1bfd8).
  PyAwaitAll: PyAwaitAll(8c3a4e5aeb5bbb9f).
---
# Module: [`csrc/internal/batch_transfer/batch_transfer_impl.cc`](../../../../../../../raw/code/torch_tpu/csrc/internal/batch_transfer/batch_transfer_impl.cc)

## Functions
- <a id="PyAwaitAll"></a>`PyAwaitAll(std::vector<TransferFuture>& futures)` — [`L108`](../../../../../../../raw/code/torch_tpu/csrc/internal/batch_transfer/batch_transfer_impl.cc#L108)
- <a id="PyBatchTransferD2H"></a>`PyBatchTransferD2H(const std::vector<at::Tensor>& src_arrs, const std::vector<at::Tensor>& dst_arrs, const std::vector<int64_t>& src_offsets_major_dim, const std::vector<int64_t>& dst_offsets_major_dim, const std::vector<int64_t>& copy_sizes_major_dim)` — [`L70`](../../../../../../../raw/code/torch_tpu/csrc/internal/batch_transfer/batch_transfer_impl.cc#L70)
- <a id="PyBatchTransferD2HSync"></a>`PyBatchTransferD2HSync(const std::vector<at::Tensor>& src_arrs, const std::vector<at::Tensor>& dst_arrs, const std::vector<int64_t>& src_offsets_major_dim, const std::vector<int64_t>& dst_offsets_major_dim, const std::vector<int64_t>& copy_sizes_major_dim)` — [`L36`](../../../../../../../raw/code/torch_tpu/csrc/internal/batch_transfer/batch_transfer_impl.cc#L36)
- <a id="PyBatchTransferH2D"></a>`PyBatchTransferH2D(const std::vector<at::Tensor>& src_arrs, const std::vector<at::Tensor>& dst_arrs, const std::vector<int64_t>& src_offsets_major_dim, const std::vector<int64_t>& dst_offsets_major_dim, const std::vector<int64_t>& copy_sizes_major_dim)` — [`L89`](../../../../../../../raw/code/torch_tpu/csrc/internal/batch_transfer/batch_transfer_impl.cc#L89)
- <a id="PyBatchTransferH2DSync"></a>`PyBatchTransferH2DSync(const std::vector<at::Tensor>& src_arrs, const std::vector<at::Tensor>& dst_arrs, const std::vector<int64_t>& src_offsets_major_dim, const std::vector<int64_t>& dst_offsets_major_dim, const std::vector<int64_t>& copy_sizes_major_dim)` — [`L53`](../../../../../../../raw/code/torch_tpu/csrc/internal/batch_transfer/batch_transfer_impl.cc#L53)
- <a id="TorchTpuPyBindInitModule_batch_transfer_impl"></a>`TorchTpuPyBindInitModule_batch_transfer_impl(batch_transfer_impl, m)` — [`L115`](../../../../../../../raw/code/torch_tpu/csrc/internal/batch_transfer/batch_transfer_impl.cc#L115)
- <a id="pybind11_exec_batch_transfer_impl"></a>`pybind11_exec_batch_transfer_impl(batch_transfer_impl, m)` — [`L115`](../../../../../../../raw/code/torch_tpu/csrc/internal/batch_transfer/batch_transfer_impl.cc#L115)
- <a id="pybind11_init_batch_transfer_impl"></a>`pybind11_init_batch_transfer_impl(batch_transfer_impl, m)` — [`L115`](../../../../../../../raw/code/torch_tpu/csrc/internal/batch_transfer/batch_transfer_impl.cc#L115)

