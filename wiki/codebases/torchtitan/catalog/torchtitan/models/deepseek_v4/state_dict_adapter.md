---
title: 'Module: torchtitan/models/deepseek_v4/state_dict_adapter.py'
type: catalog
provenance: extracted
module: torchtitan/models/deepseek_v4/state_dict_adapter.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.models.deepseek_v4.state_dict_adapter`/DeepSeekV4StateDictAdapter#
symbols:
  DeepSeekV4StateDictAdapter.from_hf: from_hf().
  DeepSeekV4StateDictAdapter.to_hf: to_hf().
  DeepSeekV4StateDictAdapter.compress_ratios: compress_ratios.
  DeepSeekV4StateDictAdapter._can_delegate_hf_key: _can_delegate_hf_key().
  DeepSeekV4StateDictAdapter.from_hf_map: from_hf_map.
  DeepSeekV4StateDictAdapter.__init__: __init__().
  DeepSeekV4StateDictAdapter.num_main_layers: num_main_layers.
  DeepSeekV4StateDictAdapter: ''
  DeepSeekV4StateDictAdapter._abstract_key: _abstract_key().
  DeepSeekV4StateDictAdapter._can_delegate_titan_key: _can_delegate_titan_key().
  DeepSeekV4StateDictAdapter._first_number: _first_number().
  DeepSeekV4StateDictAdapter.hf_experts_key_fragment: hf_experts_key_fragment.
  DeepSeekV4StateDictAdapter._is_v4_special_titan_key: _is_v4_special_titan_key().
  DeepSeekV4StateDictAdapter._is_v4_special_hf_key: _is_v4_special_hf_key().
---
# Module: [`torchtitan/models/deepseek_v4/state_dict_adapter.py`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/state_dict_adapter.py)

## Classes
### <a id="DeepSeekV4StateDictAdapter"></a>`DeepSeekV4StateDictAdapter`  ·  implements/extends DeepSeekV3StateDictAdapter
- def: [`torchtitan/models/deepseek_v4/state_dict_adapter.py:17`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/state_dict_adapter.py#L17)
- signature: `class DeepSeekV4StateDictAdapter(DeepSeekV3StateDictAdapter):`
- members:
  - <a id="DeepSeekV4StateDictAdapter.from_hf"></a>`from_hf(self, hf_state_dict: dict[str, Any])` — [`L203`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/state_dict_adapter.py#L203) — documented in [deepseek-v4-model](../../../../concepts/deepseek-v4-model.md)
  - <a id="DeepSeekV4StateDictAdapter.to_hf"></a>`to_hf(self, state_dict: dict[str, Any])` — [`L169`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/state_dict_adapter.py#L169) — documented in [deepseek-v4-model](../../../../concepts/deepseek-v4-model.md)
  - <a id="DeepSeekV4StateDictAdapter.compress_ratios"></a>`compress_ratios` — [`L77`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/state_dict_adapter.py#L77)
  - <a id="DeepSeekV4StateDictAdapter.from_hf_map"></a>`from_hf_map` — [`L30`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/state_dict_adapter.py#L30) — documented in [deepseek-v4-model](../../../../concepts/deepseek-v4-model.md)
  - <a id="DeepSeekV4StateDictAdapter.hf_experts_key_fragment"></a>`hf_experts_key_fragment` — [`L18`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/state_dict_adapter.py#L18)
  - <a id="DeepSeekV4StateDictAdapter.num_main_layers"></a>`num_main_layers` — [`L76`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/state_dict_adapter.py#L76)
- protocol/private: <a id="DeepSeekV4StateDictAdapter.__init__"></a>`__init__`[`L20`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/state_dict_adapter.py#L20), <a id="DeepSeekV4StateDictAdapter._abstract_key"></a>`_abstract_key`[`L129`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/state_dict_adapter.py#L129), <a id="DeepSeekV4StateDictAdapter._can_delegate_hf_key"></a>`_can_delegate_hf_key`[`L161`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/state_dict_adapter.py#L161), <a id="DeepSeekV4StateDictAdapter._can_delegate_titan_key"></a>`_can_delegate_titan_key`[`L147`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/state_dict_adapter.py#L147), <a id="DeepSeekV4StateDictAdapter._first_number"></a>`_first_number`[`L133`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/state_dict_adapter.py#L133), <a id="DeepSeekV4StateDictAdapter._is_v4_special_hf_key"></a>`_is_v4_special_hf_key`[`L144`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/state_dict_adapter.py#L144), <a id="DeepSeekV4StateDictAdapter._is_v4_special_titan_key"></a>`_is_v4_special_titan_key`[`L140`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/state_dict_adapter.py#L140)
- uses (calls/refs, reference-scoped): [`layers`](../common/decoder.md#Decoder.Config.layers), [`from_hf`](../deepseek_v3/state_dict_adapter.md#DeepSeekV3StateDictAdapter.from_hf), [`to_hf`](../deepseek_v3/state_dict_adapter.md#DeepSeekV3StateDictAdapter.to_hf), [`DeepSeekV3StateDictAdapter`](../deepseek_v3/state_dict_adapter.md#DeepSeekV3StateDictAdapter), [`DeepSeekV4Model`](model.md#DeepSeekV4Model), [`Config`](model.md#DeepSeekV4Model.Config), [`_map_from_hf_layer_key`](../deepseek_v3/state_dict_adapter.md#DeepSeekV3StateDictAdapter._map_from_hf_layer_key), [`__init__`](../deepseek_v3/state_dict_adapter.md#DeepSeekV3StateDictAdapter.__init__), [`_map_to_hf_layer_key`](../deepseek_v3/state_dict_adapter.md#DeepSeekV3StateDictAdapter._map_to_hf_layer_key), [`n_layers`](model.md#DeepSeekV4Model.Config.n_layers), [`compress_ratios`](model.md#DeepSeekV4Model.Config.compress_ratios)
- used by: [`model_registry`](__init__.md#model_registry), [`from_hf`](../deepseek_v3/state_dict_adapter.md#DeepSeekV3StateDictAdapter.from_hf), [`to_hf`](../deepseek_v3/state_dict_adapter.md#DeepSeekV3StateDictAdapter.to_hf), [`DeepSeekV3StateDictAdapter`](../deepseek_v3/state_dict_adapter.md#DeepSeekV3StateDictAdapter)

