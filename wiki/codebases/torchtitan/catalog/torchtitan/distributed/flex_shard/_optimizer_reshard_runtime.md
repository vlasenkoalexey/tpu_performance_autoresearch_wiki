---
title: 'Module: torchtitan/distributed/flex_shard/_optimizer_reshard_runtime.py'
type: catalog
provenance: extracted
module: torchtitan/distributed/flex_shard/_optimizer_reshard_runtime.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.distributed.flex_shard._optimizer_reshard_runtime`/
symbols:
  _BucketedRedistributionRuntime.reserve_buffers: _BucketedRedistributionRuntime#reserve_buffers().
  _compute_redistributed: _compute_redistributed().
  _finalize_redistributed: _finalize_redistributed().
  _BucketedRedistributionRuntime.run: _BucketedRedistributionRuntime#run().
  _prepare_redistributed: _prepare_redistributed().
  _BucketedRedistributionRuntime._enqueue_compute_to_storage: _BucketedRedistributionRuntime#_enqueue_compute_to_storage().
  _BufferSlot.reserve: _BufferSlot#reserve().
  _BucketedRedistributionRuntime._enqueue_storage_to_compute: _BucketedRedistributionRuntime#_enqueue_storage_to_compute().
  _BucketedRedistributionRuntime._compute_bucket: _BucketedRedistributionRuntime#_compute_bucket().
  _BufferSlot.communication_buffers: _BufferSlot#communication_buffers().
  _execute_packed_all_to_all: _execute_packed_all_to_all().
  _CommunicationContext.create_slot: _CommunicationContext#create_slot().
  _BucketedRedistributionRuntime.prefetch_next: _BucketedRedistributionRuntime#prefetch_next().
  _BucketWork: _BucketWork#
  _include_compute_scratch_requirement: _include_compute_scratch_requirement().
  _BucketedRedistributionRuntime._release: _BucketedRedistributionRuntime#_release().
  _CommunicationContext.slots: _CommunicationContext#slots.
  _tensor_region_view: _tensor_region_view().
  _BufferSlot.buffers: _BufferSlot#buffers.
  _BucketWork.plan: _BucketWork#plan.
  _BufferSlot.record_compute_stream: _BufferSlot#record_compute_stream().
  _PipelineSlot.buffers: _PipelineSlot#buffers.
  _BufferSlot.compute_buffer: _BufferSlot#compute_buffer().
  _BufferSlot.storage_partition_buffer: _BufferSlot#storage_partition_buffer().
  _BucketedRedistributionRuntime._compute_without_redistribution: _BucketedRedistributionRuntime#_compute_without_redistribution().
  _BucketWork.slot: _BucketWork#slot.
  _CommunicationContext.create: _CommunicationContext#create().
  _BufferSlot: _BufferSlot#
  _PipelineSlot: _PipelineSlot#
  _CommunicationContext.transfer_stream: _CommunicationContext#transfer_stream.
  _BucketedRedistributionRuntime: _BucketedRedistributionRuntime#
  _CommunicationContext: _CommunicationContext#
  _BucketedRedistributionRuntime._context: _BucketedRedistributionRuntime#_context.
  _BucketedRedistributionRuntime._local_slot: _BucketedRedistributionRuntime#_local_slot.
  _BufferRequirements: _BufferRequirements#
  _BufferRequirements.include_communication: _BufferRequirements#include_communication().
  _CommunicationContext.device_handle: _CommunicationContext#device_handle.
  _BucketedRedistributionRuntime._device: _BucketedRedistributionRuntime#_device.
  _BufferRequirements.storage_exchange_numel: _BufferRequirements#storage_exchange_numel.
  _BufferRequirements.compute_exchange_numel: _BufferRequirements#compute_exchange_numel.
  _BufferRequirements.compute_scratch_numel: _BufferRequirements#compute_scratch_numel.
  _BufferRequirements.storage_scratch_numel: _BufferRequirements#storage_scratch_numel.
  _ReservedBuffers.compute_scratch: _ReservedBuffers#compute_scratch.
  _reserve_tensor: _reserve_tensor().
  _reserved_view: _reserved_view().
  _PipelineSlot.compute_input_ready: _PipelineSlot#compute_input_ready.
  _PipelineSlot.compute_done: _PipelineSlot#compute_done.
  _PipelineSlot.done: _PipelineSlot#done.
  _batched_copy_: _batched_copy_().
  _BufferKey._BufferKey: _BufferKey._BufferKey.
  _BufferRequirements.include_compute_scratch: _BufferRequirements#include_compute_scratch().
  _ReservedBuffers: _ReservedBuffers#
  _ReservedBuffers.storage_exchange: _ReservedBuffers#storage_exchange.
  _ReservedBuffers.compute_exchange: _ReservedBuffers#compute_exchange.
  _ReservedBuffers.storage_scratch: _ReservedBuffers#storage_scratch.
  _BufferSlot._recorded_compute_streams: _BufferSlot#_recorded_compute_streams.
  _BucketWork.compute_fragment_buffer: _BucketWork#compute_fragment_buffer.
  _BufferRequirements.include_storage_scratch: _BufferRequirements#include_storage_scratch().
  _BucketWork.storage_buffer: _BucketWork#storage_buffer.
  _NUM_PIPELINE_SLOTS: _NUM_PIPELINE_SLOTS.
  _BucketedRedistributionRuntime.__init__: _BucketedRedistributionRuntime#__init__().
  __all__.__all__: __all__.__all__.
---
# Module: [`torchtitan/distributed/flex_shard/_optimizer_reshard_runtime.py`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_runtime.py)

## Classes
### <a id="_BucketWork"></a>`_BucketWork`  ·  implements/extends Generic
- def: [`torchtitan/distributed/flex_shard/_optimizer_reshard_runtime.py:248`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_runtime.py#L248)
- signature: `class _BucketWork(Generic[_ItemT]):`
- members:
  - <a id="_BucketWork.compute_fragment_buffer"></a>`compute_fragment_buffer` — [`L252`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_runtime.py#L252)
  - <a id="_BucketWork.plan"></a>`plan` — [`L249`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_runtime.py#L249)
  - <a id="_BucketWork.slot"></a>`slot` — [`L250`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_runtime.py#L250)
  - <a id="_BucketWork.storage_buffer"></a>`storage_buffer` — [`L251`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_runtime.py#L251)
- uses (calls/refs, reference-scoped): [`_ItemT`](_optimizer_reshard_schedule.md#_ItemT), [`_RedistributionBucketPlan`](_optimizer_reshard_schedule.md#_RedistributionBucketPlan), [`_PipelineSlot`](_optimizer_reshard_runtime.md#_PipelineSlot)
- used by: [`_compute_redistributed`](_optimizer_reshard_runtime.md#_compute_redistributed), [`_finalize_redistributed`](_optimizer_reshard_runtime.md#_finalize_redistributed), [`run`](_optimizer_reshard_runtime.md#_BucketedRedistributionRuntime.run), [`_enqueue_compute_to_storage`](_optimizer_reshard_runtime.md#_BucketedRedistributionRuntime._enqueue_compute_to_storage), [`_enqueue_storage_to_compute`](_optimizer_reshard_runtime.md#_BucketedRedistributionRuntime._enqueue_storage_to_compute), [`_compute_bucket`](_optimizer_reshard_runtime.md#_BucketedRedistributionRuntime._compute_bucket), [`prefetch_next`](_optimizer_reshard_runtime.md#_BucketedRedistributionRuntime.prefetch_next), [`_release`](_optimizer_reshard_runtime.md#_BucketedRedistributionRuntime._release)

### <a id="_BucketedRedistributionRuntime"></a>`_BucketedRedistributionRuntime`  ·  implements/extends Generic
- def: [`torchtitan/distributed/flex_shard/_optimizer_reshard_runtime.py:295`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_runtime.py#L295)
- doc: Execute bucket plans with a rolling communication prefetch window.
- signature: `class _BucketedRedistributionRuntime(Generic[_ItemT]):`
- members:
  - <a id="_BucketedRedistributionRuntime.prefetch_next"></a>`prefetch_next(slot: _PipelineSlot)` — [`L449`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_runtime.py#L449)
  - <a id="_BucketedRedistributionRuntime.reserve_buffers"></a>`reserve_buffers(self, plans: Sequence[_BucketPlan[_ItemT]], *, local_tensor_spec: Callable[[_ItemT], tuple[torch.Size, torch.dtype, torch.device]])` — [`L324`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_runtime.py#L324) — Eagerly grow runtime-owned tensors to the plans' maximum sizes. — documented in [flex-shard](../../../../concepts/flex-shard.md)
  - <a id="_BucketedRedistributionRuntime.run"></a>`run(self, plans: Sequence[_BucketPlan[_ItemT]], *, local_tensor_spec: Callable[[_ItemT], tuple[torch.Size, torch.dtype, torch.device]], prepare: Callable[[_ItemT, Tensor], None], compute: Callable[[_ItemT, Tensor], None], finalize: Callable[[_ItemT, Tensor], None])` — [`L419`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_runtime.py#L419) — documented in [flex-shard](../../../../concepts/flex-shard.md)
- protocol/private: <a id="_BucketedRedistributionRuntime.__init__"></a>`__init__`[`L315`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_runtime.py#L315), <a id="_BucketedRedistributionRuntime._compute_bucket"></a>`_compute_bucket`[`L589`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_runtime.py#L589), <a id="_BucketedRedistributionRuntime._compute_without_redistribution"></a>`_compute_without_redistribution`[`L644`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_runtime.py#L644), <a id="_BucketedRedistributionRuntime._context"></a>`_context`[`L321`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_runtime.py#L321), <a id="_BucketedRedistributionRuntime._device"></a>`_device`[`L320`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_runtime.py#L320), <a id="_BucketedRedistributionRuntime._enqueue_compute_to_storage"></a>`_enqueue_compute_to_storage`[`L621`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_runtime.py#L621), <a id="_BucketedRedistributionRuntime._enqueue_storage_to_compute"></a>`_enqueue_storage_to_compute`[`L559`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_runtime.py#L559), <a id="_BucketedRedistributionRuntime._local_slot"></a>`_local_slot`[`L322`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_runtime.py#L322), <a id="_BucketedRedistributionRuntime._release"></a>`_release`[`L640`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_runtime.py#L640)
- uses (calls/refs, reference-scoped): [`_ItemT`](_optimizer_reshard_schedule.md#_ItemT), [`_compute_redistributed`](_optimizer_reshard_runtime.md#_compute_redistributed), [`_finalize_redistributed`](_optimizer_reshard_runtime.md#_finalize_redistributed), [`_prepare_redistributed`](_optimizer_reshard_runtime.md#_prepare_redistributed), [`reserve`](_optimizer_reshard_runtime.md#_BufferSlot.reserve), [`communication_buffers`](_optimizer_reshard_runtime.md#_BufferSlot.communication_buffers), [`_execute_packed_all_to_all`](_optimizer_reshard_runtime.md#_execute_packed_all_to_all), [`tensor_shape`](_optimizer_reshard_schedule.md#_ParticipantPartition.tensor_shape), [`_BucketWork`](_optimizer_reshard_runtime.md#_BucketWork), [`_BucketPlan`](_optimizer_reshard_schedule.md#_BucketPlan._BucketPlan), [`_include_compute_scratch_requirement`](_optimizer_reshard_runtime.md#_include_compute_scratch_requirement), [`slots`](_optimizer_reshard_runtime.md#_CommunicationContext.slots), [`storage_partition`](_optimizer_reshard_schedule.md#_RedistributionPlan.storage_partition), [`plan`](_optimizer_reshard_runtime.md#_BucketWork.plan), [`_RedistributionBucketPlan`](_optimizer_reshard_schedule.md#_RedistributionBucketPlan), [`buffers`](_optimizer_reshard_runtime.md#_PipelineSlot.buffers), [`record_compute_stream`](_optimizer_reshard_runtime.md#_BufferSlot.record_compute_stream), [`_LocalBucketPlan`](_optimizer_reshard_schedule.md#_LocalBucketPlan), [`compute_buffer`](_optimizer_reshard_runtime.md#_BufferSlot.compute_buffer), [`compute_partition`](_optimizer_reshard_schedule.md#_RedistributionPlan.compute_partition), [`compute_to_storage_schedule`](_optimizer_reshard_schedule.md#_RedistributionBucketPlan.compute_to_storage_schedule), [`create`](_optimizer_reshard_runtime.md#_CommunicationContext.create), [`group`](_optimizer_reshard_schedule.md#_RedistributionBucketPlan.group), [`redistribution_plans`](_optimizer_reshard_schedule.md#_RedistributionBucketPlan.redistribution_plans), [`slot`](_optimizer_reshard_runtime.md#_BucketWork.slot), [`storage_to_compute_schedule`](_optimizer_reshard_schedule.md#_RedistributionBucketPlan.storage_to_compute_schedule), [`device`](_optimizer_reshard_schedule.md#_RedistributionBucketPlan.device), [`_BufferSlot`](_optimizer_reshard_runtime.md#_BufferSlot), [`_PipelineSlot`](_optimizer_reshard_runtime.md#_PipelineSlot), [`dtype`](_optimizer_reshard_schedule.md#_RedistributionBucketPlan.dtype), [`input_buffer_numel`](_optimizer_reshard_schedule.md#_PackedAllToAllSchedule.input_buffer_numel), [`output_buffer_numel`](_optimizer_reshard_schedule.md#_PackedAllToAllSchedule.output_buffer_numel), [`transfer_stream`](_optimizer_reshard_runtime.md#_CommunicationContext.transfer_stream), [`unredistributed_items`](_optimizer_reshard_schedule.md#_RedistributionBucketPlan.unredistributed_items), [`_CommunicationContext`](_optimizer_reshard_runtime.md#_CommunicationContext), [`_BufferRequirements`](_optimizer_reshard_runtime.md#_BufferRequirements), [`device_handle`](_optimizer_reshard_runtime.md#_CommunicationContext.device_handle), [`local_participant`](_optimizer_reshard_schedule.md#_RedistributionGroup.local_participant), [`_BufferKey`](_optimizer_reshard_runtime.md#_BufferKey._BufferKey), [`compute_done`](_optimizer_reshard_runtime.md#_PipelineSlot.compute_done)  (+5 more)
- used by: [`_initialize_dist_muon`](dist_muon.md#_initialize_dist_muon), [`DistMuon`](dist_muon.md#DistMuon), [`_after_load_state_dict`](dist_muon.md#_after_load_state_dict), [`_redistribution_runtime`](dist_muon.md#DistMuon._redistribution_runtime)

### <a id="_BufferRequirements"></a>`_BufferRequirements`
- def: [`torchtitan/distributed/flex_shard/_optimizer_reshard_runtime.py:48`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_runtime.py#L48)
- signature: `class _BufferRequirements:`
- members:
  - <a id="_BufferRequirements.include_communication"></a>`include_communication(self, *, storage_exchange_numel: int, compute_exchange_numel: int)` — [`L54`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_runtime.py#L54)
  - <a id="_BufferRequirements.include_compute_scratch"></a>`include_compute_scratch(self, numel: int)` — [`L69`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_runtime.py#L69)
  - <a id="_BufferRequirements.include_storage_scratch"></a>`include_storage_scratch(self, numel: int)` — [`L72`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_runtime.py#L72)
  - <a id="_BufferRequirements.compute_exchange_numel"></a>`compute_exchange_numel` — [`L50`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_runtime.py#L50)
  - <a id="_BufferRequirements.compute_scratch_numel"></a>`compute_scratch_numel` — [`L51`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_runtime.py#L51)
  - <a id="_BufferRequirements.storage_exchange_numel"></a>`storage_exchange_numel` — [`L49`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_runtime.py#L49)
  - <a id="_BufferRequirements.storage_scratch_numel"></a>`storage_scratch_numel` — [`L52`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_runtime.py#L52)
- used by: [`reserve_buffers`](_optimizer_reshard_runtime.md#_BucketedRedistributionRuntime.reserve_buffers), [`reserve`](_optimizer_reshard_runtime.md#_BufferSlot.reserve), [`_include_compute_scratch_requirement`](_optimizer_reshard_runtime.md#_include_compute_scratch_requirement)

### <a id="_BufferSlot"></a>`_BufferSlot`
- def: [`torchtitan/distributed/flex_shard/_optimizer_reshard_runtime.py:124`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_runtime.py#L124)
- signature: `class _BufferSlot:`
- members:
  - <a id="_BufferSlot.communication_buffers"></a>`communication_buffers(self, plan: _RedistributionBucketPlan[Any])` — [`L190`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_runtime.py#L190) — documented in [flex-shard](../../../../concepts/flex-shard.md)
  - <a id="_BufferSlot.compute_buffer"></a>`compute_buffer(self, shape: torch.Size | tuple[int, ...], *, dtype: torch.dtype, device: torch.device)` — [`L213`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_runtime.py#L213)
  - <a id="_BufferSlot.record_compute_stream"></a>`record_compute_stream(self, stream: torch.Stream)` — [`L178`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_runtime.py#L178)
  - <a id="_BufferSlot.reserve"></a>`reserve(self, requirements: dict[_BufferKey, _BufferRequirements], *, device_handle: ModuleType, compute_stream: torch.Stream, transfer_stream: torch.Stream | None)` — [`L128`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_runtime.py#L128) — documented in [flex-shard](../../../../concepts/flex-shard.md)
  - <a id="_BufferSlot.storage_partition_buffer"></a>`storage_partition_buffer(self, shape: torch.Size | tuple[int, ...], *, dtype: torch.dtype, device: torch.device)` — [`L223`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_runtime.py#L223)
  - <a id="_BufferSlot.buffers"></a>`buffers` — [`L125`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_runtime.py#L125)
- protocol/private: <a id="_BufferSlot._recorded_compute_streams"></a>`_recorded_compute_streams`[`L126`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_runtime.py#L126)
- uses (calls/refs, reference-scoped): [`_RedistributionBucketPlan`](_optimizer_reshard_schedule.md#_RedistributionBucketPlan), [`compute_to_storage_schedule`](_optimizer_reshard_schedule.md#_RedistributionBucketPlan.compute_to_storage_schedule), [`storage_to_compute_schedule`](_optimizer_reshard_schedule.md#_RedistributionBucketPlan.storage_to_compute_schedule), [`device`](_optimizer_reshard_schedule.md#_RedistributionBucketPlan.device), [`dtype`](_optimizer_reshard_schedule.md#_RedistributionBucketPlan.dtype), [`input_buffer_numel`](_optimizer_reshard_schedule.md#_PackedAllToAllSchedule.input_buffer_numel), [`output_buffer_numel`](_optimizer_reshard_schedule.md#_PackedAllToAllSchedule.output_buffer_numel), [`_BufferRequirements`](_optimizer_reshard_runtime.md#_BufferRequirements), [`_BufferKey`](_optimizer_reshard_runtime.md#_BufferKey._BufferKey), [`_reserve_tensor`](_optimizer_reshard_runtime.md#_reserve_tensor), [`_reserved_view`](_optimizer_reshard_runtime.md#_reserved_view), [`compute_exchange_numel`](_optimizer_reshard_runtime.md#_BufferRequirements.compute_exchange_numel), [`compute_scratch`](_optimizer_reshard_runtime.md#_ReservedBuffers.compute_scratch), [`compute_scratch_numel`](_optimizer_reshard_runtime.md#_BufferRequirements.compute_scratch_numel), [`storage_exchange_numel`](_optimizer_reshard_runtime.md#_BufferRequirements.storage_exchange_numel), [`storage_scratch_numel`](_optimizer_reshard_runtime.md#_BufferRequirements.storage_scratch_numel), [`_ReservedBuffers`](_optimizer_reshard_runtime.md#_ReservedBuffers), [`compute_exchange`](_optimizer_reshard_runtime.md#_ReservedBuffers.compute_exchange), [`storage_exchange`](_optimizer_reshard_runtime.md#_ReservedBuffers.storage_exchange), [`storage_scratch`](_optimizer_reshard_runtime.md#_ReservedBuffers.storage_scratch)
- used by: [`reserve_buffers`](_optimizer_reshard_runtime.md#_BucketedRedistributionRuntime.reserve_buffers), [`_compute_redistributed`](_optimizer_reshard_runtime.md#_compute_redistributed), [`_finalize_redistributed`](_optimizer_reshard_runtime.md#_finalize_redistributed), [`run`](_optimizer_reshard_runtime.md#_BucketedRedistributionRuntime.run), [`_prepare_redistributed`](_optimizer_reshard_runtime.md#_prepare_redistributed), [`_enqueue_storage_to_compute`](_optimizer_reshard_runtime.md#_BucketedRedistributionRuntime._enqueue_storage_to_compute), [`create_slot`](_optimizer_reshard_runtime.md#_CommunicationContext.create_slot), [`buffers`](_optimizer_reshard_runtime.md#_PipelineSlot.buffers), [`_compute_without_redistribution`](_optimizer_reshard_runtime.md#_BucketedRedistributionRuntime._compute_without_redistribution), [`_local_slot`](_optimizer_reshard_runtime.md#_BucketedRedistributionRuntime._local_slot)

### <a id="_CommunicationContext"></a>`_CommunicationContext`
- def: [`torchtitan/distributed/flex_shard/_optimizer_reshard_runtime.py:256`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_runtime.py#L256)
- signature: `class _CommunicationContext:`
- members:
  - <a id="_CommunicationContext.create"></a>`create(cls, device: torch.device)` — [`L262`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_runtime.py#L262)
  - <a id="_CommunicationContext.create_slot"></a>`create_slot()` — [`L269`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_runtime.py#L269)
  - <a id="_CommunicationContext.device_handle"></a>`device_handle` — [`L257`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_runtime.py#L257)
  - <a id="_CommunicationContext.slots"></a>`slots` — [`L259`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_runtime.py#L259)
  - <a id="_CommunicationContext.transfer_stream"></a>`transfer_stream` — [`L258`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_runtime.py#L258)
- uses (calls/refs, reference-scoped): [`buffers`](_optimizer_reshard_runtime.md#_PipelineSlot.buffers), [`_BufferSlot`](_optimizer_reshard_runtime.md#_BufferSlot), [`_PipelineSlot`](_optimizer_reshard_runtime.md#_PipelineSlot), [`compute_done`](_optimizer_reshard_runtime.md#_PipelineSlot.compute_done), [`compute_input_ready`](_optimizer_reshard_runtime.md#_PipelineSlot.compute_input_ready), [`done`](_optimizer_reshard_runtime.md#_PipelineSlot.done), [`_NUM_PIPELINE_SLOTS`](_optimizer_reshard_runtime.md#_NUM_PIPELINE_SLOTS)
- used by: [`reserve_buffers`](_optimizer_reshard_runtime.md#_BucketedRedistributionRuntime.reserve_buffers), [`run`](_optimizer_reshard_runtime.md#_BucketedRedistributionRuntime.run), [`_enqueue_compute_to_storage`](_optimizer_reshard_runtime.md#_BucketedRedistributionRuntime._enqueue_compute_to_storage), [`_enqueue_storage_to_compute`](_optimizer_reshard_runtime.md#_BucketedRedistributionRuntime._enqueue_storage_to_compute), [`_compute_bucket`](_optimizer_reshard_runtime.md#_BucketedRedistributionRuntime._compute_bucket), [`_context`](_optimizer_reshard_runtime.md#_BucketedRedistributionRuntime._context)

### <a id="_PipelineSlot"></a>`_PipelineSlot`
- def: [`torchtitan/distributed/flex_shard/_optimizer_reshard_runtime.py:235`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_runtime.py#L235)
- doc: Persistent buffer keepalive and reusable cross-stream handoff events.
- signature: `class _PipelineSlot:`
- members:
  - <a id="_PipelineSlot.buffers"></a>`buffers` — [`L238`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_runtime.py#L238)
  - <a id="_PipelineSlot.compute_done"></a>`compute_done` — [`L242`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_runtime.py#L242)
  - <a id="_PipelineSlot.compute_input_ready"></a>`compute_input_ready` — [`L240`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_runtime.py#L240)
  - <a id="_PipelineSlot.done"></a>`done` — [`L244`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_runtime.py#L244)
- uses (calls/refs, reference-scoped): [`_BufferSlot`](_optimizer_reshard_runtime.md#_BufferSlot)
- used by: [`reserve_buffers`](_optimizer_reshard_runtime.md#_BucketedRedistributionRuntime.reserve_buffers), [`run`](_optimizer_reshard_runtime.md#_BucketedRedistributionRuntime.run), [`_enqueue_compute_to_storage`](_optimizer_reshard_runtime.md#_BucketedRedistributionRuntime._enqueue_compute_to_storage), [`_enqueue_storage_to_compute`](_optimizer_reshard_runtime.md#_BucketedRedistributionRuntime._enqueue_storage_to_compute), [`_compute_bucket`](_optimizer_reshard_runtime.md#_BucketedRedistributionRuntime._compute_bucket), [`create_slot`](_optimizer_reshard_runtime.md#_CommunicationContext.create_slot), [`prefetch_next`](_optimizer_reshard_runtime.md#_BucketedRedistributionRuntime.prefetch_next), [`_release`](_optimizer_reshard_runtime.md#_BucketedRedistributionRuntime._release), [`slots`](_optimizer_reshard_runtime.md#_CommunicationContext.slots), [`slot`](_optimizer_reshard_runtime.md#_BucketWork.slot)

### <a id="_ReservedBuffers"></a>`_ReservedBuffers`
- def: [`torchtitan/distributed/flex_shard/_optimizer_reshard_runtime.py:77`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_runtime.py#L77)
- signature: `class _ReservedBuffers:`
- members:
  - <a id="_ReservedBuffers.compute_exchange"></a>`compute_exchange` — [`L79`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_runtime.py#L79)
  - <a id="_ReservedBuffers.compute_scratch"></a>`compute_scratch` — [`L82`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_runtime.py#L82)
  - <a id="_ReservedBuffers.storage_exchange"></a>`storage_exchange` — [`L78`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_runtime.py#L78)
  - <a id="_ReservedBuffers.storage_scratch"></a>`storage_scratch` — [`L83`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_runtime.py#L83)
- used by: [`reserve`](_optimizer_reshard_runtime.md#_BufferSlot.reserve), [`communication_buffers`](_optimizer_reshard_runtime.md#_BufferSlot.communication_buffers), [`buffers`](_optimizer_reshard_runtime.md#_BufferSlot.buffers), [`record_compute_stream`](_optimizer_reshard_runtime.md#_BufferSlot.record_compute_stream), [`compute_buffer`](_optimizer_reshard_runtime.md#_BufferSlot.compute_buffer), [`storage_partition_buffer`](_optimizer_reshard_runtime.md#_BufferSlot.storage_partition_buffer)

## Functions
- <a id="_batched_copy_"></a>`_batched_copy_(destinations: tuple[Tensor, ...], sources: tuple[Tensor, ...])` — [`L784`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_runtime.py#L784) — Copy aligned region views with a single foreach launch.
- <a id="_compute_redistributed"></a>`_compute_redistributed(work: _BucketWork[_ItemT], slot: _BufferSlot, *, compute: Callable[[_ItemT, Tensor], None])` — [`L697`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_runtime.py#L697) — documented in [flex-shard](../../../../concepts/flex-shard.md)
- <a id="_execute_packed_all_to_all"></a>`_execute_packed_all_to_all(schedule: _PackedAllToAllSchedule, *, output: Tensor, input: Tensor)` — [`L103`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_runtime.py#L103)
- <a id="_finalize_redistributed"></a>`_finalize_redistributed(work: _BucketWork[_ItemT], slot: _BufferSlot, *, finalize: Callable[[_ItemT, Tensor], None])` — [`L750`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_runtime.py#L750) — documented in [flex-shard](../../../../concepts/flex-shard.md)
- <a id="_include_compute_scratch_requirement"></a>`_include_compute_scratch_requirement(requirements: dict[_BufferKey, _BufferRequirements], item: _ItemT, local_tensor_spec: Callable[[_ItemT], tuple[torch.Size, torch.dtype, torch.device]])` — [`L284`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_runtime.py#L284)
- <a id="_prepare_redistributed"></a>`_prepare_redistributed(plan: _RedistributionBucketPlan[_ItemT], slot: _BufferSlot, storage_buffer: Tensor, *, prepare: Callable[[_ItemT, Tensor], None])` — [`L663`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_runtime.py#L663) — documented in [flex-shard](../../../../concepts/flex-shard.md)
- <a id="_reserve_tensor"></a>`_reserve_tensor(tensor: Tensor | None, *, numel: int, dtype: torch.dtype, device: torch.device)` — [`L86`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_runtime.py#L86)
- <a id="_reserved_view"></a>`_reserved_view(tensor: Tensor | None, numel: int)` — [`L98`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_runtime.py#L98)
- <a id="_tensor_region_view"></a>`_tensor_region_view(tensor: Tensor, region: _TensorRegion)` — [`L799`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_runtime.py#L799)

## Module values
- <a id="_BufferKey._BufferKey"></a>`_BufferKey` — [`L44`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_runtime.py#L44)
- <a id="_NUM_PIPELINE_SLOTS"></a>`_NUM_PIPELINE_SLOTS` — [`L41`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_runtime.py#L41)
- <a id="__all__.__all__"></a>`__all__` — [`L38`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_runtime.py#L38)

