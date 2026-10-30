---
title: 'Module: csrc/api/tensor_buffer.cc'
type: catalog
provenance: extracted
module: csrc/api/tensor_buffer.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  MakeTensorBuffer: MakeTensorBuffer(1562c0892b9ac6c6).
  GetBaseTensorBuffer: GetBaseTensorBuffer(4aaf33e43acb5757).
  TensorBufferHandle.state: TensorBufferHandle#state(e86f93d2ea6c1758).
  TensorBufferHandle.size_bytes: TensorBufferHandle#size_bytes(57a65ae535d7db84).
  TensorBufferHandle.Materialize: TensorBufferHandle#Materialize(c8a92d17d58c956f).
  TensorBufferHandle.dimensions: TensorBufferHandle#dimensions(b11922e6bc9fa98a).
  TensorBufferHandle.num_elements: TensorBufferHandle#num_elements(57a65ae535d7db84).
  TensorBufferHandle.AwaitBuffer: TensorBufferHandle#AwaitBuffer(a9916c97d8eea36e).
  TensorBufferHandle.ToTensor: TensorBufferHandle#ToTensor(21e0cbdc9b7087ae).
  TensorBufferHandle.TensorBufferHandle: TensorBufferHandle#TensorBufferHandle(2173cfc7d7a69704).
  TensorBufferHandle.Synchronize: TensorBufferHandle#Synchronize(c8a92d17d58c956f).
  TensorBufferHandle.Impl.buffer_ref: TensorBufferHandle#Impl#buffer_ref(d294d26e35a87f48).
  TensorBufferHandle.Impl: TensorBufferHandle#Impl#
  TensorBufferHandle.Impl.Impl: TensorBufferHandle#Impl#Impl(52d56d831ef57b53).
  TensorBufferHandle.Impl.buffer_ref_: TensorBufferHandle#Impl#buffer_ref_.
  TensorBufferHandle.-TensorBufferHandle: TensorBufferHandle#`~TensorBufferHandle`(ced63f7c635d850d).
  TensorBufferHandle.operator: TensorBufferHandle#`operator=`(5506bb1b58ee7795).
---
# Module: [`csrc/api/tensor_buffer.cc`](../../../../../../raw/code/torch_tpu/csrc/api/tensor_buffer.cc)

## Classes
### <a id="TensorBufferHandle.Impl"></a>`TensorBufferHandle.Impl`
- def: [`csrc/api/tensor_buffer.cc:39`](../../../../../../raw/code/torch_tpu/csrc/api/tensor_buffer.cc#L39)
- signature: `class TensorBufferHandle::Impl`
- members:
  - <a id="TensorBufferHandle.Impl.Impl"></a>`Impl(DeviceBufferRef buffer_ref)` — [`L41`](../../../../../../raw/code/torch_tpu/csrc/api/tensor_buffer.cc#L41)
  - `buffer_ref()` — [`L44`](../../../../../../raw/code/torch_tpu/csrc/api/tensor_buffer.cc#L44)
  - <a id="TensorBufferHandle.Impl.buffer_ref"></a>`buffer_ref()` — [`L45`](../../../../../../raw/code/torch_tpu/csrc/api/tensor_buffer.cc#L45)
  - <a id="TensorBufferHandle.Impl.buffer_ref_"></a>`buffer_ref_` — [`L48`](../../../../../../raw/code/torch_tpu/csrc/api/tensor_buffer.cc#L48)
- uses (calls/refs, reference-scoped): [`DeviceBufferRef`](../eager/device_buffer.h.md#DeviceBufferRef), [`DeviceBufferRef`](../eager/device_buffer.h.md#DeviceBufferRef.DeviceBufferRef), [`TensorBufferHandle`](tensor_buffer.h.md#TensorBufferHandle)
- used by: [`MakeTensorBuffer`](tensor_buffer.cc.md#MakeTensorBuffer), [`GetBaseTensorBuffer`](tensor_buffer.cc.md#GetBaseTensorBuffer), [`state`](tensor_buffer.cc.md#TensorBufferHandle.state), [`operator=`](tensor_buffer.h.md#TensorBufferHandle.operator), [`size_bytes`](tensor_buffer.cc.md#TensorBufferHandle.size_bytes), [`Materialize`](tensor_buffer.cc.md#TensorBufferHandle.Materialize), [`dimensions`](tensor_buffer.cc.md#TensorBufferHandle.dimensions), [`num_elements`](tensor_buffer.cc.md#TensorBufferHandle.num_elements), [`AwaitBuffer`](tensor_buffer.cc.md#TensorBufferHandle.AwaitBuffer), [`ToTensor`](tensor_buffer.cc.md#TensorBufferHandle.ToTensor), [`Synchronize`](tensor_buffer.cc.md#TensorBufferHandle.Synchronize), [`TensorBufferHandle`](tensor_buffer.cc.md#TensorBufferHandle.TensorBufferHandle)

## Functions
- <a id="GetBaseTensorBuffer"></a>`GetBaseTensorBuffer(const at::Tensor& tensor)` — [`L105`](../../../../../../raw/code/torch_tpu/csrc/api/tensor_buffer.cc#L105) — Extracts the TensorBufferHandle for the given tensor's base buffer.
- `MakeTensorBuffer(absl_nonnull std::unique_ptr<xla::PjRtBuffer> buffer)` — [`L117`](../../../../../../raw/code/torch_tpu/csrc/api/tensor_buffer.cc#L117) — Creates a TensorBufferHandle from an owned materialized PjRtBuffer.
- <a id="MakeTensorBuffer"></a>`MakeTensorBuffer(absl_nonnull std::unique_ptr<xla::PjRtBuffer> buffer)` — [`L117`](../../../../../../raw/code/torch_tpu/csrc/api/tensor_buffer.cc#L117) — Creates a TensorBufferHandle from an owned materialized PjRtBuffer.

## Other members
- `TensorBufferHandle` — [`L51`](../../../../../../raw/code/torch_tpu/csrc/api/tensor_buffer.cc#L51)
- `TensorBufferHandle` — [`L51`](../../../../../../raw/code/torch_tpu/csrc/api/tensor_buffer.cc#L51)
- <a id="TensorBufferHandle.-TensorBufferHandle"></a>`TensorBufferHandle.-TensorBufferHandle` — [`L60`](../../../../../../raw/code/torch_tpu/csrc/api/tensor_buffer.cc#L60)
- <a id="TensorBufferHandle.AwaitBuffer"></a>`TensorBufferHandle.AwaitBuffer` — [`L97`](../../../../../../raw/code/torch_tpu/csrc/api/tensor_buffer.cc#L97)
- <a id="TensorBufferHandle.Materialize"></a>`TensorBufferHandle.Materialize` — [`L90`](../../../../../../raw/code/torch_tpu/csrc/api/tensor_buffer.cc#L90)
- <a id="TensorBufferHandle.Synchronize"></a>`TensorBufferHandle.Synchronize` — [`L101`](../../../../../../raw/code/torch_tpu/csrc/api/tensor_buffer.cc#L101)
- <a id="TensorBufferHandle.TensorBufferHandle"></a>`TensorBufferHandle.TensorBufferHandle` — [`L54`](../../../../../../raw/code/torch_tpu/csrc/api/tensor_buffer.cc#L54)
- <a id="TensorBufferHandle.ToTensor"></a>`TensorBufferHandle.ToTensor` — [`L112`](../../../../../../raw/code/torch_tpu/csrc/api/tensor_buffer.cc#L112)
- <a id="TensorBufferHandle.dimensions"></a>`TensorBufferHandle.dimensions` — [`L66`](../../../../../../raw/code/torch_tpu/csrc/api/tensor_buffer.cc#L66)
- <a id="TensorBufferHandle.num_elements"></a>`TensorBufferHandle.num_elements` — [`L70`](../../../../../../raw/code/torch_tpu/csrc/api/tensor_buffer.cc#L70)
- <a id="TensorBufferHandle.operator"></a>`TensorBufferHandle.operator` — [`L57`](../../../../../../raw/code/torch_tpu/csrc/api/tensor_buffer.cc#L57)
- <a id="TensorBufferHandle.size_bytes"></a>`TensorBufferHandle.size_bytes` — [`L62`](../../../../../../raw/code/torch_tpu/csrc/api/tensor_buffer.cc#L62)
- <a id="TensorBufferHandle.state"></a>`TensorBufferHandle.state` — [`L74`](../../../../../../raw/code/torch_tpu/csrc/api/tensor_buffer.cc#L74)

