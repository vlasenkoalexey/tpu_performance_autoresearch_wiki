---
title: 'Module: src/vllm_torchtpu/kernels/kimi_k3/mega_kda/__init__.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/kimi_k3/mega_kda/__init__.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.kimi_k3.mega_kda`/
symbols:
  kda_forward_inference: kda_forward_inference().
  _layout_supported: _layout_supported().
---
# Module: [`src/vllm_torchtpu/kernels/kimi_k3/mega_kda/__init__.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/mega_kda/__init__.py)

## Functions
- <a id="_layout_supported"></a>`_layout_supported(query_start_loc: jax.Array, num_tokens: int, chunk_size: int = 64)` — [`L32`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/mega_kda/__init__.py#L32) — Whether every mega-KDA tile intersects at most two live requests.
- <a id="kda_forward_inference"></a>`kda_forward_inference(q: jax.Array, k: jax.Array, v: jax.Array, g: jax.Array, beta: jax.Array, *, segment_ids: jax.Array, A_log: jax.Array | None = None, dt_bias: jax.Array | None = None, scale: float | None = None, initial_state: jax.Array | None = None, output_final_state: bool = False, use_qk_l2norm_in_kernel: bool = False, use_gate_in_kernel: bool = False, safe_gate: bool = True, lower_bound: float | None = None, chunk_size: int = 64, N_max: int | None = None, mini_batch: int | None = None)` — [`L65`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/mega_kda/__init__.py#L65) — Run the standalone KDA inference forward kernel.

