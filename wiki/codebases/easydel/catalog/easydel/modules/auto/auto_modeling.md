---
title: 'Module: easydel/modules/auto/auto_modeling.py'
type: catalog
provenance: extracted
module: easydel/modules/auto/auto_modeling.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.auto.auto_modeling`/
symbols:
  BaseAutoEasyModel: BaseAutoEasyModel#
  BaseAutoEasyState: BaseAutoEasyState#
  BaseAutoEasyModel.from_pretrained: BaseAutoEasyModel#from_pretrained().
  BaseAutoEasyModel.from_config: BaseAutoEasyModel#from_config().
  BaseAutoEasyState.from_pretrained: BaseAutoEasyState#from_pretrained().
  AutoEasyDeLVisionModel: AutoEasyDeLVisionModel#
  AutoEasyDeLModel: AutoEasyDeLModel#
  BaseAutoEasyState.from_config: BaseAutoEasyState#from_config().
  BaseAutoEasyModel._from_easydel_params: BaseAutoEasyModel#_from_easydel_params().
  BaseAutoEasyModel._from_torch_pretrained: BaseAutoEasyModel#_from_torch_pretrained().
  AutoEasyDeLModelForCausalLM: AutoEasyDeLModelForCausalLM#
  BaseAutoEasyModel._is_easydel: BaseAutoEasyModel#_is_easydel().
  AutoEasyDeLModelForSpeechSeq2Seq: AutoEasyDeLModelForSpeechSeq2Seq#
  AutoEasyDeLModelForDiffusionLM: AutoEasyDeLModelForDiffusionLM#
  AutoEasyDeLModelForZeroShotImageClassification: AutoEasyDeLModelForZeroShotImageClassification#
  AutoEasyDeLModelForSeq2SeqLM: AutoEasyDeLModelForSeq2SeqLM#
  AutoEasyDeLModelForImageTextToText: AutoEasyDeLModelForImageTextToText#
  AutoEasyDeLModelForSequenceClassification: AutoEasyDeLModelForSequenceClassification#
  AutoEasyDeLModelForEmbedding: AutoEasyDeLModelForEmbedding#
  AutoEasyDeLAnyToAnyModel: AutoEasyDeLAnyToAnyModel#
  AutoStateAnyToAnyModel: AutoStateAnyToAnyModel#
  BaseAutoEasyModel._from_easydel_params.Base: BaseAutoEasyModel#_from_easydel_params().Base#
  BaseAutoEasyModel._from_torch_pretrained.Base: BaseAutoEasyModel#_from_torch_pretrained().Base#
  BaseAutoEasyModel.model_task: BaseAutoEasyModel#model_task.
  BaseAutoEasyModel._from_easydel_params.Base._model_task: BaseAutoEasyModel#_from_easydel_params().Base#_model_task.
  BaseAutoEasyModel._from_torch_pretrained.Base._model_task: BaseAutoEasyModel#_from_torch_pretrained().Base#_model_task.
  AutoEasyDeLModelForCausalLM.model_task: AutoEasyDeLModelForCausalLM#model_task.
  AutoEasyDeLModelForDiffusionLM.model_task: AutoEasyDeLModelForDiffusionLM#model_task.
  AutoEasyDeLModelForZeroShotImageClassification.model_task: AutoEasyDeLModelForZeroShotImageClassification#model_task.
  AutoEasyDeLModelForSpeechSeq2Seq.model_task: AutoEasyDeLModelForSpeechSeq2Seq#model_task.
  AutoEasyDeLModelForSeq2SeqLM.model_task: AutoEasyDeLModelForSeq2SeqLM#model_task.
  AutoEasyDeLModelForImageTextToText.model_task: AutoEasyDeLModelForImageTextToText#model_task.
  AutoEasyDeLModelForSequenceClassification.model_task: AutoEasyDeLModelForSequenceClassification#model_task.
  AutoEasyDeLModelForEmbedding.model_task: AutoEasyDeLModelForEmbedding#model_task.
  AutoEasyDeLModel.model_task: AutoEasyDeLModel#model_task.
  AutoEasyDeLVisionModel.model_task: AutoEasyDeLVisionModel#model_task.
  AutoEasyDeLAnyToAnyModel.model_task: AutoEasyDeLAnyToAnyModel#model_task.
  BaseAutoEasyState._base: BaseAutoEasyState#_base.
  AutoStateForCausalLM: AutoStateForCausalLM#
  AutoStateForDiffusionLM: AutoStateForDiffusionLM#
  AutoStateForZeroShotImageClassification: AutoStateForZeroShotImageClassification#
  AutoStateForSpeechSeq2Seq: AutoStateForSpeechSeq2Seq#
  AutoStateForSeq2SeqLM: AutoStateForSeq2SeqLM#
  AutoStateForImageTextToText: AutoStateForImageTextToText#
  AutoStateForImageSequenceClassification: AutoStateForImageSequenceClassification#
  AutoStateForEmbedding: AutoStateForEmbedding#
  AutoState: AutoState#
  AutoStateVisionModel: AutoStateVisionModel#
  AutoStateForCausalLM._base: AutoStateForCausalLM#_base.
  AutoStateForDiffusionLM._base: AutoStateForDiffusionLM#_base.
  AutoStateForZeroShotImageClassification._base: AutoStateForZeroShotImageClassification#_base.
  AutoStateForSpeechSeq2Seq._base: AutoStateForSpeechSeq2Seq#_base.
  AutoStateForSeq2SeqLM._base: AutoStateForSeq2SeqLM#_base.
  AutoStateForImageTextToText._base: AutoStateForImageTextToText#_base.
  AutoStateForImageSequenceClassification._base: AutoStateForImageSequenceClassification#_base.
  AutoStateForEmbedding._base: AutoStateForEmbedding#_base.
  AutoState._base: AutoState#_base.
  AutoStateVisionModel._base: AutoStateVisionModel#_base.
  MODEL_INDEX_NAME: MODEL_INDEX_NAME.
  SAFETENSOR_INDEX_NAME: SAFETENSOR_INDEX_NAME.
  AutoStateAnyToAnyModel._base: AutoStateAnyToAnyModel#_base.
---
# Module: [`easydel/modules/auto/auto_modeling.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/auto/auto_modeling.py)

## Classes
### `AutoEasyDeLAnyToAnyModel`  ·  implements/extends BaseAutoEasyModel
- def: [`easydel/modules/auto/auto_modeling.py:808`](../../../../../../../raw/code/EasyDeL/easydel/modules/auto/auto_modeling.py#L808)
- doc: Auto loader for generic models that map arbitrary input modalities to any output type.
- signature: `class AutoEasyDeLAnyToAnyModel(BaseAutoEasyModel):`
- members:
  - `model_task` — [`L811`](../../../../../../../raw/code/EasyDeL/easydel/modules/auto/auto_modeling.py#L811)
- uses (calls/refs, reference-scoped): [`TaskType`](../../infra/factory.md#TaskType), [`BaseAutoEasyModel`](auto_modeling.md#BaseAutoEasyModel), [`ANY_TO_ANY`](../../infra/factory.md#TaskType.ANY_TO_ANY)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`build_model`](../../infra/elarge/builders.md#build_model), [`BaseAutoEasyModel`](auto_modeling.md#BaseAutoEasyModel), [`AutoStateAnyToAnyModel`](auto_modeling.md#AutoStateAnyToAnyModel)

### `AutoEasyDeLModel`  ·  implements/extends BaseAutoEasyModel
- def: [`easydel/modules/auto/auto_modeling.py:770`](../../../../../../../raw/code/EasyDeL/easydel/modules/auto/auto_modeling.py#L770)
- doc: This class provides a convenient way to load and shard pretrained  models from the Hugging Face Hub
- signature: `class AutoEasyDeLModel(BaseAutoEasyModel):`
- members:
  - `model_task` — [`L780`](../../../../../../../raw/code/EasyDeL/easydel/modules/auto/auto_modeling.py#L780)
- uses (calls/refs, reference-scoped): [`TaskType`](../../infra/factory.md#TaskType), [`BASE_MODULE`](../../infra/factory.md#TaskType.BASE_MODULE), [`BaseAutoEasyModel`](auto_modeling.md#BaseAutoEasyModel)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`build_model`](../../infra/elarge/builders.md#build_model), [`BaseAutoEasyModel`](auto_modeling.md#BaseAutoEasyModel), [`language_model`](../aya_vision/modeling_aya_vision.md#AyaVisionModel.language_model), [`language_model`](../llava/modeling_llava.md#LlavaModel.language_model), [`language_model`](../mistral3/modeling_mistral3.md#Mistral3Model.language_model), [`_base`](auto_modeling.md#AutoState._base)

### `AutoEasyDeLModelForCausalLM`  ·  implements/extends BaseAutoEasyModel
- def: [`easydel/modules/auto/auto_modeling.py:569`](../../../../../../../raw/code/EasyDeL/easydel/modules/auto/auto_modeling.py#L569)
- doc: This class provides a convenient way to load and shard pretrained  models from the Hugging Face Hub
- signature: `class AutoEasyDeLModelForCausalLM(BaseAutoEasyModel):`
- members:
  - `model_task` — [`L603`](../../../../../../../raw/code/EasyDeL/easydel/modules/auto/auto_modeling.py#L603)
- uses (calls/refs, reference-scoped): [`TaskType`](../../infra/factory.md#TaskType), [`CAUSAL_LM`](../../infra/factory.md#TaskType.CAUSAL_LM), [`BaseAutoEasyModel`](auto_modeling.md#BaseAutoEasyModel)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`_worker_startup_timeout`](../../inference/esurge/esurge_engine.md#eSurge._worker_startup_timeout), [`build_model`](../../infra/elarge/builders.md#build_model), [`BaseAutoEasyModel`](auto_modeling.md#BaseAutoEasyModel), [`__init__`](../../inference/esurge/esurge_engine.md#eSurge.__init__), [`_base`](auto_modeling.md#AutoStateForCausalLM._base)

### `AutoEasyDeLModelForDiffusionLM`  ·  implements/extends BaseAutoEasyModel
- def: [`easydel/modules/auto/auto_modeling.py:612`](../../../../../../../raw/code/EasyDeL/easydel/modules/auto/auto_modeling.py#L612)
- doc: This class provides a convenient way to load and shard pretrained  models from the Hugging Face Hub
- signature: `class AutoEasyDeLModelForDiffusionLM(BaseAutoEasyModel):`
- members:
  - `model_task` — [`L623`](../../../../../../../raw/code/EasyDeL/easydel/modules/auto/auto_modeling.py#L623)
- uses (calls/refs, reference-scoped): [`TaskType`](../../infra/factory.md#TaskType), [`BaseAutoEasyModel`](auto_modeling.md#BaseAutoEasyModel), [`DIFFUSION_LM`](../../infra/factory.md#TaskType.DIFFUSION_LM)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`build_model`](../../infra/elarge/builders.md#build_model), [`BaseAutoEasyModel`](auto_modeling.md#BaseAutoEasyModel), [`_base`](auto_modeling.md#AutoStateForDiffusionLM._base)

### `AutoEasyDeLModelForEmbedding`  ·  implements/extends BaseAutoEasyModel
- def: [`easydel/modules/auto/auto_modeling.py:753`](../../../../../../../raw/code/EasyDeL/easydel/modules/auto/auto_modeling.py#L753)
- doc: Auto loader for embedding models that produce dense vector representations.
- signature: `class AutoEasyDeLModelForEmbedding(BaseAutoEasyModel):`
- members:
  - `model_task` — [`L761`](../../../../../../../raw/code/EasyDeL/easydel/modules/auto/auto_modeling.py#L761)
- uses (calls/refs, reference-scoped): [`TaskType`](../../infra/factory.md#TaskType), [`BaseAutoEasyModel`](auto_modeling.md#BaseAutoEasyModel), [`EMBEDDING`](../../infra/factory.md#TaskType.EMBEDDING)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`build_model`](../../infra/elarge/builders.md#build_model), [`BaseAutoEasyModel`](auto_modeling.md#BaseAutoEasyModel), [`_base`](auto_modeling.md#AutoStateForEmbedding._base)

### `AutoEasyDeLModelForImageTextToText`  ·  implements/extends BaseAutoEasyModel
- def: [`easydel/modules/auto/auto_modeling.py:715`](../../../../../../../raw/code/EasyDeL/easydel/modules/auto/auto_modeling.py#L715)
- doc: This class provides a convenient way to load and shard pretrained  models from the Hugging Face Hub
- signature: `class AutoEasyDeLModelForImageTextToText(BaseAutoEasyModel):`
- members:
  - `model_task` — [`L725`](../../../../../../../raw/code/EasyDeL/easydel/modules/auto/auto_modeling.py#L725)
- uses (calls/refs, reference-scoped): [`TaskType`](../../infra/factory.md#TaskType), [`BaseAutoEasyModel`](auto_modeling.md#BaseAutoEasyModel), [`IMAGE_TEXT_TO_TEXT`](../../infra/factory.md#TaskType.IMAGE_TEXT_TO_TEXT)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`build_model`](../../infra/elarge/builders.md#build_model), [`BaseAutoEasyModel`](auto_modeling.md#BaseAutoEasyModel), [`_base`](auto_modeling.md#AutoStateForImageTextToText._base)

### `AutoEasyDeLModelForSeq2SeqLM`  ·  implements/extends BaseAutoEasyModel
- def: [`easydel/modules/auto/auto_modeling.py:696`](../../../../../../../raw/code/EasyDeL/easydel/modules/auto/auto_modeling.py#L696)
- doc: This class provides a convenient way to load and shard pretrained  models from the Hugging Face Hub
- signature: `class AutoEasyDeLModelForSeq2SeqLM(BaseAutoEasyModel):`
- members:
  - `model_task` — [`L706`](../../../../../../../raw/code/EasyDeL/easydel/modules/auto/auto_modeling.py#L706)
- uses (calls/refs, reference-scoped): [`TaskType`](../../infra/factory.md#TaskType), [`BaseAutoEasyModel`](auto_modeling.md#BaseAutoEasyModel), [`SEQUENCE_TO_SEQUENCE`](../../infra/factory.md#TaskType.SEQUENCE_TO_SEQUENCE)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`build_model`](../../infra/elarge/builders.md#build_model), [`BaseAutoEasyModel`](auto_modeling.md#BaseAutoEasyModel), [`_base`](auto_modeling.md#AutoStateForSeq2SeqLM._base)

### `AutoEasyDeLModelForSequenceClassification`  ·  implements/extends BaseAutoEasyModel
- def: [`easydel/modules/auto/auto_modeling.py:734`](../../../../../../../raw/code/EasyDeL/easydel/modules/auto/auto_modeling.py#L734)
- doc: This class provides a convenient way to load and shard pretrained  models from the Hugging Face Hub
- signature: `class AutoEasyDeLModelForSequenceClassification(BaseAutoEasyModel):`
- members:
  - `model_task` — [`L744`](../../../../../../../raw/code/EasyDeL/easydel/modules/auto/auto_modeling.py#L744)
- uses (calls/refs, reference-scoped): [`TaskType`](../../infra/factory.md#TaskType), [`SEQUENCE_CLASSIFICATION`](../../infra/factory.md#TaskType.SEQUENCE_CLASSIFICATION), [`BaseAutoEasyModel`](auto_modeling.md#BaseAutoEasyModel)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`build_model`](../../infra/elarge/builders.md#build_model), [`BaseAutoEasyModel`](auto_modeling.md#BaseAutoEasyModel), [`_base`](auto_modeling.md#AutoStateForImageSequenceClassification._base)

### `AutoEasyDeLModelForSpeechSeq2Seq`  ·  implements/extends BaseAutoEasyModel
- def: [`easydel/modules/auto/auto_modeling.py:652`](../../../../../../../raw/code/EasyDeL/easydel/modules/auto/auto_modeling.py#L652)
- doc: This class provides a convenient way to load and shard pretrained  models from the Hugging Face Hub
- signature: `class AutoEasyDeLModelForSpeechSeq2Seq(BaseAutoEasyModel):`
- members:
  - `model_task` — [`L687`](../../../../../../../raw/code/EasyDeL/easydel/modules/auto/auto_modeling.py#L687)
- uses (calls/refs, reference-scoped): [`TaskType`](../../infra/factory.md#TaskType), [`BaseAutoEasyModel`](auto_modeling.md#BaseAutoEasyModel), [`SPEECH_SEQUENCE_TO_SEQUENCE`](../../infra/factory.md#TaskType.SPEECH_SEQUENCE_TO_SEQUENCE)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`build_model`](../../infra/elarge/builders.md#build_model), [`BaseAutoEasyModel`](auto_modeling.md#BaseAutoEasyModel), [`model`](../../inference/vwhisper/server.md#WhisperModel.model), [`_base`](auto_modeling.md#AutoStateForSpeechSeq2Seq._base)

### `AutoEasyDeLModelForZeroShotImageClassification`  ·  implements/extends BaseAutoEasyModel
- def: [`easydel/modules/auto/auto_modeling.py:632`](../../../../../../../raw/code/EasyDeL/easydel/modules/auto/auto_modeling.py#L632)
- doc: This class provides a convenient way to load and shard pretrained  models from the Hugging Face Hub
- signature: `class AutoEasyDeLModelForZeroShotImageClassification(BaseAutoEasyModel):`
- members:
  - `model_task` — [`L643`](../../../../../../../raw/code/EasyDeL/easydel/modules/auto/auto_modeling.py#L643)
- uses (calls/refs, reference-scoped): [`TaskType`](../../infra/factory.md#TaskType), [`BaseAutoEasyModel`](auto_modeling.md#BaseAutoEasyModel), [`ZERO_SHOT_IMAGE_CLASSIFICATION`](../../infra/factory.md#TaskType.ZERO_SHOT_IMAGE_CLASSIFICATION)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`build_model`](../../infra/elarge/builders.md#build_model), [`BaseAutoEasyModel`](auto_modeling.md#BaseAutoEasyModel), [`_base`](auto_modeling.md#AutoStateForZeroShotImageClassification._base)

### `AutoEasyDeLVisionModel`  ·  implements/extends BaseAutoEasyModel
- def: [`easydel/modules/auto/auto_modeling.py:789`](../../../../../../../raw/code/EasyDeL/easydel/modules/auto/auto_modeling.py#L789)
- doc: This class provides a convenient way to load and shard pretrained  models from the Hugging Face Hub
- signature: `class AutoEasyDeLVisionModel(BaseAutoEasyModel):`
- members:
  - `model_task` — [`L799`](../../../../../../../raw/code/EasyDeL/easydel/modules/auto/auto_modeling.py#L799)
- uses (calls/refs, reference-scoped): [`TaskType`](../../infra/factory.md#TaskType), [`BaseAutoEasyModel`](auto_modeling.md#BaseAutoEasyModel), [`BASE_VISION`](../../infra/factory.md#TaskType.BASE_VISION)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`BaseAutoEasyModel`](auto_modeling.md#BaseAutoEasyModel), [`vision_tower`](../gemma4/modeling_gemma4.md#Gemma4Model.vision_tower), [`vision_tower`](../aya_vision/modeling_aya_vision.md#AyaVisionModel.vision_tower), [`vision_tower`](../gemma3/modeling_gemma3.md#Gemma3Model.vision_tower), [`vision_tower`](../llava/modeling_llava.md#LlavaModel.vision_tower), [`vision_tower`](../mistral3/modeling_mistral3.md#Mistral3Model.vision_tower), [`_base`](auto_modeling.md#AutoStateVisionModel._base)

### `AutoState`  ·  implements/extends BaseAutoEasyState
- def: [`easydel/modules/auto/auto_modeling.py:783`](../../../../../../../raw/code/EasyDeL/easydel/modules/auto/auto_modeling.py#L783)
- doc: Loads saved states for generic text-only EasyDeL modules.
- signature: `class AutoState(BaseAutoEasyState):`
- protocol/private: `_base`[`L786`](../../../../../../../raw/code/EasyDeL/easydel/modules/auto/auto_modeling.py#L786)
- uses (calls/refs, reference-scoped): [`BaseAutoEasyState`](auto_modeling.md#BaseAutoEasyState), [`AutoEasyDeLModel`](auto_modeling.md#AutoEasyDeLModel)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`BaseAutoEasyState`](auto_modeling.md#BaseAutoEasyState)

### `AutoStateAnyToAnyModel`  ·  implements/extends BaseAutoEasyModel
- def: [`easydel/modules/auto/auto_modeling.py:814`](../../../../../../../raw/code/EasyDeL/easydel/modules/auto/auto_modeling.py#L814)
- doc: Loads or builds states for the generic any-to-any EasyDeL modules.
- signature: `class AutoStateAnyToAnyModel(BaseAutoEasyModel):`
- protocol/private: `_base`[`L817`](../../../../../../../raw/code/EasyDeL/easydel/modules/auto/auto_modeling.py#L817)
- uses (calls/refs, reference-scoped): [`BaseAutoEasyModel`](auto_modeling.md#BaseAutoEasyModel), [`AutoEasyDeLAnyToAnyModel`](auto_modeling.md#AutoEasyDeLAnyToAnyModel)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`BaseAutoEasyModel`](auto_modeling.md#BaseAutoEasyModel)

### `AutoStateForCausalLM`  ·  implements/extends BaseAutoEasyState
- def: [`easydel/modules/auto/auto_modeling.py:606`](../../../../../../../raw/code/EasyDeL/easydel/modules/auto/auto_modeling.py#L606)
- doc: Loads saved states for causal language modeling tasks.
- signature: `class AutoStateForCausalLM(BaseAutoEasyState):`
- protocol/private: `_base`[`L609`](../../../../../../../raw/code/EasyDeL/easydel/modules/auto/auto_modeling.py#L609)
- uses (calls/refs, reference-scoped): [`BaseAutoEasyState`](auto_modeling.md#BaseAutoEasyState), [`AutoEasyDeLModelForCausalLM`](auto_modeling.md#AutoEasyDeLModelForCausalLM)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`BaseAutoEasyState`](auto_modeling.md#BaseAutoEasyState)

### `AutoStateForDiffusionLM`  ·  implements/extends BaseAutoEasyState
- def: [`easydel/modules/auto/auto_modeling.py:626`](../../../../../../../raw/code/EasyDeL/easydel/modules/auto/auto_modeling.py#L626)
- doc: Loads saved states for diffusion-based language models.
- signature: `class AutoStateForDiffusionLM(BaseAutoEasyState):`
- protocol/private: `_base`[`L629`](../../../../../../../raw/code/EasyDeL/easydel/modules/auto/auto_modeling.py#L629)
- uses (calls/refs, reference-scoped): [`BaseAutoEasyState`](auto_modeling.md#BaseAutoEasyState), [`AutoEasyDeLModelForDiffusionLM`](auto_modeling.md#AutoEasyDeLModelForDiffusionLM)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`BaseAutoEasyState`](auto_modeling.md#BaseAutoEasyState)

### `AutoStateForEmbedding`  ·  implements/extends BaseAutoEasyState
- def: [`easydel/modules/auto/auto_modeling.py:764`](../../../../../../../raw/code/EasyDeL/easydel/modules/auto/auto_modeling.py#L764)
- doc: Loads saved states for embedding models.
- signature: `class AutoStateForEmbedding(BaseAutoEasyState):`
- protocol/private: `_base`[`L767`](../../../../../../../raw/code/EasyDeL/easydel/modules/auto/auto_modeling.py#L767)
- uses (calls/refs, reference-scoped): [`BaseAutoEasyState`](auto_modeling.md#BaseAutoEasyState), [`AutoEasyDeLModelForEmbedding`](auto_modeling.md#AutoEasyDeLModelForEmbedding)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`BaseAutoEasyState`](auto_modeling.md#BaseAutoEasyState)

### `AutoStateForImageSequenceClassification`  ·  implements/extends BaseAutoEasyState
- def: [`easydel/modules/auto/auto_modeling.py:747`](../../../../../../../raw/code/EasyDeL/easydel/modules/auto/auto_modeling.py#L747)
- doc: Loads saved states for image-conditioned sequence classification.
- signature: `class AutoStateForImageSequenceClassification(BaseAutoEasyState):`
- protocol/private: `_base`[`L750`](../../../../../../../raw/code/EasyDeL/easydel/modules/auto/auto_modeling.py#L750)
- uses (calls/refs, reference-scoped): [`BaseAutoEasyState`](auto_modeling.md#BaseAutoEasyState), [`AutoEasyDeLModelForSequenceClassification`](auto_modeling.md#AutoEasyDeLModelForSequenceClassification)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`BaseAutoEasyState`](auto_modeling.md#BaseAutoEasyState)

### `AutoStateForImageTextToText`  ·  implements/extends BaseAutoEasyState
- def: [`easydel/modules/auto/auto_modeling.py:728`](../../../../../../../raw/code/EasyDeL/easydel/modules/auto/auto_modeling.py#L728)
- doc: Loads saved states for image-conditioned text-to-text models.
- signature: `class AutoStateForImageTextToText(BaseAutoEasyState):`
- protocol/private: `_base`[`L731`](../../../../../../../raw/code/EasyDeL/easydel/modules/auto/auto_modeling.py#L731)
- uses (calls/refs, reference-scoped): [`BaseAutoEasyState`](auto_modeling.md#BaseAutoEasyState), [`AutoEasyDeLModelForImageTextToText`](auto_modeling.md#AutoEasyDeLModelForImageTextToText)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`BaseAutoEasyState`](auto_modeling.md#BaseAutoEasyState)

### `AutoStateForSeq2SeqLM`  ·  implements/extends BaseAutoEasyState
- def: [`easydel/modules/auto/auto_modeling.py:709`](../../../../../../../raw/code/EasyDeL/easydel/modules/auto/auto_modeling.py#L709)
- doc: Loads saved states for text-to-text sequence-to-sequence models.
- signature: `class AutoStateForSeq2SeqLM(BaseAutoEasyState):`
- protocol/private: `_base`[`L712`](../../../../../../../raw/code/EasyDeL/easydel/modules/auto/auto_modeling.py#L712)
- uses (calls/refs, reference-scoped): [`BaseAutoEasyState`](auto_modeling.md#BaseAutoEasyState), [`AutoEasyDeLModelForSeq2SeqLM`](auto_modeling.md#AutoEasyDeLModelForSeq2SeqLM)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`BaseAutoEasyState`](auto_modeling.md#BaseAutoEasyState)

### `AutoStateForSpeechSeq2Seq`  ·  implements/extends BaseAutoEasyState
- def: [`easydel/modules/auto/auto_modeling.py:690`](../../../../../../../raw/code/EasyDeL/easydel/modules/auto/auto_modeling.py#L690)
- doc: Loads saved states for speech-to-text sequence-to-sequence models.
- signature: `class AutoStateForSpeechSeq2Seq(BaseAutoEasyState):`
- protocol/private: `_base`[`L693`](../../../../../../../raw/code/EasyDeL/easydel/modules/auto/auto_modeling.py#L693)
- uses (calls/refs, reference-scoped): [`BaseAutoEasyState`](auto_modeling.md#BaseAutoEasyState), [`AutoEasyDeLModelForSpeechSeq2Seq`](auto_modeling.md#AutoEasyDeLModelForSpeechSeq2Seq)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`BaseAutoEasyState`](auto_modeling.md#BaseAutoEasyState)

### `AutoStateForZeroShotImageClassification`  ·  implements/extends BaseAutoEasyState
- def: [`easydel/modules/auto/auto_modeling.py:646`](../../../../../../../raw/code/EasyDeL/easydel/modules/auto/auto_modeling.py#L646)
- doc: Loads saved states for zero-shot image classification models.
- signature: `class AutoStateForZeroShotImageClassification(BaseAutoEasyState):`
- protocol/private: `_base`[`L649`](../../../../../../../raw/code/EasyDeL/easydel/modules/auto/auto_modeling.py#L649)
- uses (calls/refs, reference-scoped): [`BaseAutoEasyState`](auto_modeling.md#BaseAutoEasyState), [`AutoEasyDeLModelForZeroShotImageClassification`](auto_modeling.md#AutoEasyDeLModelForZeroShotImageClassification)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`BaseAutoEasyState`](auto_modeling.md#BaseAutoEasyState)

### `AutoStateVisionModel`  ·  implements/extends BaseAutoEasyState
- def: [`easydel/modules/auto/auto_modeling.py:802`](../../../../../../../raw/code/EasyDeL/easydel/modules/auto/auto_modeling.py#L802)
- doc: Loads saved states for vision-only EasyDeL modules.
- signature: `class AutoStateVisionModel(BaseAutoEasyState):`
- protocol/private: `_base`[`L805`](../../../../../../../raw/code/EasyDeL/easydel/modules/auto/auto_modeling.py#L805)
- uses (calls/refs, reference-scoped): [`BaseAutoEasyState`](auto_modeling.md#BaseAutoEasyState), [`AutoEasyDeLVisionModel`](auto_modeling.md#AutoEasyDeLVisionModel)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`BaseAutoEasyState`](auto_modeling.md#BaseAutoEasyState)

### `Base`  ·  implements/extends EasyDeLBaseModule
- def: [`easydel/modules/auto/auto_modeling.py:330`](../../../../../../../raw/code/EasyDeL/easydel/modules/auto/auto_modeling.py#L330)
- signature: `class Base(EasyDeLBaseModule):`
- protocol/private: `_model_task`[`L248`](../../../../../../../raw/code/EasyDeL/easydel/modules/auto/auto_modeling.py#L248), `_model_task`[`L331`](../../../../../../../raw/code/EasyDeL/easydel/modules/auto/auto_modeling.py#L331)
- uses (calls/refs, reference-scoped): [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`_from_torch_pretrained`](../../infra/mixins/bridge.md#EasyBridgeMixin._from_torch_pretrained), [`from_pretrained`](../../infra/mixins/bridge.md#EasyBridgeMixin.from_pretrained), [`Base`](auto_modeling.md#BaseAutoEasyModel._from_easydel_params.Base), [`model_task`](auto_modeling.md#BaseAutoEasyModel.model_task)
- used by: [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule)

### `BaseAutoEasyModel`
- def: [`easydel/modules/auto/auto_modeling.py:38`](../../../../../../../raw/code/EasyDeL/easydel/modules/auto/auto_modeling.py#L38)
- doc: Base class for all Auto EasyDeL model classes. Provides common class methods
- signature: `class BaseAutoEasyModel:`
- members:
  - `_from_easydel_params(cls, pretrained_model_name_or_path: str, device: jax.Device | None = None, dtype: jax.numpy.dtype = jax.numpy.float32, param_dtype: jax.numpy.dtype = jax.numpy.float32, precision: jax.lax.Precision | None = None, sharding_axis_dims: Sequence[int] = (1, -1, 1, 1, 1), sharding_dcn_axis_dims: Sequence[int] | None = None, sharding_axis_names: Sequence[str] = ("dp", "fsdp", "ep", "tp", "sp"), partition_axis: PartitionAxis | None = None, shard_fns: Mapping[tuple, Callable] | dict | None = None, backend: EasyDeLBackends | None = None, platform: EasyDeLPlatforms | None = None, config_kwargs: EasyDeLBaseConfigDict | None = None, auto_shard_model: bool = True, partition_rules: tuple[tuple[str, PartitionSpec], ...] | None = None, quantization_config: QuantizationConfig | None = None, apply_quantization: bool = False, verbose: bool = True, **kwargs)` — [`L190`](../../../../../../../raw/code/EasyDeL/easydel/modules/auto/auto_modeling.py#L190) — Loads a model from EasyDeL saved parameters.
  - `_from_torch_pretrained(cls, pretrained_model_name_or_path: str, device: jax.Device | None = None, dtype: jax.numpy.dtype = jax.numpy.float32, param_dtype: jax.numpy.dtype = jax.numpy.float32, precision: jax.lax.Precision | None = None, sharding_axis_dims: Sequence[int] = (1, -1, 1, 1, 1), sharding_dcn_axis_dims: Sequence[int] | None = None, sharding_axis_names: Sequence[str] = ("dp", "fsdp", "ep", "tp", "sp"), partition_axis: PartitionAxis | None = None, shard_fns: Mapping[tuple, Callable] | dict | None = None, backend: EasyDeLBackends | None = None, platform: EasyDeLPlatforms | None = None, config_kwargs: EasyDeLBaseConfigDict | None = None, auto_shard_model: bool = True, partition_rules: tuple[tuple[str, PartitionSpec], ...] | None = None, quantization_config: QuantizationConfig | None = None, apply_quantization: bool = False, verbose: bool = True, **kwargs)` — [`L273`](../../../../../../../raw/code/EasyDeL/easydel/modules/auto/auto_modeling.py#L273) — Loads a model from PyTorch pretrained weights.
  - `_is_easydel(cls, pretrained_model_name_or_path, FLAX_WEIGHTS_NAME="easydel-model.parameters", MULTI_PART_NAME="easydel-model.parameters.safetensors.index.json", cache_dir: str | os.PathLike | None = None, force_download: bool = False, local_files_only: bool = False, token: str | bool | None = None, revision: str = "main")` — [`L356`](../../../../../../../raw/code/EasyDeL/easydel/modules/auto/auto_modeling.py#L356) — Checks if the given path or identifier points to an EasyDeL model checkpoint.
  - `from_config(cls, config: EasyDeLBaseConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.Precision | None = None, *, rngs: flax.nnx.Rngs | None = None)` — [`L50`](../../../../../../../raw/code/EasyDeL/easydel/modules/auto/auto_modeling.py#L50) — Instantiates a model module directly from a configuration object.
  - `from_pretrained(cls, pretrained_model_name_or_path: str, device: jax.Device | None = None, dtype: jax.numpy.dtype = jax.numpy.float32, param_dtype: jax.numpy.dtype = jax.numpy.float32, precision: jax.lax.Precision | None = None, sharding_axis_dims: Sequence[int] = (1, -1, 1, 1, 1), sharding_dcn_axis_dims: Sequence[int] | None = None, sharding_axis_names: Sequence[str] = ("dp", "fsdp", "ep", "tp", "sp"), partition_axis: PartitionAxis | None = None, shard_fns: Mapping[tuple, Callable] | dict | None = None, backend: EasyDeLBackends | None = None, platform: EasyDeLPlatforms | None = None, config_kwargs: EasyDeLBaseConfigDict | None = None, auto_shard_model: bool = True, partition_rules: tuple[tuple[str, PartitionSpec], ...] | None = None, quantization_config: QuantizationConfig | None = None, apply_quantization: bool = False, verbose: bool = True, from_torch: bool | None = None, **kwargs)` — [`L83`](../../../../../../../raw/code/EasyDeL/easydel/modules/auto/auto_modeling.py#L83) — Loads and shards a pretrained model from the Hugging Face Hub and converts it into an EasyDeL compatible model.
  - `model_task` — [`L47`](../../../../../../../raw/code/EasyDeL/easydel/modules/auto/auto_modeling.py#L47)
- uses (calls/refs, reference-scoped): [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`TaskType`](../../infra/factory.md#TaskType), [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`QuantizationConfig`](../../layers/quantization/_configs.md#QuantizationConfig), [`EasyDeLBackends`](../../infra/etils.md#EasyDeLBackends), [`EasyDeLBaseConfigDict`](../../infra/base_config.md#EasyDeLBaseConfigDict), [`EasyDeLPlatforms`](../../infra/etils.md#EasyDeLPlatforms), [`registry`](../../infra/factory.md#registry), [`AutoEasyDeLVisionModel`](auto_modeling.md#AutoEasyDeLVisionModel), [`AutoEasyDeLModel`](auto_modeling.md#AutoEasyDeLModel), [`get_module_registration`](../../infra/factory.md#Registry.get_module_registration), [`AutoEasyDeLModelForCausalLM`](auto_modeling.md#AutoEasyDeLModelForCausalLM), [`AutoEasyDeLModelForSpeechSeq2Seq`](auto_modeling.md#AutoEasyDeLModelForSpeechSeq2Seq), [`AutoEasyDeLAnyToAnyModel`](auto_modeling.md#AutoEasyDeLAnyToAnyModel), [`AutoEasyDeLModelForDiffusionLM`](auto_modeling.md#AutoEasyDeLModelForDiffusionLM), [`AutoEasyDeLModelForEmbedding`](auto_modeling.md#AutoEasyDeLModelForEmbedding), [`AutoEasyDeLModelForImageTextToText`](auto_modeling.md#AutoEasyDeLModelForImageTextToText), [`AutoEasyDeLModelForSeq2SeqLM`](auto_modeling.md#AutoEasyDeLModelForSeq2SeqLM), [`AutoEasyDeLModelForSequenceClassification`](auto_modeling.md#AutoEasyDeLModelForSequenceClassification), [`AutoEasyDeLModelForZeroShotImageClassification`](auto_modeling.md#AutoEasyDeLModelForZeroShotImageClassification), [`AutoStateAnyToAnyModel`](auto_modeling.md#AutoStateAnyToAnyModel), [`TENSORSTORE_INDEX_NAME`](../../infra/mixins/bridge.md#TENSORSTORE_INDEX_NAME), [`module`](../../infra/factory.md#ModuleRegistration.module), [`MODEL_INDEX_NAME`](auto_modeling.md#MODEL_INDEX_NAME), [`SAFETENSOR_INDEX_NAME`](auto_modeling.md#SAFETENSOR_INDEX_NAME)
- used by: [`_worker_startup_timeout`](../../inference/esurge/esurge_engine.md#eSurge._worker_startup_timeout), [`build_model`](../../infra/elarge/builders.md#build_model), [`from_pretrained`](auto_modeling.md#BaseAutoEasyState.from_pretrained), [`AutoEasyDeLVisionModel`](auto_modeling.md#AutoEasyDeLVisionModel), [`AutoEasyDeLModel`](auto_modeling.md#AutoEasyDeLModel), [`language_model`](../aya_vision/modeling_aya_vision.md#AyaVisionModel.language_model), [`from_config`](auto_modeling.md#BaseAutoEasyState.from_config), [`language_model`](../llava/modeling_llava.md#LlavaModel.language_model), [`language_model`](../mistral3/modeling_mistral3.md#Mistral3Model.language_model), [`vision_tower`](../gemma4/modeling_gemma4.md#Gemma4Model.vision_tower), [`vision_tower`](../aya_vision/modeling_aya_vision.md#AyaVisionModel.vision_tower), [`vision_tower`](../gemma3/modeling_gemma3.md#Gemma3Model.vision_tower), [`vision_tower`](../llava/modeling_llava.md#LlavaModel.vision_tower), [`vision_tower`](../mistral3/modeling_mistral3.md#Mistral3Model.vision_tower), [`AutoEasyDeLModelForCausalLM`](auto_modeling.md#AutoEasyDeLModelForCausalLM), [`AutoEasyDeLModelForSpeechSeq2Seq`](auto_modeling.md#AutoEasyDeLModelForSpeechSeq2Seq), [`AutoEasyDeLAnyToAnyModel`](auto_modeling.md#AutoEasyDeLAnyToAnyModel), [`AutoEasyDeLModelForDiffusionLM`](auto_modeling.md#AutoEasyDeLModelForDiffusionLM), [`AutoEasyDeLModelForEmbedding`](auto_modeling.md#AutoEasyDeLModelForEmbedding), [`AutoEasyDeLModelForImageTextToText`](auto_modeling.md#AutoEasyDeLModelForImageTextToText), [`AutoEasyDeLModelForSeq2SeqLM`](auto_modeling.md#AutoEasyDeLModelForSeq2SeqLM), [`AutoEasyDeLModelForSequenceClassification`](auto_modeling.md#AutoEasyDeLModelForSequenceClassification), [`AutoEasyDeLModelForZeroShotImageClassification`](auto_modeling.md#AutoEasyDeLModelForZeroShotImageClassification), [`AutoStateAnyToAnyModel`](auto_modeling.md#AutoStateAnyToAnyModel), [`Base`](auto_modeling.md#BaseAutoEasyModel._from_easydel_params.Base), [`Base`](auto_modeling.md#BaseAutoEasyModel._from_torch_pretrained.Base), [`model`](../../inference/vwhisper/server.md#WhisperModel.model), [`_base`](auto_modeling.md#BaseAutoEasyState._base)

### `BaseAutoEasyState`
- def: [`easydel/modules/auto/auto_modeling.py:442`](../../../../../../../raw/code/EasyDeL/easydel/modules/auto/auto_modeling.py#L442)
- doc: Base class for Auto EasyDeL state classes. Provides common class methods
- signature: `class BaseAutoEasyState:`
- members:
  - `from_config(cls, config: EasyDeLBaseConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.Precision | None = None, *, rngs: flax.nnx.Rngs | None = None)` — [`L454`](../../../../../../../raw/code/EasyDeL/easydel/modules/auto/auto_modeling.py#L454) — Creates an EasyDeLState directly from a configuration object.
  - `from_pretrained(cls, pretrained_model_name_or_path: str, device: jax.Device | None = None, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.Precision | None = None, sharding_axis_dims: Sequence[int] = (1, -1, 1, 1, 1), sharding_dcn_axis_dims: Sequence[int] | None = None, sharding_axis_names: Sequence[str] = ("dp", "fsdp", "ep", "tp", "sp"), partition_axis: PartitionAxis | None = None, shard_fns: Mapping[tuple, Callable] | dict | None = None, backend: EasyDeLBackends | None = None, platform: EasyDeLPlatforms | None = None, config_kwargs: EasyDeLBaseConfigDict | None = None, auto_shard_model: bool = True, partition_rules: tuple[tuple[str, PartitionSpec], ...] | None = None, quantization_config: QuantizationConfig | None = None, from_torch: bool | None = None, **kwargs)` — [`L484`](../../../../../../../raw/code/EasyDeL/easydel/modules/auto/auto_modeling.py#L484) — Loads and shards a pretrained model from the Hugging Face Hub and converts it into an EasyDeL compatible state.
- protocol/private: `_base`[`L451`](../../../../../../../raw/code/EasyDeL/easydel/modules/auto/auto_modeling.py#L451)
- uses (calls/refs, reference-scoped): [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`EasyDeLState`](../../infra/base_state.md#EasyDeLState), [`QuantizationConfig`](../../layers/quantization/_configs.md#QuantizationConfig), [`to_state`](../../infra/base_module.md#EasyDeLBaseModule.to_state), [`BaseAutoEasyModel`](auto_modeling.md#BaseAutoEasyModel), [`from_pretrained`](auto_modeling.md#BaseAutoEasyModel.from_pretrained), [`EasyDeLBackends`](../../infra/etils.md#EasyDeLBackends), [`EasyDeLBaseConfigDict`](../../infra/base_config.md#EasyDeLBaseConfigDict), [`EasyDeLPlatforms`](../../infra/etils.md#EasyDeLPlatforms), [`from_config`](auto_modeling.md#BaseAutoEasyModel.from_config), [`create`](../../infra/base_state.md#EasyDeLState.create), [`AutoState`](auto_modeling.md#AutoState), [`AutoStateForCausalLM`](auto_modeling.md#AutoStateForCausalLM), [`AutoStateForDiffusionLM`](auto_modeling.md#AutoStateForDiffusionLM), [`AutoStateForEmbedding`](auto_modeling.md#AutoStateForEmbedding), [`AutoStateForImageSequenceClassification`](auto_modeling.md#AutoStateForImageSequenceClassification), [`AutoStateForImageTextToText`](auto_modeling.md#AutoStateForImageTextToText), [`AutoStateForSeq2SeqLM`](auto_modeling.md#AutoStateForSeq2SeqLM), [`AutoStateForSpeechSeq2Seq`](auto_modeling.md#AutoStateForSpeechSeq2Seq), [`AutoStateForZeroShotImageClassification`](auto_modeling.md#AutoStateForZeroShotImageClassification), [`AutoStateVisionModel`](auto_modeling.md#AutoStateVisionModel)
- used by: [`AutoState`](auto_modeling.md#AutoState), [`AutoStateForCausalLM`](auto_modeling.md#AutoStateForCausalLM), [`AutoStateForDiffusionLM`](auto_modeling.md#AutoStateForDiffusionLM), [`AutoStateForEmbedding`](auto_modeling.md#AutoStateForEmbedding), [`AutoStateForImageSequenceClassification`](auto_modeling.md#AutoStateForImageSequenceClassification), [`AutoStateForImageTextToText`](auto_modeling.md#AutoStateForImageTextToText), [`AutoStateForSeq2SeqLM`](auto_modeling.md#AutoStateForSeq2SeqLM), [`AutoStateForSpeechSeq2Seq`](auto_modeling.md#AutoStateForSpeechSeq2Seq), [`AutoStateForZeroShotImageClassification`](auto_modeling.md#AutoStateForZeroShotImageClassification), [`AutoStateVisionModel`](auto_modeling.md#AutoStateVisionModel)

## Module values
- `MODEL_INDEX_NAME` — [`L35`](../../../../../../../raw/code/EasyDeL/easydel/modules/auto/auto_modeling.py#L35)
- `SAFETENSOR_INDEX_NAME` — [`L34`](../../../../../../../raw/code/EasyDeL/easydel/modules/auto/auto_modeling.py#L34)

