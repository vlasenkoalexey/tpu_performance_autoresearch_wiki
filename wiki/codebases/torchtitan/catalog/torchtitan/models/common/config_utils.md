---
title: 'Module: torchtitan/models/common/config_utils.py'
type: catalog
provenance: extracted
module: torchtitan/models/common/config_utils.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.models.common.config_utils`/
symbols:
  make_gqa_config: make_gqa_config().
  decoder_vocab_size: decoder_vocab_size().
  make_token_dispatcher_config: make_token_dispatcher_config().
  DEFAULT_DEBUG_MODEL_SEQ_LEN: DEFAULT_DEBUG_MODEL_SEQ_LEN.
  make_moe_config: make_moe_config().
  make_router_config: make_router_config().
  get_attention_config: get_attention_config().
  make_ffn_config: make_ffn_config().
  make_routed_experts_config: make_routed_experts_config().
  make_aux_loss_config: make_aux_loss_config().
  _FusedQKVInit.__call__: _FusedQKVInit#__call__().
  TpGemmBackend: TpGemmBackend.
  update_moe_aux_loss_configs: update_moe_aux_loss_configs().
  moe_load_balance_aux_loss_configs: moe_load_balance_aux_loss_configs().
  _fused_qkv_param_init: _fused_qkv_param_init().
  _FusedQKVInit: _FusedQKVInit#
  _FusedQKVInit.base_init: _FusedQKVInit#base_init.
  _FusedQKVInit.n_heads: _FusedQKVInit#n_heads.
  _FusedQKVInit.n_kv_heads: _FusedQKVInit#n_kv_heads.
  _FusedQKVInit.head_dim: _FusedQKVInit#head_dim.
  _FusedQKVInit.heads_per_kv: _FusedQKVInit#heads_per_kv.
  _FusedQKVInit.__init__: _FusedQKVInit#__init__().
---
# Module: [`torchtitan/models/common/config_utils.py`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/config_utils.py)

## Classes
### <a id="_FusedQKVInit"></a>`_FusedQKVInit`
- def: [`torchtitan/models/common/config_utils.py:110`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/config_utils.py#L110)
- signature: `class _FusedQKVInit:`
- members:
  - <a id="_FusedQKVInit.base_init"></a>`base_init` — [`L118`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/config_utils.py#L118)
  - <a id="_FusedQKVInit.head_dim"></a>`head_dim` — [`L121`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/config_utils.py#L121)
  - <a id="_FusedQKVInit.heads_per_kv"></a>`heads_per_kv` — [`L122`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/config_utils.py#L122)
  - <a id="_FusedQKVInit.n_heads"></a>`n_heads` — [`L119`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/config_utils.py#L119)
  - <a id="_FusedQKVInit.n_kv_heads"></a>`n_kv_heads` — [`L120`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/config_utils.py#L120)
- protocol/private: <a id="_FusedQKVInit.__call__"></a>`__call__`[`L124`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/config_utils.py#L124), <a id="_FusedQKVInit.__init__"></a>`__init__`[`L111`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/config_utils.py#L111)
- uses (calls/refs, reference-scoped): [`current_spmd_mesh`](../../distributed/spmd_types.md#current_spmd_mesh), [`spmd_mesh_size`](../../distributed/spmd_types.md#spmd_mesh_size)
- used by: [`_fused_qkv_param_init`](config_utils.md#_fused_qkv_param_init)

## Functions
- <a id="_fused_qkv_param_init"></a>`_fused_qkv_param_init(base_param_init: dict[str, Callable], *, n_heads: int, n_kv_heads: int, head_dim: int)` — [`L155`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/config_utils.py#L155)
- <a id="decoder_vocab_size"></a>`decoder_vocab_size(model_spec: ModelSpec)` — [`L61`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/config_utils.py#L61) — Assert Decoder.Config type so lint is not annoyed. — documented in [model-building-blocks](../../../../concepts/model-building-blocks.md)
- <a id="get_attention_config"></a>`get_attention_config(backend: str)` — [`L77`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/config_utils.py#L77) — Map backend string to an inner_attention config.
- <a id="make_aux_loss_config"></a>`make_aux_loss_config(*, type: Literal["sequence_wise", "batch_wise"], coeff: float, top_k: int)` — [`L295`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/config_utils.py#L295) — Build a MoELoadBalanceAuxLoss.Config for ``router.aux_loss``.
- <a id="make_ffn_config"></a>`make_ffn_config(*, dim: int, hidden_dim: int, w1_param_init: dict[str, Callable], w2w3_param_init: dict[str, Callable], tp_gemm_backend: TpGemmBackend = "default")` — [`L267`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/config_utils.py#L267) — Build a fully-specified FeedForward.Config. — documented in [model-building-blocks](../../../../concepts/model-building-blocks.md)
- <a id="make_gqa_config"></a>`make_gqa_config(*, dim: int, n_heads: int, wqkv_param_init: dict[str, Callable], wo_param_init: dict[str, Callable], inner_attention: Module.Config, rope: RoPE.Config | None, n_kv_heads: int | None = None, head_dim: int | None = None, fuse_qkv: bool = False, qk_norm: RMSNorm.Config | None = None, tp_gemm_backend: TpGemmBackend = "default")` — [`L170`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/config_utils.py#L170) — Build a fully-specified GQAttention.Config. — documented in [model-building-blocks](../../../../concepts/model-building-blocks.md)
- <a id="make_moe_config"></a>`make_moe_config(*, num_experts: int = 8, router: TokenChoiceTopKRouter.Config, routed_experts: RoutedExperts.Config, shared_experts: FeedForward.Config | None = None, load_balance_coeff: float | None = 0.001, aux_loss_coeff: float | None = None)` — [`L305`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/config_utils.py#L305) — Build a fully-specified MoE.Config.
- <a id="make_routed_experts_config"></a>`make_routed_experts_config(*, dim: int, hidden_dim: int, num_experts: int, top_k: int, param_init: dict[str, Callable], comm_backend: str, non_blocking_capacity_factor: float | None = None, num_max_tokens_per_rank: int | None = None, cudagraphable: bool = False)` — [`L429`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/config_utils.py#L429) — Build a fully-specified RoutedExperts.Config (inner_experts + token_dispatcher).
- <a id="make_router_config"></a>`make_router_config(*, dim: int, num_experts: int, gate_param_init: dict[str, Callable], top_k: int = 1, score_func: Literal["sigmoid", "softmax", "sqrtsoftplus"] = "sigmoid", route_norm: bool = False, route_scale: float = 1, num_expert_groups: int | None = None, num_limited_groups: int | None = None, bias: bool = False)` — [`L329`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/config_utils.py#L329) — Build a fully-specified TokenChoiceTopKRouter.Config. — documented in [model-building-blocks](../../../../concepts/model-building-blocks.md)
- <a id="make_token_dispatcher_config"></a>`make_token_dispatcher_config(*, num_experts: int, top_k: int, comm_backend: str, hidden_dim: int, non_blocking_capacity_factor: float | None = None, num_max_tokens_per_rank: int | None = None, cudagraphable: bool = False)` — [`L360`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/config_utils.py#L360) — Build the appropriate token dispatcher config.
- <a id="moe_load_balance_aux_loss_configs"></a>`moe_load_balance_aux_loss_configs(layers: list)` — [`L461`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/config_utils.py#L461) — The ``MoELoadBalanceAuxLoss`` router configs among ``layers``.
- <a id="update_moe_aux_loss_configs"></a>`update_moe_aux_loss_configs(layers: list, *, pp_enabled: bool, local_global_batch_size: int, global_batch_size: int, seq_len: int)` — [`L478`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/config_utils.py#L478) — Update aux loss configs for all MoE layers from trainer config.

## Module values
- <a id="DEFAULT_DEBUG_MODEL_SEQ_LEN"></a>`DEFAULT_DEBUG_MODEL_SEQ_LEN` — [`L58`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/config_utils.py#L58)
- <a id="TpGemmBackend"></a>`TpGemmBackend` — [`L74`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/config_utils.py#L74)

