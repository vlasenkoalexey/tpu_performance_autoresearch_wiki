---
title: 'Module: torchtitan/experiments/transformers_modeling_backend/tokenizer.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/transformers_modeling_backend/tokenizer.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.transformers_modeling_backend.tokenizer`/
symbols:
  HFBackendTokenizer.__init__: HFBackendTokenizer#__init__().
  HFBackendTokenizer.apply_chat_template: HFBackendTokenizer#apply_chat_template().
  HFBackendTokenizer.Config: HFBackendTokenizer#Config#
  HFBackendTokenizer.eos_token: HFBackendTokenizer#eos_token.
  HFBackendTokenizer: HFBackendTokenizer#
  HFBackendTokenizer.set_chat_template: HFBackendTokenizer#set_chat_template().
  HFBackendTokenizer.encode: HFBackendTokenizer#encode().
  _GENERATION_TAG: _GENERATION_TAG.
---
# Module: [`torchtitan/experiments/transformers_modeling_backend/tokenizer.py`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/tokenizer.py)

## Classes
### <a id="HFBackendTokenizer"></a>`HFBackendTokenizer`  ·  implements/extends HuggingFaceTokenizer
- def: [`torchtitan/experiments/transformers_modeling_backend/tokenizer.py:15`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/tokenizer.py#L15)
- doc: Tokenizer that passes special tokens to chat templates.
- signature: `class HFBackendTokenizer(HuggingFaceTokenizer):`
- members:
  - <a id="HFBackendTokenizer.apply_chat_template"></a>`apply_chat_template(self, messages, **kwargs)` — [`L46`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/tokenizer.py#L46)
  - <a id="HFBackendTokenizer.encode"></a>`encode(self, text: str, **kwargs)` — [`L51`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/tokenizer.py#L51)
  - <a id="HFBackendTokenizer.set_chat_template"></a>`set_chat_template(self, template: str)` — [`L37`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/tokenizer.py#L37)
  - <a id="HFBackendTokenizer.eos_token"></a>`eos_token` — [`L34`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/tokenizer.py#L34)
- protocol/private: <a id="HFBackendTokenizer.__init__"></a>`__init__`[`L27`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/tokenizer.py#L27)
- uses (calls/refs, reference-scoped): [`HuggingFaceTokenizer`](../../components/tokenizer.md#HuggingFaceTokenizer), [`_hf_config`](../../components/tokenizer.md#HuggingFaceTokenizer._hf_config), [`encode`](../../components/tokenizer.md#HuggingFaceTokenizer.encode), [`set_chat_template`](../../components/tokenizer.md#BaseTokenizer.set_chat_template), [`tokenizer`](../../components/tokenizer.md#HuggingFaceTokenizer.tokenizer), [`eos_id`](../../components/tokenizer.md#BaseTokenizer.eos_id), [`apply_chat_template`](../../components/tokenizer.md#BaseTokenizer.apply_chat_template), [`__init__`](../../components/tokenizer.md#HuggingFaceTokenizer.__init__), [`bos_token`](../../components/tokenizer.md#HuggingFaceTokenizer.bos_token), [`_get_token_from_config`](../../components/tokenizer.md#HuggingFaceTokenizer._get_token_from_config), [`_GENERATION_TAG`](tokenizer.md#_GENERATION_TAG)
- used by: [`transformers_modeling_backend_sft_full`](config_registry.md#transformers_modeling_backend_sft_full), [`transformers_modeling_backend_sft_debugmodel`](config_registry.md#transformers_modeling_backend_sft_debugmodel), [`HuggingFaceTokenizer`](../../components/tokenizer.md#HuggingFaceTokenizer), [`encode`](../../components/tokenizer.md#HuggingFaceTokenizer.encode), [`set_chat_template`](../../components/tokenizer.md#BaseTokenizer.set_chat_template), [`apply_chat_template`](../../components/tokenizer.md#BaseTokenizer.apply_chat_template)

### <a id="HFBackendTokenizer.Config"></a>`HFBackendTokenizer.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/transformers_modeling_backend/tokenizer.py:24`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/tokenizer.py#L24)
- signature: `class Config(HuggingFaceTokenizer.Config):`
- uses (calls/refs, reference-scoped): [`HuggingFaceTokenizer`](../../components/tokenizer.md#HuggingFaceTokenizer), [`Config`](../../components/tokenizer.md#HuggingFaceTokenizer.Config)
- used by: [`transformers_modeling_backend_sft_full`](config_registry.md#transformers_modeling_backend_sft_full), [`transformers_modeling_backend_sft_debugmodel`](config_registry.md#transformers_modeling_backend_sft_debugmodel)

## Module values
- <a id="_GENERATION_TAG"></a>`_GENERATION_TAG` — [`L12`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/tokenizer.py#L12)

