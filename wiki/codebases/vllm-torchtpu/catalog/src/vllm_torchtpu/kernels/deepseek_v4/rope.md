---
title: 'Module: src/vllm_torchtpu/kernels/deepseek_v4/rope.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/deepseek_v4/rope.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.deepseek_v4.rope`/
symbols:
  LANE: LANE.
  _kernel: _kernel().
  _rope_call: _rope_call().
  _qnorm_rope_kernel: _qnorm_rope_kernel().
  qnorm_rope: qnorm_rope().
  _cos_sin_lanes: _cos_sin_lanes().
  _rotate_gptj: _rotate_gptj().
  _rope_body: _rope_body().
  _qnorm_rope_body: _qnorm_rope_body().
  CosSinRef.create: CosSinRef#create().
  CosSinRef: CosSinRef#
  rope_quant: rope_quant().
  rope: rope().
  _lane_gather: _lane_gather().
  _kernel.x_index_map: _kernel().x_index_map().
  CosSinRef.copy_in: CosSinRef#copy_in().
  DEFAULT_VMEM_LIMIT_BYTES: DEFAULT_VMEM_LIMIT_BYTES.
  CosSinRef.tile_n: CosSinRef#tile_n.
  _kernel._run: _kernel()._run().
  _qnorm_rope_kernel._run: _qnorm_rope_kernel()._run().
  CosSinRef.wait_in: CosSinRef#wait_in().
---
# Module: [`src/vllm_torchtpu/kernels/deepseek_v4/rope.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/rope.py)

## Classes
### <a id="CosSinRef"></a>`CosSinRef`  ·  implements/extends BufferedRef
- def: [`src/vllm_torchtpu/kernels/deepseek_v4/rope.py:35`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/rope.py#L35)
- doc: Per-token gather of `cos_sin_cache` rows into a `(tile_n, rotary_dim)`
- signature: `class CosSinRef(pltpu.BufferedRef):`
- members:
  - <a id="CosSinRef.copy_in"></a>`copy_in(self, src_ref: tuple[jax.Ref, jax.Ref], grid_indices: tuple[int | jax.Array, ...])` — [`L60`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/rope.py#L60)
  - <a id="CosSinRef.create"></a>`create(cls, *, spec: pl.BlockSpec, dtype: jnp.dtype, buffer_count: int, tile_n: int)` — [`L41`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/rope.py#L41)
  - <a id="CosSinRef.wait_in"></a>`wait_in(self, src_ref: tuple[jax.Ref, jax.Ref], grid_indices: tuple[int | jax.Array, ...])` — [`L81`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/rope.py#L81)
  - <a id="CosSinRef.tile_n"></a>`tile_n` — [`L38`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/rope.py#L38)
- used by: [`_cos_sin_kernel`](o_projection.md#_cos_sin_kernel), [`_kernel`](rope.md#_kernel), [`_qnorm_rope_kernel`](rope.md#_qnorm_rope_kernel)

## Functions
- <a id="_cos_sin_lanes"></a>`_cos_sin_lanes(cos_sin: jax.Array, *, rotary_dim: int, inverse: bool)` — [`L121`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/rope.py#L121) — The reference's ``np.split`` + ``np.repeat(..., 2)``, over a whole block.
- <a id="_kernel"></a>`_kernel(positions_ref: jax.Ref, x_hbm_ref: jax.Ref, cos_sin_cache_hbm_ref: jax.Ref, *out_hbm_refs: jax.Ref, num_tiles: int, tile_n: int, x_block_shape: tuple[int, ...], scale_block_shape: tuple[int, ...], lane_block: int, rotary_dim: int, inverse: bool, in_dtype: jnp.dtype, out_dtype: jnp.dtype, cos_sin_dtype: jnp.dtype, quant_dtype: jnp.dtype | None)` — [`L205`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/rope.py#L205)
- <a id="_lane_gather"></a>`_lane_gather(operand: jax.Array, indices: jax.Array)` — [`L94`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/rope.py#L94) — ``out[b..., i] = operand[b..., indices[i]]`` over the last axis.
- <a id="_qnorm_rope_body"></a>`_qnorm_rope_body(x_ref: jax.Ref, cos_sin_ref: jax.Ref, out_ref: jax.Ref, *, rotary_dim: int, eps: float, inverse: bool, out_dtype: jnp.dtype)` — [`L299`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/rope.py#L299) — Process one ``(tile_n, num_heads, head_dim)`` chunk.
- <a id="_qnorm_rope_kernel"></a>`_qnorm_rope_kernel(positions_ref: jax.Ref, x_hbm_ref: jax.Ref, cos_sin_cache_hbm_ref: jax.Ref, out_hbm_ref: jax.Ref, *, num_tiles: int, tile_n: int, x_block_shape: tuple[int, ...], rotary_dim: int, eps: float, inverse: bool, in_dtype: jnp.dtype, cos_sin_dtype: jnp.dtype)` — [`L330`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/rope.py#L330)
- <a id="_rope_body"></a>`_rope_body(x_ref: jax.Ref, cos_sin_ref: jax.Ref, *out_refs: jax.Ref, rotary_dim: int, inverse: bool, out_dtype: jnp.dtype, quant_dtype: jnp.dtype | None)` — [`L167`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/rope.py#L167) — Process one ``(tile_n, [num_heads,] LANE)`` chunk.
- <a id="_rope_call"></a>`_rope_call(x: jax.Array, positions: jax.Array, cos_sin_cache: jax.Array, *, inverse: bool, quant_dtype: jnp.dtype | None, name: str)` — [`L392`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/rope.py#L392) — Builds the ``pallas_call``; see the public wrappers for the contract.
- <a id="_rotate_gptj"></a>`_rotate_gptj(x: jax.Array)` — [`L154`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/rope.py#L154) — The reference's ``rotated``: ``[-x1, x0, -x3, x2, ...]`` along the lanes.
- <a id="_kernel._run"></a>`_run(allocations)` — [`L288`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/rope.py#L288)
- <a id="_qnorm_rope_kernel._run"></a>`_run(allocations)` — [`L381`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/rope.py#L381)
- <a id="qnorm_rope"></a>`qnorm_rope(x: jax.Array, positions: jax.Array, cos_sin_cache: jax.Array, *, eps: float = 0.000001, inverse: bool = False, name: str = "qnorm_rope")` — [`L524`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/rope.py#L524) — Per-head RMSNorm (no weight) fused with DeepSeek-V4 RoPE.
- <a id="rope"></a>`rope(x: jax.Array, positions: jax.Array, cos_sin_cache: jax.Array, *, inverse: bool = False, name: str = "rope")` — [`L483`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/rope.py#L483) — Applies DeepSeek-V4 RoPE to the trailing ``rotary_dim`` channels of ``x``.
- <a id="rope_quant"></a>`rope_quant(x: jax.Array, positions: jax.Array, cos_sin_cache: jax.Array, *, inverse: bool = False, quant_dtype: jnp.dtype = jnp.float8_e4m3fn, name: str = "rope_quant")` — [`L582`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/rope.py#L582) — RoPE fused with per-row dynamic quantization of the rotated values.
- <a id="_kernel.x_index_map"></a>`x_index_map(i)` — [`L225`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/rope.py#L225)

## Module values
- <a id="DEFAULT_VMEM_LIMIT_BYTES"></a>`DEFAULT_VMEM_LIMIT_BYTES` — [`L30`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/rope.py#L30)
- <a id="LANE"></a>`LANE` — [`L28`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/rope.py#L28)

