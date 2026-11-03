---
title: 'Module: src/vllm_torchtpu/kernels/fused_moe/v2/host.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/fused_moe/v2/host.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.fused_moe.v2.host`/
symbols:
  build_routing_tables_sharded: build_routing_tables_sharded().
  build_routing_tables: build_routing_tables().
  ROWBLK: ROWBLK.
  vmem_scratch_arrays: vmem_scratch_arrays().
  HIDDEN_LANE_BLOCK: HIDDEN_LANE_BLOCK.
  WEIGHT_FORMS: WEIGHT_FORMS.
  vmem_tile_body_arrays: vmem_tile_body_arrays().
  WeightFormat: WeightFormat#
  fit_weight_slots: fit_weight_slots().
  vmem_estimate_bytes: vmem_estimate_bytes().
  weight_form: weight_form().
  FP8: FP8.
  U32_SUBLANE_TILE: U32_SUBLANE_TILE.
  OUT_PARITIES: OUT_PARITIES.
  PACK4: PACK4.
  WIDEN_KCHUNK: WIDEN_KCHUNK.
  WeightForm.quantized_activations: WeightForm#quantized_activations().
  WeightForm.has_scales: WeightForm#has_scales().
  weight_format_of_dtype: weight_format_of_dtype().
  ALIGNMENT_SLOT_FIELD: ALIGNMENT_SLOT_FIELD.
  align_up: align_up().
  QB4: QB4.
  pow2_shift: pow2_shift().
  token_gather_window_rows: token_gather_window_rows().
  act_scale_slab_rows: act_scale_slab_rows().
  WeightFormat.FP8: WeightFormat#FP8.
  shard_transport_tables_in_blocks.i32: shard_transport_tables_in_blocks().i32().
  BF16: BF16.
  ROWBLK_SHIFT: ROWBLK_SHIFT.
  ragged_stride_bound: ragged_stride_bound().
  shard_count_vector.over_experts: shard_count_vector().over_experts().
  act_scale_window_rows: act_scale_window_rows().
  _lookup_per_pair: _lookup_per_pair().
  _refuse_bad_plan_args: _refuse_bad_plan_args().
  off_shard_slab_row: off_shard_slab_row().
  shard_token_gather: shard_token_gather().
  shard_transport_tables_in_blocks: shard_transport_tables_in_blocks().
  WeightSlots.fits: WeightSlots#fits().
  vmem_limit: vmem_limit().
  MAX_NBUF: MAX_NBUF.
  SLOT_FIELD_SHIFT: SLOT_FIELD_SHIFT.
  WeightFormat.FP4: WeightFormat#FP4.
  WeightFormat.INT8: WeightFormat#INT8.
  rank_window: rank_window().
  _rank_within_window: _rank_within_window().
  _lookup_per_sub_pair: _lookup_per_sub_pair().
  TOKEN_GATHER_DMA_ALIGNMENT: TOKEN_GATHER_DMA_ALIGNMENT.
  routing_block: routing_block().
  pair_block_hist: pair_block_hist().
  ShardRoutingTables.pair_grid: ShardRoutingTables#pair_grid().
  token_gather_smem_bytes: token_gather_smem_bytes().
  mirror_run_tiles: mirror_run_tiles().
  row_lane_blocks: row_lane_blocks().
  WEIGHT_FORMAT_NAMES: WEIGHT_FORMAT_NAMES.
  shard_count_vector: shard_count_vector().
  FP8_MAX: FP8_MAX.
  FP4: FP4.
  MAX_WEIGHT_PREFETCH_DISTANCE: MAX_WEIGHT_PREFETCH_DISTANCE.
  WeightFormat.BF16: WeightFormat#BF16.
  WeightForm: WeightForm#
  WeightForm.weight_dtype: WeightForm#weight_dtype.
  WeightForm.scale_layout: WeightForm#scale_layout.
  WeightForm.wire_dtype: WeightForm#wire_dtype.
  RoutingTables: RoutingTables#
  ShardRoutingTables: ShardRoutingTables#
  SLOT_FIELD_MASK: SLOT_FIELD_MASK.
  _window_hist: _window_hist().
  array_vmem_bytes: array_vmem_bytes().
  check_u32_sublane_tile: check_u32_sublane_tile().
  HIDDEN_MAX_BLOCKS: HIDDEN_MAX_BLOCKS.
  MAX_ROUTING_BLOCK: MAX_ROUTING_BLOCK.
  RoutingTables.arrival_row: RoutingTables#arrival_row.
  _block_hist: _block_hist().
  local_slab_rows: local_slab_rows().
  WeightSlots.vmem_bytes: WeightSlots#vmem_bytes.
  WeightSlots.limit: WeightSlots#limit.
  WeightForm.name: WeightForm#name.
  RoutingTables.pair_grid: RoutingTables#pair_grid().
  nbuf_for: nbuf_for().
  TOKEN_GATHER_TILES_PER_WINDOW: TOKEN_GATHER_TILES_PER_WINDOW.
  WIDENED_BLOCK_BUFFERS: WIDENED_BLOCK_BUFFERS.
  RoutingTables.mirror_row: RoutingTables#mirror_row.
  ShardRoutingTables.pos: ShardRoutingTables#pos.
  ShardRoutingTables.mirror_pos: ShardRoutingTables#mirror_pos.
  ShardRoutingTables.n_tokens: ShardRoutingTables#n_tokens.
  ShardRoutingTables.topk: ShardRoutingTables#topk.
  _rank_within_block: _rank_within_block().
  _per_sub_block: _per_sub_block().
  GatheredPairs: GatheredPairs#
  shard_expert_slabs: shard_expert_slabs().
  expert_visit_list: expert_visit_list().
  shard_push_tables_in_rows: shard_push_tables_in_rows().
  COUNT_RECV_ROWS: COUNT_RECV_ROWS.
  COUNT_RECV_MIRROR: COUNT_RECV_MIRROR.
  INT8: INT8.
  VMEM_FRACTION: VMEM_FRACTION.
  ROUTING_WINDOW: ROUTING_WINDOW.
  ROUTING_WINDOW_MIN_PAIRS: ROUTING_WINDOW_MIN_PAIRS.
  contrib_mirror_rows: contrib_mirror_rows().
  arrival_mirror_rows: arrival_mirror_rows().
  WeightForm.act_dtype: WeightForm#act_dtype.
  WeightForm.act_max: WeightForm#act_max.
  gather_clamp_bounds: gather_clamp_bounds().
  RoutingTables.run_tiles: RoutingTables#run_tiles.
  RoutingTables.slab_row: RoutingTables#slab_row.
  RoutingTables.run_rows: RoutingTables#run_rows.
  RoutingTables.run_rows_aligned: RoutingTables#run_rows_aligned.
  RoutingTables.run_start_aligned: RoutingTables#run_start_aligned.
  RoutingTables.region_rows: RoutingTables#region_rows.
  RoutingTables.recv_base: RoutingTables#recv_base.
  RoutingTables.recv_rows: RoutingTables#recv_rows.
  RoutingTables.expert_rows_aligned: RoutingTables#expert_rows_aligned.
  RoutingTables.expert_base: RoutingTables#expert_base.
  RoutingTables.rows_alloc: RoutingTables#rows_alloc.
  ShardRoutingTables.run_tiles: ShardRoutingTables#run_tiles.
  ShardRoutingTables.slab_row: ShardRoutingTables#slab_row.
  ShardRoutingTables.run_rows: ShardRoutingTables#run_rows.
  ShardRoutingTables.run_rows_aligned: ShardRoutingTables#run_rows_aligned.
  ShardRoutingTables.run_start_aligned: ShardRoutingTables#run_start_aligned.
  ShardRoutingTables.region_rows: ShardRoutingTables#region_rows.
  ShardRoutingTables.recv_base: ShardRoutingTables#recv_base.
  ShardRoutingTables.recv_rows: ShardRoutingTables#recv_rows.
  ShardRoutingTables.expert_rows_aligned: ShardRoutingTables#expert_rows_aligned.
  ShardRoutingTables.expert_base: ShardRoutingTables#expert_base.
  ShardRoutingTables.rows_alloc: ShardRoutingTables#rows_alloc.
  _over_sub_blocks: _over_sub_blocks().
  _window_table: _window_table().
  GatheredPairs.expert_blocks: GatheredPairs#expert_blocks.
  GatheredPairs.local_blocks: GatheredPairs#local_blocks.
  GatheredPairs.block_hist: GatheredPairs#block_hist.
  GatheredPairs.rows_by_dest: GatheredPairs#rows_by_dest.
  GatheredPairs.n_tokens: GatheredPairs#n_tokens.
  GatheredPairs.topk: GatheredPairs#topk.
  COUNT_SEND_ROWS: COUNT_SEND_ROWS.
  COUNT_VISITS: COUNT_VISITS.
  COUNT_SEND_MIRROR: COUNT_SEND_MIRROR.
  COUNT_SELF_MIRROR: COUNT_SELF_MIRROR.
  MIN_GENERATION: MIN_GENERATION.
  chip_generation: chip_generation().
  WeightSlots: WeightSlots#
  WeightSlots.distance: WeightSlots#distance.
  WeightSlots.nbuf: WeightSlots#nbuf.
  WeightFormat.__str__: WeightFormat#__str__().
  WeightFormat.__repr__: WeightFormat#__repr__().
  COUNT_SEND_ALIGNED_ROWS: COUNT_SEND_ALIGNED_ROWS.
  COUNT_RECV_ALIGNED_ROWS: COUNT_RECV_ALIGNED_ROWS.
  N_COUNTS: N_COUNTS.
---
# Module: [`src/vllm_torchtpu/kernels/fused_moe/v2/host.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py)

## Classes
### <a id="GatheredPairs"></a>`GatheredPairs`  ·  implements/extends NamedTuple
- def: [`src/vllm_torchtpu/kernels/fused_moe/v2/host.py:805`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L805)
- doc: The routing exchange, already unpacked by the caller.
- signature: `class GatheredPairs(NamedTuple):`
- members:
  - <a id="GatheredPairs.block_hist"></a>`block_hist` — [`L819`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L819)
  - <a id="GatheredPairs.expert_blocks"></a>`expert_blocks` — [`L817`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L817)
  - <a id="GatheredPairs.local_blocks"></a>`local_blocks` — [`L818`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L818)
  - <a id="GatheredPairs.n_tokens"></a>`n_tokens` — [`L821`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L821)
  - <a id="GatheredPairs.rows_by_dest"></a>`rows_by_dest` — [`L820`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L820)
  - <a id="GatheredPairs.topk"></a>`topk` — [`L822`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L822)
- used by: [`compute_local`](layer.md#fused_ep_moe_v2.compute_local)

### <a id="RoutingTables"></a>`RoutingTables`  ·  implements/extends NamedTuple
- def: [`src/vllm_torchtpu/kernels/fused_moe/v2/host.py:423`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L423)
- doc: Where every routed (token, expert) pair computes, and where it lands.
- signature: `class RoutingTables(NamedTuple):`
- members:
  - <a id="RoutingTables.pair_grid"></a>`pair_grid(self)` — [`L459`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L459) — (tokens, selections) the plan was built over.
  - <a id="RoutingTables.arrival_row"></a>`arrival_row` — [`L432`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L432)
  - <a id="RoutingTables.expert_base"></a>`expert_base` — [`L454`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L454)
  - <a id="RoutingTables.expert_rows_aligned"></a>`expert_rows_aligned` — [`L452`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L452)
  - <a id="RoutingTables.mirror_row"></a>`mirror_row` — [`L434`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L434)
  - <a id="RoutingTables.recv_base"></a>`recv_base` — [`L448`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L448)
  - <a id="RoutingTables.recv_rows"></a>`recv_rows` — [`L450`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L450)
  - <a id="RoutingTables.region_rows"></a>`region_rows` — [`L446`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L446)
  - <a id="RoutingTables.rows_alloc"></a>`rows_alloc` — [`L456`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L456)
  - <a id="RoutingTables.run_rows"></a>`run_rows` — [`L440`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L440)
  - <a id="RoutingTables.run_rows_aligned"></a>`run_rows_aligned` — [`L442`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L442)
  - <a id="RoutingTables.run_start_aligned"></a>`run_start_aligned` — [`L444`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L444)
  - <a id="RoutingTables.run_tiles"></a>`run_tiles` — [`L436`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L436)
  - <a id="RoutingTables.slab_row"></a>`slab_row` — [`L438`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L438)
- used by: [`compute_local`](layer.md#fused_ep_moe_v2.compute_local), [`build_routing_tables`](host.md#build_routing_tables)

### <a id="ShardRoutingTables"></a>`ShardRoutingTables`  ·  implements/extends NamedTuple
- def: [`src/vllm_torchtpu/kernels/fused_moe/v2/host.py:642`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L642)
- doc: One shard's complementary slices of the routing plan.
- signature: `class ShardRoutingTables(NamedTuple):`
- members:
  - <a id="ShardRoutingTables.pair_grid"></a>`pair_grid(self)` — [`L669`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L669)
  - <a id="ShardRoutingTables.expert_base"></a>`expert_base` — [`L663`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L663)
  - <a id="ShardRoutingTables.expert_rows_aligned"></a>`expert_rows_aligned` — [`L662`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L662)
  - <a id="ShardRoutingTables.mirror_pos"></a>`mirror_pos` — [`L653`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L653)
  - <a id="ShardRoutingTables.n_tokens"></a>`n_tokens` — [`L665`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L665)
  - <a id="ShardRoutingTables.pos"></a>`pos` — [`L652`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L652)
  - <a id="ShardRoutingTables.recv_base"></a>`recv_base` — [`L660`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L660)
  - <a id="ShardRoutingTables.recv_rows"></a>`recv_rows` — [`L661`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L661)
  - <a id="ShardRoutingTables.region_rows"></a>`region_rows` — [`L659`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L659)
  - <a id="ShardRoutingTables.rows_alloc"></a>`rows_alloc` — [`L664`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L664)
  - <a id="ShardRoutingTables.run_rows"></a>`run_rows` — [`L656`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L656)
  - <a id="ShardRoutingTables.run_rows_aligned"></a>`run_rows_aligned` — [`L657`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L657)
  - <a id="ShardRoutingTables.run_start_aligned"></a>`run_start_aligned` — [`L658`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L658)
  - <a id="ShardRoutingTables.run_tiles"></a>`run_tiles` — [`L654`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L654)
  - <a id="ShardRoutingTables.slab_row"></a>`slab_row` — [`L655`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L655)
  - <a id="ShardRoutingTables.topk"></a>`topk` — [`L666`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L666)
- used by: [`compute_local`](layer.md#fused_ep_moe_v2.compute_local), [`build_routing_tables_sharded`](host.md#build_routing_tables_sharded)

### <a id="WeightForm"></a>`WeightForm`  ·  implements/extends NamedTuple
- def: [`src/vllm_torchtpu/kernels/fused_moe/v2/host.py:278`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L278)
- doc: One weight format the kernel takes, and everything that follows it.
- signature: `class WeightForm(NamedTuple):`
- members:
  - <a id="WeightForm.has_scales"></a>`has_scales(self)` — [`L305`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L305) — Whether the caller supplies weight scales at all. — documented in [fused-moe-kernels](../../../../../../concepts/fused-moe-kernels.md)
  - <a id="WeightForm.quantized_activations"></a>`quantized_activations(self)` — [`L310`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L310) — Whether token rows are quantized, and so carry a row scale. — documented in [fused-moe-kernels](../../../../../../concepts/fused-moe-kernels.md)
  - <a id="WeightForm.act_dtype"></a>`act_dtype` — [`L299`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L299)
  - <a id="WeightForm.act_max"></a>`act_max` — [`L300`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L300)
  - <a id="WeightForm.name"></a>`name` — [`L297`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L297)
  - <a id="WeightForm.scale_layout"></a>`scale_layout` — [`L301`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L301)
  - <a id="WeightForm.weight_dtype"></a>`weight_dtype` — [`L298`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L298)
  - <a id="WeightForm.wire_dtype"></a>`wire_dtype` — [`L302`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L302)
- uses (calls/refs, reference-scoped): [`WeightFormat`](host.md#WeightFormat)
- used by: [`_build_fused_ep_moe_kernel`](kernel.md#_build_fused_ep_moe_kernel), [`compute_local`](layer.md#fused_ep_moe_v2.compute_local), [`fused_ep_moe_v2`](layer.md#fused_ep_moe_v2), [`compute_tile`](kernel.md#_build_fused_ep_moe_kernel.kernel.expert_tiles.tile_body.compute_tile), [`vmem_scratch_arrays`](host.md#vmem_scratch_arrays), [`_build_split_ops`](../../../layers/adapter/fused_moe_ep.md#_build_split_ops), [`make_call`](kernel.md#_build_fused_ep_moe_kernel.make_call), [`WEIGHT_FORMS`](host.md#WEIGHT_FORMS), [`vmem_tile_body_arrays`](host.md#vmem_tile_body_arrays), [`quantize_local`](layer.md#fused_ep_moe_v2.quantize_local), [`weight_format_of_dtype`](host.md#weight_format_of_dtype), [`unpack_operands`](layer.md#fused_ep_moe_v2.unpack_operands)

### <a id="WeightFormat"></a>`WeightFormat`  ·  implements/extends Enum, str
- def: [`src/vllm_torchtpu/kernels/fused_moe/v2/host.py:254`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L254) — documented in [fused-moe-kernels](../../../../../../concepts/fused-moe-kernels.md)
- doc: The weight formats the kernel takes, one member per accepted form.
- signature: `class WeightFormat(str, enum.Enum):`
- members:
  - <a id="WeightFormat.BF16"></a>`BF16` — [`L269`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L269)
  - <a id="WeightFormat.FP4"></a>`FP4` — [`L267`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L267)
  - <a id="WeightFormat.FP8"></a>`FP8` — [`L266`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L266)
  - <a id="WeightFormat.INT8"></a>`INT8` — [`L268`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L268)
- protocol/private: <a id="WeightFormat.__repr__"></a>`__repr__`[`L274`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L274), <a id="WeightFormat.__str__"></a>`__str__`[`L271`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L271)
- used by: [`_build_fused_ep_moe_kernel`](kernel.md#_build_fused_ep_moe_kernel), [`fused_ep_moe_v2`](layer.md#fused_ep_moe_v2), [`compute_tile`](kernel.md#_build_fused_ep_moe_kernel.kernel.expert_tiles.tile_body.compute_tile), [`vmem_scratch_arrays`](host.md#vmem_scratch_arrays), [`make_call`](kernel.md#_build_fused_ep_moe_kernel.make_call), [`WEIGHT_FORMS`](host.md#WEIGHT_FORMS), [`vmem_tile_body_arrays`](host.md#vmem_tile_body_arrays), [`fit_weight_slots`](host.md#fit_weight_slots), [`vmem_estimate_bytes`](host.md#vmem_estimate_bytes), [`weight_form`](host.md#weight_form), [`weight_format_of_dtype`](host.md#weight_format_of_dtype), [`WeightFormat`](__init__.md#WeightFormat), [`name`](host.md#WeightForm.name)

### <a id="WeightSlots"></a>`WeightSlots`  ·  implements/extends NamedTuple
- def: [`src/vllm_torchtpu/kernels/fused_moe/v2/host.py:1567`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L1567)
- doc: The weight-slot schedule one build runs at, and what it costs.
- signature: `class WeightSlots(NamedTuple):`
- members:
  - <a id="WeightSlots.fits"></a>`fits(self)` — [`L1581`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L1581) — Whether the build at this depth is inside the budget.
  - <a id="WeightSlots.distance"></a>`distance` — [`L1575`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L1575)
  - <a id="WeightSlots.limit"></a>`limit` — [`L1578`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L1578)
  - <a id="WeightSlots.nbuf"></a>`nbuf` — [`L1576`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L1576)
  - <a id="WeightSlots.vmem_bytes"></a>`vmem_bytes` — [`L1577`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L1577)
- used by: [`_build_fused_ep_moe_kernel`](kernel.md#_build_fused_ep_moe_kernel), [`fit_weight_slots`](host.md#fit_weight_slots)

## Functions
- <a id="_block_hist"></a>`_block_hist(expert_blocks, bins)` — [`L685`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L685) — Number of pairs per routing block and expert bin.
- <a id="_lookup_per_pair"></a>`_lookup_per_pair(table, expert_blocks, bins)` — [`L464`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L464) — ``table[b, expert_blocks[b, i]]`` -- one value per routed pair.
- <a id="_lookup_per_sub_pair"></a>`_lookup_per_sub_pair(table, expert_blocks, bins, window)` — [`L786`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L786) — ``table[b, i // window, expert_blocks[b, i]]`` -- one value per pair.
- <a id="_over_sub_blocks"></a>`_over_sub_blocks(window_hist)` — [`L761`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L761) — The per-block histogram a sub-block histogram refines.
- <a id="_per_sub_block"></a>`_per_sub_block(x, window)` — [`L707`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L707) — ``x[b, sub, ...]`` read back as ``x[b, pair, ...]``.
- <a id="_rank_within_block"></a>`_rank_within_block(expert_blocks, block)` — [`L678`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L678) — ``#{j < i : e_j == e_i}`` for each pair in a routing block.
- <a id="_rank_within_window"></a>`_rank_within_window(expert_blocks, window)` — [`L722`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L722) — ``#{j < i : e_j == e_i}`` over i's sub-block rather than its block.
- <a id="_refuse_bad_plan_args"></a>`_refuse_bad_plan_args(T, K, *, e_total, ep, t_local, block, tile_m)` — [`L479`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L479) — Argument checks shared by the replicated and sharded plan builders.
- <a id="_window_hist"></a>`_window_hist(expert_blocks, bins, window)` — [`L746`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L746) — Pairs per (routing block, sub-block, expert bin).
- <a id="_window_table"></a>`_window_table(table, window_hist)` — [`L766`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L766) — A per-block plan table resolved per sub-block, for the lookup.
- <a id="act_scale_slab_rows"></a>`act_scale_slab_rows(rows_alloc)` — [`L228`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L228) — Sublanes the activation row-scale slab is handed to the kernel as.
- <a id="act_scale_window_rows"></a>`act_scale_window_rows(tile_m)` — [`L249`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L249) — Sublanes of the scale slab one tile of `tile_m` rows can touch.
- <a id="align_up"></a>`align_up(v, m)` — [`L181`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L181)
- <a id="array_vmem_bytes"></a>`array_vmem_bytes(shape, dtype, info)` — [`L1300`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L1300) — Bytes one VMEM array of this shape and dtype occupies.
- <a id="arrival_mirror_rows"></a>`arrival_mirror_rows(recv_rows, e_total, tile_m)` — [`L218`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L218) — Sublanes the arrival mirror needs, on the same slack rule.
- <a id="build_routing_tables"></a>`build_routing_tables(topk_idx, *, e_total, ep, t_local, block, tile_m, shard_stride)` — [`L522`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L522) — Assign every routed (token, expert) pair the slab row it computes on. — documented in [fused-moe-kernels](../../../../../../concepts/fused-moe-kernels.md)
- <a id="build_routing_tables_sharded"></a>`build_routing_tables_sharded(topk_idx, me, *, e_total, ep, t_local, block, tile_m, shard_stride, all_gather_rows=None, gathered=None)` — [`L825`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L825) — Build only the routing-plan slices consumed by shard ``me``. — documented in [fused-moe-kernels](../../../../../../concepts/fused-moe-kernels.md)
- <a id="check_u32_sublane_tile"></a>`check_u32_sublane_tile(info=None)` — [`L1328`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L1328) — Refuse a chip whose 32-bit sublane tiling is not the one the packed
- <a id="chip_generation"></a>`chip_generation(info=None)` — [`L1288`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L1288) — The generation of the chip this build is for.
- <a id="contrib_mirror_rows"></a>`contrib_mirror_rows(rows_alloc, g_local, tile_m)` — [`L206`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L206) — Sublanes the contribution mirror needs.
- <a id="expert_visit_list"></a>`expert_visit_list(rows, g_local)` — [`L1053`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L1053) — The local experts to visit, and how many, from rows [g_local] i32.
- <a id="fit_weight_slots"></a>`fit_weight_slots(g_local, capacity, hidden, inter, *, max_distance=MAX_WEIGHT_PREFETCH_DISTANCE, weight_format=WeightFormat.FP8, rhs_qb=QB4, has_w1_bias=False, has_w2_bias=False, info=None, limit=None)` — [`L1586`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L1586) — The deepest prefetch schedule this shape's VMEM leaves room for. — documented in [fused-moe-kernels](../../../../../../concepts/fused-moe-kernels.md)
- <a id="gather_clamp_bounds"></a>`gather_clamp_bounds(T)` — [`L395`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L395) — The (low, high) token numbers the routing gather table is clipped to.
- <a id="shard_transport_tables_in_blocks.i32"></a>`i32(a)` — [`L1154`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L1154) — One table in block units: the row count's high bits.
- <a id="local_slab_rows"></a>`local_slab_rows(routing, me, *, shard_stride)` — [`L991`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L991) — `routing.slab_row` rebased onto shard `me`'s own slab.
- <a id="mirror_run_tiles"></a>`mirror_run_tiles(run_start, run_rows, tile_m)` — [`L195`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L195) — Mirror sublanes a run owns: the source tiles its rows fall in.
- <a id="nbuf_for"></a>`nbuf_for(distance)` — [`L64`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L64) — Weight buffer slots a prefetch distance needs.
- <a id="off_shard_slab_row"></a>`off_shard_slab_row(shard_stride, ep)` — [`L673`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L673) — Sentinel beyond both slab destinations after any shard rebasing.
- <a id="shard_count_vector.over_experts"></a>`over_experts(term)` — [`L1242`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L1242) — One count's reduction, keeping the expert-parallel axis.
- <a id="pair_block_hist"></a>`pair_block_hist(expert_blocks, e_total)` — [`L692`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L692) — Pairs per routing block and expert, over ``e_total`` bins.
- <a id="pow2_shift"></a>`pow2_shift(m, what)` — [`L133`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L133) — The shift a division by `m` is, refusing anything else by name.
- <a id="ragged_stride_bound"></a>`ragged_stride_bound(num_tokens, topk, e_total, capacity)` — [`L371`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L371) — Per-shard slab rows the no-drop worst case needs: every routed row — documented in [fused-moe-kernels](../../../../../../concepts/fused-moe-kernels.md)
- <a id="rank_window"></a>`rank_window(block, shard_pairs)` — [`L697`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L697) — The width the rank pass self-compares over, `block` where it pays.
- <a id="routing_block"></a>`routing_block(t_local, topk)` — [`L415`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L415) — The widest power-of-two block dividing this shard's routed pairs. — documented in [fused-moe-kernels](../../../../../../concepts/fused-moe-kernels.md)
- <a id="row_lane_blocks"></a>`row_lane_blocks(hidden)` — [`L223`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L223) — Lane blocks one token row is staged as: a row is (this many, 128).
- <a id="shard_count_vector"></a>`shard_count_vector(routing, expert_rows, me, *, e_total, ep)` — [`L1183`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L1183) — Shard `me`'s five kernel counts, one per row, [N_COUNTS, ep] i32.
- <a id="shard_expert_slabs"></a>`shard_expert_slabs(routing, me, *, e_total, ep)` — [`L982`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L982) — Shard `me`'s local experts: (rows, slab start) i32 [G], in row units.
- <a id="shard_push_tables_in_rows"></a>`shard_push_tables_in_rows(routing, me, *, e_total, ep)` — [`L1085`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L1085) — Shard `me`'s push tables in ROW units, for true-length pushes.
- <a id="shard_token_gather"></a>`shard_token_gather(routing, me, *, shard_stride, rows=None)` — [`L1011`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L1011) — The token number each of shard `me`'s slab rows computes, [stride].
- <a id="shard_transport_tables_in_blocks"></a>`shard_transport_tables_in_blocks(routing, me, *, e_total, ep)` — [`L1111`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L1111) — Shard `me`'s transport tables in ROWBLK-row block units.
- <a id="token_gather_smem_bytes"></a>`token_gather_smem_bytes(tile_m)` — [`L190`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L190) — Fixed scalar-memory footprint of the two token-gather windows.
- <a id="token_gather_window_rows"></a>`token_gather_window_rows(tile_m)` — [`L185`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L185) — Int32 rows in one aligned HBM-to-SMEM token-gather window.
- <a id="vmem_estimate_bytes"></a>`vmem_estimate_bytes(g_local, capacity, hidden, inter, nbuf, weight_format=WeightFormat.FP8, rhs_qb=QB4, has_w1_bias=False, has_w2_bias=False, info=None)` — [`L1524`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L1524) — VMEM one built kernel occupies, from the arrays it declares. — documented in [fused-moe-kernels](../../../../../../concepts/fused-moe-kernels.md)
- <a id="vmem_limit"></a>`vmem_limit(info=None)` — [`L1267`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L1267) — VMEM budget for the kernel, read from this generation's capacity.
- <a id="vmem_scratch_arrays"></a>`vmem_scratch_arrays(g_local, capacity, hidden, inter, *, nbuf, weight_format=WeightFormat.FP8, rhs_qb=QB4, has_w1_bias=False, has_w2_bias=False)` — [`L1354`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L1354) — The kernel's VMEM scratch buffers, as (name, shape, dtype). — documented in [fused-moe-kernels](../../../../../../concepts/fused-moe-kernels.md)
- <a id="vmem_tile_body_arrays"></a>`vmem_tile_body_arrays(capacity, hidden, inter, *, weight_format=WeightFormat.FP8, rhs_qb=QB4)` — [`L1458`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L1458) — What one tile body keeps live, as (name, shape, dtype). — documented in [fused-moe-kernels](../../../../../../concepts/fused-moe-kernels.md)
- <a id="weight_form"></a>`weight_form(weight_format)` — [`L347`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L347) — The record for a format; raises naming the accepted set. — documented in [fused-moe-kernels](../../../../../../concepts/fused-moe-kernels.md)
- <a id="weight_format_of_dtype"></a>`weight_format_of_dtype(dtype)` — [`L358`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L358) — The format carrying this weight element type, or None. — documented in [fused-moe-kernels](../../../../../../concepts/fused-moe-kernels.md)

## Module values
- <a id="ALIGNMENT_SLOT_FIELD"></a>`ALIGNMENT_SLOT_FIELD` — [`L110`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L110)
- <a id="BF16"></a>`BF16` — [`L38`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L38)
- <a id="COUNT_RECV_ALIGNED_ROWS"></a>`COUNT_RECV_ALIGNED_ROWS` — [`L1175`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L1175)
- <a id="COUNT_RECV_MIRROR"></a>`COUNT_RECV_MIRROR` — [`L1178`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L1178)
- <a id="COUNT_RECV_ROWS"></a>`COUNT_RECV_ROWS` — [`L1173`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L1173)
- <a id="COUNT_SELF_MIRROR"></a>`COUNT_SELF_MIRROR` — [`L1179`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L1179)
- <a id="COUNT_SEND_ALIGNED_ROWS"></a>`COUNT_SEND_ALIGNED_ROWS` — [`L1174`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L1174)
- <a id="COUNT_SEND_MIRROR"></a>`COUNT_SEND_MIRROR` — [`L1177`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L1177)
- <a id="COUNT_SEND_ROWS"></a>`COUNT_SEND_ROWS` — [`L1172`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L1172)
- <a id="COUNT_VISITS"></a>`COUNT_VISITS` — [`L1176`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L1176)
- <a id="FP4"></a>`FP4` — [`L31`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L31)
- <a id="FP8"></a>`FP8` — [`L29`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L29)
- <a id="FP8_MAX"></a>`FP8_MAX` — [`L28`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L28)
- <a id="HIDDEN_LANE_BLOCK"></a>`HIDDEN_LANE_BLOCK` — [`L92`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L92) — documented in [fused-moe-kernels](../../../../../../concepts/fused-moe-kernels.md)
- <a id="HIDDEN_MAX_BLOCKS"></a>`HIDDEN_MAX_BLOCKS` — [`L104`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L104)
- <a id="INT8"></a>`INT8` — [`L44`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L44)
- <a id="MAX_NBUF"></a>`MAX_NBUF` — [`L81`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L81)
- <a id="MAX_ROUTING_BLOCK"></a>`MAX_ROUTING_BLOCK` — [`L115`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L115)
- <a id="MAX_WEIGHT_PREFETCH_DISTANCE"></a>`MAX_WEIGHT_PREFETCH_DISTANCE` — [`L61`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L61)
- <a id="MIN_GENERATION"></a>`MIN_GENERATION` — [`L1285`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L1285)
- <a id="N_COUNTS"></a>`N_COUNTS` — [`L1180`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L1180)
- <a id="OUT_PARITIES"></a>`OUT_PARITIES` — [`L166`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L166) — documented in [fused-moe-kernels](../../../../../../concepts/fused-moe-kernels.md)
- <a id="PACK4"></a>`PACK4` — [`L37`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L37) — documented in [fused-moe-kernels](../../../../../../concepts/fused-moe-kernels.md)
- <a id="QB4"></a>`QB4` — [`L33`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L33) — documented in [fused-moe-kernels](../../../../../../concepts/fused-moe-kernels.md)
- <a id="ROUTING_WINDOW"></a>`ROUTING_WINDOW` — [`L123`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L123)
- <a id="ROUTING_WINDOW_MIN_PAIRS"></a>`ROUTING_WINDOW_MIN_PAIRS` — [`L130`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L130)
- <a id="ROWBLK"></a>`ROWBLK` — [`L89`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L89) — documented in [fused-moe-kernels](../../../../../../concepts/fused-moe-kernels.md)
- <a id="ROWBLK_SHIFT"></a>`ROWBLK_SHIFT` — [`L161`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L161)
- <a id="SLOT_FIELD_MASK"></a>`SLOT_FIELD_MASK` — [`L163`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L163)
- <a id="SLOT_FIELD_SHIFT"></a>`SLOT_FIELD_SHIFT` — [`L162`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L162)
- <a id="TOKEN_GATHER_DMA_ALIGNMENT"></a>`TOKEN_GATHER_DMA_ALIGNMENT` — [`L102`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L102)
- <a id="TOKEN_GATHER_TILES_PER_WINDOW"></a>`TOKEN_GATHER_TILES_PER_WINDOW` — [`L98`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L98)
- <a id="U32_SUBLANE_TILE"></a>`U32_SUBLANE_TILE` — [`L1325`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L1325) — documented in [fused-moe-kernels](../../../../../../concepts/fused-moe-kernels.md)
- <a id="VMEM_FRACTION"></a>`VMEM_FRACTION` — [`L106`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L106)
- <a id="WEIGHT_FORMAT_NAMES"></a>`WEIGHT_FORMAT_NAMES` — [`L344`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L344) — documented in [fused-moe-kernels](../../../../../../concepts/fused-moe-kernels.md)
- <a id="WEIGHT_FORMS"></a>`WEIGHT_FORMS` — [`L331`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L331) — documented in [fused-moe-kernels](../../../../../../concepts/fused-moe-kernels.md)
- <a id="WIDENED_BLOCK_BUFFERS"></a>`WIDENED_BLOCK_BUFFERS` — [`L170`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L170)
- <a id="WIDEN_KCHUNK"></a>`WIDEN_KCHUNK` — [`L47`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/host.py#L47) — documented in [fused-moe-kernels](../../../../../../concepts/fused-moe-kernels.md)

