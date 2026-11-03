---
title: 'Module: src/vllm_torchtpu/kernels/megablox/gmm_v2.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/megablox/gmm_v2.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.megablox.gmm_v2`/
symbols:
  gmm_v2: gmm_v2().
  kernel_main: kernel_main().
  inner_kernel._matmul: inner_kernel()._matmul().
  generate_block_specs: generate_block_specs().
  make_gmm_configs: make_gmm_configs().
  calculate_tiling: calculate_tiling().
  get_cost_estimate: get_cost_estimate().
  GmmConfigs.tiles: GmmConfigs#tiles.
  GmmConfigs.dims: GmmConfigs#dims.
  get_scope_name: get_scope_name().
  inner_kernel: inner_kernel().
  Dimensions.size_lhs_sublane: Dimensions#size_lhs_sublane.
  IndexMaps.rhs_scale_index_map: IndexMaps#rhs_scale_index_map().
  validate_inputs: validate_inputs().
  GmmConfigs.rhs_cfgs: GmmConfigs#rhs_cfgs.
  calculate_tiling._gmm_vmem_estimate: calculate_tiling()._gmm_vmem_estimate().
  inner_kernel.run_matmul_step: inner_kernel().run_matmul_step().
  fill_metadata: fill_metadata().
  fill_metadata.inner_tm_loop: fill_metadata().inner_tm_loop().
  zero_out_start: zero_out_start().
  TileSizes.tile_k: TileSizes#tile_k.
  IndexMaps.lhs_index_map: IndexMaps#lhs_index_map().
  IndexMaps.out_index_map: IndexMaps#out_index_map().
  fill_metadata.outer_group_loop: fill_metadata().outer_group_loop().
  InputConfigs.quant_dtype: InputConfigs#quant_dtype.
  InputConfigs.quant_block_size: InputConfigs#quant_block_size.
  GmmConfigs.num_quant_blocks_per_tile_k: GmmConfigs#num_quant_blocks_per_tile_k().
  GmmConfigs.out_size_n: GmmConfigs#out_size_n().
  MetadataRef.gm_id_to_m_offset: MetadataRef#gm_id_to_m_offset.
  Dimensions.size_k: Dimensions#size_k.
  apply_act_fn: apply_act_fn().
  TileSizes.tile_n: TileSizes#tile_n.
  InputConfigs.dtype: InputConfigs#dtype.
  GmmConfigs.lhs_cfgs: GmmConfigs#lhs_cfgs.
  FusedWeightsRef.get_weight: FusedWeightsRef#get_weight().
  FusedWeightsRef.get_scale: FusedWeightsRef#get_scale().
  FusedWeightsRef.get_bias: FusedWeightsRef#get_bias().
  TileSizes.tile_m: TileSizes#tile_m.
  Dimensions.size_m: Dimensions#size_m.
  Dimensions.size_n: Dimensions#size_n.
  WeightsRef: WeightsRef#
  TileFn: TileFn.
  GmmConfigs: GmmConfigs#
  InputConfigs.should_unpack: InputConfigs#should_unpack().
  RhsRef: RhsRef#
  RhsRef.get_scale: RhsRef#get_scale().
  InputConfigs: InputConfigs#
  InputConfigs.should_dequantize_after_matmul: InputConfigs#should_dequantize_after_matmul().
  InputConfigs.should_quantize: InputConfigs#should_quantize().
  IndexMaps.cfgs: IndexMaps#cfgs.
  FusedWeightsRef.gate: FusedWeightsRef#gate.
  FusedWeightsRef.up: FusedWeightsRef#up.
  align_to: align_to().
  MetadataRef: MetadataRef#
  TileSizes: TileSizes#
  Dimensions: Dimensions#
  Dimensions.size_group: Dimensions#size_group.
  InputConfigs.should_dequantize_before_matmul: InputConfigs#should_dequantize_before_matmul().
  IndexMaps.metadata_ref: IndexMaps#metadata_ref.
  RhsRef.get_weight: RhsRef#get_weight().
  RhsRef.get_bias: RhsRef#get_bias().
  WeightsRef.scale: WeightsRef#scale.
  InputConfigs.has_scale: InputConfigs#has_scale.
  GmmConfigs.out_dtype: GmmConfigs#out_dtype.
  GmmConfigs.fuse_act: GmmConfigs#fuse_act.
  IndexMaps.rhs_weight_index_map: IndexMaps#rhs_weight_index_map().
  IndexMaps.rhs_bias_index_map: IndexMaps#rhs_bias_index_map().
  zero_out_end: zero_out_end().
  swigluoai: swigluoai().
  get_packing_factor: get_packing_factor().
  WeightsRef.weight: WeightsRef#weight.
  WeightsRef.bias: WeightsRef#bias.
  MetadataRef.gm_id_to_group_id: MetadataRef#gm_id_to_group_id.
  InputConfigs.has_bias: InputConfigs#has_bias.
  IndexMaps.__init__: IndexMaps#__init__().
  WeightsRef.get_weight: WeightsRef#get_weight().
  WeightsRef.get_scale: WeightsRef#get_scale().
  WeightsRef.get_bias: WeightsRef#get_bias().
  FusedWeightsRef: FusedWeightsRef#
  inner_kernel.run_matmul_step.matmul_first_last: inner_kernel().run_matmul_step().matmul_first_last().
  inner_kernel.run_matmul_step.matmul_last: inner_kernel().run_matmul_step().matmul_last().
  TileSizes.bucket_base: TileSizes#bucket_base.
  GmmConfigs.zero_init: GmmConfigs#zero_init.
  inner_kernel.run_matmul_step.matmul_first: inner_kernel().run_matmul_step().matmul_first().
  inner_kernel.run_matmul_step.matmul_mid: inner_kernel().run_matmul_step().matmul_mid().
  zero_out_start.left_fill_zero: zero_out_start().left_fill_zero().
  zero_out_start.right_fill_zero: zero_out_start().right_fill_zero().
  calculate_tiling._is_tile_k_quant_block_compatible: calculate_tiling()._is_tile_k_quant_block_compatible().
  get_metadata: get_metadata().
  silu_and_mul_with_clamp: silu_and_mul_with_clamp().
  interleave_lane: interleave_lane().
  _get_lhs_sublane_size: _get_lhs_sublane_size().
  GmmConfigs.acc_dtype: GmmConfigs#acc_dtype.
  zero_out_start.fill_zero: zero_out_start().fill_zero().
  situ_and_mul: situ_and_mul().
  deinterleave_lane: deinterleave_lane().
  Dimensions.size_lhs_group: Dimensions#size_lhs_group.
  IndexMaps: IndexMaps#
---
# Module: [`src/vllm_torchtpu/kernels/megablox/gmm_v2.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py)

## Classes
### <a id="Dimensions"></a>`Dimensions`
- def: [`src/vllm_torchtpu/kernels/megablox/gmm_v2.py:232`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L232)
- signature: `class Dimensions:`
- members:
  - <a id="Dimensions.size_group"></a>`size_group` — [`L236`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L236)
  - <a id="Dimensions.size_k"></a>`size_k` — [`L234`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L234)
  - <a id="Dimensions.size_lhs_group"></a>`size_lhs_group` — [`L237`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L237)
  - <a id="Dimensions.size_lhs_sublane"></a>`size_lhs_sublane` — [`L238`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L238)
  - <a id="Dimensions.size_m"></a>`size_m` — [`L233`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L233)
  - <a id="Dimensions.size_n"></a>`size_n` — [`L235`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L235)
- used by: [`gmm_v2`](gmm_v2.md#gmm_v2), [`kernel_main`](gmm_v2.md#kernel_main), [`_matmul`](gmm_v2.md#inner_kernel._matmul), [`generate_block_specs`](gmm_v2.md#generate_block_specs), [`make_gmm_configs`](gmm_v2.md#make_gmm_configs), [`calculate_tiling`](gmm_v2.md#calculate_tiling), [`get_cost_estimate`](gmm_v2.md#get_cost_estimate), [`dims`](gmm_v2.md#GmmConfigs.dims), [`get_scope_name`](gmm_v2.md#get_scope_name), [`inner_kernel`](gmm_v2.md#inner_kernel), [`validate_inputs`](gmm_v2.md#validate_inputs), [`fill_metadata`](gmm_v2.md#fill_metadata), [`inner_tm_loop`](gmm_v2.md#fill_metadata.inner_tm_loop), [`zero_out_start`](gmm_v2.md#zero_out_start), [`lhs_index_map`](gmm_v2.md#IndexMaps.lhs_index_map), [`out_index_map`](gmm_v2.md#IndexMaps.out_index_map), [`outer_group_loop`](gmm_v2.md#fill_metadata.outer_group_loop), [`out_size_n`](gmm_v2.md#GmmConfigs.out_size_n), [`TileFn`](gmm_v2.md#TileFn), [`zero_out_end`](gmm_v2.md#zero_out_end)

### <a id="FusedWeightsRef"></a>`FusedWeightsRef`  ·  implements/extends RhsRef
- def: [`src/vllm_torchtpu/kernels/megablox/gmm_v2.py:194`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L194)
- doc: Dataclass for gate and up weights used in fused activation.
- signature: `class FusedWeightsRef(RhsRef):`
- members:
  - <a id="FusedWeightsRef.get_bias"></a>`get_bias(self)` — [`L210`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L210)
  - <a id="FusedWeightsRef.get_scale"></a>`get_scale(self, replicate_size: int | None = None)` — [`L205`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L205)
  - <a id="FusedWeightsRef.get_weight"></a>`get_weight(self)` — [`L200`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L200)
  - <a id="FusedWeightsRef.gate"></a>`gate` — [`L197`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L197)
  - <a id="FusedWeightsRef.up"></a>`up` — [`L198`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L198)
- uses (calls/refs, reference-scoped): [`WeightsRef`](gmm_v2.md#WeightsRef), [`RhsRef`](gmm_v2.md#RhsRef), [`get_bias`](gmm_v2.md#WeightsRef.get_bias), [`get_scale`](gmm_v2.md#WeightsRef.get_scale), [`get_weight`](gmm_v2.md#WeightsRef.get_weight), [`interleave_lane`](gmm_v2.md#interleave_lane)
- used by: [`kernel_main`](gmm_v2.md#kernel_main), [`RhsRef`](gmm_v2.md#RhsRef), [`get_scale`](gmm_v2.md#RhsRef.get_scale), [`get_bias`](gmm_v2.md#RhsRef.get_bias), [`get_weight`](gmm_v2.md#RhsRef.get_weight)

### <a id="GmmConfigs"></a>`GmmConfigs`
- def: [`src/vllm_torchtpu/kernels/megablox/gmm_v2.py:276`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L276)
- signature: `class GmmConfigs:`
- members:
  - <a id="GmmConfigs.num_quant_blocks_per_tile_k"></a>`num_quant_blocks_per_tile_k(self)` — [`L287`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L287)
  - <a id="GmmConfigs.out_size_n"></a>`out_size_n(self)` — [`L291`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L291)
  - <a id="GmmConfigs.acc_dtype"></a>`acc_dtype` — [`L282`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L282)
  - <a id="GmmConfigs.dims"></a>`dims` — [`L278`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L278)
  - <a id="GmmConfigs.fuse_act"></a>`fuse_act` — [`L284`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L284)
  - <a id="GmmConfigs.lhs_cfgs"></a>`lhs_cfgs` — [`L279`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L279)
  - <a id="GmmConfigs.out_dtype"></a>`out_dtype` — [`L281`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L281)
  - <a id="GmmConfigs.rhs_cfgs"></a>`rhs_cfgs` — [`L280`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L280)
  - <a id="GmmConfigs.tiles"></a>`tiles` — [`L277`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L277)
  - <a id="GmmConfigs.zero_init"></a>`zero_init` — [`L283`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L283)
- uses (calls/refs, reference-scoped): [`tile_k`](gmm_v2.md#TileSizes.tile_k), [`quant_block_size`](gmm_v2.md#InputConfigs.quant_block_size), [`size_n`](gmm_v2.md#Dimensions.size_n), [`InputConfigs`](gmm_v2.md#InputConfigs), [`Dimensions`](gmm_v2.md#Dimensions), [`TileSizes`](gmm_v2.md#TileSizes)
- used by: [`gmm_v2`](gmm_v2.md#gmm_v2), [`kernel_main`](gmm_v2.md#kernel_main), [`_matmul`](gmm_v2.md#inner_kernel._matmul), [`generate_block_specs`](gmm_v2.md#generate_block_specs), [`make_gmm_configs`](gmm_v2.md#make_gmm_configs), [`get_cost_estimate`](gmm_v2.md#get_cost_estimate), [`get_scope_name`](gmm_v2.md#get_scope_name), [`inner_kernel`](gmm_v2.md#inner_kernel), [`rhs_scale_index_map`](gmm_v2.md#IndexMaps.rhs_scale_index_map), [`run_matmul_step`](gmm_v2.md#inner_kernel.run_matmul_step), [`fill_metadata`](gmm_v2.md#fill_metadata), [`inner_tm_loop`](gmm_v2.md#fill_metadata.inner_tm_loop), [`lhs_index_map`](gmm_v2.md#IndexMaps.lhs_index_map), [`out_index_map`](gmm_v2.md#IndexMaps.out_index_map), [`outer_group_loop`](gmm_v2.md#fill_metadata.outer_group_loop), [`__init__`](gmm_v2.md#IndexMaps.__init__), [`get_metadata`](gmm_v2.md#get_metadata)

### <a id="IndexMaps"></a>`IndexMaps`
- def: [`src/vllm_torchtpu/kernels/megablox/gmm_v2.py:301`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L301)
- doc: Index maps for GMM kernel.
- signature: `class IndexMaps:`
- members:
  - <a id="IndexMaps.lhs_index_map"></a>`lhs_index_map(self, _: jax.Array, gm_id: jax.Array, k_id: jax.Array)` — [`L308`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L308)
  - <a id="IndexMaps.out_index_map"></a>`out_index_map(self, n_id: jax.Array, gm_id: jax.Array, _: jax.Array)` — [`L335`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L335)
  - <a id="IndexMaps.rhs_bias_index_map"></a>`rhs_bias_index_map(self, n_id: jax.Array, gm_id: jax.Array, _: jax.Array)` — [`L322`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L322)
  - <a id="IndexMaps.rhs_scale_index_map"></a>`rhs_scale_index_map(self, n_id: jax.Array, gm_id: jax.Array, k_id: jax.Array)` — [`L326`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L326)
  - <a id="IndexMaps.rhs_weight_index_map"></a>`rhs_weight_index_map(self, n_id: jax.Array, gm_id: jax.Array, k_id: jax.Array)` — [`L318`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L318)
  - <a id="IndexMaps.cfgs"></a>`cfgs` — [`L306`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L306)
  - <a id="IndexMaps.metadata_ref"></a>`metadata_ref` — [`L305`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L305)
- protocol/private: <a id="IndexMaps.__init__"></a>`__init__`[`L304`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L304)
- uses (calls/refs, reference-scoped): [`tiles`](gmm_v2.md#GmmConfigs.tiles), [`dims`](gmm_v2.md#GmmConfigs.dims), [`size_lhs_sublane`](gmm_v2.md#Dimensions.size_lhs_sublane), [`rhs_cfgs`](gmm_v2.md#GmmConfigs.rhs_cfgs), [`tile_k`](gmm_v2.md#TileSizes.tile_k), [`num_quant_blocks_per_tile_k`](gmm_v2.md#GmmConfigs.num_quant_blocks_per_tile_k), [`quant_block_size`](gmm_v2.md#InputConfigs.quant_block_size), [`gm_id_to_m_offset`](gmm_v2.md#MetadataRef.gm_id_to_m_offset), [`GmmConfigs`](gmm_v2.md#GmmConfigs), [`MetadataRef`](gmm_v2.md#MetadataRef), [`gm_id_to_group_id`](gmm_v2.md#MetadataRef.gm_id_to_group_id)
- used by: [`generate_block_specs`](gmm_v2.md#generate_block_specs)

### <a id="InputConfigs"></a>`InputConfigs`
- def: [`src/vllm_torchtpu/kernels/megablox/gmm_v2.py:242`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L242)
- signature: `class InputConfigs:`
- members:
  - <a id="InputConfigs.should_dequantize_after_matmul"></a>`should_dequantize_after_matmul(self)` — [`L265`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L265)
  - <a id="InputConfigs.should_dequantize_before_matmul"></a>`should_dequantize_before_matmul(self)` — [`L256`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L256) — Dequantize rhs before matmul if block size limits MXU utilization.
  - <a id="InputConfigs.should_quantize"></a>`should_quantize(self)` — [`L269`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L269)
  - <a id="InputConfigs.should_unpack"></a>`should_unpack(self)` — [`L250`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L250) — True if rhs weights are sub-byte (e.g. INT4) packed in
  - <a id="InputConfigs.dtype"></a>`dtype` — [`L245`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L245)
  - <a id="InputConfigs.has_bias"></a>`has_bias` — [`L246`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L246)
  - <a id="InputConfigs.has_scale"></a>`has_scale` — [`L247`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L247)
  - <a id="InputConfigs.quant_block_size"></a>`quant_block_size` — [`L244`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L244)
  - <a id="InputConfigs.quant_dtype"></a>`quant_dtype` — [`L243`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L243)
- uses (calls/refs, reference-scoped): [`get_packing_factor`](gmm_v2.md#get_packing_factor)
- used by: [`kernel_main`](gmm_v2.md#kernel_main), [`_matmul`](gmm_v2.md#inner_kernel._matmul), [`generate_block_specs`](gmm_v2.md#generate_block_specs), [`make_gmm_configs`](gmm_v2.md#make_gmm_configs), [`calculate_tiling`](gmm_v2.md#calculate_tiling), [`get_cost_estimate`](gmm_v2.md#get_cost_estimate), [`rhs_scale_index_map`](gmm_v2.md#IndexMaps.rhs_scale_index_map), [`rhs_cfgs`](gmm_v2.md#GmmConfigs.rhs_cfgs), [`_gmm_vmem_estimate`](gmm_v2.md#calculate_tiling._gmm_vmem_estimate), [`num_quant_blocks_per_tile_k`](gmm_v2.md#GmmConfigs.num_quant_blocks_per_tile_k), [`lhs_cfgs`](gmm_v2.md#GmmConfigs.lhs_cfgs), [`TileFn`](gmm_v2.md#TileFn), [`_is_tile_k_quant_block_compatible`](gmm_v2.md#calculate_tiling._is_tile_k_quant_block_compatible)

### <a id="MetadataRef"></a>`MetadataRef`
- def: [`src/vllm_torchtpu/kernels/megablox/gmm_v2.py:218`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L218)
- signature: `class MetadataRef:`
- members:
  - <a id="MetadataRef.gm_id_to_group_id"></a>`gm_id_to_group_id` — [`L219`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L219)
  - <a id="MetadataRef.gm_id_to_m_offset"></a>`gm_id_to_m_offset` — [`L220`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L220)
- used by: [`gmm_v2`](gmm_v2.md#gmm_v2), [`kernel_main`](gmm_v2.md#kernel_main), [`generate_block_specs`](gmm_v2.md#generate_block_specs), [`inner_kernel`](gmm_v2.md#inner_kernel), [`rhs_scale_index_map`](gmm_v2.md#IndexMaps.rhs_scale_index_map), [`fill_metadata`](gmm_v2.md#fill_metadata), [`inner_tm_loop`](gmm_v2.md#fill_metadata.inner_tm_loop), [`zero_out_start`](gmm_v2.md#zero_out_start), [`lhs_index_map`](gmm_v2.md#IndexMaps.lhs_index_map), [`out_index_map`](gmm_v2.md#IndexMaps.out_index_map), [`rhs_bias_index_map`](gmm_v2.md#IndexMaps.rhs_bias_index_map), [`rhs_weight_index_map`](gmm_v2.md#IndexMaps.rhs_weight_index_map), [`__init__`](gmm_v2.md#IndexMaps.__init__)

### <a id="RhsRef"></a>`RhsRef`  ·  implements/extends ABC
- def: [`src/vllm_torchtpu/kernels/megablox/gmm_v2.py:153`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L153)
- doc: Abstract class that defines interfaces for rhs values.
- signature: `class RhsRef(ABC):`
- members:
  - <a id="RhsRef.get_bias"></a>`get_bias(self)` — [`L165`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L165)
  - <a id="RhsRef.get_scale"></a>`get_scale(self, replicate_size: int | None = None)` — [`L160`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L160) — Returns scale array, optionally replicated across sublanes.
  - <a id="RhsRef.get_weight"></a>`get_weight(self)` — [`L157`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L157)
- uses (calls/refs, reference-scoped): [`get_bias`](gmm_v2.md#FusedWeightsRef.get_bias), [`get_scale`](gmm_v2.md#FusedWeightsRef.get_scale), [`get_weight`](gmm_v2.md#FusedWeightsRef.get_weight), [`WeightsRef`](gmm_v2.md#WeightsRef), [`FusedWeightsRef`](gmm_v2.md#FusedWeightsRef), [`get_bias`](gmm_v2.md#WeightsRef.get_bias), [`get_scale`](gmm_v2.md#WeightsRef.get_scale), [`get_weight`](gmm_v2.md#WeightsRef.get_weight)
- used by: [`_matmul`](gmm_v2.md#inner_kernel._matmul), [`inner_kernel`](gmm_v2.md#inner_kernel), [`WeightsRef`](gmm_v2.md#WeightsRef), [`FusedWeightsRef`](gmm_v2.md#FusedWeightsRef)

### <a id="TileSizes"></a>`TileSizes`
- def: [`src/vllm_torchtpu/kernels/megablox/gmm_v2.py:224`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L224)
- signature: `class TileSizes:`
- members:
  - <a id="TileSizes.bucket_base"></a>`bucket_base` — [`L228`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L228)
  - <a id="TileSizes.tile_k"></a>`tile_k` — [`L226`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L226)
  - <a id="TileSizes.tile_m"></a>`tile_m` — [`L225`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L225)
  - <a id="TileSizes.tile_n"></a>`tile_n` — [`L227`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L227)
- used by: [`gmm_v2`](gmm_v2.md#gmm_v2), [`kernel_main`](gmm_v2.md#kernel_main), [`_matmul`](gmm_v2.md#inner_kernel._matmul), [`generate_block_specs`](gmm_v2.md#generate_block_specs), [`make_gmm_configs`](gmm_v2.md#make_gmm_configs), [`calculate_tiling`](gmm_v2.md#calculate_tiling), [`tiles`](gmm_v2.md#GmmConfigs.tiles), [`get_scope_name`](gmm_v2.md#get_scope_name), [`inner_kernel`](gmm_v2.md#inner_kernel), [`rhs_scale_index_map`](gmm_v2.md#IndexMaps.rhs_scale_index_map), [`run_matmul_step`](gmm_v2.md#inner_kernel.run_matmul_step), [`inner_tm_loop`](gmm_v2.md#fill_metadata.inner_tm_loop), [`outer_group_loop`](gmm_v2.md#fill_metadata.outer_group_loop), [`num_quant_blocks_per_tile_k`](gmm_v2.md#GmmConfigs.num_quant_blocks_per_tile_k), [`TileFn`](gmm_v2.md#TileFn)

### <a id="WeightsRef"></a>`WeightsRef`  ·  implements/extends RhsRef
- def: [`src/vllm_torchtpu/kernels/megablox/gmm_v2.py:170`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L170)
- doc: Dataclass for a single weights.
- signature: `class WeightsRef(RhsRef):`
- members:
  - <a id="WeightsRef.get_bias"></a>`get_bias(self)` — [`L187`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L187)
  - <a id="WeightsRef.get_scale"></a>`get_scale(self, replicate_size: int | None = None)` — [`L180`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L180)
  - <a id="WeightsRef.get_weight"></a>`get_weight(self)` — [`L177`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L177)
  - <a id="WeightsRef.bias"></a>`bias` — [`L175`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L175)
  - <a id="WeightsRef.scale"></a>`scale` — [`L174`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L174)
  - <a id="WeightsRef.weight"></a>`weight` — [`L173`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L173)
- uses (calls/refs, reference-scoped): [`RhsRef`](gmm_v2.md#RhsRef)
- used by: [`gmm_v2`](gmm_v2.md#gmm_v2), [`kernel_main`](gmm_v2.md#kernel_main), [`generate_block_specs`](gmm_v2.md#generate_block_specs), [`get_bias`](gmm_v2.md#FusedWeightsRef.get_bias), [`get_scale`](gmm_v2.md#FusedWeightsRef.get_scale), [`get_weight`](gmm_v2.md#FusedWeightsRef.get_weight), [`RhsRef`](gmm_v2.md#RhsRef), [`get_scale`](gmm_v2.md#RhsRef.get_scale), [`gate`](gmm_v2.md#FusedWeightsRef.gate), [`up`](gmm_v2.md#FusedWeightsRef.up), [`get_bias`](gmm_v2.md#RhsRef.get_bias), [`get_weight`](gmm_v2.md#RhsRef.get_weight)

## Functions
- <a id="_get_lhs_sublane_size"></a>`_get_lhs_sublane_size(dtype: jnp.dtype, size_m: int)` — [`L129`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L129) — Sublane block size the kernel processes lhs rows in.
- <a id="calculate_tiling._gmm_vmem_estimate"></a>`_gmm_vmem_estimate(tm: int, tn: int, tk: int)` — [`L972`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L972)
- <a id="calculate_tiling._is_tile_k_quant_block_compatible"></a>`_is_tile_k_quant_block_compatible(tk: int)` — [`L961`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L961)
- <a id="inner_kernel._matmul"></a>`_matmul(is_first_k_step: bool, is_last_k_step: bool, bucket_m: int)` — [`L439`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L439)
- <a id="align_to"></a>`align_to(x, a)` — [`L125`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L125)
- <a id="apply_act_fn"></a>`apply_act_fn(acc: jax.Array, fuse_act: str | None)` — [`L84`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L84) — Applies a fused activation function to the accumulator.
- <a id="calculate_tiling"></a>`calculate_tiling(dims: Dimensions, lhs_cfgs: InputConfigs, rhs_cfgs: InputConfigs, vmem_limit_bytes: int, fuse_act: str | None = None)` — [`L922`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L922) — Calculate optimal tile sizes for GMM kernel.
- <a id="deinterleave_lane"></a>`deinterleave_lane(val: jax.Array)` — [`L74`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L74) — Deinterleaves an array along lane dim at zero-cost.
- <a id="fill_metadata"></a>`fill_metadata(lhs_group_sizes_ref: jax.Array, group_offset_ref: jax.Array, metadata_ref: MetadataRef, *, cfgs: GmmConfigs)` — [`L656`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L656) — Fills the metadata for the given lhs group sizes and group offset.
- <a id="zero_out_start.fill_zero"></a>`fill_zero(i, zero_size, *, start, end)` — [`L778`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L778)
- <a id="generate_block_specs"></a>`generate_block_specs(metadata_ref: MetadataRef, cfgs: GmmConfigs)` — [`L349`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L349) — Generates block specs for the given lhs, rhs, and out refs.
- <a id="get_cost_estimate"></a>`get_cost_estimate(cfgs: GmmConfigs)` — [`L1106`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L1106) — Returns the cost estimate for the GMM kernel.
- <a id="get_metadata"></a>`get_metadata(cfgs: GmmConfigs)` — [`L1256`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L1256)
- <a id="get_packing_factor"></a>`get_packing_factor(storage_dtype: jnp.dtype, quant_dtype: jnp.dtype | None)` — [`L136`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L136)
- <a id="get_scope_name"></a>`get_scope_name(cfgs: GmmConfigs)` — [`L1141`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L1141)
- <a id="gmm_v2"></a>`gmm_v2(lhs: jax.Array, rhs: jax.Array, group_sizes: jax.Array, rhs_scale: jax.Array | None = None, rhs_bias: jax.Array | None = None, group_offset: jax.Array | None = None, *, tile_info: TileSizes | TileFn = calculate_tiling, vmem_limit_bytes: int | None = None, precision: jax.lax.Precision = jax.lax.Precision.DEFAULT, preferred_element_type: jnp.dtype | None = None, acc_dtype: jnp.dtype | None = None, maybe_quantize_lhs: bool = True, zero_initialize: bool = True, fuse_act: str | None = None, rhs_quant_dtype: jnp.dtype | None = None)` — [`L1280`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L1280) — GMM kernel implemented with emit_pipeline.
- <a id="inner_kernel"></a>`inner_kernel(tiled_lhs_ref: jax.Array, tiled_rhs_ref: RhsRef, tiled_out_ref: jax.Array, partial_out_ref: jax.Array, acc_ref: jax.Array, metadata_ref: MetadataRef, *, cfgs: GmmConfigs)` — [`L396`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L396) — Inner kernel invoked by emit_pipeline to perform matmul.
- <a id="fill_metadata.inner_tm_loop"></a>`inner_tm_loop(tm_id, curr_m_offset, *, end_m_offset, group_id)` — [`L686`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L686)
- <a id="interleave_lane"></a>`interleave_lane(lhs: jax.Array, rhs: jax.Array)` — [`L61`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L61) — Interleaves two arrays along lane dim at zero-cost.
- <a id="kernel_main"></a>`kernel_main(lhs_group_sizes_ref: jax.Array, group_offset_ref: jax.Array, lhs_ref: jax.Array, rhs_ref: WeightsRef, out_ref: jax.Array, partial_out_ref: jax.Array, acc_ref: jax.Array, metadata_ref: MetadataRef, zero_ref: jax.Array | None, semaphore_ref: jax.Array | None, *, cfgs: GmmConfigs)` — [`L822`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L822) — Entry point for GMM kernel.
- <a id="zero_out_start.left_fill_zero"></a>`left_fill_zero(i, zero_size)` — [`L795`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L795)
- <a id="make_gmm_configs"></a>`make_gmm_configs(lhs: jax.Array, rhs: jax.Array, rhs_scale: jax.Array | None, rhs_bias: jax.Array | None, group_sizes: jax.Array, group_offset: jax.Array, *, tile_info: TileSizes | TileFn, vmem_limit_bytes: int, out_dtype: jnp.dtype | None, acc_dtype: jnp.dtype | None, maybe_quantize_lhs: bool, zero_initialize: bool, fuse_act: str | None = None, rhs_quant_dtype: jnp.dtype | None = None)` — [`L1150`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L1150) — Fills the GMM config for the GMM kernel.
- <a id="inner_kernel.run_matmul_step.matmul_first"></a>`matmul_first()` — [`L623`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L623)
- <a id="inner_kernel.run_matmul_step.matmul_first_last"></a>`matmul_first_last()` — [`L619`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L619)
- <a id="inner_kernel.run_matmul_step.matmul_last"></a>`matmul_last()` — [`L631`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L631)
- <a id="inner_kernel.run_matmul_step.matmul_mid"></a>`matmul_mid()` — [`L627`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L627)
- <a id="fill_metadata.outer_group_loop"></a>`outer_group_loop(lhs_group_id, carry)` — [`L701`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L701)
- <a id="zero_out_start.right_fill_zero"></a>`right_fill_zero(i, zero_size)` — [`L799`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L799)
- <a id="inner_kernel.run_matmul_step"></a>`run_matmul_step(bucket_idx: int)` — [`L615`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L615)
- <a id="silu_and_mul_with_clamp"></a>`silu_and_mul_with_clamp(gate: jax.Array, up: jax.Array, limit: float = 10)` — [`L41`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L41) — Activation used in some models DeepSeek V4.
- <a id="situ_and_mul"></a>`situ_and_mul(gate: jax.Array, up: jax.Array, beta: float, linear_beta: float | None)` — [`L52`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L52)
- <a id="swigluoai"></a>`swigluoai(gate: jax.Array, up: jax.Array, *, alpha: float = 1.702, limit: float = 7)` — [`L30`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L30) — Activation used in some models such as GPT-OSS.
- <a id="validate_inputs"></a>`validate_inputs(lhs: jax.Array, rhs: jax.Array, rhs_scale: jax.Array | None, rhs_bias: jax.Array | None, group_sizes: jax.Array, group_offset: jax.Array, fuse_act: str | None = None, packing_factor: int = 1)` — [`L1058`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L1058) — Validates the inputs for the GMM kernel.
- <a id="zero_out_end"></a>`zero_out_end(out_ref: jax.Array, semaphore_ref: jax.Array, zero_size: jax.Array, *, dims: Dimensions)` — [`L807`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L807)
- <a id="zero_out_start"></a>`zero_out_start(out_ref: jax.Array, zero_ref: jax.Array, semaphore_ref: jax.Array, metadata_ref: MetadataRef, num_gm: jax.Array, *, dims: Dimensions)` — [`L746`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L746) — Zero out output rows that are not used in the computation.

## Module values
- <a id="TileFn"></a>`TileFn` — [`L298`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/gmm_v2.py#L298)

