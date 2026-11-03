---
title: 'Module: src/vllm_torchtpu/kernels/flash_attention/kernel.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/flash_attention/kernel.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.flash_attention.kernel`/
symbols:
  flash_attention: flash_attention().
  _flash_attention_impl: _flash_attention_impl().
  BlockSizes.get_default: BlockSizes#get_default().
  calculate_vmem_usage_bytes: calculate_vmem_usage_bytes().
  mha_reference_no_custom_vjp: mha_reference_no_custom_vjp().
  MIN_BLOCK_SIZE: MIN_BLOCK_SIZE.
  BlockSizes.block_b: BlockSizes#block_b.
  _fwd_cost_estimate: _fwd_cost_estimate().
  mha_reference: mha_reference().
  BlockSizes.block_q: BlockSizes#block_q.
  BlockSizes.__post_init__: BlockSizes#__post_init__().
  _flash_attention_kernel_single_batch.run._body: _flash_attention_kernel_single_batch().run()._body().
  NUM_LANES: NUM_LANES.
  SegmentIds: SegmentIds#
  BlockSizes: BlockSizes#
  _flash_attention_kernel: _flash_attention_kernel().
  _flash_attention_kernel_single_batch_single_step: _flash_attention_kernel_single_batch_single_step().
  _mha_reference: _mha_reference().
  _flash_attention_impl.kv_index_map: _flash_attention_impl().kv_index_map().
  BlockSizes.block_k_major: BlockSizes#block_k_major.
  BlockSizes.block_k: BlockSizes#block_k.
  below_or_on_diag: below_or_on_diag().
  _verify_block: _verify_block().
  _flash_attention: _flash_attention().
  _flash_attention_kernel_single_batch: _flash_attention_kernel_single_batch().
  _flash_attention_impl.ab_index_map: _flash_attention_impl().ab_index_map().
  _flash_attention_impl.kv_segment_ids_index_map: _flash_attention_impl().kv_segment_ids_index_map().
  DEFAULT_MASK_VALUE: DEFAULT_MASK_VALUE.
  NUM_SUBLANES: NUM_SUBLANES.
  SegmentIds.q: SegmentIds#q.
  SegmentIds.kv: SegmentIds#kv.
  TRANS_B_DIM_NUMBERS: TRANS_B_DIM_NUMBERS.
  _bytes: _bytes().
  _flash_attention_impl.lm_index_map: _flash_attention_impl().lm_index_map().
  BlockSizes.verify_major_minor: BlockSizes#verify_major_minor().
  _flash_attention_impl.q_index_map: _flash_attention_impl().q_index_map().
  _flash_attention_impl.o_index_map: _flash_attention_impl().o_index_map().
  _flash_attention_impl.q_segment_ids_index_map: _flash_attention_impl().q_segment_ids_index_map().
  _flash_attention_kernel_single_batch.start_new_sequence: _flash_attention_kernel_single_batch().start_new_sequence().
  _flash_attention_kernel_single_batch.run: _flash_attention_kernel_single_batch().run().
  _flash_attention_kernel_single_batch.store_output: _flash_attention_kernel_single_batch().store_output().
---
# Module: [`src/vllm_torchtpu/kernels/flash_attention/kernel.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/flash_attention/kernel.py)

## Classes
### <a id="BlockSizes"></a>`BlockSizes`
- def: [`src/vllm_torchtpu/kernels/flash_attention/kernel.py:58`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/flash_attention/kernel.py#L58)
- doc: Tile sizes parameterizing FlashAttention kernels.
- signature: `class BlockSizes:`
- members:
  - <a id="BlockSizes.get_default"></a>`get_default(cls, batch_size, num_heads, q_seq_len, kv_len, d_model)` — [`L86`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/flash_attention/kernel.py#L86)
  - <a id="BlockSizes.verify_major_minor"></a>`verify_major_minor(prefix, suffix, major, minor)` — [`L71`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/flash_attention/kernel.py#L71)
  - <a id="BlockSizes.block_b"></a>`block_b` — [`L68`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/flash_attention/kernel.py#L68)
  - <a id="BlockSizes.block_k"></a>`block_k` — [`L67`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/flash_attention/kernel.py#L67)
  - <a id="BlockSizes.block_k_major"></a>`block_k_major` — [`L66`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/flash_attention/kernel.py#L66)
  - <a id="BlockSizes.block_q"></a>`block_q` — [`L65`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/flash_attention/kernel.py#L65)
- protocol/private: <a id="BlockSizes.__post_init__"></a>`__post_init__`[`L70`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/flash_attention/kernel.py#L70)
- used by: [`flash_attention`](kernel.md#flash_attention), [`calculate_vmem_usage_bytes`](kernel.md#calculate_vmem_usage_bytes)

### <a id="SegmentIds"></a>`SegmentIds`  ·  implements/extends NamedTuple
- def: [`src/vllm_torchtpu/kernels/flash_attention/kernel.py:40`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/flash_attention/kernel.py#L40)
- doc: SegmentIds for Q and KV sequences.
- signature: `class SegmentIds(NamedTuple):`
- members:
  - <a id="SegmentIds.kv"></a>`kv` — [`L54`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/flash_attention/kernel.py#L54)
  - <a id="SegmentIds.q"></a>`q` — [`L53`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/flash_attention/kernel.py#L53)
- used by: [`_vision_flash_core`](../../layers/adapter/vision_attention.md#_vision_flash_core), [`mha_reference_no_custom_vjp`](kernel.md#mha_reference_no_custom_vjp), [`_fwd_cost_estimate`](kernel.md#_fwd_cost_estimate), [`mha_reference`](kernel.md#mha_reference), [`_mha_reference`](kernel.md#_mha_reference)

## Functions
- <a id="_flash_attention_kernel_single_batch.run._body"></a>`_body(start_k)` — [`L354`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/flash_attention/kernel.py#L354)
- <a id="_bytes"></a>`_bytes(x: jax.Array | jax.ShapeDtypeStruct)` — [`L525`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/flash_attention/kernel.py#L525)
- <a id="_flash_attention"></a>`_flash_attention(q, k, v, ab, segment_ids, save_residuals, causal, sm_scale, block_sizes, vmem_limit_bytes, debug)` — [`L258`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/flash_attention/kernel.py#L258)
- <a id="_flash_attention_impl"></a>`_flash_attention_impl(q, k, v, ab, segment_ids, save_residuals, causal, sm_scale, block_b, block_q, block_k_major, block_k, vmem_limit_bytes, debug)` — [`L553`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/flash_attention/kernel.py#L553)
- <a id="_flash_attention_kernel"></a>`_flash_attention_kernel(q_tile_ref, *args, **kwargs)` — [`L299`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/flash_attention/kernel.py#L299)
- <a id="_flash_attention_kernel_single_batch"></a>`_flash_attention_kernel_single_batch(batch_idx: tuple[int, ...], q_tile_ref, k_tile_ref, v_tile_ref, ab_tile_ref, q_segment_ids_tile_ref, kv_segment_ids_tile_ref, o_tile_ref, l_ref, m_ref, m_scratch_ref, l_scratch_ref, acc_scratch_ref, *, causal, sm_scale, block_k, kv_seq_len, mask_value)` — [`L310`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/flash_attention/kernel.py#L310)
- <a id="_flash_attention_kernel_single_batch_single_step"></a>`_flash_attention_kernel_single_batch_single_step(batch_idx: tuple[int, ...], q_tile_ref, k_tile_ref, v_tile_ref, ab_tile_ref, q_segment_ids_tile_ref, kv_segment_ids_tile_ref, o_tile_ref, l_ref: Any | None = None, m_ref: Any | None = None, *, causal, sm_scale, block_k, kv_seq_len, mask_value)` — [`L453`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/flash_attention/kernel.py#L453)
- <a id="_fwd_cost_estimate"></a>`_fwd_cost_estimate(q: jax.Array, k: jax.Array, v: jax.Array, ab: jax.Array | None, segment_ids: SegmentIds | None, *, causal: bool, sm_scale: jax.Array | None, kernel_inputs_specs, kernel_outputs_specs)` — [`L529`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/flash_attention/kernel.py#L529)
- <a id="_mha_reference"></a>`_mha_reference(q, k, v, ab, segment_ids: SegmentIds | None, causal: bool, mask_value: float, sm_scale: float, save_residuals: bool)` — [`L834`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/flash_attention/kernel.py#L834)
- <a id="_verify_block"></a>`_verify_block(block_name, dim_name, block, dim, should_divide=True)` — [`L858`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/flash_attention/kernel.py#L858)
- <a id="_flash_attention_impl.ab_index_map"></a>`ab_index_map(batch_index, head_index, q_seq_index, kv_seq_index)` — [`L600`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/flash_attention/kernel.py#L600)
- <a id="below_or_on_diag"></a>`below_or_on_diag(r, r_blk_size, c, c_blk_size)` — [`L293`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/flash_attention/kernel.py#L293)
- <a id="calculate_vmem_usage_bytes"></a>`calculate_vmem_usage_bytes(block_sizes: BlockSizes, q_dtype, kv_dtype, head_dim: int, kv_seq_len: int, ab=None, segment_ids=None)` — [`L97`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/flash_attention/kernel.py#L97) — Estimate VMEM needed by the whole-KV single-step kernel.
- <a id="flash_attention"></a>`flash_attention(q, k, v, ab=None, segment_ids=None, *, causal: bool = False, sm_scale: float = 1, block_sizes: BlockSizes | None = None, vmem_limit_bytes: int | None, debug: bool = False)` — [`L150`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/flash_attention/kernel.py#L150)
- <a id="_flash_attention_impl.kv_index_map"></a>`kv_index_map(batch_index, head_index, q_seq_index, kv_seq_index)` — [`L587`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/flash_attention/kernel.py#L587)
- <a id="_flash_attention_impl.kv_segment_ids_index_map"></a>`kv_segment_ids_index_map(batch_index, head_index, q_seq_index, kv_seq_index)` — [`L678`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/flash_attention/kernel.py#L678)
- <a id="_flash_attention_impl.lm_index_map"></a>`lm_index_map(batch_index, head_index, q_seq_index, _)` — [`L624`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/flash_attention/kernel.py#L624)
- <a id="mha_reference"></a>`mha_reference(q, k, v, ab, segment_ids: SegmentIds | None = None, causal: bool = False, mask_value: float = DEFAULT_MASK_VALUE, sm_scale=1)` — [`L811`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/flash_attention/kernel.py#L811)
- <a id="mha_reference_no_custom_vjp"></a>`mha_reference_no_custom_vjp(q, k, v, ab: jax.Array | None = None, segment_ids: SegmentIds | None = None, *, causal: bool = False, mask_value: float = DEFAULT_MASK_VALUE, sm_scale: float = 1, save_residuals: bool = False)` — [`L765`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/flash_attention/kernel.py#L765)
- <a id="_flash_attention_impl.o_index_map"></a>`o_index_map(batch_index, head_index, q_seq_index, _)` — [`L621`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/flash_attention/kernel.py#L621)
- <a id="_flash_attention_impl.q_index_map"></a>`q_index_map(batch_index, head_index, q_seq_index, _)` — [`L584`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/flash_attention/kernel.py#L584)
- <a id="_flash_attention_impl.q_segment_ids_index_map"></a>`q_segment_ids_index_map(batch_index, head_index, q_seq_index, _)` — [`L674`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/flash_attention/kernel.py#L674)
- <a id="_flash_attention_kernel_single_batch.run"></a>`run()` — [`L352`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/flash_attention/kernel.py#L352)
- <a id="_flash_attention_kernel_single_batch.start_new_sequence"></a>`start_new_sequence()` — [`L338`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/flash_attention/kernel.py#L338)
- <a id="_flash_attention_kernel_single_batch.store_output"></a>`store_output()` — [`L443`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/flash_attention/kernel.py#L443)

## Module values
- <a id="DEFAULT_MASK_VALUE"></a>`DEFAULT_MASK_VALUE` — [`L35`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/flash_attention/kernel.py#L35)
- <a id="MIN_BLOCK_SIZE"></a>`MIN_BLOCK_SIZE` — [`L289`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/flash_attention/kernel.py#L289)
- <a id="NUM_LANES"></a>`NUM_LANES` — [`L36`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/flash_attention/kernel.py#L36)
- <a id="NUM_SUBLANES"></a>`NUM_SUBLANES` — [`L37`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/flash_attention/kernel.py#L37)
- <a id="TRANS_B_DIM_NUMBERS"></a>`TRANS_B_DIM_NUMBERS` — [`L290`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/flash_attention/kernel.py#L290)

