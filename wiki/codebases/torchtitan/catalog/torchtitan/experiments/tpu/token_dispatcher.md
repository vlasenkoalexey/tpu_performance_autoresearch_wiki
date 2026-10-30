---
title: 'Module: torchtitan/experiments/tpu/token_dispatcher.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/token_dispatcher.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.token_dispatcher`/
symbols:
  TpuAllToAllTokenDispatcher.combine: TpuAllToAllTokenDispatcher#combine().
  TpuRoutedExperts.forward: TpuRoutedExperts#forward().
  TpuAllToAllTokenDispatcher: TpuAllToAllTokenDispatcher#
  TpuTokenDispatcherConverter: TpuTokenDispatcherConverter#
  TpuAllToAllTokenDispatcher.Config: TpuAllToAllTokenDispatcher#Config#
  TpuTokenDispatcherConverter.convert: TpuTokenDispatcherConverter#convert().
  TpuRoutedExpertsConverter.convert: TpuRoutedExpertsConverter#convert().
  TpuRoutedExperts.scale_before_down_proj: TpuRoutedExperts#scale_before_down_proj.
  TpuTokenDispatcherConverter.Config: TpuTokenDispatcherConverter#Config#
  TpuRoutedExperts.Config: TpuRoutedExperts#Config#
  TpuRoutedExperts: TpuRoutedExperts#
  local_reorder: local_reorder().
  scale_route_weights: scale_route_weights().
  TpuRoutedExpertsConverter.Config: TpuRoutedExpertsConverter#Config#
  stable_grouped_reduce: stable_grouped_reduce().
  TpuRoutedExpertsConverter: TpuRoutedExpertsConverter#
  TpuAllToAllTokenDispatcher.__init__: TpuAllToAllTokenDispatcher#__init__().
  TpuAllToAllTokenDispatcher._local_reorder: TpuAllToAllTokenDispatcher#_local_reorder().
  TpuRoutedExperts.__init__: TpuRoutedExperts#__init__().
  TpuAllToAllTokenDispatcher.fuse_route_score_backward: TpuAllToAllTokenDispatcher#fuse_route_score_backward.
  TpuAllToAllTokenDispatcher.Config.fuse_route_score_backward: TpuAllToAllTokenDispatcher#Config#fuse_route_score_backward.
  TpuRoutedExperts.Config.scale_before_down_proj: TpuRoutedExperts#Config#scale_before_down_proj.
  _ScaleRouteWeights.backward: _ScaleRouteWeights#backward().
  TpuRoutedExpertsConverter.__init__: TpuRoutedExpertsConverter#__init__().
  TpuTokenDispatcherConverter.__init__: TpuTokenDispatcherConverter#__init__().
  _ScaleRouteWeights: _ScaleRouteWeights#
  _StableGroupedReduce: _StableGroupedReduce#
  _LocalReorder: _LocalReorder#
  _ScaleRouteWeights.forward: _ScaleRouteWeights#forward().
  _StableGroupedReduce.forward: _StableGroupedReduce#forward().
  _StableGroupedReduce.backward: _StableGroupedReduce#backward().
  _LocalReorder.forward: _LocalReorder#forward().
  _LocalReorder.backward: _LocalReorder#backward().
  __all__: __all__.
---
# Module: [`torchtitan/experiments/tpu/token_dispatcher.py`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/token_dispatcher.py)

## Classes
### <a id="TpuAllToAllTokenDispatcher"></a>`TpuAllToAllTokenDispatcher`  ·  implements/extends AllToAllTokenDispatcher
- def: [`torchtitan/experiments/tpu/token_dispatcher.py:235`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/token_dispatcher.py#L235) — documented in [tpu-moe-dispatch-and-grouped-experts](../../../../concepts/tpu-moe-dispatch-and-grouped-experts.md)
- doc: Standard dispatcher with TPU-local permutation VJPs.
- signature: `class TpuAllToAllTokenDispatcher(AllToAllTokenDispatcher):`
- members:
  - <a id="TpuAllToAllTokenDispatcher.combine"></a>`combine(self, routed_output_RD: torch.Tensor, metadata: AllToAllDispatchMetadata | LocalDispatchMetadata, x_TD: torch.Tensor)` — [`L267`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/token_dispatcher.py#L267) — documented in [tpu-moe-dispatch-and-grouped-experts](../../../../concepts/tpu-moe-dispatch-and-grouped-experts.md)
  - <a id="TpuAllToAllTokenDispatcher.fuse_route_score_backward"></a>`fuse_route_score_backward` — [`L252`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/token_dispatcher.py#L252)
- protocol/private: <a id="TpuAllToAllTokenDispatcher.__init__"></a>`__init__`[`L250`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/token_dispatcher.py#L250), <a id="TpuAllToAllTokenDispatcher._local_reorder"></a>`_local_reorder`[`L254`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/token_dispatcher.py#L254)
- uses (calls/refs, reference-scoped): [`combine`](../../models/common/token_dispatcher.md#AllToAllTokenDispatcher.combine), [`AllToAllTokenDispatcher`](../../models/common/token_dispatcher.md#AllToAllTokenDispatcher), [`ep_mesh`](../../models/common/token_dispatcher.md#BaseEPTokenDispatcher.ep_mesh), [`Config`](token_dispatcher.md#TpuAllToAllTokenDispatcher.Config), [`LocalDispatchMetadata`](../../models/common/token_dispatcher.md#LocalDispatchMetadata), [`local_reorder`](token_dispatcher.md#local_reorder), [`AllToAllDispatchMetadata`](../../models/common/token_dispatcher.md#AllToAllDispatchMetadata), [`scale_route_weights`](token_dispatcher.md#scale_route_weights), [`topk_scores_experts_sorted_N`](../../models/common/token_dispatcher.md#LocalDispatchMetadata.topk_scores_experts_sorted_N), [`stable_grouped_reduce`](token_dispatcher.md#stable_grouped_reduce), [`top_k`](../../models/common/token_dispatcher.md#LocalTokenDispatcher.top_k), [`token_indices_experts_sorted_N`](../../models/common/token_dispatcher.md#LocalDispatchMetadata.token_indices_experts_sorted_N), [`__init__`](../../models/common/token_dispatcher.md#AllToAllTokenDispatcher.__init__), [`fuse_route_score_backward`](token_dispatcher.md#TpuAllToAllTokenDispatcher.Config.fuse_route_score_backward)
- used by: [`combine`](../../models/common/token_dispatcher.md#AllToAllTokenDispatcher.combine), [`AllToAllTokenDispatcher`](../../models/common/token_dispatcher.md#AllToAllTokenDispatcher), [`convert`](token_dispatcher.md#TpuTokenDispatcherConverter.convert), [`scale_before_down_proj`](token_dispatcher.md#TpuRoutedExperts.scale_before_down_proj), [`_local_reorder`](../../models/common/token_dispatcher.md#LocalTokenDispatcher._local_reorder)  (9 test-only)

### <a id="TpuAllToAllTokenDispatcher.Config"></a>`TpuAllToAllTokenDispatcher.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/tpu/token_dispatcher.py:247`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/token_dispatcher.py#L247)
- signature: `class Config(AllToAllTokenDispatcher.Config):`
- members:
  - <a id="TpuAllToAllTokenDispatcher.Config.fuse_route_score_backward"></a>`fuse_route_score_backward` — [`L248`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/token_dispatcher.py#L248)
- uses (calls/refs, reference-scoped): [`AllToAllTokenDispatcher`](../../models/common/token_dispatcher.md#AllToAllTokenDispatcher), [`Config`](../../models/common/token_dispatcher.md#AllToAllTokenDispatcher.Config)
- used by: [`convert`](token_dispatcher.md#TpuTokenDispatcherConverter.convert), [`__init__`](token_dispatcher.md#TpuAllToAllTokenDispatcher.__init__), [`fuse_route_score_backward`](token_dispatcher.md#TpuAllToAllTokenDispatcher.fuse_route_score_backward)  (9 test-only)

### <a id="TpuRoutedExperts"></a>`TpuRoutedExperts`  ·  implements/extends RoutedExperts
- def: [`torchtitan/experiments/tpu/token_dispatcher.py:294`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/token_dispatcher.py#L294) — documented in [tpu-moe-dispatch-and-grouped-experts](../../../../concepts/tpu-moe-dispatch-and-grouped-experts.md)
- doc: Routed experts that can apply the routing scores before W2.
- signature: `class TpuRoutedExperts(RoutedExperts):`
- members:
  - <a id="TpuRoutedExperts.forward"></a>`forward(self, x_TD: torch.Tensor, topk_scores_TK: torch.Tensor, topk_expert_ids_TK: torch.Tensor, num_local_tokens_per_expert_E: torch.Tensor)` — [`L324`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/token_dispatcher.py#L324)
  - <a id="TpuRoutedExperts.scale_before_down_proj"></a>`scale_before_down_proj` — [`L311`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/token_dispatcher.py#L311)
- protocol/private: <a id="TpuRoutedExperts.__init__"></a>`__init__`[`L309`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/token_dispatcher.py#L309)
- uses (calls/refs, reference-scoped): [`RoutedExperts`](../../models/common/moe.md#RoutedExperts), [`TpuAllToAllTokenDispatcher`](token_dispatcher.md#TpuAllToAllTokenDispatcher), [`maybe_set_sparse_mesh`](../../distributed/spmd_types.md#maybe_set_sparse_mesh), [`Config`](token_dispatcher.md#TpuRoutedExperts.Config), [`token_dispatcher`](../../models/common/moe.md#RoutedExperts.token_dispatcher), [`LocalDispatchMetadata`](../../models/common/token_dispatcher.md#LocalDispatchMetadata), [`forward`](../../models/common/moe.md#RoutedExperts.forward), [`topk_scores_experts_sorted_N`](../../models/common/token_dispatcher.md#LocalDispatchMetadata.topk_scores_experts_sorted_N), [`stable_grouped_reduce`](token_dispatcher.md#stable_grouped_reduce), [`token_indices_experts_sorted_N`](../../models/common/token_dispatcher.md#LocalDispatchMetadata.token_indices_experts_sorted_N), [`inner_experts`](../../models/common/moe.md#RoutedExperts.inner_experts), [`fuse_route_score_backward`](token_dispatcher.md#TpuAllToAllTokenDispatcher.fuse_route_score_backward), [`__init__`](../../models/common/moe.md#RoutedExperts.__init__), [`scale_before_down_proj`](token_dispatcher.md#TpuRoutedExperts.Config.scale_before_down_proj)
- used by: [`RoutedExperts`](../../models/common/moe.md#RoutedExperts), [`_scale_routes_before_down_proj`](qwen3/config_registry.md#_scale_routes_before_down_proj), [`convert`](token_dispatcher.md#TpuRoutedExpertsConverter.convert), [`forward`](../../models/common/moe.md#RoutedExperts.forward)  (5 test-only)

### <a id="TpuRoutedExperts.Config"></a>`TpuRoutedExperts.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/tpu/token_dispatcher.py:306`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/token_dispatcher.py#L306)
- signature: `class Config(RoutedExperts.Config):`
- members:
  - <a id="TpuRoutedExperts.Config.scale_before_down_proj"></a>`scale_before_down_proj` — [`L307`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/token_dispatcher.py#L307)
- uses (calls/refs, reference-scoped): [`RoutedExperts`](../../models/common/moe.md#RoutedExperts), [`Config`](../../models/common/moe.md#RoutedExperts.Config)
- used by: [`_scale_routes_before_down_proj`](qwen3/config_registry.md#_scale_routes_before_down_proj), [`convert`](token_dispatcher.md#TpuRoutedExpertsConverter.convert), [`scale_before_down_proj`](token_dispatcher.md#TpuRoutedExperts.scale_before_down_proj), [`__init__`](token_dispatcher.md#TpuRoutedExperts.__init__)  (5 test-only)

### <a id="TpuRoutedExpertsConverter"></a>`TpuRoutedExpertsConverter`  ·  implements/extends ModelConfigConverter
- def: [`torchtitan/experiments/tpu/token_dispatcher.py:358`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/token_dispatcher.py#L358) — documented in [tpu-moe-dispatch-and-grouped-experts](../../../../concepts/tpu-moe-dispatch-and-grouped-experts.md)
- doc: Select `TpuRoutedExperts` for the standard routed-experts block.
- signature: `class TpuRoutedExpertsConverter(ModelConfigConverter):`
- members:
  - <a id="TpuRoutedExpertsConverter.convert"></a>`convert(self, model_config)` — [`L368`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/token_dispatcher.py#L368)
- protocol/private: <a id="TpuRoutedExpertsConverter.__init__"></a>`__init__`[`L365`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/token_dispatcher.py#L365)
- uses (calls/refs, reference-scoped): [`ModelConfigConverter`](../../protocols/model.md#ModelConfigConverter), [`derive`](../../config/override.md#derive), [`traverse`](../../config/configurable.md#Configurable.Config.traverse), [`RoutedExperts`](../../models/common/moe.md#RoutedExperts), [`Config`](../../models/common/moe.md#RoutedExperts.Config), [`Config`](token_dispatcher.md#TpuRoutedExperts.Config), [`TpuRoutedExperts`](token_dispatcher.md#TpuRoutedExperts), [`Config`](token_dispatcher.md#TpuRoutedExpertsConverter.Config)
- used by: [`qwen3_moe_30b`](qwen3/config_registry.md#qwen3_moe_30b), [`qwen3_moe_235b_scan`](qwen3/config_registry.md#qwen3_moe_235b_scan), [`_qwen3_moe_235b_fsdp_only`](qwen3/config_registry.md#_qwen3_moe_235b_fsdp_only), [`ModelConfigConverter`](../../protocols/model.md#ModelConfigConverter), [`convert`](../../protocols/model.md#ModelConfigConverter.convert)

### <a id="TpuRoutedExpertsConverter.Config"></a>`TpuRoutedExpertsConverter.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/tpu/token_dispatcher.py:362`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/token_dispatcher.py#L362)
- signature: `class Config(ModelConfigConverter.Config):`
- uses (calls/refs, reference-scoped): [`ModelConfigConverter`](../../protocols/model.md#ModelConfigConverter), [`Config`](../../protocols/model.md#ModelConfigConverter.Config)
- used by: [`qwen3_moe_30b`](qwen3/config_registry.md#qwen3_moe_30b), [`qwen3_moe_235b_scan`](qwen3/config_registry.md#qwen3_moe_235b_scan), [`_qwen3_moe_235b_fsdp_only`](qwen3/config_registry.md#_qwen3_moe_235b_fsdp_only), [`__init__`](token_dispatcher.md#TpuRoutedExpertsConverter.__init__)

### <a id="TpuTokenDispatcherConverter"></a>`TpuTokenDispatcherConverter`  ·  implements/extends ModelConfigConverter
- def: [`torchtitan/experiments/tpu/token_dispatcher.py:385`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/token_dispatcher.py#L385) — documented in [tpu-moe-dispatch-and-grouped-experts](../../../../concepts/tpu-moe-dispatch-and-grouped-experts.md)
- doc: Select TPU local reorder and combine VJPs for the standard dispatcher.
- signature: `class TpuTokenDispatcherConverter(ModelConfigConverter):`
- members:
  - <a id="TpuTokenDispatcherConverter.convert"></a>`convert(self, model_config)` — [`L395`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/token_dispatcher.py#L395)
- protocol/private: <a id="TpuTokenDispatcherConverter.__init__"></a>`__init__`[`L392`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/token_dispatcher.py#L392)
- uses (calls/refs, reference-scoped): [`ModelConfigConverter`](../../protocols/model.md#ModelConfigConverter), [`derive`](../../config/override.md#derive), [`AllToAllTokenDispatcher`](../../models/common/token_dispatcher.md#AllToAllTokenDispatcher), [`traverse`](../../config/configurable.md#Configurable.Config.traverse), [`TpuAllToAllTokenDispatcher`](token_dispatcher.md#TpuAllToAllTokenDispatcher), [`Config`](token_dispatcher.md#TpuAllToAllTokenDispatcher.Config), [`Config`](../../models/common/token_dispatcher.md#AllToAllTokenDispatcher.Config), [`Config`](token_dispatcher.md#TpuTokenDispatcherConverter.Config)
- used by: [`qwen3_moe_30b`](qwen3/config_registry.md#qwen3_moe_30b), [`qwen3_moe_235b_scan`](qwen3/config_registry.md#qwen3_moe_235b_scan), [`_qwen3_moe_235b_fsdp_only`](qwen3/config_registry.md#_qwen3_moe_235b_fsdp_only), [`ModelConfigConverter`](../../protocols/model.md#ModelConfigConverter), [`convert`](../../protocols/model.md#ModelConfigConverter.convert), [`substitute_tpu_experts`](transformers_modeling_backend/model.md#substitute_tpu_experts), [`_TPU_MOE_CONVERTERS`](qwen3_5/config_registry.md#_TPU_MOE_CONVERTERS)  (3 test-only)

### <a id="TpuTokenDispatcherConverter.Config"></a>`TpuTokenDispatcherConverter.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/tpu/token_dispatcher.py:389`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/token_dispatcher.py#L389)
- signature: `class Config(ModelConfigConverter.Config):`
- uses (calls/refs, reference-scoped): [`ModelConfigConverter`](../../protocols/model.md#ModelConfigConverter), [`Config`](../../protocols/model.md#ModelConfigConverter.Config)
- used by: [`qwen3_moe_30b`](qwen3/config_registry.md#qwen3_moe_30b), [`qwen3_moe_235b_scan`](qwen3/config_registry.md#qwen3_moe_235b_scan), [`_qwen3_moe_235b_fsdp_only`](qwen3/config_registry.md#_qwen3_moe_235b_fsdp_only), [`substitute_tpu_experts`](transformers_modeling_backend/model.md#substitute_tpu_experts), [`_TPU_MOE_CONVERTERS`](qwen3_5/config_registry.md#_TPU_MOE_CONVERTERS), [`__init__`](token_dispatcher.md#TpuTokenDispatcherConverter.__init__)  (3 test-only)

### <a id="_LocalReorder"></a>`_LocalReorder`
- def: [`torchtitan/experiments/tpu/token_dispatcher.py:160`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/token_dispatcher.py#L160)
- doc: Invert the expert permutation instead of scattering repeated rows.
- signature: `class _LocalReorder(torch.autograd.Function):`
- members:
  - <a id="_LocalReorder.backward"></a>`backward(ctx, grad_routed_ND, _grad_token_indices_N, grad_scores_N)` — [`L203`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/token_dispatcher.py#L203)
  - <a id="_LocalReorder.forward"></a>`forward(ctx, x_TD, scores_TK, permutation_N, top_k)` — [`L187`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/token_dispatcher.py#L187)
- used by: [`local_reorder`](token_dispatcher.md#local_reorder)

### <a id="_ScaleRouteWeights"></a>`_ScaleRouteWeights`
- def: [`torchtitan/experiments/tpu/token_dispatcher.py:45`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/token_dispatcher.py#L45)
- doc: Scale expert outputs and fuse the FP32 route-score gradient reduction.
- signature: `class _ScaleRouteWeights(torch.autograd.Function):`
- members:
  - <a id="_ScaleRouteWeights.backward"></a>`backward(ctx, grad_output_ND)` — [`L58`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/token_dispatcher.py#L58)
  - <a id="_ScaleRouteWeights.forward"></a>`forward(ctx, routed_output_ND, scores_N)` — [`L49`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/token_dispatcher.py#L49)
- uses (calls/refs, reference-scoped): [`route_score_grad`](kernels/route_score.md#route_score_grad)
- used by: [`scale_route_weights`](token_dispatcher.md#scale_route_weights)

### <a id="_StableGroupedReduce"></a>`_StableGroupedReduce`
- def: [`torchtitan/experiments/tpu/token_dispatcher.py:106`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/token_dispatcher.py#L106)
- doc: Combine a dropless EP=1 route set without collision scatter autograd.
- signature: `class _StableGroupedReduce(torch.autograd.Function):`
- members:
  - <a id="_StableGroupedReduce.backward"></a>`backward(ctx, grad_output_TD)` — [`L143`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/token_dispatcher.py#L143)
  - <a id="_StableGroupedReduce.forward"></a>`forward(ctx, src_ND, index_N, top_k)` — [`L133`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/token_dispatcher.py#L133)
- used by: [`stable_grouped_reduce`](token_dispatcher.md#stable_grouped_reduce)

## Functions
- <a id="local_reorder"></a>`local_reorder(x_TD: torch.Tensor, scores_TK: torch.Tensor, expert_ids_TK: torch.Tensor, top_k: int)` — [`L222`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/token_dispatcher.py#L222) — Sort routes by expert while keeping all gathers row-indexed. — documented in [tpu-moe-dispatch-and-grouped-experts](../../../../concepts/tpu-moe-dispatch-and-grouped-experts.md)
- <a id="scale_route_weights"></a>`scale_route_weights(routed_output_ND: torch.Tensor, scores_N: torch.Tensor)` — [`L75`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/token_dispatcher.py#L75) — Weight expert outputs while optimizing the supported TPU backward. — documented in [tpu-moe-dispatch-and-grouped-experts](../../../../concepts/tpu-moe-dispatch-and-grouped-experts.md)
- <a id="stable_grouped_reduce"></a>`stable_grouped_reduce(src_ND: torch.Tensor, index_N: torch.Tensor, top_k: int)` — [`L151`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/token_dispatcher.py#L151) — Reduce fixed-K routes by token with FP32 accumulation. — documented in [tpu-moe-dispatch-and-grouped-experts](../../../../concepts/tpu-moe-dispatch-and-grouped-experts.md)

## Module values
- <a id="__all__"></a>`__all__` — [`L412`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/token_dispatcher.py#L412)

