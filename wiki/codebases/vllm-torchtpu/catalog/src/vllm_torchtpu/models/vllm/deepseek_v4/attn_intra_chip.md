---
title: 'Module: src/vllm_torchtpu/models/vllm/deepseek_v4/attn_intra_chip.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/models/vllm/deepseek_v4/attn_intra_chip.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.models.vllm.deepseek_v4.attn_intra_chip`/
symbols:
  VllmDeepseekV4MLAAttentionIntraChip._o_proj: VllmDeepseekV4MLAAttentionIntraChip#_o_proj().
  VllmDeepseekV4MLAAttentionIntraChip.wo_b: VllmDeepseekV4MLAAttentionIntraChip#wo_b.
  VllmDeepseekV4MLAAttentionIntraChip._project_q: VllmDeepseekV4MLAAttentionIntraChip#_project_q().
  VllmDeepseekV4MLAAttentionIntraChip.n_local_groups: VllmDeepseekV4MLAAttentionIntraChip#n_local_groups.
  VllmDeepseekV4MLAAttentionIntraChip.__init__: VllmDeepseekV4MLAAttentionIntraChip#__init__().
  VllmDeepseekV4MLAAttentionIntraChip.wo_a: VllmDeepseekV4MLAAttentionIntraChip#wo_a.
  VllmDeepseekV4MLAAttentionIntraChip.process_weights_after_loading: VllmDeepseekV4MLAAttentionIntraChip#process_weights_after_loading().
  logger: logger.
  _chip_pair_group: _chip_pair_group().
  VllmDeepseekV4MLAAttentionIntraChip: VllmDeepseekV4MLAAttentionIntraChip#
  VllmDeepseekV4MLAAttentionIntraChip._chip_pair: VllmDeepseekV4MLAAttentionIntraChip#_chip_pair.
  VllmDeepseekV4MLAAttentionIntraChip.n_local_heads: VllmDeepseekV4MLAAttentionIntraChip#n_local_heads.
  _swap_with_peer_chiplet: _swap_with_peer_chiplet().
  VllmDeepseekV4MLAAttentionIntraChip.wq_b: VllmDeepseekV4MLAAttentionIntraChip#wq_b.
  _load_current_chiplet_slice: _load_current_chiplet_slice().
---
# Module: [`src/vllm_torchtpu/models/vllm/deepseek_v4/attn_intra_chip.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/attn_intra_chip.py)

## Classes
### <a id="VllmDeepseekV4MLAAttentionIntraChip"></a>`VllmDeepseekV4MLAAttentionIntraChip`  ·  implements/extends VllmDeepseekV4MLAAttention
- def: [`src/vllm_torchtpu/models/vllm/deepseek_v4/attn_intra_chip.py:106`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/attn_intra_chip.py#L106)
- doc: DSv4 attention with `wq_b`/`wo_a`/`wo_b` split across a chip's two cores.
- signature: `class VllmDeepseekV4MLAAttentionIntraChip(VllmDeepseekV4MLAAttention):`
- members:
  - <a id="VllmDeepseekV4MLAAttentionIntraChip.process_weights_after_loading"></a>`process_weights_after_loading(self, act_dtype: torch.dtype)` — [`L187`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/attn_intra_chip.py#L187)
  - <a id="VllmDeepseekV4MLAAttentionIntraChip.n_local_groups"></a>`n_local_groups` — [`L192`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/attn_intra_chip.py#L192)
  - <a id="VllmDeepseekV4MLAAttentionIntraChip.n_local_heads"></a>`n_local_heads` — [`L192`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/attn_intra_chip.py#L192)
  - <a id="VllmDeepseekV4MLAAttentionIntraChip.wo_a"></a>`wo_a` — [`L153`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/attn_intra_chip.py#L153)
  - <a id="VllmDeepseekV4MLAAttentionIntraChip.wo_b"></a>`wo_b` — [`L170`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/attn_intra_chip.py#L170) — documented in [deepseek-v4-model](../../../../../../concepts/deepseek-v4-model.md)
  - <a id="VllmDeepseekV4MLAAttentionIntraChip.wq_b"></a>`wq_b` — [`L143`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/attn_intra_chip.py#L143)
- protocol/private: <a id="VllmDeepseekV4MLAAttentionIntraChip.__init__"></a>`__init__`[`L112`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/attn_intra_chip.py#L112), <a id="VllmDeepseekV4MLAAttentionIntraChip._chip_pair"></a>`_chip_pair`[`L110`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/attn_intra_chip.py#L110), <a id="VllmDeepseekV4MLAAttentionIntraChip._o_proj"></a>`_o_proj`[`L217`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/attn_intra_chip.py#L217), <a id="VllmDeepseekV4MLAAttentionIntraChip._project_q"></a>`_project_q`[`L198`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/attn_intra_chip.py#L198)
- uses (calls/refs, reference-scoped): [`mla_attn`](attention.md#VllmDeepseekV4MLAAttention.mla_attn), [`o_proj_op`](attention.md#VllmDeepseekV4MLAAttention.o_proj_op), [`__init__`](attention.md#VllmDeepseekV4MLAAttention.__init__), [`get_dp_size`](../../../utils.md#get_dp_size), [`VllmDeepseekV4MLAAttention`](attention.md#VllmDeepseekV4MLAAttention), [`process_weights_after_loading`](attention.md#VllmDeepseekV4MLAAttention.process_weights_after_loading), [`_chip_pair_group`](attn_intra_chip.md#_chip_pair_group), [`logger`](attn_intra_chip.md#logger), [`_swap_with_peer_chiplet`](attn_intra_chip.md#_swap_with_peer_chiplet), [`_load_current_chiplet_slice`](attn_intra_chip.md#_load_current_chiplet_slice)
- used by: [`rms_norm_eps`](model.md#DeepseekV4DecoderLayer.rms_norm_eps), [`VllmDeepseekV4MLAAttention`](attention.md#VllmDeepseekV4MLAAttention), [`_o_proj`](attention.md#VllmDeepseekV4MLAAttention._o_proj), [`_project_q`](attention.md#VllmDeepseekV4MLAAttention._project_q), [`process_weights_after_loading`](attention.md#VllmDeepseekV4MLAAttention.process_weights_after_loading)

## Functions
- <a id="_chip_pair_group"></a>`_chip_pair_group()` — [`L64`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/attn_intra_chip.py#L64) — The intra-chip group, which must exist and pair exactly two cores.
- <a id="_load_current_chiplet_slice"></a>`_load_current_chiplet_slice(layer: torch.nn.Module, rank: int, size: int)` — [`L78`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/attn_intra_chip.py#L78) — Make `layer` load slice `rank` of `size` from the full checkpoint tensors.
- <a id="_swap_with_peer_chiplet"></a>`_swap_with_peer_chiplet(group, mine: torch.Tensor, theirs: torch.Tensor)` — [`L96`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/attn_intra_chip.py#L96) — Send `theirs` to the peer core; return what the peer sent us.

## Module values
- <a id="logger"></a>`logger` — [`L61`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/attn_intra_chip.py#L61)

