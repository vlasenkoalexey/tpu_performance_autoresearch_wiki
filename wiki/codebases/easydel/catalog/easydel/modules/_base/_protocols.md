---
title: 'Module: easydel/modules/_base/_protocols.py'
type: catalog
provenance: extracted
module: easydel/modules/_base/_protocols.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules._base._protocols`/
symbols:
  BaseModelProtocol.__call__: BaseModelProtocol#__call__().
  VisionLanguageProtocol.__call__: VisionLanguageProtocol#__call__().
  BaseModelProtocol: BaseModelProtocol#
  EncoderDecoderProtocol: EncoderDecoderProtocol#
  VisionModelProtocol.__call__: VisionModelProtocol#__call__().
  BaseModelProtocol.get_embedding: BaseModelProtocol#get_embedding().
  BaseModelProtocol.get_decoder: BaseModelProtocol#get_decoder().
  VisionModelProtocol: VisionModelProtocol#
  VisionLanguageProtocol: VisionLanguageProtocol#
  BaseModelProtocol.config: BaseModelProtocol#config.
  BaseModelProtocol.dtype: BaseModelProtocol#dtype.
  BaseModelProtocol.param_dtype: BaseModelProtocol#param_dtype.
  BaseModelProtocol.precision: BaseModelProtocol#precision.
  EncoderDecoderProtocol.get_encoder: EncoderDecoderProtocol#get_encoder().
  VisionModelProtocol.config: VisionModelProtocol#config.
  VisionModelProtocol.dtype: VisionModelProtocol#dtype.
  VisionModelProtocol.param_dtype: VisionModelProtocol#param_dtype.
  VisionModelProtocol.precision: VisionModelProtocol#precision.
  VisionModelProtocol.get_embedding: VisionModelProtocol#get_embedding().
  VisionLanguageProtocol.config: VisionLanguageProtocol#config.
  VisionLanguageProtocol.dtype: VisionLanguageProtocol#dtype.
  VisionLanguageProtocol.param_dtype: VisionLanguageProtocol#param_dtype.
  VisionLanguageProtocol.precision: VisionLanguageProtocol#precision.
  VisionLanguageProtocol.get_vision_tower: VisionLanguageProtocol#get_vision_tower().
  VisionLanguageProtocol.get_language_model: VisionLanguageProtocol#get_language_model().
---
# Module: [`easydel/modules/_base/_protocols.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_protocols.py)

## Classes
### `BaseModelProtocol`  ·  implements/extends Protocol
- def: [`easydel/modules/_base/_protocols.py:77`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_protocols.py#L77)
- doc: Protocol defining the expected interface for decoder-only base models.
- signature: `class BaseModelProtocol(Protocol):`
- members:
  - `__call__(self, input_ids: Int[Array, "batch seq_len"] | None = None, inputs_embeds: Float[Array, "batch seq_len hidden_dim"] | None = None, attention_mask: Bool[Array, "batch seq_len"] | None = None, mask_info: MaskInfo | None = None, position_ids: Int[Array, "batch seq_len"] | None = None, mode: common_types.RUNTIME_MODE_TYPES | None = None, past_key_values: TransformerCache | RaggedPagesCache | HybridCache | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, output_attentions: bool | None = None, output_hidden_states: bool | None = None)` — [`L127`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_protocols.py#L127) — Forward pass through the base model.
  - `get_decoder(self)` — [`L190`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_protocols.py#L190) — Return the decoder (transformer layers) part of the model.
  - `get_embedding(self)` — [`L177`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_protocols.py#L177) — Return the input embedding layer of the model.
  - `config` — [`L122`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_protocols.py#L122)
  - `dtype` — [`L123`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_protocols.py#L123)
  - `param_dtype` — [`L124`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_protocols.py#L124)
  - `precision` — [`L125`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_protocols.py#L125)
- uses (calls/refs, reference-scoped): [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`TransformerCache`](../../caching/transformer/cache.md#TransformerCache), [`HybridCache`](../../caching/hybrid/cache.md#HybridCache), [`RaggedPagesCache`](../../caching/ragged_page/cache.md#RaggedPagesCache), [`BaseModelOutput`](../../infra/modeling_outputs.md#BaseModelOutput), [`EncoderDecoderProtocol`](_protocols.md#EncoderDecoderProtocol)
- used by: [`get_embedding`](_base_task_module.md#BaseTaskModule.get_embedding), [`get_decoder`](_base_task_module.md#BaseTaskModule.get_decoder), [`ModelT`](_base_task_module.md#ModelT), [`EncoderDecoderProtocol`](_protocols.md#EncoderDecoderProtocol)

### `EncoderDecoderProtocol`  ·  implements/extends BaseModelProtocol, Protocol
- def: [`easydel/modules/_base/_protocols.py:203`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_protocols.py#L203)
- doc: Protocol for encoder-decoder models (e.g., T5, BART).
- signature: `class EncoderDecoderProtocol(BaseModelProtocol, Protocol):`
- members:
  - `get_encoder(self)` — [`L231`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_protocols.py#L231) — Return the encoder part of the model.
- uses (calls/refs, reference-scoped): [`BaseModelProtocol`](_protocols.md#BaseModelProtocol)
- used by: [`BaseModelProtocol`](_protocols.md#BaseModelProtocol)

### `VisionLanguageProtocol`  ·  implements/extends Protocol
- def: [`easydel/modules/_base/_protocols.py:317`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_protocols.py#L317)
- doc: Protocol for vision-language models (e.g., LLaVA, Qwen2-VL).
- signature: `class VisionLanguageProtocol(Protocol):`
- members:
  - `__call__(self, input_ids: Int[Array, "batch seq_len"] | None = None, pixel_values: Float[Array, "batch channels height width"] | None = None, attention_mask: Bool[Array, "batch seq_len"] | None = None, mask_info: MaskInfo | None = None, position_ids: Int[Array, "batch seq_len"] | None = None, mode: common_types.RUNTIME_MODE_TYPES | None = None, past_key_values: TransformerCache | RaggedPagesCache | HybridCache | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, output_attentions: bool | None = None, output_hidden_states: bool | None = None)` — [`L361`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_protocols.py#L361) — Forward pass through the vision-language model.
  - `get_language_model(self)` — [`L411`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_protocols.py#L411) — Return the language model component.
  - `get_vision_tower(self)` — [`L400`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_protocols.py#L400) — Return the vision encoder component.
  - `config` — [`L356`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_protocols.py#L356)
  - `dtype` — [`L357`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_protocols.py#L357)
  - `param_dtype` — [`L358`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_protocols.py#L358)
  - `precision` — [`L359`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_protocols.py#L359)
- uses (calls/refs, reference-scoped): [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`TransformerCache`](../../caching/transformer/cache.md#TransformerCache), [`HybridCache`](../../caching/hybrid/cache.md#HybridCache), [`RaggedPagesCache`](../../caching/ragged_page/cache.md#RaggedPagesCache), [`BaseModelOutput`](../../infra/modeling_outputs.md#BaseModelOutput)

### `VisionModelProtocol`  ·  implements/extends Protocol
- def: [`easydel/modules/_base/_protocols.py:244`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_protocols.py#L244)
- doc: Protocol for vision models (e.g., ViT, CLIP vision encoder).
- signature: `class VisionModelProtocol(Protocol):`
- members:
  - `__call__(self, pixel_values: Float[Array, "batch channels height width"] | None = None, output_attentions: bool | None = None, output_hidden_states: bool | None = None)` — [`L275`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_protocols.py#L275) — Forward pass through the vision model.
  - `get_embedding(self)` — [`L304`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_protocols.py#L304) — Return the patch embedding/projection layer.
  - `config` — [`L270`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_protocols.py#L270)
  - `dtype` — [`L271`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_protocols.py#L271)
  - `param_dtype` — [`L272`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_protocols.py#L272)
  - `precision` — [`L273`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_protocols.py#L273)
- uses (calls/refs, reference-scoped): [`BaseModelOutput`](../../infra/modeling_outputs.md#BaseModelOutput)

