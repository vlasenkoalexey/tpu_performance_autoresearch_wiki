---
title: 'Module: easydel/modules/whisper/whisper_configuration.py'
type: catalog
provenance: extracted
module: easydel/modules/whisper/whisper_configuration.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.whisper.whisper_configuration`/WhisperConfig#
symbols:
  WhisperConfig: ''
  WhisperConfig.__init__: __init__().
  WhisperConfig.attention_dropout: attention_dropout.
  WhisperConfig.d_model: d_model.
  WhisperConfig.init_std: init_std.
  WhisperConfig.max_position_embeddings: max_position_embeddings.
  WhisperConfig.dropout: dropout.
  WhisperConfig.activation_function: activation_function.
  WhisperConfig.activation_dropout: activation_dropout.
  WhisperConfig.encoder_ffn_dim: encoder_ffn_dim.
  WhisperConfig.decoder_attention_heads: decoder_attention_heads.
  WhisperConfig.decoder_ffn_dim: decoder_ffn_dim.
  WhisperConfig.gradient_checkpointing: gradient_checkpointing.
  WhisperConfig.classifier_proj_size: classifier_proj_size.
  WhisperConfig.encoder_attention_heads: encoder_attention_heads.
  WhisperConfig.num_hidden_layers: num_hidden_layers.
  WhisperConfig.use_weighted_layer_sum: use_weighted_layer_sum.
  WhisperConfig.model_type: model_type.
  WhisperConfig.attribute_map: attribute_map.
  WhisperConfig.vocab_size: vocab_size.
  WhisperConfig.num_mel_bins: num_mel_bins.
  WhisperConfig.encoder_layers: encoder_layers.
  WhisperConfig.decoder_layers: decoder_layers.
  WhisperConfig.encoder_layerdrop: encoder_layerdrop.
  WhisperConfig.decoder_layerdrop: decoder_layerdrop.
  WhisperConfig.use_cache: use_cache.
  WhisperConfig.scale_embedding: scale_embedding.
  WhisperConfig.max_source_positions: max_source_positions.
  WhisperConfig.max_target_positions: max_target_positions.
  WhisperConfig.apply_spec_augment: apply_spec_augment.
  WhisperConfig.mask_time_prob: mask_time_prob.
  WhisperConfig.mask_time_length: mask_time_length.
  WhisperConfig.mask_time_min_masks: mask_time_min_masks.
  WhisperConfig.mask_feature_prob: mask_feature_prob.
  WhisperConfig.mask_feature_length: mask_feature_length.
  WhisperConfig.mask_feature_min_masks: mask_feature_min_masks.
  WhisperConfig.median_filter_width: median_filter_width.
  WhisperConfig.bits: bits.
  WhisperConfig.get_partition_rules: get_partition_rules().
---
# Module: [`easydel/modules/whisper/whisper_configuration.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/whisper/whisper_configuration.py)

## Classes
### `WhisperConfig`  ·  implements/extends EasyDeLBaseConfig
- def: [`easydel/modules/whisper/whisper_configuration.py:26`](../../../../../../../raw/code/EasyDeL/easydel/modules/whisper/whisper_configuration.py#L26)
- doc: Configuration objects inherit from \[`EasyDeLBaseConfig`\] and can be used to control the model outputs. Read
- signature: `class WhisperConfig(EasyDeLBaseConfig):`
- members:
  - `__init__(self, vocab_size: int = 51865, num_mel_bins: int = 80, encoder_layers: int = 4, encoder_attention_heads: int = 6, decoder_layers: int = 4, decoder_attention_heads: int = 6, decoder_ffn_dim: int = 1536, encoder_ffn_dim: int = 1536, encoder_layerdrop: float = 0, decoder_layerdrop: float = 0, decoder_start_token_id: int = 50257, use_cache: bool = True, is_encoder_decoder: bool = True, activation_function: str = "gelu", d_model: int = 384, dropout: float = 0, attention_dropout: float = 0, activation_dropout: float = 0, init_std: float = 0.02, scale_embedding: bool = False, max_source_positions: int = 1500, max_target_positions: int = 448, pad_token_id: int = 50256, bos_token_id: int = 50256, eos_token_id: int = 50256, suppress_tokens: list[int] | None = None, begin_suppress_tokens: list[int] | None = None, use_weighted_layer_sum: bool = False, classifier_proj_size: int = 256, apply_spec_augment: bool = False, mask_time_prob: float = 0.05, mask_time_length: int = 10, mask_time_min_masks: int = 2, mask_feature_prob: float = 0, mask_feature_length: int = 10, mask_feature_min_masks: int = 0, median_filter_width: int = 7, bits: int | None = None, gradient_checkpointing: EasyDeLGradientCheckPointers = EasyDeLGradientCheckPointers.NONE, **kwargs)` — [`L113`](../../../../../../../raw/code/EasyDeL/easydel/modules/whisper/whisper_configuration.py#L113) — Initializes the WhisperConfig object.
  - `get_partition_rules(self, *args, **kwargs)` — [`L252`](../../../../../../../raw/code/EasyDeL/easydel/modules/whisper/whisper_configuration.py#L252) — Returns partition rules for model sharding.
  - `activation_dropout` — [`L211`](../../../../../../../raw/code/EasyDeL/easydel/modules/whisper/whisper_configuration.py#L211)
  - `activation_function` — [`L212`](../../../../../../../raw/code/EasyDeL/easydel/modules/whisper/whisper_configuration.py#L212)
  - `apply_spec_augment` — [`L227`](../../../../../../../raw/code/EasyDeL/easydel/modules/whisper/whisper_configuration.py#L227)
  - `attention_dropout` — [`L210`](../../../../../../../raw/code/EasyDeL/easydel/modules/whisper/whisper_configuration.py#L210)
  - `attribute_map` — [`L108`](../../../../../../../raw/code/EasyDeL/easydel/modules/whisper/whisper_configuration.py#L108)
  - `bits` — [`L236`](../../../../../../../raw/code/EasyDeL/easydel/modules/whisper/whisper_configuration.py#L236)
  - `classifier_proj_size` — [`L223`](../../../../../../../raw/code/EasyDeL/easydel/modules/whisper/whisper_configuration.py#L223)
  - `d_model` — [`L202`](../../../../../../../raw/code/EasyDeL/easydel/modules/whisper/whisper_configuration.py#L202)
  - `decoder_attention_heads` — [`L206`](../../../../../../../raw/code/EasyDeL/easydel/modules/whisper/whisper_configuration.py#L206)
  - `decoder_ffn_dim` — [`L207`](../../../../../../../raw/code/EasyDeL/easydel/modules/whisper/whisper_configuration.py#L207)
  - `decoder_layerdrop` — [`L215`](../../../../../../../raw/code/EasyDeL/easydel/modules/whisper/whisper_configuration.py#L215)
  - `decoder_layers` — [`L205`](../../../../../../../raw/code/EasyDeL/easydel/modules/whisper/whisper_configuration.py#L205)
  - `dropout` — [`L209`](../../../../../../../raw/code/EasyDeL/easydel/modules/whisper/whisper_configuration.py#L209)
  - `encoder_attention_heads` — [`L204`](../../../../../../../raw/code/EasyDeL/easydel/modules/whisper/whisper_configuration.py#L204)
  - `encoder_ffn_dim` — [`L208`](../../../../../../../raw/code/EasyDeL/easydel/modules/whisper/whisper_configuration.py#L208)
  - `encoder_layerdrop` — [`L214`](../../../../../../../raw/code/EasyDeL/easydel/modules/whisper/whisper_configuration.py#L214)
  - `encoder_layers` — [`L203`](../../../../../../../raw/code/EasyDeL/easydel/modules/whisper/whisper_configuration.py#L203)
  - `gradient_checkpointing` — [`L237`](../../../../../../../raw/code/EasyDeL/easydel/modules/whisper/whisper_configuration.py#L237)
  - `init_std` — [`L213`](../../../../../../../raw/code/EasyDeL/easydel/modules/whisper/whisper_configuration.py#L213)
  - `mask_feature_length` — [`L232`](../../../../../../../raw/code/EasyDeL/easydel/modules/whisper/whisper_configuration.py#L232)
  - `mask_feature_min_masks` — [`L233`](../../../../../../../raw/code/EasyDeL/easydel/modules/whisper/whisper_configuration.py#L233)
  - `mask_feature_prob` — [`L231`](../../../../../../../raw/code/EasyDeL/easydel/modules/whisper/whisper_configuration.py#L231)
  - `mask_time_length` — [`L229`](../../../../../../../raw/code/EasyDeL/easydel/modules/whisper/whisper_configuration.py#L229)
  - `mask_time_min_masks` — [`L230`](../../../../../../../raw/code/EasyDeL/easydel/modules/whisper/whisper_configuration.py#L230)
  - `mask_time_prob` — [`L228`](../../../../../../../raw/code/EasyDeL/easydel/modules/whisper/whisper_configuration.py#L228)
  - `max_position_embeddings` — [`L238`](../../../../../../../raw/code/EasyDeL/easydel/modules/whisper/whisper_configuration.py#L238)
  - `max_source_positions` — [`L219`](../../../../../../../raw/code/EasyDeL/easydel/modules/whisper/whisper_configuration.py#L219)
  - `max_target_positions` — [`L220`](../../../../../../../raw/code/EasyDeL/easydel/modules/whisper/whisper_configuration.py#L220)
  - `median_filter_width` — [`L235`](../../../../../../../raw/code/EasyDeL/easydel/modules/whisper/whisper_configuration.py#L235)
  - `model_type` — [`L107`](../../../../../../../raw/code/EasyDeL/easydel/modules/whisper/whisper_configuration.py#L107)
  - `num_hidden_layers` — [`L217`](../../../../../../../raw/code/EasyDeL/easydel/modules/whisper/whisper_configuration.py#L217)
  - `num_mel_bins` — [`L201`](../../../../../../../raw/code/EasyDeL/easydel/modules/whisper/whisper_configuration.py#L201)
  - `scale_embedding` — [`L218`](../../../../../../../raw/code/EasyDeL/easydel/modules/whisper/whisper_configuration.py#L218)
  - `use_cache` — [`L216`](../../../../../../../raw/code/EasyDeL/easydel/modules/whisper/whisper_configuration.py#L216)
  - `use_weighted_layer_sum` — [`L224`](../../../../../../../raw/code/EasyDeL/easydel/modules/whisper/whisper_configuration.py#L224)
  - `vocab_size` — [`L200`](../../../../../../../raw/code/EasyDeL/easydel/modules/whisper/whisper_configuration.py#L200)
- uses (calls/refs, reference-scoped): [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`register_config`](../../infra/factory.md#register_config), [`__init__`](../../infra/base_config.md#EasyDeLBaseConfig.__init__), [`EasyDeLGradientCheckPointers`](../../infra/etils.md#EasyDeLGradientCheckPointers), [`NONE`](../../infra/etils.md#EasyDeLGradientCheckPointers.NONE)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`get_partition_rules`](../../infra/base_config.md#EasyDeLBaseConfig.get_partition_rules), [`__all__`](modeling_whisper.md#__all__), [`encoder_attn_layer_norm`](modeling_whisper.md#WhisperDecoderLayer.encoder_attn_layer_norm), [`WhisperForConditionalGeneration`](modeling_whisper.md#WhisperForConditionalGeneration), [`self_attn`](modeling_whisper.md#WhisperEncoderLayer.self_attn), [`embed_positions`](modeling_whisper.md#WhisperDecoder.embed_positions), [`WhisperForAudioClassification`](modeling_whisper.md#WhisperForAudioClassification), [`WhisperModel`](modeling_whisper.md#WhisperModel), [`dropout_layer`](modeling_whisper.md#WhisperEncoder.dropout_layer), [`encoder_attn`](modeling_whisper.md#WhisperDecoderLayer.encoder_attn), [`self_attn`](modeling_whisper.md#WhisperDecoderLayer.self_attn), [`encoder`](modeling_whisper.md#WhisperForAudioClassification.encoder), [`__init__`](modeling_whisper.md#WhisperForConditionalGeneration.__init__), [`embed_dim`](modeling_whisper.md#WhisperDecoderLayer.embed_dim), [`embed_dim`](modeling_whisper.md#WhisperEncoderLayer.embed_dim), [`activation_fn`](modeling_whisper.md#WhisperDecoderLayer.activation_fn), [`activation_fn`](modeling_whisper.md#WhisperEncoderLayer.activation_fn), [`attention_performer`](modeling_whisper.md#WhisperAttention.attention_performer), [`fc1`](modeling_whisper.md#WhisperDecoderLayer.fc1), [`fc1`](modeling_whisper.md#WhisperEncoderLayer.fc1), [`fc2`](modeling_whisper.md#WhisperDecoderLayer.fc2), [`fc2`](modeling_whisper.md#WhisperEncoderLayer.fc2), [`projector`](modeling_whisper.md#WhisperForAudioClassification.projector), [`dropout_layer`](modeling_whisper.md#WhisperDecoderLayer.dropout_layer), [`dropout_layer`](modeling_whisper.md#WhisperEncoderLayer.dropout_layer), [`activation_dropout_layer`](modeling_whisper.md#WhisperDecoderLayer.activation_dropout_layer), [`activation_dropout_layer`](modeling_whisper.md#WhisperEncoderLayer.activation_dropout_layer), [`classifier`](modeling_whisper.md#WhisperForAudioClassification.classifier), [`__init__`](modeling_whisper.md#WhisperAttention.__init__), [`__init__`](modeling_whisper.md#WhisperDecoder.__init__), [`__init__`](modeling_whisper.md#WhisperEncoder.__init__), [`__init__`](modeling_whisper.md#WhisperForAudioClassification.__init__), [`__init__`](modeling_whisper.md#WhisperModel.__init__), [`__init__`](modeling_whisper.md#WhisperDecoderLayer.__init__), [`__init__`](modeling_whisper.md#WhisperEncoderLayer.__init__), [`_config_class`](modeling_whisper.md#WhisperForConditionalGeneration._config_class)

