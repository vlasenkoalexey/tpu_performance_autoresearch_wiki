---
title: 'Module: torchtitan/models/llama3/state_dict_adapter.py'
type: catalog
provenance: extracted
module: torchtitan/models/llama3/state_dict_adapter.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.models.llama3.state_dict_adapter`/
symbols:
  Llama3StateDictAdapter.from_hf: Llama3StateDictAdapter#from_hf().
  Llama3StateDictAdapter.to_hf: Llama3StateDictAdapter#to_hf().
  Llama3StateDictAdapter: Llama3StateDictAdapter#
  Llama3StateDictAdapter.model_config: Llama3StateDictAdapter#model_config.
  logger: logger.
  Llama3StateDictAdapter.__init__: Llama3StateDictAdapter#__init__().
  Llama3StateDictAdapter.from_hf_map: Llama3StateDictAdapter#from_hf_map.
  Llama3StateDictAdapter._permute: Llama3StateDictAdapter#_permute().
  Llama3StateDictAdapter._reverse_permute: Llama3StateDictAdapter#_reverse_permute().
---
# Module: [`torchtitan/models/llama3/state_dict_adapter.py`](../../../../../../../raw/code/torchtitan/torchtitan/models/llama3/state_dict_adapter.py)

## Classes
### <a id="Llama3StateDictAdapter"></a>`Llama3StateDictAdapter`  ·  implements/extends StateDictAdapter
- def: [`torchtitan/models/llama3/state_dict_adapter.py:18`](../../../../../../../raw/code/torchtitan/torchtitan/models/llama3/state_dict_adapter.py#L18) — documented in [llama3-model](../../../../concepts/llama3-model.md)
- signature: `class Llama3StateDictAdapter(StateDictAdapter):`
- members:
  - <a id="Llama3StateDictAdapter.from_hf"></a>`from_hf(self, hf_state_dict: dict[str, Any])` — [`L113`](../../../../../../../raw/code/torchtitan/torchtitan/models/llama3/state_dict_adapter.py#L113) — documented in [llama3-model](../../../../concepts/llama3-model.md)
  - <a id="Llama3StateDictAdapter.to_hf"></a>`to_hf(self, state_dict: dict[str, Any])` — [`L69`](../../../../../../../raw/code/torchtitan/torchtitan/models/llama3/state_dict_adapter.py#L69) — documented in [llama3-model](../../../../concepts/llama3-model.md)
  - <a id="Llama3StateDictAdapter.from_hf_map"></a>`from_hf_map` — [`L29`](../../../../../../../raw/code/torchtitan/torchtitan/models/llama3/state_dict_adapter.py#L29) — documented in [llama3-model](../../../../concepts/llama3-model.md)
  - <a id="Llama3StateDictAdapter.model_config"></a>`model_config` — [`L26`](../../../../../../../raw/code/torchtitan/torchtitan/models/llama3/state_dict_adapter.py#L26) — documented in [llama3-model](../../../../concepts/llama3-model.md)
- protocol/private: <a id="Llama3StateDictAdapter.__init__"></a>`__init__`[`L19`](../../../../../../../raw/code/torchtitan/torchtitan/models/llama3/state_dict_adapter.py#L19), <a id="Llama3StateDictAdapter._permute"></a>`_permute`[`L46`](../../../../../../../raw/code/torchtitan/torchtitan/models/llama3/state_dict_adapter.py#L46), <a id="Llama3StateDictAdapter._reverse_permute"></a>`_reverse_permute`[`L58`](../../../../../../../raw/code/torchtitan/torchtitan/models/llama3/state_dict_adapter.py#L58)
- uses (calls/refs, reference-scoped): [`layers`](../common/decoder.md#Decoder.Config.layers), [`ComplexRoPE`](../common/rope.md#ComplexRoPE), [`Llama3Model`](model.md#Llama3Model), [`Config`](../common/rope.md#ComplexRoPE.Config), [`StateDictAdapter`](../../protocols/state_dict_adapter.md#StateDictAdapter), [`Config`](model.md#Llama3Model.Config), [`fqn_to_index_mapping`](../../protocols/state_dict_adapter.md#BaseStateDictAdapter.fqn_to_index_mapping), [`enable_weight_tying`](../common/decoder.md#Decoder.Config.enable_weight_tying), [`dim`](model.md#Llama3Model.Config.dim), [`__init__`](../../protocols/state_dict_adapter.md#StateDictAdapter.__init__), [`hf_assets_path`](../../protocols/state_dict_adapter.md#BaseStateDictAdapter.hf_assets_path), [`_validate_hf_rope_config`](../../protocols/state_dict_adapter.md#StateDictAdapter._validate_hf_rope_config)
- used by: [`model_registry`](__init__.md#model_registry), [`model_registry`](../../experiments/graph_trainer/llama3/__init__.md#model_registry), [`model_registry`](../../experiments/torchft/llama3/__init__.md#model_registry), [`StateDictAdapter`](../../protocols/state_dict_adapter.md#StateDictAdapter), [`to_hf`](../../protocols/state_dict_adapter.md#BaseStateDictAdapter.to_hf), [`from_hf`](../../protocols/state_dict_adapter.md#BaseStateDictAdapter.from_hf)  (1 test-only)

## Module values
- <a id="logger"></a>`logger` — [`L11`](../../../../../../../raw/code/torchtitan/torchtitan/models/llama3/state_dict_adapter.py#L11)

