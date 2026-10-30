---
title: 'Module: csrc/common/dynamism_utils.h'
type: catalog
provenance: extracted
module: csrc/common/dynamism_utils.h
status: fresh
symbol_base: cxx . . $ torch_tpu/DeviceRefDimensions#
symbols:
  DeviceRefDimensions.dims: dims.
  DeviceRefDimensions: ''
  DeviceRefDimensions.ref: ref.
---
# Module: [`csrc/common/dynamism_utils.h`](../../../../../../raw/code/torch_tpu/csrc/common/dynamism_utils.h)

## Classes
### <a id="DeviceRefDimensions"></a>`DeviceRefDimensions`
- def: [`csrc/common/dynamism_utils.h:31`](../../../../../../raw/code/torch_tpu/csrc/common/dynamism_utils.h#L31)
- doc: Struct to hold a DeviceBufferRef and its inferred MLIR StableHLO dimensions.
- signature: `struct DeviceRefDimensions`
- members:
  - <a id="DeviceRefDimensions.dims"></a>`dims` — [`L33`](../../../../../../raw/code/torch_tpu/csrc/common/dynamism_utils.h#L33)
  - <a id="DeviceRefDimensions.ref"></a>`ref` — [`L32`](../../../../../../raw/code/torch_tpu/csrc/common/dynamism_utils.h#L32)
- uses (calls/refs, reference-scoped): [`DeviceBufferRef`](../eager/device_buffer.h.md#DeviceBufferRef), [`Traversal`](../eager/traversal.h.md#Traversal), [`GetTraversalOutputDimensions`](dynamism_utils.cc.md#GetTraversalOutputDimensions), [`GetTraversalOutputDimensions`](dynamism_utils.cc.md#GetTraversalOutputDimensions)
- used by: [`TestBody`](dynamism_utils_test.cc.md#DynamismOpsTest_GetTraversalOutputDimensionsWithBoundedInput_Test.TestBody), [`TestBody`](dynamism_utils_test.cc.md#DynamismOpsTest_GetTraversalOutputDimensionsNoBoundedInput_Test.TestBody), [`GetTraversalOutputDimensions`](dynamism_utils.cc.md#GetTraversalOutputDimensions), [`PropagateBoundedDynamism`](../eager/execution_task.cc.md#PropagateBoundedDynamism)

