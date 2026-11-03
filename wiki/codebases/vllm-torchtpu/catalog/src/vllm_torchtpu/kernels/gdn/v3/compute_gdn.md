---
title: 'Module: src/vllm_torchtpu/kernels/gdn/v3/compute_gdn.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/gdn/v3/compute_gdn.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.gdn.v3.compute_gdn`/
symbols:
  recurrent_gdn: recurrent_gdn().
  chunked_gdn_per_seq: chunked_gdn_per_seq().
  chunked_gdn: chunked_gdn().
  recurrent_gdn_per_seq: recurrent_gdn_per_seq().
  fused_transpose_broadcast: fused_transpose_broadcast().
  get_mask_dtype: get_mask_dtype().
  l2_norm: l2_norm().
  invert_triangular_matrix: invert_triangular_matrix().
  invert_triangular_matrix.local_forward_sub: invert_triangular_matrix().local_forward_sub().
---
# Module: [`src/vllm_torchtpu/kernels/gdn/v3/compute_gdn.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/compute_gdn.py)

## Functions
- <a id="chunked_gdn"></a>`chunked_gdn(real_sizes: jax.Array, q_large: jax.Array, k_large: jax.Array, v_large: jax.Array, b_large: jax.Array, a_large: jax.Array, state_prev: jax.Array, a_log: jax.Array, dt_bias: jax.Array, cfg: config.GDNConfig)` — [`L252`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/compute_gdn.py#L252) — Perform chunked GDN over input [seq, num_heads, chunk, head_dim]. — documented in [gated-deltanet-kernels](../../../../../../concepts/gated-deltanet-kernels.md)
- <a id="chunked_gdn_per_seq"></a>`chunked_gdn_per_seq(q_large: jax.Array, k_large: jax.Array, v_large: jax.Array, gating_log: jax.Array, beta: jax.Array, state_prev: jax.Array, cfg: config.GDNConfig)` — [`L106`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/compute_gdn.py#L106) — Perform chunked GDN over input [num_heads, chunk, head_dim]. — documented in [gated-deltanet-kernels](../../../../../../concepts/gated-deltanet-kernels.md)
- <a id="fused_transpose_broadcast"></a>`fused_transpose_broadcast(x: jax.Array, src_dim: int, dst_dim: int)` — [`L91`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/compute_gdn.py#L91) — Perform 1D transpose where results are broadcasted along src_dim.
- <a id="get_mask_dtype"></a>`get_mask_dtype(dtype: jnp.dtype)` — [`L28`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/compute_gdn.py#L28)
- <a id="invert_triangular_matrix"></a>`invert_triangular_matrix(t: jax.Array, block_size=16)` — [`L39`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/compute_gdn.py#L39) — Compute invert matrix of a given triauglar matrix.
- <a id="l2_norm"></a>`l2_norm(x: jax.Array, eps: float = 0.000001)` — [`L21`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/compute_gdn.py#L21) — L2-normalize along the last dim, accumulating in float32.
- <a id="invert_triangular_matrix.local_forward_sub"></a>`local_forward_sub(t_mat, b_mat)` — [`L48`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/compute_gdn.py#L48)
- <a id="recurrent_gdn"></a>`recurrent_gdn(real_sizes: jax.Array, q_compact: jax.Array, k_compact: jax.Array, v_compact: jax.Array, b_compact: jax.Array, a_compact: jax.Array, state_prev: jax.Array, a_log: jax.Array, dt_bias: jax.Array, cfg: config.GDNConfig)` — [`L406`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/compute_gdn.py#L406) — Perform recurrent GDN over input [seq, num_heads, chunk, 1, head_dim]. — documented in [gated-deltanet-kernels](../../../../../../concepts/gated-deltanet-kernels.md)
- <a id="recurrent_gdn_per_seq"></a>`recurrent_gdn_per_seq(q_compact: jax.Array, k_compact: jax.Array, k_compact_t: jax.Array, v_compact: jax.Array, gating_log: jax.Array, beta: jax.Array, state: jax.Array, cfgs: config.GDNConfig)` — [`L327`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/compute_gdn.py#L327) — Perform recurrent GDN over input [num_heads, chunk, 1, head_dim].

