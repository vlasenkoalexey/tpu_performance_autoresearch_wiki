---
title: 'Module: csrc/api/tensor_buffer.h'
type: catalog
provenance: extracted
module: csrc/api/tensor_buffer.h
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  TensorBufferHandle: TensorBufferHandle#
  TensorBufferHandle.operator: TensorBufferHandle#`operator=`(4c180269bad7994c).
  TensorBufferHandle.impl_: TensorBufferHandle#impl_.
  DeviceBufferState: DeviceBufferState#
  DeviceBufferState.kDeferred: DeviceBufferState#kDeferred.
  DeviceBufferState.kMaterialized: DeviceBufferState#kMaterialized.
  TensorBufferHandle.TensorBufferHandle: TensorBufferHandle#TensorBufferHandle(7ff6a86d49d40381).
  DeviceBufferState.kPlaceholder: DeviceBufferState#kPlaceholder.
  DeviceBufferState.kMaterializing: DeviceBufferState#kMaterializing.
  DeviceBufferState.kExecuting: DeviceBufferState#kExecuting.
---
# Module: [`csrc/api/tensor_buffer.h`](../../../../../../raw/code/torch_tpu/csrc/api/tensor_buffer.h)

## Classes
### <a id="DeviceBufferState"></a>`DeviceBufferState`
- def: [`csrc/api/tensor_buffer.h:33`](../../../../../../raw/code/torch_tpu/csrc/api/tensor_buffer.h#L33)
- doc: Lifecycle state of the underlying TPU device buffer.
- signature: `enum class DeviceBufferState`
- members:
  - <a id="DeviceBufferState.kDeferred"></a>`kDeferred` — [`L35`](../../../../../../raw/code/torch_tpu/csrc/api/tensor_buffer.h#L35)
  - <a id="DeviceBufferState.kExecuting"></a>`kExecuting` — [`L36`](../../../../../../raw/code/torch_tpu/csrc/api/tensor_buffer.h#L36)
  - <a id="DeviceBufferState.kMaterialized"></a>`kMaterialized` — [`L38`](../../../../../../raw/code/torch_tpu/csrc/api/tensor_buffer.h#L38)
  - <a id="DeviceBufferState.kMaterializing"></a>`kMaterializing` — [`L37`](../../../../../../raw/code/torch_tpu/csrc/api/tensor_buffer.h#L37)
  - <a id="DeviceBufferState.kPlaceholder"></a>`kPlaceholder` — [`L34`](../../../../../../raw/code/torch_tpu/csrc/api/tensor_buffer.h#L34)
- used by: [`state`](tensor_buffer.cc.md#TensorBufferHandle.state), [`TestBody`](tensor_buffer_test.cc.md#TensorBufferTest_CreateTensorBufferFromPjRtBufferAndToTensor_Test.TestBody), [`TestBody`](tensor_buffer_test.cc.md#TensorBufferTest_MaterializeAndAwaitBuffer_Test.TestBody), [`TestBody`](tensor_buffer_test.cc.md#TensorBufferTest_MoveSemantics_Test.TestBody), [`TestBody`](tensor_buffer_test.cc.md#TensorBufferTest_TpuTensorBufferExtraction_Test.TestBody), [`operator=`](tensor_buffer.h.md#TensorBufferHandle.operator), [`num_elements`](tensor_buffer.cc.md#TensorBufferHandle.num_elements)

### <a id="TensorBufferHandle"></a>`TensorBufferHandle`
- def: [`csrc/api/tensor_buffer.h:44`](../../../../../../raw/code/torch_tpu/csrc/api/tensor_buffer.h#L44)
- doc: Public-facing handle representing the underlying device buffer of a TPU
- signature: `class TensorBufferHandle final`
- members:
  - <a id="TensorBufferHandle.TensorBufferHandle"></a>`TensorBufferHandle(const TensorBufferHandle&)` — [`L47`](../../../../../../raw/code/torch_tpu/csrc/api/tensor_buffer.h#L47) — Move-only semantics to enforce const-correctness.
  - <a id="TensorBufferHandle.operator"></a>`operator=(const TensorBufferHandle&)` — [`L48`](../../../../../../raw/code/torch_tpu/csrc/api/tensor_buffer.h#L48)
  - <a id="TensorBufferHandle.impl_"></a>`impl_` — [`L85`](../../../../../../raw/code/torch_tpu/csrc/api/tensor_buffer.h#L85)
- uses (calls/refs, reference-scoped): [`MakeTensorBuffer`](tensor_buffer.cc.md#MakeTensorBuffer), [`GetBaseTensorBuffer`](tensor_buffer.cc.md#GetBaseTensorBuffer), [`state`](tensor_buffer.cc.md#TensorBufferHandle.state), [`size_bytes`](tensor_buffer.cc.md#TensorBufferHandle.size_bytes), [`Materialize`](tensor_buffer.cc.md#TensorBufferHandle.Materialize), [`dimensions`](tensor_buffer.cc.md#TensorBufferHandle.dimensions), [`num_elements`](tensor_buffer.cc.md#TensorBufferHandle.num_elements), [`AwaitBuffer`](tensor_buffer.cc.md#TensorBufferHandle.AwaitBuffer), [`ToTensor`](tensor_buffer.cc.md#TensorBufferHandle.ToTensor), [`TensorBufferHandle`](tensor_buffer.cc.md#TensorBufferHandle.TensorBufferHandle), [`DeviceBufferState`](tensor_buffer.h.md#DeviceBufferState), [`Synchronize`](tensor_buffer.cc.md#TensorBufferHandle.Synchronize), [`Impl`](tensor_buffer.cc.md#TensorBufferHandle.Impl), [`TensorBufferHandle`](tensor_buffer.cc.md#TensorBufferHandle.TensorBufferHandle), [`operator=`](tensor_buffer.cc.md#TensorBufferHandle.operator), [`~TensorBufferHandle`](tensor_buffer.cc.md#TensorBufferHandle.-TensorBufferHandle), [`MakeTensorBuffer`](tensor_buffer.cc.md#MakeTensorBuffer), [`TensorBufferHandle`](tensor_buffer.cc.md#TensorBufferHandle.TensorBufferHandle)
- used by: [`MakeTensorBuffer`](tensor_buffer.cc.md#MakeTensorBuffer), [`GetBaseTensorBuffer`](tensor_buffer.cc.md#GetBaseTensorBuffer), [`state`](tensor_buffer.cc.md#TensorBufferHandle.state), [`TestBody`](tensor_buffer_test.cc.md#TensorBufferTest_CreateTensorBufferFromPjRtBufferAndToTensor_Test.TestBody), [`TestBody`](tensor_buffer_test.cc.md#TensorBufferTest_MaterializeAndAwaitBuffer_Test.TestBody), [`TestBody`](tensor_buffer_test.cc.md#TensorBufferTest_MoveSemantics_Test.TestBody), [`TestBody`](tensor_buffer_test.cc.md#TensorBufferTest_TpuTensorBufferExtraction_Test.TestBody), [`TestBody`](tensor_buffer_test.cc.md#TensorBufferTest_ViewTensorBaseBufferSharing_Test.TestBody), [`size_bytes`](tensor_buffer.cc.md#TensorBufferHandle.size_bytes), [`Materialize`](tensor_buffer.cc.md#TensorBufferHandle.Materialize), [`dimensions`](tensor_buffer.cc.md#TensorBufferHandle.dimensions), [`num_elements`](tensor_buffer.cc.md#TensorBufferHandle.num_elements), [`AwaitBuffer`](tensor_buffer.cc.md#TensorBufferHandle.AwaitBuffer), [`ToTensor`](tensor_buffer.cc.md#TensorBufferHandle.ToTensor), [`TensorBufferHandle`](tensor_buffer.cc.md#TensorBufferHandle.TensorBufferHandle), [`Synchronize`](tensor_buffer.cc.md#TensorBufferHandle.Synchronize), [`TensorBufferHandle`](tensor_buffer.cc.md#TensorBufferHandle.TensorBufferHandle), [`buffer_ref_`](tensor_buffer.cc.md#TensorBufferHandle.Impl.buffer_ref_), [`operator=`](tensor_buffer.cc.md#TensorBufferHandle.operator), [`~TensorBufferHandle`](tensor_buffer.cc.md#TensorBufferHandle.-TensorBufferHandle)

