---
title: 'Module: src/vllm_torchtpu/kernels/gdn/v3/memory_ref.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/gdn/v3/memory_ref.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.gdn.v3.memory_ref`/
symbols:
  create_allocs: create_allocs().
  StateInBufferedRef.copy_in: StateInBufferedRef#copy_in().
  StateOutBufferedRef.copy_out: StateOutBufferedRef#copy_out().
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
  MetadataRef.create: MetadataRef#create().
  _GranuleStateRef: _GranuleStateRef#
  _GranuleStateRef._ckpt_state_idx: _GranuleStateRef#_ckpt_state_idx().
  WeightRefs.conv: WeightRefs#conv.
  MetadataRef.p_id_to_s_idx: MetadataRef#p_id_to_s_idx.
  InBufferedRef: InBufferedRef#
  WeightRefs: WeightRefs#
  MetadataRef.p_id_is_first_tile: MetadataRef#p_id_is_first_tile.
  StateInBufferedRef: StateInBufferedRef#
  StateOutBufferedRef: StateOutBufferedRef#
  WeightRefs.gdn: WeightRefs#gdn.
  SmemWrapper.__getitem__: SmemWrapper#__getitem__().
  BaseBufferedRef.create: BaseBufferedRef#create().
  MetadataRef.p_id_to_r_base: MetadataRef#p_id_to_r_base.
  MetadataRef.p_id_is_last_tile: MetadataRef#p_id_is_last_tile.
  OutBufferedRef: OutBufferedRef#
  granule_view: granule_view().
  SmemWrapper._get_pos: SmemWrapper#_get_pos().
  ConvWeightsRef.bias: ConvWeightsRef#bias.
  GDNWeightsRef.a_log: GDNWeightsRef#a_log.
  GDNWeightsRef.dt_bias: GDNWeightsRef#dt_bias.
  MetadataRef.s_idx_has_initial_state: MetadataRef#s_idx_has_initial_state.
  ConvWeightsRef: ConvWeightsRef#
  ConvWeightsRef.weight: ConvWeightsRef#weight.
  GDNWeightsRef: GDNWeightsRef#
  _GranuleStateRef.offset: _GranuleStateRef#offset.
  SmemWrapper.data: SmemWrapper#data.
  SmemWrapper.shape: SmemWrapper#shape.
  MetadataRef.num_tiles: MetadataRef#num_tiles.
  MetadataRef.s_idx_to_state_indices: MetadataRef#s_idx_to_state_indices.
  MetadataRef.s_idx_to_read_offset: MetadataRef#s_idx_to_read_offset.
  MetadataRef.s_idx_to_ckpt_indices: MetadataRef#s_idx_to_ckpt_indices.
  MetadataRef.__len__: MetadataRef#__len__().
---
# Module: [`src/vllm_torchtpu/kernels/gdn/v3/memory_ref.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/memory_ref.py)

## Classes
### <a id="BaseBufferedRef"></a>`BaseBufferedRef`  ·  implements/extends BufferedRef
- def: [`src/vllm_torchtpu/kernels/gdn/v3/memory_ref.py:134`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/memory_ref.py#L134)
- signature: `class BaseBufferedRef(pltpu.BufferedRef):`
- members:
  - <a id="BaseBufferedRef.create"></a>`create(cls, spec: pl.BlockSpec, dtype_or_type: jax.Array, buffer_type: pltpu.BufferType, buffer_count: int, use_lookahead: bool, cfg: config.GDNConfig, metadata_ref: MetadataRef, **fields)` — [`L142`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/memory_ref.py#L142)
  - <a id="BaseBufferedRef.cfg"></a>`cfg` — [`L135`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/memory_ref.py#L135)
  - <a id="BaseBufferedRef.metadata_ref"></a>`metadata_ref` — [`L139`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/memory_ref.py#L139) — documented in [gated-deltanet-kernels](../../../../../../concepts/gated-deltanet-kernels.md)
- uses (calls/refs, reference-scoped): [`GDNConfig`](config.md#GDNConfig), [`MetadataRef`](memory_ref.md#MetadataRef), [`_GranuleStateRef`](memory_ref.md#_GranuleStateRef), [`InBufferedRef`](memory_ref.md#InBufferedRef), [`OutBufferedRef`](memory_ref.md#OutBufferedRef)
- used by: [`copy_in`](memory_ref.md#StateInBufferedRef.copy_in), [`copy_out`](memory_ref.md#StateOutBufferedRef.copy_out), [`wait_in`](memory_ref.md#StateInBufferedRef.wait_in), [`wait_out`](memory_ref.md#StateOutBufferedRef.wait_out), [`copy_in`](memory_ref.md#InBufferedRef.copy_in), [`copy_out`](memory_ref.md#OutBufferedRef.copy_out), [`wait_in`](memory_ref.md#InBufferedRef.wait_in), [`wait_out`](memory_ref.md#OutBufferedRef.wait_out), [`_GranuleStateRef`](memory_ref.md#_GranuleStateRef), [`_ckpt_state_idx`](memory_ref.md#_GranuleStateRef._ckpt_state_idx), [`InBufferedRef`](memory_ref.md#InBufferedRef), [`OutBufferedRef`](memory_ref.md#OutBufferedRef)

### <a id="ConvWeightsRef"></a>`ConvWeightsRef`
- def: [`src/vllm_torchtpu/kernels/gdn/v3/memory_ref.py:34`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/memory_ref.py#L34)
- signature: `class ConvWeightsRef:`
- members:
  - <a id="ConvWeightsRef.bias"></a>`bias` — [`L36`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/memory_ref.py#L36)
  - <a id="ConvWeightsRef.weight"></a>`weight` — [`L35`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/memory_ref.py#L35)
- used by: [`inner_kernel`](wrapper.md#inner_kernel), [`fused_conv1d_gdn`](wrapper.md#fused_conv1d_gdn), [`conv`](memory_ref.md#WeightRefs.conv)

### <a id="GDNWeightsRef"></a>`GDNWeightsRef`
- def: [`src/vllm_torchtpu/kernels/gdn/v3/memory_ref.py:41`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/memory_ref.py#L41)
- signature: `class GDNWeightsRef:`
- members:
  - <a id="GDNWeightsRef.a_log"></a>`a_log` — [`L42`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/memory_ref.py#L42)
  - <a id="GDNWeightsRef.dt_bias"></a>`dt_bias` — [`L43`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/memory_ref.py#L43)
- used by: [`inner_kernel`](wrapper.md#inner_kernel), [`fused_conv1d_gdn`](wrapper.md#fused_conv1d_gdn), [`WeightRefs`](memory_ref.md#WeightRefs)

### <a id="InBufferedRef"></a>`InBufferedRef`  ·  implements/extends BaseBufferedRef
- def: [`src/vllm_torchtpu/kernels/gdn/v3/memory_ref.py:174`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/memory_ref.py#L174)
- signature: `class InBufferedRef(BaseBufferedRef):`
- members:
  - <a id="InBufferedRef.copy_in"></a>`copy_in(self, src_ref: jax.Ref, grid_indices: tuple[int | jax.Array])` — [`L175`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/memory_ref.py#L175)
  - <a id="InBufferedRef.wait_in"></a>`wait_in(self, src_ref: jax.Ref, grid_indices: tuple[int | jax.Array])` — [`L192`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/memory_ref.py#L192)
- uses (calls/refs, reference-scoped): [`seq_tile_size`](config.md#GDNConfig.seq_tile_size), [`metadata_ref`](memory_ref.md#BaseBufferedRef.metadata_ref), [`cfg`](memory_ref.md#BaseBufferedRef.cfg), [`BaseBufferedRef`](memory_ref.md#BaseBufferedRef), [`p_id_to_r_size`](memory_ref.md#MetadataRef.p_id_to_r_size), [`p_id_to_r_base`](memory_ref.md#MetadataRef.p_id_to_r_base)
- used by: [`create_allocs`](memory_ref.md#create_allocs), [`BaseBufferedRef`](memory_ref.md#BaseBufferedRef)

### <a id="MetadataRef"></a>`MetadataRef`
- def: [`src/vllm_torchtpu/kernels/gdn/v3/memory_ref.py:76`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/memory_ref.py#L76)
- signature: `class MetadataRef:`
- members:
  - <a id="MetadataRef.create"></a>`create(cls, cfgs: config.GDNConfig, num_tiles: jax.Array, p_id_to_s_idx: jax.Array, p_id_to_r_base: jax.Array, p_id_to_r_size: jax.Array, p_id_is_first_tile: jax.Array, p_id_is_last_tile: jax.Array, s_idx_has_initial_state: jax.Array, s_idx_to_state_indices: jax.Array, s_idx_to_read_offset: jax.Array, s_idx_to_ckpt_indices: jax.Array | None = None)` — [`L100`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/memory_ref.py#L100)
  - <a id="MetadataRef.num_tiles"></a>`num_tiles` — [`L77`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/memory_ref.py#L77)
  - <a id="MetadataRef.p_id_is_first_tile"></a>`p_id_is_first_tile` — [`L81`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/memory_ref.py#L81)
  - <a id="MetadataRef.p_id_is_last_tile"></a>`p_id_is_last_tile` — [`L82`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/memory_ref.py#L82)
  - <a id="MetadataRef.p_id_to_r_base"></a>`p_id_to_r_base` — [`L79`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/memory_ref.py#L79)
  - <a id="MetadataRef.p_id_to_r_size"></a>`p_id_to_r_size` — [`L80`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/memory_ref.py#L80)
  - <a id="MetadataRef.p_id_to_s_idx"></a>`p_id_to_s_idx` — [`L78`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/memory_ref.py#L78)
  - <a id="MetadataRef.s_idx_has_initial_state"></a>`s_idx_has_initial_state` — [`L83`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/memory_ref.py#L83)
  - <a id="MetadataRef.s_idx_to_ckpt_indices"></a>`s_idx_to_ckpt_indices` — [`L97`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/memory_ref.py#L97)
  - <a id="MetadataRef.s_idx_to_read_offset"></a>`s_idx_to_read_offset` — [`L89`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/memory_ref.py#L89)
  - <a id="MetadataRef.s_idx_to_state_indices"></a>`s_idx_to_state_indices` — [`L84`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/memory_ref.py#L84)
- protocol/private: <a id="MetadataRef.__len__"></a>`__len__`[`L129`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/memory_ref.py#L129)
- uses (calls/refs, reference-scoped): [`seq_tile_size`](config.md#GDNConfig.seq_tile_size), [`GDNConfig`](config.md#GDNConfig), [`SmemWrapper`](memory_ref.md#SmemWrapper)
- used by: [`inner_kernel`](wrapper.md#inner_kernel), [`create_allocs`](memory_ref.md#create_allocs), [`copy_in`](memory_ref.md#StateInBufferedRef.copy_in), [`copy_out`](memory_ref.md#StateOutBufferedRef.copy_out), [`load_and_select_states`](vmem_ldst.md#load_and_select_states), [`metadata_ref`](memory_ref.md#BaseBufferedRef.metadata_ref), [`outer_kernel`](wrapper.md#outer_kernel), [`compute_per_seq_metadata`](metadata.md#compute_per_seq_metadata), [`wait_in`](memory_ref.md#StateInBufferedRef.wait_in), [`wait_out`](memory_ref.md#StateOutBufferedRef.wait_out), [`copy_in`](memory_ref.md#InBufferedRef.copy_in), [`copy_out`](memory_ref.md#OutBufferedRef.copy_out), [`compute_batched_seq_metadata`](metadata.md#compute_batched_seq_metadata), [`wait_in`](memory_ref.md#InBufferedRef.wait_in), [`wait_out`](memory_ref.md#OutBufferedRef.wait_out), [`_ckpt_state_idx`](memory_ref.md#_GranuleStateRef._ckpt_state_idx), [`create`](memory_ref.md#BaseBufferedRef.create)

### <a id="OutBufferedRef"></a>`OutBufferedRef`  ·  implements/extends BaseBufferedRef
- def: [`src/vllm_torchtpu/kernels/gdn/v3/memory_ref.py:213`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/memory_ref.py#L213)
- signature: `class OutBufferedRef(BaseBufferedRef):`
- members:
  - <a id="OutBufferedRef.copy_out"></a>`copy_out(self, dst_ref: jax.Ref, grid_indices: tuple[int | jax.Array])` — [`L214`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/memory_ref.py#L214)
  - <a id="OutBufferedRef.wait_out"></a>`wait_out(self, dst_ref: jax.Ref, grid_indices: tuple[int | jax.Array])` — [`L231`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/memory_ref.py#L231)
- uses (calls/refs, reference-scoped): [`seq_tile_size`](config.md#GDNConfig.seq_tile_size), [`metadata_ref`](memory_ref.md#BaseBufferedRef.metadata_ref), [`cfg`](memory_ref.md#BaseBufferedRef.cfg), [`BaseBufferedRef`](memory_ref.md#BaseBufferedRef), [`p_id_to_r_size`](memory_ref.md#MetadataRef.p_id_to_r_size), [`p_id_to_r_base`](memory_ref.md#MetadataRef.p_id_to_r_base)
- used by: [`create_allocs`](memory_ref.md#create_allocs), [`BaseBufferedRef`](memory_ref.md#BaseBufferedRef)

### <a id="SmemWrapper"></a>`SmemWrapper`
- def: [`src/vllm_torchtpu/kernels/gdn/v3/memory_ref.py:55`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/memory_ref.py#L55)
- doc: Maps physical 1-D data into logical N-D representation.
- signature: `class SmemWrapper:`
- members:
  - <a id="SmemWrapper.data"></a>`data` — [`L58`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/memory_ref.py#L58)
  - <a id="SmemWrapper.shape"></a>`shape` — [`L59`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/memory_ref.py#L59)
- protocol/private: <a id="SmemWrapper.__getitem__"></a>`__getitem__`[`L70`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/memory_ref.py#L70), <a id="SmemWrapper._get_pos"></a>`_get_pos`[`L61`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/memory_ref.py#L61)
- used by: [`create`](memory_ref.md#MetadataRef.create), [`p_id_to_r_size`](memory_ref.md#MetadataRef.p_id_to_r_size), [`p_id_to_s_idx`](memory_ref.md#MetadataRef.p_id_to_s_idx), [`p_id_is_first_tile`](memory_ref.md#MetadataRef.p_id_is_first_tile), [`p_id_is_last_tile`](memory_ref.md#MetadataRef.p_id_is_last_tile), [`p_id_to_r_base`](memory_ref.md#MetadataRef.p_id_to_r_base)

### <a id="StateInBufferedRef"></a>`StateInBufferedRef`  ·  implements/extends _GranuleStateRef
- def: [`src/vllm_torchtpu/kernels/gdn/v3/memory_ref.py:279`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/memory_ref.py#L279)
- doc: Input buffered ref for the per-sequence initial state (conv / recurrent).
- signature: `class StateInBufferedRef(_GranuleStateRef):`
- members:
  - <a id="StateInBufferedRef.copy_in"></a>`copy_in(self, src_ref: jax.Ref, grid_indices: tuple[int | jax.Array])` — [`L291`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/memory_ref.py#L291) — documented in [gated-deltanet-kernels](../../../../../../concepts/gated-deltanet-kernels.md)
  - <a id="StateInBufferedRef.wait_in"></a>`wait_in(self, src_ref: jax.Ref, grid_indices: tuple[int | jax.Array])` — [`L322`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/memory_ref.py#L322)
- uses (calls/refs, reference-scoped): [`seq_tile_size`](config.md#GDNConfig.seq_tile_size), [`metadata_ref`](memory_ref.md#BaseBufferedRef.metadata_ref), [`cfg`](memory_ref.md#BaseBufferedRef.cfg), [`_GranuleStateRef`](memory_ref.md#_GranuleStateRef), [`_ckpt_state_idx`](memory_ref.md#_GranuleStateRef._ckpt_state_idx), [`p_id_to_s_idx`](memory_ref.md#MetadataRef.p_id_to_s_idx), [`p_id_is_first_tile`](memory_ref.md#MetadataRef.p_id_is_first_tile), [`granule_view`](memory_ref.md#granule_view), [`s_idx_has_initial_state`](memory_ref.md#MetadataRef.s_idx_has_initial_state), [`offset`](memory_ref.md#_GranuleStateRef.offset), [`s_idx_to_read_offset`](memory_ref.md#MetadataRef.s_idx_to_read_offset)
- used by: [`create_allocs`](memory_ref.md#create_allocs), [`_GranuleStateRef`](memory_ref.md#_GranuleStateRef)

### <a id="StateOutBufferedRef"></a>`StateOutBufferedRef`  ·  implements/extends _GranuleStateRef
- def: [`src/vllm_torchtpu/kernels/gdn/v3/memory_ref.py:347`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/memory_ref.py#L347)
- doc: Output buffered ref for the per-sequence state checkpoints.
- signature: `class StateOutBufferedRef(_GranuleStateRef):`
- members:
  - <a id="StateOutBufferedRef.copy_out"></a>`copy_out(self, dst_ref: jax.Ref, grid_indices: tuple[int | jax.Array])` — [`L357`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/memory_ref.py#L357) — documented in [gated-deltanet-kernels](../../../../../../concepts/gated-deltanet-kernels.md)
  - <a id="StateOutBufferedRef.wait_out"></a>`wait_out(self, dst_ref: jax.Ref, grid_indices: tuple[int | jax.Array])` — [`L391`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/memory_ref.py#L391)
- uses (calls/refs, reference-scoped): [`seq_tile_size`](config.md#GDNConfig.seq_tile_size), [`metadata_ref`](memory_ref.md#BaseBufferedRef.metadata_ref), [`window_size`](config.md#GDNConfig.window_size), [`cfg`](memory_ref.md#BaseBufferedRef.cfg), [`_GranuleStateRef`](memory_ref.md#_GranuleStateRef), [`_ckpt_state_idx`](memory_ref.md#_GranuleStateRef._ckpt_state_idx), [`p_id_to_r_size`](memory_ref.md#MetadataRef.p_id_to_r_size), [`p_id_to_s_idx`](memory_ref.md#MetadataRef.p_id_to_s_idx), [`p_id_is_last_tile`](memory_ref.md#MetadataRef.p_id_is_last_tile), [`granule_view`](memory_ref.md#granule_view), [`offset`](memory_ref.md#_GranuleStateRef.offset)
- used by: [`create_allocs`](memory_ref.md#create_allocs), [`_GranuleStateRef`](memory_ref.md#_GranuleStateRef)

### <a id="WeightRefs"></a>`WeightRefs`
- def: [`src/vllm_torchtpu/kernels/gdn/v3/memory_ref.py:48`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/memory_ref.py#L48)
- signature: `class WeightRefs:`
- members:
  - <a id="WeightRefs.conv"></a>`conv` — [`L49`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/memory_ref.py#L49)
  - <a id="WeightRefs.gdn"></a>`gdn` — [`L50`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/memory_ref.py#L50)
- uses (calls/refs, reference-scoped): [`ConvWeightsRef`](memory_ref.md#ConvWeightsRef), [`GDNWeightsRef`](memory_ref.md#GDNWeightsRef)
- used by: [`inner_kernel`](wrapper.md#inner_kernel), [`fused_conv1d_gdn`](wrapper.md#fused_conv1d_gdn), [`outer_kernel`](wrapper.md#outer_kernel)

### <a id="_GranuleStateRef"></a>`_GranuleStateRef`  ·  implements/extends BaseBufferedRef
- def: [`src/vllm_torchtpu/kernels/gdn/v3/memory_ref.py:252`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/memory_ref.py#L252)
- doc: Shared addressing of the per-sequence state refs below.
- signature: `class _GranuleStateRef(BaseBufferedRef):`
- members:
  - <a id="_GranuleStateRef._ckpt_state_idx"></a>`_ckpt_state_idx(self, s_idx, ckpt)` — [`L263`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/memory_ref.py#L263) — Source block holding checkpoint `ckpt` of sequence `s_idx`.
  - <a id="_GranuleStateRef.offset"></a>`offset` — [`L261`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/memory_ref.py#L261)
- uses (calls/refs, reference-scoped): [`metadata_ref`](memory_ref.md#BaseBufferedRef.metadata_ref), [`BaseBufferedRef`](memory_ref.md#BaseBufferedRef), [`StateInBufferedRef`](memory_ref.md#StateInBufferedRef), [`StateOutBufferedRef`](memory_ref.md#StateOutBufferedRef), [`s_idx_to_ckpt_indices`](memory_ref.md#MetadataRef.s_idx_to_ckpt_indices), [`s_idx_to_state_indices`](memory_ref.md#MetadataRef.s_idx_to_state_indices)
- used by: [`copy_in`](memory_ref.md#StateInBufferedRef.copy_in), [`copy_out`](memory_ref.md#StateOutBufferedRef.copy_out), [`BaseBufferedRef`](memory_ref.md#BaseBufferedRef), [`StateInBufferedRef`](memory_ref.md#StateInBufferedRef), [`StateOutBufferedRef`](memory_ref.md#StateOutBufferedRef)

## Functions
- <a id="create_allocs"></a>`create_allocs(metadata_ref: MetadataRef, qkv_ref: jax.Array, b_ref: jax.Array, a_ref: jax.Array, out_ref: jax.Array, conv_state_ref: jax.Array, recurrent_state_ref: jax.Array, cfg: config.GDNConfig)` — [`L412`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/memory_ref.py#L412) — Allocate the pipeline's buffered refs. — documented in [gated-deltanet-kernels](../../../../../../concepts/gated-deltanet-kernels.md)
- <a id="granule_view"></a>`granule_view(ref: jax.Ref, leading_shape: tuple[int, ...])` — [`L27`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/memory_ref.py#L27)

