---
title: 'Module: torchtitan/models/gpt_oss/state_dict_adapter.py'
type: catalog
provenance: extracted
module: torchtitan/models/gpt_oss/state_dict_adapter.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.models.gpt_oss.state_dict_adapter`/GptOssStateDictAdapter#
symbols:
  GptOssStateDictAdapter.from_hf: from_hf().
  GptOssStateDictAdapter.__init__: __init__().
  GptOssStateDictAdapter.to_hf: to_hf().
  GptOssStateDictAdapter: ''
  GptOssStateDictAdapter._expert_bias_templates: _expert_bias_templates.
  GptOssStateDictAdapter.from_hf_map: from_hf_map.
  GptOssStateDictAdapter._EXPERT_BIAS_KEY: _EXPERT_BIAS_KEY.
  GptOssStateDictAdapter.get_hf_storage_reader: get_hf_storage_reader().
---
# Module: [`torchtitan/models/gpt_oss/state_dict_adapter.py`](../../../../../../../raw/code/torchtitan/torchtitan/models/gpt_oss/state_dict_adapter.py)

## Classes
### <a id="GptOssStateDictAdapter"></a>`GptOssStateDictAdapter`  ·  implements/extends MoEStateDictAdapter
- def: [`torchtitan/models/gpt_oss/state_dict_adapter.py:18`](../../../../../../../raw/code/torchtitan/torchtitan/models/gpt_oss/state_dict_adapter.py#L18)
- signature: `class GptOssStateDictAdapter(MoEStateDictAdapter):`
- members:
  - <a id="GptOssStateDictAdapter.from_hf"></a>`from_hf(self, hf_state_dict: dict[str, Any])` — [`L114`](../../../../../../../raw/code/torchtitan/torchtitan/models/gpt_oss/state_dict_adapter.py#L114) — Convert from hf format state dict to tt model state dict. — documented in [gpt-oss-model](../../../../concepts/gpt-oss-model.md)
  - <a id="GptOssStateDictAdapter.get_hf_storage_reader"></a>`get_hf_storage_reader(self, path: str, from_quantized: bool = False)` — [`L55`](../../../../../../../raw/code/torchtitan/torchtitan/models/gpt_oss/state_dict_adapter.py#L55) — Override default get_hf_storage_reader function to return QuantizedHFStorageReader.
  - <a id="GptOssStateDictAdapter.to_hf"></a>`to_hf(self, state_dict: dict[str, Any])` — [`L76`](../../../../../../../raw/code/torchtitan/torchtitan/models/gpt_oss/state_dict_adapter.py#L76) — Convert from a tt model state dict to a hf format state dict. — documented in [gpt-oss-model](../../../../concepts/gpt-oss-model.md)
  - <a id="GptOssStateDictAdapter.from_hf_map"></a>`from_hf_map` — [`L29`](../../../../../../../raw/code/torchtitan/torchtitan/models/gpt_oss/state_dict_adapter.py#L29) — documented in [gpt-oss-model](../../../../concepts/gpt-oss-model.md)
- protocol/private: <a id="GptOssStateDictAdapter._EXPERT_BIAS_KEY"></a>`_EXPERT_BIAS_KEY`[`L19`](../../../../../../../raw/code/torchtitan/torchtitan/models/gpt_oss/state_dict_adapter.py#L19), <a id="GptOssStateDictAdapter.__init__"></a>`__init__`[`L21`](../../../../../../../raw/code/torchtitan/torchtitan/models/gpt_oss/state_dict_adapter.py#L21), <a id="GptOssStateDictAdapter._expert_bias_templates"></a>`_expert_bias_templates`[`L27`](../../../../../../../raw/code/torchtitan/torchtitan/models/gpt_oss/state_dict_adapter.py#L27)
- uses (calls/refs, reference-scoped): [`layers`](../common/decoder.md#Decoder.Config.layers), [`CosSinRoPE`](../common/rope.md#CosSinRoPE), [`Config`](../common/rope.md#CosSinRoPE.Config), [`GptOssModel`](model.md#GptOssModel), [`MoEStateDictAdapter`](../utils.md#MoEStateDictAdapter), [`Config`](model.md#GptOssModel.Config), [`model_config`](../utils.md#MoEStateDictAdapter.model_config), [`__init__`](../utils.md#MoEStateDictAdapter.__init__), [`_validate_hf_rope_config`](../../protocols/state_dict_adapter.md#StateDictAdapter._validate_hf_rope_config)
- used by: [`model_registry`](__init__.md#model_registry), [`to_hf`](../../protocols/state_dict_adapter.md#BaseStateDictAdapter.to_hf), [`from_hf`](../../protocols/state_dict_adapter.md#BaseStateDictAdapter.from_hf), [`MoEStateDictAdapter`](../utils.md#MoEStateDictAdapter), [`get_hf_storage_reader`](../../protocols/state_dict_adapter.md#StateDictAdapter.get_hf_storage_reader)

