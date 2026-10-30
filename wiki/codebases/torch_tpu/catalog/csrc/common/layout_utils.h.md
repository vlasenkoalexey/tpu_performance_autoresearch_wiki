---
title: 'Module: csrc/common/layout_utils.h'
type: catalog
provenance: extracted
module: csrc/common/layout_utils.h
status: fresh
symbol_base: cxx . . $ torch_tpu/TpuLayout#
symbols:
  TpuLayout.element_type: element_type.
  TpuLayout.sizes: sizes.
  TpuLayout.storage_offset: storage_offset.
  TpuLayout: ''
  TpuLayout.strides: strides.
---
# Module: [`csrc/common/layout_utils.h`](../../../../../../raw/code/torch_tpu/csrc/common/layout_utils.h)

## Classes
### <a id="TpuLayout"></a>`TpuLayout`
- def: [`csrc/common/layout_utils.h:30`](../../../../../../raw/code/torch_tpu/csrc/common/layout_utils.h#L30)
- doc: Represents the layout metrics of a TPU tensor mapped from PyTorch.
- signature: `struct TpuLayout`
- members:
  - <a id="TpuLayout.element_type"></a>`element_type` — [`L44`](../../../../../../raw/code/torch_tpu/csrc/common/layout_utils.h#L44) — The element type on the TPU/StableHLO side. Defaults to an invalid element
  - <a id="TpuLayout.sizes"></a>`sizes` — [`L33`](../../../../../../raw/code/torch_tpu/csrc/common/layout_utils.h#L33) — The sizes of the tensor dimensions. Must have the same size (rank) as
  - <a id="TpuLayout.storage_offset"></a>`storage_offset` — [`L40`](../../../../../../raw/code/torch_tpu/csrc/common/layout_utils.h#L40) — The offset in elements from the start of the storage. Defaults to -1 (an
  - <a id="TpuLayout.strides"></a>`strides` — [`L36`](../../../../../../raw/code/torch_tpu/csrc/common/layout_utils.h#L36) — The strides of the tensor dimensions. Must have the same size (rank) as
- uses (calls/refs, reference-scoped): [`Dimensions`](dimension_types.h.md#Dimensions), [`ResolveTpuLayout`](layout_utils.cc.md#ResolveTpuLayout), [`Strides`](dimension_types.h.md#Strides)
- used by: [`AssignBufferToAtTensor`](../eager/tensor_to_buffer.cc.md#AssignBufferToAtTensor), [`GetBuffer`](../eager/tensor_to_buffer.cc.md#GetBuffer), [`CreateViewDeviceBufferRef`](../eager/device_buffer_utils.cc.md#CreateViewDeviceBufferRef), [`CreateInverseViewDeviceBufferRef`](../eager/device_buffer_utils.cc.md#CreateInverseViewDeviceBufferRef), [`PyCallCustomKernel`](../internal/pallas/pallas_py.cc.md#PyCallCustomKernel), [`ResolveTpuLayout`](layout_utils.cc.md#ResolveTpuLayout), [`CopyCpuToTpuBuffer`](../ops/copy_from/cpu_to_tpu.cc.md#CopyCpuToTpuBuffer), [`device_assignment`](../eager/device_buffer_utils.h.md#DeferredOpParams.device_assignment), [`TestBody`](layout_utils_test.cc.md#LayoutUtilsTest_ResolveTpuLayout_FP4TensorWithOffset_Success_Test.TestBody), [`TestBody`](layout_utils_test.cc.md#LayoutUtilsTest_ResolveTpuLayout_FP4Tensor_Success_Test.TestBody), [`TestBody`](layout_utils_test.cc.md#LayoutUtilsTest_ResolveTpuLayout_StandardTensorZeroDim_Success_Test.TestBody), [`TestBody`](layout_utils_test.cc.md#LayoutUtilsTest_ResolveTpuLayout_StandardTensor_Success_Test.TestBody)

