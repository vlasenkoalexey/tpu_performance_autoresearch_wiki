---
title: 'Module: torchtitan/experiments/tpu/kernels/splash_attention.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/kernels/splash_attention.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.kernels.splash_attention`/
symbols:
  _make_splash_attention_fn: _make_splash_attention_fn().
  SplashAttention.forward: SplashAttention#forward().
  splash_sdpa: splash_sdpa().
  _get_splash_op_names: _get_splash_op_names().
  _make_mask: _make_mask.
  _maybe_document_aware_mask_info: _maybe_document_aware_mask_info().
  _make_splash_attention_fn.splash_bwd_fn: _make_splash_attention_fn().splash_bwd_fn().
  _slice_mask_info: _slice_mask_info().
  _make_splash_attention_fn.splash_bwd_fn._single_bwd: _make_splash_attention_fn().splash_bwd_fn()._single_bwd().
  _make_splash_attention_fn.splash_fn._single_fwd_with_lse: _make_splash_attention_fn().splash_fn()._single_fwd_with_lse().
  splash_block_size_for: splash_block_size_for().
  _make_splash_attention_fn.splash_fn: _make_splash_attention_fn().splash_fn().
  SplashAttention: SplashAttention#
  _make_splash_attention_fn._segment_ids: _make_splash_attention_fn()._segment_ids().
  _make_splash_attention_fn.splash_bwd_fn._scan_bwd_body: _make_splash_attention_fn().splash_bwd_fn()._scan_bwd_body().
  _warned_cp_block_skipping: _warned_cp_block_skipping.
  _make_splash_attention_fn._get_layout: _make_splash_attention_fn()._get_layout().
  _splash_op_name_cache: _splash_op_name_cache.
  custom_jax_kernel: custom_jax_kernel.
  SplashAttention.original_module: SplashAttention#original_module.
  _DEFAULT_MASK_VALUE: _DEFAULT_MASK_VALUE.
  _document_aware_mask_info: _document_aware_mask_info().
  _MASK_INFO_SLICE_AXES: _MASK_INFO_SLICE_AXES.
  _get_splash_op_names.setup_context: _get_splash_op_names().setup_context().
  _get_splash_op_names.backward: _get_splash_op_names().backward().
  _SPLASH_BLOCK_KWARGS: _SPLASH_BLOCK_KWARGS.
  SplashAttention.is_causal: SplashAttention#is_causal.
  SplashAttention.local_window_size: SplashAttention#local_window_size.
  SplashAttention.auto_block_size: SplashAttention#auto_block_size.
  SplashAttention.sa_kwargs: SplashAttention#sa_kwargs.
  SplashAttention.__init__: SplashAttention#__init__().
---
# Module: [`torchtitan/experiments/tpu/kernels/splash_attention.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/splash_attention.py)

## Classes
### <a id="SplashAttention"></a>`SplashAttention`
- def: [`torchtitan/experiments/tpu/kernels/splash_attention.py:674`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/splash_attention.py#L674) — documented in [tpu-pallas-kernels](../../../../../concepts/tpu-pallas-kernels.md)
- doc: Inner attention using custom Splash Attention Pallas kernel.
- signature: `class SplashAttention(nn.Module):`
- members:
  - <a id="SplashAttention.forward"></a>`forward(self, q: torch.Tensor, k: torch.Tensor, v: torch.Tensor, *, scale: Optional[float] = None, enable_gqa: bool = False, is_causal: Optional[bool] = None, attention_masks: Any = None, positions: Optional[torch.Tensor] = None, segment_ids: Optional[torch.Tensor] = None, cp_rank: Optional[torch.Tensor] = None, **kwargs)` — [`L699`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/splash_attention.py#L699)
  - <a id="SplashAttention.auto_block_size"></a>`auto_block_size` — [`L696`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/splash_attention.py#L696)
  - <a id="SplashAttention.is_causal"></a>`is_causal` — [`L693`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/splash_attention.py#L693)
  - <a id="SplashAttention.local_window_size"></a>`local_window_size` — [`L694`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/splash_attention.py#L694)
  - <a id="SplashAttention.original_module"></a>`original_module` — [`L695`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/splash_attention.py#L695)
  - <a id="SplashAttention.sa_kwargs"></a>`sa_kwargs` — [`L697`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/splash_attention.py#L697)
- protocol/private: <a id="SplashAttention.__init__"></a>`__init__`[`L684`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/splash_attention.py#L684)
- uses (calls/refs, reference-scoped): [`segment_ids_from_positions`](../../../models/common/attention.md#segment_ids_from_positions), [`splash_sdpa`](splash_attention.md#splash_sdpa), [`splash_block_size_for`](splash_attention.md#splash_block_size_for), [`_SPLASH_BLOCK_KWARGS`](splash_attention.md#_SPLASH_BLOCK_KWARGS)
- used by: [`use_splash_attention_patch`](../workarounds.md#use_splash_attention_patch)  (2 test-only)

## Functions
- <a id="_document_aware_mask_info"></a>`_document_aware_mask_info(mask_info, segment_ids_b, block_q, block_kv, is_dkv)` — [`L39`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/splash_attention.py#L39) — Extend block sparsity to skip tiles that are entirely cross-document.
- <a id="_make_splash_attention_fn._get_layout"></a>`_get_layout(layout_str)` — [`L186`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/splash_attention.py#L186)
- <a id="_get_splash_op_names"></a>`_get_splash_op_names(**splash_kwargs)` — [`L436`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/splash_attention.py#L436) — Create and cache PyTorch forward/backward functions for splash attention.
- <a id="_make_splash_attention_fn"></a>`_make_splash_attention_fn(seq_len: int, n_heads: int, n_kv_heads: int, is_causal: bool = True, local_window_size: int | None = None, block_q: int = 512, block_kv: int = 512, block_kv_compute: int = 512, block_q_dkv: int = 512, block_kv_dkv: int = 512, block_kv_dkv_compute: int = 512, block_q_dq: int | None = None, block_kv_dq: int | None = None, use_fused_bwd_kernel: bool = True, q_layout: str = "HEAD_DIM_MINOR", k_layout: str = "HEAD_DIM_MINOR", v_layout: str = "HEAD_DIM_MINOR", use_vmap_bwd: bool = False, use_document_aware_block_skipping: bool = True, kv_seq_len: int | None = None)` — [`L132`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/splash_attention.py#L132) — Create JAX splash attention forward and backward functions.
- <a id="_maybe_document_aware_mask_info"></a>`_maybe_document_aware_mask_info(mask_info, segment_ids_b, block_q, block_kv, is_dkv, use_document_aware_block_skipping)` — [`L85`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/splash_attention.py#L85) — Choose document-aware block skipping or batch-native masking.
- <a id="_make_splash_attention_fn.splash_bwd_fn._scan_bwd_body"></a>`_scan_bwd_body(carry, args)` — [`L396`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/splash_attention.py#L396) — Single-element backward body for jax.lax.scan (sequential over batch).
- <a id="_make_splash_attention_fn._segment_ids"></a>`_segment_ids(segment_ids_b, cp_rank=None)` — [`L250`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/splash_attention.py#L250) — documented in [tpu-context-parallel-attention](../../../../../concepts/tpu-context-parallel-attention.md)
- <a id="_make_splash_attention_fn.splash_bwd_fn._single_bwd"></a>`_single_bwd(q_scaled_b, k_b, v_b, out_b, logsumexp_b, g_b, segment_ids_b)` — [`L340`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/splash_attention.py#L340) — Backward for one batch element using precomputed residuals.
- <a id="_make_splash_attention_fn.splash_fn._single_fwd_with_lse"></a>`_single_fwd_with_lse(q_b, k_b, v_b, segment_ids_b)` — [`L267`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/splash_attention.py#L267) — Forward for one batch element; returns (out_b, logsumexp_b).
- <a id="_slice_mask_info"></a>`_slice_mask_info(mask_info, cp_size: int, cp_rank: jax.Array | None)` — [`L127`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/splash_attention.py#L127) — Slice a stock JAX MaskInfo crafted for q_seq_shards=cp_size to cp_rank's shard. — documented in [tpu-context-parallel-attention](../../../../../concepts/tpu-context-parallel-attention.md)
- <a id="_get_splash_op_names.backward"></a>`backward(ctx, grad_out, grad_lse)` — [`L496`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/splash_attention.py#L496)
- <a id="_get_splash_op_names.setup_context"></a>`setup_context(ctx, inputs, output)` — [`L491`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/splash_attention.py#L491)
- <a id="splash_block_size_for"></a>`splash_block_size_for(seq_len: int, max_block_size: int = 512, min_block_size: int = 128)` — [`L646`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/splash_attention.py#L646) — Largest power-of-two block size <= ``max_block_size`` dividing ``seq_len``.
- <a id="_make_splash_attention_fn.splash_bwd_fn"></a>`splash_bwd_fn(q, k, v, out, logsumexp, g, segment_ids=None, cp_rank=None)` — [`L315`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/splash_attention.py#L315) — Backward: uses saved (out, logsumexp) — no extra forward pass.
- <a id="_make_splash_attention_fn.splash_fn"></a>`splash_fn(q, k, v, segment_ids=None, cp_rank=None)` — [`L260`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/splash_attention.py#L260) — Forward: returns (out, logsumexp) for the whole batch.
- <a id="splash_sdpa"></a>`splash_sdpa(q: torch.Tensor, k: torch.Tensor, v: torch.Tensor, *, segment_ids: Optional[torch.Tensor] = None, cp_rank: Optional[torch.Tensor] = None, scale: Optional[float] = None, is_causal: bool = True, local_window_size: Optional[int] = None, enable_gqa: bool = False, block_q: int = 512, block_kv: int = 512, block_dkv: int = 512, block_kv_compute: int = 512, block_q_dkv: int = 512, block_kv_dkv: int = 512, block_kv_dkv_compute: int = 512, block_q_dq: Optional[int] = None, block_kv_dq: Optional[int] = None, use_fused_bwd_kernel: bool = True, use_vmap_bwd: bool = False, use_document_aware_block_skipping: bool = True, q_layout: str = "HEAD_DIM_MINOR", k_layout: str = "HEAD_DIM_MINOR", v_layout: str = "HEAD_DIM_MINOR")` — [`L515`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/splash_attention.py#L515) — Replacement for F.scaled_dot_product_attention using splash attention.

## Module values
- <a id="_DEFAULT_MASK_VALUE"></a>`_DEFAULT_MASK_VALUE` — [`L35`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/splash_attention.py#L35)
- <a id="_MASK_INFO_SLICE_AXES"></a>`_MASK_INFO_SLICE_AXES` — [`L117`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/splash_attention.py#L117)
- <a id="_SPLASH_BLOCK_KWARGS"></a>`_SPLASH_BLOCK_KWARGS` — [`L663`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/splash_attention.py#L663)
- <a id="_make_mask"></a>`_make_mask` — [`L124`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/splash_attention.py#L124) — documented in [tpu-context-parallel-attention](../../../../../concepts/tpu-context-parallel-attention.md)
- <a id="_splash_op_name_cache"></a>`_splash_op_name_cache` — [`L432`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/splash_attention.py#L432)
- <a id="_warned_cp_block_skipping"></a>`_warned_cp_block_skipping` — [`L36`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/splash_attention.py#L36)
- <a id="custom_jax_kernel"></a>`custom_jax_kernel` — [`L33`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/splash_attention.py#L33)

