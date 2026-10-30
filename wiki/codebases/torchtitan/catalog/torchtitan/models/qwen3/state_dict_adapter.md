---
title: 'Module: torchtitan/models/qwen3/state_dict_adapter.py'
type: catalog
provenance: extracted
module: torchtitan/models/qwen3/state_dict_adapter.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.models.qwen3.state_dict_adapter`/Qwen3StateDictAdapter#
symbols:
  Qwen3StateDictAdapter.to_hf: to_hf().
  Qwen3StateDictAdapter.from_hf: from_hf().
  Qwen3StateDictAdapter: ''
  Qwen3StateDictAdapter.__init__: __init__().
  Qwen3StateDictAdapter.from_hf_map: from_hf_map.
---
# Module: [`torchtitan/models/qwen3/state_dict_adapter.py`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3/state_dict_adapter.py)

## Classes
### <a id="Qwen3StateDictAdapter"></a>`Qwen3StateDictAdapter`  ·  implements/extends MoEStateDictAdapter
- def: [`torchtitan/models/qwen3/state_dict_adapter.py:26`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3/state_dict_adapter.py#L26) — documented in [qwen3-model](../../../../concepts/qwen3-model.md)
- signature: `class Qwen3StateDictAdapter(MoEStateDictAdapter):`
- members:
  - <a id="Qwen3StateDictAdapter.from_hf"></a>`from_hf(self, hf_state_dict: dict[str, Any])` — [`L131`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3/state_dict_adapter.py#L131) — 1. Convert between the HF shape and the torchtitan shape. — documented in [qwen3-model](../../../../concepts/qwen3-model.md)
  - <a id="Qwen3StateDictAdapter.to_hf"></a>`to_hf(self, state_dict: dict[str, Any])` — [`L56`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3/state_dict_adapter.py#L56) — 1. Convert between the HF shape and the torchtitan shape. — documented in [qwen3-model](../../../../concepts/qwen3-model.md)
  - <a id="Qwen3StateDictAdapter.from_hf_map"></a>`from_hf_map` — [`L30`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3/state_dict_adapter.py#L30)
- protocol/private: <a id="Qwen3StateDictAdapter.__init__"></a>`__init__`[`L27`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3/state_dict_adapter.py#L27)
- uses (calls/refs, reference-scoped): [`layers`](../common/decoder.md#Decoder.Config.layers), [`Qwen3Model`](model.md#Qwen3Model), [`CosSinRoPE`](../common/rope.md#CosSinRoPE), [`Config`](model.md#Qwen3Model.Config), [`Config`](../common/rope.md#CosSinRoPE.Config), [`fqn_to_index_mapping`](../../protocols/state_dict_adapter.md#BaseStateDictAdapter.fqn_to_index_mapping), [`MoEStateDictAdapter`](../utils.md#MoEStateDictAdapter), [`enable_weight_tying`](../common/decoder.md#Decoder.Config.enable_weight_tying), [`_concatenate_expert_weights_dtensor`](../utils.md#MoEStateDictAdapter._concatenate_expert_weights_dtensor), [`model_config`](../utils.md#MoEStateDictAdapter.model_config), [`__init__`](../utils.md#MoEStateDictAdapter.__init__), [`_get_local_experts_weights`](../utils.md#MoEStateDictAdapter._get_local_experts_weights), [`_validate_hf_rope_config`](../../protocols/state_dict_adapter.md#StateDictAdapter._validate_hf_rope_config), [`local_experts_indices`](../utils.md#MoEStateDictAdapter.local_experts_indices), [`grouped_expert_weight_mesh`](../utils.md#MoEStateDictAdapter.grouped_expert_weight_mesh), [`grouped_expert_weight_placements`](../utils.md#MoEStateDictAdapter.grouped_expert_weight_placements), [`grouped_expert_weight_shape`](../utils.md#MoEStateDictAdapter.grouped_expert_weight_shape), [`_concatenate_expert_weights`](../utils.md#MoEStateDictAdapter._concatenate_expert_weights), [`_split_experts_weights`](../utils.md#MoEStateDictAdapter._split_experts_weights)
- used by: [`model_registry`](__init__.md#model_registry), [`model_registry`](../../experiments/tpu/qwen3/__init__.md#model_registry), [`model_registry`](../../experiments/graph_trainer/qwen3/__init__.md#model_registry), [`qwen3_moe_testmodel`](../../experiments/tpu/qwen3/config_registry.md#qwen3_moe_testmodel), [`to_hf`](../../protocols/state_dict_adapter.md#BaseStateDictAdapter.to_hf), [`from_hf`](../../protocols/state_dict_adapter.md#BaseStateDictAdapter.from_hf), [`MoEStateDictAdapter`](../utils.md#MoEStateDictAdapter)

