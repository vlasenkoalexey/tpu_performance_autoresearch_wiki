---
title: 'Module: csrc/eager/device_buffer_utils.h'
type: catalog
provenance: extracted
module: csrc/eager/device_buffer_utils.h
status: fresh
symbol_base: cxx . . $ torch_tpu/internal/DeferredOpParams#
symbols:
  DeferredOpParams.device_assignment: device_assignment.
  DeferredOpParams: ''
  DeferredOpParams.split_mode: split_mode.
  DeferredOpParams.output_shapes: output_shapes.
  DeferredOpParams.op_name: op_name.
  DeferredOpParams.op_builder: op_builder.
  DeferredOpParams.inputs: inputs.
  DeferredOpParams.computation_dtype: computation_dtype.
  DeferredOpParams.op_param_cache_keys: op_param_cache_keys.
  DeferredOpParams.donated_indices: donated_indices.
---
# Module: [`csrc/eager/device_buffer_utils.h`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer_utils.h)

## Classes
### <a id="DeferredOpParams"></a>`DeferredOpParams`
- def: [`csrc/eager/device_buffer_utils.h:40`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer_utils.h#L40)
- doc: Parameters for creating a deferred DeviceBufferList.
- signature: `struct DeferredOpParams`
- members:
  - <a id="DeferredOpParams.computation_dtype"></a>`computation_dtype` — [`L57`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer_utils.h#L57) — If specified, forces all inputs to be cast to this dtype before the op
  - <a id="DeferredOpParams.device_assignment"></a>`device_assignment` — [`L64`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer_utils.h#L64) — INT_VEC_OK
  - <a id="DeferredOpParams.donated_indices"></a>`donated_indices` — [`L62`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer_utils.h#L62) — The indices of the donated inputs. This is primarily used by custom ops
  - <a id="DeferredOpParams.inputs"></a>`inputs` — [`L50`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer_utils.h#L50) — The inputs to the operation. May be empty for nullary ops, but must match
  - <a id="DeferredOpParams.op_builder"></a>`op_builder` — [`L45`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer_utils.h#L45) — The MLIR op builder for the operation. It must take a vector of MlirOps as
  - <a id="DeferredOpParams.op_name"></a>`op_name` — [`L42`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer_utils.h#L42) — The name of the operation, see op_names.h for possible values.
  - <a id="DeferredOpParams.op_param_cache_keys"></a>`op_param_cache_keys` — [`L47`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer_utils.h#L47) — The cache keys for the operation. See cache_key.h for more details.
  - <a id="DeferredOpParams.output_shapes"></a>`output_shapes` — [`L53`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer_utils.h#L53) — The output shapes and types of the operation. Must match the number of
  - <a id="DeferredOpParams.split_mode"></a>`split_mode` — [`L59`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer_utils.h#L59) — The split mode for the operation. See device_buffer.h for more details.
- uses (calls/refs, reference-scoped): [`OpName`](../ops/op_names.h.md#OpName), [`Dimensions`](../common/dimension_types.h.md#Dimensions), [`OpParamCacheKeys`](../common/cache_key.h.md#OpParamCacheKeys), [`DeviceBufferRef`](device_buffer.h.md#DeviceBufferRef), [`Shape`](../common/shape.h.md#Shape), [`CreateViewDeviceBufferRef`](device_buffer_utils.cc.md#CreateViewDeviceBufferRef), [`Indices`](../common/dimension_types.h.md#Indices), [`CreateDeferredDeviceBufferList`](device_buffer_utils.cc.md#CreateDeferredDeviceBufferList), [`CreateZeroSizeDeviceBufferRef`](device_buffer_utils.cc.md#CreateZeroSizeDeviceBufferRef), [`CreateInverseViewDeviceBufferRef`](device_buffer_utils.cc.md#CreateInverseViewDeviceBufferRef), [`CreateEmptyDeviceBufferRef`](device_buffer_utils.cc.md#CreateEmptyDeviceBufferRef), [`CreateDeferredDeviceBufferList`](device_buffer_utils.cc.md#CreateDeferredDeviceBufferList), [`OpSplitMode`](device_buffer.h.md#OpSplitMode), [`ComputeConstantDeviceBufferRefOpParamCacheKeys`](device_buffer_utils.cc.md#ComputeConstantDeviceBufferRefOpParamCacheKeys), [`kNone`](device_buffer.h.md#OpSplitMode.kNone), [`MlirOpBuilder`](../ops/op_builder_utils.h.md#MlirOpBuilder), [`CreateConstantDeviceBufferRef`](device_buffer_utils.cc.md#CreateConstantDeviceBufferRef), [`TpuLayout`](../common/layout_utils.h.md#TpuLayout), [`CreateConstantDeviceBufferRef`](device_buffer_utils.cc.md#CreateConstantDeviceBufferRef)
- used by: [`DispatchOp`](op_dispatcher.h.md#DispatchOp), [`CreateViewDeviceBufferRef`](device_buffer_utils.cc.md#CreateViewDeviceBufferRef), [`CreateDeferredDeviceBufferList`](device_buffer_utils.cc.md#CreateDeferredDeviceBufferList), [`PyCreateAssociativeScanOp`](../internal/compile/dispatch_scan.cc.md#PyCreateAssociativeScanOp), [`CreateInverseViewDeviceBufferRef`](device_buffer_utils.cc.md#CreateInverseViewDeviceBufferRef), [`PyCreateScanOp`](../internal/compile/dispatch_scan.cc.md#PyCreateScanOp), [`CreateEmptyDeviceBufferRef`](device_buffer_utils.cc.md#CreateEmptyDeviceBufferRef), [`CreateConstantDeviceBufferRefImpl`](device_buffer_utils.cc.md#CreateConstantDeviceBufferRefImpl), [`TestBody`](op_dispatcher_test.cc.md#OpDispatcher_OutputCastingWithoutComputationDtype_Test.TestBody), [`ApplyComputationDtype`](device_buffer_utils.cc.md#ApplyComputationDtype)

