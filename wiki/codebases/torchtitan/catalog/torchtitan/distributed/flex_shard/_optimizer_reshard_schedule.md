---
title: 'Module: torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py'
type: catalog
provenance: extracted
module: torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.distributed.flex_shard._optimizer_reshard_schedule`/
symbols:
  _build_bucket_plans: _build_bucket_plans().
  _ItemT: _ItemT.
  _build_dim0_shard_redistribution_plan: _build_dim0_shard_redistribution_plan().
  _validate_redistribution_plan: _validate_redistribution_plan().
  _build_whole_tensor_redistribution_plan: _build_whole_tensor_redistribution_plan().
  _build_packed_all_to_all_schedule: _build_packed_all_to_all_schedule().
  _TensorRegion.shape: _TensorRegion#shape.
  _TensorRegion: _TensorRegion#
  _TensorRegion.offsets: _TensorRegion#offsets.
  _validate_bucket_plans_across_ranks: _validate_bucket_plans_across_ranks().
  _require_valid_plan: _require_valid_plan().
  _redistribution_plan_key: _redistribution_plan_key().
  _redistribution_plan_key.route_key: _redistribution_plan_key().route_key().
  _TensorRegionRoute.source: _TensorRegionRoute#source.
  _TensorRegionRoute.destination: _TensorRegionRoute#destination.
  _ParticipantPartition.tensor_shape: _ParticipantPartition#tensor_shape.
  _RedistributionPlan.__post_init__: _RedistributionPlan#__post_init__().
  _bind_bucket_configs: _bind_bucket_configs().
  _dtensor_storage_regions: _dtensor_storage_regions().
  _redistribution_plan_key.partition_key: _redistribution_plan_key().partition_key().
  _TensorRegion.numel: _TensorRegion#numel().
  _RedistributionDirection.routes: _RedistributionDirection#routes().
  _validate_participant_logical_partition: _validate_participant_logical_partition().
  _resolve_routes_to_transfers: _resolve_routes_to_transfers().
  _redistribution_group: _redistribution_group().
  _RedistributionPlan: _RedistributionPlan#
  _validate_disjoint_regions_in_bounds: _validate_disjoint_regions_in_bounds().
  _RouteEndpoint.participants: _RouteEndpoint#participants.
  _ParticipantPartition.logical_regions: _ParticipantPartition#logical_regions.
  _validate_regions_cover_partition: _validate_regions_cover_partition().
  _validate_tensor_region_partition: _validate_tensor_region_partition().
  _TensorRegionRoute.logical_region: _TensorRegionRoute#logical_region.
  _dtensor_storage_region_for_participant: _dtensor_storage_region_for_participant().
  _ParticipantPartition: _ParticipantPartition#
  _ParticipantPartition.participant: _ParticipantPartition#participant.
  _RouteEndpoint.tensor_region: _RouteEndpoint#tensor_region.
  _PackedAllToAllSchedule.__post_init__: _PackedAllToAllSchedule#__post_init__().
  _BucketPlan._BucketPlan: _BucketPlan._BucketPlan.
  _RedistributionPlan.storage_partition: _RedistributionPlan#storage_partition().
  _TensorRegionRoute: _TensorRegionRoute#
  _TensorRegionRoute.inverse: _TensorRegionRoute#inverse().
  _RedistributionPlan.participants: _RedistributionPlan#participants.
  _RedistributionPlan.storage_partitions: _RedistributionPlan#storage_partitions.
  _RedistributionPlan.compute_partitions: _RedistributionPlan#compute_partitions.
  _RedistributionPlan.storage_to_compute_routes: _RedistributionPlan#storage_to_compute_routes.
  _RedistributionBucketPlan: _RedistributionBucketPlan#
  _RedistributionPlan.compute_partition: _RedistributionPlan#compute_partition().
  _tensor_region_intersection: _tensor_region_intersection().
  _build_owned_redistribution_plan: _build_owned_redistribution_plan().
  _PackedSpan.region: _PackedSpan#region.
  _LocalBucketPlan: _LocalBucketPlan#
  _RouteEndpoint: _RouteEndpoint#
  _RedistributionPlan.logical_shape: _RedistributionPlan#logical_shape.
  _PackedSpan.numel: _PackedSpan#numel().
  _resolve_buckets: _resolve_buckets().
  _tensor_region_intersection_numel: _tensor_region_intersection_numel().
  _RedistributionBucketPlan.redistribution_plans: _RedistributionBucketPlan#redistribution_plans.
  _RedistributionBucketPlan.group: _RedistributionBucketPlan#group.
  _RedistributionBucketPlan.storage_to_compute_schedule: _RedistributionBucketPlan#storage_to_compute_schedule.
  _RedistributionBucketPlan.compute_to_storage_schedule: _RedistributionBucketPlan#compute_to_storage_schedule.
  _StorageRegionMapping._StorageRegionMapping: _StorageRegionMapping._StorageRegionMapping.
  _PackedSpan.buffer_offset: _PackedSpan#buffer_offset.
  _RedistributionGroup.participants: _RedistributionGroup#participants.
  _RedistributionBucketPlan.device: _RedistributionBucketPlan#device.
  _BucketPlanningContext.group: _BucketPlanningContext#group.
  _RedistributionBucketPlan.redistributed_items: _RedistributionBucketPlan#redistributed_items.
  _PackedAllToAllSchedule.input_buffer_numel: _PackedAllToAllSchedule#input_buffer_numel.
  _PackedAllToAllSchedule.output_buffer_numel: _PackedAllToAllSchedule#output_buffer_numel.
  _RedistributionBucketPlan.dtype: _RedistributionBucketPlan#dtype.
  _BucketPlanningResult.plans: _BucketPlanningResult#plans.
  _BucketPlanningContext: _BucketPlanningContext#
  _RedistributionBucketPlan.unredistributed_items: _RedistributionBucketPlan#unredistributed_items.
  _PackedSpan: _PackedSpan#
  _PackedAllToAllSchedule: _PackedAllToAllSchedule#
  _RedistributionGroup: _RedistributionGroup#
  _device_mesh_ranks: _device_mesh_ranks().
  _require_valid_planner_result: _require_valid_planner_result().
  _PackedAllToAllSchedule.input_spans_by_parameter: _PackedAllToAllSchedule#input_spans_by_parameter.
  _PackedAllToAllSchedule.output_spans_by_parameter: _PackedAllToAllSchedule#output_spans_by_parameter.
  _BucketPlanningContext.items: _BucketPlanningContext#items.
  _ParticipantPartition.__post_init__: _ParticipantPartition#__post_init__().
  _RedistributionDirection: _RedistributionDirection#
  _RedistributionGroup.local_participant: _RedistributionGroup#local_participant.
  _BucketPlanningResult: _BucketPlanningResult#
  _BucketPlanningResult.ordered_items: _BucketPlanningResult#ordered_items.
  _packed_spans_by_parameter: _packed_spans_by_parameter().
  _RedistributionPlan.compute_to_storage_routes: _RedistributionPlan#compute_to_storage_routes.
  _DTensorStorageDomain._DTensorStorageDomain: _DTensorStorageDomain._DTensorStorageDomain.
  _RedistributionDirection.STORAGE_TO_COMPUTE: _RedistributionDirection#STORAGE_TO_COMPUTE.
  _PackedAllToAllSchedule.has_remote_transfers: _PackedAllToAllSchedule#has_remote_transfers.
  _PackedAllToAllSchedule.input_split_sizes: _PackedAllToAllSchedule#input_split_sizes.
  _PackedAllToAllSchedule.output_split_sizes: _PackedAllToAllSchedule#output_split_sizes.
  _RedistributionGroup.mesh_axis_participants: _RedistributionGroup#mesh_axis_participants.
  _LocalBucketPlan.items: _LocalBucketPlan#items.
  _RouteEndpoint.__post_init__: _RouteEndpoint#__post_init__().
  _PackedAllToAllSchedule.process_group: _PackedAllToAllSchedule#process_group.
  _RedistributionGroup.process_group: _RedistributionGroup#process_group.
  _RedistributionDirection.COMPUTE_TO_STORAGE: _RedistributionDirection#COMPUTE_TO_STORAGE.
  _PackedAllToAllSchedule.participants: _PackedAllToAllSchedule#participants.
  _PackedAllToAllSchedule.local_participant: _PackedAllToAllSchedule#local_participant.
  _BucketPlanningContext.name: _BucketPlanningContext#name.
  __all__.__all__: __all__.__all__.
---
# Module: [`torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py)

## Classes
### <a id="_BucketPlanningContext"></a>`_BucketPlanningContext`  ·  implements/extends Generic
- def: [`torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py:749`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L749)
- signature: `class _BucketPlanningContext(Generic[_ItemT]):`
- members:
  - <a id="_BucketPlanningContext.group"></a>`group` — [`L751`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L751)
  - <a id="_BucketPlanningContext.items"></a>`items` — [`L750`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L750)
  - <a id="_BucketPlanningContext.name"></a>`name` — [`L752`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L752)
- uses (calls/refs, reference-scoped): [`_ItemT`](_optimizer_reshard_schedule.md#_ItemT), [`_RedistributionGroup`](_optimizer_reshard_schedule.md#_RedistributionGroup)
- used by: [`_build_bucket_plans`](_optimizer_reshard_schedule.md#_build_bucket_plans), [`_resolve_muon_redistribution_plans`](dist_muon.md#_resolve_muon_redistribution_plans)

### <a id="_BucketPlanningResult"></a>`_BucketPlanningResult`  ·  implements/extends Generic
- def: [`torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py:776`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L776)
- signature: `class _BucketPlanningResult(Generic[_ItemT]):`
- members:
  - <a id="_BucketPlanningResult.ordered_items"></a>`ordered_items` — [`L778`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L778)
  - <a id="_BucketPlanningResult.plans"></a>`plans` — [`L777`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L777)
- uses (calls/refs, reference-scoped): [`_ItemT`](_optimizer_reshard_schedule.md#_ItemT), [`_BucketPlan`](_optimizer_reshard_schedule.md#_BucketPlan._BucketPlan)
- used by: [`_build_bucket_plans`](_optimizer_reshard_schedule.md#_build_bucket_plans), [`_bucket_plans`](dist_muon.md#DistMuon._bucket_plans), [`_parameter_compute_layouts`](dist_muon.md#DistMuon._parameter_compute_layouts)

### <a id="_LocalBucketPlan"></a>`_LocalBucketPlan`  ·  implements/extends Generic
- def: [`torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py:756`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L756)
- signature: `class _LocalBucketPlan(Generic[_ItemT]):`
- members:
  - <a id="_LocalBucketPlan.items"></a>`items` — [`L757`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L757)
- uses (calls/refs, reference-scoped): [`_ItemT`](_optimizer_reshard_schedule.md#_ItemT)
- used by: [`reserve_buffers`](_optimizer_reshard_runtime.md#_BucketedRedistributionRuntime.reserve_buffers), [`_build_bucket_plans`](_optimizer_reshard_schedule.md#_build_bucket_plans), [`run`](_optimizer_reshard_runtime.md#_BucketedRedistributionRuntime.run), [`_validate_bucket_plans_across_ranks`](_optimizer_reshard_schedule.md#_validate_bucket_plans_across_ranks), [`prefetch_next`](_optimizer_reshard_runtime.md#_BucketedRedistributionRuntime.prefetch_next), [`_BucketPlan`](_optimizer_reshard_schedule.md#_BucketPlan._BucketPlan)

### <a id="_PackedAllToAllSchedule"></a>`_PackedAllToAllSchedule`
- def: [`torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py:718`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L718)
- signature: `class _PackedAllToAllSchedule:`
- members:
  - <a id="_PackedAllToAllSchedule.has_remote_transfers"></a>`has_remote_transfers` — [`L722`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L722)
  - <a id="_PackedAllToAllSchedule.input_buffer_numel"></a>`input_buffer_numel` — [`L727`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L727)
  - <a id="_PackedAllToAllSchedule.input_spans_by_parameter"></a>`input_spans_by_parameter` — [`L725`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L725)
  - <a id="_PackedAllToAllSchedule.input_split_sizes"></a>`input_split_sizes` — [`L723`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L723)
  - <a id="_PackedAllToAllSchedule.local_participant"></a>`local_participant` — [`L721`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L721)
  - <a id="_PackedAllToAllSchedule.output_buffer_numel"></a>`output_buffer_numel` — [`L728`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L728)
  - <a id="_PackedAllToAllSchedule.output_spans_by_parameter"></a>`output_spans_by_parameter` — [`L726`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L726)
  - <a id="_PackedAllToAllSchedule.output_split_sizes"></a>`output_split_sizes` — [`L724`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L724)
  - <a id="_PackedAllToAllSchedule.participants"></a>`participants` — [`L720`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L720)
  - <a id="_PackedAllToAllSchedule.process_group"></a>`process_group` — [`L719`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L719)
- protocol/private: <a id="_PackedAllToAllSchedule.__post_init__"></a>`__post_init__`[`L730`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L730)
- uses (calls/refs, reference-scoped): [`_PackedSpan`](_optimizer_reshard_schedule.md#_PackedSpan)
- used by: [`reserve_buffers`](_optimizer_reshard_runtime.md#_BucketedRedistributionRuntime.reserve_buffers), [`_compute_redistributed`](_optimizer_reshard_runtime.md#_compute_redistributed), [`_finalize_redistributed`](_optimizer_reshard_runtime.md#_finalize_redistributed), [`_prepare_redistributed`](_optimizer_reshard_runtime.md#_prepare_redistributed), [`_build_packed_all_to_all_schedule`](_optimizer_reshard_schedule.md#_build_packed_all_to_all_schedule), [`communication_buffers`](_optimizer_reshard_runtime.md#_BufferSlot.communication_buffers), [`_execute_packed_all_to_all`](_optimizer_reshard_runtime.md#_execute_packed_all_to_all), [`compute_to_storage_schedule`](_optimizer_reshard_schedule.md#_RedistributionBucketPlan.compute_to_storage_schedule), [`storage_to_compute_schedule`](_optimizer_reshard_schedule.md#_RedistributionBucketPlan.storage_to_compute_schedule)

### <a id="_PackedSpan"></a>`_PackedSpan`
- def: [`torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py:706`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L706)
- doc: Physical packed-buffer location for an endpoint tensor region.
- signature: `class _PackedSpan:`
- members:
  - <a id="_PackedSpan.numel"></a>`numel(self)` — [`L713`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L713)
  - <a id="_PackedSpan.buffer_offset"></a>`buffer_offset` — [`L710`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L710)
  - <a id="_PackedSpan.region"></a>`region` — [`L709`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L709)
- uses (calls/refs, reference-scoped): [`_TensorRegion`](_optimizer_reshard_schedule.md#_TensorRegion), [`numel`](_optimizer_reshard_schedule.md#_TensorRegion.numel)
- used by: [`_compute_redistributed`](_optimizer_reshard_runtime.md#_compute_redistributed), [`_finalize_redistributed`](_optimizer_reshard_runtime.md#_finalize_redistributed), [`_prepare_redistributed`](_optimizer_reshard_runtime.md#_prepare_redistributed), [`_build_packed_all_to_all_schedule`](_optimizer_reshard_schedule.md#_build_packed_all_to_all_schedule), [`input_spans_by_parameter`](_optimizer_reshard_schedule.md#_PackedAllToAllSchedule.input_spans_by_parameter), [`output_spans_by_parameter`](_optimizer_reshard_schedule.md#_PackedAllToAllSchedule.output_spans_by_parameter), [`_packed_spans_by_parameter`](_optimizer_reshard_schedule.md#_packed_spans_by_parameter)

### <a id="_ParticipantPartition"></a>`_ParticipantPartition`
- def: [`torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py:134`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L134)
- doc: One participant's tensor shape and its global logical regions.
- signature: `class _ParticipantPartition:`
- members:
  - <a id="_ParticipantPartition.logical_regions"></a>`logical_regions` — [`L139`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L139)
  - <a id="_ParticipantPartition.participant"></a>`participant` — [`L137`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L137)
  - <a id="_ParticipantPartition.tensor_shape"></a>`tensor_shape` — [`L138`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L138)
- protocol/private: <a id="_ParticipantPartition.__post_init__"></a>`__post_init__`[`L141`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L141)
- uses (calls/refs, reference-scoped): [`_TensorRegion`](_optimizer_reshard_schedule.md#_TensorRegion)
- used by: [`reserve_buffers`](_optimizer_reshard_runtime.md#_BucketedRedistributionRuntime.reserve_buffers), [`_build_bucket_plans`](_optimizer_reshard_schedule.md#_build_bucket_plans), [`_compute_redistributed`](_optimizer_reshard_runtime.md#_compute_redistributed), [`_finalize_redistributed`](_optimizer_reshard_runtime.md#_finalize_redistributed), [`_build_dim0_shard_redistribution_plan`](_optimizer_reshard_schedule.md#_build_dim0_shard_redistribution_plan), [`_validate_redistribution_plan`](_optimizer_reshard_schedule.md#_validate_redistribution_plan), [`_build_batched_matrix_redistribution_plan`](dist_muon.md#_build_batched_matrix_redistribution_plan), [`_build_whole_tensor_redistribution_plan`](_optimizer_reshard_schedule.md#_build_whole_tensor_redistribution_plan), [`_prepare_redistributed`](_optimizer_reshard_runtime.md#_prepare_redistributed), [`partition_key`](_optimizer_reshard_schedule.md#_redistribution_plan_key.partition_key), [`_validate_participant_logical_partition`](_optimizer_reshard_schedule.md#_validate_participant_logical_partition), [`storage_partition`](_optimizer_reshard_schedule.md#_RedistributionPlan.storage_partition), [`compute_partitions`](_optimizer_reshard_schedule.md#_RedistributionPlan.compute_partitions), [`storage_partitions`](_optimizer_reshard_schedule.md#_RedistributionPlan.storage_partitions), [`compute_partition`](_optimizer_reshard_schedule.md#_RedistributionPlan.compute_partition)

### <a id="_RedistributionBucketPlan"></a>`_RedistributionBucketPlan`  ·  implements/extends Generic
- def: [`torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py:761`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L761)
- signature: `class _RedistributionBucketPlan(Generic[_ItemT]):`
- members:
  - <a id="_RedistributionBucketPlan.compute_to_storage_schedule"></a>`compute_to_storage_schedule` — [`L767`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L767)
  - <a id="_RedistributionBucketPlan.device"></a>`device` — [`L769`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L769)
  - <a id="_RedistributionBucketPlan.dtype"></a>`dtype` — [`L768`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L768)
  - <a id="_RedistributionBucketPlan.group"></a>`group` — [`L765`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L765)
  - <a id="_RedistributionBucketPlan.redistributed_items"></a>`redistributed_items` — [`L763`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L763)
  - <a id="_RedistributionBucketPlan.redistribution_plans"></a>`redistribution_plans` — [`L764`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L764)
  - <a id="_RedistributionBucketPlan.storage_to_compute_schedule"></a>`storage_to_compute_schedule` — [`L766`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L766)
  - <a id="_RedistributionBucketPlan.unredistributed_items"></a>`unredistributed_items` — [`L762`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L762)
- uses (calls/refs, reference-scoped): [`_ItemT`](_optimizer_reshard_schedule.md#_ItemT), [`_RedistributionPlan`](_optimizer_reshard_schedule.md#_RedistributionPlan), [`_PackedAllToAllSchedule`](_optimizer_reshard_schedule.md#_PackedAllToAllSchedule), [`_RedistributionGroup`](_optimizer_reshard_schedule.md#_RedistributionGroup)
- used by: [`reserve_buffers`](_optimizer_reshard_runtime.md#_BucketedRedistributionRuntime.reserve_buffers), [`_build_bucket_plans`](_optimizer_reshard_schedule.md#_build_bucket_plans), [`_compute_redistributed`](_optimizer_reshard_runtime.md#_compute_redistributed), [`_finalize_redistributed`](_optimizer_reshard_runtime.md#_finalize_redistributed), [`_prepare_redistributed`](_optimizer_reshard_runtime.md#_prepare_redistributed), [`_enqueue_compute_to_storage`](_optimizer_reshard_runtime.md#_BucketedRedistributionRuntime._enqueue_compute_to_storage), [`_enqueue_storage_to_compute`](_optimizer_reshard_runtime.md#_BucketedRedistributionRuntime._enqueue_storage_to_compute), [`_compute_bucket`](_optimizer_reshard_runtime.md#_BucketedRedistributionRuntime._compute_bucket), [`_validate_bucket_plans_across_ranks`](_optimizer_reshard_schedule.md#_validate_bucket_plans_across_ranks), [`communication_buffers`](_optimizer_reshard_runtime.md#_BufferSlot.communication_buffers), [`_BucketPlan`](_optimizer_reshard_schedule.md#_BucketPlan._BucketPlan), [`plan`](_optimizer_reshard_runtime.md#_BucketWork.plan)

### <a id="_RedistributionDirection"></a>`_RedistributionDirection`  ·  implements/extends Enum
- def: [`torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py:173`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L173)
- signature: `class _RedistributionDirection(Enum):`
- members:
  - <a id="_RedistributionDirection.routes"></a>`routes(self, plan: _RedistributionPlan)` — [`L177`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L177)
  - <a id="_RedistributionDirection.COMPUTE_TO_STORAGE"></a>`COMPUTE_TO_STORAGE` — [`L175`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L175)
  - <a id="_RedistributionDirection.STORAGE_TO_COMPUTE"></a>`STORAGE_TO_COMPUTE` — [`L174`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L174)
- uses (calls/refs, reference-scoped): [`_RedistributionPlan`](_optimizer_reshard_schedule.md#_RedistributionPlan), [`_TensorRegionRoute`](_optimizer_reshard_schedule.md#_TensorRegionRoute), [`storage_to_compute_routes`](_optimizer_reshard_schedule.md#_RedistributionPlan.storage_to_compute_routes), [`compute_to_storage_routes`](_optimizer_reshard_schedule.md#_RedistributionPlan.compute_to_storage_routes)
- used by: [`_build_bucket_plans`](_optimizer_reshard_schedule.md#_build_bucket_plans), [`_validate_redistribution_plan`](_optimizer_reshard_schedule.md#_validate_redistribution_plan), [`_build_packed_all_to_all_schedule`](_optimizer_reshard_schedule.md#_build_packed_all_to_all_schedule)

### <a id="_RedistributionGroup"></a>`_RedistributionGroup`
- def: [`torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py:741`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L741)
- signature: `class _RedistributionGroup:`
- members:
  - <a id="_RedistributionGroup.local_participant"></a>`local_participant` — [`L745`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L745)
  - <a id="_RedistributionGroup.mesh_axis_participants"></a>`mesh_axis_participants` — [`L744`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L744)
  - <a id="_RedistributionGroup.participants"></a>`participants` — [`L743`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L743)
  - <a id="_RedistributionGroup.process_group"></a>`process_group` — [`L742`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L742)
- used by: [`reserve_buffers`](_optimizer_reshard_runtime.md#_BucketedRedistributionRuntime.reserve_buffers), [`_compute_redistributed`](_optimizer_reshard_runtime.md#_compute_redistributed), [`_finalize_redistributed`](_optimizer_reshard_runtime.md#_finalize_redistributed), [`_prepare_redistributed`](_optimizer_reshard_runtime.md#_prepare_redistributed), [`_build_parameter_redistribution_plan`](dist_muon.md#_build_parameter_redistribution_plan), [`_resolve_muon_redistribution_plans`](dist_muon.md#_resolve_muon_redistribution_plans), [`_validate_bucket_plans_across_ranks`](_optimizer_reshard_schedule.md#_validate_bucket_plans_across_ranks), [`_redistribution_group`](_optimizer_reshard_schedule.md#_redistribution_group), [`group`](_optimizer_reshard_schedule.md#_RedistributionBucketPlan.group), [`group`](_optimizer_reshard_schedule.md#_BucketPlanningContext.group)

### <a id="_RedistributionPlan"></a>`_RedistributionPlan`
- def: [`torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py:184`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L184)
- members:
  - <a id="_RedistributionPlan.compute_partition"></a>`compute_partition(self, participant: int)` — [`L216`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L216)
  - <a id="_RedistributionPlan.storage_partition"></a>`storage_partition(self, participant: int)` — [`L209`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L209)
  - <a id="_RedistributionPlan.compute_partitions"></a>`compute_partitions` — [`L190`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L190)
  - <a id="_RedistributionPlan.compute_to_storage_routes"></a>`compute_to_storage_routes` — [`L192`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L192)
  - <a id="_RedistributionPlan.logical_shape"></a>`logical_shape` — [`L188`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L188)
  - <a id="_RedistributionPlan.participants"></a>`participants` — [`L187`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L187)
  - <a id="_RedistributionPlan.storage_partitions"></a>`storage_partitions` — [`L189`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L189)
  - <a id="_RedistributionPlan.storage_to_compute_routes"></a>`storage_to_compute_routes` — [`L191`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L191)
- protocol/private: <a id="_RedistributionPlan.__post_init__"></a>`__post_init__`[`L194`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L194)
- uses (calls/refs, reference-scoped): [`_validate_redistribution_plan`](_optimizer_reshard_schedule.md#_validate_redistribution_plan), [`_ParticipantPartition`](_optimizer_reshard_schedule.md#_ParticipantPartition), [`participant`](_optimizer_reshard_schedule.md#_ParticipantPartition.participant), [`_TensorRegionRoute`](_optimizer_reshard_schedule.md#_TensorRegionRoute), [`inverse`](_optimizer_reshard_schedule.md#_TensorRegionRoute.inverse)
- used by: [`reserve_buffers`](_optimizer_reshard_runtime.md#_BucketedRedistributionRuntime.reserve_buffers), [`_build_bucket_plans`](_optimizer_reshard_schedule.md#_build_bucket_plans), [`_compute_redistributed`](_optimizer_reshard_runtime.md#_compute_redistributed), [`_finalize_redistributed`](_optimizer_reshard_runtime.md#_finalize_redistributed), [`_build_dim0_shard_redistribution_plan`](_optimizer_reshard_schedule.md#_build_dim0_shard_redistribution_plan), [`_validate_redistribution_plan`](_optimizer_reshard_schedule.md#_validate_redistribution_plan), [`_build_batched_matrix_redistribution_plan`](dist_muon.md#_build_batched_matrix_redistribution_plan), [`_build_whole_tensor_redistribution_plan`](_optimizer_reshard_schedule.md#_build_whole_tensor_redistribution_plan), [`_prepare_redistributed`](_optimizer_reshard_runtime.md#_prepare_redistributed), [`_build_packed_all_to_all_schedule`](_optimizer_reshard_schedule.md#_build_packed_all_to_all_schedule), [`_build_parameter_redistribution_plan`](dist_muon.md#_build_parameter_redistribution_plan), [`_resolve_muon_redistribution_plans`](dist_muon.md#_resolve_muon_redistribution_plans), [`_redistribution_plan_key`](_optimizer_reshard_schedule.md#_redistribution_plan_key), [`routes`](_optimizer_reshard_schedule.md#_RedistributionDirection.routes), [`_build_owned_redistribution_plan`](_optimizer_reshard_schedule.md#_build_owned_redistribution_plan), [`redistribution_plans`](_optimizer_reshard_schedule.md#_RedistributionBucketPlan.redistribution_plans)

### <a id="_RouteEndpoint"></a>`_RouteEndpoint`
- def: [`torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py:147`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L147)
- doc: One route endpoint's local tensor region and participants.
- signature: `class _RouteEndpoint:`
- members:
  - <a id="_RouteEndpoint.participants"></a>`participants` — [`L151`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L151)
  - <a id="_RouteEndpoint.tensor_region"></a>`tensor_region` — [`L150`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L150)
- protocol/private: <a id="_RouteEndpoint.__post_init__"></a>`__post_init__`[`L153`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L153)
- uses (calls/refs, reference-scoped): [`_TensorRegion`](_optimizer_reshard_schedule.md#_TensorRegion)
- used by: [`_build_dim0_shard_redistribution_plan`](_optimizer_reshard_schedule.md#_build_dim0_shard_redistribution_plan), [`_validate_redistribution_plan`](_optimizer_reshard_schedule.md#_validate_redistribution_plan), [`_build_batched_matrix_redistribution_plan`](dist_muon.md#_build_batched_matrix_redistribution_plan), [`_build_whole_tensor_redistribution_plan`](_optimizer_reshard_schedule.md#_build_whole_tensor_redistribution_plan), [`route_key`](_optimizer_reshard_schedule.md#_redistribution_plan_key.route_key), [`destination`](_optimizer_reshard_schedule.md#_TensorRegionRoute.destination), [`source`](_optimizer_reshard_schedule.md#_TensorRegionRoute.source), [`_resolve_routes_to_transfers`](_optimizer_reshard_schedule.md#_resolve_routes_to_transfers)

### <a id="_TensorRegion"></a>`_TensorRegion`
- def: [`torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py:114`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L114) — documented in [flex-shard](../../../../concepts/flex-shard.md)
- doc: One rectangular tensor region.
- signature: `class _TensorRegion:`
- members:
  - <a id="_TensorRegion.numel"></a>`numel(self)` — [`L121`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L121)
  - <a id="_TensorRegion.offsets"></a>`offsets` — [`L117`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L117) — documented in [flex-shard](../../../../concepts/flex-shard.md)
  - <a id="_TensorRegion.shape"></a>`shape` — [`L118`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L118) — documented in [flex-shard](../../../../concepts/flex-shard.md)
- used by: [`_compute_redistributed`](_optimizer_reshard_runtime.md#_compute_redistributed), [`_finalize_redistributed`](_optimizer_reshard_runtime.md#_finalize_redistributed), [`_build_dim0_shard_redistribution_plan`](_optimizer_reshard_schedule.md#_build_dim0_shard_redistribution_plan), [`_validate_redistribution_plan`](_optimizer_reshard_schedule.md#_validate_redistribution_plan), [`_build_batched_matrix_redistribution_plan`](dist_muon.md#_build_batched_matrix_redistribution_plan), [`_build_whole_tensor_redistribution_plan`](_optimizer_reshard_schedule.md#_build_whole_tensor_redistribution_plan), [`_build_packed_all_to_all_schedule`](_optimizer_reshard_schedule.md#_build_packed_all_to_all_schedule), [`route_key`](_optimizer_reshard_schedule.md#_redistribution_plan_key.route_key), [`_dtensor_storage_regions`](_optimizer_reshard_schedule.md#_dtensor_storage_regions), [`partition_key`](_optimizer_reshard_schedule.md#_redistribution_plan_key.partition_key), [`_resolve_routes_to_transfers`](_optimizer_reshard_schedule.md#_resolve_routes_to_transfers), [`_validate_participant_logical_partition`](_optimizer_reshard_schedule.md#_validate_participant_logical_partition), [`_validate_disjoint_regions_in_bounds`](_optimizer_reshard_schedule.md#_validate_disjoint_regions_in_bounds), [`_validate_regions_cover_partition`](_optimizer_reshard_schedule.md#_validate_regions_cover_partition), [`logical_regions`](_optimizer_reshard_schedule.md#_ParticipantPartition.logical_regions), [`_validate_tensor_region_partition`](_optimizer_reshard_schedule.md#_validate_tensor_region_partition), [`_dtensor_storage_region_for_participant`](_optimizer_reshard_schedule.md#_dtensor_storage_region_for_participant), [`logical_region`](_optimizer_reshard_schedule.md#_TensorRegionRoute.logical_region), [`tensor_region`](_optimizer_reshard_schedule.md#_RouteEndpoint.tensor_region), [`_tensor_region_view`](_optimizer_reshard_runtime.md#_tensor_region_view), [`_tensor_region_intersection`](_optimizer_reshard_schedule.md#_tensor_region_intersection), [`region`](_optimizer_reshard_schedule.md#_PackedSpan.region), [`numel`](_optimizer_reshard_schedule.md#_PackedSpan.numel), [`_StorageRegionMapping`](_optimizer_reshard_schedule.md#_StorageRegionMapping._StorageRegionMapping), [`_tensor_region_intersection_numel`](_optimizer_reshard_schedule.md#_tensor_region_intersection_numel)

### <a id="_TensorRegionRoute"></a>`_TensorRegionRoute`
- def: [`torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py:158`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L158)
- doc: Map one logical region between differently shaped endpoint tensors.
- signature: `class _TensorRegionRoute:`
- members:
  - <a id="_TensorRegionRoute.inverse"></a>`inverse(self)` — [`L165`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L165)
  - <a id="_TensorRegionRoute.destination"></a>`destination` — [`L163`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L163)
  - <a id="_TensorRegionRoute.logical_region"></a>`logical_region` — [`L161`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L161)
  - <a id="_TensorRegionRoute.source"></a>`source` — [`L162`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L162)
- uses (calls/refs, reference-scoped): [`_TensorRegion`](_optimizer_reshard_schedule.md#_TensorRegion), [`_RouteEndpoint`](_optimizer_reshard_schedule.md#_RouteEndpoint)
- used by: [`_build_dim0_shard_redistribution_plan`](_optimizer_reshard_schedule.md#_build_dim0_shard_redistribution_plan), [`_validate_redistribution_plan`](_optimizer_reshard_schedule.md#_validate_redistribution_plan), [`_build_batched_matrix_redistribution_plan`](dist_muon.md#_build_batched_matrix_redistribution_plan), [`_build_whole_tensor_redistribution_plan`](_optimizer_reshard_schedule.md#_build_whole_tensor_redistribution_plan), [`route_key`](_optimizer_reshard_schedule.md#_redistribution_plan_key.route_key), [`__post_init__`](_optimizer_reshard_schedule.md#_RedistributionPlan.__post_init__), [`_resolve_routes_to_transfers`](_optimizer_reshard_schedule.md#_resolve_routes_to_transfers), [`routes`](_optimizer_reshard_schedule.md#_RedistributionDirection.routes), [`storage_to_compute_routes`](_optimizer_reshard_schedule.md#_RedistributionPlan.storage_to_compute_routes), [`compute_to_storage_routes`](_optimizer_reshard_schedule.md#_RedistributionPlan.compute_to_storage_routes)

## Functions
- <a id="_bind_bucket_configs"></a>`_bind_bucket_configs(configs: Sequence[BucketConfig], items: Sequence[_ItemT], *, get_fqn: Callable[[_ItemT], str], get_storage_dtensor: Callable[[_ItemT], DTensor], requires_redistribution: Callable[[_ItemT], bool], get_redistribution_storage_mesh_axis: Callable[[_ItemT], int | None])` — [`L33`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L33) — Bind configs after each item's redistribution requirement is resolved. — documented in [flex-shard](../../../../concepts/flex-shard.md)
- <a id="_build_bucket_plans"></a>`_build_bucket_plans(items: Sequence[_ItemT], specs: Sequence[_BucketSpec], *, get_fqn: Callable[[_ItemT], str], get_storage_dtensor: Callable[[_ItemT], DTensor], requires_redistribution: Callable[[_ItemT], bool], resolve_redistribution_plans: Callable[[tuple[_BucketPlanningContext[_ItemT], ...]], Sequence[Sequence[_RedistributionPlan | None]],])` — [`L1061`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L1061) — Build ordered optimizer bucket plans with and without redistribution. — documented in [flex-shard](../../../../concepts/flex-shard.md)
- <a id="_build_dim0_shard_redistribution_plan"></a>`_build_dim0_shard_redistribution_plan(storage_regions: Sequence[_StorageRegionMapping], *, participants: tuple[int, ...], shard_participants: tuple[int, ...], logical_shape: tuple[int, ...])` — [`L585`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L585) — Route storage regions to dim-0 compute shards. — documented in [flex-shard](../../../../concepts/flex-shard.md)
- <a id="_build_owned_redistribution_plan"></a>`_build_owned_redistribution_plan(storage_regions: Sequence[_StorageRegionMapping], *, participants: tuple[int, ...], owner_rank: int, logical_shape: tuple[int, ...])` — [`L569`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L569) — Build mirrored routes to one whole-tensor compute owner.
- <a id="_build_packed_all_to_all_schedule"></a>`_build_packed_all_to_all_schedule(redistribution_plans: tuple[_RedistributionPlan, ...], *, direction: _RedistributionDirection, process_group: dist.ProcessGroup, local_participant: int)` — [`L818`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L818) — Build this participant's packed all-to-all schedule from route plans. — documented in [flex-shard](../../../../concepts/flex-shard.md)
- <a id="_build_whole_tensor_redistribution_plan"></a>`_build_whole_tensor_redistribution_plan(storage_regions: Sequence[_StorageRegionMapping], *, participants: tuple[int, ...], compute_participants: tuple[int, ...], logical_shape: tuple[int, ...])` — [`L482`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L482) — Build whole-tensor compute from a canonical region-to-holders mapping. — documented in [flex-shard](../../../../concepts/flex-shard.md)
- <a id="_device_mesh_ranks"></a>`_device_mesh_ranks(mesh: DeviceMesh)` — [`L893`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L893)
- <a id="_dtensor_storage_region_for_participant"></a>`_dtensor_storage_region_for_participant(tensor: DTensor, participant: int)` — [`L913`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L913)
- <a id="_dtensor_storage_regions"></a>`_dtensor_storage_regions(tensor: DTensor, participants: tuple[int, ...], *, required_storage_mesh_axis: int | None)` — [`L949`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L949) — Return the transport-local shape and holder-to-region mappings.
- <a id="_packed_spans_by_parameter"></a>`_packed_spans_by_parameter(indexed_spans: list[tuple[int, _PackedSpan]], num_parameters: int)` — [`L805`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L805)
- <a id="_redistribution_group"></a>`_redistribution_group(mesh: DeviceMesh)` — [`L899`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L899)
- <a id="_redistribution_plan_key"></a>`_redistribution_plan_key(plan: _RedistributionPlan)` — [`L1257`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L1257)
- <a id="_require_valid_plan"></a>`_require_valid_plan(condition: bool, message: str)` — [`L224`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L224)
- <a id="_require_valid_planner_result"></a>`_require_valid_planner_result(condition: bool, message: str)` — [`L1056`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L1056)
- <a id="_resolve_buckets"></a>`_resolve_buckets(items: Sequence[_ItemT], specs: Sequence[_BucketSpec], *, get_fqn: Callable[[_ItemT], str])` — [`L93`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L93)
- <a id="_resolve_routes_to_transfers"></a>`_resolve_routes_to_transfers(routes: tuple[_TensorRegionRoute, ...], participants: tuple[int, ...])` — [`L781`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L781)
- <a id="_tensor_region_intersection"></a>`_tensor_region_intersection(first: _TensorRegion, second: _TensorRegion)` — [`L414`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L414)
- <a id="_tensor_region_intersection_numel"></a>`_tensor_region_intersection_numel(first: _TensorRegion, second: _TensorRegion)` — [`L407`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L407)
- <a id="_validate_bucket_plans_across_ranks"></a>`_validate_bucket_plans_across_ranks(plans: Sequence[_BucketPlan[_ItemT]], *, item_signature: Callable[[_ItemT], tuple[Any, ...]])` — [`L1217`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L1217) — Collectively verify rank-stable redistribution plans. — documented in [flex-shard](../../../../concepts/flex-shard.md)
- <a id="_validate_disjoint_regions_in_bounds"></a>`_validate_disjoint_regions_in_bounds(regions: tuple[_TensorRegion, ...], bounds_shape: tuple[int, ...], *, direction: str)` — [`L321`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L321)
- <a id="_validate_participant_logical_partition"></a>`_validate_participant_logical_partition(partition: _ParticipantPartition, logical_shape: tuple[int, ...], *, direction: str)` — [`L389`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L389)
- <a id="_validate_redistribution_plan"></a>`_validate_redistribution_plan(plan: _RedistributionPlan)` — [`L229`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L229) — Validate the complete internal plan once, before building schedules. — documented in [flex-shard](../../../../concepts/flex-shard.md)
- <a id="_validate_regions_cover_partition"></a>`_validate_regions_cover_partition(regions: tuple[_TensorRegion, ...], expected: tuple[_TensorRegion, ...], logical_shape: tuple[int, ...], *, direction: str)` — [`L450`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L450) — Validate that nonoverlapping regions exactly cover an expected partition.
- <a id="_validate_tensor_region_partition"></a>`_validate_tensor_region_partition(regions: tuple[_TensorRegion, ...], logical_shape: tuple[int, ...], *, direction: str)` — [`L371`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L371)
- <a id="_redistribution_plan_key.partition_key"></a>`partition_key(partition: _ParticipantPartition)` — [`L1258`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L1258)
- <a id="_redistribution_plan_key.route_key"></a>`route_key(route: _TensorRegionRoute)` — [`L1267`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L1267)

## Module values
- <a id="_BucketPlan._BucketPlan"></a>`_BucketPlan` — [`L772`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L772)
- <a id="_DTensorStorageDomain._DTensorStorageDomain"></a>`_DTensorStorageDomain` — [`L128`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L128)
- <a id="_ItemT"></a>`_ItemT` — [`L30`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L30)
- <a id="_StorageRegionMapping._StorageRegionMapping"></a>`_StorageRegionMapping` — [`L127`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L127)
- <a id="__all__.__all__"></a>`__all__` — [`L27`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py#L27)

