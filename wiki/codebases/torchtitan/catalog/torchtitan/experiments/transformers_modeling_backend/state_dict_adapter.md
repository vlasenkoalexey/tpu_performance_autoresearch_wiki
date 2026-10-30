---
title: 'Module: torchtitan/experiments/transformers_modeling_backend/state_dict_adapter.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/transformers_modeling_backend/state_dict_adapter.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.transformers_modeling_backend.state_dict_adapter`/
symbols:
  hf_to_titan_moe_state_dict: hf_to_titan_moe_state_dict().
  titan_to_hf_moe_state_dict: titan_to_hf_moe_state_dict().
  _expert_names: _expert_names().
  HFTransformerStateDictAdapter.__init__: HFTransformerStateDictAdapter#__init__().
  _TITAN_EXPERTS_PREFIX: _TITAN_EXPERTS_PREFIX.
  _build_hf_to_titan_patterns: _build_hf_to_titan_patterns().
  _build_titan_to_hf_patterns: _build_titan_to_hf_patterns().
  HFTransformerStateDictAdapter: HFTransformerStateDictAdapter#
  _TITAN_TO_ORIGINAL_HF_KEY._TITAN_TO_ORIGINAL_HF_KEY: _TITAN_TO_ORIGINAL_HF_KEY._TITAN_TO_ORIGINAL_HF_KEY.
  HFTransformerStateDictAdapter.to_hf: HFTransformerStateDictAdapter#to_hf().
  HFTransformerStateDictAdapter._tie_word_embeddings: HFTransformerStateDictAdapter#_tie_word_embeddings.
  HFTransformerStateDictAdapter.from_hf: HFTransformerStateDictAdapter#from_hf().
---
# Module: [`torchtitan/experiments/transformers_modeling_backend/state_dict_adapter.py`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/state_dict_adapter.py)

## Classes
### <a id="HFTransformerStateDictAdapter"></a>`HFTransformerStateDictAdapter`  ·  implements/extends StateDictAdapter
- def: [`torchtitan/experiments/transformers_modeling_backend/state_dict_adapter.py:52`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/state_dict_adapter.py#L52)
- doc: State dict adapter for HFTransformerModel.
- signature: `class HFTransformerStateDictAdapter(StateDictAdapter):`
- members:
  - <a id="HFTransformerStateDictAdapter.from_hf"></a>`from_hf(self, hf_state_dict: dict[str, Any])` — [`L83`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/state_dict_adapter.py#L83)
  - <a id="HFTransformerStateDictAdapter.to_hf"></a>`to_hf(self, state_dict: dict[str, Any])` — [`L71`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/state_dict_adapter.py#L71)
- protocol/private: <a id="HFTransformerStateDictAdapter.__init__"></a>`__init__`[`L63`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/state_dict_adapter.py#L63), <a id="HFTransformerStateDictAdapter._tie_word_embeddings"></a>`_tie_word_embeddings`[`L69`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/state_dict_adapter.py#L69)
- uses (calls/refs, reference-scoped): [`HFTransformerModel`](model.md#HFTransformerModel), [`StateDictAdapter`](../../protocols/state_dict_adapter.md#StateDictAdapter), [`Config`](model.md#HFTransformerModel.Config), [`__init__`](../../protocols/state_dict_adapter.md#StateDictAdapter.__init__)
- used by: [`model_registry`](__init__.md#model_registry), [`StateDictAdapter`](../../protocols/state_dict_adapter.md#StateDictAdapter), [`to_hf`](../../protocols/state_dict_adapter.md#BaseStateDictAdapter.to_hf), [`from_hf`](../../protocols/state_dict_adapter.md#BaseStateDictAdapter.from_hf)

## Functions
- <a id="_build_hf_to_titan_patterns"></a>`_build_hf_to_titan_patterns()` — [`L105`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/state_dict_adapter.py#L105) — Build regex patterns using actual expert parameter names.
- <a id="_build_titan_to_hf_patterns"></a>`_build_titan_to_hf_patterns()` — [`L137`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/state_dict_adapter.py#L137) — Build reverse regex patterns using actual expert parameter names.
- <a id="_expert_names"></a>`_expert_names()` — [`L93`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/state_dict_adapter.py#L93) — Return ``(gate_name, down_name, up_name)`` for routed expert params.
- <a id="hf_to_titan_moe_state_dict"></a>`hf_to_titan_moe_state_dict(hf_state_dict: dict[str, torch.Tensor])` — [`L171`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/state_dict_adapter.py#L171) — Convert HF MoE state dict keys/values to titan format.
- <a id="titan_to_hf_moe_state_dict"></a>`titan_to_hf_moe_state_dict(titan_state_dict: dict[str, torch.Tensor])` — [`L227`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/state_dict_adapter.py#L227) — Convert titan MoE state dict keys/values to HF format.

## Module values
- <a id="_TITAN_EXPERTS_PREFIX"></a>`_TITAN_EXPERTS_PREFIX` — [`L49`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/state_dict_adapter.py#L49)
- <a id="_TITAN_TO_ORIGINAL_HF_KEY._TITAN_TO_ORIGINAL_HF_KEY"></a>`_TITAN_TO_ORIGINAL_HF_KEY` — [`L41`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/state_dict_adapter.py#L41)

