---
title: 'Module: src/vllm_torchtpu/distributed/kv_transfer/raiden/seq_on_lane.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/distributed/kv_transfer/raiden/seq_on_lane.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.distributed.kv_transfer.raiden.seq_on_lane`/
symbols:
  lower_fa_spans_sol: lower_fa_spans_sol().
  lower_gdn_state_fanout_spans_sol: lower_gdn_state_fanout_spans_sol().
  sol_fa_geometry_from_manifest: sol_fa_geometry_from_manifest().
  measured_sol_layout_fingerprint: measured_sol_layout_fingerprint().
  SeqOnLaneError: SeqOnLaneError#
  sol_fa_regions: sol_fa_regions().
  _lower_gdn_state_split_spans: _lower_gdn_state_split_spans().
  sol_fa_page_tokens: sol_fa_page_tokens().
  sol_fa_geometry_from_shape: sol_fa_geometry_from_shape().
  SolFaLayout.regions: SolFaLayout#regions().
  registration_source_bytes: registration_source_bytes().
  lower_gdn_state_shard_spans_sol: lower_gdn_state_shard_spans_sol().
  SolFaGeometry.page_tokens: SolFaGeometry#page_tokens.
  build_qwen35_pool_manifest_sol: build_qwen35_pool_manifest_sol().
  sol_fa_skip_bytes: sol_fa_skip_bytes().
  SolFaGeometry.slab_bytes: SolFaGeometry#slab_bytes().
  SolFaGeometry.kernel_page_bytes: SolFaGeometry#kernel_page_bytes().
  SolFaGeometry.num_kv_heads: SolFaGeometry#num_kv_heads().
  SolFaGeometry.pair_bytes: SolFaGeometry#pair_bytes().
  SolFaGeometry.shard_bytes: SolFaGeometry#shard_bytes().
  _state_region_map: _state_region_map().
  SolFaGeometry.head_dim: SolFaGeometry#head_dim().
  SolFaGeometry.bytes_per_token: SolFaGeometry#bytes_per_token().
  SolFaGeometry.packing: SolFaGeometry#packing.
  SolFaGeometry: SolFaGeometry#
  SolFaGeometry.kv_rows: SolFaGeometry#kv_rows.
  WORD_ROW_BYTES: WORD_ROW_BYTES.
  SolFaLayout.total_tokens: SolFaLayout#total_tokens().
  _tp_head_range: _tp_head_range().
  LANE_WIDTH: LANE_WIDTH.
  PACKING: PACKING.
  SOL_LAYOUT_TOKEN: SOL_LAYOUT_TOKEN.
  SolFaLayout: SolFaLayout#
  SolFaGeometry.packed_rows: SolFaGeometry#packed_rows.
  SolFaLayout.name: SolFaLayout#name.
  SOL_REGION_NAME: SOL_REGION_NAME.
  MIN_HEAD_DIM: MIN_HEAD_DIM.
  EXPECTED_SOL_MINOR_TO_MAJOR: EXPECTED_SOL_MINOR_TO_MAJOR.
  EXPECTED_SOL_TILES: EXPECTED_SOL_TILES.
  SOL_FINGERPRINT_SCHEMA: SOL_FINGERPRINT_SCHEMA.
  _STATE_REGION_FIELDS: _STATE_REGION_FIELDS.
  _default_layout_getter: _default_layout_getter().
  canonical_fingerprint: canonical_fingerprint().
  __all__: __all__.
---
# Module: [`src/vllm_torchtpu/distributed/kv_transfer/raiden/seq_on_lane.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/seq_on_lane.py)

## Classes
### <a id="SeqOnLaneError"></a>`SeqOnLaneError`  ·  implements/extends ValueError
- def: [`src/vllm_torchtpu/distributed/kv_transfer/raiden/seq_on_lane.py:89`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/seq_on_lane.py#L89)
- doc: The admitted geometry is not the seq-on-lane layout this module
- signature: `class SeqOnLaneError(ValueError):`
- used by: [`lower_fa_spans_sol`](seq_on_lane.md#lower_fa_spans_sol), [`lower_gdn_state_fanout_spans_sol`](seq_on_lane.md#lower_gdn_state_fanout_spans_sol), [`sol_fa_geometry_from_manifest`](seq_on_lane.md#sol_fa_geometry_from_manifest), [`_lower_gdn_state_split_spans`](seq_on_lane.md#_lower_gdn_state_split_spans), [`sol_fa_regions`](seq_on_lane.md#sol_fa_regions), [`sol_fa_page_tokens`](seq_on_lane.md#sol_fa_page_tokens), [`sol_fa_geometry_from_shape`](seq_on_lane.md#sol_fa_geometry_from_shape), [`regions`](seq_on_lane.md#SolFaLayout.regions), [`lower_gdn_state_shard_spans_sol`](seq_on_lane.md#lower_gdn_state_shard_spans_sol), [`sol_fa_skip_bytes`](seq_on_lane.md#sol_fa_skip_bytes), [`_state_region_map`](seq_on_lane.md#_state_region_map), [`shard_bytes`](seq_on_lane.md#SolFaGeometry.shard_bytes), [`_tp_head_range`](seq_on_lane.md#_tp_head_range)

### <a id="SolFaGeometry"></a>`SolFaGeometry`
- def: [`src/vllm_torchtpu/distributed/kv_transfer/raiden/seq_on_lane.py:95`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/seq_on_lane.py#L95)
- doc: Byte geometry of one seq-on-lane FA kernel page, derived from the live
- signature: `class SolFaGeometry:`
- members:
  - <a id="SolFaGeometry.bytes_per_token"></a>`bytes_per_token(self)` — [`L127`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/seq_on_lane.py#L127)
  - <a id="SolFaGeometry.head_dim"></a>`head_dim(self)` — [`L109`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/seq_on_lane.py#L109)
  - <a id="SolFaGeometry.kernel_page_bytes"></a>`kernel_page_bytes(self)` — [`L123`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/seq_on_lane.py#L123)
  - <a id="SolFaGeometry.num_kv_heads"></a>`num_kv_heads(self)` — [`L105`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/seq_on_lane.py#L105)
  - <a id="SolFaGeometry.pair_bytes"></a>`pair_bytes(self)` — [`L118`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/seq_on_lane.py#L118) — K and V of one KV head in one kernel page (adjacent rows).
  - <a id="SolFaGeometry.shard_bytes"></a>`shard_bytes(self, dst_shards: int)` — [`L130`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/seq_on_lane.py#L130) — Bytes of one destination head shard inside one kernel page.
  - <a id="SolFaGeometry.slab_bytes"></a>`slab_bytes(self)` — [`L113`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/seq_on_lane.py#L113) — One K or V row of one kernel page: contiguous (measured).
  - <a id="SolFaGeometry.kv_rows"></a>`kv_rows` — [`L99`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/seq_on_lane.py#L99)
  - <a id="SolFaGeometry.packed_rows"></a>`packed_rows` — [`L100`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/seq_on_lane.py#L100)
  - <a id="SolFaGeometry.packing"></a>`packing` — [`L102`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/seq_on_lane.py#L102)
  - <a id="SolFaGeometry.page_tokens"></a>`page_tokens` — [`L101`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/seq_on_lane.py#L101)
- uses (calls/refs, reference-scoped): [`SeqOnLaneError`](seq_on_lane.md#SeqOnLaneError), [`PACKING`](seq_on_lane.md#PACKING)
- used by: [`_stage3_state_pool_spans`](../tpu_connector.md#TPURaidenConnectorWorker._stage3_state_pool_spans), [`lower_fa_spans_sol`](seq_on_lane.md#lower_fa_spans_sol), [`sol_fa_geometry_from_manifest`](seq_on_lane.md#sol_fa_geometry_from_manifest), [`measured_sol_layout_fingerprint`](seq_on_lane.md#measured_sol_layout_fingerprint), [`sol_fa_regions`](seq_on_lane.md#sol_fa_regions), [`sol_fa_page_tokens`](seq_on_lane.md#sol_fa_page_tokens), [`sol_fa_geometry_from_shape`](seq_on_lane.md#sol_fa_geometry_from_shape), [`regions`](seq_on_lane.md#SolFaLayout.regions), [`sol_fa_skip_bytes`](seq_on_lane.md#sol_fa_skip_bytes), [`total_tokens`](seq_on_lane.md#SolFaLayout.total_tokens)

### <a id="SolFaLayout"></a>`SolFaLayout`  ·  implements/extends FaLayoutHook
- def: [`src/vllm_torchtpu/distributed/kv_transfer/raiden/seq_on_lane.py:208`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/seq_on_lane.py#L208)
- doc: `build_qwen35_pool_manifest` hook for the seq-on-lane FA shape.
- signature: `class SolFaLayout(FaLayoutHook):`
- members:
  - <a id="SolFaLayout.regions"></a>`regions(self, *, block_size_tokens: int, shape: Sequence[int], nbytes: int, num_kv_heads: int, head_size: int, itemsize: int)` — [`L217`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/seq_on_lane.py#L217)
  - <a id="SolFaLayout.total_tokens"></a>`total_tokens(self, shape: Sequence[int])` — [`L213`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/seq_on_lane.py#L213)
  - <a id="SolFaLayout.name"></a>`name` — [`L211`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/seq_on_lane.py#L211)
- uses (calls/refs, reference-scoped): [`SeqOnLaneError`](seq_on_lane.md#SeqOnLaneError), [`sol_fa_regions`](seq_on_lane.md#sol_fa_regions), [`sol_fa_geometry_from_shape`](seq_on_lane.md#sol_fa_geometry_from_shape), [`RegionSpec`](pool_manifest.md#RegionSpec), [`page_tokens`](seq_on_lane.md#SolFaGeometry.page_tokens), [`head_dim`](seq_on_lane.md#SolFaGeometry.head_dim), [`bytes_per_token`](seq_on_lane.md#SolFaGeometry.bytes_per_token), [`kv_rows`](seq_on_lane.md#SolFaGeometry.kv_rows), [`FaLayoutHook`](pool_manifest.md#FaLayoutHook), [`SOL_LAYOUT_TOKEN`](seq_on_lane.md#SOL_LAYOUT_TOKEN)
- used by: [`build_qwen35_pool_manifest_sol`](seq_on_lane.md#build_qwen35_pool_manifest_sol), [`regions`](pool_manifest.md#FaLayoutHook.regions), [`FaLayoutHook`](pool_manifest.md#FaLayoutHook), [`total_tokens`](pool_manifest.md#FaLayoutHook.total_tokens)

## Functions
- <a id="_default_layout_getter"></a>`_default_layout_getter(tensor: Any)` — [`L901`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/seq_on_lane.py#L901)
- <a id="_lower_gdn_state_split_spans"></a>`_lower_gdn_state_split_spans(*, tag: str, block_id: int, regions: Sequence[object], dst_shards: int, physical_granule_bytes: int = 1024)` — [`L618`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/seq_on_lane.py#L618) — Full-width producer state -> ``dst_shards`` head-sharded destination
- <a id="_state_region_map"></a>`_state_region_map(tag: str, regions: Sequence[object])` — [`L685`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/seq_on_lane.py#L685) — ``name -> (offset, stride, unit, num_units, units_per_stride)``.
- <a id="_tp_head_range"></a>`_tp_head_range(heads: int, degree: int, rank: int)` — [`L335`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/seq_on_lane.py#L335) — Global KV-head interval, including TP replication when heads < TP.
- <a id="build_qwen35_pool_manifest_sol"></a>`build_qwen35_pool_manifest_sol(*, named_kv_caches: Mapping[str, Any], kv_cache_groups: Sequence[Any], raw_tensors: Sequence[Any], gdn_geometry: GdnHeadGeometry, mamba_group_ordinal_by_layer: Mapping[str, int] | None = None, per_layer_tags: bool = False, layer_index_by_name: Mapping[str, int] | None = None)` — [`L251`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/seq_on_lane.py#L251) — The canonical Qwen3.5 manifest with seq-on-lane FA regions; GDN state
- <a id="canonical_fingerprint"></a>`canonical_fingerprint(payload: Mapping[str, Any])` — [`L907`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/seq_on_lane.py#L907)
- <a id="lower_fa_spans_sol"></a>`lower_fa_spans_sol(*, num_tokens: int, transfer_rank: int, parallelism: int, interleave_tokens: int, page_tokens: int, geometry: SolFaGeometry, dst_shards: int, block_ids: Sequence[int], producer_tp_size: int = 1, producer_tp_rank: int = 0, total_kv_heads: int | None = None, dst_dcp_size: int = 1)` — [`L351`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/seq_on_lane.py#L351) — Intersect source PCP/TP and destination TP/DCP ownership in HND. — documented in [kv-transfer-and-disaggregated-serving](../../../../../../concepts/kv-transfer-and-disaggregated-serving.md)
- <a id="lower_gdn_state_fanout_spans_sol"></a>`lower_gdn_state_fanout_spans_sol(*, tag: str, block_id: int, transfer_rank: int, parallelism: int, regions: Sequence[object], dst_shards: int, num_key_heads: int, num_value_heads: int, physical_granule_bytes: int = 1024)` — [`L703`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/seq_on_lane.py#L703) — One rank's GDN head shard into the narrower states of the — documented in [gated-deltanet-kernels](../../../../../../concepts/gated-deltanet-kernels.md)
- <a id="lower_gdn_state_shard_spans_sol"></a>`lower_gdn_state_shard_spans_sol(*, tag: str, block_id: int, transfer_rank: int, parallelism: int, regions: Sequence[object], dst_shards: int, producer_tp_size: int = 1, producer_tp_rank: int = 0, physical_granule_bytes: int = 1024, num_key_heads: int | None = None, num_value_heads: int | None = None)` — [`L511`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/seq_on_lane.py#L511) — One rank's GDN head shard into its destination shard's full state.
- <a id="measured_sol_layout_fingerprint"></a>`measured_sol_layout_fingerprint(manifest: PoolManifest, *, layout_getter: Callable[[Any], Any] | None = None, package_version: Callable[[str], str] | None = None)` — [`L914`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/seq_on_lane.py#L914) — E0' identity of the admitted seq-on-lane FA storage. — documented in [kv-transfer-and-disaggregated-serving](../../../../../../concepts/kv-transfer-and-disaggregated-serving.md)
- <a id="registration_source_bytes"></a>`registration_source_bytes(registration: PoolSpanRegistration)` — [`L875`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/seq_on_lane.py#L875) — Distinct source bytes a registration reads: the union over every span
- <a id="sol_fa_geometry_from_manifest"></a>`sol_fa_geometry_from_manifest(manifest: PoolManifest)` — [`L276`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/seq_on_lane.py#L276) — The admitted FA geometry (validated against the FA storage shape). — documented in [kv-transfer-and-disaggregated-serving](../../../../../../concepts/kv-transfer-and-disaggregated-serving.md)
- <a id="sol_fa_geometry_from_shape"></a>`sol_fa_geometry_from_shape(shape: Sequence[int], *, itemsize: int = 1)` — [`L140`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/seq_on_lane.py#L140) — Validates ``[pages, kv_rows, packed_rows, 4, page_tokens]`` fp8 and
- <a id="sol_fa_page_tokens"></a>`sol_fa_page_tokens(manifest: PoolManifest)` — [`L304`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/seq_on_lane.py#L304) — Manager page tokens of every FA pool (kernel pages x page tokens); the
- <a id="sol_fa_regions"></a>`sol_fa_regions(*, block_size_tokens: int, geometry: SolFaGeometry)` — [`L184`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/seq_on_lane.py#L184) — One dense region per manager block: ``num_units`` kernel pages of
- <a id="sol_fa_skip_bytes"></a>`sol_fa_skip_bytes(skip_tokens: int, *, geometry: SolFaGeometry, dst_shards: int)` — [`L320`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/seq_on_lane.py#L320) — Prefix-aware clip in one destination shard's compact byte space: a

## Module values
- <a id="EXPECTED_SOL_MINOR_TO_MAJOR"></a>`EXPECTED_SOL_MINOR_TO_MAJOR` — [`L85`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/seq_on_lane.py#L85)
- <a id="EXPECTED_SOL_TILES"></a>`EXPECTED_SOL_TILES` — [`L86`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/seq_on_lane.py#L86)
- <a id="LANE_WIDTH"></a>`LANE_WIDTH` — [`L75`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/seq_on_lane.py#L75)
- <a id="MIN_HEAD_DIM"></a>`MIN_HEAD_DIM` — [`L84`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/seq_on_lane.py#L84)
- <a id="PACKING"></a>`PACKING` — [`L77`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/seq_on_lane.py#L77)
- <a id="SOL_FINGERPRINT_SCHEMA"></a>`SOL_FINGERPRINT_SCHEMA` — [`L81`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/seq_on_lane.py#L81)
- <a id="SOL_LAYOUT_TOKEN"></a>`SOL_LAYOUT_TOKEN` — [`L80`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/seq_on_lane.py#L80)
- <a id="SOL_REGION_NAME"></a>`SOL_REGION_NAME` — [`L82`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/seq_on_lane.py#L82)
- <a id="WORD_ROW_BYTES"></a>`WORD_ROW_BYTES` — [`L79`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/seq_on_lane.py#L79)
- <a id="_STATE_REGION_FIELDS"></a>`_STATE_REGION_FIELDS` — [`L676`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/seq_on_lane.py#L676)
- <a id="__all__"></a>`__all__` — [`L980`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/seq_on_lane.py#L980)

