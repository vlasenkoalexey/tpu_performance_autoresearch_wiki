---
title: 'Module: csrc/internal/sync/sync.h'
type: catalog
provenance: extracted
module: csrc/internal/sync/sync.h
status: fresh
symbol_base: cxx . . $ torch_tpu/WaitOnExecution#
symbols:
  WaitOnExecution.kYes: kYes.
  WaitOnExecution.kNo: kNo.
  WaitOnExecution: ''
---
# Module: [`csrc/internal/sync/sync.h`](../../../../../../../raw/code/torch_tpu/csrc/internal/sync/sync.h)

## Classes
### <a id="WaitOnExecution"></a>`WaitOnExecution`
- def: [`csrc/internal/sync/sync.h:53`](../../../../../../../raw/code/torch_tpu/csrc/internal/sync/sync.h#L53) — documented in [tensor-synchronization](../../../../concepts/tensor-synchronization.md)
- doc: Whether to wait for execution to complete.
- signature: `enum class WaitOnExecution`
- members:
  - <a id="WaitOnExecution.kNo"></a>`kNo` — [`L56`](../../../../../../../raw/code/torch_tpu/csrc/internal/sync/sync.h#L56) — Only ensures that all deferred operations have been scheduled for — documented in [tensor-synchronization](../../../../concepts/tensor-synchronization.md)
  - <a id="WaitOnExecution.kYes"></a>`kYes` — [`L59`](../../../../../../../raw/code/torch_tpu/csrc/internal/sync/sync.h#L59) — Blocks the calling thread until all deferred operations have completed — documented in [tensor-synchronization](../../../../concepts/tensor-synchronization.md)
- uses (calls/refs, reference-scoped): [`DeviceBufferRef`](../../eager/device_buffer.h.md#DeviceBufferRef), [`IsMaterializing`](sync.cc.md#IsMaterializing), [`GetComputationMlir`](sync.cc.md#GetComputationMlir), [`IsMaterialized`](sync.cc.md#IsMaterialized), [`GetComputationGraphviz`](sync.cc.md#GetComputationGraphviz), [`GetComputationGraphviz`](sync.cc.md#GetComputationGraphviz)

