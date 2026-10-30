---
title: 'Module: torchtitan/models/common/moe.py'
type: catalog
provenance: extracted
module: torchtitan/models/common/moe.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.models.common.moe`/
symbols:
  MoE: MoE#
  GroupedExperts: GroupedExperts#
  MoE.Config: MoE#Config#
  TokenChoiceTopKRouter.forward: TokenChoiceTopKRouter#forward().
  MoELoadBalanceAuxLoss.forward: MoELoadBalanceAuxLoss#forward().
  TokenChoiceTopKRouter: TokenChoiceTopKRouter#
  GroupedExperts.forward: GroupedExperts#forward().
  MoE.forward: MoE#forward().
  GroupedExperts.Config: GroupedExperts#Config#
  GroupedExperts.Config.hidden_dim: GroupedExperts#Config#hidden_dim.
  GroupedExperts.Config.num_experts: GroupedExperts#Config#num_experts.
  RoutedExperts: RoutedExperts#
  GroupedExperts.Config.dim: GroupedExperts#Config#dim.
  MoELoadBalanceAuxLoss.__init__: MoELoadBalanceAuxLoss#__init__().
  GroupedExperts.w2_EDF: GroupedExperts#w2_EDF.
  MoELoadBalanceAuxLoss: MoELoadBalanceAuxLoss#
  GroupedExperts.w1_EFD: GroupedExperts#w1_EFD.
  RoutedExperts.Config: RoutedExperts#Config#
  GroupedExperts.w3_EFD: GroupedExperts#w3_EFD.
  MoE.Config.router: MoE#Config#router.
  MoE.load_balance_coeff: MoE#load_balance_coeff.
  RoutedExperts.Config.inner_experts: RoutedExperts#Config#inner_experts.
  TokenChoiceTopKRouter.Config: TokenChoiceTopKRouter#Config#
  TokenChoiceTopKRouter.aux_loss: TokenChoiceTopKRouter#aux_loss.
  MoELoadBalanceAuxLoss.Config: MoELoadBalanceAuxLoss#Config#
  MoE.Config.shared_experts: MoE#Config#shared_experts.
  TokenChoiceTopKRouter.Config.gate: TokenChoiceTopKRouter#Config#gate.
  MoE.Config.routed_experts: MoE#Config#routed_experts.
  GroupedExperts._grouped_mm: GroupedExperts#_grouped_mm().
  RoutedExperts.Config.token_dispatcher: RoutedExperts#Config#token_dispatcher.
  MoE.Config.num_experts: MoE#Config#num_experts.
  RoutedExperts.token_dispatcher: RoutedExperts#token_dispatcher.
  TokenChoiceTopKRouter._select_experts: TokenChoiceTopKRouter#_select_experts().
  MoE.router: MoE#router.
  MoE.routed_experts: MoE#routed_experts.
  MoE.shared_experts: MoE#shared_experts.
  configure_moe_aux_loss_reduction: configure_moe_aux_loss_reduction().
  RoutedExperts.forward: RoutedExperts#forward().
  TokenChoiceTopKRouter.Config.aux_loss: TokenChoiceTopKRouter#Config#aux_loss.
  TokenChoiceTopKRouter.Config.top_k: TokenChoiceTopKRouter#Config#top_k.
  MicrobatchWiseLoadBalanceLoss.forward: MicrobatchWiseLoadBalanceLoss#forward().
  MoE._init_self_buffers: MoE#_init_self_buffers().
  TokenChoiceTopKRouter.Config.num_experts: TokenChoiceTopKRouter#Config#num_experts.
  MoELoadBalanceAuxLoss.set_meshes: MoELoadBalanceAuxLoss#set_meshes().
  TokenChoiceTopKRouter.num_experts: TokenChoiceTopKRouter#num_experts.
  TokenChoiceTopKRouter.num_expert_groups: TokenChoiceTopKRouter#num_expert_groups.
  TokenChoiceTopKRouter._get_node_limited_routing_scores: TokenChoiceTopKRouter#_get_node_limited_routing_scores().
  RoutedExperts.parallelize: RoutedExperts#parallelize().
  TokenChoiceTopKRouter.top_k: TokenChoiceTopKRouter#top_k.
  MoE.tokens_per_expert_E: MoE#tokens_per_expert_E.
  RoutedExperts.inner_experts: RoutedExperts#inner_experts.
  TokenChoiceTopKRouter.Config.score_func: TokenChoiceTopKRouter#Config#score_func.
  MoE.__init__: MoE#__init__().
  TokenChoiceTopKRouter.score_func: TokenChoiceTopKRouter#score_func.
  _tokens_per_expert: _tokens_per_expert().
  TokenChoiceTopKRouter.Config.route_norm: TokenChoiceTopKRouter#Config#route_norm.
  TokenChoiceTopKRouter.gate: TokenChoiceTopKRouter#gate.
  TokenChoiceTopKRouter._debug_force_load_balance_routing: TokenChoiceTopKRouter#_debug_force_load_balance_routing().
  MicrobatchWiseLoadBalanceLoss.Config: MicrobatchWiseLoadBalanceLoss#Config#
  MoE.Config.load_balance_coeff: MoE#Config#load_balance_coeff.
  _batch_wise_load_balance_loss: _batch_wise_load_balance_loss().
  GroupedExperts.__init__: GroupedExperts#__init__().
  MicrobatchWiseLoadBalanceLoss: MicrobatchWiseLoadBalanceLoss#
  MoELoadBalanceAuxLoss.Config.top_k: MoELoadBalanceAuxLoss#Config#top_k.
  MoELoadBalanceAuxLoss.global_batch_size: MoELoadBalanceAuxLoss#global_batch_size.
  MoELoadBalanceAuxLoss.top_k: MoELoadBalanceAuxLoss#top_k.
  TokenChoiceTopKRouter.__init__: TokenChoiceTopKRouter#__init__().
  TokenChoiceTopKRouter.num_limited_groups: TokenChoiceTopKRouter#num_limited_groups.
  MicrobatchWiseLoadBalanceLoss._reduce_token_partials: MicrobatchWiseLoadBalanceLoss#_reduce_token_partials().
  MoE.expert_bias_E: MoE#expert_bias_E.
  MoELoadBalanceAuxLoss.Config.global_batch_size: MoELoadBalanceAuxLoss#Config#global_batch_size.
  MoELoadBalanceAuxLoss.Config.seq_len: MoELoadBalanceAuxLoss#Config#seq_len.
  TokenChoiceTopKRouter.Config.route_scale: TokenChoiceTopKRouter#Config#route_scale.
  _sequence_wise_load_balance_loss: _sequence_wise_load_balance_loss().
  MoELoadBalanceAuxLoss.seq_len: MoELoadBalanceAuxLoss#seq_len.
  RoutedExperts.__init__: RoutedExperts#__init__().
  TokenChoiceTopKRouter.route_norm: TokenChoiceTopKRouter#route_norm.
  TokenChoiceTopKRouter.route_scale: TokenChoiceTopKRouter#route_scale.
  TokenChoiceTopKRouter.build_routing_map: TokenChoiceTopKRouter#build_routing_map.
  TokenChoiceTopKRouter._debug_force_load_balance: TokenChoiceTopKRouter#_debug_force_load_balance.
  MoELoadBalanceAuxLoss.cp_mesh: MoELoadBalanceAuxLoss#cp_mesh.
  MoELoadBalanceAuxLoss.tp_mesh: MoELoadBalanceAuxLoss#tp_mesh.
  TokenChoiceTopKRouter.Config.num_expert_groups: TokenChoiceTopKRouter#Config#num_expert_groups.
  TokenChoiceTopKRouter.Config.num_limited_groups: TokenChoiceTopKRouter#Config#num_limited_groups.
  MoELoadBalanceAuxLoss._last_local_normalized_aux_loss: MoELoadBalanceAuxLoss#_last_local_normalized_aux_loss.
  MoELoadBalanceAuxLoss._last_local_tokens_per_expert_E: MoELoadBalanceAuxLoss#_last_local_tokens_per_expert_E.
  GroupedExperts.num_experts: GroupedExperts#num_experts.
  _all_reduce_expert_counts: _all_reduce_expert_counts().
  MoELoadBalanceAuxLoss.dp_mesh: MoELoadBalanceAuxLoss#dp_mesh.
  MoELoadBalanceAuxLoss.collect_routing_metrics: MoELoadBalanceAuxLoss#collect_routing_metrics.
  TokenChoiceTopKRouter.Config._debug_force_load_balance: TokenChoiceTopKRouter#Config#_debug_force_load_balance.
  TokenChoiceTopKRouter.Config.token_count_impl: TokenChoiceTopKRouter#Config#token_count_impl.
  MoELoadBalanceAuxLoss._init_self_buffers: MoELoadBalanceAuxLoss#_init_self_buffers().
---
# Module: [`torchtitan/models/common/moe.py`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe.py)

## Classes
### <a id="GroupedExperts"></a>`GroupedExperts`  ·  implements/extends Module
- def: [`torchtitan/models/common/moe.py:440`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe.py#L440) — documented in [model-building-blocks](../../../../concepts/model-building-blocks.md)
- signature: `class GroupedExperts(Module):`
- members:
  - <a id="GroupedExperts._grouped_mm"></a>`_grouped_mm(self, *, A: torch.Tensor, weight_EOI: torch.Tensor, offs: torch.Tensor)` — [`L507`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe.py#L507) — Grouped matmul of ``A @ weight_EOI.transpose(-2, -1)``.
  - <a id="GroupedExperts.forward"></a>`forward(self, x_RD: torch.Tensor, num_tokens_per_expert_E: torch.Tensor)` — [`L460`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe.py#L460) — Raw expert computation without dispatch/combine.
  - <a id="GroupedExperts.num_experts"></a>`num_experts` — [`L449`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe.py#L449)
  - <a id="GroupedExperts.w1_EFD"></a>`w1_EFD` — [`L450`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe.py#L450)
  - <a id="GroupedExperts.w2_EDF"></a>`w2_EDF` — [`L453`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe.py#L453)
  - <a id="GroupedExperts.w3_EFD"></a>`w3_EFD` — [`L456`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe.py#L456)
- protocol/private: <a id="GroupedExperts.__init__"></a>`__init__`[`L447`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe.py#L447)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`get_spmd_backend`](../../distributed/utils.md#get_spmd_backend), [`forward`](../../experiments/tpu/grouped_experts.md#TpuGroupedExperts.forward), [`TpuGroupedExperts`](../../experiments/tpu/grouped_experts.md#TpuGroupedExperts), [`Config`](moe.md#GroupedExperts.Config), [`forward`](../gpt_oss/moe.md#GptOssGroupedExperts.forward), [`hidden_dim`](moe.md#GroupedExperts.Config.hidden_dim), [`num_experts`](moe.md#GroupedExperts.Config.num_experts), [`dim`](moe.md#GroupedExperts.Config.dim), [`forward`](../kimi_k3/moe.md#KimiGroupedExperts.forward), [`spmd_mesh_size`](../../distributed/spmd_types.md#spmd_mesh_size), [`forward`](../../overrides/fused_swiglu.md#FusedGroupedExperts.forward), [`GptOssGroupedExperts`](../gpt_oss/moe.md#GptOssGroupedExperts), [`KimiGroupedExperts`](../kimi_k3/moe.md#KimiGroupedExperts), [`FusedGroupedExperts`](../../overrides/fused_swiglu.md#FusedGroupedExperts)
- used by: [`Module`](../../protocols/module.md#Module), [`forward`](../../experiments/tpu/grouped_experts.md#TpuGroupedExperts.forward), [`make_routed_experts_config`](config_utils.md#make_routed_experts_config), [`has_quantization`](../../components/quantization/utils.md#has_quantization), [`TpuGroupedExperts`](../../experiments/tpu/grouped_experts.md#TpuGroupedExperts), [`fused_grouped_experts`](../../overrides/fused_swiglu.md#fused_grouped_experts), [`convert`](../../components/quantization/mxfp8/converter.md#MXFP8GroupedExpertsConverter.convert), [`forward`](../gpt_oss/moe.md#GptOssGroupedExperts.forward), [`_get_expert_param_info`](../../experiments/transformers_modeling_backend/moe_replacement.md#_get_expert_param_info), [`convert`](../../experiments/tpu/grouped_experts.md#TpuGroupedExpertsConverter.convert), [`convert`](../../components/quantization/float8.md#Float8GroupedExpertsConverter.convert), [`_native_experts_forward`](../../experiments/tpu/grouped_experts.md#TpuGroupedExperts._native_experts_forward), [`Config`](../../experiments/tpu/grouped_experts.md#TpuGroupedExperts.Config), [`forward`](../kimi_k3/moe.md#KimiGroupedExperts.forward), [`inner_experts`](moe.md#RoutedExperts.Config.inner_experts), [`w3_EDF`](../../experiments/tpu/grouped_experts.md#TpuGroupedExperts.w3_EDF), [`__init__`](../../overrides/fused_swiglu.md#FusedGroupedExperts.__init__), [`forward`](../../overrides/fused_swiglu.md#FusedGroupedExperts.forward), [`Config`](../gpt_oss/moe.md#GptOssGroupedExperts.Config), [`Config`](../kimi_k3/moe.md#KimiGroupedExperts.Config), [`Config`](../../overrides/fused_swiglu.md#FusedGroupedExperts.Config), [`__init__`](../kimi_k3/moe.md#KimiGroupedExperts.__init__), [`GptOssGroupedExperts`](../gpt_oss/moe.md#GptOssGroupedExperts), [`KimiGroupedExperts`](../kimi_k3/moe.md#KimiGroupedExperts), [`FusedGroupedExperts`](../../overrides/fused_swiglu.md#FusedGroupedExperts)  (5 test-only)

### <a id="GroupedExperts.Config"></a>`GroupedExperts.Config`  ·  implements/extends Config
- def: [`torchtitan/models/common/moe.py:442`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe.py#L442)
- signature: `class Config(Module.Config):`
- members:
  - <a id="GroupedExperts.Config.dim"></a>`dim` — [`L443`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe.py#L443)
  - <a id="GroupedExperts.Config.hidden_dim"></a>`hidden_dim` — [`L444`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe.py#L444)
  - <a id="GroupedExperts.Config.num_experts"></a>`num_experts` — [`L445`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe.py#L445)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`Config`](../../protocols/module.md#Module.Config)
- used by: [`_latent_moe_config`](../kimi_k3/__init__.md#_latent_moe_config), [`get_maxtext_decoder_nparams_and_flops`](../../experiments/tpu/mfu_flops.md#get_maxtext_decoder_nparams_and_flops), [`make_routed_experts_config`](config_utils.md#make_routed_experts_config), [`has_quantization`](../../components/quantization/utils.md#has_quantization), [`_make_gptoss_experts_config`](../gpt_oss/__init__.md#_make_gptoss_experts_config), [`fused_grouped_experts`](../../overrides/fused_swiglu.md#fused_grouped_experts), [`convert`](../../components/quantization/mxfp8/converter.md#MXFP8GroupedExpertsConverter.convert), [`_get_expert_param_info`](../../experiments/transformers_modeling_backend/moe_replacement.md#_get_expert_param_info), [`convert`](../../experiments/tpu/grouped_experts.md#TpuGroupedExpertsConverter.convert), [`convert`](../../components/quantization/float8.md#Float8GroupedExpertsConverter.convert), [`w2_EDF`](moe.md#GroupedExperts.w2_EDF), [`w1_EFD`](moe.md#GroupedExperts.w1_EFD), [`Config`](../../experiments/tpu/grouped_experts.md#TpuGroupedExperts.Config), [`w3_EFD`](moe.md#GroupedExperts.w3_EFD), [`inner_experts`](moe.md#RoutedExperts.Config.inner_experts), [`w13`](../../overrides/fused_swiglu.md#FusedGroupedExperts.w13), [`__init__`](../gpt_oss/moe.md#GptOssGroupedExperts.__init__), [`w3_EDF`](../../experiments/tpu/grouped_experts.md#TpuGroupedExperts.w3_EDF), [`w1_EDF`](../../experiments/tpu/grouped_experts.md#TpuGroupedExperts.w1_EDF), [`w2_EFD`](../../experiments/tpu/grouped_experts.md#TpuGroupedExperts.w2_EFD), [`Config`](../gpt_oss/moe.md#GptOssGroupedExperts.Config), [`Config`](../kimi_k3/moe.md#KimiGroupedExperts.Config), [`Config`](../../overrides/fused_swiglu.md#FusedGroupedExperts.Config), [`num_experts`](../../experiments/tpu/grouped_experts.md#TpuGroupedExperts.num_experts), [`__init__`](moe.md#GroupedExperts.__init__), [`num_experts`](moe.md#GroupedExperts.num_experts)  (10 test-only)

### <a id="MicrobatchWiseLoadBalanceLoss"></a>`MicrobatchWiseLoadBalanceLoss`  ·  implements/extends AuxLoss
- def: [`torchtitan/models/common/moe.py:809`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe.py#L809)
- doc: Per-forward MoE load-balance gradient (DeepSeek-V3 Sec 2.1.2 Eqs 17-20).
- signature: `class MicrobatchWiseLoadBalanceLoss(AuxLoss):`
- members:
  - <a id="MicrobatchWiseLoadBalanceLoss._reduce_token_partials"></a>`_reduce_token_partials(self, partial_E: torch.Tensor, axes: tuple[str, ...])` — [`L855`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe.py#L855) — Partial -> Invariant all-reduce over the token-partition axes.
  - <a id="MicrobatchWiseLoadBalanceLoss.forward"></a>`forward(self, scores_TE: torch.Tensor, routing_map_TE: torch.Tensor, *, carrier: torch.Tensor)` — [`L880`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe.py#L880) — Compute the per-forward balance loss and inject its gradient.
- uses (calls/refs, reference-scoped): [`AuxLoss`](aux_loss.md#AuxLoss), [`spmd_mesh_size`](../../distributed/spmd_types.md#spmd_mesh_size), [`spmd_local_context`](../../distributed/spmd_types.md#spmd_local_context), [`inject`](aux_loss.md#AuxLoss.inject), [`spmd_sparse_mesh`](../../distributed/spmd_types.md#spmd_sparse_mesh)
- used by: [`make_moe_config`](config_utils.md#make_moe_config), [`AuxLoss`](aux_loss.md#AuxLoss)

### <a id="MicrobatchWiseLoadBalanceLoss.Config"></a>`MicrobatchWiseLoadBalanceLoss.Config`  ·  implements/extends Config
- def: [`torchtitan/models/common/moe.py:846`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe.py#L846)
- doc: Same fields as `AuxLoss.Config`; this loss adds no knobs.
- signature: `class Config(AuxLoss.Config):`
- uses (calls/refs, reference-scoped): [`AuxLoss`](aux_loss.md#AuxLoss), [`Config`](aux_loss.md#AuxLoss.Config)
- used by: [`make_moe_config`](config_utils.md#make_moe_config)

### <a id="MoE"></a>`MoE`  ·  implements/extends Module
- def: [`torchtitan/models/common/moe.py:934`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe.py#L934) — documented in [model-building-blocks](../../../../concepts/model-building-blocks.md)
- doc: Mixture of Experts layer.
- signature: `class MoE(Module):`
- members:
  - <a id="MoE.forward"></a>`forward(self, x_TD: torch.Tensor, **router_kwargs)` — [`L999`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe.py#L999) — Args:
  - <a id="MoE.expert_bias_E"></a>`expert_bias_E` — [`L991`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe.py#L991)
  - <a id="MoE.load_balance_coeff"></a>`load_balance_coeff` — [`L975`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe.py#L975)
  - <a id="MoE.routed_experts"></a>`routed_experts` — [`L965`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe.py#L965)
  - <a id="MoE.router"></a>`router` — [`L966`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe.py#L966)
  - <a id="MoE.shared_experts"></a>`shared_experts` — [`L967`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe.py#L967)
  - <a id="MoE.tokens_per_expert_E"></a>`tokens_per_expert_E` — [`L1062`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe.py#L1062)
- protocol/private: <a id="MoE.__init__"></a>`__init__`[`L961`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe.py#L961), <a id="MoE._init_self_buffers"></a>`_init_self_buffers`[`L1055`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe.py#L1055)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`build`](../../protocols/module.md#Module.Config.build), [`Config`](moe.md#MoE.Config), [`forward`](../kimi_k3/moe.md#KimiLatentMoE.forward), [`MoELoadBalanceAuxLoss`](moe.md#MoELoadBalanceAuxLoss), [`router`](moe.md#MoE.Config.router), [`shared_experts`](moe.md#MoE.Config.shared_experts), [`routed_experts`](moe.md#MoE.Config.routed_experts), [`num_experts`](moe.md#MoE.Config.num_experts), [`KimiLatentMoE`](../kimi_k3/moe.md#KimiLatentMoE), [`TpuDiscardedTokenCounterMoE`](../../experiments/tpu/overrides/discarded_token_counter.md#TpuDiscardedTokenCounterMoE), [`DeepSeekV4MoE`](../deepseek_v4/moe.md#DeepSeekV4MoE), [`_tokens_per_expert`](moe.md#_tokens_per_expert), [`load_balance_coeff`](moe.md#MoE.Config.load_balance_coeff), [`GptOssMoE`](../gpt_oss/moe.md#GptOssMoE), [`_HFBatchedMoE`](../../experiments/transformers_modeling_backend/moe_replacement.md#_HFBatchedMoE), [`forward`](../../experiments/transformers_modeling_backend/moe_replacement.md#_HFBatchedMoE.forward)  (2 test-only)
- used by: [`Module`](../../protocols/module.md#Module), [`_build_moe_config`](../../experiments/transformers_modeling_backend/moe_replacement.md#_build_moe_config), [`get_maxtext_decoder_nparams_and_flops`](../../experiments/tpu/mfu_flops.md#get_maxtext_decoder_nparams_and_flops), [`update_from_config`](decoder.md#Decoder.Config.update_from_config), [`make_moe_config`](config_utils.md#make_moe_config), [`parallelize_qwen3`](../../experiments/tpu/qwen3/infra/parallelize.md#parallelize_qwen3), [`annotate_moe_ep_regions`](../../experiments/graph_trainer/common_utils.md#annotate_moe_ep_regions), [`parallelize_qwen3_5`](../../experiments/tpu/qwen3_5/infra/parallelize.md#parallelize_qwen3_5), [`moe`](decoder.md#TransformerBlock.Config.moe), [`get_nparams_and_active_nparams`](../utils.md#get_nparams_and_active_nparams), [`maybe_update_minimal_async_ep_config`](../../distributed/minimal_async_ep/api.md#maybe_update_minimal_async_ep_config), [`update_ep_token_dispatcher_config`](token_dispatcher.md#update_ep_token_dispatcher_config), [`forward`](../kimi_k3/moe.md#KimiLatentMoE.forward), [`_init_self_buffers`](../../protocols/module.md#Module._init_self_buffers), [`_use_global_batch_aux_loss`](../../experiments/tpu/qwen3/config_registry.md#_use_global_batch_aux_loss), [`tpu_discarded_token_counter`](../../experiments/tpu/overrides/discarded_token_counter.md#tpu_discarded_token_counter), [`check_layers_are_stackable`](../../experiments/tpu/graph_trainer/layer_stack.md#check_layers_are_stackable), [`Config`](../deepseek_v4/moe.md#DeepSeekV4MoE.Config), [`Config`](../kimi_k3/moe.md#KimiLatentMoE.Config), [`Config`](../../experiments/tpu/overrides/discarded_token_counter.md#TpuDiscardedTokenCounterMoE.Config), [`KimiLatentMoE`](../kimi_k3/moe.md#KimiLatentMoE), [`TpuDiscardedTokenCounterMoE`](../../experiments/tpu/overrides/discarded_token_counter.md#TpuDiscardedTokenCounterMoE), [`first_moe`](decoder.md#Decoder.Config.first_moe), [`DeepSeekV4MoE`](../deepseek_v4/moe.md#DeepSeekV4MoE), [`Config`](../gpt_oss/moe.md#GptOssMoE.Config), [`__init__`](../kimi_k3/moe.md#KimiLatentMoE.__init__), [`GptOssMoE`](../gpt_oss/moe.md#GptOssMoE), [`_HFBatchedMoE`](../../experiments/transformers_modeling_backend/moe_replacement.md#_HFBatchedMoE), [`__getattr__`](../../experiments/tpu/overrides/discarded_token_counter.md#TpuDiscardedTokenCounterMoE.__getattr__), [`forward`](../../experiments/transformers_modeling_backend/moe_replacement.md#_HFBatchedMoE.forward)  (14 test-only)

### <a id="MoE.Config"></a>`MoE.Config`  ·  implements/extends Config
- def: [`torchtitan/models/common/moe.py:954`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe.py#L954)
- signature: `class Config(Module.Config):`
- members:
  - <a id="MoE.Config.load_balance_coeff"></a>`load_balance_coeff` — [`L958`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe.py#L958)
  - <a id="MoE.Config.num_experts"></a>`num_experts` — [`L955`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe.py#L955)
  - <a id="MoE.Config.routed_experts"></a>`routed_experts` — [`L956`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe.py#L956)
  - <a id="MoE.Config.router"></a>`router` — [`L957`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe.py#L957)
  - <a id="MoE.Config.shared_experts"></a>`shared_experts` — [`L959`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe.py#L959)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`Config`](../../protocols/module.md#Module.Config), [`FeedForward`](feed_forward.md#FeedForward), [`TokenChoiceTopKRouter`](moe.md#TokenChoiceTopKRouter), [`RoutedExperts`](moe.md#RoutedExperts), [`Config`](feed_forward.md#FeedForward.Config), [`Config`](moe.md#RoutedExperts.Config), [`Config`](moe.md#TokenChoiceTopKRouter.Config)
- used by: [`_build_mtp_layers`](../deepseek_v4/__init__.md#_build_mtp_layers), [`_latent_moe_config`](../kimi_k3/__init__.md#_latent_moe_config), [`_build_gptoss_layers`](../gpt_oss/__init__.md#_build_gptoss_layers), [`_make_v4_moe_config`](../deepseek_v4/__init__.md#_make_v4_moe_config), [`_build_moe_config`](../../experiments/transformers_modeling_backend/moe_replacement.md#_build_moe_config), [`get_maxtext_decoder_nparams_and_flops`](../../experiments/tpu/mfu_flops.md#get_maxtext_decoder_nparams_and_flops), [`update_from_config`](decoder.md#Decoder.Config.update_from_config), [`make_moe_config`](config_utils.md#make_moe_config), [`to_hf`](../kimi_k3/state_dict_adapter.md#KimiK3StateDictAdapter.to_hf), [`from_hf`](../kimi_k3/state_dict_adapter.md#KimiK3StateDictAdapter.from_hf), [`moe`](decoder.md#TransformerBlock.Config.moe), [`maybe_update_minimal_async_ep_config`](../../distributed/minimal_async_ep/api.md#maybe_update_minimal_async_ep_config), [`update_ep_token_dispatcher_config`](token_dispatcher.md#update_ep_token_dispatcher_config), [`_use_global_batch_aux_loss`](../../experiments/tpu/qwen3/config_registry.md#_use_global_batch_aux_loss), [`tpu_discarded_token_counter`](../../experiments/tpu/overrides/discarded_token_counter.md#tpu_discarded_token_counter), [`load_balance_coeff`](moe.md#MoE.load_balance_coeff), [`Config`](../deepseek_v4/moe.md#DeepSeekV4MoE.Config), [`routed_experts`](moe.md#MoE.routed_experts), [`router`](moe.md#MoE.router), [`shared_experts`](moe.md#MoE.shared_experts), [`Config`](../kimi_k3/moe.md#KimiLatentMoE.Config), [`Config`](../../experiments/tpu/overrides/discarded_token_counter.md#TpuDiscardedTokenCounterMoE.Config), [`first_moe`](decoder.md#Decoder.Config.first_moe), [`__init__`](moe.md#MoE.__init__), [`Config`](../gpt_oss/moe.md#GptOssMoE.Config)  (11 test-only)

### <a id="MoELoadBalanceAuxLoss"></a>`MoELoadBalanceAuxLoss`  ·  implements/extends AuxLoss
- def: [`torchtitan/models/common/moe.py:177`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe.py#L177)
- doc: MoE auxiliary load-balance loss, configured on the router.
- signature: `class MoELoadBalanceAuxLoss(AuxLoss):`
- members:
  - <a id="MoELoadBalanceAuxLoss.forward"></a>`forward(self, scores_TE: torch.Tensor, routing_map_TE: torch.Tensor | None, *, carrier: torch.Tensor, expert_ids_TK: torch.Tensor | None = None)` — [`L269`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe.py#L269) — Compute the load-balance loss and inject its gradient.
  - <a id="MoELoadBalanceAuxLoss.set_meshes"></a>`set_meshes(self, *, dp_mesh: DeviceMesh | None, cp_mesh: DeviceMesh | None, tp_mesh: DeviceMesh | None)` — [`L258`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe.py#L258)
  - <a id="MoELoadBalanceAuxLoss.collect_routing_metrics"></a>`collect_routing_metrics` — [`L252`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe.py#L252)
  - <a id="MoELoadBalanceAuxLoss.cp_mesh"></a>`cp_mesh` — [`L250`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe.py#L250)
  - <a id="MoELoadBalanceAuxLoss.dp_mesh"></a>`dp_mesh` — [`L249`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe.py#L249)
  - <a id="MoELoadBalanceAuxLoss.global_batch_size"></a>`global_batch_size` — [`L246`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe.py#L246)
  - <a id="MoELoadBalanceAuxLoss.seq_len"></a>`seq_len` — [`L247`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe.py#L247)
  - <a id="MoELoadBalanceAuxLoss.top_k"></a>`top_k` — [`L248`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe.py#L248)
  - <a id="MoELoadBalanceAuxLoss.tp_mesh"></a>`tp_mesh` — [`L251`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe.py#L251)
- protocol/private: <a id="MoELoadBalanceAuxLoss.__init__"></a>`__init__`[`L225`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe.py#L225), <a id="MoELoadBalanceAuxLoss._init_self_buffers"></a>`_init_self_buffers`[`L254`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe.py#L254), <a id="MoELoadBalanceAuxLoss._last_local_normalized_aux_loss"></a>`_last_local_normalized_aux_loss`[`L371`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe.py#L371), <a id="MoELoadBalanceAuxLoss._last_local_tokens_per_expert_E"></a>`_last_local_tokens_per_expert_E`[`L377`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe.py#L377)
- uses (calls/refs, reference-scoped): [`AuxLoss`](aux_loss.md#AuxLoss), [`reduce_mesh`](aux_loss.md#AuxLoss.reduce_mesh), [`Config`](moe.md#MoELoadBalanceAuxLoss.Config), [`coeff`](aux_loss.md#AuxLoss.Config.coeff), [`_group_counts`](aux_loss.md#AuxLoss._group_counts), [`_tokens_per_expert`](moe.md#_tokens_per_expert), [`instance_acc`](aux_loss.md#AuxLoss.instance_acc), [`_batch_wise_load_balance_loss`](moe.md#_batch_wise_load_balance_loss), [`top_k`](moe.md#MoELoadBalanceAuxLoss.Config.top_k), [`coeff`](aux_loss.md#AuxLoss.coeff), [`global_batch_size`](moe.md#MoELoadBalanceAuxLoss.Config.global_batch_size), [`seq_len`](moe.md#MoELoadBalanceAuxLoss.Config.seq_len), [`__init__`](aux_loss.md#AuxLoss.__init__), [`_sequence_wise_load_balance_loss`](moe.md#_sequence_wise_load_balance_loss), [`_AuxLossInjection`](aux_loss.md#_AuxLossInjection), [`metric_name`](aux_loss.md#AuxLoss.metric_name)
- used by: [`AuxLoss`](aux_loss.md#AuxLoss), [`forward`](moe.md#TokenChoiceTopKRouter.forward), [`make_aux_loss_config`](config_utils.md#make_aux_loss_config), [`aux_loss`](moe.md#TokenChoiceTopKRouter.aux_loss), [`load_balance_coeff`](moe.md#MoE.load_balance_coeff), [`configure_moe_aux_loss_reduction`](moe.md#configure_moe_aux_loss_reduction), [`moe_load_balance_aux_loss_configs`](config_utils.md#moe_load_balance_aux_loss_configs), [`_init_self_buffers`](aux_loss.md#AuxLoss._init_self_buffers)  (3 test-only)

### <a id="MoELoadBalanceAuxLoss.Config"></a>`MoELoadBalanceAuxLoss.Config`  ·  implements/extends Config
- def: [`torchtitan/models/common/moe.py:207`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe.py#L207)
- signature: `class Config(AuxLoss.Config):`
- members:
  - <a id="MoELoadBalanceAuxLoss.Config.global_batch_size"></a>`global_batch_size` — [`L214`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe.py#L214) — ---
  - <a id="MoELoadBalanceAuxLoss.Config.seq_len"></a>`seq_len` — [`L219`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe.py#L219) — ---
  - <a id="MoELoadBalanceAuxLoss.Config.top_k"></a>`top_k` — [`L212`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe.py#L212) — ---
- uses (calls/refs, reference-scoped): [`AuxLoss`](aux_loss.md#AuxLoss), [`Config`](aux_loss.md#AuxLoss.Config)
- used by: [`__init__`](moe.md#MoELoadBalanceAuxLoss.__init__), [`make_aux_loss_config`](config_utils.md#make_aux_loss_config), [`update_moe_aux_loss_configs`](config_utils.md#update_moe_aux_loss_configs), [`moe_load_balance_aux_loss_configs`](config_utils.md#moe_load_balance_aux_loss_configs), [`global_batch_size`](moe.md#MoELoadBalanceAuxLoss.global_batch_size), [`top_k`](moe.md#MoELoadBalanceAuxLoss.top_k), [`seq_len`](moe.md#MoELoadBalanceAuxLoss.seq_len)  (5 test-only)

### <a id="RoutedExperts"></a>`RoutedExperts`  ·  implements/extends Module
- def: [`torchtitan/models/common/moe.py:526`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe.py#L526)
- doc: Routed-expert `local_map` region: composes token_dispatcher + inner_experts
- signature: `class RoutedExperts(Module):`
- members:
  - <a id="RoutedExperts.forward"></a>`forward(self, x_TD: torch.Tensor, topk_scores_TK: torch.Tensor, topk_expert_ids_TK: torch.Tensor, num_local_tokens_per_expert_E: torch.Tensor)` — [`L540`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe.py#L540) — Dispatch tokens to experts, compute, combine, and scatter_add.
  - <a id="RoutedExperts.parallelize"></a>`parallelize(self, parallel_dims)` — [`L574`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe.py#L574) — Parallelize the grouped experts, then wire the EP mesh on the
  - <a id="RoutedExperts.inner_experts"></a>`inner_experts` — [`L537`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe.py#L537)
  - <a id="RoutedExperts.token_dispatcher"></a>`token_dispatcher` — [`L538`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe.py#L538)
- protocol/private: <a id="RoutedExperts.__init__"></a>`__init__`[`L535`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe.py#L535)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`build`](../../protocols/module.md#Module.Config.build), [`build`](../../config/configurable.md#Configurable.Config.build), [`get_optional_mesh`](../../distributed/parallel_dims.md#ParallelDims.get_optional_mesh), [`parallelize`](../../protocols/module.md#Module.parallelize), [`forward`](../../experiments/tpu/token_dispatcher.md#TpuRoutedExperts.forward), [`Config`](moe.md#RoutedExperts.Config), [`inner_experts`](moe.md#RoutedExperts.Config.inner_experts), [`maybe_set_sparse_mesh`](../../distributed/spmd_types.md#maybe_set_sparse_mesh), [`token_dispatcher`](moe.md#RoutedExperts.Config.token_dispatcher), [`TpuRoutedExperts`](../../experiments/tpu/token_dispatcher.md#TpuRoutedExperts)
- used by: [`Module`](../../protocols/module.md#Module), [`_latent_moe_config`](../kimi_k3/__init__.md#_latent_moe_config), [`make_moe_config`](config_utils.md#make_moe_config), [`parallelize`](../../protocols/module.md#Module.parallelize), [`make_routed_experts_config`](config_utils.md#make_routed_experts_config), [`_make_gptoss_experts_config`](../gpt_oss/__init__.md#_make_gptoss_experts_config), [`forward`](../../experiments/tpu/token_dispatcher.md#TpuRoutedExperts.forward), [`convert`](../../experiments/tpu/token_dispatcher.md#TpuRoutedExpertsConverter.convert), [`scale_before_down_proj`](../../experiments/tpu/token_dispatcher.md#TpuRoutedExperts.scale_before_down_proj), [`routed_experts`](moe.md#MoE.Config.routed_experts), [`Config`](../../experiments/tpu/token_dispatcher.md#TpuRoutedExperts.Config), [`TpuRoutedExperts`](../../experiments/tpu/token_dispatcher.md#TpuRoutedExperts), [`__init__`](../../experiments/tpu/token_dispatcher.md#TpuRoutedExperts.__init__)  (2 test-only)

### <a id="RoutedExperts.Config"></a>`RoutedExperts.Config`  ·  implements/extends Config
- def: [`torchtitan/models/common/moe.py:531`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe.py#L531)
- signature: `class Config(Module.Config):`
- members:
  - <a id="RoutedExperts.Config.inner_experts"></a>`inner_experts` — [`L532`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe.py#L532)
  - <a id="RoutedExperts.Config.token_dispatcher"></a>`token_dispatcher` — [`L533`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe.py#L533)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`Config`](../../protocols/module.md#Module.Config), [`GroupedExperts`](moe.md#GroupedExperts), [`Config`](moe.md#GroupedExperts.Config), [`LocalTokenDispatcher`](token_dispatcher.md#LocalTokenDispatcher), [`Config`](token_dispatcher.md#LocalTokenDispatcher.Config)
- used by: [`_build_mtp_layers`](../deepseek_v4/__init__.md#_build_mtp_layers), [`_latent_moe_config`](../kimi_k3/__init__.md#_latent_moe_config), [`get_maxtext_decoder_nparams_and_flops`](../../experiments/tpu/mfu_flops.md#get_maxtext_decoder_nparams_and_flops), [`make_moe_config`](config_utils.md#make_moe_config), [`make_routed_experts_config`](config_utils.md#make_routed_experts_config), [`_make_gptoss_experts_config`](../gpt_oss/__init__.md#_make_gptoss_experts_config), [`convert`](../../experiments/tpu/token_dispatcher.md#TpuRoutedExpertsConverter.convert), [`routed_experts`](moe.md#MoE.Config.routed_experts), [`Config`](../../experiments/tpu/token_dispatcher.md#TpuRoutedExperts.Config), [`token_dispatcher`](moe.md#RoutedExperts.token_dispatcher), [`inner_experts`](moe.md#RoutedExperts.inner_experts), [`__init__`](moe.md#RoutedExperts.__init__)  (5 test-only)

### <a id="TokenChoiceTopKRouter"></a>`TokenChoiceTopKRouter`  ·  implements/extends Module
- def: [`torchtitan/models/common/moe.py:586`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe.py#L586)
- doc: This class implements token-choice routing. In token-choice top-K routing, each token is
- signature: `class TokenChoiceTopKRouter(Module):`
- members:
  - <a id="TokenChoiceTopKRouter._debug_force_load_balance_routing"></a>`_debug_force_load_balance_routing(self, scores_TE: torch.Tensor)` — [`L637`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe.py#L637) — Balanced round-robin expert assignment.
  - <a id="TokenChoiceTopKRouter._get_node_limited_routing_scores"></a>`_get_node_limited_routing_scores(self, scores_for_choice_TE: torch.Tensor)` — [`L656`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe.py#L656) — Select num_limited_groups groups based on group scores,
  - <a id="TokenChoiceTopKRouter.forward"></a>`forward(self, x_TD: torch.Tensor, expert_bias_E: torch.Tensor | None = None, **router_kwargs)` — [`L716`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe.py#L716) — Args:
  - <a id="TokenChoiceTopKRouter.aux_loss"></a>`aux_loss` — [`L625`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe.py#L625)
  - <a id="TokenChoiceTopKRouter.build_routing_map"></a>`build_routing_map` — [`L632`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe.py#L632)
  - <a id="TokenChoiceTopKRouter.gate"></a>`gate` — [`L617`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe.py#L617)
  - <a id="TokenChoiceTopKRouter.num_expert_groups"></a>`num_expert_groups` — [`L619`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe.py#L619)
  - <a id="TokenChoiceTopKRouter.num_experts"></a>`num_experts` — [`L618`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe.py#L618)
  - <a id="TokenChoiceTopKRouter.num_limited_groups"></a>`num_limited_groups` — [`L620`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe.py#L620)
  - <a id="TokenChoiceTopKRouter.route_norm"></a>`route_norm` — [`L623`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe.py#L623)
  - <a id="TokenChoiceTopKRouter.route_scale"></a>`route_scale` — [`L624`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe.py#L624)
  - <a id="TokenChoiceTopKRouter.score_func"></a>`score_func` — [`L622`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe.py#L622)
  - <a id="TokenChoiceTopKRouter.top_k"></a>`top_k` — [`L621`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe.py#L621)
- protocol/private: <a id="TokenChoiceTopKRouter.__init__"></a>`__init__`[`L615`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe.py#L615), <a id="TokenChoiceTopKRouter._debug_force_load_balance"></a>`_debug_force_load_balance`[`L635`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe.py#L635), <a id="TokenChoiceTopKRouter._select_experts"></a>`_select_experts`[`L698`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe.py#L698)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`build`](../../protocols/module.md#Module.Config.build), [`MoELoadBalanceAuxLoss`](moe.md#MoELoadBalanceAuxLoss), [`Config`](moe.md#TokenChoiceTopKRouter.Config), [`gate`](moe.md#TokenChoiceTopKRouter.Config.gate), [`aux_loss`](moe.md#TokenChoiceTopKRouter.Config.aux_loss), [`top_k`](moe.md#TokenChoiceTopKRouter.Config.top_k), [`num_experts`](moe.md#TokenChoiceTopKRouter.Config.num_experts), [`_select_experts`](../deepseek_v4/moe.md#DeepSeekV4Router._select_experts), [`score_func`](moe.md#TokenChoiceTopKRouter.Config.score_func), [`route_norm`](moe.md#TokenChoiceTopKRouter.Config.route_norm), [`DeepSeekV4Router`](../deepseek_v4/moe.md#DeepSeekV4Router), [`route_scale`](moe.md#TokenChoiceTopKRouter.Config.route_scale), [`num_expert_groups`](moe.md#TokenChoiceTopKRouter.Config.num_expert_groups), [`num_limited_groups`](moe.md#TokenChoiceTopKRouter.Config.num_limited_groups), [`_debug_force_load_balance`](moe.md#TokenChoiceTopKRouter.Config._debug_force_load_balance), [`token_count_impl`](moe.md#TokenChoiceTopKRouter.Config.token_count_impl)  (2 test-only)
- used by: [`Module`](../../protocols/module.md#Module), [`_latent_moe_config`](../kimi_k3/__init__.md#_latent_moe_config), [`_build_gptoss_layers`](../gpt_oss/__init__.md#_build_gptoss_layers), [`make_moe_config`](config_utils.md#make_moe_config), [`make_router_config`](config_utils.md#make_router_config), [`hash`](../deepseek_v4/moe.md#DeepSeekV4Router.hash), [`router`](moe.md#MoE.Config.router), [`tid2eid`](../deepseek_v4/moe.md#DeepSeekV4Router.tid2eid), [`Config`](../deepseek_v4/moe.md#DeepSeekV4Router.Config), [`_select_experts`](../deepseek_v4/moe.md#DeepSeekV4Router._select_experts), [`DeepSeekV4Router`](../deepseek_v4/moe.md#DeepSeekV4Router), [`__init__`](../deepseek_v4/moe.md#DeepSeekV4Router.__init__)  (6 test-only)

### <a id="TokenChoiceTopKRouter.Config"></a>`TokenChoiceTopKRouter.Config`  ·  implements/extends Config
- def: [`torchtitan/models/common/moe.py:596`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe.py#L596)
- signature: `class Config(Module.Config):`
- members:
  - <a id="TokenChoiceTopKRouter.Config.aux_loss"></a>`aux_loss` — [`L605`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe.py#L605)
  - <a id="TokenChoiceTopKRouter.Config.gate"></a>`gate` — [`L598`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe.py#L598)
  - <a id="TokenChoiceTopKRouter.Config.num_expert_groups"></a>`num_expert_groups` — [`L599`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe.py#L599)
  - <a id="TokenChoiceTopKRouter.Config.num_experts"></a>`num_experts` — [`L597`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe.py#L597)
  - <a id="TokenChoiceTopKRouter.Config.num_limited_groups"></a>`num_limited_groups` — [`L600`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe.py#L600)
  - <a id="TokenChoiceTopKRouter.Config.route_norm"></a>`route_norm` — [`L603`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe.py#L603)
  - <a id="TokenChoiceTopKRouter.Config.route_scale"></a>`route_scale` — [`L604`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe.py#L604)
  - <a id="TokenChoiceTopKRouter.Config.score_func"></a>`score_func` — [`L602`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe.py#L602)
  - <a id="TokenChoiceTopKRouter.Config.token_count_impl"></a>`token_count_impl` — [`L606`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe.py#L606) — ---
  - <a id="TokenChoiceTopKRouter.Config.top_k"></a>`top_k` — [`L601`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe.py#L601)
- protocol/private: <a id="TokenChoiceTopKRouter.Config._debug_force_load_balance"></a>`_debug_force_load_balance`[`L613`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe.py#L613)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`Config`](../../protocols/module.md#Module.Config), [`AuxLoss`](aux_loss.md#AuxLoss), [`RouterGateLinear`](linear.md#RouterGateLinear), [`Config`](linear.md#RouterGateLinear.Config), [`Config`](aux_loss.md#AuxLoss.Config)
- used by: [`_build_mtp_layers`](../deepseek_v4/__init__.md#_build_mtp_layers), [`_latent_moe_config`](../kimi_k3/__init__.md#_latent_moe_config), [`_build_gptoss_layers`](../gpt_oss/__init__.md#_build_gptoss_layers), [`_make_v4_moe_config`](../deepseek_v4/__init__.md#_make_v4_moe_config), [`get_maxtext_decoder_nparams_and_flops`](../../experiments/tpu/mfu_flops.md#get_maxtext_decoder_nparams_and_flops), [`make_moe_config`](config_utils.md#make_moe_config), [`make_router_config`](config_utils.md#make_router_config), [`router`](moe.md#MoE.Config.router), [`aux_loss`](moe.md#TokenChoiceTopKRouter.aux_loss), [`num_expert_groups`](moe.md#TokenChoiceTopKRouter.num_expert_groups), [`num_experts`](moe.md#TokenChoiceTopKRouter.num_experts), [`Config`](../deepseek_v4/moe.md#DeepSeekV4Router.Config), [`top_k`](moe.md#TokenChoiceTopKRouter.top_k), [`score_func`](moe.md#TokenChoiceTopKRouter.score_func), [`gate`](moe.md#TokenChoiceTopKRouter.gate), [`__init__`](moe.md#TokenChoiceTopKRouter.__init__), [`num_limited_groups`](moe.md#TokenChoiceTopKRouter.num_limited_groups), [`_debug_force_load_balance`](moe.md#TokenChoiceTopKRouter._debug_force_load_balance), [`build_routing_map`](moe.md#TokenChoiceTopKRouter.build_routing_map), [`route_norm`](moe.md#TokenChoiceTopKRouter.route_norm), [`route_scale`](moe.md#TokenChoiceTopKRouter.route_scale)  (7 test-only)

## Functions
- <a id="_all_reduce_expert_counts"></a>`_all_reduce_expert_counts(counts: torch.Tensor, *, reduction: Literal["batch", "sequence"], dp_mesh: DeviceMesh | None, cp_mesh: DeviceMesh | None, tp_mesh: DeviceMesh | None)` — [`L139`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe.py#L139) — Sum non-differentiable expert counts over token-partition mesh axes.
- <a id="_batch_wise_load_balance_loss"></a>`_batch_wise_load_balance_loss(scores_BLE: torch.Tensor, routing_map_BLE: torch.Tensor, top_k: int, aux_loss_coeff: float, *, dp_mesh: DeviceMesh | None = None, cp_mesh: DeviceMesh | None = None, tp_mesh: DeviceMesh | None = None, num_tokens_per_expert: torch.Tensor | None = None)` — [`L94`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe.py#L94) — Batch-wise auxiliary load-balance loss.
- <a id="_sequence_wise_load_balance_loss"></a>`_sequence_wise_load_balance_loss(scores_BLE: torch.Tensor, routing_map_BLE: torch.Tensor, top_k: int, aux_loss_coeff: float, *, cp_mesh: DeviceMesh | None = None, tp_mesh: DeviceMesh | None = None)` — [`L54`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe.py#L54) — Sequence-wise auxiliary load-balance loss (DeepSeek-V3 Eqs 17-20).
- <a id="_tokens_per_expert"></a>`_tokens_per_expert(topk_expert_ids_BLK: torch.Tensor, num_experts: int)` — [`L427`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe.py#L427) — Count selected routes without materializing a ``(B, L, E)`` map.
- <a id="configure_moe_aux_loss_reduction"></a>`configure_moe_aux_loss_reduction(model: nn.Module, parallel_dims)` — [`L385`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe.py#L385) — Wire process meshes used to reduce MoE auxiliary-loss counts.

