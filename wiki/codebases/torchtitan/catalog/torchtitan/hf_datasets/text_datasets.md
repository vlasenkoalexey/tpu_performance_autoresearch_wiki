---
title: 'Module: torchtitan/hf_datasets/text_datasets.py'
type: catalog
provenance: extracted
module: torchtitan/hf_datasets/text_datasets.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.hf_datasets.text_datasets`/
symbols:
  DATASETS.DATASETS: DATASETS.DATASETS.
  ChatProcessor._tokenize_sample: ChatProcessor#_tokenize_sample().
  TextProcessor.__call__: TextProcessor#__call__().
  ChatProcessor: ChatProcessor#
  ChatProcessor.Config: ChatProcessor#Config#
  ChatProcessor.__init__: ChatProcessor#__init__().
  TextProcessor.Config: TextProcessor#Config#
  ChatProcessor._eos_id: ChatProcessor#_eos_id.
  ChatProcessor._tokenizer: ChatProcessor#_tokenizer.
  ChatProcessor.Config.messages_fn: ChatProcessor#Config#messages_fn.
  TextProcessor: TextProcessor#
  TextProcessor.__init__: TextProcessor#__init__().
  ChatProcessor.__call__: ChatProcessor#__call__().
  ChatProcessor._max_context_length: ChatProcessor#_max_context_length.
  TextProcessor.Config.text_fn: TextProcessor#Config#text_fn.
  TextProcessor._tokenizer: TextProcessor#_tokenizer.
  TextProcessor._text_fn: TextProcessor#_text_fn.
  ChatProcessor._messages_fn: ChatProcessor#_messages_fn.
  _is_not_none: _is_not_none().
  ChatProcessor._logged_first_sample: ChatProcessor#_logged_first_sample.
  _read_text: _read_text().
  ChatProcessor._validate_messages: ChatProcessor#_validate_messages().
---
# Module: [`torchtitan/hf_datasets/text_datasets.py`](../../../../../../raw/code/torchtitan/torchtitan/hf_datasets/text_datasets.py)

## Classes
### <a id="ChatProcessor"></a>`ChatProcessor`  ·  implements/extends SampleProcessor
- def: [`torchtitan/hf_datasets/text_datasets.py:61`](../../../../../../raw/code/torchtitan/torchtitan/hf_datasets/text_datasets.py#L61) — documented in [hf-datasets](../../../concepts/hf-datasets.md)
- doc: Tokenizes one single-turn chat sample and masks prompt labels.
- signature: `class ChatProcessor(SampleProcessor):`
- members:
  - <a id="ChatProcessor._tokenize_sample"></a>`_tokenize_sample(self, sample: dict[str, Any])` — [`L100`](../../../../../../raw/code/torchtitan/torchtitan/hf_datasets/text_datasets.py#L100) — Tokenize a single-turn sample and mask prompt labels. — documented in [hf-datasets](../../../concepts/hf-datasets.md)
  - <a id="ChatProcessor._validate_messages"></a>`_validate_messages(messages: list[dict[str, str]])` — [`L83`](../../../../../../raw/code/torchtitan/torchtitan/hf_datasets/text_datasets.py#L83) — Validate that messages are a single-turn [user, assistant] pair.
- protocol/private: <a id="ChatProcessor.__call__"></a>`__call__`[`L152`](../../../../../../raw/code/torchtitan/torchtitan/hf_datasets/text_datasets.py#L152), <a id="ChatProcessor.__init__"></a>`__init__`[`L70`](../../../../../../raw/code/torchtitan/torchtitan/hf_datasets/text_datasets.py#L70), <a id="ChatProcessor._eos_id"></a>`_eos_id`[`L77`](../../../../../../raw/code/torchtitan/torchtitan/hf_datasets/text_datasets.py#L77), <a id="ChatProcessor._logged_first_sample"></a>`_logged_first_sample`[`L80`](../../../../../../raw/code/torchtitan/torchtitan/hf_datasets/text_datasets.py#L80), <a id="ChatProcessor._max_context_length"></a>`_max_context_length`[`L78`](../../../../../../raw/code/torchtitan/torchtitan/hf_datasets/text_datasets.py#L78), <a id="ChatProcessor._messages_fn"></a>`_messages_fn`[`L79`](../../../../../../raw/code/torchtitan/torchtitan/hf_datasets/text_datasets.py#L79), <a id="ChatProcessor._tokenizer"></a>`_tokenizer`[`L76`](../../../../../../raw/code/torchtitan/torchtitan/hf_datasets/text_datasets.py#L76)
- uses (calls/refs, reference-scoped): [`logger`](../tools/logging.md#logger), [`IGNORE_INDEX`](../components/loss.md#IGNORE_INDEX), [`DatasetBuildContext`](../components/data/types.md#DatasetBuildContext), [`SampleProcessor`](../components/data/dataset.md#SampleProcessor), [`input_ids`](../components/data/dataset.md#TextSequence.input_ids), [`TextSequence`](../components/data/dataset.md#TextSequence), [`encode`](../components/tokenizer.md#BaseTokenizer.encode), [`eos_id`](../components/tokenizer.md#BaseTokenizer.eos_id), [`max_context_length`](../components/data/types.md#DatasetBuildContext.max_context_length), [`tokenizer`](../components/data/types.md#DatasetBuildContext.tokenizer), [`Config`](text_datasets.md#ChatProcessor.Config), [`labels`](../components/data/dataset.md#TextSequence.labels), [`apply_chat_template`](../components/tokenizer.md#BaseTokenizer.apply_chat_template), [`messages_fn`](text_datasets.md#ChatProcessor.Config.messages_fn)
- used by: [`sft_llama3_8b_metamath`](../experiments/tpu/llama3/config_registry.md#sft_llama3_8b_metamath), [`transformers_modeling_backend_sft_full`](../experiments/transformers_modeling_backend/config_registry.md#transformers_modeling_backend_sft_full), [`sft_debugmodel`](../models/llama3/config_registry.md#sft_debugmodel), [`sft_qwen3_8b_math`](../models/qwen3/config_registry.md#sft_qwen3_8b_math), [`transformers_modeling_backend_sft_debugmodel`](../experiments/transformers_modeling_backend/config_registry.md#transformers_modeling_backend_sft_debugmodel), [`SampleProcessor`](../components/data/dataset.md#SampleProcessor)

### <a id="ChatProcessor.Config"></a>`ChatProcessor.Config`  ·  implements/extends Config
- def: [`torchtitan/hf_datasets/text_datasets.py:65`](../../../../../../raw/code/torchtitan/torchtitan/hf_datasets/text_datasets.py#L65) — documented in [hf-datasets](../../../concepts/hf-datasets.md)
- signature: `class Config(SampleProcessor.Config):`
- members:
  - <a id="ChatProcessor.Config.messages_fn"></a>`messages_fn` — [`L66`](../../../../../../raw/code/torchtitan/torchtitan/hf_datasets/text_datasets.py#L66) — documented in [hf-datasets](../../../concepts/hf-datasets.md)
- uses (calls/refs, reference-scoped): [`SampleProcessor`](../components/data/dataset.md#SampleProcessor), [`Config`](../components/data/dataset.md#SampleProcessor.Config)
- used by: [`sft_llama3_8b_metamath`](../experiments/tpu/llama3/config_registry.md#sft_llama3_8b_metamath), [`transformers_modeling_backend_sft_full`](../experiments/transformers_modeling_backend/config_registry.md#transformers_modeling_backend_sft_full), [`sft_debugmodel`](../models/llama3/config_registry.md#sft_debugmodel), [`sft_qwen3_8b_math`](../models/qwen3/config_registry.md#sft_qwen3_8b_math), [`transformers_modeling_backend_sft_debugmodel`](../experiments/transformers_modeling_backend/config_registry.md#transformers_modeling_backend_sft_debugmodel), [`__init__`](text_datasets.md#ChatProcessor.__init__), [`_messages_fn`](text_datasets.md#ChatProcessor._messages_fn)

### <a id="TextProcessor"></a>`TextProcessor`  ·  implements/extends SampleProcessor
- def: [`torchtitan/hf_datasets/text_datasets.py:32`](../../../../../../raw/code/torchtitan/torchtitan/hf_datasets/text_datasets.py#L32) — documented in [hf-datasets](../../../concepts/hf-datasets.md)
- doc: Tokenizes plain text into next-token input and label pairs.
- signature: `class TextProcessor(SampleProcessor):`
- protocol/private: <a id="TextProcessor.__call__"></a>`__call__`[`L45`](../../../../../../raw/code/torchtitan/torchtitan/hf_datasets/text_datasets.py#L45), <a id="TextProcessor.__init__"></a>`__init__`[`L41`](../../../../../../raw/code/torchtitan/torchtitan/hf_datasets/text_datasets.py#L41), <a id="TextProcessor._text_fn"></a>`_text_fn`[`L43`](../../../../../../raw/code/torchtitan/torchtitan/hf_datasets/text_datasets.py#L43), <a id="TextProcessor._tokenizer"></a>`_tokenizer`[`L42`](../../../../../../raw/code/torchtitan/torchtitan/hf_datasets/text_datasets.py#L42)
- uses (calls/refs, reference-scoped): [`DatasetBuildContext`](../components/data/types.md#DatasetBuildContext), [`SampleProcessor`](../components/data/dataset.md#SampleProcessor), [`input_ids`](../components/data/dataset.md#TextSequence.input_ids), [`TextSequence`](../components/data/dataset.md#TextSequence), [`encode`](../components/tokenizer.md#BaseTokenizer.encode), [`tokenizer`](../components/data/types.md#DatasetBuildContext.tokenizer), [`labels`](../components/data/dataset.md#TextSequence.labels), [`Config`](text_datasets.md#TextProcessor.Config), [`text_fn`](text_datasets.md#TextProcessor.Config.text_fn)
- used by: [`DATASETS`](text_datasets.md#DATASETS.DATASETS), [`SampleProcessor`](../components/data/dataset.md#SampleProcessor)

### <a id="TextProcessor.Config"></a>`TextProcessor.Config`  ·  implements/extends Config
- def: [`torchtitan/hf_datasets/text_datasets.py:36`](../../../../../../raw/code/torchtitan/torchtitan/hf_datasets/text_datasets.py#L36) — documented in [hf-datasets](../../../concepts/hf-datasets.md)
- signature: `class Config(SampleProcessor.Config):`
- members:
  - <a id="TextProcessor.Config.text_fn"></a>`text_fn` — [`L37`](../../../../../../raw/code/torchtitan/torchtitan/hf_datasets/text_datasets.py#L37)
- uses (calls/refs, reference-scoped): [`SampleProcessor`](../components/data/dataset.md#SampleProcessor), [`Config`](../components/data/dataset.md#SampleProcessor.Config), [`_read_text`](text_datasets.md#_read_text)
- used by: [`DATASETS`](text_datasets.md#DATASETS.DATASETS), [`__init__`](text_datasets.md#TextProcessor.__init__), [`_text_fn`](text_datasets.md#TextProcessor._text_fn)

## Functions
- <a id="_is_not_none"></a>`_is_not_none(sample: Any)` — [`L159`](../../../../../../raw/code/torchtitan/torchtitan/hf_datasets/text_datasets.py#L159) — documented in [hf-datasets](../../../concepts/hf-datasets.md)
- <a id="_read_text"></a>`_read_text(sample: dict[str, Any])` — [`L28`](../../../../../../raw/code/torchtitan/torchtitan/hf_datasets/text_datasets.py#L28)

## Module values
- <a id="DATASETS.DATASETS"></a>`DATASETS` — [`L163`](../../../../../../raw/code/torchtitan/torchtitan/hf_datasets/text_datasets.py#L163) — documented in [hf-datasets](../../../concepts/hf-datasets.md)

