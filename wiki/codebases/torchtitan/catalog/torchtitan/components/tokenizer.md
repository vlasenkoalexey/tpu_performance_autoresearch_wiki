---
title: 'Module: torchtitan/components/tokenizer.py'
type: catalog
provenance: extracted
module: torchtitan/components/tokenizer.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.components.tokenizer`/
symbols:
  HuggingFaceTokenizer: HuggingFaceTokenizer#
  MultiModalTokenizer: MultiModalTokenizer#
  HuggingFaceTokenizer._hf_config: HuggingFaceTokenizer#_hf_config.
  MultiModalTokenizer.Config: MultiModalTokenizer#Config#
  BaseTokenizer: BaseTokenizer#
  HuggingFaceTokenizer.encode: HuggingFaceTokenizer#encode().
  HuggingFaceTokenizer.hf_adds_eos: HuggingFaceTokenizer#hf_adds_eos.
  HuggingFaceTokenizer._infer_special_tokens: HuggingFaceTokenizer#_infer_special_tokens().
  BaseTokenizer.set_chat_template: BaseTokenizer#set_chat_template().
  HuggingFaceTokenizer.tokenizer: HuggingFaceTokenizer#tokenizer.
  HuggingFaceTokenizer._process_special_token: HuggingFaceTokenizer#_process_special_token().
  HuggingFaceTokenizer.Config: HuggingFaceTokenizer#Config#
  BaseTokenizer.encode: BaseTokenizer#encode().
  BaseTokenizer.eos_id: BaseTokenizer#eos_id.
  BaseTokenizer.decode: BaseTokenizer#decode().
  HuggingFaceTokenizer.bos_id: HuggingFaceTokenizer#bos_id.
  BaseTokenizer.get_vocab_size: BaseTokenizer#get_vocab_size().
  MultiModalTokenizer.__init__: MultiModalTokenizer#__init__().
  BaseTokenizer.Config: BaseTokenizer#Config#
  BaseTokenizer.apply_chat_template: BaseTokenizer#apply_chat_template().
  HuggingFaceTokenizer.__init__: HuggingFaceTokenizer#__init__().
  HuggingFaceTokenizer.bos_token: HuggingFaceTokenizer#bos_token.
  HuggingFaceTokenizer.vocab_size: HuggingFaceTokenizer#vocab_size().
  HuggingFaceTokenizer.token_to_id: HuggingFaceTokenizer#token_to_id().
  BaseTokenizer.__init__: BaseTokenizer#__init__().
  HuggingFaceTokenizer.eos_token: HuggingFaceTokenizer#eos_token.
  HuggingFaceTokenizer._get_token_from_config: HuggingFaceTokenizer#_get_token_from_config().
  HuggingFaceTokenizer._load_tokenizer_from_path: HuggingFaceTokenizer#_load_tokenizer_from_path().
  HuggingFaceTokenizer.decode: HuggingFaceTokenizer#decode().
  BaseTokenizer._chat_template: BaseTokenizer#_chat_template.
  HuggingFaceTokenizer.get_vocab_size: HuggingFaceTokenizer#get_vocab_size().
  HuggingFaceTokenizer.get_vocab: HuggingFaceTokenizer#get_vocab().
  HuggingFaceTokenizer.id_to_token: HuggingFaceTokenizer#id_to_token().
  HuggingFaceTokenizer.tokenizer_path: HuggingFaceTokenizer#tokenizer_path.
  HuggingFaceTokenizer.default_add_bos: HuggingFaceTokenizer#default_add_bos.
  HuggingFaceTokenizer.default_add_eos: HuggingFaceTokenizer#default_add_eos.
  HuggingFaceTokenizer.hf_adds_bos: HuggingFaceTokenizer#hf_adds_bos.
  MultiModalTokenizer.TOKEN_FIELDS: MultiModalTokenizer#TOKEN_FIELDS.
  BaseTokenizer.raise_exception: BaseTokenizer#raise_exception().
  BaseTokenizer.tojson: BaseTokenizer#tojson().
  BaseTokenizer.strftime_now: BaseTokenizer#strftime_now().
  HuggingFaceTokenizer.CHAT_TEMPLATE_FILE: HuggingFaceTokenizer#CHAT_TEMPLATE_FILE.
  HuggingFaceTokenizer._load_config: HuggingFaceTokenizer#_load_config().
  HuggingFaceTokenizer._infer_should_add_bos_eos: HuggingFaceTokenizer#_infer_should_add_bos_eos().
  MultiModalTokenizer.Config.image_token: MultiModalTokenizer#Config#image_token.
  MultiModalTokenizer.Config.video_token: MultiModalTokenizer#Config#video_token.
  MultiModalTokenizer.Config.vision_start_token: MultiModalTokenizer#Config#vision_start_token.
  MultiModalTokenizer.Config.vision_end_token: MultiModalTokenizer#Config#vision_end_token.
  MultiModalTokenizer.Config.pad_token: MultiModalTokenizer#Config#pad_token.
---
# Module: [`torchtitan/components/tokenizer.py`](../../../../../../raw/code/torchtitan/torchtitan/components/tokenizer.py)

## Classes
### <a id="BaseTokenizer"></a>`BaseTokenizer`  ·  implements/extends ABC, Configurable
- def: [`torchtitan/components/tokenizer.py:19`](../../../../../../raw/code/torchtitan/torchtitan/components/tokenizer.py#L19) — documented in [training-components](../../../concepts/training-components.md)
- signature: `class BaseTokenizer(ABC, Configurable):`
- members:
  - <a id="BaseTokenizer.apply_chat_template"></a>`apply_chat_template(self, messages: list[dict[str, str]], **kwargs)` — [`L80`](../../../../../../raw/code/torchtitan/torchtitan/components/tokenizer.py#L80) — Render messages through the Jinja chat template. Returns formatted text.
  - <a id="BaseTokenizer.decode"></a>`decode(self, *args, **kwargs)` — [`L36`](../../../../../../raw/code/torchtitan/torchtitan/components/tokenizer.py#L36)
  - <a id="BaseTokenizer.encode"></a>`encode(self, *args, **kwargs)` — [`L32`](../../../../../../raw/code/torchtitan/torchtitan/components/tokenizer.py#L32)
  - <a id="BaseTokenizer.get_vocab_size"></a>`get_vocab_size(self)` — [`L40`](../../../../../../raw/code/torchtitan/torchtitan/components/tokenizer.py#L40)
  - <a id="BaseTokenizer.raise_exception"></a>`raise_exception(msg)` — [`L51`](../../../../../../raw/code/torchtitan/torchtitan/components/tokenizer.py#L51)
  - <a id="BaseTokenizer.set_chat_template"></a>`set_chat_template(self, template: str)` — [`L43`](../../../../../../raw/code/torchtitan/torchtitan/components/tokenizer.py#L43) — Compile and store a Jinja chat template.
  - <a id="BaseTokenizer.strftime_now"></a>`strftime_now(fmt)` — [`L65`](../../../../../../raw/code/torchtitan/torchtitan/components/tokenizer.py#L65)
  - <a id="BaseTokenizer.tojson"></a>`tojson(x, ensure_ascii=False, indent=None, separators=None, sort_keys=False)` — [`L54`](../../../../../../raw/code/torchtitan/torchtitan/components/tokenizer.py#L54)
  - <a id="BaseTokenizer.eos_id"></a>`eos_id` — [`L25`](../../../../../../raw/code/torchtitan/torchtitan/components/tokenizer.py#L25)
- protocol/private: <a id="BaseTokenizer.__init__"></a>`__init__`[`L27`](../../../../../../raw/code/torchtitan/torchtitan/components/tokenizer.py#L27), <a id="BaseTokenizer._chat_template"></a>`_chat_template`[`L29`](../../../../../../raw/code/torchtitan/torchtitan/components/tokenizer.py#L29)
- uses (calls/refs, reference-scoped): [`Configurable`](../config/configurable.md#Configurable), [`HuggingFaceTokenizer`](tokenizer.md#HuggingFaceTokenizer), [`encode`](tokenizer.md#HuggingFaceTokenizer.encode), [`FluxTokenizerContainer`](../models/flux/tokenizer.md#FluxTokenizerContainer), [`encode`](../models/flux/tokenizer.md#FluxTestTokenizer.encode), [`encode`](../models/flux/tokenizer.md#FluxTokenizerContainer.encode), [`apply_chat_template`](../experiments/transformers_modeling_backend/tokenizer.md#HFBackendTokenizer.apply_chat_template), [`decode`](../models/flux/tokenizer.md#FluxTokenizerContainer.decode), [`decode`](../models/flux/tokenizer.md#FluxTestTokenizer.decode), [`encode`](../models/flux/tokenizer.md#FluxTokenizer.encode), [`get_vocab_size`](../models/flux/tokenizer.md#FluxTestTokenizer.get_vocab_size), [`get_vocab_size`](../models/flux/tokenizer.md#FluxTokenizerContainer.get_vocab_size), [`set_chat_template`](../experiments/transformers_modeling_backend/tokenizer.md#HFBackendTokenizer.set_chat_template), [`decode`](tokenizer.md#HuggingFaceTokenizer.decode), [`decode`](../models/flux/tokenizer.md#FluxTokenizer.decode), [`get_vocab_size`](tokenizer.md#HuggingFaceTokenizer.get_vocab_size), [`get_vocab_size`](../models/flux/tokenizer.md#FluxTokenizer.get_vocab_size), `globals`, `filters`
- used by: [`Configurable`](../config/configurable.md#Configurable), [`HuggingFaceTokenizer`](tokenizer.md#HuggingFaceTokenizer), [`tokenizer`](../trainer.md#Trainer.Config.tokenizer), [`_hf_config`](tokenizer.md#HuggingFaceTokenizer._hf_config), [`_tokenize_sample`](../hf_datasets/text_datasets.md#ChatProcessor._tokenize_sample), [`encode`](tokenizer.md#HuggingFaceTokenizer.encode), [`hf_adds_eos`](tokenizer.md#HuggingFaceTokenizer.hf_adds_eos), [`_infer_special_tokens`](tokenizer.md#HuggingFaceTokenizer._infer_special_tokens), [`__init__`](validate.md#Validator.__init__), [`_process_special_token`](tokenizer.md#HuggingFaceTokenizer._process_special_token), [`Config`](tokenizer.md#HuggingFaceTokenizer.Config), [`FluxTokenizerContainer`](../models/flux/tokenizer.md#FluxTokenizerContainer), [`__init__`](../models/flux/tokenizer.md#FluxTokenizerContainer.__init__), [`__init__`](../models/flux/validate.md#FluxValidator.__init__), [`__call__`](../hf_datasets/text_datasets.md#TextProcessor.__call__), [`encode`](../models/flux/tokenizer.md#FluxTokenizerContainer.encode), [`tokenizer`](data/types.md#DatasetBuildContext.tokenizer), [`bos_id`](tokenizer.md#HuggingFaceTokenizer.bos_id), [`Config`](../models/flux/tokenizer.md#FluxTokenizerContainer.Config), [`__init__`](../experiments/transformers_modeling_backend/tokenizer.md#HFBackendTokenizer.__init__), [`__init__`](../hf_datasets/text_datasets.md#ChatProcessor.__init__), [`tokenizer`](../trainer.md#Trainer.tokenizer), [`__init__`](data/loader.md#GrainDataLoader.__init__), [`t5_tokenizer`](../models/flux/tokenizer.md#FluxTokenizerContainer.t5_tokenizer), [`apply_chat_template`](../experiments/transformers_modeling_backend/tokenizer.md#HFBackendTokenizer.apply_chat_template), [`decode`](../models/flux/tokenizer.md#FluxTokenizerContainer.decode), [`__init__`](tokenizer.md#HuggingFaceTokenizer.__init__), [`_eos_id`](../hf_datasets/text_datasets.md#ChatProcessor._eos_id), [`eos_token`](../experiments/transformers_modeling_backend/tokenizer.md#HFBackendTokenizer.eos_token), [`get_vocab_size`](../models/flux/tokenizer.md#FluxTokenizerContainer.get_vocab_size), [`set_chat_template`](../experiments/transformers_modeling_backend/tokenizer.md#HFBackendTokenizer.set_chat_template), [`clip_tokenizer`](../models/flux/tokenizer.md#FluxTokenizerContainer.clip_tokenizer), [`FluxTestTokenizer`](../models/flux/tokenizer.md#FluxTestTokenizer), [`FluxTokenizer`](../models/flux/tokenizer.md#FluxTokenizer), [`eos_token_id`](../experiments/rl/renderer.md#RendererTokenizerWrapper.eos_token_id), [`__init__`](../models/flux/tokenizer.md#FluxTokenizer.__init__)  (1 test-only)

### <a id="BaseTokenizer.Config"></a>`BaseTokenizer.Config`  ·  implements/extends Config
- def: [`torchtitan/components/tokenizer.py:21`](../../../../../../raw/code/torchtitan/torchtitan/components/tokenizer.py#L21)
- signature: `class Config(Configurable.Config):`
- uses (calls/refs, reference-scoped): [`Configurable`](../config/configurable.md#Configurable), [`Config`](../config/configurable.md#Configurable.Config)
- used by: [`tokenizer`](../trainer.md#Trainer.Config.tokenizer), [`Config`](tokenizer.md#HuggingFaceTokenizer.Config), [`Config`](../models/flux/tokenizer.md#FluxTokenizerContainer.Config)

### <a id="HuggingFaceTokenizer"></a>`HuggingFaceTokenizer`  ·  implements/extends BaseTokenizer
- def: [`torchtitan/components/tokenizer.py:94`](../../../../../../raw/code/torchtitan/torchtitan/components/tokenizer.py#L94) — documented in [training-components](../../../concepts/training-components.md)
- doc: A tokenizer wrapper that handles BOS/EOS token inference and encoding.
- signature: `class HuggingFaceTokenizer(BaseTokenizer):`
- members:
  - <a id="HuggingFaceTokenizer._get_token_from_config"></a>`_get_token_from_config(self, config: dict[str, Any], key: str)` — [`L263`](../../../../../../raw/code/torchtitan/torchtitan/components/tokenizer.py#L263) — Parse special tokens from config that can be either strings or dicts.
  - <a id="HuggingFaceTokenizer._infer_should_add_bos_eos"></a>`_infer_should_add_bos_eos(self)` — [`L392`](../../../../../../raw/code/torchtitan/torchtitan/components/tokenizer.py#L392) — Determine the default BOS/EOS behavior for ``encode``.
  - <a id="HuggingFaceTokenizer._infer_special_tokens"></a>`_infer_special_tokens(self)` — [`L337`](../../../../../../raw/code/torchtitan/torchtitan/components/tokenizer.py#L337) — Read special tokens from config and add them to the underlying tokenizer.
  - <a id="HuggingFaceTokenizer._load_config"></a>`_load_config(self, config_path: str)` — [`L162`](../../../../../../raw/code/torchtitan/torchtitan/components/tokenizer.py#L162) — Load configuration from JSON file if it exists.
  - <a id="HuggingFaceTokenizer._load_tokenizer_from_path"></a>`_load_tokenizer_from_path(self, tokenizer_path: str)` — [`L169`](../../../../../../raw/code/torchtitan/torchtitan/components/tokenizer.py#L169) — Load tokenizer from various file formats.
  - <a id="HuggingFaceTokenizer._process_special_token"></a>`_process_special_token(self, token_str: str, token_config: dict, token_id: int | None = None)` — [`L279`](../../../../../../raw/code/torchtitan/torchtitan/components/tokenizer.py#L279) — Process a special token and update BOS/EOS attributes if applicable.
  - <a id="HuggingFaceTokenizer.decode"></a>`decode(self, *args, **kwargs)` — [`L455`](../../../../../../raw/code/torchtitan/torchtitan/components/tokenizer.py#L455) — Decode token IDs back to text.
  - <a id="HuggingFaceTokenizer.encode"></a>`encode(self, *args, **kwargs)` — [`L421`](../../../../../../raw/code/torchtitan/torchtitan/components/tokenizer.py#L421) — Encode text into token IDs with BOS/EOS handling.
  - <a id="HuggingFaceTokenizer.get_vocab"></a>`get_vocab(self)` — [`L486`](../../../../../../raw/code/torchtitan/torchtitan/components/tokenizer.py#L486) — Get the vocabulary as a dictionary.
  - <a id="HuggingFaceTokenizer.get_vocab_size"></a>`get_vocab_size(self)` — [`L482`](../../../../../../raw/code/torchtitan/torchtitan/components/tokenizer.py#L482) — Get the vocabulary size.
  - <a id="HuggingFaceTokenizer.id_to_token"></a>`id_to_token(self, token_id: int)` — [`L494`](../../../../../../raw/code/torchtitan/torchtitan/components/tokenizer.py#L494) — Convert ID to token.
  - <a id="HuggingFaceTokenizer.token_to_id"></a>`token_to_id(self, token: str)` — [`L490`](../../../../../../raw/code/torchtitan/torchtitan/components/tokenizer.py#L490) — Convert token to ID.
  - <a id="HuggingFaceTokenizer.vocab_size"></a>`vocab_size(self)` — [`L478`](../../../../../../raw/code/torchtitan/torchtitan/components/tokenizer.py#L478) — Get the vocabulary size.
  - <a id="HuggingFaceTokenizer.CHAT_TEMPLATE_FILE"></a>`CHAT_TEMPLATE_FILE` — [`L111`](../../../../../../raw/code/torchtitan/torchtitan/components/tokenizer.py#L111)
  - <a id="HuggingFaceTokenizer.bos_id"></a>`bos_id` — [`L127`](../../../../../../raw/code/torchtitan/torchtitan/components/tokenizer.py#L127)
  - <a id="HuggingFaceTokenizer.bos_token"></a>`bos_token` — [`L129`](../../../../../../raw/code/torchtitan/torchtitan/components/tokenizer.py#L129)
  - <a id="HuggingFaceTokenizer.default_add_bos"></a>`default_add_bos` — [`L400`](../../../../../../raw/code/torchtitan/torchtitan/components/tokenizer.py#L400)
  - <a id="HuggingFaceTokenizer.default_add_eos"></a>`default_add_eos` — [`L401`](../../../../../../raw/code/torchtitan/torchtitan/components/tokenizer.py#L401)
  - <a id="HuggingFaceTokenizer.eos_token"></a>`eos_token` — [`L130`](../../../../../../raw/code/torchtitan/torchtitan/components/tokenizer.py#L130)
  - <a id="HuggingFaceTokenizer.hf_adds_bos"></a>`hf_adds_bos` — [`L402`](../../../../../../raw/code/torchtitan/torchtitan/components/tokenizer.py#L402)
  - <a id="HuggingFaceTokenizer.hf_adds_eos"></a>`hf_adds_eos` — [`L403`](../../../../../../raw/code/torchtitan/torchtitan/components/tokenizer.py#L403)
  - <a id="HuggingFaceTokenizer.tokenizer"></a>`tokenizer` — [`L133`](../../../../../../raw/code/torchtitan/torchtitan/components/tokenizer.py#L133)
  - <a id="HuggingFaceTokenizer.tokenizer_path"></a>`tokenizer_path` — [`L124`](../../../../../../raw/code/torchtitan/torchtitan/components/tokenizer.py#L124)
- protocol/private: <a id="HuggingFaceTokenizer.__init__"></a>`__init__`[`L117`](../../../../../../raw/code/torchtitan/torchtitan/components/tokenizer.py#L117), <a id="HuggingFaceTokenizer._hf_config"></a>`_hf_config`[`L136`](../../../../../../raw/code/torchtitan/torchtitan/components/tokenizer.py#L136)
- uses (calls/refs, reference-scoped): [`logger`](../tools/logging.md#logger), [`MultiModalTokenizer`](tokenizer.md#MultiModalTokenizer), [`BaseTokenizer`](tokenizer.md#BaseTokenizer), [`set_chat_template`](tokenizer.md#BaseTokenizer.set_chat_template), [`Config`](tokenizer.md#HuggingFaceTokenizer.Config), [`eos_id`](tokenizer.md#BaseTokenizer.eos_id), [`HFBackendTokenizer`](../experiments/transformers_modeling_backend/tokenizer.md#HFBackendTokenizer), [`__init__`](tokenizer.md#BaseTokenizer.__init__), [`encode`](../experiments/transformers_modeling_backend/tokenizer.md#HFBackendTokenizer.encode)
- used by: [`start_trainer`](../experiments/tpu/conformer/train_minimal.md#start_trainer), [`conformer_test`](../experiments/tpu/conformer/config_registry.md#conformer_test), [`model_config`](../experiments/tpu/train_minimal.md#TrainerMinimal.model_config), [`tokenizer`](../trainer.md#Trainer.Config.tokenizer), [`MultiModalTokenizer`](tokenizer.md#MultiModalTokenizer), [`setup_async`](../experiments/rl/rollout/rollouter.md#Rollouter.setup_async), [`Config`](tokenizer.md#MultiModalTokenizer.Config), [`BaseTokenizer`](tokenizer.md#BaseTokenizer), [`_process_mm_sample`](../hf_datasets/multimodal/mm_datasets.md#_process_mm_sample), [`setup_async`](../experiments/rl/rollout/rollouter.md#RolloutWorker.setup_async), [`encode`](tokenizer.md#BaseTokenizer.encode), [`tokenizer`](../experiments/tpu/train_minimal.md#TrainerMinimal.tokenizer), [`encode`](../models/flux/tokenizer.md#FluxTestTokenizer.encode), [`setup_async`](../experiments/rl/actors/rollout_worker.md#RolloutWorkerActor.setup_async), [`build`](../experiments/rl/renderer.md#RenderersLibraryConfig.build), [`decode`](tokenizer.md#BaseTokenizer.decode), [`get_vocab_size`](tokenizer.md#BaseTokenizer.get_vocab_size), [`__init__`](tokenizer.md#MultiModalTokenizer.__init__), [`__init__`](../experiments/transformers_modeling_backend/tokenizer.md#HFBackendTokenizer.__init__), [`build`](../experiments/rl/models/muse_glimmer/renderer.md#MuseGlimmerRendererConfig.build), [`build`](../experiments/rl/renderer.md#RendererConfig.build), [`_tokenizer_backend`](../experiments/rl/renderer.md#RendererTokenizerWrapper._tokenizer_backend), [`apply_chat_template`](../experiments/transformers_modeling_backend/tokenizer.md#HFBackendTokenizer.apply_chat_template), [`tiktokenizer`](../models/flux/tokenizer.md#FluxTestTokenizer.tiktokenizer), [`Config`](../experiments/transformers_modeling_backend/tokenizer.md#HFBackendTokenizer.Config), [`tokenizer`](../experiments/rl/controller.md#Controller.Config.tokenizer), [`eos_token`](../experiments/transformers_modeling_backend/tokenizer.md#HFBackendTokenizer.eos_token), [`HFBackendTokenizer`](../experiments/transformers_modeling_backend/tokenizer.md#HFBackendTokenizer), [`decode`](../models/flux/tokenizer.md#FluxTestTokenizer.decode), [`encode`](../experiments/transformers_modeling_backend/tokenizer.md#HFBackendTokenizer.encode), [`get_vocab_size`](../models/flux/tokenizer.md#FluxTestTokenizer.get_vocab_size), [`__init__`](../experiments/rl/renderer.md#RendererTokenizerWrapper.__init__), [`bos_token`](../experiments/rl/renderer.md#RendererTokenizerWrapper.bos_token), [`bos_token_id`](../experiments/rl/renderer.md#RendererTokenizerWrapper.bos_token_id), [`eos_token`](../experiments/rl/renderer.md#RendererTokenizerWrapper.eos_token), [`name_or_path`](../experiments/rl/renderer.md#RendererTokenizerWrapper.name_or_path)  (12 test-only)

### <a id="HuggingFaceTokenizer.Config"></a>`HuggingFaceTokenizer.Config`  ·  implements/extends Config
- def: [`torchtitan/components/tokenizer.py:114`](../../../../../../raw/code/torchtitan/torchtitan/components/tokenizer.py#L114)
- signature: `class Config(BaseTokenizer.Config):`
- uses (calls/refs, reference-scoped): [`BaseTokenizer`](tokenizer.md#BaseTokenizer), [`Config`](tokenizer.md#BaseTokenizer.Config)
- used by: [`conformer_test`](../experiments/tpu/conformer/config_registry.md#conformer_test), [`tokenizer`](../trainer.md#Trainer.Config.tokenizer), [`setup_async`](../experiments/rl/rollout/rollouter.md#Rollouter.setup_async), [`Config`](tokenizer.md#MultiModalTokenizer.Config), [`setup_async`](../experiments/rl/rollout/rollouter.md#RolloutWorker.setup_async), [`setup_async`](../experiments/rl/actors/rollout_worker.md#RolloutWorkerActor.setup_async), [`Config`](../experiments/transformers_modeling_backend/tokenizer.md#HFBackendTokenizer.Config), [`__init__`](tokenizer.md#HuggingFaceTokenizer.__init__), [`tokenizer`](../experiments/rl/controller.md#Controller.Config.tokenizer)  (3 test-only)

### <a id="MultiModalTokenizer"></a>`MultiModalTokenizer`  ·  implements/extends HuggingFaceTokenizer
- def: [`torchtitan/components/tokenizer.py:499`](../../../../../../raw/code/torchtitan/torchtitan/components/tokenizer.py#L499)
- doc: Single source of truth for multimodal special tokens.
- signature: `class MultiModalTokenizer(HuggingFaceTokenizer):`
- members:
  - <a id="MultiModalTokenizer.TOKEN_FIELDS"></a>`TOKEN_FIELDS` — [`L533`](../../../../../../raw/code/torchtitan/torchtitan/components/tokenizer.py#L533)
- protocol/private: <a id="MultiModalTokenizer.__init__"></a>`__init__`[`L535`](../../../../../../raw/code/torchtitan/torchtitan/components/tokenizer.py#L535)
- uses (calls/refs, reference-scoped): [`HuggingFaceTokenizer`](tokenizer.md#HuggingFaceTokenizer), [`Config`](tokenizer.md#MultiModalTokenizer.Config), [`tokenizer`](tokenizer.md#HuggingFaceTokenizer.tokenizer), [`__init__`](tokenizer.md#HuggingFaceTokenizer.__init__)
- used by: [`qwen35_debugmodel_moe`](../models/qwen3_5/config_registry.md#qwen35_debugmodel_moe), [`qwen38_debugmodel_moe`](../models/qwen3_8/config_registry.md#qwen38_debugmodel_moe), [`qwen36_debugmodel_moe`](../models/qwen3_6/config_registry.md#qwen36_debugmodel_moe), [`kimi_k2_5_debugmodel`](../models/kimi_k2_7/config_registry.md#kimi_k2_5_debugmodel), [`qwen35_debugmodel`](../models/qwen3_5/config_registry.md#qwen35_debugmodel), [`qwen38_debugmodel`](../models/qwen3_8/config_registry.md#qwen38_debugmodel), [`muse_glimmer_debugmodel_mm`](../models/muse_glimmer/config_registry.md#muse_glimmer_debugmodel_mm), [`qwen36_debugmodel`](../models/qwen3_6/config_registry.md#qwen36_debugmodel), [`qwen35_122b_a10b`](../models/qwen3_5/config_registry.md#qwen35_122b_a10b), [`qwen35_35b_a3b`](../models/qwen3_5/config_registry.md#qwen35_35b_a3b), [`qwen35_397b_a17b`](../models/qwen3_5/config_registry.md#qwen35_397b_a17b), [`qwen36_35b_a3b`](../models/qwen3_6/config_registry.md#qwen36_35b_a3b), [`kimi_k3_debugmodel`](../models/kimi_k3/config_registry.md#kimi_k3_debugmodel), [`qwen35_27b`](../models/qwen3_5/config_registry.md#qwen35_27b), [`qwen35_9b`](../models/qwen3_5/config_registry.md#qwen35_9b), [`qwen36_27b`](../models/qwen3_6/config_registry.md#qwen36_27b), [`qwen38_27b`](../models/qwen3_8/config_registry.md#qwen38_27b), [`kimi_vl_a3b`](../models/kimi_k2_7/config_registry.md#kimi_vl_a3b), [`qwen35_0_8b`](../models/qwen3_5/config_registry.md#qwen35_0_8b), [`qwen35_2b`](../models/qwen3_5/config_registry.md#qwen35_2b), [`muse_glimmer_30b_mm`](../models/muse_glimmer/config_registry.md#muse_glimmer_30b_mm), [`qwen35_4b`](../models/qwen3_5/config_registry.md#qwen35_4b), [`HuggingFaceTokenizer`](tokenizer.md#HuggingFaceTokenizer), [`__call__`](../hf_datasets/multimodal/mm_collator.md#MultiModalCollator.__call__), [`_process_mm_sample`](../hf_datasets/multimodal/mm_datasets.md#_process_mm_sample), [`tokenizer`](../hf_datasets/multimodal/mm_collator.md#MultiModalCollator.tokenizer), [`_process_cc12_wd_sample`](../hf_datasets/multimodal/mm_datasets.md#_process_cc12_wd_sample), [`_process_obelics_sample`](../hf_datasets/multimodal/mm_datasets.md#_process_obelics_sample)

### <a id="MultiModalTokenizer.Config"></a>`MultiModalTokenizer.Config`  ·  implements/extends Config
- def: [`torchtitan/components/tokenizer.py:516`](../../../../../../raw/code/torchtitan/torchtitan/components/tokenizer.py#L516)
- signature: `class Config(HuggingFaceTokenizer.Config):`
- members:
  - <a id="MultiModalTokenizer.Config.image_token"></a>`image_token` — [`L517`](../../../../../../raw/code/torchtitan/torchtitan/components/tokenizer.py#L517) — ---
  - <a id="MultiModalTokenizer.Config.pad_token"></a>`pad_token` — [`L529`](../../../../../../raw/code/torchtitan/torchtitan/components/tokenizer.py#L529) — ---
  - <a id="MultiModalTokenizer.Config.video_token"></a>`video_token` — [`L520`](../../../../../../raw/code/torchtitan/torchtitan/components/tokenizer.py#L520) — ---
  - <a id="MultiModalTokenizer.Config.vision_end_token"></a>`vision_end_token` — [`L526`](../../../../../../raw/code/torchtitan/torchtitan/components/tokenizer.py#L526) — ---
  - <a id="MultiModalTokenizer.Config.vision_start_token"></a>`vision_start_token` — [`L523`](../../../../../../raw/code/torchtitan/torchtitan/components/tokenizer.py#L523) — ---
- uses (calls/refs, reference-scoped): [`HuggingFaceTokenizer`](tokenizer.md#HuggingFaceTokenizer), [`Config`](tokenizer.md#HuggingFaceTokenizer.Config)
- used by: [`qwen35_debugmodel_moe`](../models/qwen3_5/config_registry.md#qwen35_debugmodel_moe), [`qwen38_debugmodel_moe`](../models/qwen3_8/config_registry.md#qwen38_debugmodel_moe), [`qwen36_debugmodel_moe`](../models/qwen3_6/config_registry.md#qwen36_debugmodel_moe), [`kimi_k2_5_debugmodel`](../models/kimi_k2_7/config_registry.md#kimi_k2_5_debugmodel), [`qwen35_debugmodel`](../models/qwen3_5/config_registry.md#qwen35_debugmodel), [`qwen38_debugmodel`](../models/qwen3_8/config_registry.md#qwen38_debugmodel), [`muse_glimmer_debugmodel_mm`](../models/muse_glimmer/config_registry.md#muse_glimmer_debugmodel_mm), [`qwen36_debugmodel`](../models/qwen3_6/config_registry.md#qwen36_debugmodel), [`qwen35_122b_a10b`](../models/qwen3_5/config_registry.md#qwen35_122b_a10b), [`qwen35_35b_a3b`](../models/qwen3_5/config_registry.md#qwen35_35b_a3b), [`qwen35_397b_a17b`](../models/qwen3_5/config_registry.md#qwen35_397b_a17b), [`qwen36_35b_a3b`](../models/qwen3_6/config_registry.md#qwen36_35b_a3b), [`kimi_k3_debugmodel`](../models/kimi_k3/config_registry.md#kimi_k3_debugmodel), [`qwen35_27b`](../models/qwen3_5/config_registry.md#qwen35_27b), [`qwen35_9b`](../models/qwen3_5/config_registry.md#qwen35_9b), [`qwen36_27b`](../models/qwen3_6/config_registry.md#qwen36_27b), [`qwen38_27b`](../models/qwen3_8/config_registry.md#qwen38_27b), [`kimi_vl_a3b`](../models/kimi_k2_7/config_registry.md#kimi_vl_a3b), [`qwen35_0_8b`](../models/qwen3_5/config_registry.md#qwen35_0_8b), [`qwen35_2b`](../models/qwen3_5/config_registry.md#qwen35_2b), [`muse_glimmer_30b_mm`](../models/muse_glimmer/config_registry.md#muse_glimmer_30b_mm), [`qwen35_4b`](../models/qwen3_5/config_registry.md#qwen35_4b), [`__init__`](tokenizer.md#MultiModalTokenizer.__init__)

