---
title: 'Module: src/vllm_torchtpu/layers/adapter/linear_common.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/layers/adapter/linear_common.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.layers.adapter.linear_common`/
symbols:
  WEIGHT_FLIPPED_ATTR: WEIGHT_FLIPPED_ATTR.
  _get_quantized_matmul_op: _get_quantized_matmul_op().
  _get_quantized_matmul_fp4_op: _get_quantized_matmul_fp4_op().
  KEEP_VLLM_LAYOUT_ATTR: KEEP_VLLM_LAYOUT_ATTR.
  _quantized_matmul_jax: _quantized_matmul_jax().
  _quantized_matmul_kernel_op._quantized_matmul_kernel_op: _quantized_matmul_kernel_op._quantized_matmul_kernel_op.
  _quantized_matmul_fp4_op._quantized_matmul_fp4_op: _quantized_matmul_fp4_op._quantized_matmul_fp4_op.
  quantized_matmul: quantized_matmul().
  quantized_matmul_fp4: quantized_matmul_fp4().
  logger: logger.
  _quantized_matmul_fp4_jax: _quantized_matmul_fp4_jax().
  sharded_quantized_matmul.wrapper: sharded_quantized_matmul().wrapper().
  sharded_quantized_matmul: sharded_quantized_matmul().
  get_model_matmul_fusion_assignment: get_model_matmul_fusion_assignment().
  _quantized_matmul_kernel_op_lock: _quantized_matmul_kernel_op_lock.
  _get_quantized_matmul_op._fake_quantized_matmul: _get_quantized_matmul_op()._fake_quantized_matmul().
  _quantized_matmul_fp4_op_lock: _quantized_matmul_fp4_op_lock.
  _get_quantized_matmul_fp4_op._fake_quantized_matmul_fp4: _get_quantized_matmul_fp4_op()._fake_quantized_matmul_fp4().
  MODEL_MATMUL_FUSION_TRUTH_TABLE: MODEL_MATMUL_FUSION_TRUTH_TABLE.
  _get_x_q_dtype: _get_x_q_dtype().
  reorder_concatenated_tensor_for_sharding: reorder_concatenated_tensor_for_sharding().
  slice_sharded_tensor_for_concatenation: slice_sharded_tensor_for_concatenation().
---
# Module: [`src/vllm_torchtpu/layers/adapter/linear_common.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/linear_common.py)

## Functions
- <a id="_get_quantized_matmul_op._fake_quantized_matmul"></a>`_fake_quantized_matmul(x: torch.Tensor, w_q: torch.Tensor, w_s: torch.Tensor, w8a16_max_rows: int = 0)` — [`L146`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/linear_common.py#L146)
- <a id="_get_quantized_matmul_fp4_op._fake_quantized_matmul_fp4"></a>`_fake_quantized_matmul_fp4(x: torch.Tensor, w_q: torch.Tensor, w_s: torch.Tensor)` — [`L229`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/linear_common.py#L229)
- <a id="_get_quantized_matmul_fp4_op"></a>`_get_quantized_matmul_fp4_op()` — [`L216`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/linear_common.py#L216)
- <a id="_get_quantized_matmul_op"></a>`_get_quantized_matmul_op()` — [`L135`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/linear_common.py#L135)
- <a id="_get_x_q_dtype"></a>`_get_x_q_dtype(w_q_dtype: jnp.dtype)` — [`L56`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/linear_common.py#L56) — Return the activation quant dtype paired with a given weight dtype.
- <a id="_quantized_matmul_fp4_jax"></a>`_quantized_matmul_fp4_jax(x: jax.Array, w_q: jax.Array, w_s: jax.Array)` — [`L188`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/linear_common.py#L188) — W4A16 dense matmul for NVFP4 weights via gmm_v2 (single group).
- <a id="_quantized_matmul_jax"></a>`_quantized_matmul_jax(x: jax.Array, w_q: jax.Array, w_s: jax.Array, w8a16_max_rows: int = 0)` — [`L69`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/linear_common.py#L69) — FP8 dense matmul on the canonical (k, n) weight layout.
- <a id="get_model_matmul_fusion_assignment"></a>`get_model_matmul_fusion_assignment(model_name: str, batch_size: int, tp_size: int, layer_name: str)` — [`L401`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/linear_common.py#L401)
- <a id="quantized_matmul"></a>`quantized_matmul(x: torch.Tensor, w_q: torch.Tensor, w_s: torch.Tensor, w8a16_max_rows: int = 0)` — [`L162`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/linear_common.py#L162) — Torch entry point for the runtime FP8 dense-linear matmul.
- <a id="quantized_matmul_fp4"></a>`quantized_matmul_fp4(x: torch.Tensor, w_q: torch.Tensor, w_s: torch.Tensor)` — [`L242`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/linear_common.py#L242) — Torch entry for the NVFP4 W4A16 dense-linear matmul.
- <a id="reorder_concatenated_tensor_for_sharding"></a>`reorder_concatenated_tensor_for_sharding(concatenated_tensor: jax.Array, split_sizes: list[int], n_shards: int, dim: int)` — [`L285`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/linear_common.py#L285) — Reorder a replicated concatenated tensor such that when sharded on multiple chips,
- <a id="sharded_quantized_matmul"></a>`sharded_quantized_matmul(x: jax.Array, w_q: jax.Array, w_s: jax.Array, mesh: Mesh, weight_sharding: P)` — [`L258`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/linear_common.py#L258)
- <a id="slice_sharded_tensor_for_concatenation"></a>`slice_sharded_tensor_for_concatenation(sharded_tensor: jax.Array, split_sizes: list[int], n_shards: int)` — [`L324`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/linear_common.py#L324) — Slice the input tensor which is sharded on multiple chips (on the last dim) into
- <a id="sharded_quantized_matmul.wrapper"></a>`wrapper(x, w_q, w_s)` — [`L270`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/linear_common.py#L270)

## Module values
- <a id="KEEP_VLLM_LAYOUT_ATTR"></a>`KEEP_VLLM_LAYOUT_ATTR` — [`L41`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/linear_common.py#L41) — documented in [quantization-methods](../../../../../concepts/quantization-methods.md)
- <a id="MODEL_MATMUL_FUSION_TRUTH_TABLE"></a>`MODEL_MATMUL_FUSION_TRUTH_TABLE` — [`L365`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/linear_common.py#L365)
- <a id="WEIGHT_FLIPPED_ATTR"></a>`WEIGHT_FLIPPED_ATTR` — [`L53`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/linear_common.py#L53) — documented in [kimi-k3-model](../../../../../concepts/kimi-k3-model.md)
- <a id="_quantized_matmul_fp4_op._quantized_matmul_fp4_op"></a>`_quantized_matmul_fp4_op` — [`L212`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/linear_common.py#L212)
- <a id="_quantized_matmul_fp4_op_lock"></a>`_quantized_matmul_fp4_op_lock` — [`L213`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/linear_common.py#L213)
- <a id="_quantized_matmul_kernel_op._quantized_matmul_kernel_op"></a>`_quantized_matmul_kernel_op` — [`L131`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/linear_common.py#L131)
- <a id="_quantized_matmul_kernel_op_lock"></a>`_quantized_matmul_kernel_op_lock` — [`L132`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/linear_common.py#L132)
- <a id="logger"></a>`logger` — [`L29`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/linear_common.py#L29)

