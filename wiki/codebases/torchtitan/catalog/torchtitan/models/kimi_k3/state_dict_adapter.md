---
title: 'Module: torchtitan/models/kimi_k3/state_dict_adapter.py'
type: catalog
provenance: extracted
module: torchtitan/models/kimi_k3/state_dict_adapter.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.models.kimi_k3.state_dict_adapter`/
symbols:
  KimiK3StateDictAdapter.to_hf: KimiK3StateDictAdapter#to_hf().
  KimiK3StateDictAdapter.from_hf: KimiK3StateDictAdapter#from_hf().
  KimiK3StateDictAdapter._map_from_hf_layer_key: KimiK3StateDictAdapter#_map_from_hf_layer_key().
  KimiK3StateDictAdapter.__init__: KimiK3StateDictAdapter#__init__().
  KimiK3StateDictAdapter.kimi_config: KimiK3StateDictAdapter#kimi_config.
  KimiK3StateDictAdapter.from_hf_map: KimiK3StateDictAdapter#from_hf_map.
  KimiK3StateDictAdapter: KimiK3StateDictAdapter#
  KimiK3StateDictAdapter.kda_from_hf_map: KimiK3StateDictAdapter#kda_from_hf_map.
  KimiK3StateDictAdapter.mla_from_hf_map: KimiK3StateDictAdapter#mla_from_hf_map.
  _UNUSED_HF_LAYER_ZERO_ATTN_RES_KEYS: _UNUSED_HF_LAYER_ZERO_ATTN_RES_KEYS.
---
# Module: [`torchtitan/models/kimi_k3/state_dict_adapter.py`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/state_dict_adapter.py)

## Classes
### <a id="KimiK3StateDictAdapter"></a>`KimiK3StateDictAdapter`  ·  implements/extends MoEStateDictAdapter
- def: [`torchtitan/models/kimi_k3/state_dict_adapter.py:26`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/state_dict_adapter.py#L26)
- signature: `class KimiK3StateDictAdapter(MoEStateDictAdapter):`
- members:
  - <a id="KimiK3StateDictAdapter.from_hf"></a>`from_hf(self, hf_state_dict: dict[str, Any])` — [`L267`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/state_dict_adapter.py#L267) — Convert an unquantized HuggingFace state dict to TorchTitan. — documented in [kimi-k3-model](../../../../concepts/kimi-k3-model.md)
  - <a id="KimiK3StateDictAdapter.to_hf"></a>`to_hf(self, state_dict: dict[str, Any])` — [`L136`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/state_dict_adapter.py#L136) — Convert a TorchTitan state dict to unquantized HuggingFace format. — documented in [kimi-k3-model](../../../../concepts/kimi-k3-model.md)
  - <a id="KimiK3StateDictAdapter.from_hf_map"></a>`from_hf_map` — [`L35`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/state_dict_adapter.py#L35)
  - <a id="KimiK3StateDictAdapter.kda_from_hf_map"></a>`kda_from_hf_map` — [`L98`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/state_dict_adapter.py#L98)
  - <a id="KimiK3StateDictAdapter.kimi_config"></a>`kimi_config` — [`L33`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/state_dict_adapter.py#L33)
  - <a id="KimiK3StateDictAdapter.mla_from_hf_map"></a>`mla_from_hf_map` — [`L88`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/state_dict_adapter.py#L88)
- protocol/private: <a id="KimiK3StateDictAdapter.__init__"></a>`__init__`[`L27`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/state_dict_adapter.py#L27), <a id="KimiK3StateDictAdapter._map_from_hf_layer_key"></a>`_map_from_hf_layer_key`[`L119`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/state_dict_adapter.py#L119)
- uses (calls/refs, reference-scoped): [`fqn_to_index_mapping`](../../protocols/state_dict_adapter.md#BaseStateDictAdapter.fqn_to_index_mapping), [`MoEStateDictAdapter`](../utils.md#MoEStateDictAdapter), [`delta_attention`](model.md#KimiK3TransformerBlock.Config.delta_attention), [`KimiK3Model`](model.md#KimiK3Model), [`_concatenate_expert_weights_dtensor`](../utils.md#MoEStateDictAdapter._concatenate_expert_weights_dtensor), [`layers`](model.md#KimiK3Model.Config.layers), [`moe`](model.md#KimiK3TransformerBlock.Config.moe), [`num_experts`](../common/moe.md#MoE.Config.num_experts), [`Config`](model.md#KimiK3Model.Config), [`attention`](model.md#KimiK3TransformerBlock.Config.attention), [`__init__`](../utils.md#MoEStateDictAdapter.__init__), [`vision_encoder`](model.md#KimiK3Model.Config.vision_encoder), [`attention_res_norm`](model.md#KimiK3TransformerBlock.Config.attention_res_norm), [`_get_local_experts_weights`](../utils.md#MoEStateDictAdapter._get_local_experts_weights), [`head_dim`](kda.md#KDA.Config.head_dim), [`num_heads`](kda.md#KDA.Config.num_heads), [`local_experts_indices`](../utils.md#MoEStateDictAdapter.local_experts_indices), [`grouped_expert_weight_mesh`](../utils.md#MoEStateDictAdapter.grouped_expert_weight_mesh), [`grouped_expert_weight_placements`](../utils.md#MoEStateDictAdapter.grouped_expert_weight_placements), [`grouped_expert_weight_shape`](../utils.md#MoEStateDictAdapter.grouped_expert_weight_shape), [`_concatenate_expert_weights`](../utils.md#MoEStateDictAdapter._concatenate_expert_weights), [`_split_experts_weights`](../utils.md#MoEStateDictAdapter._split_experts_weights), [`patch_size`](vision_encoder.md#KimiK3VisionEncoder.Config.patch_size), [`in_channels`](vision_encoder.md#KimiK3VisionEncoder.Config.in_channels), [`_UNUSED_HF_LAYER_ZERO_ATTN_RES_KEYS`](state_dict_adapter.md#_UNUSED_HF_LAYER_ZERO_ATTN_RES_KEYS)
- used by: [`model_registry`](__init__.md#model_registry), [`to_hf`](../../protocols/state_dict_adapter.md#BaseStateDictAdapter.to_hf), [`from_hf`](../../protocols/state_dict_adapter.md#BaseStateDictAdapter.from_hf), [`MoEStateDictAdapter`](../utils.md#MoEStateDictAdapter)

## Module values
- <a id="_UNUSED_HF_LAYER_ZERO_ATTN_RES_KEYS"></a>`_UNUSED_HF_LAYER_ZERO_ATTN_RES_KEYS` — [`L20`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/state_dict_adapter.py#L20)

