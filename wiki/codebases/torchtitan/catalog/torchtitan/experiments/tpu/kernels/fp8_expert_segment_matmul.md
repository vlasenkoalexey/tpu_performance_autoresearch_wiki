---
title: 'Module: torchtitan/experiments/tpu/kernels/fp8_expert_segment_matmul.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/kernels/fp8_expert_segment_matmul.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.kernels.fp8_expert_segment_matmul`/
symbols:
  Tiling: Tiling.
  fp8_gmm_bwd_quantized: fp8_gmm_bwd_quantized().
  swiglu_quantize: swiglu_quantize().
  fp8_segment_matmul_pallas_2d: fp8_segment_matmul_pallas_2d().
  swiglu_w2_fwd: swiglu_w2_fwd().
  fp8_gmm_fwd_quantized: fp8_gmm_fwd_quantized().
  fp8_paired_segment_matmul_pallas_2d: fp8_paired_segment_matmul_pallas_2d().
  fp8_swiglu_segment_matmul_pallas_2d: fp8_swiglu_segment_matmul_pallas_2d().
  swiglu_grad: swiglu_grad().
  _fwd_with_residuals: _fwd_with_residuals().
  _quantize: _quantize().
  fp8_gmm_fwd: fp8_gmm_fwd().
  fp8_gmm_bwd: fp8_gmm_bwd().
  _swiglu_quant_kernel: _swiglu_quant_kernel().
  swiglu_w2_bwd: swiglu_w2_bwd().
  FWD_DTYPE: FWD_DTYPE.
  quantize_operands: quantize_operands().
  _bwd_from_residuals: _bwd_from_residuals().
  _fp8_grouped_mm_fwd: _fp8_grouped_mm_fwd().
  _fp8_paired_grouped_mm_fwd: _fp8_paired_grouped_mm_fwd().
  _register_autograd: _register_autograd().
  _fp8_swiglu_fwd: _fp8_swiglu_fwd().
  _from_i8: _from_i8().
  _resolve: _resolve().
  _static: _static().
  _to_i8: _to_i8().
  _fp8_grouped_mm_bwd: _fp8_grouped_mm_bwd().
  _fp8_paired_grouped_mm_bwd: _fp8_paired_grouped_mm_bwd().
  _swiglu_grad_kernel: _swiglu_grad_kernel().
  _fp8_swiglu_bwd: _fp8_swiglu_bwd().
  _swiglu_backward: _swiglu_backward().
  _PRECISION: _PRECISION.
  _Residuals: _Residuals.
  _int32: _int32().
  BWD_DTYPE: BWD_DTYPE.
  _SWIGLU_QUANT_TILE_M: _SWIGLU_QUANT_TILE_M.
  _swiglu_f32: _swiglu_f32().
  _swiglu_grad: _swiglu_grad().
  _real_jaxtyped: _real_jaxtyped.
  _passthrough_jaxtyped: _passthrough_jaxtyped().
  _register_autograd.setup_context: _register_autograd().setup_context().
  _register_autograd.backward: _register_autograd().backward().
  _swiglu_setup_context: _swiglu_setup_context().
  __all__: __all__.
---
# Module: [`torchtitan/experiments/tpu/kernels/fp8_expert_segment_matmul.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/fp8_expert_segment_matmul.py)

## Functions
- <a id="_bwd_from_residuals"></a>`_bwd_from_residuals(residuals, dout, dlhs_tiling, drhs_tiling, interpret=False)` — [`L236`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/fp8_expert_segment_matmul.py#L236)
- <a id="_fp8_grouped_mm_bwd"></a>`_fp8_grouped_mm_bwd(dout: jax.Array, lhs_q: jax.Array, lhs_scale: jax.Array, rhs_q: jax.Array, rhs_scale: jax.Array, group_sizes: jax.Array, dlhs_tm: int, dlhs_tk: int, dlhs_tn: int, drhs_tm: int, drhs_tk: int, drhs_tn: int)` — [`L303`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/fp8_expert_segment_matmul.py#L303)
- <a id="_fp8_grouped_mm_fwd"></a>`_fp8_grouped_mm_fwd(lhs: jax.Array, rhs: jax.Array, group_sizes: jax.Array, fwd_tm: int, fwd_tk: int, fwd_tn: int, dlhs_tm: int, dlhs_tk: int, dlhs_tn: int, drhs_tm: int, drhs_tk: int, drhs_tn: int)` — [`L262`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/fp8_expert_segment_matmul.py#L262)
- <a id="_fp8_paired_grouped_mm_bwd"></a>`_fp8_paired_grouped_mm_bwd(dout: jax.Array, lhs_q: jax.Array, lhs_scale: jax.Array, rhs_q: jax.Array, rhs_scale: jax.Array, group_sizes: jax.Array, dlhs_tm: int, dlhs_tk: int, dlhs_tn: int, drhs_tm: int, drhs_tk: int, drhs_tn: int)` — [`L326`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/fp8_expert_segment_matmul.py#L326)
- <a id="_fp8_paired_grouped_mm_fwd"></a>`_fp8_paired_grouped_mm_fwd(lhs: jax.Array, rhs_a: jax.Array, rhs_b: jax.Array, group_sizes: jax.Array, fwd_tm: int, fwd_tk: int, fwd_tn: int, dlhs_tm: int, dlhs_tk: int, dlhs_tn: int, drhs_tm: int, drhs_tk: int, drhs_tn: int)` — [`L281`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/fp8_expert_segment_matmul.py#L281)
- <a id="_fp8_swiglu_bwd"></a>`_fp8_swiglu_bwd(dout: jax.Array, gate_up: jax.Array, h_q: jax.Array, h_scale: jax.Array, rhs_q: jax.Array, rhs_scale: jax.Array, group_sizes: jax.Array, fused_quant: int, dlhs_tm: int, dlhs_tk: int, dlhs_tn: int, drhs_tm: int, drhs_tk: int, drhs_tn: int)` — [`L540`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/fp8_expert_segment_matmul.py#L540)
- <a id="_fp8_swiglu_fwd"></a>`_fp8_swiglu_fwd(gate_up: jax.Array, rhs: jax.Array, group_sizes: jax.Array, fused_quant: int, fwd_tm: int, fwd_tk: int, fwd_tn: int, dlhs_tm: int, dlhs_tk: int, dlhs_tn: int, drhs_tm: int, drhs_tk: int, drhs_tn: int)` — [`L518`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/fp8_expert_segment_matmul.py#L518)
- <a id="_from_i8"></a>`_from_i8(x: jax.Array)` — [`L217`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/fp8_expert_segment_matmul.py#L217)
- <a id="_fwd_with_residuals"></a>`_fwd_with_residuals(lhs, rhs, group_sizes, tiling, interpret=False)` — [`L221`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/fp8_expert_segment_matmul.py#L221)
- <a id="_int32"></a>`_int32(group_sizes: torch.Tensor)` — [`L599`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/fp8_expert_segment_matmul.py#L599)
- <a id="_passthrough_jaxtyped"></a>`_passthrough_jaxtyped(*args, **kwargs)` — [`L41`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/fp8_expert_segment_matmul.py#L41)
- <a id="_quantize"></a>`_quantize(x: jax.Array, qdtype: jnp.dtype, axis: int | tuple[int, ...])` — [`L67`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/fp8_expert_segment_matmul.py#L67) — Absmax-quantizes `x`, one FP32 scale per slice along reduced `axis`.
- <a id="_register_autograd"></a>`_register_autograd(fwd_op, bwd_op, num_weights: int)` — [`L350`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/fp8_expert_segment_matmul.py#L350) — Autograd that saves the forward's FP8 residuals instead of its inputs.
- <a id="_resolve"></a>`_resolve(tiling: Tiling, k_dim: int, n_dim: int)` — [`L76`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/fp8_expert_segment_matmul.py#L76) — Zero-valued K/N tiles select the full dimension.
- <a id="_static"></a>`_static(fwd: Tiling, dlhs: Tiling, drhs: Tiling)` — [`L593`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/fp8_expert_segment_matmul.py#L593)
- <a id="_swiglu_backward"></a>`_swiglu_backward(ctx, grad_out, *unused_residual_grads)` — [`L579`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/fp8_expert_segment_matmul.py#L579)
- <a id="_swiglu_f32"></a>`_swiglu_f32(gate_up: jax.Array)` — [`L389`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/fp8_expert_segment_matmul.py#L389)
- <a id="_swiglu_grad"></a>`_swiglu_grad(gate_up, d_hidden)` — [`L428`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/fp8_expert_segment_matmul.py#L428) — ``d[gate | up]`` of ``silu(gate) * up`` (BF16 out, FP32 math).
- <a id="_swiglu_grad_kernel"></a>`_swiglu_grad_kernel(gate_up_ref, d_hidden_ref, d_gate_up_ref)` — [`L440`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/fp8_expert_segment_matmul.py#L440)
- <a id="_swiglu_quant_kernel"></a>`_swiglu_quant_kernel(gate_up_ref, q_ref, scale_ref)` — [`L394`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/fp8_expert_segment_matmul.py#L394)
- <a id="_swiglu_setup_context"></a>`_swiglu_setup_context(ctx, inputs, output)` — [`L570`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/fp8_expert_segment_matmul.py#L570)
- <a id="_to_i8"></a>`_to_i8(x: jax.Array)` — [`L213`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/fp8_expert_segment_matmul.py#L213)
- <a id="_register_autograd.backward"></a>`backward(ctx, grad_out, *unused_residual_grads)` — [`L362`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/fp8_expert_segment_matmul.py#L362)
- <a id="fp8_gmm_bwd"></a>`fp8_gmm_bwd(dout: jax.Array, lhs: jax.Array, rhs: jax.Array, group_sizes: jax.Array, dlhs_tiling: Tiling, drhs_tiling: Tiling, interpret: bool = False)` — [`L186`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/fp8_expert_segment_matmul.py#L186) — `fp8_gmm_bwd_quantized` on BF16 inputs, quantized as the forward does. — documented in [tpu-pallas-kernels](../../../../../concepts/tpu-pallas-kernels.md)
- <a id="fp8_gmm_bwd_quantized"></a>`fp8_gmm_bwd_quantized(dout: jax.Array, lhs_q: jax.Array, lhs_scale: jax.Array, rhs_q: jax.Array, rhs_scale: jax.Array, group_sizes: jax.Array, dlhs_tiling: Tiling, drhs_tiling: Tiling, rhs_dtype: jnp.dtype, interpret: bool = False)` — [`L118`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/fp8_expert_segment_matmul.py#L118) — Returns ``(dlhs[M, K], drhs[G, K, N])`` from the forward's FP8 operands. — documented in [tpu-pallas-kernels](../../../../../concepts/tpu-pallas-kernels.md)
- <a id="fp8_gmm_fwd"></a>`fp8_gmm_fwd(lhs: jax.Array, rhs: jax.Array, group_sizes: jax.Array, tiling: Tiling, interpret: bool = False)` — [`L169`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/fp8_expert_segment_matmul.py#L169) — ``lhs[M, K] @ rhs[G, K, N]`` per group, quantizing both operands. — documented in [tpu-pallas-kernels](../../../../../concepts/tpu-pallas-kernels.md)
- <a id="fp8_gmm_fwd_quantized"></a>`fp8_gmm_fwd_quantized(lhs_q: jax.Array, lhs_scale: jax.Array, rhs_q: jax.Array, rhs_scale: jax.Array, group_sizes: jax.Array, tiling: Tiling, out_dtype: jnp.dtype, interpret: bool = False)` — [`L91`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/fp8_expert_segment_matmul.py#L91) — ``lhs[M, K] @ rhs[G, K, N]`` per group, on pre-quantized e4m3 operands.
- <a id="fp8_paired_segment_matmul_pallas_2d"></a>`fp8_paired_segment_matmul_pallas_2d(lhs: torch.Tensor, rhs_a: torch.Tensor, rhs_b: torch.Tensor, group_sizes: torch.Tensor, *, fwd_tiling: Tiling = (512, 0, 0), dlhs_tiling: Tiling = (512, 0, 0), drhs_tiling: Tiling = (512, 0, 0), split: bool = True)` — [`L631`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/fp8_expert_segment_matmul.py#L631) — ``(lhs @ rhs_a, lhs @ rhs_b)`` per expert as one FP8 GEMM over ``[a | b]``.
- <a id="fp8_segment_matmul_pallas_2d"></a>`fp8_segment_matmul_pallas_2d(lhs: torch.Tensor, rhs: torch.Tensor, group_sizes: torch.Tensor, *, fwd_tiling: Tiling = (512, 0, 0), dlhs_tiling: Tiling = (512, 0, 0), drhs_tiling: Tiling = (512, 0, 0))` — [`L607`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/fp8_expert_segment_matmul.py#L607) — FP8 per-expert matmuls; see the module docstring for the numerics. — documented in [tpu-pallas-kernels](../../../../../concepts/tpu-pallas-kernels.md)
- <a id="fp8_swiglu_segment_matmul_pallas_2d"></a>`fp8_swiglu_segment_matmul_pallas_2d(gate_up: torch.Tensor, rhs: torch.Tensor, group_sizes: torch.Tensor, *, fused_quant: bool = True, fwd_tiling: Tiling = (512, 0, 0), dlhs_tiling: Tiling = (512, 0, 0), drhs_tiling: Tiling = (512, 0, 0))` — [`L657`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/fp8_expert_segment_matmul.py#L657) — ``(silu(gate) * up) @ rhs`` per expert, with ``gate_up = [gate | up]``.
- <a id="quantize_operands"></a>`quantize_operands(lhs: jax.Array, rhs: jax.Array)` — [`L82`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/fp8_expert_segment_matmul.py#L82) — Returns ``(lhs_q [M,K], lhs_scale [M,1], rhs_q [G,K,N], rhs_scale [1,N])``.
- <a id="_register_autograd.setup_context"></a>`setup_context(ctx, inputs, output)` — [`L353`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/fp8_expert_segment_matmul.py#L353)
- <a id="swiglu_grad"></a>`swiglu_grad(gate_up: jax.Array, d_hidden: jax.Array, fused: bool, interpret=False)` — [`L447`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/fp8_expert_segment_matmul.py#L447) — ``d[gate | up]``, in one Pallas pass when ``fused``.
- <a id="swiglu_quantize"></a>`swiglu_quantize(gate_up: jax.Array, fused: bool, interpret: bool = False)` — [`L402`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/fp8_expert_segment_matmul.py#L402) — ``silu(gate) * up`` as ``(e4m3 [M, F], FP32 row scale [M, 1])``.
- <a id="swiglu_w2_bwd"></a>`swiglu_w2_bwd(dout, gate_up, h_q, h_scale, rhs_q, rhs_scale, group_sizes, dlhs_tiling, drhs_tiling, fused, interpret=False)` — [`L488`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/fp8_expert_segment_matmul.py#L488) — Returns ``(d_gate_up[M, 2F], d_rhs)``; straight-through over the cast.
- <a id="swiglu_w2_fwd"></a>`swiglu_w2_fwd(gate_up, rhs, group_sizes, tiling, fused, interpret=False)` — [`L470`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/fp8_expert_segment_matmul.py#L470) — Returns ``(out[M, N], h_q (int8 bits), h_scale, rhs_q (int8), rhs_scale)``.

## Module values
- <a id="BWD_DTYPE"></a>`BWD_DTYPE` — [`L61`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/fp8_expert_segment_matmul.py#L61)
- <a id="FWD_DTYPE"></a>`FWD_DTYPE` — [`L60`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/fp8_expert_segment_matmul.py#L60)
- <a id="Tiling"></a>`Tiling` — [`L64`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/fp8_expert_segment_matmul.py#L64) — documented in [tpu-pallas-kernels](../../../../../concepts/tpu-pallas-kernels.md)
- <a id="_PRECISION"></a>`_PRECISION` — [`L62`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/fp8_expert_segment_matmul.py#L62)
- <a id="_Residuals"></a>`_Residuals` — [`L254`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/fp8_expert_segment_matmul.py#L254)
- <a id="_SWIGLU_QUANT_TILE_M"></a>`_SWIGLU_QUANT_TILE_M` — [`L386`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/fp8_expert_segment_matmul.py#L386)
- <a id="__all__"></a>`__all__` — [`L682`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/fp8_expert_segment_matmul.py#L682)
- <a id="_real_jaxtyped"></a>`_real_jaxtyped` — [`L38`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/fp8_expert_segment_matmul.py#L38)

