---
title: 'Module: src/torch_tpu/_internal/ops/splash_attention.py'
type: catalog
provenance: extracted
module: src/torch_tpu/_internal/ops/splash_attention.py
status: fresh
symbol_base: scip-python python torch_tpu 0.0.0 `src.torch_tpu._internal.ops.splash_attention`/
symbols:
  _make_splash_attention_fn: _make_splash_attention_fn().
  _get_splash_op_names: _get_splash_op_names().
  _make_splash_attention_fn.splash_bwd_fn: _make_splash_attention_fn().splash_bwd_fn().
  splash_sdpa: splash_sdpa().
  _make_splash_attention_fn.splash_fn: _make_splash_attention_fn().splash_fn().
  _make_splash_attention_fn._scan_bwd_body: _make_splash_attention_fn()._scan_bwd_body().
  _make_splash_attention_fn._get_layout: _make_splash_attention_fn()._get_layout().
  _splash_op_name_cache: _splash_op_name_cache.
  _custom_jax_kernel: _custom_jax_kernel.
  _make_splash_attention_fn._single_bwd: _make_splash_attention_fn()._single_bwd().
  _DEFAULT_MASK_VALUE: _DEFAULT_MASK_VALUE.
  _make_splash_attention_fn._single_fwd_with_lse: _make_splash_attention_fn()._single_fwd_with_lse().
  _SplashAttentionFn: _SplashAttentionFn#
  __all__: __all__.
  _SplashAttentionFn.forward: _SplashAttentionFn#forward().
  _SplashAttentionFn.backward: _SplashAttentionFn#backward().
---
# Module: [`src/torch_tpu/_internal/ops/splash_attention.py`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/splash_attention.py)

## Classes
### <a id="_SplashAttentionFn"></a>`_SplashAttentionFn`
- def: [`src/torch_tpu/_internal/ops/splash_attention.py:310`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/splash_attention.py#L310)
- doc: torch.autograd.Function bridging splash forward and direct backward.
- signature: `class _SplashAttentionFn(torch.autograd.Function):`
- members:
  - <a id="_SplashAttentionFn.backward"></a>`backward(ctx, grad_output)` — [`L323`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/splash_attention.py#L323)
  - <a id="_SplashAttentionFn.forward"></a>`forward(ctx, q, k, v, torch_fwd_fn, torch_bwd_fn)` — [`L314`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/splash_attention.py#L314)
- used by: [`splash_sdpa`](splash_attention.md#splash_sdpa)

## Functions
- <a id="_make_splash_attention_fn._get_layout"></a>`_get_layout(layout_str)` — [`L99`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/splash_attention.py#L99) — documented in [python-ops](../../../../../concepts/python-ops.md)
- <a id="_get_splash_op_names"></a>`_get_splash_op_names(**splash_kwargs)` — [`L342`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/splash_attention.py#L342) — Create and cache PyTorch forward/backward functions for splash attention. — documented in [python-ops](../../../../../concepts/python-ops.md)
- <a id="_make_splash_attention_fn"></a>`_make_splash_attention_fn(seq_len: int, n_heads: int, n_kv_heads: int, scale: float | None = None, is_causal: bool = True, local_window_size: int | None = None, block_q: int = 512, block_kv: int = 512, block_kv_compute: int = 512, block_q_dkv: int = 512, block_kv_dkv: int = 512, block_kv_dkv_compute: int = 512, block_q_dq: int | None = None, block_kv_dq: int | None = None, use_fused_bwd_kernel: bool = True, q_layout: str = "HEAD_DIM_MINOR", k_layout: str = "HEAD_DIM_MINOR", v_layout: str = "HEAD_DIM_MINOR", use_vmap_bwd: bool = True)` — [`L48`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/splash_attention.py#L48) — Create JAX splash attention forward and backward functions. — documented in [python-ops](../../../../../concepts/python-ops.md)
- <a id="_make_splash_attention_fn._scan_bwd_body"></a>`_scan_bwd_body(carry, args)` — [`L259`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/splash_attention.py#L259) — Single-element backward body for jax.lax.scan (sequential over batch). — documented in [python-ops](../../../../../concepts/python-ops.md)
- <a id="_make_splash_attention_fn._single_bwd"></a>`_single_bwd(q_scaled_b, k_b, v_b, out_b, logsumexp_b, g_b)` — [`L217`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/splash_attention.py#L217) — Backward for one batch element using precomputed residuals. — documented in [python-ops](../../../../../concepts/python-ops.md)
- <a id="_make_splash_attention_fn._single_fwd_with_lse"></a>`_single_fwd_with_lse(q_b, k_b, v_b)` — [`L185`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/splash_attention.py#L185) — Forward for one batch element; returns (out_b, logsumexp_b).
- <a id="_make_splash_attention_fn.splash_bwd_fn"></a>`splash_bwd_fn(q, k, v, out, logsumexp, g)` — [`L268`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/splash_attention.py#L268) — Backward: uses saved (out, logsumexp) — no extra forward pass. — documented in [python-ops](../../../../../concepts/python-ops.md)
- <a id="_make_splash_attention_fn.splash_fn"></a>`splash_fn(q, k, v)` — [`L208`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/splash_attention.py#L208) — Forward: returns (out, logsumexp) for the whole batch. — documented in [python-ops](../../../../../concepts/python-ops.md)
- <a id="splash_sdpa"></a>`splash_sdpa(q: torch.Tensor, k: torch.Tensor, v: torch.Tensor, *, scale: Optional[float] = None, is_causal: bool = True, local_window_size: Optional[int] = None, enable_gqa: bool = False, block_q: int = 512, block_kv: int = 512, block_dkv: int = 512, block_kv_compute: int = 512, block_q_dkv: int = 512, block_kv_dkv: int = 512, block_kv_dkv_compute: int = 512, block_q_dq: Optional[int] = None, block_kv_dq: Optional[int] = None, use_fused_bwd_kernel: bool = True, use_vmap_bwd: bool = True, q_layout: str = "HEAD_DIM_MINOR", k_layout: str = "HEAD_DIM_MINOR", v_layout: str = "HEAD_DIM_MINOR")` — [`L442`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/splash_attention.py#L442) — Replacement for F.scaled_dot_product_attention using splash attention. — documented in [python-ops](../../../../../concepts/python-ops.md)

## Module values
- <a id="_DEFAULT_MASK_VALUE"></a>`_DEFAULT_MASK_VALUE` — [`L45`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/splash_attention.py#L45)
- <a id="__all__"></a>`__all__` — [`L41`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/splash_attention.py#L41)
- <a id="_custom_jax_kernel"></a>`_custom_jax_kernel` — [`L39`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/splash_attention.py#L39)
- <a id="_splash_op_name_cache"></a>`_splash_op_name_cache` — [`L338`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/splash_attention.py#L338)

