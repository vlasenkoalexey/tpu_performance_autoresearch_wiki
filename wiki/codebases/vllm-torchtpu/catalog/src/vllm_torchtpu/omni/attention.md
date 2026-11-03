---
title: 'Module: src/vllm_torchtpu/omni/attention.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/omni/attention.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.omni.attention`/
symbols:
  TpuSDPAImpl: TpuSDPAImpl#
  TpuFlashAttentionImpl.forward: TpuFlashAttentionImpl#forward().
  TpuSDPAImpl.forward: TpuSDPAImpl#forward().
  TpuFlashAttentionImpl: TpuFlashAttentionImpl#
  logger: logger.
  _flash_attention_op: _flash_attention_op().
  _flash_attention_op.diffusion_flash_attention: _flash_attention_op().diffusion_flash_attention().
  TpuFlashAttentionImpl._op: TpuFlashAttentionImpl#_op.
  TpuFlashAttentionImpl._needs_sdpa_fallback: TpuFlashAttentionImpl#_needs_sdpa_fallback().
  TpuSDPABackend.get_impl_cls: TpuSDPABackend#get_impl_cls().
  TpuFlashAttentionBackend.get_impl_cls: TpuFlashAttentionBackend#get_impl_cls().
  TpuSDPABackend: TpuSDPABackend#
  TpuSDPABackend.get_name: TpuSDPABackend#get_name().
  TpuFlashAttentionImpl.__init__: TpuFlashAttentionImpl#__init__().
  TpuFlashAttentionBackend: TpuFlashAttentionBackend#
  TpuFlashAttentionBackend.get_name: TpuFlashAttentionBackend#get_name().
---
# Module: [`src/vllm_torchtpu/omni/attention.py`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/attention.py)

## Classes
### <a id="TpuFlashAttentionBackend"></a>`TpuFlashAttentionBackend`
- def: [`src/vllm_torchtpu/omni/attention.py:127`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/attention.py#L127)
- doc: TPU diffusion attention backend using a Pallas flash kernel.
- signature: `class TpuFlashAttentionBackend(SDPABackend):`
- members:
  - <a id="TpuFlashAttentionBackend.get_impl_cls"></a>`get_impl_cls()` — [`L135`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/attention.py#L135)
  - <a id="TpuFlashAttentionBackend.get_name"></a>`get_name()` — [`L131`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/attention.py#L131)
- uses (calls/refs, reference-scoped): [`TpuFlashAttentionImpl`](attention.md#TpuFlashAttentionImpl)

### <a id="TpuFlashAttentionImpl"></a>`TpuFlashAttentionImpl`  ·  implements/extends TpuSDPAImpl
- def: [`src/vllm_torchtpu/omni/attention.py:77`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/attention.py#L77) — documented in [omni-diffusion-support](../../../../concepts/omni-diffusion-support.md)
- doc: Pallas flash attention for diffusion transformers on TPU.
- signature: `class TpuFlashAttentionImpl(TpuSDPAImpl):`
- members:
  - <a id="TpuFlashAttentionImpl.forward"></a>`forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor, attn_metadata: Any | None = None)` — [`L109`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/attention.py#L109) — documented in [omni-diffusion-support](../../../../concepts/omni-diffusion-support.md)
- protocol/private: <a id="TpuFlashAttentionImpl.__init__"></a>`__init__`[`L80`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/attention.py#L80), <a id="TpuFlashAttentionImpl._needs_sdpa_fallback"></a>`_needs_sdpa_fallback`[`L85`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/attention.py#L85), <a id="TpuFlashAttentionImpl._op"></a>`_op`[`L83`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/attention.py#L83)
- uses (calls/refs, reference-scoped): [`TpuSDPAImpl`](attention.md#TpuSDPAImpl), [`forward`](attention.md#TpuSDPAImpl.forward), [`_flash_attention_op`](attention.md#_flash_attention_op), [`logger`](attention.md#logger)
- used by: [`TpuSDPAImpl`](attention.md#TpuSDPAImpl), [`forward`](attention.md#TpuSDPAImpl.forward), [`get_impl_cls`](attention.md#TpuFlashAttentionBackend.get_impl_cls)

### <a id="TpuSDPABackend"></a>`TpuSDPABackend`
- def: [`src/vllm_torchtpu/omni/attention.py:51`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/attention.py#L51)
- doc: TPU attention backend for diffusion models using PyTorch SDPA.
- signature: `class TpuSDPABackend(SDPABackend):`
- members:
  - <a id="TpuSDPABackend.get_impl_cls"></a>`get_impl_cls()` — [`L59`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/attention.py#L59)
  - <a id="TpuSDPABackend.get_name"></a>`get_name()` — [`L55`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/attention.py#L55)
- uses (calls/refs, reference-scoped): [`TpuSDPAImpl`](attention.md#TpuSDPAImpl)

### <a id="TpuSDPAImpl"></a>`TpuSDPAImpl`
- def: [`src/vllm_torchtpu/omni/attention.py:36`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/attention.py#L36) — documented in [omni-diffusion-support](../../../../concepts/omni-diffusion-support.md)
- doc: TPU implementation of SDPA attention for diffusion models.
- signature: `class TpuSDPAImpl(SDPAImpl):`
- members:
  - <a id="TpuSDPAImpl.forward"></a>`forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor, attn_metadata: Any | None = None)` — [`L39`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/attention.py#L39) — documented in [omni-diffusion-support](../../../../concepts/omni-diffusion-support.md)
- uses (calls/refs, reference-scoped): [`forward`](attention.md#TpuFlashAttentionImpl.forward), [`TpuFlashAttentionImpl`](attention.md#TpuFlashAttentionImpl)
- used by: [`_patch_sdpa_fallback_dispatch`](patches.md#_patch_sdpa_fallback_dispatch), [`forward`](attention.md#TpuFlashAttentionImpl.forward), [`TpuFlashAttentionImpl`](attention.md#TpuFlashAttentionImpl), [`get_impl_cls`](attention.md#TpuSDPABackend.get_impl_cls)

## Functions
- <a id="_flash_attention_op"></a>`_flash_attention_op()` — [`L64`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/attention.py#L64) — Builds the torch custom op wrapping the Pallas kernel (once, eagerly).
- <a id="_flash_attention_op.diffusion_flash_attention"></a>`diffusion_flash_attention(q: jax.Array, k: jax.Array, v: jax.Array, scale: float)` — [`L67`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/attention.py#L67)

## Module values
- <a id="logger"></a>`logger` — [`L33`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/attention.py#L33)

