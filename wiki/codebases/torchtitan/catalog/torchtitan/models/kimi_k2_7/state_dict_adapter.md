---
title: 'Module: torchtitan/models/kimi_k2_7/state_dict_adapter.py'
type: catalog
provenance: extracted
module: torchtitan/models/kimi_k2_7/state_dict_adapter.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.models.kimi_k2_7.state_dict_adapter`/KimiK25StateDictAdapter#
symbols:
  KimiK25StateDictAdapter.to_hf: to_hf().
  KimiK25StateDictAdapter.vision_encoder: vision_encoder.
  KimiK25StateDictAdapter.__init__: __init__().
  KimiK25StateDictAdapter.from_hf: from_hf().
  KimiK25StateDictAdapter.patch_size: patch_size.
  KimiK25StateDictAdapter.in_channels: in_channels.
  KimiK25StateDictAdapter.vision_from_hf_map: vision_from_hf_map.
  KimiK25StateDictAdapter: ''
---
# Module: [`torchtitan/models/kimi_k2_7/state_dict_adapter.py`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/state_dict_adapter.py)

## Classes
### <a id="KimiK25StateDictAdapter"></a>`KimiK25StateDictAdapter`  ·  implements/extends DeepSeekV3StateDictAdapter
- def: [`torchtitan/models/kimi_k2_7/state_dict_adapter.py:31`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/state_dict_adapter.py#L31)
- signature: `class KimiK25StateDictAdapter(DeepSeekV3StateDictAdapter):`
- members:
  - <a id="KimiK25StateDictAdapter.from_hf"></a>`from_hf(self, hf_state_dict: dict[str, Any])` — [`L79`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/state_dict_adapter.py#L79)
  - <a id="KimiK25StateDictAdapter.to_hf"></a>`to_hf(self, state_dict: dict[str, Any])` — [`L167`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/state_dict_adapter.py#L167) — documented in [kimi-k2-7-model](../../../../concepts/kimi-k2-7-model.md)
  - <a id="KimiK25StateDictAdapter.in_channels"></a>`in_channels` — [`L44`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/state_dict_adapter.py#L44) — documented in [kimi-k2-7-model](../../../../concepts/kimi-k2-7-model.md)
  - <a id="KimiK25StateDictAdapter.patch_size"></a>`patch_size` — [`L43`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/state_dict_adapter.py#L43) — documented in [kimi-k2-7-model](../../../../concepts/kimi-k2-7-model.md)
  - <a id="KimiK25StateDictAdapter.vision_encoder"></a>`vision_encoder` — [`L39`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/state_dict_adapter.py#L39) — documented in [kimi-k2-7-model](../../../../concepts/kimi-k2-7-model.md)
  - <a id="KimiK25StateDictAdapter.vision_from_hf_map"></a>`vision_from_hf_map` — [`L47`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/state_dict_adapter.py#L47)
- protocol/private: <a id="KimiK25StateDictAdapter.__init__"></a>`__init__`[`L32`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/state_dict_adapter.py#L32)
- uses (calls/refs, reference-scoped): [`from_hf`](../deepseek_v3/state_dict_adapter.md#DeepSeekV3StateDictAdapter.from_hf), [`to_hf`](../deepseek_v3/state_dict_adapter.md#DeepSeekV3StateDictAdapter.to_hf), [`fqn_to_index_mapping`](../../protocols/state_dict_adapter.md#BaseStateDictAdapter.fqn_to_index_mapping), [`KimiK25Model`](model.md#KimiK25Model), [`Config`](model.md#KimiK25Model.Config), [`vision_encoder`](model.md#KimiK25Model.Config.vision_encoder), [`DeepSeekV3StateDictAdapter`](../deepseek_v3/state_dict_adapter.md#DeepSeekV3StateDictAdapter), [`__init__`](../deepseek_v3/state_dict_adapter.md#DeepSeekV3StateDictAdapter.__init__), [`in_channels`](vision_encoder.md#KimiK25VisionEncoder.Config.in_channels), [`patch_size`](vision_encoder.md#KimiK25VisionEncoder.Config.patch_size)
- used by: [`model_registry`](__init__.md#model_registry), [`from_hf`](../deepseek_v3/state_dict_adapter.md#DeepSeekV3StateDictAdapter.from_hf), [`to_hf`](../deepseek_v3/state_dict_adapter.md#DeepSeekV3StateDictAdapter.to_hf), [`DeepSeekV3StateDictAdapter`](../deepseek_v3/state_dict_adapter.md#DeepSeekV3StateDictAdapter)

