---
title: 'Module: src/vllm_torchtpu/layers/adapter/vision_attention.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/layers/adapter/vision_attention.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.layers.adapter.vision_attention`/
symbols:
  _vision_flash_core: _vision_flash_core().
  TpuMMEncoderAttention._flash_attention: TpuMMEncoderAttention#_flash_attention().
  TpuMMEncoderAttention.__init__: TpuMMEncoderAttention#__init__().
  TpuMMEncoderAttention: TpuMMEncoderAttention#
  TpuMMEncoderAttention.forward_oot: TpuMMEncoderAttention#forward_oot().
  TpuMMEncoderAttention._vision_op: TpuMMEncoderAttention#_vision_op.
  TpuMMEncoderAttention._prep: TpuMMEncoderAttention#_prep().
  logger: logger.
  _BLOCK_SIZE: _BLOCK_SIZE.
  _VMEM_LIMIT_BYTES: _VMEM_LIMIT_BYTES.
  TpuMMEncoderAttention.forward_tpu: TpuMMEncoderAttention#forward_tpu.
---
# Module: [`src/vllm_torchtpu/layers/adapter/vision_attention.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/vision_attention.py)

## Classes
### <a id="TpuMMEncoderAttention"></a>`TpuMMEncoderAttention`
- def: [`src/vllm_torchtpu/layers/adapter/vision_attention.py:73`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/vision_attention.py#L73)
- doc: MMEncoderAttention whose TPU path uses the Pallas flash kernel.
- signature: `class TpuMMEncoderAttention(MMEncoderAttention):`
- members:
  - <a id="TpuMMEncoderAttention._flash_attention"></a>`_flash_attention(self, q: torch.Tensor, k: torch.Tensor, v: torch.Tensor, cu_seqlens: torch.Tensor | None)` — [`L115`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/vision_attention.py#L115) — q,k,v: ``[batch, seq, num_heads, head_dim]``; cu_seqlens packs images.
  - <a id="TpuMMEncoderAttention.forward_oot"></a>`forward_oot(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor, cu_seqlens: torch.Tensor | None = None, max_seqlen: torch.Tensor | None = None, sequence_lengths: torch.Tensor | None = None)` — [`L87`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/vision_attention.py#L87)
  - <a id="TpuMMEncoderAttention.forward_tpu"></a>`forward_tpu` — [`L157`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/vision_attention.py#L157)
- protocol/private: <a id="TpuMMEncoderAttention.__init__"></a>`__init__`[`L80`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/vision_attention.py#L80), <a id="TpuMMEncoderAttention._prep"></a>`_prep`[`L140`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/vision_attention.py#L140), <a id="TpuMMEncoderAttention._vision_op"></a>`_vision_op`[`L78`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/vision_attention.py#L78)
- uses (calls/refs, reference-scoped): [`_vision_flash_core`](vision_attention.md#_vision_flash_core), [`_BLOCK_SIZE`](vision_attention.md#_BLOCK_SIZE)

## Functions
- <a id="_vision_flash_core"></a>`_vision_flash_core(q: jax.Array, k: jax.Array, v: jax.Array, q_seg: jax.Array, kv_seg: jax.Array)` — [`L56`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/vision_attention.py#L56)

## Module values
- <a id="_BLOCK_SIZE"></a>`_BLOCK_SIZE` — [`L52`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/vision_attention.py#L52)
- <a id="_VMEM_LIMIT_BYTES"></a>`_VMEM_LIMIT_BYTES` — [`L53`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/vision_attention.py#L53)
- <a id="logger"></a>`logger` — [`L49`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/vision_attention.py#L49)

