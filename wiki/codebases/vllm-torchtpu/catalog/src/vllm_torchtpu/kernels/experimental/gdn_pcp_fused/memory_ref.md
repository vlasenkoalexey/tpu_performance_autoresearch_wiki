---
title: 'Module: src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/memory_ref.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/memory_ref.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.experimental.gdn_pcp_fused.memory_ref`/
symbols:
  create_allocs: create_allocs().
  StateOutBufferedRef.copy_out: StateOutBufferedRef#copy_out().
  StateInBufferedRef.copy_in: StateInBufferedRef#copy_in().
  BaseBufferedRef.metadata_ref: BaseBufferedRef#metadata_ref.
  StateInBufferedRef.wait_in: StateInBufferedRef#wait_in().
  StateOutBufferedRef.wait_out: StateOutBufferedRef#wait_out().
  BaseBufferedRef.cfg: BaseBufferedRef#cfg.
  InBufferedRef.copy_in: InBufferedRef#copy_in().
  OutBufferedRef.copy_out: OutBufferedRef#copy_out().
  BaseBufferedRef: BaseBufferedRef#
  SmemWrapper: SmemWrapper#
  MetadataRef: MetadataRef#
  InBufferedRef.wait_in: InBufferedRef#wait_in().
  OutBufferedRef.wait_out: OutBufferedRef#wait_out().
  MetadataRef.p_id_to_r_size: MetadataRef#p_id_to_r_size.
  _GranuleStateRef: _GranuleStateRef#
  _GranuleStateRef._ckpt_state_idx: _GranuleStateRef#_ckpt_state_idx().
  MetadataRef.create: MetadataRef#create().
  WeightRefs: WeightRefs#
  WeightRefs.conv: WeightRefs#conv.
  MetadataRef.p_id_to_s_idx: MetadataRef#p_id_to_s_idx.
  InBufferedRef: InBufferedRef#
  granule_view: granule_view().
  MetadataRef.p_id_is_first_tile: MetadataRef#p_id_is_first_tile.
  StateInBufferedRef: StateInBufferedRef#
  StateOutBufferedRef: StateOutBufferedRef#
  SmemWrapper.__getitem__: SmemWrapper#__getitem__().
  BaseBufferedRef.create: BaseBufferedRef#create().
  MetadataRef.p_id_to_r_base: MetadataRef#p_id_to_r_base.
  MetadataRef.p_id_is_last_tile: MetadataRef#p_id_is_last_tile.
  OutBufferedRef: OutBufferedRef#
  SmemWrapper._get_pos: SmemWrapper#_get_pos().
  ConvWeightsRef.bias: ConvWeightsRef#bias.
  WeightRefs.gdn: WeightRefs#gdn.
  MetadataRef.s_idx_has_initial_state: MetadataRef#s_idx_has_initial_state.
  ConvWeightsRef: ConvWeightsRef#
  ConvWeightsRef.weight: ConvWeightsRef#weight.
  GDNWeightsRef: GDNWeightsRef#
  GDNWeightsRef.a_log: GDNWeightsRef#a_log.
  GDNWeightsRef.dt_bias: GDNWeightsRef#dt_bias.
  _GranuleStateRef.offset: _GranuleStateRef#offset.
  StateOutBufferedRef.compact_output_ref: StateOutBufferedRef#compact_output_ref.
  SmemWrapper.data: SmemWrapper#data.
  SmemWrapper.shape: SmemWrapper#shape.
  MetadataRef.num_tiles: MetadataRef#num_tiles.
  MetadataRef.s_idx_to_state_indices: MetadataRef#s_idx_to_state_indices.
  MetadataRef.s_idx_to_read_offset: MetadataRef#s_idx_to_read_offset.
  MetadataRef.s_idx_to_ckpt_indices: MetadataRef#s_idx_to_ckpt_indices.
  MetadataRef.__len__: MetadataRef#__len__().
---
# Module: [`src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/memory_ref.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/memory_ref.py)

## Classes
### <a id="BaseBufferedRef"></a>`BaseBufferedRef`  ·  implements/extends BufferedRef
- def: [`src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/memory_ref.py:141`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/memory_ref.py#L141) — documented in [gdn-pcp-fused-kernel](../../../../../../concepts/gdn-pcp-fused-kernel.md)
- signature: `class BaseBufferedRef(pltpu.BufferedRef):`
- members:
  - <a id="BaseBufferedRef.create"></a>`create(cls, spec: pl.BlockSpec, dtype_or_type: jax.Array, buffer_type: pltpu.BufferType, buffer_count: int, use_lookahead: bool, cfg: config.GDNConfig, metadata_ref: MetadataRef, **fields)` — [`L149`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/memory_ref.py#L149)
  - <a id="BaseBufferedRef.cfg"></a>`cfg` — [`L142`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/memory_ref.py#L142)
  - <a id="BaseBufferedRef.metadata_ref"></a>`metadata_ref` — [`L146`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/memory_ref.py#L146) — documented in [gdn-pcp-fused-kernel](../../../../../../concepts/gdn-pcp-fused-kernel.md)
- uses (calls/refs, reference-scoped): [`GDNConfig`](config.md#GDNConfig), [`MetadataRef`](memory_ref.md#MetadataRef), [`_GranuleStateRef`](memory_ref.md#_GranuleStateRef), [`InBufferedRef`](memory_ref.md#InBufferedRef), [`OutBufferedRef`](memory_ref.md#OutBufferedRef)
- used by: [`copy_out`](memory_ref.md#StateOutBufferedRef.copy_out), [`copy_in`](memory_ref.md#StateInBufferedRef.copy_in), [`wait_in`](memory_ref.md#StateInBufferedRef.wait_in), [`wait_out`](memory_ref.md#StateOutBufferedRef.wait_out), [`copy_in`](memory_ref.md#InBufferedRef.copy_in), [`copy_out`](memory_ref.md#OutBufferedRef.copy_out), [`wait_in`](memory_ref.md#InBufferedRef.wait_in), [`wait_out`](memory_ref.md#OutBufferedRef.wait_out), [`_GranuleStateRef`](memory_ref.md#_GranuleStateRef), [`_ckpt_state_idx`](memory_ref.md#_GranuleStateRef._ckpt_state_idx), [`InBufferedRef`](memory_ref.md#InBufferedRef), [`OutBufferedRef`](memory_ref.md#OutBufferedRef)

### <a id="ConvWeightsRef"></a>`ConvWeightsRef`
- def: [`src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/memory_ref.py:41`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/memory_ref.py#L41)
- signature: `class ConvWeightsRef:`
- members:
  - <a id="ConvWeightsRef.bias"></a>`bias` — [`L43`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/memory_ref.py#L43)
  - <a id="ConvWeightsRef.weight"></a>`weight` — [`L42`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/memory_ref.py#L42)
- used by: [`fused_qkvz_projection_pcp_gdn`](pcp_wrapper.md#fused_qkvz_projection_pcp_gdn), [`inner_kernel`](kernel.md#inner_kernel), [`conv`](memory_ref.md#WeightRefs.conv)

### <a id="GDNWeightsRef"></a>`GDNWeightsRef`
- def: [`src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/memory_ref.py:48`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/memory_ref.py#L48)
- signature: `class GDNWeightsRef:`
- members:
  - <a id="GDNWeightsRef.a_log"></a>`a_log` — [`L49`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/memory_ref.py#L49)
  - <a id="GDNWeightsRef.dt_bias"></a>`dt_bias` — [`L50`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/memory_ref.py#L50)
- used by: [`fused_qkvz_projection_pcp_gdn`](pcp_wrapper.md#fused_qkvz_projection_pcp_gdn), [`inner_kernel`](kernel.md#inner_kernel), [`WeightRefs`](memory_ref.md#WeightRefs)

### <a id="InBufferedRef"></a>`InBufferedRef`  ·  implements/extends BaseBufferedRef
- def: [`src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/memory_ref.py:181`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/memory_ref.py#L181)
- signature: `class InBufferedRef(BaseBufferedRef):`
- members:
  - <a id="InBufferedRef.copy_in"></a>`copy_in(self, src_ref: jax.Ref, grid_indices: tuple[int | jax.Array])` — [`L182`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/memory_ref.py#L182) — documented in [gdn-pcp-fused-kernel](../../../../../../concepts/gdn-pcp-fused-kernel.md)
  - <a id="InBufferedRef.wait_in"></a>`wait_in(self, src_ref: jax.Ref, grid_indices: tuple[int | jax.Array])` — [`L199`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/memory_ref.py#L199) — documented in [gdn-pcp-fused-kernel](../../../../../../concepts/gdn-pcp-fused-kernel.md)
- uses (calls/refs, reference-scoped): [`seq_tile_size`](config.md#GDNConfig.seq_tile_size), [`metadata_ref`](memory_ref.md#BaseBufferedRef.metadata_ref), [`cfg`](memory_ref.md#BaseBufferedRef.cfg), [`BaseBufferedRef`](memory_ref.md#BaseBufferedRef), [`p_id_to_r_size`](memory_ref.md#MetadataRef.p_id_to_r_size), [`p_id_to_r_base`](memory_ref.md#MetadataRef.p_id_to_r_base)
- used by: [`create_allocs`](memory_ref.md#create_allocs), [`BaseBufferedRef`](memory_ref.md#BaseBufferedRef)

### <a id="MetadataRef"></a>`MetadataRef`
- def: [`src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/memory_ref.py:83`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/memory_ref.py#L83) — documented in [gdn-pcp-fused-kernel](../../../../../../concepts/gdn-pcp-fused-kernel.md)
- signature: `class MetadataRef:`
- members:
  - <a id="MetadataRef.create"></a>`create(cls, cfgs: config.GDNConfig, num_tiles: jax.Array, p_id_to_s_idx: jax.Array, p_id_to_r_base: jax.Array, p_id_to_r_size: jax.Array, p_id_is_first_tile: jax.Array, p_id_is_last_tile: jax.Array, s_idx_has_initial_state: jax.Array, s_idx_to_state_indices: jax.Array, s_idx_to_read_offset: jax.Array, s_idx_to_ckpt_indices: jax.Array | None = None)` — [`L107`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/memory_ref.py#L107) — documented in [gdn-pcp-fused-kernel](../../../../../../concepts/gdn-pcp-fused-kernel.md)
  - <a id="MetadataRef.num_tiles"></a>`num_tiles` — [`L84`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/memory_ref.py#L84)
  - <a id="MetadataRef.p_id_is_first_tile"></a>`p_id_is_first_tile` — [`L88`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/memory_ref.py#L88)
  - <a id="MetadataRef.p_id_is_last_tile"></a>`p_id_is_last_tile` — [`L89`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/memory_ref.py#L89)
  - <a id="MetadataRef.p_id_to_r_base"></a>`p_id_to_r_base` — [`L86`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/memory_ref.py#L86)
  - <a id="MetadataRef.p_id_to_r_size"></a>`p_id_to_r_size` — [`L87`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/memory_ref.py#L87)
  - <a id="MetadataRef.p_id_to_s_idx"></a>`p_id_to_s_idx` — [`L85`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/memory_ref.py#L85)
  - <a id="MetadataRef.s_idx_has_initial_state"></a>`s_idx_has_initial_state` — [`L90`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/memory_ref.py#L90)
  - <a id="MetadataRef.s_idx_to_ckpt_indices"></a>`s_idx_to_ckpt_indices` — [`L104`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/memory_ref.py#L104)
  - <a id="MetadataRef.s_idx_to_read_offset"></a>`s_idx_to_read_offset` — [`L96`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/memory_ref.py#L96)
  - <a id="MetadataRef.s_idx_to_state_indices"></a>`s_idx_to_state_indices` — [`L91`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/memory_ref.py#L91)
- protocol/private: <a id="MetadataRef.__len__"></a>`__len__`[`L136`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/memory_ref.py#L136)
- uses (calls/refs, reference-scoped): [`seq_tile_size`](config.md#GDNConfig.seq_tile_size), [`GDNConfig`](config.md#GDNConfig), [`SmemWrapper`](memory_ref.md#SmemWrapper)
- used by: [`_compute_pcp_stage_metadata_from_coordinates`](pcp_metadata.md#_compute_pcp_stage_metadata_from_coordinates), [`create_allocs`](memory_ref.md#create_allocs), [`inner_kernel`](kernel.md#inner_kernel), [`_pcp_qkvz_projection_gdn_outer_kernel`](pcp_wrapper.md#_pcp_qkvz_projection_gdn_outer_kernel), [`_compute_gdn_tile`](pcp_wrapper.md#_compute_gdn_tile), [`copy_out`](memory_ref.md#StateOutBufferedRef.copy_out), [`copy_in`](memory_ref.md#StateInBufferedRef.copy_in), [`load_and_select_states`](vmem_ldst.md#load_and_select_states), [`metadata_ref`](memory_ref.md#BaseBufferedRef.metadata_ref), [`wait_in`](memory_ref.md#StateInBufferedRef.wait_in), [`wait_out`](memory_ref.md#StateOutBufferedRef.wait_out), [`copy_in`](memory_ref.md#InBufferedRef.copy_in), [`copy_out`](memory_ref.md#OutBufferedRef.copy_out), [`compute_pcp_stage_metadata`](pcp_metadata.md#compute_pcp_stage_metadata), [`wait_in`](memory_ref.md#InBufferedRef.wait_in), [`wait_out`](memory_ref.md#OutBufferedRef.wait_out), [`_ckpt_state_idx`](memory_ref.md#_GranuleStateRef._ckpt_state_idx), [`create`](memory_ref.md#BaseBufferedRef.create)

### <a id="OutBufferedRef"></a>`OutBufferedRef`  ·  implements/extends BaseBufferedRef
- def: [`src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/memory_ref.py:220`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/memory_ref.py#L220)
- signature: `class OutBufferedRef(BaseBufferedRef):`
- members:
  - <a id="OutBufferedRef.copy_out"></a>`copy_out(self, dst_ref: jax.Ref, grid_indices: tuple[int | jax.Array])` — [`L221`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/memory_ref.py#L221) — documented in [gdn-pcp-fused-kernel](../../../../../../concepts/gdn-pcp-fused-kernel.md)
  - <a id="OutBufferedRef.wait_out"></a>`wait_out(self, dst_ref: jax.Ref, grid_indices: tuple[int | jax.Array])` — [`L238`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/memory_ref.py#L238) — documented in [gdn-pcp-fused-kernel](../../../../../../concepts/gdn-pcp-fused-kernel.md)
- uses (calls/refs, reference-scoped): [`seq_tile_size`](config.md#GDNConfig.seq_tile_size), [`metadata_ref`](memory_ref.md#BaseBufferedRef.metadata_ref), [`cfg`](memory_ref.md#BaseBufferedRef.cfg), [`BaseBufferedRef`](memory_ref.md#BaseBufferedRef), [`p_id_to_r_size`](memory_ref.md#MetadataRef.p_id_to_r_size), [`p_id_to_r_base`](memory_ref.md#MetadataRef.p_id_to_r_base)
- used by: [`create_allocs`](memory_ref.md#create_allocs), [`BaseBufferedRef`](memory_ref.md#BaseBufferedRef)

### <a id="SmemWrapper"></a>`SmemWrapper`
- def: [`src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/memory_ref.py:62`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/memory_ref.py#L62)
- doc: Maps physical 1-D data into logical N-D representation.
- signature: `class SmemWrapper:`
- members:
  - <a id="SmemWrapper.data"></a>`data` — [`L65`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/memory_ref.py#L65)
  - <a id="SmemWrapper.shape"></a>`shape` — [`L66`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/memory_ref.py#L66)
- protocol/private: <a id="SmemWrapper.__getitem__"></a>`__getitem__`[`L77`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/memory_ref.py#L77), <a id="SmemWrapper._get_pos"></a>`_get_pos`[`L68`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/memory_ref.py#L68)
- used by: [`p_id_to_r_size`](memory_ref.md#MetadataRef.p_id_to_r_size), [`create`](memory_ref.md#MetadataRef.create), [`p_id_to_s_idx`](memory_ref.md#MetadataRef.p_id_to_s_idx), [`p_id_is_first_tile`](memory_ref.md#MetadataRef.p_id_is_first_tile), [`p_id_is_last_tile`](memory_ref.md#MetadataRef.p_id_is_last_tile), [`p_id_to_r_base`](memory_ref.md#MetadataRef.p_id_to_r_base)

### <a id="StateInBufferedRef"></a>`StateInBufferedRef`  ·  implements/extends _GranuleStateRef
- def: [`src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/memory_ref.py:285`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/memory_ref.py#L285)
- doc: Input buffered ref for the per-sequence initial state (conv / recurrent).
- signature: `class StateInBufferedRef(_GranuleStateRef):`
- members:
  - <a id="StateInBufferedRef.copy_in"></a>`copy_in(self, src_ref: jax.Ref, grid_indices: tuple[int | jax.Array])` — [`L297`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/memory_ref.py#L297) — documented in [gdn-pcp-fused-kernel](../../../../../../concepts/gdn-pcp-fused-kernel.md)
  - <a id="StateInBufferedRef.wait_in"></a>`wait_in(self, src_ref: jax.Ref, grid_indices: tuple[int | jax.Array])` — [`L328`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/memory_ref.py#L328) — documented in [gdn-pcp-fused-kernel](../../../../../../concepts/gdn-pcp-fused-kernel.md)
- uses (calls/refs, reference-scoped): [`seq_tile_size`](config.md#GDNConfig.seq_tile_size), [`metadata_ref`](memory_ref.md#BaseBufferedRef.metadata_ref), [`cfg`](memory_ref.md#BaseBufferedRef.cfg), [`_GranuleStateRef`](memory_ref.md#_GranuleStateRef), [`_ckpt_state_idx`](memory_ref.md#_GranuleStateRef._ckpt_state_idx), [`p_id_to_s_idx`](memory_ref.md#MetadataRef.p_id_to_s_idx), [`granule_view`](memory_ref.md#granule_view), [`p_id_is_first_tile`](memory_ref.md#MetadataRef.p_id_is_first_tile), [`s_idx_has_initial_state`](memory_ref.md#MetadataRef.s_idx_has_initial_state), [`offset`](memory_ref.md#_GranuleStateRef.offset), [`s_idx_to_read_offset`](memory_ref.md#MetadataRef.s_idx_to_read_offset)
- used by: [`create_allocs`](memory_ref.md#create_allocs), [`_GranuleStateRef`](memory_ref.md#_GranuleStateRef)

### <a id="StateOutBufferedRef"></a>`StateOutBufferedRef`  ·  implements/extends _GranuleStateRef
- def: [`src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/memory_ref.py:353`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/memory_ref.py#L353)
- doc: Output buffered ref for the per-sequence state checkpoints.
- signature: `class StateOutBufferedRef(_GranuleStateRef):`
- members:
  - <a id="StateOutBufferedRef.copy_out"></a>`copy_out(self, dst_ref: jax.Ref, grid_indices: tuple[int | jax.Array])` — [`L375`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/memory_ref.py#L375) — documented in [gdn-pcp-fused-kernel](../../../../../../concepts/gdn-pcp-fused-kernel.md)
  - <a id="StateOutBufferedRef.wait_out"></a>`wait_out(self, dst_ref: jax.Ref, grid_indices: tuple[int | jax.Array])` — [`L416`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/memory_ref.py#L416) — documented in [gdn-pcp-fused-kernel](../../../../../../concepts/gdn-pcp-fused-kernel.md)
  - <a id="StateOutBufferedRef.compact_output_ref"></a>`compact_output_ref` — [`L371`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/memory_ref.py#L371)
- uses (calls/refs, reference-scoped): [`seq_tile_size`](config.md#GDNConfig.seq_tile_size), [`metadata_ref`](memory_ref.md#BaseBufferedRef.metadata_ref), [`cfg`](memory_ref.md#BaseBufferedRef.cfg), [`window_size`](config.md#GDNConfig.window_size), [`_GranuleStateRef`](memory_ref.md#_GranuleStateRef), [`_ckpt_state_idx`](memory_ref.md#_GranuleStateRef._ckpt_state_idx), [`p_id_to_r_size`](memory_ref.md#MetadataRef.p_id_to_r_size), [`p_id_to_s_idx`](memory_ref.md#MetadataRef.p_id_to_s_idx), [`granule_view`](memory_ref.md#granule_view), [`p_id_is_last_tile`](memory_ref.md#MetadataRef.p_id_is_last_tile), [`offset`](memory_ref.md#_GranuleStateRef.offset)
- used by: [`create_allocs`](memory_ref.md#create_allocs), [`_GranuleStateRef`](memory_ref.md#_GranuleStateRef)

### <a id="WeightRefs"></a>`WeightRefs`
- def: [`src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/memory_ref.py:55`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/memory_ref.py#L55)
- signature: `class WeightRefs:`
- members:
  - <a id="WeightRefs.conv"></a>`conv` — [`L56`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/memory_ref.py#L56)
  - <a id="WeightRefs.gdn"></a>`gdn` — [`L57`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/memory_ref.py#L57)
- uses (calls/refs, reference-scoped): [`ConvWeightsRef`](memory_ref.md#ConvWeightsRef), [`GDNWeightsRef`](memory_ref.md#GDNWeightsRef)
- used by: [`fused_qkvz_projection_pcp_gdn`](pcp_wrapper.md#fused_qkvz_projection_pcp_gdn), [`inner_kernel`](kernel.md#inner_kernel), [`_pcp_qkvz_projection_gdn_outer_kernel`](pcp_wrapper.md#_pcp_qkvz_projection_gdn_outer_kernel), [`_compute_gdn_tile`](pcp_wrapper.md#_compute_gdn_tile)

### <a id="_GranuleStateRef"></a>`_GranuleStateRef`  ·  implements/extends BaseBufferedRef
- def: [`src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/memory_ref.py:259`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/memory_ref.py#L259)
- doc: Shared addressing of the per-sequence state refs below.
- signature: `class _GranuleStateRef(BaseBufferedRef):`
- members:
  - <a id="_GranuleStateRef._ckpt_state_idx"></a>`_ckpt_state_idx(self, s_idx, ckpt)` — [`L269`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/memory_ref.py#L269) — Source block holding checkpoint `ckpt` of sequence `s_idx`.
  - <a id="_GranuleStateRef.offset"></a>`offset` — [`L267`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/memory_ref.py#L267)
- uses (calls/refs, reference-scoped): [`metadata_ref`](memory_ref.md#BaseBufferedRef.metadata_ref), [`BaseBufferedRef`](memory_ref.md#BaseBufferedRef), [`StateInBufferedRef`](memory_ref.md#StateInBufferedRef), [`StateOutBufferedRef`](memory_ref.md#StateOutBufferedRef), [`s_idx_to_ckpt_indices`](memory_ref.md#MetadataRef.s_idx_to_ckpt_indices), [`s_idx_to_state_indices`](memory_ref.md#MetadataRef.s_idx_to_state_indices)
- used by: [`copy_out`](memory_ref.md#StateOutBufferedRef.copy_out), [`copy_in`](memory_ref.md#StateInBufferedRef.copy_in), [`BaseBufferedRef`](memory_ref.md#BaseBufferedRef), [`StateInBufferedRef`](memory_ref.md#StateInBufferedRef), [`StateOutBufferedRef`](memory_ref.md#StateOutBufferedRef)

## Functions
- <a id="create_allocs"></a>`create_allocs(metadata_ref: MetadataRef, qkv_ref: jax.Array, b_ref: jax.Array, a_ref: jax.Array, out_ref: jax.Array, conv_state_ref: jax.Array, recurrent_state_ref: jax.Array, cfg: config.GDNConfig, state_output_ref: jax.Array | None = None)` — [`L437`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/memory_ref.py#L437) — Build the pipeline allocations. — documented in [gdn-pcp-fused-kernel](../../../../../../concepts/gdn-pcp-fused-kernel.md)
- <a id="granule_view"></a>`granule_view(ref: jax.Ref, leading_shape: tuple[int, ...])` — [`L34`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/memory_ref.py#L34)

