---
title: 'Module: torchtitan/models/qwen3_5/state_dict_adapter.py'
type: catalog
provenance: extracted
module: torchtitan/models/qwen3_5/state_dict_adapter.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.models.qwen3_5.state_dict_adapter`/Qwen35StateDictAdapter#
symbols:
  Qwen35StateDictAdapter.to_hf: to_hf().
  Qwen35StateDictAdapter.from_hf: from_hf().
  Qwen35StateDictAdapter.from_hf_map: from_hf_map.
  Qwen35StateDictAdapter.hf_language_model_prefix: hf_language_model_prefix.
  Qwen35StateDictAdapter: ''
  Qwen35StateDictAdapter.__init__: __init__().
  Qwen35StateDictAdapter.model_config: model_config.
---
# Module: [`torchtitan/models/qwen3_5/state_dict_adapter.py`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/state_dict_adapter.py)

## Classes
### <a id="Qwen35StateDictAdapter"></a>`Qwen35StateDictAdapter`  ·  implements/extends StateDictAdapter
- def: [`torchtitan/models/qwen3_5/state_dict_adapter.py:36`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/state_dict_adapter.py#L36) — documented in [qwen3-5-model](../../../../concepts/qwen3-5-model.md)
- signature: `class Qwen35StateDictAdapter(StateDictAdapter):`
- members:
  - <a id="Qwen35StateDictAdapter.from_hf"></a>`from_hf(self, hf_state_dict: dict[str, Any])` — [`L266`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/state_dict_adapter.py#L266) — Convert HuggingFace Qwen3.5 state dict to torchtitan format.
  - <a id="Qwen35StateDictAdapter.to_hf"></a>`to_hf(self, state_dict: dict[str, Any])` — [`L123`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/state_dict_adapter.py#L123) — Convert torchtitan state dict to HuggingFace Qwen3.5 format.
  - <a id="Qwen35StateDictAdapter.from_hf_map"></a>`from_hf_map` — [`L46`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/state_dict_adapter.py#L46)
  - <a id="Qwen35StateDictAdapter.hf_language_model_prefix"></a>`hf_language_model_prefix` — [`L40`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/state_dict_adapter.py#L40)
  - <a id="Qwen35StateDictAdapter.model_config"></a>`model_config` — [`L39`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/state_dict_adapter.py#L39)
- protocol/private: <a id="Qwen35StateDictAdapter.__init__"></a>`__init__`[`L37`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/state_dict_adapter.py#L37)
- uses (calls/refs, reference-scoped): [`layers`](../common/decoder.md#Decoder.Config.layers), [`StateDictAdapter`](../../protocols/state_dict_adapter.md#StateDictAdapter), [`Qwen35Model`](model.md#Qwen35Model), [`Config`](model.md#Qwen35Model.Config), [`fqn_to_index_mapping`](../../protocols/state_dict_adapter.md#BaseStateDictAdapter.fqn_to_index_mapping), [`vision_encoder`](model.md#Qwen35Model.Config.vision_encoder), [`__init__`](../../protocols/state_dict_adapter.md#StateDictAdapter.__init__), [`patch_size`](vision_encoder.md#Qwen35VisionEncoder.Config.patch_size), [`in_channels`](vision_encoder.md#Qwen35VisionEncoder.Config.in_channels), [`temporal_patch_size`](vision_encoder.md#Qwen35VisionEncoder.Config.temporal_patch_size)
- used by: [`model_registry`](__init__.md#model_registry), [`model_registry`](../qwen3_6/__init__.md#model_registry), [`model_registry`](../qwen3_8/__init__.md#model_registry), [`StateDictAdapter`](../../protocols/state_dict_adapter.md#StateDictAdapter), [`to_hf`](../../protocols/state_dict_adapter.md#BaseStateDictAdapter.to_hf), [`from_hf`](../../protocols/state_dict_adapter.md#BaseStateDictAdapter.from_hf)  (1 test-only)

