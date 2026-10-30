---
title: 'Module: torchtitan/models/deepseek_v3/state_dict_adapter.py'
type: catalog
provenance: extracted
module: torchtitan/models/deepseek_v3/state_dict_adapter.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.models.deepseek_v3.state_dict_adapter`/DeepSeekV3StateDictAdapter#
symbols:
  DeepSeekV3StateDictAdapter.from_hf: from_hf().
  DeepSeekV3StateDictAdapter.to_hf: to_hf().
  DeepSeekV3StateDictAdapter: ''
  DeepSeekV3StateDictAdapter._map_from_hf_layer_key: _map_from_hf_layer_key().
  DeepSeekV3StateDictAdapter.from_hf_map: from_hf_map.
  DeepSeekV3StateDictAdapter.__init__: __init__().
  DeepSeekV3StateDictAdapter._map_to_hf_layer_key: _map_to_hf_layer_key().
  DeepSeekV3StateDictAdapter.hf_experts_key_fragment: hf_experts_key_fragment.
  DeepSeekV3StateDictAdapter.get_hf_storage_reader: get_hf_storage_reader().
---
# Module: [`torchtitan/models/deepseek_v3/state_dict_adapter.py`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/state_dict_adapter.py)

## Classes
### <a id="DeepSeekV3StateDictAdapter"></a>`DeepSeekV3StateDictAdapter`  ·  implements/extends MoEStateDictAdapter
- def: [`torchtitan/models/deepseek_v3/state_dict_adapter.py:20`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/state_dict_adapter.py#L20) — documented in [deepseek-v3-model](../../../../concepts/deepseek-v3-model.md)
- doc: StateDictAdapter for DeepSeekV3 model.
- signature: `class DeepSeekV3StateDictAdapter(MoEStateDictAdapter):`
- members:
  - <a id="DeepSeekV3StateDictAdapter.from_hf"></a>`from_hf(self, hf_state_dict: dict[str, Any])` — [`L211`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/state_dict_adapter.py#L211) — 1. When loading from HF checkpoint, dequantize the weights from float8 to float32. — documented in [deepseek-v3-model](../../../../concepts/deepseek-v3-model.md)
  - <a id="DeepSeekV3StateDictAdapter.get_hf_storage_reader"></a>`get_hf_storage_reader(self, path: str, from_quantized: bool = False)` — [`L129`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/state_dict_adapter.py#L129) — Override default get_hf_storage_reader function to return QuantizedHFStorageReader.
  - <a id="DeepSeekV3StateDictAdapter.to_hf"></a>`to_hf(self, state_dict: dict[str, Any])` — [`L152`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/state_dict_adapter.py#L152) — 1. Convert between the HF shape and the torchtitan shape. — documented in [deepseek-v3-model](../../../../concepts/deepseek-v3-model.md)
  - <a id="DeepSeekV3StateDictAdapter.from_hf_map"></a>`from_hf_map` — [`L33`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/state_dict_adapter.py#L33) — documented in [deepseek-v3-model](../../../../concepts/deepseek-v3-model.md)
  - <a id="DeepSeekV3StateDictAdapter.hf_experts_key_fragment"></a>`hf_experts_key_fragment` — [`L25`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/state_dict_adapter.py#L25)
- protocol/private: <a id="DeepSeekV3StateDictAdapter.__init__"></a>`__init__`[`L27`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/state_dict_adapter.py#L27), <a id="DeepSeekV3StateDictAdapter._map_from_hf_layer_key"></a>`_map_from_hf_layer_key`[`L81`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/state_dict_adapter.py#L81), <a id="DeepSeekV3StateDictAdapter._map_to_hf_layer_key"></a>`_map_to_hf_layer_key`[`L106`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/state_dict_adapter.py#L106)
- uses (calls/refs, reference-scoped): [`layers`](../common/decoder.md#Decoder.Config.layers), [`ComplexRoPE`](../common/rope.md#ComplexRoPE), [`DeepSeekV3Model`](model.md#DeepSeekV3Model), [`Config`](../common/rope.md#ComplexRoPE.Config), [`Config`](model.md#DeepSeekV3Model.Config), [`MoEStateDictAdapter`](../utils.md#MoEStateDictAdapter), [`from_hf`](../deepseek_v4/state_dict_adapter.md#DeepSeekV4StateDictAdapter.from_hf), [`to_hf`](../deepseek_v4/state_dict_adapter.md#DeepSeekV4StateDictAdapter.to_hf), [`to_hf`](../kimi_k2_7/state_dict_adapter.md#KimiK25StateDictAdapter.to_hf), [`_concatenate_expert_weights_dtensor`](../utils.md#MoEStateDictAdapter._concatenate_expert_weights_dtensor), [`model_config`](../utils.md#MoEStateDictAdapter.model_config), [`__init__`](../utils.md#MoEStateDictAdapter.__init__), [`_get_local_experts_weights`](../utils.md#MoEStateDictAdapter._get_local_experts_weights), [`_validate_hf_rope_config`](../../protocols/state_dict_adapter.md#StateDictAdapter._validate_hf_rope_config), [`from_hf`](../kimi_k2_7/state_dict_adapter.md#KimiK25StateDictAdapter.from_hf), [`local_experts_indices`](../utils.md#MoEStateDictAdapter.local_experts_indices), [`grouped_expert_weight_mesh`](../utils.md#MoEStateDictAdapter.grouped_expert_weight_mesh), [`grouped_expert_weight_placements`](../utils.md#MoEStateDictAdapter.grouped_expert_weight_placements), [`DeepSeekV4StateDictAdapter`](../deepseek_v4/state_dict_adapter.md#DeepSeekV4StateDictAdapter), [`KimiK25StateDictAdapter`](../kimi_k2_7/state_dict_adapter.md#KimiK25StateDictAdapter), [`grouped_expert_weight_shape`](../utils.md#MoEStateDictAdapter.grouped_expert_weight_shape), [`_concatenate_expert_weights`](../utils.md#MoEStateDictAdapter._concatenate_expert_weights), [`_split_experts_weights`](../utils.md#MoEStateDictAdapter._split_experts_weights)
- used by: [`model_registry`](__init__.md#model_registry), [`model_registry`](../../experiments/graph_trainer/deepseek_v3/__init__.md#model_registry), [`to_hf`](../../protocols/state_dict_adapter.md#BaseStateDictAdapter.to_hf), [`from_hf`](../../protocols/state_dict_adapter.md#BaseStateDictAdapter.from_hf), [`MoEStateDictAdapter`](../utils.md#MoEStateDictAdapter), [`from_hf`](../deepseek_v4/state_dict_adapter.md#DeepSeekV4StateDictAdapter.from_hf), [`to_hf`](../deepseek_v4/state_dict_adapter.md#DeepSeekV4StateDictAdapter.to_hf), [`to_hf`](../kimi_k2_7/state_dict_adapter.md#KimiK25StateDictAdapter.to_hf), [`get_hf_storage_reader`](../../protocols/state_dict_adapter.md#StateDictAdapter.get_hf_storage_reader), [`__init__`](../deepseek_v4/state_dict_adapter.md#DeepSeekV4StateDictAdapter.__init__), [`__init__`](../kimi_k2_7/state_dict_adapter.md#KimiK25StateDictAdapter.__init__), [`from_hf`](../kimi_k2_7/state_dict_adapter.md#KimiK25StateDictAdapter.from_hf), [`DeepSeekV4StateDictAdapter`](../deepseek_v4/state_dict_adapter.md#DeepSeekV4StateDictAdapter), [`KimiK25StateDictAdapter`](../kimi_k2_7/state_dict_adapter.md#KimiK25StateDictAdapter)

