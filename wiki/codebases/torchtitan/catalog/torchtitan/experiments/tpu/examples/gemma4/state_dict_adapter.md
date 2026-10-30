---
title: 'Module: torchtitan/experiments/tpu/examples/gemma4/state_dict_adapter.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/examples/gemma4/state_dict_adapter.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.examples.gemma4.state_dict_adapter`/
symbols:
  Gemma4StateDictAdapter.__init__: Gemma4StateDictAdapter#__init__().
  Gemma4StateDictAdapter.to_hf: Gemma4StateDictAdapter#to_hf().
  Gemma4StateDictAdapter: Gemma4StateDictAdapter#
  Gemma4StateDictAdapter.from_hf: Gemma4StateDictAdapter#from_hf().
  Gemma4StateDictAdapter.from_hf_map: Gemma4StateDictAdapter#from_hf_map.
  _normalize_hf_key: _normalize_hf_key().
  _IGNORED_HF_PREFIXES: _IGNORED_HF_PREFIXES.
  _single_file_safetensors_keys: _single_file_safetensors_keys().
  Gemma4StateDictAdapter._hf_has_lm_head: Gemma4StateDictAdapter#_hf_has_lm_head.
  Gemma4StateDictAdapter._hf_text_only_layout: Gemma4StateDictAdapter#_hf_text_only_layout.
---
# Module: [`torchtitan/experiments/tpu/examples/gemma4/state_dict_adapter.py`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/state_dict_adapter.py)

## Classes
### <a id="Gemma4StateDictAdapter"></a>`Gemma4StateDictAdapter`  ·  implements/extends StateDictAdapter
- def: [`torchtitan/experiments/tpu/examples/gemma4/state_dict_adapter.py:53`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/state_dict_adapter.py#L53)
- doc: Converts state dicts between TorchTitan Gemma4Model and HuggingFace Gemma4 format.
- signature: `class Gemma4StateDictAdapter(StateDictAdapter):`
- members:
  - <a id="Gemma4StateDictAdapter.from_hf"></a>`from_hf(self, hf_state_dict: dict[str, Any])` — [`L186`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/state_dict_adapter.py#L186) — Convert from a HuggingFace Gemma4 state dict to a TorchTitan state dict.
  - <a id="Gemma4StateDictAdapter.to_hf"></a>`to_hf(self, state_dict: dict[str, Any])` — [`L124`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/state_dict_adapter.py#L124) — Convert from a TorchTitan Gemma4 state dict to a HuggingFace state dict.
  - <a id="Gemma4StateDictAdapter.from_hf_map"></a>`from_hf_map` — [`L92`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/state_dict_adapter.py#L92)
- protocol/private: <a id="Gemma4StateDictAdapter.__init__"></a>`__init__`[`L56`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/state_dict_adapter.py#L56), <a id="Gemma4StateDictAdapter._hf_has_lm_head"></a>`_hf_has_lm_head`[`L85`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/state_dict_adapter.py#L85), <a id="Gemma4StateDictAdapter._hf_text_only_layout"></a>`_hf_text_only_layout`[`L88`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/state_dict_adapter.py#L88)
- uses (calls/refs, reference-scoped): [`layers`](../../../../models/common/decoder.md#Decoder.Config.layers), [`StateDictAdapter`](../../../../protocols/state_dict_adapter.md#StateDictAdapter), [`FusedQKVLinear`](../../../../models/common/attention.md#FusedQKVLinear), [`fqn_to_index_mapping`](../../../../protocols/state_dict_adapter.md#BaseStateDictAdapter.fqn_to_index_mapping), [`Config`](../../../../models/common/attention.md#FusedQKVLinear.Config), [`__init__`](../../../../protocols/state_dict_adapter.md#StateDictAdapter.__init__), [`model_config`](../../../../protocols/state_dict_adapter.md#StateDictAdapter.model_config)  (4 test-only)
- used by: [`StateDictAdapter`](../../../../protocols/state_dict_adapter.md#StateDictAdapter), [`to_hf`](../../../../protocols/state_dict_adapter.md#BaseStateDictAdapter.to_hf), [`from_hf`](../../../../protocols/state_dict_adapter.md#BaseStateDictAdapter.from_hf)  (7 test-only)

## Functions
- <a id="_normalize_hf_key"></a>`_normalize_hf_key(key: str)` — [`L23`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/state_dict_adapter.py#L23) — Normalize text-only HF keys (``model.layers.*``) to ``model.language_model.layers.*``.
- <a id="_single_file_safetensors_keys"></a>`_single_file_safetensors_keys(hf_assets_path: str)` — [`L38`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/state_dict_adapter.py#L38) — Tensor names in a single-file ``model.safetensors``, or None if absent.

## Module values
- <a id="_IGNORED_HF_PREFIXES"></a>`_IGNORED_HF_PREFIXES` — [`L14`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/state_dict_adapter.py#L14)

