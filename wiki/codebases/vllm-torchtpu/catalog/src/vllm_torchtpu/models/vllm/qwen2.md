---
title: 'Module: src/vllm_torchtpu/models/vllm/qwen2.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/models/vllm/qwen2.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.models.vllm.qwen2`/TPUTPPaddedQwen2Attention#
symbols:
  TPUTPPaddedQwen2Attention.__init__: __init__().
  TPUTPPaddedQwen2Attention: ''
  TPUTPPaddedQwen2Attention.qkv_proj: qkv_proj.
  TPUTPPaddedQwen2Attention.o_proj: o_proj.
  TPUTPPaddedQwen2Attention.orig_total_num_heads: orig_total_num_heads.
  TPUTPPaddedQwen2Attention.hidden_size: hidden_size.
---
# Module: [`src/vllm_torchtpu/models/vllm/qwen2.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen2.py)

## Classes
### <a id="TPUTPPaddedQwen2Attention"></a>`TPUTPPaddedQwen2Attention`
- def: [`src/vllm_torchtpu/models/vllm/qwen2.py:33`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen2.py#L33)
- doc: Qwen2Attention that zero-pads Q heads per KV group when heads % tp != 0.
- signature: `class TPUTPPaddedQwen2Attention(Qwen2Attention):`
- members:
  - <a id="TPUTPPaddedQwen2Attention.hidden_size"></a>`hidden_size` — [`L94`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen2.py#L94)
  - <a id="TPUTPPaddedQwen2Attention.o_proj"></a>`o_proj` — [`L104`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen2.py#L104)
  - <a id="TPUTPPaddedQwen2Attention.orig_total_num_heads"></a>`orig_total_num_heads` — [`L90`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen2.py#L90)
  - <a id="TPUTPPaddedQwen2Attention.qkv_proj"></a>`qkv_proj` — [`L95`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen2.py#L95)
- protocol/private: <a id="TPUTPPaddedQwen2Attention.__init__"></a>`__init__`[`L46`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen2.py#L46)
- uses (calls/refs, reference-scoped): [`head_dim`](../../gqa_head_padding.md#GqaPaddingSpec.head_dim), [`install_o_proj_padded_loader`](../../gqa_head_padding.md#install_o_proj_padded_loader), [`install_qkv_padded_loader`](../../gqa_head_padding.md#install_qkv_padded_loader), [`GqaPaddingSpec`](../../gqa_head_padding.md#GqaPaddingSpec), [`compute_padded_gqa_heads`](../../gqa_head_padding.md#compute_padded_gqa_heads), [`num_kv_heads`](../../gqa_head_padding.md#GqaPaddingSpec.num_kv_heads), [`orig_q_per_kv`](../../gqa_head_padding.md#GqaPaddingSpec.orig_q_per_kv), [`padded_q_per_kv`](../../gqa_head_padding.md#GqaPaddingSpec.padded_q_per_kv)
- used by: [`maybe_patch_qwen2`](qwen2_patch.md#maybe_patch_qwen2)

