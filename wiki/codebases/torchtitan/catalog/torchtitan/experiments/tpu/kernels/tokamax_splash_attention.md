---
title: 'Module: torchtitan/experiments/tpu/kernels/tokamax_splash_attention.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/kernels/tokamax_splash_attention.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.kernels.tokamax_splash_attention`/
symbols:
  splash_sdpa: splash_sdpa().
  TokamaxConfig: TokamaxConfig#
  _make_splash_attention_fn: _make_splash_attention_fn().
  _make_splash_attention_fn.splash_bwd_fn: _make_splash_attention_fn().splash_bwd_fn().
  _slice_mask_info: _slice_mask_info().
  _make_mask: _make_mask.
  _make_splash_attention_fn.splash_fn: _make_splash_attention_fn().splash_fn().
  _kernel_config_args: _kernel_config_args().
  TokamaxConfig.use_vmap_bwd: TokamaxConfig#use_vmap_bwd.
  _make_splash_attention_fn._segment_ids: _make_splash_attention_fn()._segment_ids().
  _make_splash_attention_fn.splash_bwd_fn._single_bwd: _make_splash_attention_fn().splash_bwd_fn()._single_bwd().
  splash_op.splash_op: splash_op.splash_op.
  _dummy_jaxtyped: _dummy_jaxtyped().
  _make_splash_attention_fn.splash_fn._single_fwd_with_lse: _make_splash_attention_fn().splash_fn()._single_fwd_with_lse().
  _make_splash_attention_fn.splash_bwd_fn._scan_bwd_body: _make_splash_attention_fn().splash_bwd_fn()._scan_bwd_body().
  jax_attention_fwd: jax_attention_fwd().
  jax_attention_bwd: jax_attention_bwd().
  backward: backward().
  splash_op_backward.splash_op_backward: splash_op_backward.splash_op_backward.
  TokamaxConfig.block_q: TokamaxConfig#block_q.
  TokamaxConfig.update: TokamaxConfig#update().
  _make_splash_attention_fn._get_layout: _make_splash_attention_fn()._get_layout().
  TokamaxConfig.block_kv: TokamaxConfig#block_kv.
  TokamaxConfig.block_kv_compute: TokamaxConfig#block_kv_compute.
  _real_jaxtyped: _real_jaxtyped.
  _dummy_jaxtyped.decorator: _dummy_jaxtyped().decorator().
  _DEFAULT_MASK_VALUE: _DEFAULT_MASK_VALUE.
  _MASK_INFO_SLICE_AXES: _MASK_INFO_SLICE_AXES.
  TokamaxConfig.block_q_dkv: TokamaxConfig#block_q_dkv.
  TokamaxConfig.block_kv_dkv: TokamaxConfig#block_kv_dkv.
  TokamaxConfig.block_kv_dkv_compute: TokamaxConfig#block_kv_dkv_compute.
  TokamaxConfig.q_layout: TokamaxConfig#q_layout.
  TokamaxConfig.k_layout: TokamaxConfig#k_layout.
  TokamaxConfig.v_layout: TokamaxConfig#v_layout.
  _KERNEL_CONFIG_FIELDS: _KERNEL_CONFIG_FIELDS.
  setup_context: setup_context().
  TokamaxConfig.block_q_dq: TokamaxConfig#block_q_dq.
  TokamaxConfig.block_kv_dq: TokamaxConfig#block_kv_dq.
  TokamaxConfig.use_fused_bwd_kernel: TokamaxConfig#use_fused_bwd_kernel.
---
# Module: [`torchtitan/experiments/tpu/kernels/tokamax_splash_attention.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tokamax_splash_attention.py)

## Classes
### <a id="TokamaxConfig"></a>`TokamaxConfig`
- def: [`torchtitan/experiments/tpu/kernels/tokamax_splash_attention.py:77`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tokamax_splash_attention.py#L77) — documented in [tpu-pallas-kernels](../../../../../concepts/tpu-pallas-kernels.md)
- doc: Global configuration container for hardware-static hyperparameters.
- signature: `class TokamaxConfig:`
- members:
  - <a id="TokamaxConfig.update"></a>`update(cls, **kwargs)` — [`L94`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tokamax_splash_attention.py#L94)
  - <a id="TokamaxConfig.block_kv"></a>`block_kv` — [`L80`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tokamax_splash_attention.py#L80)
  - <a id="TokamaxConfig.block_kv_compute"></a>`block_kv_compute` — [`L81`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tokamax_splash_attention.py#L81)
  - <a id="TokamaxConfig.block_kv_dkv"></a>`block_kv_dkv` — [`L83`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tokamax_splash_attention.py#L83)
  - <a id="TokamaxConfig.block_kv_dkv_compute"></a>`block_kv_dkv_compute` — [`L84`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tokamax_splash_attention.py#L84)
  - <a id="TokamaxConfig.block_kv_dq"></a>`block_kv_dq` — [`L86`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tokamax_splash_attention.py#L86)
  - <a id="TokamaxConfig.block_q"></a>`block_q` — [`L79`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tokamax_splash_attention.py#L79)
  - <a id="TokamaxConfig.block_q_dkv"></a>`block_q_dkv` — [`L82`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tokamax_splash_attention.py#L82)
  - <a id="TokamaxConfig.block_q_dq"></a>`block_q_dq` — [`L85`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tokamax_splash_attention.py#L85)
  - <a id="TokamaxConfig.k_layout"></a>`k_layout` — [`L90`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tokamax_splash_attention.py#L90)
  - <a id="TokamaxConfig.q_layout"></a>`q_layout` — [`L89`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tokamax_splash_attention.py#L89)
  - <a id="TokamaxConfig.use_fused_bwd_kernel"></a>`use_fused_bwd_kernel` — [`L87`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tokamax_splash_attention.py#L87)
  - <a id="TokamaxConfig.use_vmap_bwd"></a>`use_vmap_bwd` — [`L88`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tokamax_splash_attention.py#L88)
  - <a id="TokamaxConfig.v_layout"></a>`v_layout` — [`L91`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tokamax_splash_attention.py#L91)
- used by: [`use_tokamax_splash_attention_patch`](../workarounds.md#use_tokamax_splash_attention_patch), [`splash_sdpa`](tokamax_splash_attention.md#splash_sdpa), [`_kernel_config_args`](tokamax_splash_attention.md#_kernel_config_args)  (7 test-only)

## Functions
- <a id="_dummy_jaxtyped"></a>`_dummy_jaxtyped(*args, **kwargs)` — [`L30`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tokamax_splash_attention.py#L30)
- <a id="_make_splash_attention_fn._get_layout"></a>`_get_layout(layout_str)` — [`L139`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tokamax_splash_attention.py#L139)
- <a id="_kernel_config_args"></a>`_kernel_config_args()` — [`L518`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tokamax_splash_attention.py#L518) — TokamaxConfig values, in jax_attention_fwd/bwd argument order.
- <a id="_make_splash_attention_fn"></a>`_make_splash_attention_fn(seq_len: int, n_heads: int, n_kv_heads: int, is_causal: bool = True, local_window_size: int | None = None, block_q: int = 512, block_kv: int = 512, block_kv_compute: int = 512, block_q_dkv: int = 512, block_kv_dkv: int = 512, block_kv_dkv_compute: int = 512, block_q_dq: int | None = None, block_kv_dq: int | None = None, use_fused_bwd_kernel: bool = True, q_layout: str = "HEAD_DIM_MINOR", k_layout: str = "HEAD_DIM_MINOR", v_layout: str = "HEAD_DIM_MINOR", use_vmap_bwd: bool = False, kv_seq_len: int | None = None)` — [`L100`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tokamax_splash_attention.py#L100) — Create JAX splash attention forward and backward functions using Tokamax.
- <a id="_make_splash_attention_fn.splash_bwd_fn._scan_bwd_body"></a>`_scan_bwd_body(carry, args)` — [`L289`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tokamax_splash_attention.py#L289) — Single-element backward body for jax.lax.scan (sequential over batch).
- <a id="_make_splash_attention_fn._segment_ids"></a>`_segment_ids(segment_ids_b, cp_rank=None)` — [`L206`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tokamax_splash_attention.py#L206) — documented in [tpu-context-parallel-attention](../../../../../concepts/tpu-context-parallel-attention.md)
- <a id="_make_splash_attention_fn.splash_bwd_fn._single_bwd"></a>`_single_bwd(q_scaled_b, k_b, v_b, out_b, logsumexp_b, g_b, segment_ids_b)` — [`L259`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tokamax_splash_attention.py#L259) — Backward for one batch element using precomputed residuals.
- <a id="_make_splash_attention_fn.splash_fn._single_fwd_with_lse"></a>`_single_fwd_with_lse(q_b, k_b, v_b, segment_ids_b)` — [`L223`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tokamax_splash_attention.py#L223) — Forward for one batch element; returns (out_b, logsumexp_b).
- <a id="_slice_mask_info"></a>`_slice_mask_info(mask_info, cp_size: int, cp_rank: jax.Array | None)` — [`L72`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tokamax_splash_attention.py#L72) — Slice a Tokamax MaskInfo crafted for q_seq_shards=cp_size to cp_rank's shard. — documented in [tpu-context-parallel-attention](../../../../../concepts/tpu-context-parallel-attention.md)
- <a id="backward"></a>`backward(ctx, grad_out, grad_lse)` — [`L551`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tokamax_splash_attention.py#L551)
- <a id="_dummy_jaxtyped.decorator"></a>`decorator(f)` — [`L31`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tokamax_splash_attention.py#L31)
- <a id="jax_attention_bwd"></a>`jax_attention_bwd(q: jax.Array, k: jax.Array, v: jax.Array, out: jax.Array, logsumexp: jax.Array, grad_out: jax.Array, segment_ids: jax.Array | None, cp_rank: jax.Array | None, is_causal: bool, local_window_size: int, scale: float, block_q: int, block_kv: int, block_kv_compute: int, block_q_dkv: int, block_kv_dkv: int, block_kv_dkv_compute: int, block_q_dq: int | None, block_kv_dq: int | None, use_fused_bwd_kernel: bool, use_vmap_bwd: bool, q_layout: str, k_layout: str, v_layout: str)` — [`L396`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tokamax_splash_attention.py#L396) — Backward attention in JAX calling direct Pallas kernel backward.
- <a id="jax_attention_fwd"></a>`jax_attention_fwd(q: jax.Array, k: jax.Array, v: jax.Array, segment_ids: jax.Array | None, cp_rank: jax.Array | None, is_causal: bool, local_window_size: int, scale: float, block_q: int, block_kv: int, block_kv_compute: int, block_q_dkv: int, block_kv_dkv: int, block_kv_dkv_compute: int, block_q_dq: int | None, block_kv_dq: int | None, use_fused_bwd_kernel: bool, use_vmap_bwd: bool, q_layout: str, k_layout: str, v_layout: str)` — [`L315`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tokamax_splash_attention.py#L315) — Forward attention in JAX using Pallas.
- <a id="setup_context"></a>`setup_context(ctx, inputs, output, **kwargs)` — [`L528`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tokamax_splash_attention.py#L528)
- <a id="_make_splash_attention_fn.splash_bwd_fn"></a>`splash_bwd_fn(q, k, v, out, logsumexp, g, segment_ids=None, cp_rank=None)` — [`L252`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tokamax_splash_attention.py#L252) — Backward: uses saved (out, logsumexp) — no extra forward pass.
- <a id="_make_splash_attention_fn.splash_fn"></a>`splash_fn(q, k, v, segment_ids=None, cp_rank=None)` — [`L216`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tokamax_splash_attention.py#L216) — Forward: returns (out, logsumexp) for the whole batch.
- <a id="splash_sdpa"></a>`splash_sdpa(q: torch.Tensor, k: torch.Tensor, v: torch.Tensor, *, segment_ids: Optional[torch.Tensor] = None, cp_rank: Optional[torch.Tensor] = None, scale: Optional[float] = None, is_causal: bool = True, local_window_size: Optional[int] = None, enable_gqa: bool = False, block_q: Optional[int] = None, block_kv: Optional[int] = None, block_dkv: Optional[int] = None, block_kv_compute: Optional[int] = None, block_q_dkv: Optional[int] = None, block_kv_dkv: Optional[int] = None, block_kv_dkv_compute: Optional[int] = None, block_q_dq: Optional[int] = None, block_kv_dq: Optional[int] = None, use_fused_bwd_kernel: Optional[bool] = None, use_vmap_bwd: Optional[bool] = None, q_layout: Optional[str] = None, k_layout: Optional[str] = None, v_layout: Optional[str] = None)` — [`L578`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tokamax_splash_attention.py#L578) — Replacement for F.scaled_dot_product_attention using Tokamax splash attention. — documented in [tpu-pallas-kernels](../../../../../concepts/tpu-pallas-kernels.md)

## Module values
- <a id="_DEFAULT_MASK_VALUE"></a>`_DEFAULT_MASK_VALUE` — [`L55`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tokamax_splash_attention.py#L55)
- <a id="_KERNEL_CONFIG_FIELDS"></a>`_KERNEL_CONFIG_FIELDS` — [`L501`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tokamax_splash_attention.py#L501)
- <a id="_MASK_INFO_SLICE_AXES"></a>`_MASK_INFO_SLICE_AXES` — [`L60`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tokamax_splash_attention.py#L60)
- <a id="_make_mask"></a>`_make_mask` — [`L69`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tokamax_splash_attention.py#L69) — documented in [tpu-context-parallel-attention](../../../../../concepts/tpu-context-parallel-attention.md)
- <a id="_real_jaxtyped"></a>`_real_jaxtyped` — [`L27`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tokamax_splash_attention.py#L27)
- <a id="splash_op.splash_op"></a>`splash_op` — [`L492`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tokamax_splash_attention.py#L492)
- <a id="splash_op_backward.splash_op_backward"></a>`splash_op_backward` — [`L496`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tokamax_splash_attention.py#L496)

