---
title: 'Module: src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/compute_gdn.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/compute_gdn.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.experimental.gdn_pcp_fused.compute_gdn`/
symbols:
  chunked_gdn_per_seq: chunked_gdn_per_seq().
  recurrent_gdn: recurrent_gdn().
  chunked_gdn: chunked_gdn().
  recurrent_gdn_per_seq: recurrent_gdn_per_seq().
  fused_transpose_broadcast: fused_transpose_broadcast().
  l2_norm: l2_norm().
  get_mask_dtype: get_mask_dtype().
  invert_triangular_matrix: invert_triangular_matrix().
  invert_triangular_matrix.local_forward_sub: invert_triangular_matrix().local_forward_sub().
---
# Module: [`src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/compute_gdn.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/compute_gdn.py)

## Functions
- <a id="chunked_gdn"></a>`chunked_gdn(real_sizes: jax.Array, q_large: jax.Array, k_large: jax.Array, v_large: jax.Array, b_large: jax.Array, a_large: jax.Array, state_prev: jax.Array, a_log: jax.Array, dt_bias: jax.Array, cfg: config.GDNConfig)` — [`L256`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/compute_gdn.py#L256) — Perform chunked GDN over input [seq, num_heads, chunk, head_dim]. — documented in [gdn-pcp-fused-kernel](../../../../../../concepts/gdn-pcp-fused-kernel.md)
- <a id="chunked_gdn_per_seq"></a>`chunked_gdn_per_seq(q_large: jax.Array, k_large: jax.Array, v_large: jax.Array, gating_log: jax.Array, beta: jax.Array, state_prev: jax.Array, cfg: config.GDNConfig)` — [`L110`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/compute_gdn.py#L110) — Perform chunked GDN over input [num_heads, chunk, head_dim].
- <a id="fused_transpose_broadcast"></a>`fused_transpose_broadcast(x: jax.Array, src_dim: int, dst_dim: int)` — [`L95`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/compute_gdn.py#L95) — Perform 1D transpose where results are broadcasted along src_dim.
- <a id="get_mask_dtype"></a>`get_mask_dtype(dtype: jnp.dtype)` — [`L32`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/compute_gdn.py#L32)
- <a id="invert_triangular_matrix"></a>`invert_triangular_matrix(t: jax.Array, block_size=16)` — [`L43`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/compute_gdn.py#L43) — Compute invert matrix of a given triauglar matrix.
- <a id="l2_norm"></a>`l2_norm(x: jax.Array, eps: float = 0.000001)` — [`L27`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/compute_gdn.py#L27)
- <a id="invert_triangular_matrix.local_forward_sub"></a>`local_forward_sub(t_mat, b_mat)` — [`L52`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/compute_gdn.py#L52)
- <a id="recurrent_gdn"></a>`recurrent_gdn(real_sizes: jax.Array, q_compact: jax.Array, k_compact: jax.Array, v_compact: jax.Array, b_compact: jax.Array, a_compact: jax.Array, state_prev: jax.Array, a_log: jax.Array, dt_bias: jax.Array, cfg: config.GDNConfig)` — [`L410`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/compute_gdn.py#L410) — Perform recurrent GDN over input [seq, num_heads, chunk, 1, head_dim]. — documented in [gdn-pcp-fused-kernel](../../../../../../concepts/gdn-pcp-fused-kernel.md)
- <a id="recurrent_gdn_per_seq"></a>`recurrent_gdn_per_seq(q_compact: jax.Array, k_compact: jax.Array, k_compact_t: jax.Array, v_compact: jax.Array, gating_log: jax.Array, beta: jax.Array, state: jax.Array, cfgs: config.GDNConfig)` — [`L331`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/compute_gdn.py#L331) — Perform recurrent GDN over input [num_heads, chunk, 1, head_dim].

