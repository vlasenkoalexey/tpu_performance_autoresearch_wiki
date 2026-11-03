---
title: 'Module: src/vllm_torchtpu/kernels/deepseek_v4/o_projection.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/deepseek_v4/o_projection.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.deepseek_v4.o_projection`/
symbols:
  _cos_sin_kernel: _cos_sin_kernel().
  wo_a_projection: wo_a_projection().
  gather_cos_sin: gather_cos_sin().
  fused_reverse_rope_wo_a_projection: fused_reverse_rope_wo_a_projection().
  _rope_heads: _rope_heads().
  _kernel: _kernel().
  _cos_sin_body: _cos_sin_body().
  _largest_divisor: _largest_divisor().
  DEFAULT_VMEM_LIMIT_BYTES: DEFAULT_VMEM_LIMIT_BYTES.
  SUBLANE: SUBLANE.
  _cos_sin_kernel._run: _cos_sin_kernel()._run().
---
# Module: [`src/vllm_torchtpu/kernels/deepseek_v4/o_projection.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/o_projection.py)

## Functions
- <a id="_cos_sin_body"></a>`_cos_sin_body(cos_sin_ref: jax.Ref, out_ref: jax.Ref, *, rotary_dim: int, inverse: bool, out_dtype: jnp.dtype)` — [`L43`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/o_projection.py#L43) — Expand a ``(tile_n, rotary_dim)`` block to ``(tile_n, 2 * LANE)``.
- <a id="_cos_sin_kernel"></a>`_cos_sin_kernel(positions_ref: jax.Ref, cos_sin_cache_hbm_ref: jax.Ref, out_hbm_ref: jax.Ref, *, num_tiles: int, tile_n: int, rotary_dim: int, inverse: bool, cos_sin_dtype: jnp.dtype, out_dtype: jnp.dtype)` — [`L56`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/o_projection.py#L56)
- <a id="_kernel"></a>`_kernel(x_ref: jax.Ref, w_ref: jax.Ref, scale_ref: jax.Ref, cos_sin_ref: jax.Ref, out_ref: jax.Ref, *, tile_t: int, num_sub_t: int, quantize_activations: bool, head_dim: int)` — [`L173`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/o_projection.py#L173)
- <a id="_largest_divisor"></a>`_largest_divisor(x: int, cap: int)` — [`L35`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/o_projection.py#L35) — Largest divisor of ``x`` that is <= ``cap``.
- <a id="_rope_heads"></a>`_rope_heads(x: jax.Array, cos_sin: jax.Array, *, head_dim: int)` — [`L163`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/o_projection.py#L163) — apply RoPE to the last rope dim of head dim of ``x``.
- <a id="_cos_sin_kernel._run"></a>`_run(allocations)` — [`L103`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/o_projection.py#L103)
- <a id="fused_reverse_rope_wo_a_projection"></a>`fused_reverse_rope_wo_a_projection(x: jax.Array, positions: jax.Array, cos_sin_cache: jax.Array, wo_a: jax.Array, wo_a_scale: jax.Array, *, head_dim: int, inverse: bool = True, tile_t: int | None = None, tile_r: int | None = None, sub_t: int | None = None, quantize_activations: bool = True, name: str = "wo_a_projection")` — [`L339`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/o_projection.py#L339) — ``The RoPE-fused ``wo_a_projection``.
- <a id="gather_cos_sin"></a>`gather_cos_sin(positions: jax.Array, cos_sin_cache: jax.Array, *, inverse: bool = False, out_dtype: jnp.dtype = jnp.float32, name: str = "gather_cos_sin")` — [`L117`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/o_projection.py#L117) — Builds ``wo_a_projection``'s ``[T, 2 * LANE]`` cos/sin table.
- <a id="wo_a_projection"></a>`wo_a_projection(x: jax.Array, wo_a: jax.Array, wo_a_scale: jax.Array, cos_sin: jax.Array, *, tile_t: int | None = None, tile_r: int | None = None, sub_t: int | None = None, quantize_activations: bool = True, name: str = "wo_a_projection")` — [`L230`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/o_projection.py#L230) — Do DSv4 wo_a projection.

## Module values
- <a id="DEFAULT_VMEM_LIMIT_BYTES"></a>`DEFAULT_VMEM_LIMIT_BYTES` — [`L30`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/o_projection.py#L30)
- <a id="SUBLANE"></a>`SUBLANE` — [`L32`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/o_projection.py#L32)

