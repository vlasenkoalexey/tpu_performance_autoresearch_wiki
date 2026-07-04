---
title: 'Module: easydel/modules/llama/llama_configuration.py'
type: catalog
provenance: extracted
module: easydel/modules/llama/llama_configuration.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.llama.llama_configuration`/
symbols:
  LlamaConfig: LlamaConfig#
  LlamaConfig.layer_types: LlamaConfig#layer_types.
  LlamaConfig.__init__: LlamaConfig#__init__().
  LlamaConfig.hidden_size: LlamaConfig#hidden_size.
  VisionLlamaConfig: VisionLlamaConfig#
  LlamaConfig.intermediate_size: LlamaConfig#intermediate_size.
  LlamaConfig.get_partition_rules: LlamaConfig#get_partition_rules().
  VisionLlamaConfig.__init__: VisionLlamaConfig#__init__().
  LlamaConfig.initializer_range: LlamaConfig#initializer_range.
  LlamaConfig.rms_norm_eps: LlamaConfig#rms_norm_eps.
  LlamaConfig.mlp_bias: LlamaConfig#mlp_bias.
  LlamaConfig.num_hidden_layers: LlamaConfig#num_hidden_layers.
  LlamaConfig.resid_pdrop: LlamaConfig#resid_pdrop.
  LlamaConfig.gradient_checkpointing: LlamaConfig#gradient_checkpointing.
  LlamaConfig.hidden_act: LlamaConfig#hidden_act.
  LlamaConfig.model_type: LlamaConfig#model_type.
  LlamaConfig.num_key_value_heads: LlamaConfig#num_key_value_heads.
  LlamaConfig.vocab_size: LlamaConfig#vocab_size.
  LlamaConfig.number_rep_kv: LlamaConfig#number_rep_kv.
  LlamaConfig.rope_theta: LlamaConfig#rope_theta.
  LlamaConfig.attention_bias: LlamaConfig#attention_bias.
  LlamaConfig.num_attention_heads: LlamaConfig#num_attention_heads.
  LlamaConfig.max_position_embeddings: LlamaConfig#max_position_embeddings.
  LlamaConfig.use_cache: LlamaConfig#use_cache.
  LlamaConfig.pretraining_tp: LlamaConfig#pretraining_tp.
  LlamaConfig.embd_pdrop: LlamaConfig#embd_pdrop.
  LlamaConfig.attention_dropout: LlamaConfig#attention_dropout.
  LlamaConfig.fcm_min_ratio: LlamaConfig#fcm_min_ratio.
  LlamaConfig.fcm_max_ratio: LlamaConfig#fcm_max_ratio.
  LlamaConfig.rope_scaling: LlamaConfig#rope_scaling.
  LlamaConfig.bits: LlamaConfig#bits.
  LlamaConfig.scan_layers: LlamaConfig#scan_layers.
  LlamaConfig.head_dim: LlamaConfig#head_dim.
  VisionLlamaConfig.vision_vocab_size: VisionLlamaConfig#vision_vocab_size.
  VisionLlamaConfig.tie_vision_embeddings: VisionLlamaConfig#tie_vision_embeddings.
  VisionLlamaConfig.sample_mode: VisionLlamaConfig#sample_mode.
  VisionLlamaConfig.get_partition_rules: VisionLlamaConfig#get_partition_rules().
---
# Module: [`easydel/modules/llama/llama_configuration.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama/llama_configuration.py)

## Classes
### `LlamaConfig`  ·  implements/extends EasyDeLBaseConfig
- def: [`easydel/modules/llama/llama_configuration.py:24`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama/llama_configuration.py#L24)
- doc: Configuration objects inherit from \[`EasyDeLBaseConfig`\] and can be used to control the model outputs. Read
- signature: `class LlamaConfig(EasyDeLBaseConfig):`
- members:
  - `get_partition_rules(self, *args, **kwargs)` — [`L173`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama/llama_configuration.py#L173) — Returns partition rules for model sharding.
  - `attention_bias` — [`L143`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama/llama_configuration.py#L143)
  - `attention_dropout` — [`L151`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama/llama_configuration.py#L151)
  - `bits` — [`L158`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama/llama_configuration.py#L158)
  - `embd_pdrop` — [`L150`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama/llama_configuration.py#L150)
  - `fcm_max_ratio` — [`L156`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama/llama_configuration.py#L156)
  - `fcm_min_ratio` — [`L154`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama/llama_configuration.py#L154)
  - `gradient_checkpointing` — [`L152`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama/llama_configuration.py#L152)
  - `head_dim` — [`L160`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama/llama_configuration.py#L160)
  - `hidden_act` — [`L155`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama/llama_configuration.py#L155)
  - `hidden_size` — [`L138`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama/llama_configuration.py#L138)
  - `initializer_range` — [`L139`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama/llama_configuration.py#L139)
  - `intermediate_size` — [`L140`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama/llama_configuration.py#L140)
  - `layer_types` — [`L161`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama/llama_configuration.py#L161)
  - `max_position_embeddings` — [`L145`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama/llama_configuration.py#L145)
  - `mlp_bias` — [`L153`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama/llama_configuration.py#L153)
  - `model_type` — [`L96`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama/llama_configuration.py#L96)
  - `num_attention_heads` — [`L144`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama/llama_configuration.py#L144)
  - `num_hidden_layers` — [`L141`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama/llama_configuration.py#L141)
  - `num_key_value_heads` — [`L134`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama/llama_configuration.py#L134)
  - `number_rep_kv` — [`L137`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama/llama_configuration.py#L137)
  - `pretraining_tp` — [`L148`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama/llama_configuration.py#L148)
  - `resid_pdrop` — [`L149`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama/llama_configuration.py#L149)
  - `rms_norm_eps` — [`L146`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama/llama_configuration.py#L146)
  - `rope_scaling` — [`L157`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama/llama_configuration.py#L157)
  - `rope_theta` — [`L142`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama/llama_configuration.py#L142)
  - `scan_layers` — [`L159`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama/llama_configuration.py#L159)
  - `use_cache` — [`L147`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama/llama_configuration.py#L147)
  - `vocab_size` — [`L135`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama/llama_configuration.py#L135)
- protocol/private: `__init__`[`L98`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama/llama_configuration.py#L98)
- uses (calls/refs, reference-scoped): [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`register_config`](../../infra/factory.md#register_config), [`__init__`](../../infra/base_config.md#EasyDeLBaseConfig.__init__), [`EasyDeLGradientCheckPointers`](../../infra/etils.md#EasyDeLGradientCheckPointers), [`NONE`](../../infra/etils.md#EasyDeLGradientCheckPointers.NONE), [`VisionLlamaConfig`](llama_configuration.md#VisionLlamaConfig), [`get_partition_rules`](llama_configuration.md#VisionLlamaConfig.get_partition_rules)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`get_partition_rules`](../../infra/base_config.md#EasyDeLBaseConfig.get_partition_rules), [`LlamaModel`](modeling_llama.md#LlamaModel), [`LlamaForCausalLM`](modeling_llama.md#LlamaForCausalLM), [`LlamaForSequenceClassification`](modeling_llama.md#LlamaForSequenceClassification), [`dropout`](modeling_llama.md#LlamaModel.dropout), [`precision`](modeling_llama.md#LlamaMLP.precision), [`act_fn`](modeling_llama.md#LlamaMLP.act_fn), [`input_layernorm`](modeling_llama.md#LlamaDecoderLayer.input_layernorm), [`post_attention_layernorm`](modeling_llama.md#LlamaDecoderLayer.post_attention_layernorm), [`__init__`](modeling_llama.md#LlamaForCausalLM.__init__), [`__init__`](modeling_llama.md#LlamaForSequenceClassification.__init__), [`down_proj`](modeling_llama.md#LlamaMLP.down_proj), [`dropout`](modeling_llama.md#LlamaMLP.dropout), [`gate_proj`](modeling_llama.md#LlamaMLP.gate_proj), [`up_proj`](modeling_llama.md#LlamaMLP.up_proj), [`__init__`](modeling_llama.md#LlamaAttention.__init__), [`__init__`](modeling_llama.md#LlamaModel.__init__), [`VisionLlamaConfig`](llama_configuration.md#VisionLlamaConfig), [`__init__`](llama_configuration.md#VisionLlamaConfig.__init__), [`__init__`](modeling_llama.md#LlamaDecoderLayer.__init__), [`__init__`](modeling_llama.md#LlamaMLP.__init__), [`_config_class`](modeling_llama.md#LlamaForCausalLM._config_class), [`_config_class`](modeling_llama.md#LlamaForSequenceClassification._config_class)

### `VisionLlamaConfig`  ·  implements/extends LlamaConfig
- def: [`easydel/modules/llama/llama_configuration.py:187`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama/llama_configuration.py#L187)
- doc: Configuration for Llama models extended with a discrete vision token vocabulary.
- signature: `class VisionLlamaConfig(LlamaConfig):`
- members:
  - `__init__(self, vision_vocab_size: int = 8448, tie_vision_embeddings: bool = False, sample_mode: str = "all", **kwargs)` — [`L205`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama/llama_configuration.py#L205) — Initialize VisionLlamaConfig for vision-augmented Llama models.
  - `get_partition_rules(self, *args, **kwargs)` — [`L228`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama/llama_configuration.py#L228) — Returns partition rules for model sharding.
  - `sample_mode` — [`L226`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama/llama_configuration.py#L226)
  - `tie_vision_embeddings` — [`L225`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama/llama_configuration.py#L225)
  - `vision_vocab_size` — [`L224`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama/llama_configuration.py#L224)
- uses (calls/refs, reference-scoped): [`LlamaConfig`](llama_configuration.md#LlamaConfig), [`__init__`](llama_configuration.md#LlamaConfig.__init__)
- used by: [`LlamaConfig`](llama_configuration.md#LlamaConfig), [`get_partition_rules`](llama_configuration.md#LlamaConfig.get_partition_rules)

