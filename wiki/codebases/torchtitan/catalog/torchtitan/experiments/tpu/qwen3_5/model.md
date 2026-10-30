---
title: 'Module: torchtitan/experiments/tpu/qwen3_5/model.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/qwen3_5/model.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.qwen3_5.model`/
symbols:
  TpuQwen35Attention.forward: TpuQwen35Attention#forward().
  TpuQwen35TransformerBlock.forward: TpuQwen35TransformerBlock#forward().
  TpuQwen35Attention.Config: TpuQwen35Attention#Config#
  TpuQwen35TransformerBlock.Config: TpuQwen35TransformerBlock#Config#
  TpuQwen35Attention: TpuQwen35Attention#
  TpuQwen35TransformerBlock: TpuQwen35TransformerBlock#
---
# Module: [`torchtitan/experiments/tpu/qwen3_5/model.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3_5/model.py)

## Classes
### <a id="TpuQwen35Attention"></a>`TpuQwen35Attention`  ·  implements/extends Qwen35Attention
- def: [`torchtitan/experiments/tpu/qwen3_5/model.py:13`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3_5/model.py#L13)
- doc: `Qwen35Attention` that passes `positions` to the inner attention.
- signature: `class TpuQwen35Attention(Qwen35Attention):`
- members:
  - <a id="TpuQwen35Attention.forward"></a>`forward(self, x_TD: torch.Tensor, attention_masks: AttentionMasksType | None, positions: torch.Tensor | None = None)` — [`L26`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3_5/model.py#L26)
- uses (calls/refs, reference-scoped): [`AttentionMasksType`](../../../models/common/attention.md#AttentionMasksType), [`Qwen35Attention`](../../../models/qwen3_5/model.md#Qwen35Attention), [`rotary_dim`](../../../models/qwen3_5/model.md#Qwen35Attention.rotary_dim), [`head_dim`](../../../models/qwen3_5/model.md#Qwen35Attention.head_dim), [`enable_gqa`](../../../models/qwen3_5/model.md#Qwen35Attention.enable_gqa), [`inner_attention`](../../../models/qwen3_5/model.md#Qwen35Attention.inner_attention), [`k_norm`](../../../models/qwen3_5/model.md#Qwen35Attention.k_norm), [`q_norm`](../../../models/qwen3_5/model.md#Qwen35Attention.q_norm), [`rope`](../../../models/qwen3_5/model.md#Qwen35Attention.rope), [`wk`](../../../models/qwen3_5/model.md#Qwen35Attention.wk), [`wo`](../../../models/qwen3_5/model.md#Qwen35Attention.wo), [`wq`](../../../models/qwen3_5/model.md#Qwen35Attention.wq), [`wv`](../../../models/qwen3_5/model.md#Qwen35Attention.wv), [`scaling`](../../../models/qwen3_5/model.md#Qwen35Attention.scaling)
- used by: [`use_tpu_modules`](__init__.md#use_tpu_modules), [`forward`](../../../models/qwen3_5/model.md#Qwen35Attention.forward), [`Qwen35Attention`](../../../models/qwen3_5/model.md#Qwen35Attention)  (1 test-only)

### <a id="TpuQwen35Attention.Config"></a>`TpuQwen35Attention.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/tpu/qwen3_5/model.py:23`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3_5/model.py#L23)
- signature: `class Config(Qwen35Attention.Config):`
- uses (calls/refs, reference-scoped): [`Qwen35Attention`](../../../models/qwen3_5/model.md#Qwen35Attention), [`Config`](../../../models/qwen3_5/model.md#Qwen35Attention.Config)
- used by: [`use_tpu_modules`](__init__.md#use_tpu_modules)  (1 test-only)

### <a id="TpuQwen35TransformerBlock"></a>`TpuQwen35TransformerBlock`  ·  implements/extends Qwen35TransformerBlock
- def: [`torchtitan/experiments/tpu/qwen3_5/model.py:75`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3_5/model.py#L75)
- doc: `Qwen35TransformerBlock` that also passes `positions` to GatedDeltaNet.
- signature: `class TpuQwen35TransformerBlock(Qwen35TransformerBlock):`
- members:
  - <a id="TpuQwen35TransformerBlock.forward"></a>`forward(self, x_TD: torch.Tensor, attention_masks: Qwen35AttentionMaskDict | None, positions: torch.Tensor | None = None)` — [`L87`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3_5/model.py#L87)
- uses (calls/refs, reference-scoped): [`Qwen35TransformerBlock`](../../../models/qwen3_5/model.md#Qwen35TransformerBlock), [`attn`](../../../models/qwen3_5/model.md#Qwen35TransformerBlock.attn), [`Qwen35AttentionMaskDict`](../../../models/qwen3_5/model.md#Qwen35AttentionMaskDict), [`moe`](../../../models/qwen3_5/model.md#Qwen35TransformerBlock.moe), [`moe_enabled`](../../../models/qwen3_5/model.md#Qwen35TransformerBlock.moe_enabled), [`attention_norm`](../../../models/qwen3_5/model.md#Qwen35TransformerBlock.attention_norm), [`feed_forward`](../../../models/qwen3_5/model.md#Qwen35TransformerBlock.feed_forward), [`ffn_norm`](../../../models/qwen3_5/model.md#Qwen35TransformerBlock.ffn_norm), [`attn_mask_key`](../../../models/qwen3_5/model.md#Qwen35TransformerBlock.attn_mask_key)
- used by: [`use_tpu_modules`](__init__.md#use_tpu_modules), [`forward`](../../../models/qwen3_5/model.md#Qwen35TransformerBlock.forward), [`Qwen35TransformerBlock`](../../../models/qwen3_5/model.md#Qwen35TransformerBlock)  (1 test-only)

### <a id="TpuQwen35TransformerBlock.Config"></a>`TpuQwen35TransformerBlock.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/tpu/qwen3_5/model.py:84`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3_5/model.py#L84)
- signature: `class Config(Qwen35TransformerBlock.Config):`
- uses (calls/refs, reference-scoped): [`Qwen35TransformerBlock`](../../../models/qwen3_5/model.md#Qwen35TransformerBlock), [`Config`](../../../models/qwen3_5/model.md#Qwen35TransformerBlock.Config)
- used by: [`use_tpu_modules`](__init__.md#use_tpu_modules)  (1 test-only)

