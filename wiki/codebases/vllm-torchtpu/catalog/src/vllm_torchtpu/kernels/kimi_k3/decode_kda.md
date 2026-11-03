---
title: 'Module: src/vllm_torchtpu/kernels/kimi_k3/decode_kda.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/kimi_k3/decode_kda.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.kimi_k3.decode_kda`/
symbols:
  _kernel: _kernel().
  decode_kda: decode_kda().
  _l2_norm: _l2_norm().
  decode_kda.seq_map: decode_kda().seq_map().
  _L2_EPS: _L2_EPS.
  _activate_gate: _activate_gate().
  _decode_step: _decode_step().
  __all__: __all__.
---
# Module: [`src/vllm_torchtpu/kernels/kimi_k3/decode_kda.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/decode_kda.py)

## Functions
- <a id="_activate_gate"></a>`_activate_gate(g, a_log, dt_bias, lower_bound)` — [`L46`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/decode_kda.py#L46) — KDA gate activation in the ``[n_v, d_k]`` layout.
- <a id="_decode_step"></a>`_decode_step(q, k, k_t, v, decay, beta, state, compute_dtype)` — [`L61`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/decode_kda.py#L61) — One KDA token step for one sequence.
- <a id="_kernel"></a>`_kernel(state_indices_ref, has_initial_state_ref, mixed_qkv_ref, g_ref, beta_ref, conv_state_ref, conv_weight_ref, a_log_ref, dt_bias_ref, state_ref, out_ref, conv_state_out_ref, state_out_ref, *, n_v: int, d_k: int, kernel_size: int, lower_bound: float | None, compute_dtype, scale: float, state_transposed: bool)` — [`L99`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/decode_kda.py#L99) — documented in [kimi-k3-kernels](../../../../../concepts/kimi-k3-kernels.md)
- <a id="_l2_norm"></a>`_l2_norm(x: jax.Array)` — [`L39`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/decode_kda.py#L39) — Normalize rows with float32 accumulation. — documented in [kimi-k3-kernels](../../../../../concepts/kimi-k3-kernels.md)
- <a id="decode_kda"></a>`decode_kda(mixed_qkv: jax.Array, g: jax.Array, beta: jax.Array, conv_state: jax.Array, conv_weight: jax.Array, state: jax.Array, a_log: jax.Array, dt_bias: jax.Array | None, state_indices: jax.Array, has_initial_state: jax.Array, *, lower_bound: float | None = None, compute_dtype: jnp.dtype = jnp.float32, scale: float | None = None, conv_state_dim_first: bool = False, state_transposed: bool = False)` — [`L208`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/decode_kda.py#L208) — One KDA decode step for ``num_seqs`` sequences, one token each. — documented in [kimi-k3-kernels](../../../../../concepts/kimi-k3-kernels.md)
- <a id="decode_kda.seq_map"></a>`seq_map(s, si, hi)` — [`L304`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/decode_kda.py#L304) — documented in [kimi-k3-kernels](../../../../../concepts/kimi-k3-kernels.md)

## Module values
- <a id="_L2_EPS"></a>`_L2_EPS` — [`L36`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/decode_kda.py#L36)
- <a id="__all__"></a>`__all__` — [`L34`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/decode_kda.py#L34)

