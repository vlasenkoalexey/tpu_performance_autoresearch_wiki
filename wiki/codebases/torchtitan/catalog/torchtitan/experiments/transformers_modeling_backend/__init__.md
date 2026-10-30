---
title: 'Module: torchtitan/experiments/transformers_modeling_backend/__init__.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/transformers_modeling_backend/__init__.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.transformers_modeling_backend`/
symbols:
  model_registry: model_registry().
  flavors: flavors.
  TitanModelConfig: TitanModelConfig#
  TitanMoeModelConfig: TitanMoeModelConfig#
  TitanModelConfig.dim: TitanModelConfig#dim.
  TitanModelConfig.n_layers: TitanModelConfig#n_layers.
  TitanModelConfig.n_heads: TitanModelConfig#n_heads.
  TitanModelConfig.n_kv_heads: TitanModelConfig#n_kv_heads.
  TitanModelConfig.attn_mask_type: TitanModelConfig#attn_mask_type.
  TitanMoeModelConfig.num_experts: TitanMoeModelConfig#num_experts.
  TitanMoeModelConfig.num_experts_per_tok: TitanMoeModelConfig#num_experts_per_tok.
  TitanMoeModelConfig.moe_intermediate_size: TitanMoeModelConfig#moe_intermediate_size.
  TitanModelConfig.intermediate_size: TitanModelConfig#intermediate_size.
  TitanModelConfig.norm_eps: TitanModelConfig#norm_eps.
  TitanMoeModelConfig.norm_topk_prob: TitanMoeModelConfig#norm_topk_prob.
  TitanMoeModelConfig.num_nextn_predict_layers: TitanMoeModelConfig#num_nextn_predict_layers.
  TitanMoeModelConfig.experts_implementation: TitanMoeModelConfig#experts_implementation.
  __all__: __all__.
  TitanModelConfig.vocab_size: TitanModelConfig#vocab_size.
  TitanModelConfig.rope_theta: TitanModelConfig#rope_theta.
  TitanModelConfig.multiple_of: TitanModelConfig#multiple_of.
  TitanModelConfig.ffn_dim_multiplier: TitanModelConfig#ffn_dim_multiplier.
  TitanModelConfig.max_seq_len: TitanModelConfig#max_seq_len.
  TitanModelConfig.depth_init: TitanModelConfig#depth_init.
  TitanMoeModelConfig.decoder_sparse_step: TitanMoeModelConfig#decoder_sparse_step.
  TitanMoeModelConfig.load_balance_coeff: TitanMoeModelConfig#load_balance_coeff.
  TitanMoeModelConfig.comm_backend: TitanMoeModelConfig#comm_backend.
---
# Module: [`torchtitan/experiments/transformers_modeling_backend/__init__.py`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/__init__.py)

## Classes
### <a id="TitanModelConfig"></a>`TitanModelConfig`
- def: [`torchtitan/experiments/transformers_modeling_backend/__init__.py:22`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/__init__.py#L22)
- doc: Arguments for the base TorchTitan model.
- signature: `class TitanModelConfig:`
- members:
  - <a id="TitanModelConfig.attn_mask_type"></a>`attn_mask_type` — [`L51`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/__init__.py#L51) — ---
  - <a id="TitanModelConfig.depth_init"></a>`depth_init` — [`L50`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/__init__.py#L50)
  - <a id="TitanModelConfig.dim"></a>`dim` — [`L34`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/__init__.py#L34)
  - <a id="TitanModelConfig.ffn_dim_multiplier"></a>`ffn_dim_multiplier` — [`L48`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/__init__.py#L48)
  - <a id="TitanModelConfig.intermediate_size"></a>`intermediate_size` — [`L39`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/__init__.py#L39)
  - <a id="TitanModelConfig.max_seq_len"></a>`max_seq_len` — [`L49`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/__init__.py#L49)
  - <a id="TitanModelConfig.multiple_of"></a>`multiple_of` — [`L47`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/__init__.py#L47)
  - <a id="TitanModelConfig.n_heads"></a>`n_heads` — [`L36`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/__init__.py#L36)
  - <a id="TitanModelConfig.n_kv_heads"></a>`n_kv_heads` — [`L37`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/__init__.py#L37)
  - <a id="TitanModelConfig.n_layers"></a>`n_layers` — [`L35`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/__init__.py#L35)
  - <a id="TitanModelConfig.norm_eps"></a>`norm_eps` — [`L40`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/__init__.py#L40)
  - <a id="TitanModelConfig.rope_theta"></a>`rope_theta` — [`L41`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/__init__.py#L41)
  - <a id="TitanModelConfig.vocab_size"></a>`vocab_size` — [`L38`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/__init__.py#L38)
- uses (calls/refs, reference-scoped): [`TitanMoeModelConfig`](__init__.md#TitanMoeModelConfig)
- used by: [`flavors`](__init__.md#flavors), [`_TPU_FLAVORS`](../tpu/transformers_modeling_backend/config_registry.md#_TPU_FLAVORS), [`TitanMoeModelConfig`](__init__.md#TitanMoeModelConfig)  (1 test-only)

### <a id="TitanMoeModelConfig"></a>`TitanMoeModelConfig`  ·  implements/extends TitanModelConfig
- def: [`torchtitan/experiments/transformers_modeling_backend/__init__.py:57`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/__init__.py#L57)
- doc: MoE model config — extends the base config with routed-expert parameters.
- signature: `class TitanMoeModelConfig(TitanModelConfig):`
- members:
  - <a id="TitanMoeModelConfig.comm_backend"></a>`comm_backend` — [`L101`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/__init__.py#L101) — ---
  - <a id="TitanMoeModelConfig.decoder_sparse_step"></a>`decoder_sparse_step` — [`L73`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/__init__.py#L73) — ---
  - <a id="TitanMoeModelConfig.experts_implementation"></a>`experts_implementation` — [`L85`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/__init__.py#L85) — ---
  - <a id="TitanMoeModelConfig.load_balance_coeff"></a>`load_balance_coeff` — [`L98`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/__init__.py#L98) — ---
  - <a id="TitanMoeModelConfig.moe_intermediate_size"></a>`moe_intermediate_size` — [`L70`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/__init__.py#L70) — ---
  - <a id="TitanMoeModelConfig.norm_topk_prob"></a>`norm_topk_prob` — [`L76`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/__init__.py#L76) — ---
  - <a id="TitanMoeModelConfig.num_experts"></a>`num_experts` — [`L64`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/__init__.py#L64) — ---
  - <a id="TitanMoeModelConfig.num_experts_per_tok"></a>`num_experts_per_tok` — [`L67`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/__init__.py#L67) — ---
  - <a id="TitanMoeModelConfig.num_nextn_predict_layers"></a>`num_nextn_predict_layers` — [`L79`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/__init__.py#L79) — ---
- uses (calls/refs, reference-scoped): [`TitanModelConfig`](__init__.md#TitanModelConfig)
- used by: [`flavors`](__init__.md#flavors), [`_TPU_FLAVORS`](../tpu/transformers_modeling_backend/config_registry.md#_TPU_FLAVORS), [`TitanModelConfig`](__init__.md#TitanModelConfig), [`is_moe`](model.md#Config.is_moe), [`__init__`](model.md#HFTransformerModel.Config.__init__)

## Functions
- <a id="model_registry"></a>`model_registry(flavor: str, *, seq_len: int)` — [`L163`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/__init__.py#L163)

## Module values
- <a id="__all__"></a>`__all__` — [`L16`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/__init__.py#L16)
- <a id="flavors"></a>`flavors` — [`L108`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/__init__.py#L108)

