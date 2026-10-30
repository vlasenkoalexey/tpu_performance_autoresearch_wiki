---
title: 'Module: torchtitan/experiments/tpu/kernels/splash_bias_dropout.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/kernels/splash_bias_dropout.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.kernels.splash_bias_dropout`/
symbols:
  _build_kernel: _build_kernel().
  sbd_splash_attention: sbd_splash_attention().
  SbdConfig.static_args: SbdConfig#static_args().
  SbdConfig: SbdConfig#
  sbd_attention_bwd: sbd_attention_bwd().
  SbdConfig.update: SbdConfig#update().
  sbd_attention_fwd: sbd_attention_fwd().
  sbd_attention_fwd._fwd_b: sbd_attention_fwd()._fwd_b().
  sbd_attention_bwd._bwd_b: sbd_attention_bwd()._bwd_b().
  _document_aware_mask_info: _document_aware_mask_info().
  _segment_ids: _segment_ids().
  _NUM_STATIC_ARGS: _NUM_STATIC_ARGS.
  _backward: _backward().
  _kernel_statics: _kernel_statics().
  _sbd_fwd: _sbd_fwd.
  SbdConfig.attn_logits_soft_cap: SbdConfig#attn_logits_soft_cap.
  _document_aware_mask_info._restack: _document_aware_mask_info()._restack().
  _dkv_blocks: _dkv_blocks().
  _sbd_bwd: _sbd_bwd.
  _setup_context: _setup_context().
  _MASK_VALUE: _MASK_VALUE.
  SbdConfig.dropout_rate: SbdConfig#dropout_rate.
  SbdConfig.dq_reduction_steps: SbdConfig#dq_reduction_steps.
  _batch_map: _batch_map().
  _onehot_lookup: _onehot_lookup().
  _per_example: _per_example().
  PER_KEY_ROWS: PER_KEY_ROWS.
  SbdConfig.block_q: SbdConfig#block_q.
  SbdConfig.block_kv: SbdConfig#block_kv.
  SbdConfig.block_kv_compute: SbdConfig#block_kv_compute.
  SbdConfig.block_q_dkv: SbdConfig#block_q_dkv.
  SbdConfig.block_kv_dkv: SbdConfig#block_kv_dkv.
  SbdConfig.block_kv_dkv_compute: SbdConfig#block_kv_dkv_compute.
  SbdConfig.use_experimental_scheduler: SbdConfig#use_experimental_scheduler.
  SbdConfig.use_base2_exp: SbdConfig#use_base2_exp.
  SbdConfig.dropout_fold_rescale: SbdConfig#dropout_fold_rescale.
  SbdConfig.dropout_mask_version: SbdConfig#dropout_mask_version.
  SbdConfig.dropout_bwd_fused_compare: SbdConfig#dropout_bwd_fused_compare.
  SbdConfig.bias_per_key_rows: SbdConfig#bias_per_key_rows.
  SbdConfig.bias_per_key_dbias: SbdConfig#bias_per_key_dbias.
  SbdConfig.bias_per_key_dbias_mxu_reduce: SbdConfig#bias_per_key_dbias_mxu_reduce.
  SbdConfig.document_aware_skipping: SbdConfig#document_aware_skipping.
  _DKV_TILE_BYTES: _DKV_TILE_BYTES.
  _block_doc_overlaps: _block_doc_overlaps().
  _seed_words: _seed_words().
---
# Module: [`torchtitan/experiments/tpu/kernels/splash_bias_dropout.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/splash_bias_dropout.py)

## Classes
### <a id="SbdConfig"></a>`SbdConfig`
- def: [`torchtitan/experiments/tpu/kernels/splash_bias_dropout.py:69`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/splash_bias_dropout.py#L69) — documented in [tpu-pallas-kernels](../../../../../concepts/tpu-pallas-kernels.md)
- doc: Kernel configuration, forwarded as static op arguments on every call.
- signature: `class SbdConfig:`
- members:
  - <a id="SbdConfig.static_args"></a>`static_args(cls)` — [`L137`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/splash_bias_dropout.py#L137) — The static op arguments, in the order the op signatures declare.
  - <a id="SbdConfig.update"></a>`update(cls, **kwargs)` — [`L131`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/splash_bias_dropout.py#L131)
  - <a id="SbdConfig.attn_logits_soft_cap"></a>`attn_logits_soft_cap` — [`L104`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/splash_bias_dropout.py#L104)
  - <a id="SbdConfig.bias_per_key_dbias"></a>`bias_per_key_dbias` — [`L102`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/splash_bias_dropout.py#L102)
  - <a id="SbdConfig.bias_per_key_dbias_mxu_reduce"></a>`bias_per_key_dbias_mxu_reduce` — [`L103`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/splash_bias_dropout.py#L103)
  - <a id="SbdConfig.bias_per_key_rows"></a>`bias_per_key_rows` — [`L101`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/splash_bias_dropout.py#L101)
  - <a id="SbdConfig.block_kv"></a>`block_kv` — [`L79`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/splash_bias_dropout.py#L79)
  - <a id="SbdConfig.block_kv_compute"></a>`block_kv_compute` — [`L80`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/splash_bias_dropout.py#L80)
  - <a id="SbdConfig.block_kv_dkv"></a>`block_kv_dkv` — [`L82`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/splash_bias_dropout.py#L82)
  - <a id="SbdConfig.block_kv_dkv_compute"></a>`block_kv_dkv_compute` — [`L83`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/splash_bias_dropout.py#L83)
  - <a id="SbdConfig.block_q"></a>`block_q` — [`L78`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/splash_bias_dropout.py#L78)
  - <a id="SbdConfig.block_q_dkv"></a>`block_q_dkv` — [`L81`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/splash_bias_dropout.py#L81)
  - <a id="SbdConfig.document_aware_skipping"></a>`document_aware_skipping` — [`L111`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/splash_bias_dropout.py#L111)
  - <a id="SbdConfig.dq_reduction_steps"></a>`dq_reduction_steps` — [`L128`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/splash_bias_dropout.py#L128)
  - <a id="SbdConfig.dropout_bwd_fused_compare"></a>`dropout_bwd_fused_compare` — [`L97`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/splash_bias_dropout.py#L97)
  - <a id="SbdConfig.dropout_fold_rescale"></a>`dropout_fold_rescale` — [`L95`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/splash_bias_dropout.py#L95)
  - <a id="SbdConfig.dropout_mask_version"></a>`dropout_mask_version` — [`L96`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/splash_bias_dropout.py#L96)
  - <a id="SbdConfig.dropout_rate"></a>`dropout_rate` — [`L94`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/splash_bias_dropout.py#L94)
  - <a id="SbdConfig.use_base2_exp"></a>`use_base2_exp` — [`L92`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/splash_bias_dropout.py#L92)
  - <a id="SbdConfig.use_experimental_scheduler"></a>`use_experimental_scheduler` — [`L84`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/splash_bias_dropout.py#L84)
- used by: [`sbd_splash_attention`](splash_bias_dropout.md#sbd_splash_attention), [`_sbd_forward`](../transformers_modeling_backend/attention.md#_sbd_forward), [`_dropout_block_problem`](../transformers_modeling_backend/attention.md#_dropout_block_problem), [`_NUM_STATIC_ARGS`](splash_bias_dropout.md#_NUM_STATIC_ARGS)  (8 test-only)

## Functions
- <a id="_backward"></a>`_backward(ctx, grad_out, grad_lse)` — [`L788`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/splash_bias_dropout.py#L788)
- <a id="_batch_map"></a>`_batch_map(fn, args, in_axes, serial)` — [`L263`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/splash_bias_dropout.py#L263) — `vmap(fn, in_axes)(*args)`, or a `lax.scan` over the batch if `serial`.
- <a id="_block_doc_overlaps"></a>`_block_doc_overlaps(seg_b, bq: int, bkv: int)` — [`L292`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/splash_bias_dropout.py#L292) — `(num_q_blocks, num_kv_blocks)` bool: can this tile hold a same-document pair?
- <a id="_build_kernel"></a>`_build_kernel(seq_len: int, causal: bool, scale: float, local_window_size: int, use_dropout: bool, use_bias: bool, block_q: int, block_kv: int, block_kv_compute: int, block_q_dkv: int, block_kv_dkv: int, block_kv_dkv_compute: int, use_experimental_scheduler: bool, use_base2_exp: bool, attn_logits_soft_cap: float | None, dropout_rate: float, dropout_fold_rescale: bool, dropout_mask_version: int, dropout_bwd_fused_compare: bool, bias_per_key_rows: int, bias_per_key_dbias: bool, bias_per_key_dbias_mxu_reduce: bool, dq_reduction_steps: int = 0)` — [`L161`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/splash_bias_dropout.py#L161) — Constructs the fork kernel + static mask infos for one configuration. — documented in [tpu-pallas-kernels](../../../../../concepts/tpu-pallas-kernels.md)
- <a id="sbd_attention_bwd._bwd_b"></a>`_bwd_b(q_b, k_b, v_b, out_b, lse_b, g_b, seed_b, seg_b)` — [`L680`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/splash_bias_dropout.py#L680)
- <a id="_dkv_blocks"></a>`_dkv_blocks(block_q_dkv, block_kv_dkv, block_kv_dkv_compute, head_dim, itemsize)` — [`L245`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/splash_bias_dropout.py#L245) — Caps the dkv block sizes so their tiles fit `_DKV_TILE_BYTES`.
- <a id="_document_aware_mask_info"></a>`_document_aware_mask_info(mask_info, seg_b, bq: int, bkv: int, *, is_dkv: bool)` — [`L330`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/splash_bias_dropout.py#L330) — Drop the grid steps this packed example cannot need; shrink the grid.
- <a id="sbd_attention_fwd._fwd_b"></a>`_fwd_b(q_b, k_b, v_b, seed_b, seg_b)` — [`L552`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/splash_bias_dropout.py#L552)
- <a id="_kernel_statics"></a>`_kernel_statics(kernel)` — [`L281`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/splash_bias_dropout.py#L281)
- <a id="_onehot_lookup"></a>`_onehot_lookup(table, idx)` — [`L318`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/splash_bias_dropout.py#L318) — `table[idx]` for in-range `idx`, without an XLA gather.
- <a id="_per_example"></a>`_per_example(mask_info, segment_ids, document_aware_skipping)` — [`L750`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/splash_bias_dropout.py#L750) — Whether `_document_aware_mask_info` gives each of several examples its
- <a id="_document_aware_mask_info._restack"></a>`_restack(values, dead, dtype)` — [`L450`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/splash_bias_dropout.py#L450)
- <a id="_seed_words"></a>`_seed_words(seed: int, batch: int, device: torch.device)` — [`L801`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/splash_bias_dropout.py#L801) — Deterministic per-batch (B, 2) int32 seed words from one python int.
- <a id="_segment_ids"></a>`_segment_ids(seg_b)` — [`L762`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/splash_bias_dropout.py#L762) — One batch element's `(S,)` ids as the kernel's `SegmentIds`, or None.
- <a id="_setup_context"></a>`_setup_context(ctx, inputs, output)` — [`L781`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/splash_bias_dropout.py#L781)
- <a id="sbd_attention_bwd"></a>`sbd_attention_bwd(q: jax.Array, k: jax.Array, v: jax.Array, bias: jax.Array | None, dropout_seed: jax.Array | None, segment_ids: jax.Array | None, out: jax.Array, logsumexp: jax.Array, grad_out: jax.Array, causal: bool, scale: float, local_window_size: int, heads_first: bool, block_q: int, block_kv: int, block_kv_compute: int, block_q_dkv: int, block_kv_dkv: int, block_kv_dkv_compute: int, use_experimental_scheduler: bool, use_base2_exp: bool, attn_logits_soft_cap: float | None, dropout_rate: float, dropout_fold_rescale: bool, dropout_mask_version: int, dropout_bwd_fused_compare: bool, bias_per_key_rows: int, bias_per_key_dbias: bool, bias_per_key_dbias_mxu_reduce: bool, document_aware_skipping: bool, dq_reduction_steps: int)` — [`L595`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/splash_bias_dropout.py#L595) — Backward from saved residuals -- no forward re-run. Returns
- <a id="sbd_attention_fwd"></a>`sbd_attention_fwd(q: jax.Array, k: jax.Array, v: jax.Array, bias: jax.Array | None, dropout_seed: jax.Array | None, segment_ids: jax.Array | None, causal: bool, scale: float, local_window_size: int, heads_first: bool, block_q: int, block_kv: int, block_kv_compute: int, block_q_dkv: int, block_kv_dkv: int, block_kv_dkv_compute: int, use_experimental_scheduler: bool, use_base2_exp: bool, attn_logits_soft_cap: float | None, dropout_rate: float, dropout_fold_rescale: bool, dropout_mask_version: int, dropout_bwd_fused_compare: bool, bias_per_key_rows: int, bias_per_key_dbias: bool, bias_per_key_dbias_mxu_reduce: bool, document_aware_skipping: bool, dq_reduction_steps: int)` — [`L464`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/splash_bias_dropout.py#L464) — Forward. Layouts: q `(B, S, H, D)` torch-standard; k/v `(B, S, H_kv, D)`
- <a id="sbd_splash_attention"></a>`sbd_splash_attention(q: torch.Tensor, k: torch.Tensor, v: torch.Tensor, bias: Optional[torch.Tensor] = None, *, dropout_seed: int | torch.Tensor = 0, segment_ids: Optional[torch.Tensor] = None, is_causal: bool = True, scale: Optional[float] = None, local_window_size: Optional[int] = None, heads_first: bool = False)` — [`L820`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/splash_bias_dropout.py#L820) — Splash attention with optional additive bias and PRNG dropout. — documented in [tpu-pallas-kernels](../../../../../concepts/tpu-pallas-kernels.md)

## Module values
- <a id="PER_KEY_ROWS"></a>`PER_KEY_ROWS` — [`L66`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/splash_bias_dropout.py#L66)
- <a id="_DKV_TILE_BYTES"></a>`_DKV_TILE_BYTES` — [`L242`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/splash_bias_dropout.py#L242)
- <a id="_MASK_VALUE"></a>`_MASK_VALUE` — [`L65`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/splash_bias_dropout.py#L65)
- <a id="_NUM_STATIC_ARGS"></a>`_NUM_STATIC_ARGS` — [`L778`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/splash_bias_dropout.py#L778)
- <a id="_sbd_bwd"></a>`_sbd_bwd` — [`L776`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/splash_bias_dropout.py#L776)
- <a id="_sbd_fwd"></a>`_sbd_fwd` — [`L775`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/splash_bias_dropout.py#L775)

