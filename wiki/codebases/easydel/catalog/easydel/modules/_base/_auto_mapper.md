---
title: 'Module: easydel/modules/_base/_auto_mapper.py'
type: catalog
provenance: extracted
module: easydel/modules/_base/_auto_mapper.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules._base._auto_mapper`/
symbols:
  AUTO_MODEL_FACTORY_REGISTRY.AUTO_MODEL_FACTORY_REGISTRY: AUTO_MODEL_FACTORY_REGISTRY.AUTO_MODEL_FACTORY_REGISTRY.
  create_causal_lm_class: create_causal_lm_class().
  create_sequence_classification_class: create_sequence_classification_class().
  create_image_classification_class: create_image_classification_class().
  create_embedding_class: create_embedding_class().
  create_conditional_generation_class: create_conditional_generation_class().
  ModelT: ModelT.
  ConfigT: ConfigT.
  create_token_classification_class: create_token_classification_class().
  create_question_answering_class: create_question_answering_class().
  create_task_model_class: create_task_model_class().
  create_causal_lm_class.__init__: create_causal_lm_class().__init__().
  create_sequence_classification_class.__init__: create_sequence_classification_class().__init__().
  create_token_classification_class.__init__: create_token_classification_class().__init__().
  create_question_answering_class.__init__: create_question_answering_class().__init__().
  create_conditional_generation_class.__init__: create_conditional_generation_class().__init__().
  create_image_classification_class.__init__: create_image_classification_class().__init__().
  create_embedding_class.__init__: create_embedding_class().__init__().
---
# Module: [`easydel/modules/_base/_auto_mapper.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_auto_mapper.py)

## Functions
- `__init__(self, config, dtype=None, param_dtype=None, precision=None, *, rngs, **kwargs)` — [`L148`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_auto_mapper.py#L148) — Initialize the dynamically created ForCausalLM model.
- `__init__(self, config, dtype=None, param_dtype=None, precision=None, *, rngs, **kwargs)` — [`L244`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_auto_mapper.py#L244) — Initialize the dynamically created ForSequenceClassification model.
- `__init__(self, config, dtype=None, param_dtype=None, precision=None, *, rngs, **kwargs)` — [`L332`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_auto_mapper.py#L332) — Initialize the dynamically created ForTokenClassification model.
- `__init__(self, config, dtype=None, param_dtype=None, precision=None, *, rngs, **kwargs)` — [`L420`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_auto_mapper.py#L420) — Initialize the dynamically created ForQuestionAnswering model.
- `__init__(self, config, dtype=None, param_dtype=None, precision=None, *, rngs, **kwargs)` — [`L508`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_auto_mapper.py#L508) — Initialize the dynamically created ForConditionalGeneration model.
- `__init__(self, config, dtype=None, param_dtype=None, precision=None, *, rngs, **kwargs)` — [`L600`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_auto_mapper.py#L600) — Initialize the dynamically created ForImageClassification model.
- `__init__(self, config, dtype=None, param_dtype=None, precision=None, *, rngs, **kwargs)` — [`L674`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_auto_mapper.py#L674)
- `create_causal_lm_class(model_name: str, base_model_class: type[ModelT], config_class: type[ConfigT], model_type: str, base_model_name: str = "model", **default_feature_kwargs: Any)` — [`L80`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_auto_mapper.py#L80) — Create a ForCausalLM class dynamically.
- `create_conditional_generation_class(model_name: str, base_model_class: type[ModelT], config_class: type[ConfigT], model_type: str, base_model_name: str = "model", **default_feature_kwargs: Any)` — [`L465`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_auto_mapper.py#L465) — Create a ForConditionalGeneration class dynamically.
- `create_embedding_class(model_name: str, base_model_class: type[ModelT], config_class: type[ConfigT], model_type: str, base_model_name: str = "model", **default_feature_kwargs: Any)` — [`L645`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_auto_mapper.py#L645) — Create a ForEmbedding class dynamically.
- `create_image_classification_class(model_name: str, base_model_class: type[ModelT], config_class: type[ConfigT], model_type: str, base_model_name: str = "vision_model", **default_feature_kwargs: Any)` — [`L553`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_auto_mapper.py#L553) — Create a ForImageClassification class dynamically.
- `create_question_answering_class(model_name: str, base_model_class: type[ModelT], config_class: type[ConfigT], model_type: str, base_model_name: str = "model", **default_feature_kwargs: Any)` — [`L377`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_auto_mapper.py#L377) — Create a ForQuestionAnswering class dynamically.
- `create_sequence_classification_class(model_name: str, base_model_class: type[ModelT], config_class: type[ConfigT], model_type: str, base_model_name: str = "model", **default_feature_kwargs: Any)` — [`L196`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_auto_mapper.py#L196) — Create a ForSequenceClassification class dynamically.
- `create_task_model_class(task_type: TaskType, model_name: str, base_model_class: type[ModelT], config_class: type[ConfigT], model_type: str, base_model_name: str = "model", **default_feature_kwargs: Any)` — [`L735`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_auto_mapper.py#L735) — Create a task-specific model class using the appropriate factory.
- `create_token_classification_class(model_name: str, base_model_class: type[ModelT], config_class: type[ConfigT], model_type: str, base_model_name: str = "model", **default_feature_kwargs: Any)` — [`L289`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_auto_mapper.py#L289) — Create a ForTokenClassification class dynamically.

## Module values
- `AUTO_MODEL_FACTORY_REGISTRY` — [`L709`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_auto_mapper.py#L709)
- `ConfigT` — [`L76`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_auto_mapper.py#L76)
- `ModelT` — [`L73`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_auto_mapper.py#L73)

