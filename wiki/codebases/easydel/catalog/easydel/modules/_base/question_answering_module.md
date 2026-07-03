---
title: 'Module: easydel/modules/_base/question_answering_module.py'
type: catalog
provenance: extracted
module: easydel/modules/_base/question_answering_module.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules._base.question_answering_module`/BaseQuestionAnsweringModule#
symbols:
  BaseQuestionAnsweringModule.__call__: __call__().
  BaseQuestionAnsweringModule.__init__: __init__().
  BaseQuestionAnsweringModule: ''
  BaseQuestionAnsweringModule.qa_outputs: qa_outputs.
  BaseQuestionAnsweringModule.get_task_head: get_task_head().
  BaseQuestionAnsweringModule.get_lm_head: get_lm_head().
---
# Module: [`easydel/modules/_base/question_answering_module.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/question_answering_module.py)

## Classes
### `BaseQuestionAnsweringModule`  ·  implements/extends BaseTaskModule
- def: [`easydel/modules/_base/question_answering_module.py:74`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/question_answering_module.py#L74)
- doc: Generic base class for Question Answering (extractive QA).
- signature: `class BaseQuestionAnsweringModule(BaseTaskModule[ModelT, ConfigT]):`
- members:
  - `__call__(self, input_ids: Int[Array, "batch seq_len"] | None = None, inputs_embeds: Float[Array, "batch seq_len hidden_dim"] | None = None, attention_mask: Bool[Array, "batch seq_len"] | None = None, mask_info: MaskInfo | None = None, position_ids: Int[Array, "batch seq_len"] | None = None, mode: common_types.RUNTIME_MODE_TYPES | None = None, past_key_values: TransformerCache | RaggedPagesCache | HybridCache | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, output_attentions: bool | None = None, output_hidden_states: bool | None = None)` — [`L215`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/question_answering_module.py#L215) — Forward pass for question answering.
  - `__init__(self, config: ConfigT, base_model: ModelT | None = None, base_model_class: type[ModelT] | None = None, base_model_name: str = "model", dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs, qa_head_bias: bool = True, qa_head_kernel_init: Callable | None = None)` — [`L125`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/question_answering_module.py#L125) — Initialize the Question Answering module.
  - `get_lm_head(self)` — [`L342`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/question_answering_module.py#L342) — Raises NotImplementedError as QA models have no LM head.
  - `get_task_head(self)` — [`L324`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/question_answering_module.py#L324) — Returns the QA output head module.
  - `qa_outputs` — [`L204`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/question_answering_module.py#L204)
- uses (calls/refs, reference-scoped): [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`TransformerCache`](../../caching/transformer/cache.md#TransformerCache), [`ColumnParallelLinear`](../../layers/linears/_linear.md#ColumnParallelLinear), [`HybridCache`](../../caching/hybrid/cache.md#HybridCache), [`RaggedPagesCache`](../../caching/ragged_page/cache.md#RaggedPagesCache), [`auto_remat`](../../infra/utils.md#auto_remat), [`base_model`](_base_task_module.md#BaseTaskModule.base_model), [`BaseTaskModule`](_base_task_module.md#BaseTaskModule), [`ModelT`](_base_task_module.md#ModelT), [`last_hidden_state`](../../infra/modeling_outputs.md#BaseModelOutput.last_hidden_state), [`ConfigT`](_base_task_module.md#ConfigT), [`attentions`](../../infra/modeling_outputs.md#BaseModelOutput.attentions), [`hidden_states`](../../infra/modeling_outputs.md#BaseModelOutput.hidden_states), [`__init__`](_base_task_module.md#BaseTaskModule.__init__), [`_gradient_checkpointing_feature`](_base_task_module.md#BaseTaskModule._gradient_checkpointing_feature), [`get_config`](_features.md#GradientCheckpointingFeature.get_config), [`QuestionAnsweringModelOutput`](../../infra/modeling_outputs.md#QuestionAnsweringModelOutput), [`RobertaForQuestionAnswering`](../roberta/modeling_roberta.md#RobertaForQuestionAnswering), [`should_checkpoint`](_features.md#GradientCheckpointingFeature.should_checkpoint), [`_head_bias`](_base_task_module.md#BaseTaskModule._head_bias), [`_head_kernel_init`](_base_task_module.md#BaseTaskModule._head_kernel_init), [`get_task_head`](../roberta/modeling_roberta.md#RobertaForQuestionAnswering.get_task_head), [`get_lm_head`](../roberta/modeling_roberta.md#RobertaForQuestionAnswering.get_lm_head)
- used by: [`get_lm_head`](../../infra/base_module.md#EasyDeLBaseModule.get_lm_head), [`BaseTaskModule`](_base_task_module.md#BaseTaskModule), [`get_task_head`](_base_task_module.md#BaseTaskModule.get_task_head), [`create_question_answering_class`](_auto_mapper.md#create_question_answering_class), [`__call__`](../roberta/modeling_roberta.md#RobertaForQuestionAnswering.__call__), [`RobertaForQuestionAnswering`](../roberta/modeling_roberta.md#RobertaForQuestionAnswering), [`__init__`](../roberta/modeling_roberta.md#RobertaForQuestionAnswering.__init__), [`get_task_head`](../roberta/modeling_roberta.md#RobertaForQuestionAnswering.get_task_head)

