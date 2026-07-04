---
title: 'Module: easydel/modules/qwen3_next/qwen3_next_configuration.py'
type: catalog
provenance: extracted
module: easydel/modules/qwen3_next/qwen3_next_configuration.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.qwen3_next.qwen3_next_configuration`/
symbols:
  Qwen3NextConfig: Qwen3NextConfig#
  Qwen3NextConfig.hidden_size: Qwen3NextConfig#hidden_size.
  Qwen3NextConfig.initializer_range: Qwen3NextConfig#initializer_range.
  Qwen3NextConfig.layer_types: Qwen3NextConfig#layer_types.
  Qwen3NextConfig.linear_d_inner: Qwen3NextConfig#linear_d_inner().
  Qwen3NextConfig.is_moe_layer: Qwen3NextConfig#is_moe_layer().
  Qwen3NextConfig.rms_norm_eps: Qwen3NextConfig#rms_norm_eps.
  _patch_hf_qwen3_next_load_balancing_loss: _patch_hf_qwen3_next_load_balancing_loss().
  Qwen3NextConfig.mlp_only_layers: Qwen3NextConfig#mlp_only_layers.
  Qwen3NextConfig.vocab_size: Qwen3NextConfig#vocab_size.
  Qwen3NextConfig.num_experts: Qwen3NextConfig#num_experts.
  Qwen3NextConfig.rotary_dim: Qwen3NextConfig#rotary_dim().
  Qwen3NextConfig.get_partition_rules: Qwen3NextConfig#get_partition_rules().
  _patch_hf_qwen3_next_load_balancing_loss._patched_load_balancing_loss_func: _patch_hf_qwen3_next_load_balancing_loss()._patched_load_balancing_loss_func().
  Qwen3NextConfig.num_hidden_layers: Qwen3NextConfig#num_hidden_layers.
  Qwen3NextConfig.hidden_act: Qwen3NextConfig#hidden_act.
  Qwen3NextConfig.rope_scaling: Qwen3NextConfig#rope_scaling.
  Qwen3NextConfig.is_full_attention_layer: Qwen3NextConfig#is_full_attention_layer().
  Qwen3NextConfig.intermediate_size: Qwen3NextConfig#intermediate_size.
  Qwen3NextConfig.head_dim: Qwen3NextConfig#head_dim.
  Qwen3NextConfig.moe_intermediate_size: Qwen3NextConfig#moe_intermediate_size.
  Qwen3NextConfig.linear_value_head_dim: Qwen3NextConfig#linear_value_head_dim.
  Qwen3NextConfig.linear_conv_kernel_dim: Qwen3NextConfig#linear_conv_kernel_dim.
  Qwen3NextConfig.linear_d_state: Qwen3NextConfig#linear_d_state().
  Qwen3NextConfig.num_attention_heads: Qwen3NextConfig#num_attention_heads.
  Qwen3NextConfig.num_key_value_heads: Qwen3NextConfig#num_key_value_heads.
  Qwen3NextConfig.max_position_embeddings: Qwen3NextConfig#max_position_embeddings.
  Qwen3NextConfig.use_cache: Qwen3NextConfig#use_cache.
  Qwen3NextConfig.rope_theta: Qwen3NextConfig#rope_theta.
  Qwen3NextConfig.attention_bias: Qwen3NextConfig#attention_bias.
  Qwen3NextConfig.attention_dropout: Qwen3NextConfig#attention_dropout.
  Qwen3NextConfig.linear_num_key_heads: Qwen3NextConfig#linear_num_key_heads.
  Qwen3NextConfig.linear_num_value_heads: Qwen3NextConfig#linear_num_value_heads.
  Qwen3NextConfig.linear_key_head_dim: Qwen3NextConfig#linear_key_head_dim.
  _ensure_loss_tensor: _ensure_loss_tensor().
  _patch_hf_qwen3_next_load_balancing_loss._patched_get_seq_length: _patch_hf_qwen3_next_load_balancing_loss()._patched_get_seq_length().
  Qwen3NextConfig.__init__: Qwen3NextConfig#__init__().
  Qwen3NextConfig.num_experts_per_tok: Qwen3NextConfig#num_experts_per_tok.
  Qwen3NextConfig.norm_topk_prob: Qwen3NextConfig#norm_topk_prob.
  Qwen3NextConfig.shared_expert_intermediate_size: Qwen3NextConfig#shared_expert_intermediate_size.
  Qwen3NextConfig.partial_rotary_factor: Qwen3NextConfig#partial_rotary_factor.
  Qwen3NextConfig.full_attention_interval: Qwen3NextConfig#full_attention_interval.
  Qwen3NextConfig.decoder_sparse_step: Qwen3NextConfig#decoder_sparse_step.
  logger: logger.
  Qwen3NextConfig.model_type: Qwen3NextConfig#model_type.
  Qwen3NextConfig.output_router_logits: Qwen3NextConfig#output_router_logits.
  Qwen3NextConfig.router_aux_loss_coef: Qwen3NextConfig#router_aux_loss_coef.
  __all__: __all__.
---
# Module: [`easydel/modules/qwen3_next/qwen3_next_configuration.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_next/qwen3_next_configuration.py)

## Classes
### `Qwen3NextConfig`  ·  implements/extends EasyDeLBaseConfig
- def: [`easydel/modules/qwen3_next/qwen3_next_configuration.py:105`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_next/qwen3_next_configuration.py#L105)
- doc: Configuration for Qwen3Next - a hybrid attention model with GatedDeltaRule.
- signature: `class Qwen3NextConfig(EasyDeLBaseConfig):`
- members:
  - `__init__(self, vocab_size: int = 151936, hidden_size: int = 2048, intermediate_size: int = 5632, num_hidden_layers: int = 48, num_attention_heads: int = 16, num_key_value_heads: int = 2, head_dim: int = 256, hidden_act: str = "silu", max_position_embeddings: int = 32768, initializer_range: float = 0.02, rms_norm_eps: float = 0.000001, use_cache: bool = True, tie_word_embeddings: bool = False, rope_theta: float = 10000, rope_scaling: dict | None = None, attention_bias: bool = False, attention_dropout: float = 0, partial_rotary_factor: float = 0.25, layer_types: list[str] | None = None, full_attention_interval: int = 4, linear_conv_kernel_dim: int = 4, linear_key_head_dim: int = 128, linear_value_head_dim: int = 128, linear_num_key_heads: int = 16, linear_num_value_heads: int = 32, decoder_sparse_step: int = 1, moe_intermediate_size: int = 512, shared_expert_intermediate_size: int = 512, num_experts_per_tok: int = 10, num_experts: int = 512, norm_topk_prob: bool = True, output_router_logits: bool = False, router_aux_loss_coef: float = 0.001, mlp_only_layers: list[int] | None = None, **kwargs)` — [`L158`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_next/qwen3_next_configuration.py#L158) — Initialize Qwen3NextConfig with hybrid attention and MoE hyperparameters.
  - `get_partition_rules(self, *args, **kwargs)` — [`L270`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_next/qwen3_next_configuration.py#L270) — Returns partition rules for model sharding.
  - `is_full_attention_layer(self, layer_idx: int)` — [`L283`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_next/qwen3_next_configuration.py#L283) — Check if a layer uses full attention.
  - `is_moe_layer(self, layer_idx: int)` — [`L294`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_next/qwen3_next_configuration.py#L294) — Check if a layer uses MoE FFN.
  - `linear_d_inner(self)` — [`L254`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_next/qwen3_next_configuration.py#L254) — Return the inner dimension for linear attention convolution state.
  - `linear_d_state(self)` — [`L266`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_next/qwen3_next_configuration.py#L266) — Return the state dimension for linear attention recurrence.
  - `rotary_dim(self)` — [`L249`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_next/qwen3_next_configuration.py#L249) — Return the dimension used for rotary embeddings (partial RoPE).
  - `attention_bias` — [`L214`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_next/qwen3_next_configuration.py#L214)
  - `attention_dropout` — [`L215`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_next/qwen3_next_configuration.py#L215)
  - `decoder_sparse_step` — [`L233`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_next/qwen3_next_configuration.py#L233)
  - `full_attention_interval` — [`L219`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_next/qwen3_next_configuration.py#L219)
  - `head_dim` — [`L206`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_next/qwen3_next_configuration.py#L206)
  - `hidden_act` — [`L207`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_next/qwen3_next_configuration.py#L207)
  - `hidden_size` — [`L201`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_next/qwen3_next_configuration.py#L201)
  - `initializer_range` — [`L209`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_next/qwen3_next_configuration.py#L209)
  - `intermediate_size` — [`L202`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_next/qwen3_next_configuration.py#L202)
  - `layer_types` — [`L220`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_next/qwen3_next_configuration.py#L220)
  - `linear_conv_kernel_dim` — [`L227`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_next/qwen3_next_configuration.py#L227)
  - `linear_key_head_dim` — [`L228`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_next/qwen3_next_configuration.py#L228)
  - `linear_num_key_heads` — [`L230`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_next/qwen3_next_configuration.py#L230)
  - `linear_num_value_heads` — [`L231`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_next/qwen3_next_configuration.py#L231)
  - `linear_value_head_dim` — [`L229`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_next/qwen3_next_configuration.py#L229)
  - `max_position_embeddings` — [`L208`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_next/qwen3_next_configuration.py#L208)
  - `mlp_only_layers` — [`L241`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_next/qwen3_next_configuration.py#L241)
  - `model_type` — [`L156`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_next/qwen3_next_configuration.py#L156)
  - `moe_intermediate_size` — [`L234`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_next/qwen3_next_configuration.py#L234)
  - `norm_topk_prob` — [`L238`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_next/qwen3_next_configuration.py#L238)
  - `num_attention_heads` — [`L204`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_next/qwen3_next_configuration.py#L204)
  - `num_experts` — [`L237`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_next/qwen3_next_configuration.py#L237)
  - `num_experts_per_tok` — [`L236`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_next/qwen3_next_configuration.py#L236)
  - `num_hidden_layers` — [`L203`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_next/qwen3_next_configuration.py#L203)
  - `num_key_value_heads` — [`L205`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_next/qwen3_next_configuration.py#L205)
  - `output_router_logits` — [`L239`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_next/qwen3_next_configuration.py#L239)
  - `partial_rotary_factor` — [`L217`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_next/qwen3_next_configuration.py#L217)
  - `rms_norm_eps` — [`L210`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_next/qwen3_next_configuration.py#L210)
  - `rope_scaling` — [`L213`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_next/qwen3_next_configuration.py#L213)
  - `rope_theta` — [`L212`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_next/qwen3_next_configuration.py#L212)
  - `router_aux_loss_coef` — [`L240`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_next/qwen3_next_configuration.py#L240)
  - `shared_expert_intermediate_size` — [`L235`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_next/qwen3_next_configuration.py#L235)
  - `use_cache` — [`L211`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_next/qwen3_next_configuration.py#L211)
  - `vocab_size` — [`L200`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_next/qwen3_next_configuration.py#L200)
- uses (calls/refs, reference-scoped): [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`register_config`](../../infra/factory.md#register_config), [`__init__`](../../infra/base_config.md#EasyDeLBaseConfig.__init__), [`Qwen3_5TextConfig`](../qwen3_5/qwen3_5_configuration.md#Qwen3_5TextConfig), [`Qwen3_5MoeTextConfig`](../qwen3_5_moe/qwen3_5_moe_configuration.md#Qwen3_5MoeTextConfig), [`get_partition_rules`](../qwen3_5/qwen3_5_configuration.md#Qwen3_5TextConfig.get_partition_rules), [`get_partition_rules`](../qwen3_5_moe/qwen3_5_moe_configuration.md#Qwen3_5MoeTextConfig.get_partition_rules), [`is_moe_layer`](../qwen3_5/qwen3_5_configuration.md#Qwen3_5TextConfig.is_moe_layer)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`get_partition_rules`](../../infra/base_config.md#EasyDeLBaseConfig.get_partition_rules), [`__call__`](modeling_qwen3_next.md#Qwen3NextLinearAttention.__call__), [`__init__`](../qwen3_5/modeling_qwen3_5.md#Qwen3_5Model.__init__), [`__init__`](../qwen3_5_moe/modeling_qwen3_5_moe.md#Qwen3_5MoeModel.__init__), [`__init__`](modeling_qwen3_next.md#Qwen3NextSparseMoeBlock.__init__), [`Qwen3NextModel`](modeling_qwen3_next.md#Qwen3NextModel), [`Qwen3NextForCausalLM`](modeling_qwen3_next.md#Qwen3NextForCausalLM), [`embed_tokens`](modeling_qwen3_next.md#Qwen3NextModel.embed_tokens), [`num_v_heads`](modeling_qwen3_next.md#Qwen3NextLinearAttention.num_v_heads), [`Qwen3_5TextConfig`](../qwen3_5/qwen3_5_configuration.md#Qwen3_5TextConfig), [`down_proj`](modeling_qwen3_next.md#Qwen3NextMLPStack.down_proj), [`gate_proj`](modeling_qwen3_next.md#Qwen3NextMLPStack.gate_proj), [`up_proj`](modeling_qwen3_next.md#Qwen3NextMLPStack.up_proj), [`Qwen3_5MoeTextConfig`](../qwen3_5_moe/qwen3_5_moe_configuration.md#Qwen3_5MoeTextConfig), [`in_proj_a`](modeling_qwen3_next.md#Qwen3NextLinearAttention.in_proj_a), [`in_proj_qkv`](modeling_qwen3_next.md#Qwen3NextLinearAttention.in_proj_qkv), [`head_v_dim`](modeling_qwen3_next.md#Qwen3NextLinearAttention.head_v_dim), [`out_proj`](modeling_qwen3_next.md#Qwen3NextLinearAttention.out_proj), [`gate`](modeling_qwen3_next.md#Qwen3NextSparseMoeBlock.gate), [`in_proj_b`](modeling_qwen3_next.md#Qwen3NextLinearAttention.in_proj_b), [`in_proj_qkvz`](modeling_qwen3_next.md#Qwen3NextLinearAttention.in_proj_qkvz), [`in_proj_z`](modeling_qwen3_next.md#Qwen3NextLinearAttention.in_proj_z), [`num_k_heads`](modeling_qwen3_next.md#Qwen3NextLinearAttention.num_k_heads), [`precision`](modeling_qwen3_next.md#Qwen3NextMLP.precision), [`head_k_dim`](modeling_qwen3_next.md#Qwen3NextLinearAttention.head_k_dim), [`norm`](modeling_qwen3_next.md#Qwen3NextLinearAttention.norm), [`in_proj_ba`](modeling_qwen3_next.md#Qwen3NextLinearAttention.in_proj_ba), [`input_layernorm`](modeling_qwen3_next.md#Qwen3NextDecoderLayer.input_layernorm), [`norm`](modeling_qwen3_next.md#Qwen3NextModel.norm), [`post_attention_layernorm`](modeling_qwen3_next.md#Qwen3NextDecoderLayer.post_attention_layernorm), [`shared_expert_gate`](modeling_qwen3_next.md#Qwen3NextSparseMoeBlock.shared_expert_gate), [`conv1d`](modeling_qwen3_next.md#Qwen3NextLinearAttention.conv1d), [`__init__`](modeling_qwen3_next.md#Qwen3NextForCausalLM.__init__), [`act_fn`](modeling_qwen3_next.md#Qwen3NextMLPStack.act_fn), [`is_moe`](modeling_qwen3_next.md#Qwen3NextDecoderLayer.is_moe), [`act_fn`](modeling_qwen3_next.md#Qwen3NextMLP.act_fn), [`shared_expert`](modeling_qwen3_next.md#Qwen3NextSparseMoeBlock.shared_expert), [`__init__`](../qwen3_5/qwen3_5_configuration.md#Qwen3_5TextConfig.__init__)  (+15 more)

## Functions
- `_ensure_loss_tensor(result, gate_logits)` — [`L26`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_next/qwen3_next_configuration.py#L26) — Wrap a plain Python numeric loss in a torch tensor on the right device.
- `_patch_hf_qwen3_next_load_balancing_loss()` — [`L38`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_next/qwen3_next_configuration.py#L38) — HF compatibility: guard Qwen3-Next aux-loss mask shape regressions.
- `_patched_get_seq_length(self, layer_idx: int | None = 0)` — [`L92`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_next/qwen3_next_configuration.py#L92)
- `_patched_load_balancing_loss_func(gate_logits, num_experts=None, top_k=2, attention_mask=None)` — [`L49`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_next/qwen3_next_configuration.py#L49)

## Module values
- `__all__` — [`L308`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_next/qwen3_next_configuration.py#L308)
- `logger` — [`L23`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_next/qwen3_next_configuration.py#L23)

