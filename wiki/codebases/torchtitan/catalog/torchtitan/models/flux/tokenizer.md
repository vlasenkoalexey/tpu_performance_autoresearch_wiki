---
title: 'Module: torchtitan/models/flux/tokenizer.py'
type: catalog
provenance: extracted
module: torchtitan/models/flux/tokenizer.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.models.flux.tokenizer`/
symbols:
  FluxTokenizerContainer: FluxTokenizerContainer#
  FluxTokenizerContainer.__init__: FluxTokenizerContainer#__init__().
  FluxTokenizerContainer.encode: FluxTokenizerContainer#encode().
  FluxTestTokenizer.encode: FluxTestTokenizer#encode().
  FluxTokenizerContainer.Config: FluxTokenizerContainer#Config#
  FluxTokenizerContainer.t5_tokenizer: FluxTokenizerContainer#t5_tokenizer.
  FluxTokenizerContainer.decode: FluxTokenizerContainer#decode().
  FluxTestTokenizer.tiktokenizer: FluxTestTokenizer#tiktokenizer.
  FluxTokenizer._tokenizer: FluxTokenizer#_tokenizer.
  FluxTokenizerContainer.Config.t5_tokenizer_path: FluxTokenizerContainer#Config#t5_tokenizer_path.
  FluxTokenizerContainer.Config.clip_tokenizer_path: FluxTokenizerContainer#Config#clip_tokenizer_path.
  FluxTokenizerContainer.Config.max_t5_encoding_len: FluxTokenizerContainer#Config#max_t5_encoding_len.
  FluxTokenizerContainer.get_vocab_size: FluxTokenizerContainer#get_vocab_size().
  FluxTestTokenizer.get_vocab_size: FluxTestTokenizer#get_vocab_size().
  FluxTestTokenizer.decode: FluxTestTokenizer#decode().
  FluxTokenizer.encode: FluxTokenizer#encode().
  FluxTokenizerContainer.clip_tokenizer: FluxTokenizerContainer#clip_tokenizer.
  FluxTokenizer.is_clip: FluxTokenizer#is_clip.
  FluxTestTokenizer: FluxTestTokenizer#
  FluxTokenizer: FluxTokenizer#
  FluxTestTokenizer._max_length: FluxTestTokenizer#_max_length.
  FluxTestTokenizer.pad_id: FluxTestTokenizer#pad_id.
  FluxTestTokenizer._pad_and_chunk_tokens: FluxTestTokenizer#_pad_and_chunk_tokens().
  FluxTokenizer.__init__: FluxTokenizer#__init__().
  FluxTokenizer.get_vocab_size: FluxTokenizer#get_vocab_size().
  FluxTokenizer.decode: FluxTokenizer#decode().
  FluxTokenizerContainer.Config.test_mode: FluxTokenizerContainer#Config#test_mode.
  FluxTokenizer._max_length: FluxTokenizer#_max_length.
  FluxTestTokenizer.__init__: FluxTestTokenizer#__init__().
  FluxTokenizer._n_words: FluxTokenizer#_n_words.
---
# Module: [`torchtitan/models/flux/tokenizer.py`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/tokenizer.py)

## Classes
### <a id="FluxTestTokenizer"></a>`FluxTestTokenizer`
- def: [`torchtitan/models/flux/tokenizer.py:87`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/tokenizer.py#L87)
- members:
  - <a id="FluxTestTokenizer.decode"></a>`decode(self, t: list[int])` — [`L144`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/tokenizer.py#L144) — Decode function. This function will not be called.
  - <a id="FluxTestTokenizer.encode"></a>`encode(self, text: str | list[str])` — [`L117`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/tokenizer.py#L117) — Use TikTokenizer to encode the text into tokens, and then pad and chunk the tokens to max_length.
  - <a id="FluxTestTokenizer.get_vocab_size"></a>`get_vocab_size(self)` — [`L113`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/tokenizer.py#L113)
  - <a id="FluxTestTokenizer.pad_id"></a>`pad_id` — [`L96`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/tokenizer.py#L96)
  - <a id="FluxTestTokenizer.tiktokenizer"></a>`tiktokenizer` — [`L94`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/tokenizer.py#L94)
- protocol/private: <a id="FluxTestTokenizer.__init__"></a>`__init__`[`L93`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/tokenizer.py#L93), <a id="FluxTestTokenizer._max_length"></a>`_max_length`[`L95`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/tokenizer.py#L95), <a id="FluxTestTokenizer._pad_and_chunk_tokens"></a>`_pad_and_chunk_tokens`[`L98`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/tokenizer.py#L98)
- uses (calls/refs, reference-scoped): [`HuggingFaceTokenizer`](../../components/tokenizer.md#HuggingFaceTokenizer), [`BaseTokenizer`](../../components/tokenizer.md#BaseTokenizer), [`encode`](../../components/tokenizer.md#HuggingFaceTokenizer.encode), [`vocab_size`](../../components/tokenizer.md#HuggingFaceTokenizer.vocab_size), [`decode`](../../components/tokenizer.md#HuggingFaceTokenizer.decode)
- used by: [`__init__`](tokenizer.md#FluxTokenizerContainer.__init__), [`encode`](../../components/tokenizer.md#BaseTokenizer.encode), [`decode`](../../components/tokenizer.md#BaseTokenizer.decode), [`get_vocab_size`](../../components/tokenizer.md#BaseTokenizer.get_vocab_size)

### <a id="FluxTokenizer"></a>`FluxTokenizer`
- def: [`torchtitan/models/flux/tokenizer.py:151`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/tokenizer.py#L151)
- members:
  - <a id="FluxTokenizer.decode"></a>`decode(self, t: list[int])` — [`L201`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/tokenizer.py#L201) — Decode function. This function will not be called.
  - <a id="FluxTokenizer.encode"></a>`encode(self, s: str | list[str])` — [`L182`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/tokenizer.py#L182) — Encode the prompt text into tokens.
  - <a id="FluxTokenizer.get_vocab_size"></a>`get_vocab_size(self)` — [`L178`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/tokenizer.py#L178)
  - <a id="FluxTokenizer.is_clip"></a>`is_clip` — [`L165`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/tokenizer.py#L165)
- protocol/private: <a id="FluxTokenizer.__init__"></a>`__init__`[`L160`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/tokenizer.py#L160), <a id="FluxTokenizer._max_length"></a>`_max_length`[`L163`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/tokenizer.py#L163), <a id="FluxTokenizer._n_words"></a>`_n_words`[`L162`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/tokenizer.py#L162), <a id="FluxTokenizer._tokenizer"></a>`_tokenizer`[`L169`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/tokenizer.py#L169)
- uses (calls/refs, reference-scoped): [`BaseTokenizer`](../../components/tokenizer.md#BaseTokenizer), [`__init__`](../../components/tokenizer.md#BaseTokenizer.__init__)
- used by: [`__init__`](tokenizer.md#FluxTokenizerContainer.__init__), [`encode`](../../components/tokenizer.md#BaseTokenizer.encode), [`decode`](../../components/tokenizer.md#BaseTokenizer.decode), [`get_vocab_size`](../../components/tokenizer.md#BaseTokenizer.get_vocab_size)

### <a id="FluxTokenizerContainer"></a>`FluxTokenizerContainer`  ·  implements/extends BaseTokenizer
- def: [`torchtitan/models/flux/tokenizer.py:19`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/tokenizer.py#L19) — documented in [flux-diffusion-model](../../../../concepts/flux-diffusion-model.md)
- doc: Container holding both T5 and CLIP tokenizers for Flux.
- signature: `class FluxTokenizerContainer(BaseTokenizer):`
- members:
  - <a id="FluxTokenizerContainer.decode"></a>`decode(self, tokens: dict[str, list[int]])` — [`L67`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/tokenizer.py#L67) — Decode token IDs using both T5 and CLIP tokenizers.
  - <a id="FluxTokenizerContainer.encode"></a>`encode(self, text: str | list[str])` — [`L52`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/tokenizer.py#L52) — Encode text using both T5 and CLIP tokenizers.
  - <a id="FluxTokenizerContainer.get_vocab_size"></a>`get_vocab_size(self)` — [`L83`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/tokenizer.py#L83)
  - <a id="FluxTokenizerContainer.clip_tokenizer"></a>`clip_tokenizer` — [`L49`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/tokenizer.py#L49)
  - <a id="FluxTokenizerContainer.t5_tokenizer"></a>`t5_tokenizer` — [`L46`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/tokenizer.py#L46)
- protocol/private: <a id="FluxTokenizerContainer.__init__"></a>`__init__`[`L36`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/tokenizer.py#L36)
- uses (calls/refs, reference-scoped): [`BaseTokenizer`](../../components/tokenizer.md#BaseTokenizer), [`encode`](../../components/tokenizer.md#BaseTokenizer.encode), [`decode`](../../components/tokenizer.md#BaseTokenizer.decode), [`Config`](tokenizer.md#FluxTokenizerContainer.Config), [`get_vocab_size`](../../components/tokenizer.md#BaseTokenizer.get_vocab_size), [`__init__`](../../components/tokenizer.md#BaseTokenizer.__init__), [`clip_tokenizer_path`](tokenizer.md#FluxTokenizerContainer.Config.clip_tokenizer_path), [`max_t5_encoding_len`](tokenizer.md#FluxTokenizerContainer.Config.max_t5_encoding_len), [`t5_tokenizer_path`](tokenizer.md#FluxTokenizerContainer.Config.t5_tokenizer_path), [`FluxTestTokenizer`](tokenizer.md#FluxTestTokenizer), [`FluxTokenizer`](tokenizer.md#FluxTokenizer), [`test_mode`](tokenizer.md#FluxTokenizerContainer.Config.test_mode)
- used by: [`flux_debugmodel`](config_registry.md#flux_debugmodel), [`flux_dev`](config_registry.md#flux_dev), [`flux_schnell`](config_registry.md#flux_schnell), [`BaseTokenizer`](../../components/tokenizer.md#BaseTokenizer), [`generate_image`](inference/sampling.md#generate_image), [`all_timesteps`](validate.md#FluxValidator.all_timesteps), [`encode`](../../components/tokenizer.md#BaseTokenizer.encode), [`tokenizer`](trainer.md#FluxTrainer.Config.tokenizer), [`decode`](../../components/tokenizer.md#BaseTokenizer.decode), [`_cc12m_wds_data_processor`](flux_datasets.md#_cc12m_wds_data_processor), [`get_vocab_size`](../../components/tokenizer.md#BaseTokenizer.get_vocab_size), [`__init__`](flux_datasets.md#FluxSampleProcessor.__init__), [`_tokenizer`](flux_datasets.md#FluxSampleProcessor._tokenizer), [`_coco_data_processor`](flux_datasets.md#_coco_data_processor)

### <a id="FluxTokenizerContainer.Config"></a>`FluxTokenizerContainer.Config`  ·  implements/extends Config
- def: [`torchtitan/models/flux/tokenizer.py:28`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/tokenizer.py#L28)
- signature: `class Config(BaseTokenizer.Config):`
- members:
  - <a id="FluxTokenizerContainer.Config.clip_tokenizer_path"></a>`clip_tokenizer_path` — [`L31`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/tokenizer.py#L31) — ---
  - <a id="FluxTokenizerContainer.Config.max_t5_encoding_len"></a>`max_t5_encoding_len` — [`L33`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/tokenizer.py#L33)
  - <a id="FluxTokenizerContainer.Config.t5_tokenizer_path"></a>`t5_tokenizer_path` — [`L29`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/tokenizer.py#L29) — ---
  - <a id="FluxTokenizerContainer.Config.test_mode"></a>`test_mode` — [`L34`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/tokenizer.py#L34)
- uses (calls/refs, reference-scoped): [`BaseTokenizer`](../../components/tokenizer.md#BaseTokenizer), [`Config`](../../components/tokenizer.md#BaseTokenizer.Config)
- used by: [`flux_debugmodel`](config_registry.md#flux_debugmodel), [`flux_dev`](config_registry.md#flux_dev), [`flux_schnell`](config_registry.md#flux_schnell), [`t5_encoder`](trainer.md#FluxTrainer.t5_encoder), [`flux_testmodel`](../../experiments/tpu/flux/config_registry.md#flux_testmodel), [`__init__`](tokenizer.md#FluxTokenizerContainer.__init__), [`tokenizer`](trainer.md#FluxTrainer.Config.tokenizer), [`t5_tokenizer`](tokenizer.md#FluxTokenizerContainer.t5_tokenizer)

