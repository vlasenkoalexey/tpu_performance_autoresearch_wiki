---
title: 'Module: src/vllm_torchtpu/layers/core/fused_moe_gmm.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/layers/core/fused_moe_gmm.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.layers.core.fused_moe_gmm`/
symbols:
  moe_gmm: moe_gmm().
  fused_moe_func: fused_moe_func().
  prepare_routed_gmm_inputs: prepare_routed_gmm_inputs().
  resolve_onehot_permute_threshold: resolve_onehot_permute_threshold().
  _select_ragged_gather_reduce: _select_ragged_gather_reduce().
  ragged_gather_reduce: ragged_gather_reduce.
  logger: logger.
  gmm_wrapper: gmm_wrapper().
  _DENSE_EXPERT_THRESHOLD: _DENSE_EXPERT_THRESHOLD.
  _SINGLE_SORT: _SINGLE_SORT.
  _COUNTING_SORT: _COUNTING_SORT.
  _COUNTING_SORT_SCATTER_MAX_ROWS: _COUNTING_SORT_SCATTER_MAX_ROWS.
  _counting_sort_positions: _counting_sort_positions().
  _COUNTING_SORT_BLOCK: _COUNTING_SORT_BLOCK.
  _SINGLE_SORT_MAX_ROWS: _SINGLE_SORT_MAX_ROWS.
  unpack_fp4_to_e2m1: unpack_fp4_to_e2m1().
  requant_unpack_kmajor: requant_unpack_kmajor().
  quantize_to_native_fp4_kmajor: quantize_to_native_fp4_kmajor().
  _ONEHOT_AUTO_CAP: _ONEHOT_AUTO_CAP.
  _single_sort_permutation: _single_sort_permutation().
---
# Module: [`src/vllm_torchtpu/layers/core/fused_moe_gmm.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/fused_moe_gmm.py)

## Functions
- <a id="_counting_sort_positions"></a>`_counting_sort_positions(sort_keys: jax.Array, num_buckets: int)` — [`L237`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/fused_moe_gmm.py#L237) — Stable counting sort: row -> its position in the sorted order.
- <a id="_select_ragged_gather_reduce"></a>`_select_ragged_gather_reduce(version: str)` — [`L49`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/fused_moe_gmm.py#L49)
- <a id="_single_sort_permutation"></a>`_single_sort_permutation(sort_keys: jax.Array, topk: int, flat_bits: int)` — [`L316`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/fused_moe_gmm.py#L316) — Returns the stable argsort of `sort_keys`, its inverse, and token ids.
- <a id="fused_moe_func"></a>`fused_moe_func(hidden_states: jax.Array, w1: jax.Array, w2: jax.Array, w1_scale: jax.Array | None, w2_scale: jax.Array | None, w1_bias: jax.Array | None, w2_bias: jax.Array | None, topk_weights: jax.Array, topk_ids: jax.Array, experts_start: jax.Array | None = None, topk: int = 1, activation: str = "silu", use_ep: bool = False, use_sparse_core: bool = True, onehot_moe_permute_threshold: int = 0, rhs_quant_dtype: jnp.dtype | None = None, skip_padded_tokens: bool = False)` — [`L673`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/fused_moe_gmm.py#L673) — Run MoE with precomputed expert ids and weights. — documented in [attention-and-layer-core](../../../../../concepts/attention-and-layer-core.md)
- <a id="gmm_wrapper"></a>`gmm_wrapper(lhs, rhs, rhs_scale, rhs_bias, group_sizes, group_offset, zero_initialize=False, fuse_act=None, preferred_element_type=None, rhs_quant_dtype=None)` — [`L203`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/fused_moe_gmm.py#L203)
- <a id="moe_gmm"></a>`moe_gmm(x: jax.Array, w1: jax.Array, w1_scale: jax.Array | None, w1_bias: jax.Array | None, w2: jax.Array, w2_scale: jax.Array | None, w2_bias: jax.Array | None, group_sizes: jax.Array, argsort_revert_indices: jax.Array, topk_weights_flat: jax.Array, valid_mask_flat: jax.Array, token_indices_sorted: jax.Array, *, activation: str, num_tokens: int, topk: int, use_ep: bool, use_sparse_core: bool, onehot_moe_permute_threshold: int = 0, rhs_quant_dtype: jnp.dtype | None = None)` — [`L492`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/fused_moe_gmm.py#L492) — Run grouped GEMM for routed tokens and reduce back to tokens. — documented in [attention-and-layer-core](../../../../../concepts/attention-and-layer-core.md)
- <a id="prepare_routed_gmm_inputs"></a>`prepare_routed_gmm_inputs(hidden_states_local: jax.Array, topk_indices_local: jax.Array, topk_weights_local: jax.Array, *, local_num_experts: int, topk: int, use_ep: bool, use_sparse_core: bool, onehot_moe_permute_threshold: int = 0, skip_padded_tokens: bool = False)` — [`L332`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/fused_moe_gmm.py#L332) — Prepare the local-only routing layout using already-local expert ids. — documented in [attention-and-layer-core](../../../../../concepts/attention-and-layer-core.md)
- <a id="quantize_to_native_fp4_kmajor"></a>`quantize_to_native_fp4_kmajor(w: jax.Array, block: int, pack: bool = True)` — [`L159`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/fused_moe_gmm.py#L159) — Quantize K-major float weight ([..., K, N]) to packed uint8 e2m1 and
- <a id="requant_unpack_kmajor"></a>`requant_unpack_kmajor(w_packed: jax.Array, scale_f: jax.Array, block: int)` — [`L126`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/fused_moe_gmm.py#L126) — W4A8 requantization in JAX: unpack the checkpoint block-16 fp4 weight,
- <a id="resolve_onehot_permute_threshold"></a>`resolve_onehot_permute_threshold()` — [`L89`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/fused_moe_gmm.py#L89) — Routed-row count at/below which MoE permute+combine run as TensorCore
- <a id="unpack_fp4_to_e2m1"></a>`unpack_fp4_to_e2m1(w_packed: jax.Array)` — [`L114`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/fused_moe_gmm.py#L114) — Unpack a uint8-packed E2M1 weight (2 fp4 per byte along the last axis)

## Module values
- <a id="_COUNTING_SORT"></a>`_COUNTING_SORT` — [`L71`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/fused_moe_gmm.py#L71)
- <a id="_COUNTING_SORT_BLOCK"></a>`_COUNTING_SORT_BLOCK` — [`L80`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/fused_moe_gmm.py#L80)
- <a id="_COUNTING_SORT_SCATTER_MAX_ROWS"></a>`_COUNTING_SORT_SCATTER_MAX_ROWS` — [`L86`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/fused_moe_gmm.py#L86)
- <a id="_DENSE_EXPERT_THRESHOLD"></a>`_DENSE_EXPERT_THRESHOLD` — [`L65`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/fused_moe_gmm.py#L65)
- <a id="_ONEHOT_AUTO_CAP"></a>`_ONEHOT_AUTO_CAP` — [`L63`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/fused_moe_gmm.py#L63)
- <a id="_SINGLE_SORT"></a>`_SINGLE_SORT` — [`L67`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/fused_moe_gmm.py#L67)
- <a id="_SINGLE_SORT_MAX_ROWS"></a>`_SINGLE_SORT_MAX_ROWS` — [`L77`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/fused_moe_gmm.py#L77)
- <a id="logger"></a>`logger` — [`L46`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/fused_moe_gmm.py#L46)
- <a id="ragged_gather_reduce"></a>`ragged_gather_reduce` — [`L61`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/fused_moe_gmm.py#L61)

