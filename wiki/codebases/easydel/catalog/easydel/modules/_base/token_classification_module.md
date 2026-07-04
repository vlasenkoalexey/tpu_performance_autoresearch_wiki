---
title: 'Module: easydel/modules/_base/token_classification_module.py'
type: catalog
provenance: extracted
module: easydel/modules/_base/token_classification_module.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules._base.token_classification_module`/BaseTokenClassificationModule#
symbols:
  BaseTokenClassificationModule.__call__: __call__().
  BaseTokenClassificationModule: ''
  BaseTokenClassificationModule.dropout: dropout.
  BaseTokenClassificationModule.classifier: classifier.
  BaseTokenClassificationModule.__init__: __init__().
  BaseTokenClassificationModule.get_task_head: get_task_head().
  BaseTokenClassificationModule.get_lm_head: get_lm_head().
---
# Module: [`easydel/modules/_base/token_classification_module.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/token_classification_module.py)

## Classes
### `BaseTokenClassificationModule`  ·  implements/extends BaseTaskModule
- def: [`easydel/modules/_base/token_classification_module.py:73`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/token_classification_module.py#L73)
- doc: Generic base class for Token Classification.
- signature: `class BaseTokenClassificationModule(BaseTaskModule[ModelT, ConfigT]):`
- members:
  - `__call__(self, input_ids: Int[Array, "batch seq_len"] | None = None, inputs_embeds: Float[Array, "batch seq_len hidden_dim"] | None = None, attention_mask: Bool[Array, "batch seq_len"] | None = None, mask_info: MaskInfo | None = None, position_ids: Int[Array, "batch seq_len"] | None = None, mode: common_types.RUNTIME_MODE_TYPES | None = None, past_key_values: TransformerCache | RaggedPagesCache | HybridCache | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, output_attentions: bool | None = None, output_hidden_states: bool | None = None)` — [`L227`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/token_classification_module.py#L227) — Forward pass for token classification.
  - `__init__(self, config: ConfigT, base_model: ModelT | None = None, base_model_class: type[ModelT] | None = None, base_model_name: str = "model", dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs, classifier_dropout: float | None = None, classifier_bias: bool = True, classifier_kernel_init: Callable | None = None)` — [`L125`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/token_classification_module.py#L125) — Initialize the Token Classification module.
  - `get_lm_head(self)` — [`L345`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/token_classification_module.py#L345) — Raises NotImplementedError as token classification has no LM head.
  - `get_task_head(self)` — [`L327`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/token_classification_module.py#L327) — Returns the token classification head module.
  - `classifier` — [`L216`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/token_classification_module.py#L216)
  - `dropout` — [`L206`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/token_classification_module.py#L206)
- uses (calls/refs, reference-scoped): [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`TransformerCache`](../../caching/transformer/cache.md#TransformerCache), [`ColumnParallelLinear`](../../layers/linears/_linear.md#ColumnParallelLinear), [`HybridCache`](../../caching/hybrid/cache.md#HybridCache), [`RaggedPagesCache`](../../caching/ragged_page/cache.md#RaggedPagesCache), [`auto_remat`](../../infra/utils.md#auto_remat), [`base_model`](_base_task_module.md#BaseTaskModule.base_model), [`BaseTaskModule`](_base_task_module.md#BaseTaskModule), [`ModelT`](_base_task_module.md#ModelT), [`last_hidden_state`](../../infra/modeling_outputs.md#BaseModelOutput.last_hidden_state), [`ConfigT`](_base_task_module.md#ConfigT), [`attentions`](../../infra/modeling_outputs.md#BaseModelOutput.attentions), [`hidden_states`](../../infra/modeling_outputs.md#BaseModelOutput.hidden_states), [`__init__`](_base_task_module.md#BaseTaskModule.__init__), [`_gradient_checkpointing_feature`](_base_task_module.md#BaseTaskModule._gradient_checkpointing_feature), [`get_config`](_features.md#GradientCheckpointingFeature.get_config), [`TokenClassifierOutput`](../../infra/modeling_outputs.md#TokenClassifierOutput), [`RobertaForTokenClassification`](../roberta/modeling_roberta.md#RobertaForTokenClassification), [`should_checkpoint`](_features.md#GradientCheckpointingFeature.should_checkpoint), [`_head_bias`](_base_task_module.md#BaseTaskModule._head_bias), [`_head_kernel_init`](_base_task_module.md#BaseTaskModule._head_kernel_init), [`get_task_head`](../roberta/modeling_roberta.md#RobertaForTokenClassification.get_task_head), [`get_lm_head`](../roberta/modeling_roberta.md#RobertaForTokenClassification.get_lm_head)
- used by: [`get_lm_head`](../../infra/base_module.md#EasyDeLBaseModule.get_lm_head), [`BaseTaskModule`](_base_task_module.md#BaseTaskModule), [`get_task_head`](_base_task_module.md#BaseTaskModule.get_task_head), [`create_token_classification_class`](_auto_mapper.md#create_token_classification_class), [`__call__`](../roberta/modeling_roberta.md#RobertaForTokenClassification.__call__), [`__init__`](../roberta/modeling_roberta.md#RobertaForTokenClassification.__init__), [`RobertaForTokenClassification`](../roberta/modeling_roberta.md#RobertaForTokenClassification), [`get_task_head`](../roberta/modeling_roberta.md#RobertaForTokenClassification.get_task_head)

