---
title: 'Module: torchtitan/distributed/flex_shard/dist_muon.py'
type: catalog
provenance: extracted
module: torchtitan/distributed/flex_shard/dist_muon.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.distributed.flex_shard.dist_muon`/
symbols:
  _initialize_dist_muon: _initialize_dist_muon().
  DistMuon._build_parameter_compute_layouts: DistMuon#_build_parameter_compute_layouts().
  _resolve_storage_to_compute_transition: _resolve_storage_to_compute_transition().
  _build_batched_matrix_redistribution_plan: _build_batched_matrix_redistribution_plan().
  _build_parameter_redistribution_plan: _build_parameter_redistribution_plan().
  _resolve_muon_redistribution_plans: _resolve_muon_redistribution_plans().
  _ParameterComputeLayout.param: _ParameterComputeLayout#param.
  DistMuon: DistMuon#
  DistMuon._plan_item_signature: DistMuon#_plan_item_signature().
  DistMuon._preflight_step: DistMuon#_preflight_step().
  _after_load_state_dict: _after_load_state_dict().
  _assign_balanced_owner_ranks: _assign_balanced_owner_ranks().
  _matrix_batch_view_from_compute_layout: _matrix_batch_view_from_compute_layout().
  _resolve_storage_to_compute_redistribution_requirement: _resolve_storage_to_compute_redistribution_requirement().
  DistMuon._initialize_plan: DistMuon#_initialize_plan().
  _ParameterComputeLayout: _ParameterComputeLayout#
  DistMuon._has_storage_layout: DistMuon#_has_storage_layout().
  _normalize_storage_placement: _normalize_storage_placement().
  DistMuon._apply_update: DistMuon#_apply_update().
  _normalize_dim: _normalize_dim().
  DistMuon._compute_update: DistMuon#_compute_update().
  _normalize_compute_placement: _normalize_compute_placement().
  build_dist_muon: build_dist_muon().
  _ParameterComputeLayout.storage_is_compute_ready: _ParameterComputeLayout#storage_is_compute_ready().
  _row_intervals_by_mesh_axis_coordinate: _row_intervals_by_mesh_axis_coordinate().
  _AxisComputeSharding: _AxisComputeSharding.
  DistMuon._validate_momentum: DistMuon#_validate_momentum().
  DistMuon._local_gradient_and_momentum: DistMuon#_local_gradient_and_momentum().
  _validate_shard_order_compute_targets: _validate_shard_order_compute_targets().
  _is_supported_orthogonal_dim0_shard_redistribution: _is_supported_orthogonal_dim0_shard_redistribution().
  DistMuon._first_step_validated: DistMuon#_first_step_validated.
  DistMuon._local_tensor_spec: DistMuon#_local_tensor_spec().
  DistMuon._validate_plan_across_ranks: DistMuon#_validate_plan_across_ranks().
  DistMuon._redistribution_runtime: DistMuon#_redistribution_runtime.
  DistMuon._group: DistMuon#_group().
  _ParameterComputeLayout.fqn: _ParameterComputeLayout#fqn.
  DistMuon._prepare_local: DistMuon#_prepare_local().
  _lower_shard_order_to_strided_shards: _lower_shard_order_to_strided_shards().
  _LoweredComputeSharding: _LoweredComputeSharding.
  _MatrixBatchView: _MatrixBatchView#
  _ParameterComputeLayout.compute_sharding: _ParameterComputeLayout#compute_sharding.
  _MatrixBatchView.matrix_batch_shape: _MatrixBatchView#matrix_batch_shape().
  _ParameterComputeLayout.global_compute_shape: _ParameterComputeLayout#global_compute_shape.
  _StorageToComputeTransition: _StorageToComputeTransition.
  DistMuon._bucket_plans: DistMuon#_bucket_plans.
  DistMuon._group_signature: DistMuon#_group_signature().
  DistMuon._momentum: DistMuon#_momentum().
  _PreparedParameterComputeLayout.compute_view: _PreparedParameterComputeLayout#compute_view.
  _ParameterComputeLayout.compute_view: _ParameterComputeLayout#compute_view.
  _ParameterComputeLayout.storage_to_compute_transition: _ParameterComputeLayout#storage_to_compute_transition.
  _ResolvedComputeSharding: _ResolvedComputeSharding.
  _ResolvedStorageToComputeTransition.compute_sharding: _ResolvedStorageToComputeTransition#compute_sharding.
  _ResolvedStorageToComputeTransition.storage_to_compute_transition: _ResolvedStorageToComputeTransition#storage_to_compute_transition.
  DistMuon.__init__: DistMuon#__init__().
  _UnsupportedStoragePlacement: _UnsupportedStoragePlacement#
  DistMuon._prepared_compute_layouts: DistMuon#_prepared_compute_layouts.
  DistMuon._specs: DistMuon#_specs.
  DistMuon._parameter_compute_layouts: DistMuon#_parameter_compute_layouts.
  _PreparedParameterComputeLayout.compute_layout: _PreparedParameterComputeLayout#compute_layout.
  _MatrixBatchView.matrix_rows: _MatrixBatchView#matrix_rows.
  _ParameterComputeLayout.redistribution_storage_mesh_axis: _ParameterComputeLayout#redistribution_storage_mesh_axis.
  _NoRedistributionTransition: _NoRedistributionTransition#
  _validate_compute_sharding_configuration: _validate_compute_sharding_configuration().
  _MatrixBatchView.from_storage_shape: _MatrixBatchView#from_storage_shape().
  _MatrixBatchView.view_as_matrix_batch: _MatrixBatchView#view_as_matrix_batch().
  _compute_muon_direction: _compute_muon_direction().
  _apply_muon_update: _apply_muon_update().
  DistMuon._param_groups_frozen: DistMuon#_param_groups_frozen.
  _ParameterComputeLayout.group_index: _ParameterComputeLayout#group_index.
  _ParameterComputeLayout.storage_mesh_ranks: _ParameterComputeLayout#storage_mesh_ranks.
  _ParameterComputeLayout.storage_layout_signature: _ParameterComputeLayout#storage_layout_signature.
  _RedistributionTransition: _RedistributionTransition#
  _UnsupportedStoragePlacement.type_name: _UnsupportedStoragePlacement#type_name.
  _UnsupportedStoragePlacement.representation: _UnsupportedStoragePlacement#representation.
  _ResolvedStorageToComputeTransition.resolved_compute_layout_signature: _ResolvedStorageToComputeTransition#resolved_compute_layout_signature.
  _ResolvedStorageToComputeTransition: _ResolvedStorageToComputeTransition#
  DistMuon.add_param_group: DistMuon#add_param_group().
  DistMuon.step: DistMuon#step().
  DistMuon._validate_groups: DistMuon#_validate_groups().
  _MatrixBatchView.matrix_columns: _MatrixBatchView#matrix_columns.
  _PreparedParameterComputeLayout.compute_view_key: _PreparedParameterComputeLayout#compute_view_key.
  _PreparedParameterComputeLayout.global_compute_shape: _PreparedParameterComputeLayout#global_compute_shape.
  _ParameterComputeLayout.compute_view_key: _ParameterComputeLayout#compute_view_key.
  _ParameterComputeLayout.local_storage_signature: _ParameterComputeLayout#local_storage_signature.
  _ParameterComputeLayout.resolved_compute_layout_signature: _ParameterComputeLayout#resolved_compute_layout_signature.
  _ResolvedStorageToComputeTransition.redistribution_storage_mesh_axis: _ResolvedStorageToComputeTransition#redistribution_storage_mesh_axis.
  _local_storage_signature: _local_storage_signature().
  _storage_layout_signature: _storage_layout_signature().
  _PreparedParameterComputeLayout: _PreparedParameterComputeLayout#
  _normalize_param_groups: _normalize_param_groups().
  DistMuon._validate_parameter_storage: DistMuon#_validate_parameter_storage().
  _validate_matrix_batch_storage_placements: _validate_matrix_batch_storage_placements().
  _estimate_muon_compute_cost: _estimate_muon_compute_cost().
  _balance_loads_across_partitions: _balance_loads_across_partitions().
  _raise_unsupported_layout: _raise_unsupported_layout().
  _adjust_muon_learning_rate: _adjust_muon_learning_rate().
  _prepare_muon_input: _prepare_muon_input().
  _zeropower_via_newtonschulz: _zeropower_via_newtonschulz().
  __all__: __all__.
---
# Module: [`torchtitan/distributed/flex_shard/dist_muon.py`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py)

## Classes
### <a id="DistMuon"></a>`DistMuon`
- def: [`torchtitan/distributed/flex_shard/dist_muon.py:252`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L252) — documented in [flex-shard](../../../../concepts/flex-shard.md)
- members:
  - <a id="DistMuon._preflight_step"></a>`_preflight_step(self)` — [`L486`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L486) — Fail the local worker before bucket communication on invalid input. — documented in [flex-shard](../../../../concepts/flex-shard.md)
  - <a id="DistMuon.add_param_group"></a>`add_param_group(self, param_group: dict[str, Any])` — [`L332`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L332)
  - <a id="DistMuon.step"></a>`step(self, closure: Callable[[], float] | None = None)` — [`L308`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L308)
- protocol/private: <a id="DistMuon.__init__"></a>`__init__`[`L271`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L271), <a id="DistMuon._apply_update"></a>`_apply_update`[`L624`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L624), <a id="DistMuon._bucket_plans"></a>`_bucket_plans`[`L437`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L437), <a id="DistMuon._build_parameter_compute_layouts"></a>`_build_parameter_compute_layouts`[`L371`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L371), <a id="DistMuon._compute_update"></a>`_compute_update`[`L610`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L610), <a id="DistMuon._first_step_validated"></a>`_first_step_validated`[`L296`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L296), <a id="DistMuon._group"></a>`_group`[`L465`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L465), <a id="DistMuon._group_signature"></a>`_group_signature`[`L468`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L468), <a id="DistMuon._has_storage_layout"></a>`_has_storage_layout`[`L546`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L546), <a id="DistMuon._initialize_plan"></a>`_initialize_plan`[`L421`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L421), <a id="DistMuon._local_gradient_and_momentum"></a>`_local_gradient_and_momentum`[`L579`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L579), <a id="DistMuon._local_tensor_spec"></a>`_local_tensor_spec`[`L642`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L642), <a id="DistMuon._momentum"></a>`_momentum`[`L569`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L569), <a id="DistMuon._param_groups_frozen"></a>`_param_groups_frozen`[`L269`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L269), <a id="DistMuon._parameter_compute_layouts"></a>`_parameter_compute_layouts`[`L438`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L438), <a id="DistMuon._plan_item_signature"></a>`_plan_item_signature`[`L446`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L446), <a id="DistMuon._prepare_local"></a>`_prepare_local`[`L595`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L595), <a id="DistMuon._prepared_compute_layouts"></a>`_prepared_compute_layouts`[`L266`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L266), <a id="DistMuon._redistribution_runtime"></a>`_redistribution_runtime`[`L268`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L268), <a id="DistMuon._specs"></a>`_specs`[`L267`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L267), <a id="DistMuon._validate_groups"></a>`_validate_groups`[`L337`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L337), <a id="DistMuon._validate_momentum"></a>`_validate_momentum`[`L558`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L558), <a id="DistMuon._validate_parameter_storage"></a>`_validate_parameter_storage`[`L359`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L359), <a id="DistMuon._validate_plan_across_ranks"></a>`_validate_plan_across_ranks`[`L440`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L440)
- uses (calls/refs, reference-scoped): [`_build_bucket_plans`](_optimizer_reshard_schedule.md#_build_bucket_plans), [`_initialize_dist_muon`](dist_muon.md#_initialize_dist_muon), [`_resolve_storage_to_compute_transition`](dist_muon.md#_resolve_storage_to_compute_transition), [`run`](_optimizer_reshard_runtime.md#_BucketedRedistributionRuntime.run), [`_resolve_muon_redistribution_plans`](dist_muon.md#_resolve_muon_redistribution_plans), [`_validate_bucket_plans_across_ranks`](_optimizer_reshard_schedule.md#_validate_bucket_plans_across_ranks), [`param`](dist_muon.md#_ParameterComputeLayout.param), [`ComputeLayout`](optimizer_reshard.md#ComputeLayout), [`_ParameterComputeLayout`](dist_muon.md#_ParameterComputeLayout), [`storage_is_compute_ready`](dist_muon.md#_ParameterComputeLayout.storage_is_compute_ready), [`BucketConfig`](optimizer_reshard.md#BucketConfig), [`fqn`](dist_muon.md#_ParameterComputeLayout.fqn), [`_BucketSpec`](optimizer_reshard.md#_BucketSpec), [`compute_sharding`](dist_muon.md#_ParameterComputeLayout.compute_sharding), [`global_compute_shape`](dist_muon.md#_ParameterComputeLayout.global_compute_shape), [`plans`](_optimizer_reshard_schedule.md#_BucketPlanningResult.plans), [`_BucketedRedistributionRuntime`](_optimizer_reshard_runtime.md#_BucketedRedistributionRuntime), [`_device_mesh_ranks`](_optimizer_reshard_schedule.md#_device_mesh_ranks), [`compute_sharding`](dist_muon.md#_ResolvedStorageToComputeTransition.compute_sharding), [`compute_view`](dist_muon.md#_ParameterComputeLayout.compute_view), [`compute_view`](dist_muon.md#_PreparedParameterComputeLayout.compute_view), [`storage_to_compute_transition`](dist_muon.md#_ParameterComputeLayout.storage_to_compute_transition), [`storage_to_compute_transition`](dist_muon.md#_ResolvedStorageToComputeTransition.storage_to_compute_transition), [`compute_layout`](dist_muon.md#_PreparedParameterComputeLayout.compute_layout), [`ordered_items`](_optimizer_reshard_schedule.md#_BucketPlanningResult.ordered_items), [`redistribution_storage_mesh_axis`](dist_muon.md#_ParameterComputeLayout.redistribution_storage_mesh_axis), [`_apply_muon_update`](dist_muon.md#_apply_muon_update), [`_compute_muon_direction`](dist_muon.md#_compute_muon_direction), [`view_as_matrix_batch`](dist_muon.md#_MatrixBatchView.view_as_matrix_batch), [`group_index`](dist_muon.md#_ParameterComputeLayout.group_index), [`resolved_compute_layout_signature`](dist_muon.md#_ResolvedStorageToComputeTransition.resolved_compute_layout_signature), [`storage_layout_signature`](dist_muon.md#_ParameterComputeLayout.storage_layout_signature), [`storage_mesh_ranks`](dist_muon.md#_ParameterComputeLayout.storage_mesh_ranks), [`_PreparedParameterComputeLayout`](dist_muon.md#_PreparedParameterComputeLayout), [`_local_storage_signature`](dist_muon.md#_local_storage_signature), [`_storage_layout_signature`](dist_muon.md#_storage_layout_signature), [`compute_view_key`](dist_muon.md#_ParameterComputeLayout.compute_view_key), [`compute_view_key`](dist_muon.md#_PreparedParameterComputeLayout.compute_view_key), [`global_compute_shape`](dist_muon.md#_PreparedParameterComputeLayout.global_compute_shape), [`local_storage_signature`](dist_muon.md#_ParameterComputeLayout.local_storage_signature)  (+3 more)
- used by: [`_initialize_dist_muon`](dist_muon.md#_initialize_dist_muon), [`_after_load_state_dict`](dist_muon.md#_after_load_state_dict), [`build_dist_muon`](dist_muon.md#build_dist_muon)

### <a id="_MatrixBatchView"></a>`_MatrixBatchView`
- def: [`torchtitan/distributed/flex_shard/dist_muon.py:651`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L651)
- members:
  - <a id="_MatrixBatchView.from_storage_shape"></a>`from_storage_shape(cls, storage_shape: torch.Size, *, matrix_rows: int)` — [`L656`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L656)
  - <a id="_MatrixBatchView.matrix_batch_shape"></a>`matrix_batch_shape(self, compute_tensor_shape: torch.Size)` — [`L676`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L676)
  - <a id="_MatrixBatchView.view_as_matrix_batch"></a>`view_as_matrix_batch(self, compute_tensor: Tensor)` — [`L694`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L694) — Return a zero-copy matrix-batch view of the compute tensor.
  - <a id="_MatrixBatchView.matrix_columns"></a>`matrix_columns` — [`L653`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L653)
  - <a id="_MatrixBatchView.matrix_rows"></a>`matrix_rows` — [`L652`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L652)
- used by: [`_initialize_dist_muon`](dist_muon.md#_initialize_dist_muon), [`_resolve_storage_to_compute_transition`](dist_muon.md#_resolve_storage_to_compute_transition), [`_matrix_batch_view_from_compute_layout`](dist_muon.md#_matrix_batch_view_from_compute_layout), [`_resolve_storage_to_compute_redistribution_requirement`](dist_muon.md#_resolve_storage_to_compute_redistribution_requirement), [`_compute_update`](dist_muon.md#DistMuon._compute_update), [`_is_supported_orthogonal_dim0_shard_redistribution`](dist_muon.md#_is_supported_orthogonal_dim0_shard_redistribution), [`compute_view`](dist_muon.md#_ParameterComputeLayout.compute_view), [`compute_view`](dist_muon.md#_PreparedParameterComputeLayout.compute_view)

### <a id="_NoRedistributionTransition"></a>`_NoRedistributionTransition`
- def: [`torchtitan/distributed/flex_shard/dist_muon.py:910`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L910)
- used by: [`_resolve_storage_to_compute_transition`](dist_muon.md#_resolve_storage_to_compute_transition), [`_build_parameter_redistribution_plan`](dist_muon.md#_build_parameter_redistribution_plan), [`storage_is_compute_ready`](dist_muon.md#_ParameterComputeLayout.storage_is_compute_ready), [`_StorageToComputeTransition`](dist_muon.md#_StorageToComputeTransition)

### <a id="_ParameterComputeLayout"></a>`_ParameterComputeLayout`
- def: [`torchtitan/distributed/flex_shard/dist_muon.py:887`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L887) — documented in [flex-shard](../../../../concepts/flex-shard.md)
- members:
  - <a id="_ParameterComputeLayout.storage_is_compute_ready"></a>`storage_is_compute_ready(self)` — [`L903`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L903)
  - <a id="_ParameterComputeLayout.compute_sharding"></a>`compute_sharding` — [`L897`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L897)
  - <a id="_ParameterComputeLayout.compute_view"></a>`compute_view` — [`L893`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L893)
  - <a id="_ParameterComputeLayout.compute_view_key"></a>`compute_view_key` — [`L891`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L891)
  - <a id="_ParameterComputeLayout.fqn"></a>`fqn` — [`L888`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L888)
  - <a id="_ParameterComputeLayout.global_compute_shape"></a>`global_compute_shape` — [`L892`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L892)
  - <a id="_ParameterComputeLayout.group_index"></a>`group_index` — [`L890`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L890)
  - <a id="_ParameterComputeLayout.local_storage_signature"></a>`local_storage_signature` — [`L896`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L896)
  - <a id="_ParameterComputeLayout.param"></a>`param` — [`L889`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L889) — documented in [flex-shard](../../../../concepts/flex-shard.md)
  - <a id="_ParameterComputeLayout.redistribution_storage_mesh_axis"></a>`redistribution_storage_mesh_axis` — [`L900`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L900)
  - <a id="_ParameterComputeLayout.resolved_compute_layout_signature"></a>`resolved_compute_layout_signature` — [`L899`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L899)
  - <a id="_ParameterComputeLayout.storage_layout_signature"></a>`storage_layout_signature` — [`L895`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L895)
  - <a id="_ParameterComputeLayout.storage_mesh_ranks"></a>`storage_mesh_ranks` — [`L894`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L894)
  - <a id="_ParameterComputeLayout.storage_to_compute_transition"></a>`storage_to_compute_transition` — [`L898`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L898)
- uses (calls/refs, reference-scoped): [`_MatrixBatchView`](dist_muon.md#_MatrixBatchView), [`_StorageToComputeTransition`](dist_muon.md#_StorageToComputeTransition), [`_ResolvedComputeSharding`](dist_muon.md#_ResolvedComputeSharding), [`_NoRedistributionTransition`](dist_muon.md#_NoRedistributionTransition)
- used by: [`_initialize_dist_muon`](dist_muon.md#_initialize_dist_muon), [`_build_parameter_compute_layouts`](dist_muon.md#DistMuon._build_parameter_compute_layouts), [`_build_parameter_redistribution_plan`](dist_muon.md#_build_parameter_redistribution_plan), [`_resolve_muon_redistribution_plans`](dist_muon.md#_resolve_muon_redistribution_plans), [`_plan_item_signature`](dist_muon.md#DistMuon._plan_item_signature), [`_preflight_step`](dist_muon.md#DistMuon._preflight_step), [`_assign_balanced_owner_ranks`](dist_muon.md#_assign_balanced_owner_ranks), [`_initialize_plan`](dist_muon.md#DistMuon._initialize_plan), [`_has_storage_layout`](dist_muon.md#DistMuon._has_storage_layout), [`_apply_update`](dist_muon.md#DistMuon._apply_update), [`_compute_update`](dist_muon.md#DistMuon._compute_update), [`_local_gradient_and_momentum`](dist_muon.md#DistMuon._local_gradient_and_momentum), [`_validate_momentum`](dist_muon.md#DistMuon._validate_momentum), [`_local_tensor_spec`](dist_muon.md#DistMuon._local_tensor_spec), [`_group`](dist_muon.md#DistMuon._group), [`_redistribution_runtime`](dist_muon.md#DistMuon._redistribution_runtime), [`_prepare_local`](dist_muon.md#DistMuon._prepare_local), [`_group_signature`](dist_muon.md#DistMuon._group_signature), [`_momentum`](dist_muon.md#DistMuon._momentum)

### <a id="_PreparedParameterComputeLayout"></a>`_PreparedParameterComputeLayout`
- def: [`torchtitan/distributed/flex_shard/dist_muon.py:879`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L879)
- members:
  - <a id="_PreparedParameterComputeLayout.compute_layout"></a>`compute_layout` — [`L881`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L881)
  - <a id="_PreparedParameterComputeLayout.compute_view"></a>`compute_view` — [`L883`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L883)
  - <a id="_PreparedParameterComputeLayout.compute_view_key"></a>`compute_view_key` — [`L880`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L880)
  - <a id="_PreparedParameterComputeLayout.global_compute_shape"></a>`global_compute_shape` — [`L882`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L882)
- uses (calls/refs, reference-scoped): [`ComputeLayout`](optimizer_reshard.md#ComputeLayout), [`_MatrixBatchView`](dist_muon.md#_MatrixBatchView)
- used by: [`_initialize_dist_muon`](dist_muon.md#_initialize_dist_muon), [`_build_parameter_compute_layouts`](dist_muon.md#DistMuon._build_parameter_compute_layouts), [`_prepared_compute_layouts`](dist_muon.md#DistMuon._prepared_compute_layouts)

### <a id="_RedistributionTransition"></a>`_RedistributionTransition`
- def: [`torchtitan/distributed/flex_shard/dist_muon.py:915`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L915)
- signature: `class _RedistributionTransition:`
- used by: [`_resolve_storage_to_compute_transition`](dist_muon.md#_resolve_storage_to_compute_transition), [`_build_parameter_redistribution_plan`](dist_muon.md#_build_parameter_redistribution_plan), [`_StorageToComputeTransition`](dist_muon.md#_StorageToComputeTransition)

### <a id="_ResolvedStorageToComputeTransition"></a>`_ResolvedStorageToComputeTransition`
- def: [`torchtitan/distributed/flex_shard/dist_muon.py:947`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L947)
- members:
  - <a id="_ResolvedStorageToComputeTransition.compute_sharding"></a>`compute_sharding` — [`L948`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L948)
  - <a id="_ResolvedStorageToComputeTransition.redistribution_storage_mesh_axis"></a>`redistribution_storage_mesh_axis` — [`L951`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L951)
  - <a id="_ResolvedStorageToComputeTransition.resolved_compute_layout_signature"></a>`resolved_compute_layout_signature` — [`L950`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L950)
  - <a id="_ResolvedStorageToComputeTransition.storage_to_compute_transition"></a>`storage_to_compute_transition` — [`L949`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L949)
- uses (calls/refs, reference-scoped): [`_StorageToComputeTransition`](dist_muon.md#_StorageToComputeTransition), [`_ResolvedComputeSharding`](dist_muon.md#_ResolvedComputeSharding)
- used by: [`_build_parameter_compute_layouts`](dist_muon.md#DistMuon._build_parameter_compute_layouts), [`_resolve_storage_to_compute_transition`](dist_muon.md#_resolve_storage_to_compute_transition)

### <a id="_UnsupportedStoragePlacement"></a>`_UnsupportedStoragePlacement`
- def: [`torchtitan/distributed/flex_shard/dist_muon.py:941`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L941)
- members:
  - <a id="_UnsupportedStoragePlacement.representation"></a>`representation` — [`L943`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L943)
  - <a id="_UnsupportedStoragePlacement.type_name"></a>`type_name` — [`L942`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L942)
- used by: [`_resolve_storage_to_compute_transition`](dist_muon.md#_resolve_storage_to_compute_transition), [`_resolve_storage_to_compute_redistribution_requirement`](dist_muon.md#_resolve_storage_to_compute_redistribution_requirement), [`_normalize_storage_placement`](dist_muon.md#_normalize_storage_placement)

## Functions
- <a id="_adjust_muon_learning_rate"></a>`_adjust_muon_learning_rate(lr: float, adjust_lr_fn: str | None, compute_matrix_shape: torch.Size | tuple[int, ...])` — [`L1824`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L1824) — Adjust Muon's learning rate for the matrix aspect ratio.
- <a id="_after_load_state_dict"></a>`_after_load_state_dict(optimizer: Optimizer)` — [`L1937`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L1937) — documented in [flex-shard](../../../../concepts/flex-shard.md)
- <a id="_apply_muon_update"></a>`_apply_muon_update(parameter: Tensor, direction: Tensor, *, lr: float, weight_decay: float, adjust_lr_fn: str | None, compute_matrix_shape: torch.Size | tuple[int, ...])` — [`L1883`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L1883) — Apply decoupled weight decay and a computed Muon direction.
- <a id="_assign_balanced_owner_ranks"></a>`_assign_balanced_owner_ranks(compute_layouts: Sequence[_ParameterComputeLayout], *, participants: tuple[int, ...], cumulative_loads: Sequence[int], ns_steps_by_group: Sequence[int])` — [`L1006`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L1006) — Balance temporary compute ownership within and across ordered buckets. — documented in [flex-shard](../../../../concepts/flex-shard.md)
- <a id="_balance_loads_across_partitions"></a>`_balance_loads_across_partitions(loads: Sequence[tuple[int, int, str]], *, initial_cumulative_primary_loads: Sequence[int])` — [`L1053`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L1053) — Balance keyed loads with a deterministic LPT heuristic.
- <a id="_build_batched_matrix_redistribution_plan"></a>`_build_batched_matrix_redistribution_plan(storage_regions: Sequence[_StorageRegionMapping], *, participants: tuple[int, ...], storage_shape: tuple[int, ...], compute_shape: tuple[int, ...])` — [`L1148`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L1148) — Build flat 2D routes whose destination shards contain complete matrices. — documented in [flex-shard](../../../../concepts/flex-shard.md)
- <a id="_build_parameter_redistribution_plan"></a>`_build_parameter_redistribution_plan(compute_layout: _ParameterComputeLayout, group: _RedistributionGroup, owner_rank: int | None)` — [`L1104`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L1104) — documented in [flex-shard](../../../../concepts/flex-shard.md)
- <a id="_compute_muon_direction"></a>`_compute_muon_direction(prepared: Tensor, *, ns_coefficients: tuple[float, float, float], ns_steps: int, eps: float, out: Tensor)` — [`L1864`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L1864) — Compute Muon's approximate orthogonal update direction.
- <a id="_estimate_muon_compute_cost"></a>`_estimate_muon_compute_cost(matrix_shape: torch.Size, ns_steps: int)` — [`L1043`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L1043)
- <a id="_initialize_dist_muon"></a>`_initialize_dist_muon(optimizer: DistMuon, *, compute_sharding_by_fqn: Mapping[str, ComputeLayout], bucket_configs: Sequence[BucketConfig])` — [`L170`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L170) — Initialize FlexShard for one newly constructed DistMuon. — documented in [flex-shard](../../../../concepts/flex-shard.md)
- <a id="_is_supported_orthogonal_dim0_shard_redistribution"></a>`_is_supported_orthogonal_dim0_shard_redistribution(*, ndim: int, compute_view: _MatrixBatchView | None, source_storage_placement: object, target_compute_sharding: _AxisComputeSharding | None, preserved_storage_placement: object)` — [`L1388`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L1388) — documented in [flex-shard](../../../../concepts/flex-shard.md)
- <a id="_local_storage_signature"></a>`_local_storage_signature(tensor: Tensor)` — [`L1952`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L1952)
- <a id="_lower_shard_order_to_strided_shards"></a>`_lower_shard_order_to_strided_shards(param: DTensor, compute_layout: ComputeLayout, storage_axis_by_name: Mapping[str, int], shardings_by_storage_mesh_axis: Mapping[int, _LoweredComputeSharding])` — [`L1291`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L1291) — Encode a declared shard order as DTensor placements. — documented in [flex-shard](../../../../concepts/flex-shard.md)
- <a id="_matrix_batch_view_from_compute_layout"></a>`_matrix_batch_view_from_compute_layout(fqn: str, param: Tensor, compute_layout: ComputeLayout)` — [`L121`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L121) — documented in [flex-shard](../../../../concepts/flex-shard.md)
- <a id="_normalize_compute_placement"></a>`_normalize_compute_placement(placement: _AxisComputeSharding, *, ndim: int, mesh_axis_size: int)` — [`L1763`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L1763)
- <a id="_normalize_dim"></a>`_normalize_dim(dim: int, ndim: int)` — [`L1817`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L1817)
- <a id="_normalize_param_groups"></a>`_normalize_param_groups(params: Iterable[dict[str, Any]])` — [`L84`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L84) — Copy parameter groups and materialize their aligned values.
- <a id="_normalize_storage_placement"></a>`_normalize_storage_placement(placement: object, *, ndim: int, mesh_axis_size: int)` — [`L1793`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L1793)
- <a id="_prepare_muon_input"></a>`_prepare_muon_input(gradient: Tensor, momentum_buffer: Tensor, *, momentum: float, nesterov: bool, out: Tensor)` — [`L1842`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L1842) — Update momentum and prepare the Tensor passed to Muon computation.
- <a id="_raise_unsupported_layout"></a>`_raise_unsupported_layout(fqn: str)` — [`L1759`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L1759)
- <a id="_resolve_muon_redistribution_plans"></a>`_resolve_muon_redistribution_plans(contexts: tuple[_BucketPlanningContext[_ParameterComputeLayout], ...], *, ns_steps_by_group: Sequence[int])` — [`L954`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L954) — Resolve Muon compute shardings directly into transport plans. — documented in [flex-shard](../../../../concepts/flex-shard.md)
- <a id="_resolve_storage_to_compute_redistribution_requirement"></a>`_resolve_storage_to_compute_redistribution_requirement(fqn: str, param: DTensor, compute_view: _MatrixBatchView | None, target_sharding_by_storage_mesh_axis: Mapping[int, _AxisComputeSharding], declared_storage_mesh_axes: Sequence[int])` — [`L761`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L761) — Compare actual storage with the target compute tensor. — documented in [flex-shard](../../../../concepts/flex-shard.md)
- <a id="_resolve_storage_to_compute_transition"></a>`_resolve_storage_to_compute_transition(fqn: str, param: DTensor, global_compute_shape: torch.Size, compute_view: _MatrixBatchView | None, compute_layout: ComputeLayout)` — [`L1411`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L1411) — Validate one storage layout and resolve its concrete compute transition. — documented in [flex-shard](../../../../concepts/flex-shard.md)
- <a id="_row_intervals_by_mesh_axis_coordinate"></a>`_row_intervals_by_mesh_axis_coordinate(num_rows: int, sharding: _AxisComputeSharding, *, mesh_axis_size: int)` — [`L724`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L724) — Resolve the global rows owned by each mesh-axis coordinate. — documented in [flex-shard](../../../../concepts/flex-shard.md)
- <a id="_storage_layout_signature"></a>`_storage_layout_signature(tensor: DTensor)` — [`L1963`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L1963)
- <a id="_validate_compute_sharding_configuration"></a>`_validate_compute_sharding_configuration(compute_sharding_by_fqn: Mapping[str, ComputeLayout])` — [`L110`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L110) — Validate per-parameter compute sharding configuration.
- <a id="_validate_matrix_batch_storage_placements"></a>`_validate_matrix_batch_storage_placements(fqn: str, param: DTensor)` — [`L700`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L700) — Validate placements supported by matrix-batch storage.
- <a id="_validate_shard_order_compute_targets"></a>`_validate_shard_order_compute_targets(fqn: str, param: DTensor, target_sharding_by_storage_mesh_axis: Mapping[int, _AxisComputeSharding], owned_storage_mesh_axes: Sequence[int])` — [`L1326`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L1326) — Reject declared shard orders that DistMuon cannot lower to a transport plan. — documented in [flex-shard](../../../../concepts/flex-shard.md)
- <a id="_zeropower_via_newtonschulz"></a>`_zeropower_via_newtonschulz(update: Tensor, *, ns_coefficients: tuple[float, float, float], ns_steps: int, eps: float)` — [`L1903`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L1903) — Compute Muon's approximate polar factor without optimizer state.
- <a id="build_dist_muon"></a>`build_dist_muon(params: Iterable[dict[str, Any]], *, compute_sharding_by_fqn: Mapping[str, ComputeLayout], bucket_configs: Sequence[BucketConfig], **kwargs: Any)` — [`L58`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L58) — Construct a DistMuon optimizer with FlexShard redistribution. — documented in [flex-shard](../../../../concepts/flex-shard.md)

## Module values
- <a id="_AxisComputeSharding"></a>`_AxisComputeSharding` — [`L933`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L933) — documented in [flex-shard](../../../../concepts/flex-shard.md)
- <a id="_LoweredComputeSharding"></a>`_LoweredComputeSharding` — [`L929`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L929) — documented in [flex-shard](../../../../concepts/flex-shard.md)
- <a id="_ResolvedComputeSharding"></a>`_ResolvedComputeSharding` — [`L937`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L937)
- <a id="_StorageToComputeTransition"></a>`_StorageToComputeTransition` — [`L919`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L919)
- <a id="__all__"></a>`__all__` — [`L53`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/dist_muon.py#L53)

