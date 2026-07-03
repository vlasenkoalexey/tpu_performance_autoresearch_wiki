---
title: 'Module: easydel/modules/phimoe/phimoe_configuration.py'
type: catalog
provenance: extracted
module: easydel/modules/phimoe/phimoe_configuration.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.phimoe.phimoe_configuration`/
symbols:
  PhiMoeConfig.rope_scaling: PhiMoeConfig#rope_scaling.
  PhiMoeConfig: PhiMoeConfig#
  PhiMoeConfig.get_mask_details: PhiMoeConfig#get_mask_details().
  PhiMoeConfig.layer_types: PhiMoeConfig#layer_types.
  PhiMoeConfig.hidden_size: PhiMoeConfig#hidden_size.
  PhiMoeConfig._rope_scaling_validation: PhiMoeConfig#_rope_scaling_validation().
  PhiMoeConfig.num_local_experts: PhiMoeConfig#num_local_experts.
  PhiMoeConfig.__init__: PhiMoeConfig#__init__().
  PhiMoeConfig.num_attention_heads: PhiMoeConfig#num_attention_heads.
  _patch_hf_phimoe_rotary_mscale: _patch_hf_phimoe_rotary_mscale().
  PhiMoeConfig.sliding_window: PhiMoeConfig#sliding_window.
  PhiMoeConfig.rms_norm_eps: PhiMoeConfig#rms_norm_eps.
  PhiMoeConfig.original_max_position_embeddings: PhiMoeConfig#original_max_position_embeddings.
  PhiMoeConfig.initializer_range: PhiMoeConfig#initializer_range.
  PhiMoeConfig.intermediate_size: PhiMoeConfig#intermediate_size.
  PhiMoeConfig.num_experts_per_tok: PhiMoeConfig#num_experts_per_tok.
  PhiMoeConfig.vocab_size: PhiMoeConfig#vocab_size.
  _patch_hf_phimoe_rotary_mscale._patched_init: _patch_hf_phimoe_rotary_mscale()._patched_init().
  PhiMoeConfig.num_hidden_layers: PhiMoeConfig#num_hidden_layers.
  PhiMoeConfig.hidden_act: PhiMoeConfig#hidden_act.
  PhiMoeConfig.router_jitter_noise: PhiMoeConfig#router_jitter_noise.
  PhiMoeConfig.input_jitter_noise: PhiMoeConfig#input_jitter_noise.
  PhiMoeConfig.embd_pdrop: PhiMoeConfig#embd_pdrop.
  PhiMoeConfig.gradient_checkpointing: PhiMoeConfig#gradient_checkpointing.
  PhiMoeConfig.lm_head_bias: PhiMoeConfig#lm_head_bias.
  PhiMoeConfig.model_type: PhiMoeConfig#model_type.
  PhiMoeConfig.max_position_embeddings: PhiMoeConfig#max_position_embeddings.
  PhiMoeConfig.attention_bias: PhiMoeConfig#attention_bias.
  PhiMoeConfig.num_key_value_heads: PhiMoeConfig#num_key_value_heads.
  PhiMoeConfig.head_dim: PhiMoeConfig#head_dim.
  PhiMoeConfig.use_cache: PhiMoeConfig#use_cache.
  PhiMoeConfig.rope_theta: PhiMoeConfig#rope_theta.
  PhiMoeConfig.attention_dropout: PhiMoeConfig#attention_dropout.
  PhiMoeConfig.output_router_logits: PhiMoeConfig#output_router_logits.
  PhiMoeConfig.router_aux_loss_coef: PhiMoeConfig#router_aux_loss_coef.
  PhiMoeConfig.bits: PhiMoeConfig#bits.
  PhiMoeConfig.get_partition_rules: PhiMoeConfig#get_partition_rules().
---
# Module: [`easydel/modules/phimoe/phimoe_configuration.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/phimoe_configuration.py)

## Classes
### `PhiMoeConfig`  ·  implements/extends EasyDeLBaseConfig
- def: [`easydel/modules/phimoe/phimoe_configuration.py:55`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/phimoe_configuration.py#L55)
- doc: Configuration objects inherit from \[`EasyDeLBaseConfig`\] and can be used to control the model outputs. Read
- signature: `class PhiMoeConfig(EasyDeLBaseConfig):`
- members:
  - `__init__(self, vocab_size=32064, hidden_size=4096, intermediate_size=6400, num_hidden_layers=32, num_attention_heads=32, num_key_value_heads: int | None = 8, head_dim: int | None = None, hidden_act="silu", max_position_embeddings=4096 * 32, initializer_range=0.02, rms_norm_eps=0.00001, use_cache=True, pad_token_id=None, bos_token_id=1, eos_token_id=2, tie_word_embeddings=False, rope_theta=1000000, rope_scaling=None, sliding_window=None, attention_dropout=0, num_experts_per_tok=2, num_local_experts=16, output_router_logits=False, router_aux_loss_coef=0.001, router_jitter_noise=0.01, input_jitter_noise=0, attention_bias=False, embd_pdrop: float = 0, lm_head_bias=False, bits: int | None = None, layer_types: list[str] | None = None, gradient_checkpointing: EasyDeLGradientCheckPointers = EasyDeLGradientCheckPointers.NONE, **kwargs)` — [`L135`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/phimoe_configuration.py#L135) — Initialize PhiMoeConfig with MoE architecture hyperparameters.
  - `_rope_scaling_validation(self)` — [`L238`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/phimoe_configuration.py#L238) — Validate the `rope_scaling` configuration.
  - `get_mask_details(self)` — [`L315`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/phimoe_configuration.py#L315) — Retrieve attention mask details for each layer in the model.
  - `get_partition_rules(self, *args, **kwargs)` — [`L225`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/phimoe_configuration.py#L225) — Returns partition rules for model sharding.
  - `attention_bias` — [`L182`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/phimoe_configuration.py#L182)
  - `attention_dropout` — [`L195`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/phimoe_configuration.py#L195)
  - `bits` — [`L208`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/phimoe_configuration.py#L208)
  - `embd_pdrop` — [`L203`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/phimoe_configuration.py#L203)
  - `gradient_checkpointing` — [`L209`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/phimoe_configuration.py#L209)
  - `head_dim` — [`L189`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/phimoe_configuration.py#L189)
  - `hidden_act` — [`L190`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/phimoe_configuration.py#L190)
  - `hidden_size` — [`L177`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/phimoe_configuration.py#L177)
  - `initializer_range` — [`L191`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/phimoe_configuration.py#L191)
  - `input_jitter_noise` — [`L202`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/phimoe_configuration.py#L202)
  - `intermediate_size` — [`L178`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/phimoe_configuration.py#L178)
  - `layer_types` — [`L210`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/phimoe_configuration.py#L210)
  - `lm_head_bias` — [`L183`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/phimoe_configuration.py#L183)
  - `max_position_embeddings` — [`L176`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/phimoe_configuration.py#L176)
  - `model_type` — [`L133`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/phimoe_configuration.py#L133)
  - `num_attention_heads` — [`L180`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/phimoe_configuration.py#L180)
  - `num_experts_per_tok` — [`L197`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/phimoe_configuration.py#L197)
  - `num_hidden_layers` — [`L179`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/phimoe_configuration.py#L179)
  - `num_key_value_heads` — [`L188`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/phimoe_configuration.py#L188)
  - `num_local_experts` — [`L198`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/phimoe_configuration.py#L198)
  - `original_max_position_embeddings` — [`L207`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/phimoe_configuration.py#L207)
  - `output_router_logits` — [`L199`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/phimoe_configuration.py#L199)
  - `rms_norm_eps` — [`L192`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/phimoe_configuration.py#L192)
  - `rope_scaling` — [`L204`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/phimoe_configuration.py#L204)
  - `rope_theta` — [`L194`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/phimoe_configuration.py#L194)
  - `router_aux_loss_coef` — [`L200`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/phimoe_configuration.py#L200)
  - `router_jitter_noise` — [`L201`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/phimoe_configuration.py#L201)
  - `sliding_window` — [`L181`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/phimoe_configuration.py#L181)
  - `use_cache` — [`L193`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/phimoe_configuration.py#L193)
  - `vocab_size` — [`L175`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/phimoe_configuration.py#L175)
- uses (calls/refs, reference-scoped): [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`register_config`](../../infra/factory.md#register_config), [`__init__`](../../infra/base_config.md#EasyDeLBaseConfig.__init__), [`EasyDeLGradientCheckPointers`](../../infra/etils.md#EasyDeLGradientCheckPointers), [`AttnMaskDetail`](../../infra/utils.md#AttnMaskDetail), [`AttnMaskType`](../../infra/utils.md#AttnMaskType), [`NONE`](../../infra/etils.md#EasyDeLGradientCheckPointers.NONE), [`from_hf`](../../infra/utils.md#AttnMaskType.from_hf)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`get_partition_rules`](../../infra/base_config.md#EasyDeLBaseConfig.get_partition_rules), [`get_mask_details`](../../infra/base_config.md#EasyDeLBaseConfig.get_mask_details), [`__call__`](modeling_phimoe.md#PhiMoeSparseMoeBlock.__call__), [`PhiMoeForCausalLM`](modeling_phimoe.md#PhiMoeForCausalLM), [`PhiMoeModel`](modeling_phimoe.md#PhiMoeModel), [`__init__`](modeling_phimoe.md#PhiMoEAttention.__init__), [`embed_dropout`](modeling_phimoe.md#PhiMoeModel.embed_dropout), [`precision`](modeling_phimoe.md#PhiMoEBlockSparseTop2MLP.precision), [`gate`](modeling_phimoe.md#PhiMoeSparseMoeBlock.gate), [`__init__`](modeling_phimoe.md#PhiMoeForCausalLM.__init__), [`embed_tokens`](modeling_phimoe.md#PhiMoeModel.embed_tokens), [`experts`](modeling_phimoe.md#PhiMoeSparseMoeBlock.experts), [`act_fn`](modeling_phimoe.md#PhiMoEBlockSparseTop2MLP.act_fn), [`input_layernorm`](modeling_phimoe.md#PhiMoeDecoderLayer.input_layernorm), [`norm`](modeling_phimoe.md#PhiMoeModel.norm), [`post_attention_layernorm`](modeling_phimoe.md#PhiMoeDecoderLayer.post_attention_layernorm), [`__init__`](modeling_phimoe.md#PhiMoeModel.__init__), [`router_jitter_noise`](modeling_phimoe.md#PhiMoeSparseMoeBlock.router_jitter_noise), [`__init__`](modeling_phimoe.md#PhiMoEBlockSparseTop2MLP.__init__), [`__init__`](modeling_phimoe.md#PhiMoeDecoderLayer.__init__), [`__init__`](modeling_phimoe.md#PhiMoeSparseMoeBlock.__init__), [`_config_class`](modeling_phimoe.md#PhiMoeForCausalLM._config_class), [`ffn_dim`](modeling_phimoe.md#PhiMoeSparseMoeBlock.ffn_dim), [`hidden_dim`](modeling_phimoe.md#PhiMoeSparseMoeBlock.hidden_dim), [`input_jitter_noise`](modeling_phimoe.md#PhiMoeSparseMoeBlock.input_jitter_noise), [`num_experts`](modeling_phimoe.md#PhiMoeSparseMoeBlock.num_experts), [`precision`](modeling_phimoe.md#PhiMoeDecoderLayer.precision), [`top_k`](modeling_phimoe.md#PhiMoeSparseMoeBlock.top_k), [`vocab_size`](modeling_phimoe.md#PhiMoeModel.vocab_size)

## Functions
- `_patch_hf_phimoe_rotary_mscale()` — [`L24`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/phimoe_configuration.py#L24) — HF compatibility: initialize missing Phimoe rotary mscale attributes.
- `_patched_init(self, config, device=None)` — [`L39`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/phimoe_configuration.py#L39)

