---
title: 'Module: easydel/modules/_base/embedding_module.py'
type: catalog
provenance: extracted
module: easydel/modules/_base/embedding_module.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules._base.embedding_module`/BaseEmbeddingModule#
symbols:
  BaseEmbeddingModule.__call__: __call__().
  BaseEmbeddingModule: ''
  BaseEmbeddingModule.encode: encode().
  BaseEmbeddingModule.__init__: __init__().
  BaseEmbeddingModule._embedding_dim: _embedding_dim.
  BaseEmbeddingModule._normalize_embeddings: _normalize_embeddings.
  BaseEmbeddingModule.get_task_head: get_task_head().
  BaseEmbeddingModule.get_lm_head: get_lm_head().
  BaseEmbeddingModule.cosine_similarity: cosine_similarity().
  BaseEmbeddingModule.dot_product_similarity: dot_product_similarity().
---
# Module: [`easydel/modules/_base/embedding_module.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/embedding_module.py)

## Classes
### `BaseEmbeddingModule`  ·  implements/extends BaseTaskModule
- def: [`easydel/modules/_base/embedding_module.py:79`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/embedding_module.py#L79)
- doc: Generic base class for Embedding models.
- signature: `class BaseEmbeddingModule(BaseTaskModule[ModelT, ConfigT]):`
- members:
  - `__call__(self, input_ids: Int[Array, "batch seq_len"] | None = None, inputs_embeds: Float[Array, "batch seq_len hidden_dim"] | None = None, attention_mask: Bool[Array, "batch seq_len"] | None = None, mask_info: MaskInfo | None = None, position_ids: Int[Array, "batch seq_len"] | None = None, mode: common_types.RUNTIME_MODE_TYPES | None = None, past_key_values: TransformerCache | RaggedPagesCache | HybridCache | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, output_attentions: bool | None = None, output_hidden_states: bool | None = None)` — [`L173`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/embedding_module.py#L173) — Forward pass through the Embedding model.
  - `__init__(self, config: ConfigT, base_model: ModelT | None = None, base_model_class: type[ModelT] | None = None, base_model_name: str = "model", dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs, pooling_strategy: str = "last", router_aux_loss_coef: float | None = None, normalize_embeddings: bool = True, embedding_dim: int | None = None)` — [`L117`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/embedding_module.py#L117) — Initialize the Embedding module.
  - `cosine_similarity(a: Float[Array, "n dim"], b: Float[Array, "m dim"])` — [`L336`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/embedding_module.py#L336) — Compute pairwise cosine similarity between two sets of embeddings.
  - `dot_product_similarity(a: Float[Array, "n dim"], b: Float[Array, "m dim"])` — [`L355`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/embedding_module.py#L355) — Compute pairwise dot-product similarity between embeddings.
  - `encode(self, texts: list[str] | str, tokenizer=None, max_length: int | None = None, batch_size: int = 32, normalize: bool | None = None, embedding_dim: int | None = None)` — [`L252`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/embedding_module.py#L252) — Encode texts into dense embedding vectors.
  - `get_lm_head(self)` — [`L248`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/embedding_module.py#L248) — Embedding models do not have a language modeling head.
  - `get_task_head(self)` — [`L244`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/embedding_module.py#L244) — Embedding models have no task-specific head.
- protocol/private: `_embedding_dim`[`L171`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/embedding_module.py#L171), `_normalize_embeddings`[`L170`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/embedding_module.py#L170)
- uses (calls/refs, reference-scoped): [`config`](../../infra/base_module.md#EasyDeLBaseModule.config), [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`TransformerCache`](../../caching/transformer/cache.md#TransformerCache), [`HybridCache`](../../caching/hybrid/cache.md#HybridCache), [`RaggedPagesCache`](../../caching/ragged_page/cache.md#RaggedPagesCache), [`base_model`](_base_task_module.md#BaseTaskModule.base_model), [`BaseTaskModule`](_base_task_module.md#BaseTaskModule), [`ModelT`](_base_task_module.md#ModelT), [`last_hidden_state`](../../infra/modeling_outputs.md#BaseModelOutput.last_hidden_state), [`ConfigT`](_base_task_module.md#ConfigT), [`attentions`](../../infra/modeling_outputs.md#BaseModelOutput.attentions), [`hidden_states`](../../infra/modeling_outputs.md#BaseModelOutput.hidden_states), [`Qwen2ForEmbedding`](../qwen2/modeling_qwen.md#Qwen2ForEmbedding), [`Qwen3ForEmbedding`](../qwen3/modeling_qwen3.md#Qwen3ForEmbedding), [`__init__`](_base_task_module.md#BaseTaskModule.__init__), [`past_key_values`](../../infra/modeling_outputs.md#BaseModelOutput.past_key_values), [`pool_sequence`](_base_task_module.md#BaseTaskModule.pool_sequence), [`EmbeddingOutput`](../../infra/modeling_outputs.md#EmbeddingOutput), [`embeddings`](../../infra/modeling_outputs.md#EmbeddingOutput.embeddings)
- used by: [`get_lm_head`](../../infra/base_module.md#EasyDeLBaseModule.get_lm_head), [`BaseTaskModule`](_base_task_module.md#BaseTaskModule), [`get_task_head`](_base_task_module.md#BaseTaskModule.get_task_head), [`Qwen2ForEmbedding`](../qwen2/modeling_qwen.md#Qwen2ForEmbedding), [`Qwen3ForEmbedding`](../qwen3/modeling_qwen3.md#Qwen3ForEmbedding), [`create_embedding_class`](_auto_mapper.md#create_embedding_class), [`__init__`](../qwen2/modeling_qwen.md#Qwen2ForEmbedding.__init__), [`__init__`](../qwen3/modeling_qwen3.md#Qwen3ForEmbedding.__init__)

