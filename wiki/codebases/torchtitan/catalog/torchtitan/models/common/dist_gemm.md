---
title: 'Module: torchtitan/models/common/dist_gemm.py'
type: catalog
provenance: extracted
module: torchtitan/models/common/dist_gemm.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.models.common.dist_gemm`/
symbols:
  AllGatherFusedQKVLinear.forward: AllGatherFusedQKVLinear#forward().
  DistGEMMFeedForward.forward: DistGEMMFeedForward#forward().
  _warn_once_unfused: _warn_once_unfused().
  DistGEMMFeedForward: DistGEMMFeedForward#
  DistGEMMFeedForward.Config: DistGEMMFeedForward#Config#
  _tp_group_from_context: _tp_group_from_context().
  RowParallelLinear.forward: RowParallelLinear#forward().
  DistGEMMFeedForward.Config.__post_init__: DistGEMMFeedForward#Config#__post_init__().
  RowParallelLinear.Config: RowParallelLinear#Config#
  RowParallelLinear: RowParallelLinear#
  AllGatherFusedQKVLinear.Config: AllGatherFusedQKVLinear#Config#
  validate_dist_gemm_preconditions: validate_dist_gemm_preconditions().
  AllGatherFusedQKVLinear: AllGatherFusedQKVLinear#
  _WARNED_NO_TP: _WARNED_NO_TP.
  __all__: __all__.
---
# Module: [`torchtitan/models/common/dist_gemm.py`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/dist_gemm.py)

## Classes
### <a id="AllGatherFusedQKVLinear"></a>`AllGatherFusedQKVLinear`  ·  implements/extends FusedQKVLinear
- def: [`torchtitan/models/common/dist_gemm.py:113`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/dist_gemm.py#L113)
- doc: Fused QKV projection whose forward all-gathers the TP sequence shard.
- signature: `class AllGatherFusedQKVLinear(FusedQKVLinear):`
- members:
  - <a id="AllGatherFusedQKVLinear.forward"></a>`forward(self, x: torch.Tensor)` — [`L122`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/dist_gemm.py#L122)
- uses (calls/refs, reference-scoped): [`FusedQKVLinear`](attention.md#FusedQKVLinear), [`forward`](attention.md#FusedQKVLinear.forward), [`head_dim`](attention.md#BaseQKVLinear.head_dim), [`_warn_once_unfused`](dist_gemm.md#_warn_once_unfused), [`wqkv`](attention.md#FusedQKVLinear.wqkv), [`heads_per_kv`](attention.md#FusedQKVLinear.heads_per_kv), [`_tp_group_from_context`](dist_gemm.md#_tp_group_from_context), [`AllGatherLinear`](../../distributed/linear.md#AllGatherLinear), [`r_dim`](attention.md#FusedQKVLinear.r_dim)
- used by: [`make_gqa_config`](config_utils.md#make_gqa_config), [`FusedQKVLinear`](attention.md#FusedQKVLinear), [`forward`](attention.md#FusedQKVLinear.forward)

### <a id="AllGatherFusedQKVLinear.Config"></a>`AllGatherFusedQKVLinear.Config`  ·  implements/extends Config
- def: [`torchtitan/models/common/dist_gemm.py:117`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/dist_gemm.py#L117)
- doc: Same fields as the stock fused QKV. The subclass exists because it is
- signature: `class Config(FusedQKVLinear.Config):`
- uses (calls/refs, reference-scoped): [`FusedQKVLinear`](attention.md#FusedQKVLinear), [`Config`](attention.md#FusedQKVLinear.Config)
- used by: [`make_gqa_config`](config_utils.md#make_gqa_config)

### <a id="DistGEMMFeedForward"></a>`DistGEMMFeedForward`  ·  implements/extends FeedForward
- def: [`torchtitan/models/common/dist_gemm.py:178`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/dist_gemm.py#L178)
- doc: SwiGLU feed-forward with both TP collectives folded into its GEMMs.
- signature: `class DistGEMMFeedForward(FeedForward):`
- members:
  - <a id="DistGEMMFeedForward.forward"></a>`forward(self, x: torch.Tensor)` — [`L210`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/dist_gemm.py#L210)
- uses (calls/refs, reference-scoped): [`FeedForward`](feed_forward.md#FeedForward), [`forward`](feed_forward.md#FeedForward.forward), [`_warn_once_unfused`](dist_gemm.md#_warn_once_unfused), [`w2`](feed_forward.md#FeedForward.w2), [`w1`](feed_forward.md#FeedForward.w1), [`w3`](feed_forward.md#FeedForward.w3), [`_tp_group_from_context`](dist_gemm.md#_tp_group_from_context), [`LinearReduceScatter`](../../distributed/linear.md#LinearReduceScatter), [`AllGatherLinearMulti`](../../distributed/linear.md#AllGatherLinearMulti)
- used by: [`FeedForward`](feed_forward.md#FeedForward), [`make_ffn_config`](config_utils.md#make_ffn_config), [`set_dense_ffn_sharding`](decoder_sharding.md#set_dense_ffn_sharding), [`forward`](feed_forward.md#FeedForward.forward), [`dist_gemm_fused_swiglu`](../../overrides/fused_swiglu.md#dist_gemm_fused_swiglu)

### <a id="DistGEMMFeedForward.Config"></a>`DistGEMMFeedForward.Config`  ·  implements/extends Config
- def: [`torchtitan/models/common/dist_gemm.py:192`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/dist_gemm.py#L192)
- doc: Same fields as the stock FFN. The subclass exists because it is what
- signature: `class Config(FeedForward.Config):`
- protocol/private: <a id="DistGEMMFeedForward.Config.__post_init__"></a>`__post_init__`[`L197`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/dist_gemm.py#L197)
- uses (calls/refs, reference-scoped): [`bias`](linear.md#Linear.Config.bias), [`FeedForward`](feed_forward.md#FeedForward), [`Config`](feed_forward.md#FeedForward.Config), [`w1`](feed_forward.md#FeedForward.Config.w1), [`w3`](feed_forward.md#FeedForward.Config.w3)
- used by: [`make_ffn_config`](config_utils.md#make_ffn_config), [`set_dense_ffn_sharding`](decoder_sharding.md#set_dense_ffn_sharding), [`dist_gemm_fused_swiglu`](../../overrides/fused_swiglu.md#dist_gemm_fused_swiglu)

### <a id="RowParallelLinear"></a>`RowParallelLinear`  ·  implements/extends Linear
- def: [`torchtitan/models/common/dist_gemm.py:148`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/dist_gemm.py#L148)
- doc: Attention output projection: matmul fused with the TP reduce-scatter.
- signature: `class RowParallelLinear(Linear):`
- members:
  - <a id="RowParallelLinear.forward"></a>`forward(self, input: torch.Tensor)` — [`L163`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/dist_gemm.py#L163)
- uses (calls/refs, reference-scoped): [`Linear`](linear.md#Linear), [`_warn_once_unfused`](dist_gemm.md#_warn_once_unfused), [`_tp_group_from_context`](dist_gemm.md#_tp_group_from_context), [`LinearReduceScatter`](../../distributed/linear.md#LinearReduceScatter)
- used by: [`Linear`](linear.md#Linear), [`make_gqa_config`](config_utils.md#make_gqa_config), [`set_gqa_attention_sharding`](decoder_sharding.md#set_gqa_attention_sharding)

### <a id="RowParallelLinear.Config"></a>`RowParallelLinear.Config`  ·  implements/extends Config
- def: [`torchtitan/models/common/dist_gemm.py:158`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/dist_gemm.py#L158)
- doc: Same fields as a stock Linear. The subclass exists because it is what
- signature: `class Config(Linear.Config):`
- uses (calls/refs, reference-scoped): [`Linear`](linear.md#Linear), [`Config`](linear.md#Linear.Config)
- used by: [`make_gqa_config`](config_utils.md#make_gqa_config), [`set_gqa_attention_sharding`](decoder_sharding.md#set_gqa_attention_sharding)

## Functions
- <a id="_tp_group_from_context"></a>`_tp_group_from_context()` — [`L70`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/dist_gemm.py#L70) — The TP process group from the current spmd_types mesh context, or None.
- <a id="_warn_once_unfused"></a>`_warn_once_unfused()` — [`L53`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/dist_gemm.py#L53) — Say so when the fused modules were selected but TP is not on.
- <a id="validate_dist_gemm_preconditions"></a>`validate_dist_gemm_preconditions(*, enable_sp: bool)` — [`L88`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/dist_gemm.py#L88) — Reject configurations the fused modules cannot serve.

## Module values
- <a id="_WARNED_NO_TP"></a>`_WARNED_NO_TP` — [`L50`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/dist_gemm.py#L50)
- <a id="__all__"></a>`__all__` — [`L234`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/dist_gemm.py#L234)

