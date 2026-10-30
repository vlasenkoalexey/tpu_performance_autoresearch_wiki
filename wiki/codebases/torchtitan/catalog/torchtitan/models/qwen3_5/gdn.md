---
title: 'Module: torchtitan/models/qwen3_5/gdn.py'
type: catalog
provenance: extracted
module: torchtitan/models/qwen3_5/gdn.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.models.qwen3_5.gdn`/
symbols:
  GatedDeltaNet.forward: GatedDeltaNet#forward().
  GatedDeltaNet: GatedDeltaNet#
  GatedDeltaNet.Config: GatedDeltaNet#Config#
  GatedDeltaNet.value_head_dim: GatedDeltaNet#value_head_dim.
  GatedDeltaKernel: GatedDeltaKernel#
  InnerGatedDeltaNet: InnerGatedDeltaNet#
  InnerGatedDeltaNet.forward: InnerGatedDeltaNet#forward().
  GatedDeltaNet.conv_v: GatedDeltaNet#conv_v.
  GatedDeltaKernel.Config: GatedDeltaKernel#Config#
  GatedDeltaNet.Config.in_proj_v: GatedDeltaNet#Config#in_proj_v.
  GatedDeltaNet.Config.conv_q: GatedDeltaNet#Config#conv_q.
  GatedDeltaNet.Config.conv_k: GatedDeltaNet#Config#conv_k.
  GatedDeltaNet.Config.conv_v: GatedDeltaNet#Config#conv_v.
  RMSNormGated.Config: RMSNormGated#Config#
  InnerGatedDeltaNet.Config: InnerGatedDeltaNet#Config#
  InnerGatedDeltaNet.Config.kernel: InnerGatedDeltaNet#Config#kernel.
  GatedDeltaNet.Config.inner_gated_delta_net: GatedDeltaNet#Config#inner_gated_delta_net.
  GatedDeltaNet.Config.norm: GatedDeltaNet#Config#norm.
  GatedDeltaNet.Config.out_proj: GatedDeltaNet#Config#out_proj.
  GatedDeltaKernel.forward: GatedDeltaKernel#forward().
  InnerGatedDeltaNet.kernel: InnerGatedDeltaNet#kernel.
  GatedDeltaNet.in_proj_q: GatedDeltaNet#in_proj_q.
  GatedDeltaNet.in_proj_k: GatedDeltaNet#in_proj_k.
  GatedDeltaNet.in_proj_v: GatedDeltaNet#in_proj_v.
  GatedDeltaNet.in_proj_z: GatedDeltaNet#in_proj_z.
  GatedDeltaNet.in_proj_a: GatedDeltaNet#in_proj_a.
  GatedDeltaNet.in_proj_b: GatedDeltaNet#in_proj_b.
  GatedDeltaNet.inner_gated_delta_net: GatedDeltaNet#inner_gated_delta_net.
  GatedDeltaNet.conv_q: GatedDeltaNet#conv_q.
  GatedDeltaNet.conv_k: GatedDeltaNet#conv_k.
  GatedDeltaNet.norm: GatedDeltaNet#norm.
  GatedDeltaNet.out_proj: GatedDeltaNet#out_proj.
  GatedDeltaNet.Config.in_proj_q: GatedDeltaNet#Config#in_proj_q.
  GatedDeltaNet.Config.in_proj_k: GatedDeltaNet#Config#in_proj_k.
  GatedDeltaNet.Config.in_proj_z: GatedDeltaNet#Config#in_proj_z.
  GatedDeltaNet.Config.in_proj_a: GatedDeltaNet#Config#in_proj_a.
  GatedDeltaNet.Config.in_proj_b: GatedDeltaNet#Config#in_proj_b.
  RMSNormGated: RMSNormGated#
  InnerGatedDeltaNet.causal_conv: InnerGatedDeltaNet#causal_conv().
  RMSNormGated.forward: RMSNormGated#forward().
  GatedDeltaNet.Config.value_head_dim: GatedDeltaNet#Config#value_head_dim.
  GatedDeltaNet.key_head_dim: GatedDeltaNet#key_head_dim.
  RMSNormGated.eps: RMSNormGated#eps.
  RMSNormGated.weight: RMSNormGated#weight.
  _recurrent_gdn_backward: _recurrent_gdn_backward().
  GatedDeltaKernel.__init__: GatedDeltaKernel#__init__().
  _recurrent_gdn_fwd: _recurrent_gdn_fwd().
  GatedDeltaNet.Config.key_head_dim: GatedDeltaNet#Config#key_head_dim.
  RMSNormGated.__init__: RMSNormGated#__init__().
  _recurrent_gdn_fwd_fake: _recurrent_gdn_fwd_fake().
  InnerGatedDeltaNet.__init__: InnerGatedDeltaNet#__init__().
  GatedDeltaNet.__init__: GatedDeltaNet#__init__().
  GatedDeltaNet.A_log: GatedDeltaNet#A_log.
  GatedDeltaNet.dt_bias: GatedDeltaNet#dt_bias.
  RMSNormGated.Config.dim: RMSNormGated#Config#dim.
  RMSNormGated.Config.eps: RMSNormGated#Config#eps.
  _causal_conv1d_varlen: _causal_conv1d_varlen().
  _chunk_gdn_gradients: _chunk_gdn_gradients().
  _recurrent_gdn_setup_context: _recurrent_gdn_setup_context().
  GatedDeltaNet.Config.conv_kernel_size: GatedDeltaNet#Config#conv_kernel_size.
---
# Module: [`torchtitan/models/qwen3_5/gdn.py`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/gdn.py)

## Classes
### <a id="GatedDeltaKernel"></a>`GatedDeltaKernel`  ·  implements/extends Module
- def: [`torchtitan/models/qwen3_5/gdn.py:207`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/gdn.py#L207)
- doc: Run GDN on rank-local tensors.
- signature: `class GatedDeltaKernel(Module):`
- members:
  - <a id="GatedDeltaKernel.forward"></a>`forward(self, xq_THK: torch.Tensor, xk_THK: torch.Tensor, xv_THV: torch.Tensor, g_TH: torch.Tensor, beta_TH: torch.Tensor, *, cu_seqlens: torch.Tensor | None = None)` — [`L222`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/gdn.py#L222)
- protocol/private: <a id="GatedDeltaKernel.__init__"></a>`__init__`[`L219`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/gdn.py#L219)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`is_in_batch_invariant_mode`](../../distributed/utils.md#is_in_batch_invariant_mode), [`Config`](gdn.md#GatedDeltaKernel.Config), [`forward`](../../experiments/tpu/qwen3_5/gated_delta.md#TpuGatedDeltaKernel.forward), [`TpuGatedDeltaKernel`](../../experiments/tpu/qwen3_5/gated_delta.md#TpuGatedDeltaKernel), [`_recurrent_gdn_fwd`](gdn.md#_recurrent_gdn_fwd)
- used by: [`Module`](../../protocols/module.md#Module), [`_qwen35_deltanet_config`](__init__.md#_qwen35_deltanet_config), [`kernel`](gdn.md#InnerGatedDeltaNet.Config.kernel), [`Config`](../../experiments/tpu/qwen3_5/gated_delta.md#TpuGatedDeltaKernel.Config), [`__init__`](../../experiments/tpu/qwen3_5/gated_delta.md#TpuGatedDeltaKernel.__init__), [`TpuGatedDeltaKernel`](../../experiments/tpu/qwen3_5/gated_delta.md#TpuGatedDeltaKernel)

### <a id="GatedDeltaKernel.Config"></a>`GatedDeltaKernel.Config`  ·  implements/extends Config
- def: [`torchtitan/models/qwen3_5/gdn.py:216`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/gdn.py#L216)
- signature: `class Config(Module.Config):`
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`Config`](../../protocols/module.md#Module.Config)
- used by: [`_qwen35_deltanet_config`](__init__.md#_qwen35_deltanet_config), [`kernel`](gdn.md#InnerGatedDeltaNet.Config.kernel), [`Config`](../../experiments/tpu/qwen3_5/gated_delta.md#TpuGatedDeltaKernel.Config), [`__init__`](gdn.md#GatedDeltaKernel.__init__)

### <a id="GatedDeltaNet"></a>`GatedDeltaNet`  ·  implements/extends Module
- def: [`torchtitan/models/qwen3_5/gdn.py:349`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/gdn.py#L349)
- doc: Gated DeltaNet linear attention.
- signature: `class GatedDeltaNet(Module):`
- members:
  - <a id="GatedDeltaNet.forward"></a>`forward(self, x_TD: torch.Tensor, attention_masks: VarlenMetadata | None = None)` — [`L406`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/gdn.py#L406)
  - <a id="GatedDeltaNet.A_log"></a>`A_log` — [`L399`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/gdn.py#L399)
  - <a id="GatedDeltaNet.conv_k"></a>`conv_k` — [`L395`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/gdn.py#L395)
  - <a id="GatedDeltaNet.conv_q"></a>`conv_q` — [`L394`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/gdn.py#L394)
  - <a id="GatedDeltaNet.conv_v"></a>`conv_v` — [`L396`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/gdn.py#L396)
  - <a id="GatedDeltaNet.dt_bias"></a>`dt_bias` — [`L400`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/gdn.py#L400)
  - <a id="GatedDeltaNet.in_proj_a"></a>`in_proj_a` — [`L391`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/gdn.py#L391)
  - <a id="GatedDeltaNet.in_proj_b"></a>`in_proj_b` — [`L392`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/gdn.py#L392)
  - <a id="GatedDeltaNet.in_proj_k"></a>`in_proj_k` — [`L388`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/gdn.py#L388)
  - <a id="GatedDeltaNet.in_proj_q"></a>`in_proj_q` — [`L387`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/gdn.py#L387)
  - <a id="GatedDeltaNet.in_proj_v"></a>`in_proj_v` — [`L389`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/gdn.py#L389)
  - <a id="GatedDeltaNet.in_proj_z"></a>`in_proj_z` — [`L390`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/gdn.py#L390)
  - <a id="GatedDeltaNet.inner_gated_delta_net"></a>`inner_gated_delta_net` — [`L404`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/gdn.py#L404)
  - <a id="GatedDeltaNet.key_head_dim"></a>`key_head_dim` — [`L383`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/gdn.py#L383)
  - <a id="GatedDeltaNet.norm"></a>`norm` — [`L402`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/gdn.py#L402)
  - <a id="GatedDeltaNet.out_proj"></a>`out_proj` — [`L403`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/gdn.py#L403)
  - <a id="GatedDeltaNet.value_head_dim"></a>`value_head_dim` — [`L384`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/gdn.py#L384)
- protocol/private: <a id="GatedDeltaNet.__init__"></a>`__init__`[`L381`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/gdn.py#L381)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`build`](../../protocols/module.md#Module.Config.build), [`out_features`](../common/linear.md#Linear.Config.out_features), [`forward`](../../experiments/tpu/qwen3_5/gated_delta.md#TpuGatedDeltaNet.forward), [`VarlenMetadata`](../common/attention.md#VarlenMetadata), [`Config`](gdn.md#GatedDeltaNet.Config), [`conv_k`](gdn.md#GatedDeltaNet.Config.conv_k), [`conv_q`](gdn.md#GatedDeltaNet.Config.conv_q), [`conv_v`](gdn.md#GatedDeltaNet.Config.conv_v), [`in_proj_v`](gdn.md#GatedDeltaNet.Config.in_proj_v), [`inner_gated_delta_net`](gdn.md#GatedDeltaNet.Config.inner_gated_delta_net), [`norm`](gdn.md#GatedDeltaNet.Config.norm), [`out_proj`](gdn.md#GatedDeltaNet.Config.out_proj), [`cu_seq_q`](../common/attention.md#VarlenMetadata.cu_seq_q), [`in_proj_a`](gdn.md#GatedDeltaNet.Config.in_proj_a), [`in_proj_b`](gdn.md#GatedDeltaNet.Config.in_proj_b), [`in_proj_k`](gdn.md#GatedDeltaNet.Config.in_proj_k), [`in_proj_q`](gdn.md#GatedDeltaNet.Config.in_proj_q), [`in_proj_z`](gdn.md#GatedDeltaNet.Config.in_proj_z), [`TpuGatedDeltaNet`](../../experiments/tpu/qwen3_5/gated_delta.md#TpuGatedDeltaNet), [`value_head_dim`](gdn.md#GatedDeltaNet.Config.value_head_dim), [`key_head_dim`](gdn.md#GatedDeltaNet.Config.key_head_dim)
- used by: [`Module`](../../protocols/module.md#Module), [`_qwen35_deltanet_config`](__init__.md#_qwen35_deltanet_config), [`_set_deltanet_sharding`](sharding.md#_set_deltanet_sharding), [`forward`](../../experiments/tpu/qwen3_5/gated_delta.md#TpuGatedDeltaNet.forward), [`get_nparams_and_flops`](model.md#Qwen35Model.Config.get_nparams_and_flops), [`TP`](sharding.md#TP), [`delta_net`](model.md#Qwen35TransformerBlock.Config.delta_net), [`Config`](../../experiments/tpu/qwen3_5/gated_delta.md#TpuGatedDeltaNet.Config), [`TpuGatedDeltaNet`](../../experiments/tpu/qwen3_5/gated_delta.md#TpuGatedDeltaNet)

### <a id="GatedDeltaNet.Config"></a>`GatedDeltaNet.Config`  ·  implements/extends Config
- def: [`torchtitan/models/qwen3_5/gdn.py:362`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/gdn.py#L362)
- signature: `class Config(Module.Config):`
- members:
  - <a id="GatedDeltaNet.Config.conv_k"></a>`conv_k` — [`L375`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/gdn.py#L375)
  - <a id="GatedDeltaNet.Config.conv_kernel_size"></a>`conv_kernel_size` — [`L365`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/gdn.py#L365)
  - <a id="GatedDeltaNet.Config.conv_q"></a>`conv_q` — [`L374`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/gdn.py#L374)
  - <a id="GatedDeltaNet.Config.conv_v"></a>`conv_v` — [`L376`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/gdn.py#L376)
  - <a id="GatedDeltaNet.Config.in_proj_a"></a>`in_proj_a` — [`L372`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/gdn.py#L372)
  - <a id="GatedDeltaNet.Config.in_proj_b"></a>`in_proj_b` — [`L373`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/gdn.py#L373)
  - <a id="GatedDeltaNet.Config.in_proj_k"></a>`in_proj_k` — [`L369`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/gdn.py#L369)
  - <a id="GatedDeltaNet.Config.in_proj_q"></a>`in_proj_q` — [`L368`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/gdn.py#L368)
  - <a id="GatedDeltaNet.Config.in_proj_v"></a>`in_proj_v` — [`L370`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/gdn.py#L370)
  - <a id="GatedDeltaNet.Config.in_proj_z"></a>`in_proj_z` — [`L371`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/gdn.py#L371)
  - <a id="GatedDeltaNet.Config.inner_gated_delta_net"></a>`inner_gated_delta_net` — [`L377`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/gdn.py#L377)
  - <a id="GatedDeltaNet.Config.key_head_dim"></a>`key_head_dim` — [`L363`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/gdn.py#L363)
  - <a id="GatedDeltaNet.Config.norm"></a>`norm` — [`L378`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/gdn.py#L378)
  - <a id="GatedDeltaNet.Config.out_proj"></a>`out_proj` — [`L379`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/gdn.py#L379)
  - <a id="GatedDeltaNet.Config.value_head_dim"></a>`value_head_dim` — [`L364`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/gdn.py#L364)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`Linear`](../common/linear.md#Linear), [`Config`](../common/linear.md#Linear.Config), [`Config`](../../protocols/module.md#Module.Config), [`Conv1d`](../common/nn_modules.md#Conv1d), [`Config`](../common/nn_modules.md#Conv1d.Config), [`Config`](gdn.md#RMSNormGated.Config), [`RMSNormGated`](gdn.md#RMSNormGated)
- used by: [`_qwen35_deltanet_config`](__init__.md#_qwen35_deltanet_config), [`_set_deltanet_sharding`](sharding.md#_set_deltanet_sharding), [`use_tpu_modules`](../../experiments/tpu/qwen3_5/__init__.md#use_tpu_modules), [`get_nparams_and_flops`](model.md#Qwen35Model.Config.get_nparams_and_flops), [`value_head_dim`](gdn.md#GatedDeltaNet.value_head_dim), [`delta_net`](model.md#Qwen35TransformerBlock.Config.delta_net), [`conv_v`](gdn.md#GatedDeltaNet.conv_v), [`Config`](../../experiments/tpu/qwen3_5/gated_delta.md#TpuGatedDeltaNet.Config), [`conv_k`](gdn.md#GatedDeltaNet.conv_k), [`conv_q`](gdn.md#GatedDeltaNet.conv_q), [`in_proj_a`](gdn.md#GatedDeltaNet.in_proj_a), [`in_proj_b`](gdn.md#GatedDeltaNet.in_proj_b), [`in_proj_k`](gdn.md#GatedDeltaNet.in_proj_k), [`in_proj_q`](gdn.md#GatedDeltaNet.in_proj_q), [`in_proj_v`](gdn.md#GatedDeltaNet.in_proj_v), [`in_proj_z`](gdn.md#GatedDeltaNet.in_proj_z), [`inner_gated_delta_net`](gdn.md#GatedDeltaNet.inner_gated_delta_net), [`norm`](gdn.md#GatedDeltaNet.norm), [`out_proj`](gdn.md#GatedDeltaNet.out_proj), [`key_head_dim`](gdn.md#GatedDeltaNet.key_head_dim), [`__init__`](gdn.md#GatedDeltaNet.__init__)

### <a id="InnerGatedDeltaNet"></a>`InnerGatedDeltaNet`  ·  implements/extends Module
- def: [`torchtitan/models/qwen3_5/gdn.py:263`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/gdn.py#L263)
- doc: Dense GDN computation behind the vLLM replacement boundary.
- signature: `class InnerGatedDeltaNet(Module):`
- members:
  - <a id="InnerGatedDeltaNet.causal_conv"></a>`causal_conv(x_TC: torch.Tensor, weight_C1W: torch.Tensor)` — [`L300`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/gdn.py#L300)
  - <a id="InnerGatedDeltaNet.forward"></a>`forward(self, query_TC: torch.Tensor, key_TC: torch.Tensor, value_TC: torch.Tensor, a_TH: torch.Tensor, b_TH: torch.Tensor, conv_q_weight_C1W: torch.Tensor, conv_k_weight_C1W: torch.Tensor, conv_v_weight_C1W: torch.Tensor, A_log_H: torch.Tensor, dt_bias_H: torch.Tensor, cu_seqlens: torch.Tensor, *, key_head_dim: int, value_head_dim: int)` — [`L279`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/gdn.py#L279) — Run separate Q/K/V convolutions and recurrence on local heads.
  - <a id="InnerGatedDeltaNet.kernel"></a>`kernel` — [`L277`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/gdn.py#L277)
- protocol/private: <a id="InnerGatedDeltaNet.__init__"></a>`__init__`[`L275`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/gdn.py#L275)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`build`](../../protocols/module.md#Module.Config.build), [`is_in_batch_invariant_mode`](../../distributed/utils.md#is_in_batch_invariant_mode), [`forward`](../../experiments/tpu/qwen3_5/gated_delta.md#TpuInnerGatedDeltaNet.forward), [`Config`](gdn.md#InnerGatedDeltaNet.Config), [`kernel`](gdn.md#InnerGatedDeltaNet.Config.kernel), [`TpuInnerGatedDeltaNet`](../../experiments/tpu/qwen3_5/gated_delta.md#TpuInnerGatedDeltaNet), [`_causal_conv1d_varlen`](gdn.md#_causal_conv1d_varlen)
- used by: [`Module`](../../protocols/module.md#Module), [`_qwen35_deltanet_config`](__init__.md#_qwen35_deltanet_config), [`forward`](../../experiments/tpu/qwen3_5/gated_delta.md#TpuInnerGatedDeltaNet.forward), [`Config`](../../experiments/tpu/qwen3_5/gated_delta.md#TpuInnerGatedDeltaNet.Config), [`TpuInnerGatedDeltaNet`](../../experiments/tpu/qwen3_5/gated_delta.md#TpuInnerGatedDeltaNet)

### <a id="InnerGatedDeltaNet.Config"></a>`InnerGatedDeltaNet.Config`  ·  implements/extends Config
- def: [`torchtitan/models/qwen3_5/gdn.py:272`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/gdn.py#L272)
- signature: `class Config(Module.Config):`
- members:
  - <a id="InnerGatedDeltaNet.Config.kernel"></a>`kernel` — [`L273`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/gdn.py#L273)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`Config`](../../protocols/module.md#Module.Config), [`GatedDeltaKernel`](gdn.md#GatedDeltaKernel), [`Config`](gdn.md#GatedDeltaKernel.Config)
- used by: [`_qwen35_deltanet_config`](__init__.md#_qwen35_deltanet_config), [`use_tpu_modules`](../../experiments/tpu/qwen3_5/__init__.md#use_tpu_modules), [`Config`](../../experiments/tpu/qwen3_5/gated_delta.md#TpuInnerGatedDeltaNet.Config), [`kernel`](gdn.md#InnerGatedDeltaNet.kernel), [`__init__`](gdn.md#InnerGatedDeltaNet.__init__)

### <a id="RMSNormGated"></a>`RMSNormGated`  ·  implements/extends Module
- def: [`torchtitan/models/qwen3_5/gdn.py:56`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/gdn.py#L56)
- doc: Gated RMSNorm: `silu(gate) * weight * norm(x)`.
- signature: `class RMSNormGated(Module):`
- members:
  - <a id="RMSNormGated.forward"></a>`forward(self, x: torch.Tensor, gate: torch.Tensor)` — [`L72`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/gdn.py#L72)
  - <a id="RMSNormGated.eps"></a>`eps` — [`L69`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/gdn.py#L69)
  - <a id="RMSNormGated.weight"></a>`weight` — [`L70`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/gdn.py#L70)
- protocol/private: <a id="RMSNormGated.__init__"></a>`__init__`[`L67`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/gdn.py#L67)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`Config`](gdn.md#RMSNormGated.Config), [`dim`](gdn.md#RMSNormGated.Config.dim), [`eps`](gdn.md#RMSNormGated.Config.eps)
- used by: [`Module`](../../protocols/module.md#Module), [`_qwen35_deltanet_config`](__init__.md#_qwen35_deltanet_config), [`norm`](gdn.md#GatedDeltaNet.Config.norm)

### <a id="RMSNormGated.Config"></a>`RMSNormGated.Config`  ·  implements/extends Config
- def: [`torchtitan/models/qwen3_5/gdn.py:63`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/gdn.py#L63)
- signature: `class Config(Module.Config):`
- members:
  - <a id="RMSNormGated.Config.dim"></a>`dim` — [`L64`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/gdn.py#L64)
  - <a id="RMSNormGated.Config.eps"></a>`eps` — [`L65`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/gdn.py#L65)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`Config`](../../protocols/module.md#Module.Config)
- used by: [`_qwen35_deltanet_config`](__init__.md#_qwen35_deltanet_config), [`norm`](gdn.md#GatedDeltaNet.Config.norm), [`eps`](gdn.md#RMSNormGated.eps), [`weight`](gdn.md#RMSNormGated.weight), [`__init__`](gdn.md#RMSNormGated.__init__)

## Functions
- <a id="_causal_conv1d_varlen"></a>`_causal_conv1d_varlen(x_TD: torch.Tensor, weight: torch.Tensor, cu_seqlens: torch.Tensor)` — [`L36`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/gdn.py#L36) — Depthwise causal conv with per-document resets (CUDA-only).
- <a id="_chunk_gdn_gradients"></a>`_chunk_gdn_gradients(grad_output: torch.Tensor, q: torch.Tensor, k: torch.Tensor, v: torch.Tensor, g: torch.Tensor, beta: torch.Tensor, cu_seqlens: torch.Tensor)` — [`L152`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/gdn.py#L152) — Recompute the parallel GDN chunk kernel and return its gradients.
- <a id="_recurrent_gdn_backward"></a>`_recurrent_gdn_backward(ctx, grad_output)` — [`L188`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/gdn.py#L188)
- <a id="_recurrent_gdn_fwd"></a>`_recurrent_gdn_fwd(q_BTHK: torch.Tensor, k_BTHK: torch.Tensor, v_BTHV: torch.Tensor, g: torch.Tensor, beta: torch.Tensor, cu_seqlens: torch.Tensor)` — [`L86`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/gdn.py#L86) — Run the batch-invariant GDN recurrent forward kernel.
- <a id="_recurrent_gdn_fwd_fake"></a>`_recurrent_gdn_fwd_fake(q_BTHK: torch.Tensor, k_BTHK: torch.Tensor, v_BTHV: torch.Tensor, g: torch.Tensor, beta: torch.Tensor, cu_seqlens: torch.Tensor)` — [`L141`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/gdn.py#L141)
- <a id="_recurrent_gdn_setup_context"></a>`_recurrent_gdn_setup_context(ctx, inputs, output)` — [`L184`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/gdn.py#L184)

