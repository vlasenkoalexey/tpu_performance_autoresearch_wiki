---
title: 'Module: torchtitan/experiments/tpu/transformers_modeling_backend/attention.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/transformers_modeling_backend/attention.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.transformers_modeling_backend.attention`/
symbols:
  splash_attention_forward: splash_attention_forward().
  _sbd_forward: _sbd_forward().
  _segment_ids: _segment_ids().
  _unsupported: _unsupported().
  _dropout_block_problem: _dropout_block_problem().
  _log_once: _log_once().
  _kernel_kwargs: _kernel_kwargs().
  _report: _report().
  _reported._reported: _reported._reported.
  _pick_block: _pick_block().
  document_segment_ids: document_segment_ids().
  _window: _window().
  _fallback_mask: _fallback_mask().
  _tracing: _tracing().
  _SEED_SALT._SEED_SALT: _SEED_SALT._SEED_SALT.
  _seed_salt: _seed_salt().
  register: register().
  _SBD_KERNEL_KWARGS: _SBD_KERNEL_KWARGS.
  _MIN_BLOCK: _MIN_BLOCK.
  _DROPOUT_QUANTUM: _DROPOUT_QUANTUM.
  _padding_mask: _padding_mask().
  INFO_REPORTS: INFO_REPORTS.
  _softcapped_attention: _softcapped_attention().
  _document_masked: _document_masked().
---
# Module: [`torchtitan/experiments/tpu/transformers_modeling_backend/attention.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/attention.py)

## Functions
- <a id="_document_masked"></a>`_document_masked(module)` — [`L351`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/attention.py#L351) — True when the flavor asked for document-causal attention.
- <a id="_dropout_block_problem"></a>`_dropout_block_problem(module, q_len: int, kv_len: int)` — [`L199`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/attention.py#L199) — Why the blocks this call would actually use cannot run dropout, or None.
- <a id="_fallback_mask"></a>`_fallback_mask(module, query, key, attention_mask, kwargs, is_causal, window)` — [`L311`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/attention.py#L311) — The dense equivalent of the kernel's mask, for the SDPA fallback.
- <a id="_kernel_kwargs"></a>`_kernel_kwargs(module, q_len: int, kv_len: int)` — [`L142`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/attention.py#L142) — The model's configured tuning with every block clamped to the sequence.
- <a id="_log_once"></a>`_log_once(key: str, message: str, *args)` — [`L108`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/attention.py#L108)
- <a id="_padding_mask"></a>`_padding_mask(attention_mask)` — [`L151`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/attention.py#L151) — The 2D per-token keep-mask behind ``attention_mask``, or None.
- <a id="_pick_block"></a>`_pick_block(q_len: int, kv_len: int, preferred: int)` — [`L132`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/attention.py#L132) — Largest block <= ``preferred`` that tiles both lengths, or None.
- <a id="_report"></a>`_report(reason: str)` — [`L101`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/attention.py#L101) — Report once. Call sites guard with `_tracing()`; see that helper.
- <a id="_sbd_forward"></a>`_sbd_forward(query, key, value, segment_ids, is_causal, scaling, window, dropout, kernel_kwargs, seg_desc, softcap=None)` — [`L443`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/attention.py#L443) — The kernel call: document-aware skipping, exact segment masking at — documented in [tpu-pallas-kernels](../../../../../concepts/tpu-pallas-kernels.md)
- <a id="_seed_salt"></a>`_seed_salt()` — [`L114`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/attention.py#L114) — A per-rank constant to fold into the dropout seed (0 off a mesh).
- <a id="_segment_ids"></a>`_segment_ids(module, attention_mask, kwargs)` — [`L250`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/attention.py#L250) — Fold document boundaries and padding into one segment-id tensor.
- <a id="_softcapped_attention"></a>`_softcapped_attention(module, query, key, value, mask, is_causal, scaling, softcap, dropout)` — [`L283`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/attention.py#L283) — Plain attention with HF's soft-cap, for the fallback (SDPA has no cap).
- <a id="_tracing"></a>`_tracing()` — [`L85`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/attention.py#L85) — True while Dynamo is tracing.
- <a id="_unsupported"></a>`_unsupported(module, query, key, attention_mask, dropout, is_causal, window)` — [`L169`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/attention.py#L169) — Why splash cannot take this call, or None if it can.
- <a id="_window"></a>`_window(module, kwargs)` — [`L226`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/attention.py#L226) — The layer's sliding window in HF's convention, or None.
- <a id="document_segment_ids"></a>`document_segment_ids(position_ids: torch.Tensor)` — [`L240`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/attention.py#L240) — Per-document segment ids (numbered from 1) from packed ``position_ids``.
- <a id="register"></a>`register()` — [`L516`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/attention.py#L516) — Make `attn_implementation="splash_tpu"` selectable on any HF model.
- <a id="splash_attention_forward"></a>`splash_attention_forward(module, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor, attention_mask=None, dropout: float = 0, scaling: float | None = None, is_causal: bool | None = None, **kwargs)` — [`L365`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/attention.py#L365) — HF attention implementation backed by the TPU splash-attention kernel.

## Module values
- <a id="INFO_REPORTS"></a>`INFO_REPORTS` — [`L70`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/attention.py#L70)
- <a id="_DROPOUT_QUANTUM"></a>`_DROPOUT_QUANTUM` — [`L79`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/attention.py#L79)
- <a id="_MIN_BLOCK"></a>`_MIN_BLOCK` — [`L76`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/attention.py#L76)
- <a id="_SBD_KERNEL_KWARGS"></a>`_SBD_KERNEL_KWARGS` — [`L59`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/attention.py#L59)
- <a id="_SEED_SALT._SEED_SALT"></a>`_SEED_SALT` — [`L82`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/attention.py#L82)
- <a id="_reported._reported"></a>`_reported` — [`L80`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/attention.py#L80)

