---
title: 'Module: torchtitan/models/common/feed_forward.py'
type: catalog
provenance: extracted
module: torchtitan/models/common/feed_forward.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.models.common.feed_forward`/
symbols:
  FeedForward: FeedForward#
  FeedForward.forward: FeedForward#forward().
  FeedForward.Config: FeedForward#Config#
  FeedForward.Config.w1: FeedForward#Config#w1.
  FeedForward.Config.w3: FeedForward#Config#w3.
  FeedForward.Config.w2: FeedForward#Config#w2.
  SigmoidGatedFeedForward: SigmoidGatedFeedForward#
  SigmoidGatedFeedForward.Config: SigmoidGatedFeedForward#Config#
  FeedForward.w2: FeedForward#w2.
  FeedForward.w1: FeedForward#w1.
  FeedForward.w3: FeedForward#w3.
  SigmoidGatedFeedForward.Config.gate: SigmoidGatedFeedForward#Config#gate.
  compute_ffn_hidden_dim: compute_ffn_hidden_dim().
  SigmoidGatedFeedForward.gate: SigmoidGatedFeedForward#gate.
  SigmoidGatedFeedForward.__init__: SigmoidGatedFeedForward#__init__().
  SigmoidGatedFeedForward.forward: SigmoidGatedFeedForward#forward().
  FeedForward.__init__: FeedForward#__init__().
  __all__: __all__.
---
# Module: [`torchtitan/models/common/feed_forward.py`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/feed_forward.py)

## Classes
### <a id="FeedForward"></a>`FeedForward`  ·  implements/extends Module
- def: [`torchtitan/models/common/feed_forward.py:34`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/feed_forward.py#L34) — documented in [model-building-blocks](../../../../concepts/model-building-blocks.md)
- doc: SwiGLU feed-forward module shared across models.
- signature: `class FeedForward(Module):`
- members:
  - <a id="FeedForward.forward"></a>`forward(self, x: torch.Tensor)` — [`L53`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/feed_forward.py#L53)
  - <a id="FeedForward.w1"></a>`w1` — [`L49`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/feed_forward.py#L49)
  - <a id="FeedForward.w2"></a>`w2` — [`L50`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/feed_forward.py#L50)
  - <a id="FeedForward.w3"></a>`w3` — [`L51`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/feed_forward.py#L51)
- protocol/private: <a id="FeedForward.__init__"></a>`__init__`[`L47`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/feed_forward.py#L47)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`build`](../../protocols/module.md#Module.Config.build), [`Config`](feed_forward.md#FeedForward.Config), [`forward`](dist_gemm.md#DistGEMMFeedForward.forward), [`w1`](feed_forward.md#FeedForward.Config.w1), [`forward`](../kimi_k3/moe.md#KimiFeedForward.forward), [`w3`](feed_forward.md#FeedForward.Config.w3), [`w2`](feed_forward.md#FeedForward.Config.w2), [`SigmoidGatedFeedForward`](feed_forward.md#SigmoidGatedFeedForward), [`FusedSwiGLU`](../../overrides/fused_swiglu.md#FusedSwiGLU), [`forward`](../../overrides/fused_swiglu.md#FusedSwiGLU.forward), [`DistGEMMFeedForward`](dist_gemm.md#DistGEMMFeedForward), [`KimiFeedForward`](../kimi_k3/moe.md#KimiFeedForward), [`forward`](feed_forward.md#SigmoidGatedFeedForward.forward)  (2 test-only)
- used by: [`Module`](../../protocols/module.md#Module), [`get_maxtext_decoder_nparams_and_flops`](../../experiments/tpu/mfu_flops.md#get_maxtext_decoder_nparams_and_flops), [`make_moe_config`](config_utils.md#make_moe_config), [`feed_forward`](decoder.md#TransformerBlock.Config.feed_forward), [`make_ffn_config`](config_utils.md#make_ffn_config), [`_fused_swiglu_config`](../../overrides/fused_swiglu.md#_fused_swiglu_config), [`forward`](dist_gemm.md#DistGEMMFeedForward.forward), [`forward`](../kimi_k3/moe.md#KimiFeedForward.forward), [`fused_swiglu`](../../overrides/fused_swiglu.md#fused_swiglu), [`shared_experts`](moe.md#MoE.Config.shared_experts), [`_make_v4_dense_config`](../deepseek_v4/__init__.md#_make_v4_dense_config), [`SigmoidGatedFeedForward`](feed_forward.md#SigmoidGatedFeedForward), [`Config`](feed_forward.md#SigmoidGatedFeedForward.Config), [`FusedSwiGLU`](../../overrides/fused_swiglu.md#FusedSwiGLU), [`DistGEMMFeedForward`](dist_gemm.md#DistGEMMFeedForward), [`Config`](dist_gemm.md#DistGEMMFeedForward.Config), [`Config`](../kimi_k3/moe.md#KimiFeedForward.Config), [`KimiFeedForward`](../kimi_k3/moe.md#KimiFeedForward), [`first_feed_forward`](decoder.md#Decoder.Config.first_feed_forward), [`__init__`](feed_forward.md#SigmoidGatedFeedForward.__init__), [`__init__`](../kimi_k3/moe.md#KimiFeedForward.__init__), [`forward`](feed_forward.md#SigmoidGatedFeedForward.forward)  (6 test-only)

### <a id="FeedForward.Config"></a>`FeedForward.Config`  ·  implements/extends Config
- def: [`torchtitan/models/common/feed_forward.py:42`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/feed_forward.py#L42)
- signature: `class Config(Module.Config):`
- members:
  - <a id="FeedForward.Config.w1"></a>`w1` — [`L43`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/feed_forward.py#L43)
  - <a id="FeedForward.Config.w2"></a>`w2` — [`L44`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/feed_forward.py#L44)
  - <a id="FeedForward.Config.w3"></a>`w3` — [`L45`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/feed_forward.py#L45)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`Linear`](linear.md#Linear), [`Config`](linear.md#Linear.Config), [`Config`](../../protocols/module.md#Module.Config)
- used by: [`_build_mtp_layers`](../deepseek_v4/__init__.md#_build_mtp_layers), [`_build_moe_config`](../../experiments/transformers_modeling_backend/moe_replacement.md#_build_moe_config), [`get_maxtext_decoder_nparams_and_flops`](../../experiments/tpu/mfu_flops.md#get_maxtext_decoder_nparams_and_flops), [`make_moe_config`](config_utils.md#make_moe_config), [`feed_forward`](decoder.md#TransformerBlock.Config.feed_forward), [`make_ffn_config`](config_utils.md#make_ffn_config), [`_shared_experts_config`](../qwen3_5/__init__.md#_shared_experts_config), [`_fused_swiglu_config`](../../overrides/fused_swiglu.md#_fused_swiglu_config), [`_feed_forward_config`](../kimi_k3/__init__.md#_feed_forward_config), [`fused_swiglu`](../../overrides/fused_swiglu.md#fused_swiglu), [`shared_experts`](moe.md#MoE.Config.shared_experts), [`_make_v4_dense_config`](../deepseek_v4/__init__.md#_make_v4_dense_config), [`Config`](feed_forward.md#SigmoidGatedFeedForward.Config), [`w2`](feed_forward.md#FeedForward.w2), [`Config`](dist_gemm.md#DistGEMMFeedForward.Config), [`Config`](../kimi_k3/moe.md#KimiFeedForward.Config), [`w1`](feed_forward.md#FeedForward.w1), [`w3`](feed_forward.md#FeedForward.w3), [`__post_init__`](dist_gemm.md#DistGEMMFeedForward.Config.__post_init__), [`first_feed_forward`](decoder.md#Decoder.Config.first_feed_forward), [`__init__`](feed_forward.md#FeedForward.__init__)  (3 test-only)

### <a id="SigmoidGatedFeedForward"></a>`SigmoidGatedFeedForward`  ·  implements/extends FeedForward
- def: [`torchtitan/models/common/feed_forward.py:57`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/feed_forward.py#L57)
- doc: SwiGLU feed-forward with a per-token sigmoid gate.
- signature: `class SigmoidGatedFeedForward(FeedForward):`
- members:
  - <a id="SigmoidGatedFeedForward.forward"></a>`forward(self, x: torch.Tensor)` — [`L73`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/feed_forward.py#L73)
  - <a id="SigmoidGatedFeedForward.gate"></a>`gate` — [`L71`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/feed_forward.py#L71)
- protocol/private: <a id="SigmoidGatedFeedForward.__init__"></a>`__init__`[`L69`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/feed_forward.py#L69)
- uses (calls/refs, reference-scoped): [`build`](../../protocols/module.md#Module.Config.build), [`FeedForward`](feed_forward.md#FeedForward), [`forward`](feed_forward.md#FeedForward.forward), [`Config`](feed_forward.md#SigmoidGatedFeedForward.Config), [`gate`](feed_forward.md#SigmoidGatedFeedForward.Config.gate), [`__init__`](feed_forward.md#FeedForward.__init__)
- used by: [`_build_moe_config`](../../experiments/transformers_modeling_backend/moe_replacement.md#_build_moe_config), [`build_and_swap_native_moe`](../../experiments/transformers_modeling_backend/moe_replacement.md#build_and_swap_native_moe), [`FeedForward`](feed_forward.md#FeedForward), [`_shared_experts_config`](../qwen3_5/__init__.md#_shared_experts_config), [`TP`](../qwen3_5/sharding.md#TP), [`_set_shared_expert_gate_sharding`](../qwen3_5/sharding.md#_set_shared_expert_gate_sharding), [`forward`](feed_forward.md#FeedForward.forward)

### <a id="SigmoidGatedFeedForward.Config"></a>`SigmoidGatedFeedForward.Config`  ·  implements/extends Config
- def: [`torchtitan/models/common/feed_forward.py:66`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/feed_forward.py#L66)
- signature: `class Config(FeedForward.Config):`
- members:
  - <a id="SigmoidGatedFeedForward.Config.gate"></a>`gate` — [`L67`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/feed_forward.py#L67)
- uses (calls/refs, reference-scoped): [`Linear`](linear.md#Linear), [`Config`](linear.md#Linear.Config), [`FeedForward`](feed_forward.md#FeedForward), [`Config`](feed_forward.md#FeedForward.Config)
- used by: [`_build_moe_config`](../../experiments/transformers_modeling_backend/moe_replacement.md#_build_moe_config), [`build_and_swap_native_moe`](../../experiments/transformers_modeling_backend/moe_replacement.md#build_and_swap_native_moe), [`_shared_experts_config`](../qwen3_5/__init__.md#_shared_experts_config), [`_set_shared_expert_gate_sharding`](../qwen3_5/sharding.md#_set_shared_expert_gate_sharding), [`gate`](feed_forward.md#SigmoidGatedFeedForward.gate), [`__init__`](feed_forward.md#SigmoidGatedFeedForward.__init__)

## Functions
- <a id="compute_ffn_hidden_dim"></a>`compute_ffn_hidden_dim(dim: int, *, multiple_of: int = 1, ffn_dim_multiplier: float | None = None)` — [`L18`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/feed_forward.py#L18) — Compute the SwiGLU hidden dimension for Llama3/4-style models.

## Module values
- <a id="__all__"></a>`__all__` — [`L15`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/feed_forward.py#L15)

