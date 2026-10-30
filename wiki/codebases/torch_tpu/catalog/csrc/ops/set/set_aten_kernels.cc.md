---
title: 'Module: csrc/ops/set/set_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/set/set_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenSet_SourceStorageOffset: AtenSet_SourceStorageOffset(aaa542379ec5fd41).
  AtenSet_: AtenSet_(2c0150b1d2cc4760).
  AtenSet_SourceStorage: AtenSet_SourceStorage(bbdf7f938843f44b).
  AtenSet_SourceTensor: AtenSet_SourceTensor(a07b299543d5b449).
---
# Module: [`csrc/ops/set/set_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/set/set_aten_kernels.cc)

## Functions
- <a id="AtenSet_"></a>`AtenSet_(at::Tensor& self)` — [`L41`](../../../../../../../raw/code/torch_tpu/csrc/ops/set/set_aten_kernels.cc#L41) — Sets tensor `self` to have a zero-element storage.
- <a id="AtenSet_SourceStorage"></a>`AtenSet_SourceStorage(at::Tensor& self, c10::Storage src)` — [`L56`](../../../../../../../raw/code/torch_tpu/csrc/ops/set/set_aten_kernels.cc#L56) — Sets tensor `self` to have storage `src`. The size/strides/offset
- <a id="AtenSet_SourceStorageOffset"></a>`AtenSet_SourceStorageOffset(at::Tensor& self, c10::Storage src, c10::SymInt storage_offset, c10::SymIntArrayRef size, c10::SymIntArrayRef stride)` — [`L70`](../../../../../../../raw/code/torch_tpu/csrc/ops/set/set_aten_kernels.cc#L70) — Sets tensor `self` to have the provided storage, offset, sizes, and strides.
- <a id="AtenSet_SourceTensor"></a>`AtenSet_SourceTensor(at::Tensor& self, const at::Tensor& src)` — [`L109`](../../../../../../../raw/code/torch_tpu/csrc/ops/set/set_aten_kernels.cc#L109) — Sets tensor `self` to have the storage, offset, sizes, and strides

