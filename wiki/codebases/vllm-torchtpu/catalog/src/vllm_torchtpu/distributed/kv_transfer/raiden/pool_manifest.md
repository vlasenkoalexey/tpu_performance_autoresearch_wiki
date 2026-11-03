---
title: 'Module: src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.distributed.kv_transfer.raiden.pool_manifest`/
symbols:
  build_qwen35_pool_manifest: build_qwen35_pool_manifest().
  ManifestError: ManifestError#
  build_glm_mla_pool_manifest: build_glm_mla_pool_manifest().
  build_dsv4_pool_manifest: build_dsv4_pool_manifest().
  _pooled_gdn_state_views: _pooled_gdn_state_views().
  build_kimi_k3_pool_manifest: build_kimi_k3_pool_manifest().
  _bind_pool_manifest: _bind_pool_manifest().
  _gdn_conv_regions: _gdn_conv_regions().
  _block_major_fa_view: _block_major_fa_view().
  _dsv4_classify: _dsv4_classify().
  PoolManifest.pools: PoolManifest#pools.
  gdn_state_unit_bytes: gdn_state_unit_bytes().
  PoolEntry.tag: PoolEntry#tag.
  PoolManifest: PoolManifest#
  PoolManifest.geometry_by_tag: PoolManifest#geometry_by_tag().
  _region_placement: _region_placement().
  _pooled_kda_regions: _pooled_kda_regions().
  RegionSpec: RegionSpec#
  PoolEntry.to_pool_dict: PoolEntry#to_pool_dict().
  _fa_regions: _fa_regions().
  _gdn_ssm_regions: _gdn_ssm_regions().
  _glm_row_region: _glm_row_region().
  PoolEntry.regions: PoolEntry#regions.
  _dsv4_row_region: _dsv4_row_region().
  verify_storage_binding: verify_storage_binding().
  PoolManifest.storages: PoolManifest#storages.
  _DSV4_STATE_TAG_BY_KV_TAG: _DSV4_STATE_TAG_BY_KV_TAG.
  _dsv4_kv_tag: _dsv4_kv_tag().
  _dsv4_check_role_rows: _dsv4_check_role_rows().
  RegionSpec.extent_end_bytes: RegionSpec#extent_end_bytes().
  RegionSpec.name: RegionSpec#name.
  RegionSpec.unit_bytes: RegionSpec#unit_bytes.
  RegionSpec.num_units: RegionSpec#num_units.
  GdnHeadGeometry.conv_dim: GdnHeadGeometry#conv_dim().
  _binding_for: _binding_for().
  _StorageTable.index_for: _StorageTable#index_for().
  RegionSpec.units_per_stride: RegionSpec#units_per_stride.
  PoolEntry: PoolEntry#
  PoolEntry.layer_name: PoolEntry#layer_name.
  PoolManifest.pools_of_class: PoolManifest#pools_of_class().
  RegionSpec.offset_bytes: RegionSpec#offset_bytes.
  RegionSpec.stride_bytes: RegionSpec#stride_bytes.
  PoolEntry.num_blocks: PoolEntry#num_blocks.
  PoolManifest.binding: PoolManifest#binding.
  _element_size: _element_size().
  PoolEntry.storage_index: PoolEntry#storage_index.
  RegionSpec.live_bytes: RegionSpec#live_bytes().
  _GLM_REGION_NAMES: _GLM_REGION_NAMES.
  PoolManifest.tag_counts: PoolManifest#tag_counts().
  _nbytes: _nbytes().
  materialize_storages: materialize_storages().
  _storage_offset_bytes: _storage_offset_bytes().
  PoolEntry.block_stride_bytes: PoolEntry#block_stride_bytes.
  PoolEntry.live_bytes_per_block: PoolEntry#live_bytes_per_block().
  _dtype_tag: _dtype_tag().
  _ordered_layers: _ordered_layers().
  Dsv4LayerEntry: Dsv4LayerEntry#
  _group_spec_for_layer: _group_spec_for_layer().
  PoolEntry.base_offset_bytes: PoolEntry#base_offset_bytes.
  PoolEntry.dtype_tag: PoolEntry#dtype_tag.
  PoolManifest.pool_dicts: PoolManifest#pool_dicts().
  _storage_ptr: _storage_ptr().
  _RegionPlacement.region_bytes: _RegionPlacement#region_bytes.
  GdnHeadGeometry: GdnHeadGeometry#
  GdnHeadGeometry.local_key_heads: GdnHeadGeometry#local_key_heads.
  FaLayoutHook.regions: FaLayoutHook#regions().
  dsv4_compressed_kv_layer_name: dsv4_compressed_kv_layer_name().
  _raw_index_for: _raw_index_for().
  FaLayoutHook: FaLayoutHook#
  _pool_layer_index: _pool_layer_index().
  BINDING_PRIVATE_TYPED: BINDING_PRIVATE_TYPED.
  PoolManifest.dtype_tags: PoolManifest#dtype_tags().
  GdnHeadGeometry.local_value_heads: GdnHeadGeometry#local_value_heads.
  GdnHeadGeometry.key_head_dim: GdnHeadGeometry#key_head_dim.
  GdnHeadGeometry.value_head_dim: GdnHeadGeometry#value_head_dim.
  _StorageTable.storages: _StorageTable#storages.
  DSV4_STATE_CACHE_SUFFIX: DSV4_STATE_CACHE_SUFFIX.
  _state_tag_suffix: _state_tag_suffix().
  _dsv4_layer_spec: _dsv4_layer_spec().
  _dsv4_spec_field: _dsv4_spec_field().
  DeadStorageError: DeadStorageError#
  _PooledView: _PooledView#
  _RegionPlacement: _RegionPlacement#
  _RegionPlacement.num_blocks: _RegionPlacement#num_blocks.
  GdnHeadGeometry.conv_kernel_size: GdnHeadGeometry#conv_kernel_size.
  FaLayoutHook.total_tokens: FaLayoutHook#total_tokens().
  _dsv4_num_states: _dsv4_num_states().
  BINDING_ALIASED_RAW: BINDING_ALIASED_RAW.
  _PooledView.pool: _PooledView#pool.
  _PooledView.itemsize: _PooledView#itemsize.
  _PooledView.storage_offset_elems: _PooledView#storage_offset_elems.
  _RegionPlacement.region_offset_bytes: _RegionPlacement#region_offset_bytes.
  layer_index_from_name: layer_index_from_name().
  _StorageTable: _StorageTable#
  _PooledView.element_size: _PooledView#element_size().
  _PooledView.untyped_storage: _PooledView#untyped_storage().
  _PooledView.storage_offset: _PooledView#storage_offset().
  _PooledView.shape: _PooledView#shape.
  _PooledView.dtype: _PooledView#dtype.
  _PooledView.nbytes: _PooledView#nbytes.
  _StorageTable._index_by_ptr: _StorageTable#_index_by_ptr.
  DSV4_CSA_COMPRESS_RATIO: DSV4_CSA_COMPRESS_RATIO.
  RegionSpec.to_dict: RegionSpec#to_dict().
  _KIMI_POOL_DTYPE_TAGS: _KIMI_POOL_DTYPE_TAGS.
  DSV4_INDEXER_CACHE_SUFFIX: DSV4_INDEXER_CACHE_SUFFIX.
  DSV4_IDX_SAL_ROWS: DSV4_IDX_SAL_ROWS.
  Dsv4LayerEntry.layer_name: Dsv4LayerEntry#layer_name.
  Dsv4LayerEntry.array: Dsv4LayerEntry#array.
  _StorageTable.__init__: _StorageTable#__init__().
  FaLayoutHook.name: FaLayoutHook#name.
  Dsv4LayerEntry.tag_base: Dsv4LayerEntry#tag_base.
  Dsv4LayerEntry.group_index: Dsv4LayerEntry#group_index.
---
# Module: [`src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py)

## Classes
### <a id="DeadStorageError"></a>`DeadStorageError`  ·  implements/extends RuntimeError
- def: [`src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py:91`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L91)
- doc: Pools reference storage the model kernels never read or write.
- signature: `class DeadStorageError(RuntimeError):`
- used by: [`verify_storage_binding`](pool_manifest.md#verify_storage_binding)

### <a id="Dsv4LayerEntry"></a>`Dsv4LayerEntry`  ·  implements/extends NamedTuple
- def: [`src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py:1517`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L1517)
- doc: One layer's claim on one array, which is what a pool is built from.
- signature: `class Dsv4LayerEntry(NamedTuple):`
- members:
  - <a id="Dsv4LayerEntry.array"></a>`array` — [`L1531`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L1531)
  - <a id="Dsv4LayerEntry.group_index"></a>`group_index` — [`L1530`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L1530)
  - <a id="Dsv4LayerEntry.layer_name"></a>`layer_name` — [`L1529`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L1529)
  - <a id="Dsv4LayerEntry.tag_base"></a>`tag_base` — [`L1528`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L1528)
- used by: [`build_dsv4_pool_manifest`](pool_manifest.md#build_dsv4_pool_manifest), [`_dsv4_classify`](pool_manifest.md#_dsv4_classify)

### <a id="FaLayoutHook"></a>`FaLayoutHook`
- def: [`src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py:757`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L757)
- doc: How the FA cache tensor's shape maps to tokens and live regions.
- signature: `class FaLayoutHook:`
- members:
  - <a id="FaLayoutHook.regions"></a>`regions(self, *, block_size_tokens: int, shape: Sequence[int], nbytes: int, num_kv_heads: int, head_size: int, itemsize: int)` — [`L772`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L772)
  - <a id="FaLayoutHook.total_tokens"></a>`total_tokens(self, shape: Sequence[int])` — [`L769`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L769)
  - <a id="FaLayoutHook.name"></a>`name` — [`L767`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L767)
- uses (calls/refs, reference-scoped): [`RegionSpec`](pool_manifest.md#RegionSpec), [`regions`](seq_on_lane.md#SolFaLayout.regions), [`total_tokens`](seq_on_lane.md#SolFaLayout.total_tokens), [`SolFaLayout`](seq_on_lane.md#SolFaLayout)
- used by: [`build_qwen35_pool_manifest`](pool_manifest.md#build_qwen35_pool_manifest), [`SolFaLayout`](seq_on_lane.md#SolFaLayout)

### <a id="GdnHeadGeometry"></a>`GdnHeadGeometry`
- def: [`src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py:332`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L332)
- doc: Per-rank linear-attention geometry (already TP/PCP-divided).
- signature: `class GdnHeadGeometry:`
- members:
  - <a id="GdnHeadGeometry.conv_dim"></a>`conv_dim(self)` — [`L344`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L344)
  - <a id="GdnHeadGeometry.conv_kernel_size"></a>`conv_kernel_size` — [`L341`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L341)
  - <a id="GdnHeadGeometry.key_head_dim"></a>`key_head_dim` — [`L337`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L337)
  - <a id="GdnHeadGeometry.local_key_heads"></a>`local_key_heads` — [`L335`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L335)
  - <a id="GdnHeadGeometry.local_value_heads"></a>`local_value_heads` — [`L336`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L336)
  - <a id="GdnHeadGeometry.value_head_dim"></a>`value_head_dim` — [`L338`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L338)
- used by: [`_admit_raiden_hybrid_kv_cache`](../tpu_connector.md#TPURaidenConnectorWorker._admit_raiden_hybrid_kv_cache), [`build_qwen35_pool_manifest`](pool_manifest.md#build_qwen35_pool_manifest), [`_pooled_gdn_state_views`](pool_manifest.md#_pooled_gdn_state_views), [`_gdn_conv_regions`](pool_manifest.md#_gdn_conv_regions), [`build_qwen35_pool_manifest_sol`](seq_on_lane.md#build_qwen35_pool_manifest_sol)

### <a id="ManifestError"></a>`ManifestError`  ·  implements/extends ValueError
- def: [`src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py:95`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L95) — documented in [kv-transfer-and-disaggregated-serving](../../../../../../concepts/kv-transfer-and-disaggregated-serving.md)
- doc: The live materialization cannot be described as a pool manifest.
- signature: `class ManifestError(ValueError):`
- used by: [`build_qwen35_pool_manifest`](pool_manifest.md#build_qwen35_pool_manifest), [`build_glm_mla_pool_manifest`](pool_manifest.md#build_glm_mla_pool_manifest), [`build_dsv4_pool_manifest`](pool_manifest.md#build_dsv4_pool_manifest), [`_pooled_gdn_state_views`](pool_manifest.md#_pooled_gdn_state_views), [`build_kimi_k3_pool_manifest`](pool_manifest.md#build_kimi_k3_pool_manifest), [`_bind_pool_manifest`](pool_manifest.md#_bind_pool_manifest), [`_gdn_conv_regions`](pool_manifest.md#_gdn_conv_regions), [`_block_major_fa_view`](pool_manifest.md#_block_major_fa_view), [`_dsv4_classify`](pool_manifest.md#_dsv4_classify), [`gdn_state_unit_bytes`](pool_manifest.md#gdn_state_unit_bytes), [`_pooled_kda_regions`](pool_manifest.md#_pooled_kda_regions), [`_region_placement`](pool_manifest.md#_region_placement), [`geometry_by_tag`](pool_manifest.md#PoolManifest.geometry_by_tag), [`_fa_regions`](pool_manifest.md#_fa_regions), [`_gdn_ssm_regions`](pool_manifest.md#_gdn_ssm_regions), [`_dsv4_check_role_rows`](pool_manifest.md#_dsv4_check_role_rows), [`_binding_for`](pool_manifest.md#_binding_for), [`_element_size`](pool_manifest.md#_element_size), [`_ordered_layers`](pool_manifest.md#_ordered_layers), [`_group_spec_for_layer`](pool_manifest.md#_group_spec_for_layer), [`dsv4_compressed_kv_layer_name`](pool_manifest.md#dsv4_compressed_kv_layer_name), [`_dsv4_layer_spec`](pool_manifest.md#_dsv4_layer_spec), [`_dsv4_spec_field`](pool_manifest.md#_dsv4_spec_field), [`_state_tag_suffix`](pool_manifest.md#_state_tag_suffix)

### <a id="PoolEntry"></a>`PoolEntry`
- def: [`src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py:131`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L131)
- signature: `class PoolEntry:`
- members:
  - <a id="PoolEntry.live_bytes_per_block"></a>`live_bytes_per_block(self)` — [`L142`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L142)
  - <a id="PoolEntry.to_pool_dict"></a>`to_pool_dict(self)` — [`L145`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L145) — Shape consumed by raiden's ``register_pools`` (coerce_pool_spec).
  - <a id="PoolEntry.base_offset_bytes"></a>`base_offset_bytes` — [`L135`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L135)
  - <a id="PoolEntry.block_stride_bytes"></a>`block_stride_bytes` — [`L136`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L136)
  - <a id="PoolEntry.dtype_tag"></a>`dtype_tag` — [`L139`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L139)
  - <a id="PoolEntry.layer_name"></a>`layer_name` — [`L133`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L133)
  - <a id="PoolEntry.num_blocks"></a>`num_blocks` — [`L137`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L137)
  - <a id="PoolEntry.regions"></a>`regions` — [`L138`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L138)
  - <a id="PoolEntry.storage_index"></a>`storage_index` — [`L134`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L134)
  - <a id="PoolEntry.tag"></a>`tag` — [`L132`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L132)
- uses (calls/refs, reference-scoped): [`RegionSpec`](pool_manifest.md#RegionSpec), [`live_bytes`](pool_manifest.md#RegionSpec.live_bytes), [`to_dict`](pool_manifest.md#RegionSpec.to_dict)
- used by: [`_admit_raiden_hybrid_kv_cache`](../tpu_connector.md#TPURaidenConnectorWorker._admit_raiden_hybrid_kv_cache), [`build_qwen35_pool_manifest`](pool_manifest.md#build_qwen35_pool_manifest), [`build_glm_mla_pool_manifest`](pool_manifest.md#build_glm_mla_pool_manifest), [`build_dsv4_pool_manifest`](pool_manifest.md#build_dsv4_pool_manifest), [`build_kimi_k3_pool_manifest`](pool_manifest.md#build_kimi_k3_pool_manifest), [`sol_fa_geometry_from_manifest`](seq_on_lane.md#sol_fa_geometry_from_manifest), [`_bind_pool_manifest`](pool_manifest.md#_bind_pool_manifest), [`measured_sol_layout_fingerprint`](seq_on_lane.md#measured_sol_layout_fingerprint), [`measured_fa_layout_fingerprint`](layout_fingerprint.md#measured_fa_layout_fingerprint), [`_measure_packed_row_layouts`](layout_fingerprint.md#_measure_packed_row_layouts), [`_stage3_row_geometry`](../tpu_connector.md#TPURaidenConnectorWorker._stage3_row_geometry), [`measured_kimi_k3_layout_fingerprint`](layout_fingerprint.md#measured_kimi_k3_layout_fingerprint), [`pools`](pool_manifest.md#PoolManifest.pools), [`sol_fa_page_tokens`](seq_on_lane.md#sol_fa_page_tokens), [`gdn_state_unit_bytes`](pool_manifest.md#gdn_state_unit_bytes), [`geometry_by_tag`](pool_manifest.md#PoolManifest.geometry_by_tag), [`fa_page_tokens`](layout_fingerprint.md#fa_page_tokens), [`pools_of_class`](pool_manifest.md#PoolManifest.pools_of_class), [`tag_counts`](pool_manifest.md#PoolManifest.tag_counts), [`pool_dicts`](pool_manifest.md#PoolManifest.pool_dicts), [`dtype_tags`](pool_manifest.md#PoolManifest.dtype_tags)

### <a id="PoolManifest"></a>`PoolManifest`
- def: [`src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py:159`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L159)
- signature: `class PoolManifest:`
- members:
  - <a id="PoolManifest.dtype_tags"></a>`dtype_tags(self)` — [`L198`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L198)
  - <a id="PoolManifest.geometry_by_tag"></a>`geometry_by_tag(self)` — [`L170`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L170) — Uniform (num_blocks, stride, live) per class tag; raises on
  - <a id="PoolManifest.pool_dicts"></a>`pool_dicts(self)` — [`L195`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L195)
  - <a id="PoolManifest.pools_of_class"></a>`pools_of_class(self, tag: str)` — [`L191`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L191) — Pools whose class tag is ``tag``, in manifest order.
  - <a id="PoolManifest.tag_counts"></a>`tag_counts(self)` — [`L164`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L164)
  - <a id="PoolManifest.binding"></a>`binding` — [`L160`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L160)
  - <a id="PoolManifest.pools"></a>`pools` — [`L162`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L162)
  - <a id="PoolManifest.storages"></a>`storages` — [`L161`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L161)
- uses (calls/refs, reference-scoped): [`ManifestError`](pool_manifest.md#ManifestError), [`tag`](pool_manifest.md#PoolEntry.tag), [`to_pool_dict`](pool_manifest.md#PoolEntry.to_pool_dict), [`class_tag`](tags.md#class_tag), [`PoolEntry`](pool_manifest.md#PoolEntry), [`layer_name`](pool_manifest.md#PoolEntry.layer_name), [`num_blocks`](pool_manifest.md#PoolEntry.num_blocks), [`block_stride_bytes`](pool_manifest.md#PoolEntry.block_stride_bytes), [`live_bytes_per_block`](pool_manifest.md#PoolEntry.live_bytes_per_block), [`dtype_tag`](pool_manifest.md#PoolEntry.dtype_tag)
- used by: [`_admit_raiden_hybrid_kv_cache`](../tpu_connector.md#TPURaidenConnectorWorker._admit_raiden_hybrid_kv_cache), [`build_qwen35_pool_manifest`](pool_manifest.md#build_qwen35_pool_manifest), [`_admit_raiden_dsv4_kv_cache`](../tpu_connector.md#TPURaidenConnectorWorker._admit_raiden_dsv4_kv_cache), [`build_glm_mla_pool_manifest`](pool_manifest.md#build_glm_mla_pool_manifest), [`_admit_raiden_glm_kv_cache`](../tpu_connector.md#TPURaidenConnectorWorker._admit_raiden_glm_kv_cache), [`build_dsv4_pool_manifest`](pool_manifest.md#build_dsv4_pool_manifest), [`build_kimi_k3_pool_manifest`](pool_manifest.md#build_kimi_k3_pool_manifest), [`sol_fa_geometry_from_manifest`](seq_on_lane.md#sol_fa_geometry_from_manifest), [`_bind_pool_manifest`](pool_manifest.md#_bind_pool_manifest), [`measured_sol_layout_fingerprint`](seq_on_lane.md#measured_sol_layout_fingerprint), [`measured_fa_layout_fingerprint`](layout_fingerprint.md#measured_fa_layout_fingerprint), [`_measure_packed_row_layouts`](layout_fingerprint.md#_measure_packed_row_layouts), [`_stage3_row_geometry`](../tpu_connector.md#TPURaidenConnectorWorker._stage3_row_geometry), [`measured_kimi_k3_layout_fingerprint`](layout_fingerprint.md#measured_kimi_k3_layout_fingerprint), [`sol_fa_page_tokens`](seq_on_lane.md#sol_fa_page_tokens), [`gdn_state_unit_bytes`](pool_manifest.md#gdn_state_unit_bytes), [`fa_page_tokens`](layout_fingerprint.md#fa_page_tokens), [`verify_storage_binding`](pool_manifest.md#verify_storage_binding), [`measured_glm_layout_fingerprint`](layout_fingerprint.md#measured_glm_layout_fingerprint), [`measured_dsv4_layout_fingerprint`](layout_fingerprint.md#measured_dsv4_layout_fingerprint), [`build_qwen35_pool_manifest_sol`](seq_on_lane.md#build_qwen35_pool_manifest_sol), [`materialize_storages`](pool_manifest.md#materialize_storages)

### <a id="RegionSpec"></a>`RegionSpec`
- def: [`src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py:100`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L100)
- doc: Mirror of raiden's RegionSpec (kept local so deviceless tests do not
- signature: `class RegionSpec:`
- members:
  - <a id="RegionSpec.extent_end_bytes"></a>`extent_end_bytes(self)` — [`L116`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L116) — Exclusive end of the last live byte relative to the pool base.
  - <a id="RegionSpec.live_bytes"></a>`live_bytes(self)` — [`L112`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L112)
  - <a id="RegionSpec.to_dict"></a>`to_dict(self)` — [`L126`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L126)
  - <a id="RegionSpec.name"></a>`name` — [`L104`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L104)
  - <a id="RegionSpec.num_units"></a>`num_units` — [`L108`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L108)
  - <a id="RegionSpec.offset_bytes"></a>`offset_bytes` — [`L105`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L105)
  - <a id="RegionSpec.stride_bytes"></a>`stride_bytes` — [`L106`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L106)
  - <a id="RegionSpec.unit_bytes"></a>`unit_bytes` — [`L107`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L107)
  - <a id="RegionSpec.units_per_stride"></a>`units_per_stride` — [`L109`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L109)
- used by: [`build_kimi_k3_pool_manifest`](pool_manifest.md#build_kimi_k3_pool_manifest), [`sol_fa_geometry_from_manifest`](seq_on_lane.md#sol_fa_geometry_from_manifest), [`_bind_pool_manifest`](pool_manifest.md#_bind_pool_manifest), [`_gdn_conv_regions`](pool_manifest.md#_gdn_conv_regions), [`sol_fa_regions`](seq_on_lane.md#sol_fa_regions), [`_stage3_row_geometry`](../tpu_connector.md#TPURaidenConnectorWorker._stage3_row_geometry), [`sol_fa_page_tokens`](seq_on_lane.md#sol_fa_page_tokens), [`gdn_state_unit_bytes`](pool_manifest.md#gdn_state_unit_bytes), [`_pooled_kda_regions`](pool_manifest.md#_pooled_kda_regions), [`_fa_regions`](pool_manifest.md#_fa_regions), [`_gdn_ssm_regions`](pool_manifest.md#_gdn_ssm_regions), [`_glm_row_region`](pool_manifest.md#_glm_row_region), [`to_pool_dict`](pool_manifest.md#PoolEntry.to_pool_dict), [`regions`](seq_on_lane.md#SolFaLayout.regions), [`fa_page_tokens`](layout_fingerprint.md#fa_page_tokens), [`_dsv4_row_region`](pool_manifest.md#_dsv4_row_region), [`regions`](pool_manifest.md#PoolEntry.regions), [`live_bytes_per_block`](pool_manifest.md#PoolEntry.live_bytes_per_block), [`regions`](pool_manifest.md#FaLayoutHook.regions)

### <a id="_PooledView"></a>`_PooledView`
- def: [`src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py:243`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L243)
- doc: Tensor-like metadata for one logical cache inside a unified pool.
- signature: `class _PooledView:`
- members:
  - <a id="_PooledView.element_size"></a>`element_size(self)` — [`L258`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L258)
  - <a id="_PooledView.storage_offset"></a>`storage_offset(self)` — [`L264`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L264)
  - <a id="_PooledView.untyped_storage"></a>`untyped_storage(self)` — [`L261`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L261)
  - <a id="_PooledView.dtype"></a>`dtype` — [`L253`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L253)
  - <a id="_PooledView.itemsize"></a>`itemsize` — [`L254`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L254)
  - <a id="_PooledView.nbytes"></a>`nbytes` — [`L256`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L256)
  - <a id="_PooledView.pool"></a>`pool` — [`L251`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L251)
  - <a id="_PooledView.shape"></a>`shape` — [`L252`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L252)
  - <a id="_PooledView.storage_offset_elems"></a>`storage_offset_elems` — [`L255`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L255)
- used by: [`_pooled_gdn_state_views`](pool_manifest.md#_pooled_gdn_state_views), [`_block_major_fa_view`](pool_manifest.md#_block_major_fa_view)

### <a id="_RegionPlacement"></a>`_RegionPlacement`
- def: [`src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py:280`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L280)
- doc: Byte placement of a single layer region within the merged block-major pool.
- signature: `class _RegionPlacement:`
- members:
  - <a id="_RegionPlacement.num_blocks"></a>`num_blocks` — [`L287`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L287)
  - <a id="_RegionPlacement.region_bytes"></a>`region_bytes` — [`L288`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L288)
  - <a id="_RegionPlacement.region_offset_bytes"></a>`region_offset_bytes` — [`L289`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L289)
- used by: [`_pooled_gdn_state_views`](pool_manifest.md#_pooled_gdn_state_views), [`_block_major_fa_view`](pool_manifest.md#_block_major_fa_view), [`_region_placement`](pool_manifest.md#_region_placement)

### <a id="_StorageTable"></a>`_StorageTable`
- def: [`src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py:712`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L712)
- doc: Ordered, pointer-deduplicated storage list.
- signature: `class _StorageTable:`
- members:
  - <a id="_StorageTable.index_for"></a>`index_for(self, tensor: Any)` — [`L719`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L719)
  - <a id="_StorageTable.storages"></a>`storages` — [`L716`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L716)
- protocol/private: <a id="_StorageTable.__init__"></a>`__init__`[`L715`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L715), <a id="_StorageTable._index_by_ptr"></a>`_index_by_ptr`[`L717`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L717)
- uses (calls/refs, reference-scoped): [`_storage_ptr`](pool_manifest.md#_storage_ptr)
- used by: [`build_glm_mla_pool_manifest`](pool_manifest.md#build_glm_mla_pool_manifest), [`build_dsv4_pool_manifest`](pool_manifest.md#build_dsv4_pool_manifest), [`_bind_pool_manifest`](pool_manifest.md#_bind_pool_manifest)

## Functions
- <a id="_bind_pool_manifest"></a>`_bind_pool_manifest(entries: Sequence[tuple[Any, PoolEntry]], raw_tensors: Sequence[Any])` — [`L1111`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L1111) — Resolve logical pool layouts to live storages and validate page bounds. — documented in [kv-transfer-and-disaggregated-serving](../../../../../../concepts/kv-transfer-and-disaggregated-serving.md)
- <a id="_binding_for"></a>`_binding_for(typed_tensors: Sequence[tuple[str, Any]], raw_tensors: Sequence[Any])` — [`L731`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L731) — Returns (binding, {typed position -> raw index}) after consistency
- <a id="_block_major_fa_view"></a>`_block_major_fa_view(*, pool: Any, spec: Any, layer_name: str, placement: _RegionPlacement)` — [`L685`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L685) — Describes one FA region of the merged block-major pool as a paged cache.
- <a id="_dsv4_check_role_rows"></a>`_dsv4_check_role_rows(kv_tag: str, layer_name: str, spec: Any, arrays: Sequence[Any])` — [`L1623`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L1623) — Row counts must match the runner's per-role allocation table.
- <a id="_dsv4_classify"></a>`_dsv4_classify(kv_cache_groups: Sequence[Any], named_kv_caches: Mapping[str, Any])` — [`L1534`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L1534) — Split DSv4's layers into one `Dsv4LayerEntry` per (layer, array).
- <a id="_dsv4_kv_tag"></a>`_dsv4_kv_tag(layer_name: str, spec: Any)` — [`L1505`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L1505) — The compressed-KV role of an MLA layer (CSA reports its NoPE tag).
- <a id="_dsv4_layer_spec"></a>`_dsv4_layer_spec(group_spec: Any, layer_name: str)` — [`L1462`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L1462) — The per-layer spec behind a DSv4 cache group.
- <a id="_dsv4_num_states"></a>`_dsv4_num_states(spec: Any, layer_name: str)` — [`L1497`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L1497) — Compressed states per page (`T` in the runner's allocation table).
- <a id="_dsv4_row_region"></a>`_dsv4_row_region(*, row_bytes: int, num_rows: int)` — [`L1448`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L1448) — One dense region of whole packed rows covering the full page.
- <a id="_dsv4_spec_field"></a>`_dsv4_spec_field(spec: Any, field: str, layer_name: str)` — [`L1482`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L1482) — One geometry field off a per-layer spec, or a hard failure.
- <a id="_dtype_tag"></a>`_dtype_tag(tensor: Any)` — [`L236`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L236)
- <a id="_element_size"></a>`_element_size(tensor: Any)` — [`L214`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L214)
- <a id="_fa_regions"></a>`_fa_regions(*, block_size_tokens: int, token_stride_bytes: int, num_kv_heads: int, head_size: int, itemsize: int)` — [`L351`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L351)
- <a id="_gdn_conv_regions"></a>`_gdn_conv_regions(*, conv_shape: Sequence[int], itemsize: int, geometry: GdnHeadGeometry)` — [`L378`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L378)
- <a id="_gdn_ssm_regions"></a>`_gdn_ssm_regions(*, ssm_shape: Sequence[int], itemsize: int)` — [`L444`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L444)
- <a id="_glm_row_region"></a>`_glm_row_region(tag: str, *, row_bytes: int, num_rows: int)` — [`L1264`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L1264) — One dense region of whole packed rows covering the full page.
- <a id="_group_spec_for_layer"></a>`_group_spec_for_layer(kv_cache_groups: Sequence[Any], layer_name: str)` — [`L493`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L493)
- <a id="_nbytes"></a>`_nbytes(tensor: Any)` — [`L207`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L207)
- <a id="_ordered_layers"></a>`_ordered_layers(named_kv_caches: Mapping[str, Any], layer_index_by_name: Mapping[str, int] | None = None)` — [`L1086`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L1086)
- <a id="_pool_layer_index"></a>`_pool_layer_index(layer_name: str, layer_index_by_name: Mapping[str, int] | None)` — [`L1078`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L1078)
- <a id="_pooled_gdn_state_views"></a>`_pooled_gdn_state_views(*, pool: Any, spec: Any, raw_tensors: Sequence[Any], layer_name: str, gdn_geometry: GdnHeadGeometry, placement: _RegionPlacement | None = None)` — [`L500`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L500) — Derive logical ``(conv, ssm)`` descriptors from a unified raw pool. — documented in [kv-transfer-and-disaggregated-serving](../../../../../../concepts/kv-transfer-and-disaggregated-serving.md)
- <a id="_pooled_kda_regions"></a>`_pooled_kda_regions(*, spec: Any, row_bytes: int, page_bytes: int)` — [`L630`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L630) — Expose KDA's live state through Qwen's two state pool tags.
- <a id="_raw_index_for"></a>`_raw_index_for(tensor: Any, raw_tensors: Sequence[Any])` — [`L268`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L268)
- <a id="_region_placement"></a>`_region_placement(block_major: BlockMajorPoolLayout, raw: Any, layer_name: str)` — [`L292`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L292) — documented in [kv-cache-layout-and-hbm-budget](../../../../../../concepts/kv-cache-layout-and-hbm-budget.md)
- <a id="_state_tag_suffix"></a>`_state_tag_suffix(layer_name: str, group_ordinals: Mapping[str, int] | None)` — [`L1102`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L1102)
- <a id="_storage_offset_bytes"></a>`_storage_offset_bytes(tensor: Any)` — [`L230`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L230)
- <a id="_storage_ptr"></a>`_storage_ptr(tensor: Any)` — [`L223`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L223)
- <a id="build_dsv4_pool_manifest"></a>`build_dsv4_pool_manifest(*, named_kv_caches: Mapping[str, Any], kv_cache_groups: Sequence[Any], raw_tensors: Sequence[Any])` — [`L1643`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L1643) — Builds the Pool Manifest for DeepSeek-V4, one pool per (layer, array). — documented in [kv-transfer-and-disaggregated-serving](../../../../../../concepts/kv-transfer-and-disaggregated-serving.md)
- <a id="build_glm_mla_pool_manifest"></a>`build_glm_mla_pool_manifest(*, named_kv_caches: Mapping[str, Any], raw_tensors: Sequence[Any], block_size_tokens: int, per_layer_tags: bool = False)` — [`L1280`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L1280) — Builds the Pool Manifest for GLM MLA models. — documented in [kv-transfer-and-disaggregated-serving](../../../../../../concepts/kv-transfer-and-disaggregated-serving.md)
- <a id="build_kimi_k3_pool_manifest"></a>`build_kimi_k3_pool_manifest(*, named_kv_caches: Mapping[str, Any], kv_cache_groups: Sequence[Any], raw_tensors: Sequence[Any], mamba_group_ordinal_by_layer: Mapping[str, int] | None = None)` — [`L990`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L990) — Describe K3's packed MLA/KDA rows using the shared hybrid pool tags. — documented in [kv-transfer-and-disaggregated-serving](../../../../../../concepts/kv-transfer-and-disaggregated-serving.md)
- <a id="build_qwen35_pool_manifest"></a>`build_qwen35_pool_manifest(*, named_kv_caches: Mapping[str, Any], kv_cache_groups: Sequence[Any], raw_tensors: Sequence[Any], gdn_geometry: GdnHeadGeometry, mamba_group_ordinal_by_layer: Mapping[str, int] | None = None, per_layer_tags: bool = False, fa_layout: FaLayoutHook | None = None, block_major: BlockMajorPoolLayout | None = None, layer_index_by_name: Mapping[str, int] | None = None)` — [`L785`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L785) — Builds the canonical pool manifest from the live materialization. — documented in [kv-cache-layout-and-hbm-budget](../../../../../../concepts/kv-cache-layout-and-hbm-budget.md)
- <a id="dsv4_compressed_kv_layer_name"></a>`dsv4_compressed_kv_layer_name(state_cache_name: str)` — [`L1435`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L1435) — `<...>.attn.compressor.state_cache` -> `<...>.attn`, and the indexer's
- <a id="gdn_state_unit_bytes"></a>`gdn_state_unit_bytes(manifest: PoolManifest)` — [`L465`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L465) — Per-head byte width of each GDN state region, keyed by region name.
- <a id="layer_index_from_name"></a>`layer_index_from_name(layer_name: str)` — [`L314`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L314)
- <a id="materialize_storages"></a>`materialize_storages(manifest: PoolManifest)` — [`L1175`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L1175) — Forces device-buffer materialization of every manifest storage.
- <a id="verify_storage_binding"></a>`verify_storage_binding(manifest: PoolManifest, named_kv_caches: Mapping[str, Any], raw_tensors: Sequence[Any])` — [`L1198`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L1198) — The dead-storage check (hard fail).

## Module values
- <a id="BINDING_ALIASED_RAW"></a>`BINDING_ALIASED_RAW` — [`L88`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L88)
- <a id="BINDING_PRIVATE_TYPED"></a>`BINDING_PRIVATE_TYPED` — [`L87`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L87)
- <a id="DSV4_CSA_COMPRESS_RATIO"></a>`DSV4_CSA_COMPRESS_RATIO` — [`L1425`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L1425)
- <a id="DSV4_IDX_SAL_ROWS"></a>`DSV4_IDX_SAL_ROWS` — [`L1426`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L1426)
- <a id="DSV4_INDEXER_CACHE_SUFFIX"></a>`DSV4_INDEXER_CACHE_SUFFIX` — [`L1424`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L1424)
- <a id="DSV4_STATE_CACHE_SUFFIX"></a>`DSV4_STATE_CACHE_SUFFIX` — [`L1423`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L1423)
- <a id="_DSV4_STATE_TAG_BY_KV_TAG"></a>`_DSV4_STATE_TAG_BY_KV_TAG` — [`L1428`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L1428)
- <a id="_GLM_REGION_NAMES"></a>`_GLM_REGION_NAMES` — [`L1257`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L1257)
- <a id="_KIMI_POOL_DTYPE_TAGS"></a>`_KIMI_POOL_DTYPE_TAGS` — [`L987`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/pool_manifest.py#L987)

