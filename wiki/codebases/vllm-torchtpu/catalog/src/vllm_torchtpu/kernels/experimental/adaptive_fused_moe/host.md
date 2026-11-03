---
title: 'Module: src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.experimental.adaptive_fused_moe.host`/
symbols:
  build_routing_tables_sharded: build_routing_tables_sharded().
  build_routing_tables: build_routing_tables().
  ROWBLK: ROWBLK.
  vmem_scratch_arrays: vmem_scratch_arrays().
  HIDDEN_LANE_BLOCK: HIDDEN_LANE_BLOCK.
  WEIGHT_FORMS: WEIGHT_FORMS.
  WeightFormat: WeightFormat#
  vmem_tile_body_arrays: vmem_tile_body_arrays().
  select_weight_buffers: select_weight_buffers().
  vmem_estimate_bytes: vmem_estimate_bytes().
  FP8: FP8.
  weight_form: weight_form().
  OUT_PARITIES: OUT_PARITIES.
  WIDEN_KCHUNK: WIDEN_KCHUNK.
  U32_SUBLANE_TILE: U32_SUBLANE_TILE.
  weight_format_of_dtype: weight_format_of_dtype().
  PACK4: PACK4.
  align_up: align_up().
  WeightForm.has_scales: WeightForm#has_scales().
  QB4: QB4.
  ALIGNMENT_SLOT_FIELD: ALIGNMENT_SLOT_FIELD.
  WeightForm.quantized_activations: WeightForm#quantized_activations().
  pow2_shift: pow2_shift().
  token_gather_window_rows: token_gather_window_rows().
  act_scale_slab_rows: act_scale_slab_rows().
  shard_transport_tables_in_blocks.i32: shard_transport_tables_in_blocks().i32().
  BF16: BF16.
  ROWBLK_SHIFT: ROWBLK_SHIFT.
  WeightFormat.FP8: WeightFormat#FP8.
  ragged_stride_bound: ragged_stride_bound().
  shard_count_vector.over_experts: shard_count_vector().over_experts().
  act_scale_window_rows: act_scale_window_rows().
  WeightFormat.FP4: WeightFormat#FP4.
  _lookup_per_pair: _lookup_per_pair().
  _refuse_bad_plan_args: _refuse_bad_plan_args().
  shard_token_gather: shard_token_gather().
  shard_transport_tables_in_blocks: shard_transport_tables_in_blocks().
  NBUF: NBUF.
  SLOT_FIELD_SHIFT: SLOT_FIELD_SHIFT.
  WeightFormat.INT8: WeightFormat#INT8.
  off_shard_slab_row: off_shard_slab_row().
  rank_window: rank_window().
  _rank_within_window: _rank_within_window().
  _lookup_per_sub_pair: _lookup_per_sub_pair().
  TOKEN_GATHER_DMA_ALIGNMENT: TOKEN_GATHER_DMA_ALIGNMENT.
  routing_block: routing_block().
  vmem_limit: vmem_limit().
  WeightForm.scale_layout: WeightForm#scale_layout.
  ShardRoutingTables.pair_grid: ShardRoutingTables#pair_grid().
  mirror_run_tiles: mirror_run_tiles().
  row_lane_blocks: row_lane_blocks().
  WEIGHT_FORMAT_NAMES: WEIGHT_FORMAT_NAMES.
  pair_block_hist: pair_block_hist().
  shard_count_vector: shard_count_vector().
  FP8_MAX: FP8_MAX.
  FP4: FP4.
  WeightFormat.BF16: WeightFormat#BF16.
  WeightForm: WeightForm#
  WeightForm.weight_dtype: WeightForm#weight_dtype.
  WeightForm.wire_dtype: WeightForm#wire_dtype.
  SLOT_FIELD_MASK: SLOT_FIELD_MASK.
  token_gather_smem_bytes: token_gather_smem_bytes().
  _window_hist: _window_hist().
  array_vmem_bytes: array_vmem_bytes().
  check_u32_sublane_tile: check_u32_sublane_tile().
  MAX_ROUTING_BLOCK: MAX_ROUTING_BLOCK.
  _block_hist: _block_hist().
  local_slab_rows: local_slab_rows().
  MIN_GENERATION: MIN_GENERATION.
  chip_generation: chip_generation().
  WeightForm.name: WeightForm#name.
  RoutingTables.pair_grid: RoutingTables#pair_grid().
  TOKEN_GATHER_TILES_PER_WINDOW: TOKEN_GATHER_TILES_PER_WINDOW.
  VMEM_FRACTION: VMEM_FRACTION.
  WIDENED_BLOCK_BUFFERS: WIDENED_BLOCK_BUFFERS.
  RoutingTables.arrival_row: RoutingTables#arrival_row.
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
  WeightBufferPlan: WeightBufferPlan#
  WeightBufferPlan.w1_nbuf: WeightBufferPlan#w1_nbuf.
  WeightBufferPlan.w2_nbuf: WeightBufferPlan#w2_nbuf.
  INT8: INT8.
  WEIGHT_PREFETCH_DISTANCE: WEIGHT_PREFETCH_DISTANCE.
  ROUTING_WINDOW: ROUTING_WINDOW.
  ROUTING_WINDOW_MIN_PAIRS: ROUTING_WINDOW_MIN_PAIRS.
  contrib_mirror_rows: contrib_mirror_rows().
  arrival_mirror_rows: arrival_mirror_rows().
  WeightForm.act_dtype: WeightForm#act_dtype.
  WeightForm.act_max: WeightForm#act_max.
  gather_clamp_bounds: gather_clamp_bounds().
  RoutingTables: RoutingTables#
  RoutingTables.mirror_row: RoutingTables#mirror_row.
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
  ShardRoutingTables: ShardRoutingTables#
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
  WeightBufferPlan.vmem_bytes: WeightBufferPlan#vmem_bytes.
  WeightFormat.__str__: WeightFormat#__str__().
  WeightFormat.__repr__: WeightFormat#__repr__().
  COUNT_SEND_ALIGNED_ROWS: COUNT_SEND_ALIGNED_ROWS.
  COUNT_RECV_ALIGNED_ROWS: COUNT_RECV_ALIGNED_ROWS.
  N_COUNTS: N_COUNTS.
---
# Module: [`src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py)

## Classes
### <a id="GatheredPairs"></a>`GatheredPairs`  ·  implements/extends NamedTuple
- def: [`src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py:769`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L769)
- doc: The routing exchange, already unpacked by the caller.
- signature: `class GatheredPairs(NamedTuple):`
- members:
  - <a id="GatheredPairs.block_hist"></a>`block_hist` — [`L783`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L783)
  - <a id="GatheredPairs.expert_blocks"></a>`expert_blocks` — [`L781`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L781)
  - <a id="GatheredPairs.local_blocks"></a>`local_blocks` — [`L782`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L782)
  - <a id="GatheredPairs.n_tokens"></a>`n_tokens` — [`L785`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L785)
  - <a id="GatheredPairs.rows_by_dest"></a>`rows_by_dest` — [`L784`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L784)
  - <a id="GatheredPairs.topk"></a>`topk` — [`L786`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L786)
- used by: [`local_fn`](layer.md#adaptive_fused_moe.local_fn)

### <a id="RoutingTables"></a>`RoutingTables`  ·  implements/extends NamedTuple
- def: [`src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py:392`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L392)
- doc: Where every routed (token, expert) pair computes, and where it lands.
- signature: `class RoutingTables(NamedTuple):`
- members:
  - <a id="RoutingTables.pair_grid"></a>`pair_grid(self)` — [`L428`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L428) — (tokens, selections) the plan was built over.
  - <a id="RoutingTables.arrival_row"></a>`arrival_row` — [`L401`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L401)
  - <a id="RoutingTables.expert_base"></a>`expert_base` — [`L423`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L423)
  - <a id="RoutingTables.expert_rows_aligned"></a>`expert_rows_aligned` — [`L421`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L421)
  - <a id="RoutingTables.mirror_row"></a>`mirror_row` — [`L403`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L403)
  - <a id="RoutingTables.recv_base"></a>`recv_base` — [`L417`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L417)
  - <a id="RoutingTables.recv_rows"></a>`recv_rows` — [`L419`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L419)
  - <a id="RoutingTables.region_rows"></a>`region_rows` — [`L415`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L415)
  - <a id="RoutingTables.rows_alloc"></a>`rows_alloc` — [`L425`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L425)
  - <a id="RoutingTables.run_rows"></a>`run_rows` — [`L409`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L409)
  - <a id="RoutingTables.run_rows_aligned"></a>`run_rows_aligned` — [`L411`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L411)
  - <a id="RoutingTables.run_start_aligned"></a>`run_start_aligned` — [`L413`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L413)
  - <a id="RoutingTables.run_tiles"></a>`run_tiles` — [`L405`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L405)
  - <a id="RoutingTables.slab_row"></a>`slab_row` — [`L407`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L407)
- used by: [`build_routing_tables`](host.md#build_routing_tables)

### <a id="ShardRoutingTables"></a>`ShardRoutingTables`  ·  implements/extends NamedTuple
- def: [`src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py:606`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L606)
- doc: One shard's complementary slices of the routing plan.
- signature: `class ShardRoutingTables(NamedTuple):`
- members:
  - <a id="ShardRoutingTables.pair_grid"></a>`pair_grid(self)` — [`L633`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L633)
  - <a id="ShardRoutingTables.expert_base"></a>`expert_base` — [`L627`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L627)
  - <a id="ShardRoutingTables.expert_rows_aligned"></a>`expert_rows_aligned` — [`L626`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L626)
  - <a id="ShardRoutingTables.mirror_pos"></a>`mirror_pos` — [`L617`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L617)
  - <a id="ShardRoutingTables.n_tokens"></a>`n_tokens` — [`L629`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L629)
  - <a id="ShardRoutingTables.pos"></a>`pos` — [`L616`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L616)
  - <a id="ShardRoutingTables.recv_base"></a>`recv_base` — [`L624`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L624)
  - <a id="ShardRoutingTables.recv_rows"></a>`recv_rows` — [`L625`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L625)
  - <a id="ShardRoutingTables.region_rows"></a>`region_rows` — [`L623`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L623)
  - <a id="ShardRoutingTables.rows_alloc"></a>`rows_alloc` — [`L628`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L628)
  - <a id="ShardRoutingTables.run_rows"></a>`run_rows` — [`L620`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L620)
  - <a id="ShardRoutingTables.run_rows_aligned"></a>`run_rows_aligned` — [`L621`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L621)
  - <a id="ShardRoutingTables.run_start_aligned"></a>`run_start_aligned` — [`L622`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L622)
  - <a id="ShardRoutingTables.run_tiles"></a>`run_tiles` — [`L618`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L618)
  - <a id="ShardRoutingTables.slab_row"></a>`slab_row` — [`L619`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L619)
  - <a id="ShardRoutingTables.topk"></a>`topk` — [`L630`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L630)
- used by: [`local_fn`](layer.md#adaptive_fused_moe.local_fn), [`build_routing_tables_sharded`](host.md#build_routing_tables_sharded)

### <a id="WeightBufferPlan"></a>`WeightBufferPlan`  ·  implements/extends NamedTuple
- def: [`src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py:1528`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L1528)
- signature: `class WeightBufferPlan(NamedTuple):`
- members:
  - <a id="WeightBufferPlan.vmem_bytes"></a>`vmem_bytes` — [`L1531`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L1531)
  - <a id="WeightBufferPlan.w1_nbuf"></a>`w1_nbuf` — [`L1529`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L1529)
  - <a id="WeightBufferPlan.w2_nbuf"></a>`w2_nbuf` — [`L1530`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L1530)
- used by: [`_build_fused_ep_moe_kernel`](kernel.md#_build_fused_ep_moe_kernel), [`prebuild_adaptive_fused_moe`](vllm_adapter.md#prebuild_adaptive_fused_moe), [`select_weight_buffers`](host.md#select_weight_buffers), [`WeightBufferPlan`](__init__.md#WeightBufferPlan)

### <a id="WeightForm"></a>`WeightForm`  ·  implements/extends NamedTuple
- def: [`src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py:247`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L247)
- doc: One weight format the kernel takes, and everything that follows it.
- signature: `class WeightForm(NamedTuple):`
- members:
  - <a id="WeightForm.has_scales"></a>`has_scales(self)` — [`L274`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L274) — Whether the caller supplies weight scales at all. — documented in [adaptive-fused-moe-kernel](../../../../../../concepts/adaptive-fused-moe-kernel.md)
  - <a id="WeightForm.quantized_activations"></a>`quantized_activations(self)` — [`L279`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L279) — Whether token rows are quantized, and so carry a row scale. — documented in [adaptive-fused-moe-kernel](../../../../../../concepts/adaptive-fused-moe-kernel.md)
  - <a id="WeightForm.act_dtype"></a>`act_dtype` — [`L268`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L268)
  - <a id="WeightForm.act_max"></a>`act_max` — [`L269`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L269)
  - <a id="WeightForm.name"></a>`name` — [`L266`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L266)
  - <a id="WeightForm.scale_layout"></a>`scale_layout` — [`L270`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L270)
  - <a id="WeightForm.weight_dtype"></a>`weight_dtype` — [`L267`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L267)
  - <a id="WeightForm.wire_dtype"></a>`wire_dtype` — [`L271`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L271)
- uses (calls/refs, reference-scoped): [`WeightFormat`](host.md#WeightFormat)
- used by: [`local_fn`](layer.md#adaptive_fused_moe.local_fn), [`_build_fused_ep_moe_kernel`](kernel.md#_build_fused_ep_moe_kernel), [`adaptive_fused_moe`](layer.md#adaptive_fused_moe), [`compute_tile`](kernel.md#_build_fused_ep_moe_kernel.kernel.expert_tiles.tile_body.compute_tile), [`vmem_scratch_arrays`](host.md#vmem_scratch_arrays), [`make_call`](kernel.md#_build_fused_ep_moe_kernel.make_call), [`WEIGHT_FORMS`](host.md#WEIGHT_FORMS), [`vmem_tile_body_arrays`](host.md#vmem_tile_body_arrays), [`weight_format_of_dtype`](host.md#weight_format_of_dtype)

### <a id="WeightFormat"></a>`WeightFormat`  ·  implements/extends Enum, str
- def: [`src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py:223`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L223) — documented in [adaptive-fused-moe-kernel](../../../../../../concepts/adaptive-fused-moe-kernel.md)
- doc: The weight formats the kernel takes, one member per accepted form.
- signature: `class WeightFormat(str, enum.Enum):`
- members:
  - <a id="WeightFormat.BF16"></a>`BF16` — [`L238`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L238)
  - <a id="WeightFormat.FP4"></a>`FP4` — [`L236`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L236)
  - <a id="WeightFormat.FP8"></a>`FP8` — [`L235`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L235) — documented in [adaptive-fused-moe-kernel](../../../../../../concepts/adaptive-fused-moe-kernel.md)
  - <a id="WeightFormat.INT8"></a>`INT8` — [`L237`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L237)
- protocol/private: <a id="WeightFormat.__repr__"></a>`__repr__`[`L243`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L243), <a id="WeightFormat.__str__"></a>`__str__`[`L240`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L240)
- used by: [`_build_fused_ep_moe_kernel`](kernel.md#_build_fused_ep_moe_kernel), [`adaptive_fused_moe`](layer.md#adaptive_fused_moe), [`compute_tile`](kernel.md#_build_fused_ep_moe_kernel.kernel.expert_tiles.tile_body.compute_tile), [`vmem_scratch_arrays`](host.md#vmem_scratch_arrays), [`make_call`](kernel.md#_build_fused_ep_moe_kernel.make_call), [`WEIGHT_FORMS`](host.md#WEIGHT_FORMS), [`vmem_tile_body_arrays`](host.md#vmem_tile_body_arrays), [`select_weight_buffers`](host.md#select_weight_buffers), [`vmem_estimate_bytes`](host.md#vmem_estimate_bytes), [`weight_form`](host.md#weight_form), [`weight_format_of_dtype`](host.md#weight_format_of_dtype), [`moe`](vllm_adapter.md#_build_op.moe), [`WeightFormat`](__init__.md#WeightFormat), [`name`](host.md#WeightForm.name)

## Functions
- <a id="_block_hist"></a>`_block_hist(expert_blocks, bins)` — [`L649`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L649) — Number of pairs per routing block and expert bin.
- <a id="_lookup_per_pair"></a>`_lookup_per_pair(table, expert_blocks, bins)` — [`L433`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L433) — ``table[b, expert_blocks[b, i]]`` -- one value per routed pair.
- <a id="_lookup_per_sub_pair"></a>`_lookup_per_sub_pair(table, expert_blocks, bins, window)` — [`L750`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L750) — ``table[b, i // window, expert_blocks[b, i]]`` -- one value per pair.
- <a id="_over_sub_blocks"></a>`_over_sub_blocks(window_hist)` — [`L725`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L725) — The per-block histogram a sub-block histogram refines.
- <a id="_per_sub_block"></a>`_per_sub_block(x, window)` — [`L671`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L671) — ``x[b, sub, ...]`` read back as ``x[b, pair, ...]``.
- <a id="_rank_within_block"></a>`_rank_within_block(expert_blocks, block)` — [`L642`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L642) — ``#{j < i : e_j == e_i}`` for each pair in a routing block.
- <a id="_rank_within_window"></a>`_rank_within_window(expert_blocks, window)` — [`L686`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L686) — ``#{j < i : e_j == e_i}`` over i's sub-block rather than its block.
- <a id="_refuse_bad_plan_args"></a>`_refuse_bad_plan_args(T, K, *, e_total, ep, t_local, block, tile_m)` — [`L448`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L448) — Argument checks shared by the replicated and sharded plan builders.
- <a id="_window_hist"></a>`_window_hist(expert_blocks, bins, window)` — [`L710`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L710) — Pairs per (routing block, sub-block, expert bin).
- <a id="_window_table"></a>`_window_table(table, window_hist)` — [`L730`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L730) — A per-block plan table resolved per sub-block, for the lookup.
- <a id="act_scale_slab_rows"></a>`act_scale_slab_rows(rows_alloc)` — [`L197`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L197) — Sublanes the activation row-scale slab is handed to the kernel as. — documented in [adaptive-fused-moe-kernel](../../../../../../concepts/adaptive-fused-moe-kernel.md)
- <a id="act_scale_window_rows"></a>`act_scale_window_rows(tile_m)` — [`L218`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L218) — Sublanes of the scale slab one tile of `tile_m` rows can touch.
- <a id="align_up"></a>`align_up(v, m)` — [`L150`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L150)
- <a id="array_vmem_bytes"></a>`array_vmem_bytes(shape, dtype, info)` — [`L1256`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L1256) — Bytes one VMEM array of this shape and dtype occupies.
- <a id="arrival_mirror_rows"></a>`arrival_mirror_rows(recv_rows, e_total, tile_m)` — [`L187`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L187) — Sublanes the arrival mirror needs, on the same slack rule.
- <a id="build_routing_tables"></a>`build_routing_tables(topk_idx, *, e_total, ep, t_local, block, tile_m, shard_stride)` — [`L491`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L491) — Assign every routed (token, expert) pair the slab row it computes on. — documented in [adaptive-fused-moe-kernel](../../../../../../concepts/adaptive-fused-moe-kernel.md)
- <a id="build_routing_tables_sharded"></a>`build_routing_tables_sharded(topk_idx, me, *, e_total, ep, t_local, block, tile_m, shard_stride, all_gather_rows=None, gathered=None)` — [`L789`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L789) — Build only the routing-plan slices consumed by shard ``me``. — documented in [adaptive-fused-moe-kernel](../../../../../../concepts/adaptive-fused-moe-kernel.md)
- <a id="check_u32_sublane_tile"></a>`check_u32_sublane_tile(info=None)` — [`L1284`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L1284) — Refuse a chip whose 32-bit sublane tiling is not the one the packed
- <a id="chip_generation"></a>`chip_generation(info=None)` — [`L1244`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L1244) — The generation of the chip this build is for.
- <a id="contrib_mirror_rows"></a>`contrib_mirror_rows(rows_alloc, g_local, tile_m)` — [`L175`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L175) — Sublanes the contribution mirror needs.
- <a id="expert_visit_list"></a>`expert_visit_list(rows, g_local)` — [`L1016`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L1016) — The local experts to visit, and how many, from rows [g_local] i32.
- <a id="gather_clamp_bounds"></a>`gather_clamp_bounds(T)` — [`L364`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L364) — The (low, high) token numbers the routing gather table is clipped to.
- <a id="shard_transport_tables_in_blocks.i32"></a>`i32(a)` — [`L1117`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L1117) — One table in block units: the row count's high bits.
- <a id="local_slab_rows"></a>`local_slab_rows(routing, me, *, shard_stride)` — [`L955`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L955) — `routing.slab_row` rebased onto shard `me`'s own slab.
- <a id="mirror_run_tiles"></a>`mirror_run_tiles(run_start, run_rows, tile_m)` — [`L164`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L164) — Mirror sublanes a run owns: the source tiles its rows fall in.
- <a id="off_shard_slab_row"></a>`off_shard_slab_row(shard_stride, ep)` — [`L637`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L637) — Sentinel beyond both slab destinations after any shard rebasing.
- <a id="shard_count_vector.over_experts"></a>`over_experts(term)` — [`L1205`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L1205) — One count's reduction, keeping the expert-parallel axis.
- <a id="pair_block_hist"></a>`pair_block_hist(expert_blocks, e_total)` — [`L656`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L656) — Pairs per routing block and expert, over ``e_total`` bins.
- <a id="pow2_shift"></a>`pow2_shift(m, what)` — [`L102`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L102) — The shift a division by `m` is, refusing anything else by name. — documented in [adaptive-fused-moe-kernel](../../../../../../concepts/adaptive-fused-moe-kernel.md)
- <a id="ragged_stride_bound"></a>`ragged_stride_bound(num_tokens, topk, e_total, capacity)` — [`L340`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L340) — Per-shard slab rows the no-drop worst case needs: every routed row
- <a id="rank_window"></a>`rank_window(block, shard_pairs)` — [`L661`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L661) — The width the rank pass self-compares over, `block` where it pays.
- <a id="routing_block"></a>`routing_block(t_local, topk)` — [`L384`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L384) — The widest power-of-two block dividing this shard's routed pairs.
- <a id="row_lane_blocks"></a>`row_lane_blocks(hidden)` — [`L192`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L192) — Lane blocks one token row is staged as: a row is (this many, 128).
- <a id="select_weight_buffers"></a>`select_weight_buffers(g_local, capacity, hidden, inter, *, weight_format=WeightFormat.FP8, rhs_qb=QB4, has_w1_bias=False, has_w2_bias=False, info=None)` — [`L1534`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L1534) — Choose the deepest supported W1/W2 rings that fit the VMEM budget. — documented in [adaptive-fused-moe-kernel](../../../../../../concepts/adaptive-fused-moe-kernel.md)
- <a id="shard_count_vector"></a>`shard_count_vector(routing, expert_rows, me, *, e_total, ep)` — [`L1146`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L1146) — Shard `me`'s five kernel counts, one per row, [N_COUNTS, ep] i32.
- <a id="shard_expert_slabs"></a>`shard_expert_slabs(routing, me, *, e_total, ep)` — [`L946`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L946) — Shard `me`'s local experts: (rows, slab start) i32 [G], in row units.
- <a id="shard_push_tables_in_rows"></a>`shard_push_tables_in_rows(routing, me, *, e_total, ep)` — [`L1048`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L1048) — Shard `me`'s push tables in ROW units, for true-length pushes.
- <a id="shard_token_gather"></a>`shard_token_gather(routing, me, *, shard_stride, rows=None)` — [`L975`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L975) — The token number each of shard `me`'s slab rows computes, [stride].
- <a id="shard_transport_tables_in_blocks"></a>`shard_transport_tables_in_blocks(routing, me, *, e_total, ep)` — [`L1074`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L1074) — Shard `me`'s transport tables in ROWBLK-row block units.
- <a id="token_gather_smem_bytes"></a>`token_gather_smem_bytes(tile_m)` — [`L159`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L159) — Fixed scalar-memory footprint of the two token-gather windows.
- <a id="token_gather_window_rows"></a>`token_gather_window_rows(tile_m)` — [`L154`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L154) — Int32 rows in one aligned HBM-to-SMEM token-gather window. — documented in [adaptive-fused-moe-kernel](../../../../../../concepts/adaptive-fused-moe-kernel.md)
- <a id="vmem_estimate_bytes"></a>`vmem_estimate_bytes(g_local, capacity, hidden, inter, nbuf=NBUF, weight_format=WeightFormat.FP8, rhs_qb=QB4, has_w1_bias=False, has_w2_bias=False, info=None, w2_nbuf=None)` — [`L1483`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L1483) — VMEM one built kernel occupies, from the arrays it declares. — documented in [adaptive-fused-moe-kernel](../../../../../../concepts/adaptive-fused-moe-kernel.md)
- <a id="vmem_limit"></a>`vmem_limit()` — [`L1230`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L1230) — VMEM budget for the kernel, read from this generation's capacity.
- <a id="vmem_scratch_arrays"></a>`vmem_scratch_arrays(g_local, capacity, hidden, inter, *, nbuf=NBUF, w2_nbuf=None, weight_format=WeightFormat.FP8, rhs_qb=QB4, has_w1_bias=False, has_w2_bias=False)` — [`L1310`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L1310) — The kernel's VMEM scratch buffers, as (name, shape, dtype). — documented in [adaptive-fused-moe-kernel](../../../../../../concepts/adaptive-fused-moe-kernel.md)
- <a id="vmem_tile_body_arrays"></a>`vmem_tile_body_arrays(capacity, hidden, inter, *, weight_format=WeightFormat.FP8, rhs_qb=QB4)` — [`L1417`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L1417) — What one tile body keeps live, as (name, shape, dtype). — documented in [adaptive-fused-moe-kernel](../../../../../../concepts/adaptive-fused-moe-kernel.md)
- <a id="weight_form"></a>`weight_form(weight_format)` — [`L316`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L316) — The record for a format; raises naming the accepted set. — documented in [adaptive-fused-moe-kernel](../../../../../../concepts/adaptive-fused-moe-kernel.md)
- <a id="weight_format_of_dtype"></a>`weight_format_of_dtype(dtype)` — [`L327`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L327) — The format carrying this weight element type, or None.

## Module values
- <a id="ALIGNMENT_SLOT_FIELD"></a>`ALIGNMENT_SLOT_FIELD` — [`L79`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L79)
- <a id="BF16"></a>`BF16` — [`L38`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L38)
- <a id="COUNT_RECV_ALIGNED_ROWS"></a>`COUNT_RECV_ALIGNED_ROWS` — [`L1138`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L1138)
- <a id="COUNT_RECV_MIRROR"></a>`COUNT_RECV_MIRROR` — [`L1141`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L1141)
- <a id="COUNT_RECV_ROWS"></a>`COUNT_RECV_ROWS` — [`L1136`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L1136)
- <a id="COUNT_SELF_MIRROR"></a>`COUNT_SELF_MIRROR` — [`L1142`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L1142)
- <a id="COUNT_SEND_ALIGNED_ROWS"></a>`COUNT_SEND_ALIGNED_ROWS` — [`L1137`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L1137)
- <a id="COUNT_SEND_MIRROR"></a>`COUNT_SEND_MIRROR` — [`L1140`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L1140)
- <a id="COUNT_SEND_ROWS"></a>`COUNT_SEND_ROWS` — [`L1135`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L1135)
- <a id="COUNT_VISITS"></a>`COUNT_VISITS` — [`L1139`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L1139)
- <a id="FP4"></a>`FP4` — [`L31`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L31)
- <a id="FP8"></a>`FP8` — [`L29`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L29)
- <a id="FP8_MAX"></a>`FP8_MAX` — [`L28`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L28)
- <a id="HIDDEN_LANE_BLOCK"></a>`HIDDEN_LANE_BLOCK` — [`L63`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L63) — documented in [adaptive-fused-moe-kernel](../../../../../../concepts/adaptive-fused-moe-kernel.md)
- <a id="INT8"></a>`INT8` — [`L44`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L44)
- <a id="MAX_ROUTING_BLOCK"></a>`MAX_ROUTING_BLOCK` — [`L84`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L84)
- <a id="MIN_GENERATION"></a>`MIN_GENERATION` — [`L1241`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L1241)
- <a id="NBUF"></a>`NBUF` — [`L52`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L52)
- <a id="N_COUNTS"></a>`N_COUNTS` — [`L1143`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L1143)
- <a id="OUT_PARITIES"></a>`OUT_PARITIES` — [`L135`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L135) — documented in [adaptive-fused-moe-kernel](../../../../../../concepts/adaptive-fused-moe-kernel.md)
- <a id="PACK4"></a>`PACK4` — [`L37`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L37) — documented in [adaptive-fused-moe-kernel](../../../../../../concepts/adaptive-fused-moe-kernel.md)
- <a id="QB4"></a>`QB4` — [`L33`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L33) — documented in [adaptive-fused-moe-kernel](../../../../../../concepts/adaptive-fused-moe-kernel.md)
- <a id="ROUTING_WINDOW"></a>`ROUTING_WINDOW` — [`L92`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L92)
- <a id="ROUTING_WINDOW_MIN_PAIRS"></a>`ROUTING_WINDOW_MIN_PAIRS` — [`L99`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L99)
- <a id="ROWBLK"></a>`ROWBLK` — [`L60`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L60) — documented in [adaptive-fused-moe-kernel](../../../../../../concepts/adaptive-fused-moe-kernel.md)
- <a id="ROWBLK_SHIFT"></a>`ROWBLK_SHIFT` — [`L130`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L130)
- <a id="SLOT_FIELD_MASK"></a>`SLOT_FIELD_MASK` — [`L132`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L132)
- <a id="SLOT_FIELD_SHIFT"></a>`SLOT_FIELD_SHIFT` — [`L131`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L131)
- <a id="TOKEN_GATHER_DMA_ALIGNMENT"></a>`TOKEN_GATHER_DMA_ALIGNMENT` — [`L73`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L73)
- <a id="TOKEN_GATHER_TILES_PER_WINDOW"></a>`TOKEN_GATHER_TILES_PER_WINDOW` — [`L69`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L69)
- <a id="U32_SUBLANE_TILE"></a>`U32_SUBLANE_TILE` — [`L1281`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L1281) — documented in [adaptive-fused-moe-kernel](../../../../../../concepts/adaptive-fused-moe-kernel.md)
- <a id="VMEM_FRACTION"></a>`VMEM_FRACTION` — [`L75`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L75)
- <a id="WEIGHT_FORMAT_NAMES"></a>`WEIGHT_FORMAT_NAMES` — [`L313`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L313)
- <a id="WEIGHT_FORMS"></a>`WEIGHT_FORMS` — [`L300`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L300) — documented in [adaptive-fused-moe-kernel](../../../../../../concepts/adaptive-fused-moe-kernel.md)
- <a id="WEIGHT_PREFETCH_DISTANCE"></a>`WEIGHT_PREFETCH_DISTANCE` — [`L50`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L50)
- <a id="WIDENED_BLOCK_BUFFERS"></a>`WIDENED_BLOCK_BUFFERS` — [`L139`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L139)
- <a id="WIDEN_KCHUNK"></a>`WIDEN_KCHUNK` — [`L47`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/host.py#L47) — documented in [adaptive-fused-moe-kernel](../../../../../../concepts/adaptive-fused-moe-kernel.md)

