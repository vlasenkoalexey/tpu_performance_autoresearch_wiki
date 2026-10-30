---
title: 'Module: torchtitan/models/flux/model/state_dict_adapter.py'
type: catalog
provenance: extracted
module: torchtitan/models/flux/model/state_dict_adapter.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.models.flux.model.state_dict_adapter`/
symbols:
  FluxStateDictAdapter.__init__: FluxStateDictAdapter#__init__().
  FluxStateDictAdapter.to_hf: FluxStateDictAdapter#to_hf().
  FluxStateDictAdapter.from_hf: FluxStateDictAdapter#from_hf().
  FluxStateDictAdapter: FluxStateDictAdapter#
  FluxStateDictAdapter.reverse_combination_plan: FluxStateDictAdapter#reverse_combination_plan.
  FluxStateDictAdapter.combination_plan: FluxStateDictAdapter#combination_plan.
  FluxStateDictAdapter.model_config: FluxStateDictAdapter#model_config.
  FluxStateDictAdapter.from_hf_map_direct: FluxStateDictAdapter#from_hf_map_direct.
  FluxStateDictAdapter._swap_scale_shift: FluxStateDictAdapter#_swap_scale_shift().
  logger: logger.
---
# Module: [`torchtitan/models/flux/model/state_dict_adapter.py`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/state_dict_adapter.py)

## Classes
### <a id="FluxStateDictAdapter"></a>`FluxStateDictAdapter`  ·  implements/extends StateDictAdapter
- def: [`torchtitan/models/flux/model/state_dict_adapter.py:22`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/state_dict_adapter.py#L22)
- doc: State dict adapter for Flux model to convert between HuggingFace safetensors format
- signature: `class FluxStateDictAdapter(StateDictAdapter):`
- members:
  - <a id="FluxStateDictAdapter.from_hf"></a>`from_hf(self, hf_state_dict: dict[str, Any])` — [`L219`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/state_dict_adapter.py#L219) — Convert HuggingFace safetensors state dict to TorchTitan DCP format.
  - <a id="FluxStateDictAdapter.to_hf"></a>`to_hf(self, state_dict: dict[str, Any])` — [`L165`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/state_dict_adapter.py#L165) — Convert TorchTitan DCP state dict to HuggingFace safetensors format.
  - <a id="FluxStateDictAdapter.combination_plan"></a>`combination_plan` — [`L118`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/state_dict_adapter.py#L118)
  - <a id="FluxStateDictAdapter.from_hf_map_direct"></a>`from_hf_map_direct` — [`L70`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/state_dict_adapter.py#L70)
  - <a id="FluxStateDictAdapter.model_config"></a>`model_config` — [`L66`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/state_dict_adapter.py#L66)
  - <a id="FluxStateDictAdapter.reverse_combination_plan"></a>`reverse_combination_plan` — [`L152`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/state_dict_adapter.py#L152)
- protocol/private: <a id="FluxStateDictAdapter.__init__"></a>`__init__`[`L30`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/state_dict_adapter.py#L30), <a id="FluxStateDictAdapter._swap_scale_shift"></a>`_swap_scale_shift`[`L160`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/state_dict_adapter.py#L160)
- uses (calls/refs, reference-scoped): [`StateDictAdapter`](../../../protocols/state_dict_adapter.md#StateDictAdapter), [`fqn_to_index_mapping`](../../../protocols/state_dict_adapter.md#BaseStateDictAdapter.fqn_to_index_mapping), [`FluxModel`](model.md#FluxModel), [`Config`](model.md#FluxModel.Config), [`__init__`](../../../protocols/state_dict_adapter.md#StateDictAdapter.__init__), [`hf_assets_path`](../../../protocols/state_dict_adapter.md#BaseStateDictAdapter.hf_assets_path), [`hidden_size`](model.md#FluxModel.Config.hidden_size), [`logger`](state_dict_adapter.md#logger)
- used by: [`model_registry`](../__init__.md#model_registry), [`StateDictAdapter`](../../../protocols/state_dict_adapter.md#StateDictAdapter), [`to_hf`](../../../protocols/state_dict_adapter.md#BaseStateDictAdapter.to_hf), [`from_hf`](../../../protocols/state_dict_adapter.md#BaseStateDictAdapter.from_hf)

## Module values
- <a id="logger"></a>`logger` — [`L19`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/state_dict_adapter.py#L19)

