---
title: 'Module: torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask_info.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask_info.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.kernels.sbd_splash.splash_attention_mask_info`/
symbols:
  _process_mask: _process_mask().
  _process_dynamic_mask: _process_dynamic_mask().
  MaskInfo.block_mask: MaskInfo#block_mask.
  MaskInfo.partial_mask_blocks: MaskInfo#partial_mask_blocks.
  MaskInfo.active_rows: MaskInfo#active_rows.
  MaskInfo.q_sequence: MaskInfo#q_sequence.
  MaskInfo.num_active_blocks: MaskInfo#num_active_blocks.
  MaskInfo.mask_next: MaskInfo#mask_next.
  MaskInfo.active_cols: MaskInfo#active_cols.
  MaskInfo: MaskInfo#
  _check_mask: _check_mask().
  _HashableNDArray.__init__: _HashableNDArray#__init__().
  _HashableNDArray.__eq__: _HashableNDArray#__eq__().
  _downcast_to_small_type: _downcast_to_small_type().
  _HashableNDArray: _HashableNDArray#
  process_mask: process_mask.
  _HashableNDArray.array: _HashableNDArray#array.
  _HashableNDArray.__hash__: _HashableNDArray#__hash__().
  process_mask_dkv: process_mask_dkv.
  process_dynamic_mask: process_dynamic_mask.
  process_dynamic_mask_dkv: process_dynamic_mask_dkv.
  find_bounds: find_bounds().
  lax: lax.
  MaskCallable: MaskCallable.
  _generate_shard_metadata: _generate_shard_metadata().
  _process_dynamic_mask._downcast: _process_dynamic_mask()._downcast().
  _HashableNDArray.__slots__: _HashableNDArray#__slots__.
---
# Module: [`torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask_info.py`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask_info.py)

## Classes
### <a id="MaskInfo"></a>`MaskInfo`  ·  implements/extends NamedTuple
- def: [`torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask_info.py:38`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask_info.py#L38) — documented in [tpu-pallas-kernels](../../../../../../concepts/tpu-pallas-kernels.md)
- doc: Contains runtime masking information for the Splash attention kernel.
- signature: `class MaskInfo(NamedTuple):`
- members:
  - <a id="MaskInfo.active_cols"></a>`active_cols` — [`L71`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask_info.py#L71)
  - <a id="MaskInfo.active_rows"></a>`active_rows` — [`L70`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask_info.py#L70)
  - <a id="MaskInfo.block_mask"></a>`block_mask` — [`L72`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask_info.py#L72)
  - <a id="MaskInfo.mask_next"></a>`mask_next` — [`L69`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask_info.py#L69)
  - <a id="MaskInfo.num_active_blocks"></a>`num_active_blocks` — [`L73`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask_info.py#L73)
  - <a id="MaskInfo.partial_mask_blocks"></a>`partial_mask_blocks` — [`L74`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask_info.py#L74)
  - <a id="MaskInfo.q_sequence"></a>`q_sequence` — [`L75`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask_info.py#L75)
- used by: [`_splash_attention_forward`](splash_attention_kernel.md#_splash_attention_forward), [`_splash_attention_bwd_dkv`](splash_attention_kernel.md#_splash_attention_bwd_dkv), [`_make_splash_attention`](splash_attention_kernel.md#_make_splash_attention), [`_make_dynamic_splash_attention`](splash_attention_kernel.md#_make_dynamic_splash_attention), [`_process_mask`](splash_attention_mask_info.md#_process_mask), [`manual_sharding_spec`](splash_attention_kernel.md#SplashAttentionKernel.manual_sharding_spec), [`_process_dynamic_mask`](splash_attention_mask_info.md#_process_dynamic_mask), [`MaskInfo`](splash_attention_kernel.md#MaskInfo), [`MaskInfo`](base.md#MaskInfo)  (1 test-only)

### <a id="_HashableNDArray"></a>`_HashableNDArray`
- def: [`torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask_info.py:147`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask_info.py#L147)
- doc: Helper to make a numpy array hashable: can be added associative containers.
- signature: `class _HashableNDArray:`
- members:
  - <a id="_HashableNDArray.array"></a>`array` — [`L155`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask_info.py#L155)
- protocol/private: <a id="_HashableNDArray.__eq__"></a>`__eq__`[`L164`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask_info.py#L164), <a id="_HashableNDArray.__hash__"></a>`__hash__`[`L161`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask_info.py#L161), <a id="_HashableNDArray.__init__"></a>`__init__`[`L157`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask_info.py#L157), <a id="_HashableNDArray.__slots__"></a>`__slots__`[`L154`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask_info.py#L154)
- used by: [`_process_mask`](splash_attention_mask_info.md#_process_mask)

## Functions
- <a id="_check_mask"></a>`_check_mask(mask: mask_lib.Mask)` — [`L114`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask_info.py#L114) — Check that the given mask is valid.
- <a id="_process_dynamic_mask._downcast"></a>`_downcast(array: jax.Array, max_value: int)` — [`L311`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask_info.py#L311)
- <a id="_downcast_to_small_type"></a>`_downcast_to_small_type(array: np.ndarray)` — [`L78`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask_info.py#L78) — Downcast numpy array.
- <a id="_generate_shard_metadata"></a>`_generate_shard_metadata(block_mask: np.ndarray, partial_blocks: np.ndarray, is_dkv: bool, return_dynamic_grid: bool)` — [`L170`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask_info.py#L170)
- <a id="_process_dynamic_mask"></a>`_process_dynamic_mask(mask: jax.Array, block_shape: tuple[int, int], is_dkv: bool, *, downcast_smem_data: bool = True, partial_mask_blocks_dtype: jax.typing.DTypeLike = np.int8)` — [`L218`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask_info.py#L218) — Process a dynamic mask to compute it's local sparsity data. — documented in [tpu-pallas-kernels](../../../../../../concepts/tpu-pallas-kernels.md)
- <a id="_process_mask"></a>`_process_mask(mask: mask_lib.Mask, block_shape: tuple[int, int], is_dkv: bool, *, downcast_smem_data: bool = True, partial_mask_blocks_dtype: jax.typing.DTypeLike = np.int8, q_seq_shards: int = 1, kv_seq_shards: int = 1, return_dynamic_grid: bool = True)` — [`L345`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask_info.py#L345) — Transform a dense mask into a sparse representation. — documented in [tpu-pallas-kernels](../../../../../../concepts/tpu-pallas-kernels.md)
- <a id="find_bounds"></a>`find_bounds(arr: jax.Array | np.ndarray)` — [`L20`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask_info.py#L20)

## Module values
- <a id="MaskCallable"></a>`MaskCallable` — [`L17`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask_info.py#L17)
- <a id="lax"></a>`lax` — [`L16`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask_info.py#L16)
- <a id="process_dynamic_mask"></a>`process_dynamic_mask` — [`L563`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask_info.py#L563)
- <a id="process_dynamic_mask_dkv"></a>`process_dynamic_mask_dkv` — [`L564`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask_info.py#L564)
- <a id="process_mask"></a>`process_mask` — [`L560`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask_info.py#L560)
- <a id="process_mask_dkv"></a>`process_mask_dkv` — [`L561`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask_info.py#L561)

