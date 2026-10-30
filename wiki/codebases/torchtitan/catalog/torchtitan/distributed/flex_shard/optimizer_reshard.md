---
title: 'Module: torchtitan/distributed/flex_shard/optimizer_reshard.py'
type: catalog
provenance: extracted
module: torchtitan/distributed/flex_shard/optimizer_reshard.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.distributed.flex_shard.optimizer_reshard`/
symbols:
  ComputeLayout: ComputeLayout#
  BlockShard: BlockShard#
  BlockShard.dim: BlockShard#dim.
  BucketConfig._bind: BucketConfig#_bind().
  Owned: Owned#
  ComputeLayout.__post_init__: ComputeLayout#__post_init__().
  _FrozenConfigMapping: _FrozenConfigMapping#
  ComputeLayout.shardings_by_mesh_axis: ComputeLayout#shardings_by_mesh_axis.
  BlockShard.block_size: BlockShard#block_size.
  BucketConfig: BucketConfig#
  ComputeLayout._validated_shard_order: ComputeLayout#_validated_shard_order().
  _ComputeSharding: _ComputeSharding.
  _BucketSpec: _BucketSpec#
  _FrozenConfigMapping.__init__: _FrozenConfigMapping#__init__().
  _FrozenConfigMapping.__getitem__: _FrozenConfigMapping#__getitem__().
  _FrozenConfigMapping.__deepcopy__: _FrozenConfigMapping#__deepcopy__().
  _ShardingsByMeshAxis: _ShardingsByMeshAxis.
  ComputeLayout.shard_order_by_tensor_dim: ComputeLayout#shard_order_by_tensor_dim.
  BlockShard.__post_init__: BlockShard#__post_init__().
  _KeyT: _KeyT.
  _FrozenConfigMapping.__iter__: _FrozenConfigMapping#__iter__().
  BucketConfig.patterns: BucketConfig#patterns.
  _BucketSpec.__post_init__: _BucketSpec#__post_init__().
  _ShardOrderByTensorDim: _ShardOrderByTensorDim.
  _ValueT: _ValueT.
  BucketConfig.name: BucketConfig#name.
  _DEFAULT_SHARD_ORDER: _DEFAULT_SHARD_ORDER.
  _BucketSpec.patterns: _BucketSpec#patterns.
  _BucketSpec.mesh: _BucketSpec#mesh.
  _FrozenConfigMapping.__len__: _FrozenConfigMapping#__len__().
  _FrozenConfigMapping.__hash__: _FrozenConfigMapping#__hash__().
  _FrozenConfigMapping.__repr__: _FrozenConfigMapping#__repr__().
  BucketConfig.__post_init__: BucketConfig#__post_init__().
  _BucketSpec.name: _BucketSpec#name.
  __all__: __all__.
  _FrozenConfigMapping.__slots__: _FrozenConfigMapping#__slots__.
  ComputeLayout.to_dict: ComputeLayout#to_dict().
---
# Module: [`torchtitan/distributed/flex_shard/optimizer_reshard.py`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/optimizer_reshard.py)

## Classes
### <a id="BlockShard"></a>`BlockShard`
- def: [`torchtitan/distributed/flex_shard/optimizer_reshard.py:35`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/optimizer_reshard.py#L35) — documented in [flex-shard](../../../../concepts/flex-shard.md)
- doc: Shard fixed-size blocks without changing the tensor shape.
- signature: `class BlockShard:`
- members:
  - <a id="BlockShard.block_size"></a>`block_size` — [`L46`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/optimizer_reshard.py#L46) — documented in [flex-shard](../../../../concepts/flex-shard.md)
  - <a id="BlockShard.dim"></a>`dim` — [`L45`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/optimizer_reshard.py#L45) — documented in [flex-shard](../../../../concepts/flex-shard.md)
- protocol/private: <a id="BlockShard.__post_init__"></a>`__post_init__`[`L48`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/optimizer_reshard.py#L48)
- used by: [`_dist_muon_optimizer`](../../models/kimi_k2_7/config_registry.md#_dist_muon_optimizer), [`_resolve_storage_to_compute_transition`](dist_muon.md#_resolve_storage_to_compute_transition), [`_matrix_batch_view_from_compute_layout`](dist_muon.md#_matrix_batch_view_from_compute_layout), [`_resolve_storage_to_compute_redistribution_requirement`](dist_muon.md#_resolve_storage_to_compute_redistribution_requirement), [`__post_init__`](optimizer_reshard.md#ComputeLayout.__post_init__), [`_normalize_compute_placement`](dist_muon.md#_normalize_compute_placement), [`_row_intervals_by_mesh_axis_coordinate`](dist_muon.md#_row_intervals_by_mesh_axis_coordinate), [`_AxisComputeSharding`](dist_muon.md#_AxisComputeSharding), [`_is_supported_orthogonal_dim0_shard_redistribution`](dist_muon.md#_is_supported_orthogonal_dim0_shard_redistribution), [`_validate_shard_order_compute_targets`](dist_muon.md#_validate_shard_order_compute_targets), [`_validated_shard_order`](optimizer_reshard.md#ComputeLayout._validated_shard_order), [`_ComputeSharding`](optimizer_reshard.md#_ComputeSharding), [`_LoweredComputeSharding`](dist_muon.md#_LoweredComputeSharding)

### <a id="BucketConfig"></a>`BucketConfig`
- def: [`torchtitan/distributed/flex_shard/optimizer_reshard.py:252`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/optimizer_reshard.py#L252) — documented in [flex-shard](../../../../concepts/flex-shard.md)
- doc: Ordered optimizer-work bucket selected by canonical FQN patterns.
- signature: `class BucketConfig:`
- members:
  - <a id="BucketConfig.name"></a>`name` — [`L261`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/optimizer_reshard.py#L261)
  - <a id="BucketConfig.patterns"></a>`patterns` — [`L260`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/optimizer_reshard.py#L260)
- protocol/private: <a id="BucketConfig.__post_init__"></a>`__post_init__`[`L263`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/optimizer_reshard.py#L263), <a id="BucketConfig._bind"></a>`_bind`[`L266`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/optimizer_reshard.py#L266)
- uses (calls/refs, reference-scoped): [`_BucketSpec`](optimizer_reshard.md#_BucketSpec), [`mesh`](optimizer_reshard.md#_BucketSpec.mesh), [`patterns`](optimizer_reshard.md#_BucketSpec.patterns), [`name`](optimizer_reshard.md#_BucketSpec.name)
- used by: [`_dist_muon_optimizer`](../../models/kimi_k2_7/config_registry.md#_dist_muon_optimizer), [`_initialize_dist_muon`](dist_muon.md#_initialize_dist_muon), [`_bind_bucket_configs`](_optimizer_reshard_schedule.md#_bind_bucket_configs), [`build_dist_muon`](dist_muon.md#build_dist_muon), [`__init__`](dist_muon.md#DistMuon.__init__)

### <a id="ComputeLayout"></a>`ComputeLayout`
- def: [`torchtitan/distributed/flex_shard/optimizer_reshard.py:111`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/optimizer_reshard.py#L111) — documented in [flex-shard](../../../../concepts/flex-shard.md)
- doc: Describe temporary compute shardings on named storage-mesh axes.
- signature: `class ComputeLayout:`
- members:
  - <a id="ComputeLayout.to_dict"></a>`to_dict(self)` — [`L246`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/optimizer_reshard.py#L246) — Serialize for JSON logging.
  - <a id="ComputeLayout.shard_order_by_tensor_dim"></a>`shard_order_by_tensor_dim` — [`L166`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/optimizer_reshard.py#L166)
  - <a id="ComputeLayout.shardings_by_mesh_axis"></a>`shardings_by_mesh_axis` — [`L165`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/optimizer_reshard.py#L165) — documented in [flex-shard](../../../../concepts/flex-shard.md)
- protocol/private: <a id="ComputeLayout.__post_init__"></a>`__post_init__`[`L168`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/optimizer_reshard.py#L168), <a id="ComputeLayout._validated_shard_order"></a>`_validated_shard_order`[`L196`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/optimizer_reshard.py#L196)
- uses (calls/refs, reference-scoped): [`BlockShard`](optimizer_reshard.md#BlockShard), [`dim`](optimizer_reshard.md#BlockShard.dim), [`Owned`](optimizer_reshard.md#Owned), [`_ComputeSharding`](optimizer_reshard.md#_ComputeSharding), [`_ShardingsByMeshAxis`](optimizer_reshard.md#_ShardingsByMeshAxis), [`_ShardOrderByTensorDim`](optimizer_reshard.md#_ShardOrderByTensorDim), [`_DEFAULT_SHARD_ORDER`](optimizer_reshard.md#_DEFAULT_SHARD_ORDER)
- used by: [`_dist_muon_optimizer`](../../models/kimi_k2_7/config_registry.md#_dist_muon_optimizer), [`_initialize_dist_muon`](dist_muon.md#_initialize_dist_muon), [`_resolve_storage_to_compute_transition`](dist_muon.md#_resolve_storage_to_compute_transition), [`_per_expert_compute_layout`](../../models/kimi_k2_7/config_registry.md#_per_expert_compute_layout), [`_matrix_batch_view_from_compute_layout`](dist_muon.md#_matrix_batch_view_from_compute_layout), [`_align_dist_muon_expert_compute_layouts`](../../models/kimi_k2_7/config_registry.md#_align_dist_muon_expert_compute_layouts), [`build_dist_muon`](dist_muon.md#build_dist_muon), [`_lower_shard_order_to_strided_shards`](dist_muon.md#_lower_shard_order_to_strided_shards), [`__init__`](dist_muon.md#DistMuon.__init__), [`compute_layout`](dist_muon.md#_PreparedParameterComputeLayout.compute_layout), [`_validate_compute_sharding_configuration`](dist_muon.md#_validate_compute_sharding_configuration), [`compute_shardings_for_layer`](../../models/kimi_k2_7/config_registry.md#_dist_muon_optimizer.compute_shardings_for_layer)

### <a id="Owned"></a>`Owned`
- def: [`torchtitan/distributed/flex_shard/optimizer_reshard.py:22`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/optimizer_reshard.py#L22) — documented in [flex-shard](../../../../concepts/flex-shard.md)
- doc: Assign the complete subgroup-local logical tensor to one owner rank.
- signature: `class Owned:`
- used by: [`_dist_muon_optimizer`](../../models/kimi_k2_7/config_registry.md#_dist_muon_optimizer), [`_resolve_storage_to_compute_transition`](dist_muon.md#_resolve_storage_to_compute_transition), [`_build_parameter_redistribution_plan`](dist_muon.md#_build_parameter_redistribution_plan), [`_assign_balanced_owner_ranks`](dist_muon.md#_assign_balanced_owner_ranks), [`__post_init__`](optimizer_reshard.md#ComputeLayout.__post_init__), [`_ComputeSharding`](optimizer_reshard.md#_ComputeSharding), [`_LoweredComputeSharding`](dist_muon.md#_LoweredComputeSharding), [`_ResolvedComputeSharding`](dist_muon.md#_ResolvedComputeSharding)

### <a id="_BucketSpec"></a>`_BucketSpec`
- def: [`torchtitan/distributed/flex_shard/optimizer_reshard.py:275`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/optimizer_reshard.py#L275)
- members:
  - <a id="_BucketSpec.mesh"></a>`mesh` — [`L286`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/optimizer_reshard.py#L286)
  - <a id="_BucketSpec.name"></a>`name` — [`L287`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/optimizer_reshard.py#L287)
  - <a id="_BucketSpec.patterns"></a>`patterns` — [`L285`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/optimizer_reshard.py#L285)
- protocol/private: <a id="_BucketSpec.__post_init__"></a>`__post_init__`[`L289`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/optimizer_reshard.py#L289)
- used by: [`_build_bucket_plans`](_optimizer_reshard_schedule.md#_build_bucket_plans), [`_bind`](optimizer_reshard.md#BucketConfig._bind), [`_bind_bucket_configs`](_optimizer_reshard_schedule.md#_bind_bucket_configs), [`_resolve_buckets`](_optimizer_reshard_schedule.md#_resolve_buckets), [`_specs`](dist_muon.md#DistMuon._specs)

### <a id="_FrozenConfigMapping"></a>`_FrozenConfigMapping`  ·  implements/extends Mapping
- def: [`torchtitan/distributed/flex_shard/optimizer_reshard.py:65`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/optimizer_reshard.py#L65)
- doc: Small immutable mapping that remains safe to copy with configs.
- signature: `class _FrozenConfigMapping(Mapping[_KeyT, _ValueT]):`
- protocol/private: <a id="_FrozenConfigMapping.__deepcopy__"></a>`__deepcopy__`[`L98`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/optimizer_reshard.py#L98), <a id="_FrozenConfigMapping.__getitem__"></a>`__getitem__`[`L80`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/optimizer_reshard.py#L80), <a id="_FrozenConfigMapping.__hash__"></a>`__hash__`[`L92`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/optimizer_reshard.py#L92), <a id="_FrozenConfigMapping.__init__"></a>`__init__`[`L77`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/optimizer_reshard.py#L77), <a id="_FrozenConfigMapping.__iter__"></a>`__iter__`[`L86`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/optimizer_reshard.py#L86), <a id="_FrozenConfigMapping.__len__"></a>`__len__`[`L89`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/optimizer_reshard.py#L89), <a id="_FrozenConfigMapping.__repr__"></a>`__repr__`[`L95`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/optimizer_reshard.py#L95), <a id="_FrozenConfigMapping.__slots__"></a>`__slots__`[`L75`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/optimizer_reshard.py#L75)
- uses (calls/refs, reference-scoped): [`_KeyT`](optimizer_reshard.md#_KeyT), [`_ValueT`](optimizer_reshard.md#_ValueT)
- used by: [`_ShardingsByMeshAxis`](optimizer_reshard.md#_ShardingsByMeshAxis), [`_ShardOrderByTensorDim`](optimizer_reshard.md#_ShardOrderByTensorDim)

## Module values
- <a id="_ComputeSharding"></a>`_ComputeSharding` — [`L59`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/optimizer_reshard.py#L59)
- <a id="_DEFAULT_SHARD_ORDER"></a>`_DEFAULT_SHARD_ORDER` — [`L107`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/optimizer_reshard.py#L107)
- <a id="_KeyT"></a>`_KeyT` — [`L61`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/optimizer_reshard.py#L61)
- <a id="_ShardOrderByTensorDim"></a>`_ShardOrderByTensorDim` — [`L105`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/optimizer_reshard.py#L105)
- <a id="_ShardingsByMeshAxis"></a>`_ShardingsByMeshAxis` — [`L104`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/optimizer_reshard.py#L104)
- <a id="_ValueT"></a>`_ValueT` — [`L62`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/optimizer_reshard.py#L62)
- <a id="__all__"></a>`__all__` — [`L18`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/flex_shard/optimizer_reshard.py#L18)

