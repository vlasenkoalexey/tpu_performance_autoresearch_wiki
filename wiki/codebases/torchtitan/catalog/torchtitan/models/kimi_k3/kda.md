---
title: 'Module: torchtitan/models/kimi_k3/kda.py'
type: catalog
provenance: extracted
module: torchtitan/models/kimi_k3/kda.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.models.kimi_k3.kda`/
symbols:
  KDA.forward: KDA#forward().
  KDA.Config: KDA#Config#
  KDA: KDA#
  KimiRMSNormGated.Config: KimiRMSNormGated#Config#
  KDAKernel.Config: KDAKernel#Config#
  KDA.Config.num_heads: KDA#Config#num_heads.
  KDA.Config.head_dim: KDA#Config#head_dim.
  KDA.Config.inner_kda: KDA#Config#inner_kda.
  KDA.Config.__post_init__: KDA#Config#__post_init__().
  InnerKDA.Config: InnerKDA#Config#
  InnerKDA.Config.kernel: InnerKDA#Config#kernel.
  KDA.Config.q_proj: KDA#Config#q_proj.
  KDA.Config.k_proj: KDA#Config#k_proj.
  KDA.Config.v_proj: KDA#Config#v_proj.
  KDA.Config.q_conv: KDA#Config#q_conv.
  KDA.Config.k_conv: KDA#Config#k_conv.
  KDA.Config.v_conv: KDA#Config#v_conv.
  KDA.Config.forget_a: KDA#Config#forget_a.
  KDA.Config.forget_b: KDA#Config#forget_b.
  KDA.Config.beta: KDA#Config#beta.
  KDA.Config.output_gate: KDA#Config#output_gate.
  KDA.Config.output_norm: KDA#Config#output_norm.
  KDA.Config.output_proj: KDA#Config#output_proj.
  InnerKDA.kernel: InnerKDA#kernel.
  KDA.q_proj: KDA#q_proj.
  KDA.k_proj: KDA#k_proj.
  KDA.v_proj: KDA#v_proj.
  KDA.q_conv: KDA#q_conv.
  KDA.k_conv: KDA#k_conv.
  KDA.v_conv: KDA#v_conv.
  KDA.forget_a: KDA#forget_a.
  KDA.forget_b: KDA#forget_b.
  KDA.beta: KDA#beta.
  KDA.output_gate: KDA#output_gate.
  KDA.inner_kda: KDA#inner_kda.
  KDA.output_norm: KDA#output_norm.
  KDA.output_proj: KDA#output_proj.
  KDA.dt_bias: KDA#dt_bias.
  KimiRMSNormGated: KimiRMSNormGated#
  KDAKernel: KDAKernel#
  KimiRMSNormGated.forward: KimiRMSNormGated#forward().
  InnerKDA.forward: InnerKDA#forward().
  InnerKDA: InnerKDA#
  KDA.num_heads: KDA#num_heads.
  InnerKDA.Config.head_dim: InnerKDA#Config#head_dim.
  KimiRMSNormGated.eps: KimiRMSNormGated#eps.
  KimiRMSNormGated.weight: KimiRMSNormGated#weight.
  KDAKernel.lower_bound: KDAKernel#lower_bound.
  InnerKDA.head_dim: InnerKDA#head_dim.
  KDA.head_dim: KDA#head_dim.
  KDA.A_log: KDA#A_log.
  KDAKernel.Config.lower_bound: KDAKernel#Config#lower_bound.
  KDA.Config.conv_kernel_size: KDA#Config#conv_kernel_size.
  KimiRMSNormGated.__init__: KimiRMSNormGated#__init__().
  KDAKernel.Config.__post_init__: KDAKernel#Config#__post_init__().
  KDAKernel.__init__: KDAKernel#__init__().
  KDAKernel.forward: KDAKernel#forward().
  InnerKDA.Config.__post_init__: InnerKDA#Config#__post_init__().
  InnerKDA.__init__: InnerKDA#__init__().
  KDA.__init__: KDA#__init__().
  KimiRMSNormGated.Config.dim: KimiRMSNormGated#Config#dim.
  KimiRMSNormGated.Config.eps: KimiRMSNormGated#Config#eps.
---
# Module: [`torchtitan/models/kimi_k3/kda.py`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/kda.py)

## Classes
### <a id="InnerKDA"></a>`InnerKDA`  ·  implements/extends Module
- def: [`torchtitan/models/kimi_k3/kda.py:112`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/kda.py#L112)
- doc: Run short convolution and KDA behind the vLLM replacement boundary.
- signature: `class InnerKDA(Module):`
- members:
  - <a id="InnerKDA.forward"></a>`forward(self, query_TC: torch.Tensor, key_TC: torch.Tensor, value_TC: torch.Tensor, raw_gate_THK: torch.Tensor, raw_beta_TH: torch.Tensor, conv_q_weight_C1W: torch.Tensor, conv_k_weight_C1W: torch.Tensor, conv_v_weight_C1W: torch.Tensor, A_log_H: torch.Tensor, dt_bias_HK: torch.Tensor, *, cu_seqlens: torch.Tensor | None)` — [`L131`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/kda.py#L131)
  - <a id="InnerKDA.head_dim"></a>`head_dim` — [`L128`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/kda.py#L128)
  - <a id="InnerKDA.kernel"></a>`kernel` — [`L129`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/kda.py#L129)
- protocol/private: <a id="InnerKDA.__init__"></a>`__init__`[`L126`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/kda.py#L126)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`build`](../../protocols/module.md#Module.Config.build), [`Config`](kda.md#InnerKDA.Config), [`kernel`](kda.md#InnerKDA.Config.kernel), [`head_dim`](kda.md#InnerKDA.Config.head_dim)
- used by: [`Module`](../../protocols/module.md#Module), [`_kda_config`](__init__.md#_kda_config)

### <a id="InnerKDA.Config"></a>`InnerKDA.Config`  ·  implements/extends Config
- def: [`torchtitan/models/kimi_k3/kda.py:116`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/kda.py#L116)
- signature: `class Config(Module.Config):`
- members:
  - <a id="InnerKDA.Config.head_dim"></a>`head_dim` — [`L117`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/kda.py#L117)
  - <a id="InnerKDA.Config.kernel"></a>`kernel` — [`L118`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/kda.py#L118)
- protocol/private: <a id="InnerKDA.Config.__post_init__"></a>`__post_init__`[`L120`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/kda.py#L120)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`Config`](../../protocols/module.md#Module.Config), [`Config`](kda.md#KDAKernel.Config), [`KDAKernel`](kda.md#KDAKernel)
- used by: [`_kda_config`](__init__.md#_kda_config), [`kernel`](kda.md#InnerKDA.kernel), [`head_dim`](kda.md#InnerKDA.head_dim), [`__init__`](kda.md#InnerKDA.__init__)

### <a id="KDA"></a>`KDA`  ·  implements/extends Module
- def: [`torchtitan/models/kimi_k3/kda.py:182`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/kda.py#L182)
- doc: Kimi Delta Attention with checkpoint-compatible Kimi K3 parameters.
- signature: `class KDA(Module):`
- members:
  - <a id="KDA.forward"></a>`forward(self, x_TD: torch.Tensor, attention_masks: AttentionMasksType | None = None, positions: torch.Tensor | None = None)` — [`L238`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/kda.py#L238) — documented in [kimi-k3-model](../../../../concepts/kimi-k3-model.md)
  - <a id="KDA.A_log"></a>`A_log` — [`L235`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/kda.py#L235)
  - <a id="KDA.beta"></a>`beta` — [`L229`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/kda.py#L229)
  - <a id="KDA.dt_bias"></a>`dt_bias` — [`L236`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/kda.py#L236)
  - <a id="KDA.forget_a"></a>`forget_a` — [`L227`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/kda.py#L227)
  - <a id="KDA.forget_b"></a>`forget_b` — [`L228`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/kda.py#L228)
  - <a id="KDA.head_dim"></a>`head_dim` — [`L219`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/kda.py#L219)
  - <a id="KDA.inner_kda"></a>`inner_kda` — [`L231`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/kda.py#L231)
  - <a id="KDA.k_conv"></a>`k_conv` — [`L225`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/kda.py#L225)
  - <a id="KDA.k_proj"></a>`k_proj` — [`L222`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/kda.py#L222)
  - <a id="KDA.num_heads"></a>`num_heads` — [`L218`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/kda.py#L218)
  - <a id="KDA.output_gate"></a>`output_gate` — [`L230`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/kda.py#L230)
  - <a id="KDA.output_norm"></a>`output_norm` — [`L232`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/kda.py#L232)
  - <a id="KDA.output_proj"></a>`output_proj` — [`L233`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/kda.py#L233)
  - <a id="KDA.q_conv"></a>`q_conv` — [`L224`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/kda.py#L224)
  - <a id="KDA.q_proj"></a>`q_proj` — [`L221`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/kda.py#L221)
  - <a id="KDA.v_conv"></a>`v_conv` — [`L226`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/kda.py#L226)
  - <a id="KDA.v_proj"></a>`v_proj` — [`L223`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/kda.py#L223)
- protocol/private: <a id="KDA.__init__"></a>`__init__`[`L216`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/kda.py#L216)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`build`](../../protocols/module.md#Module.Config.build), [`AttentionMasksType`](../common/attention.md#AttentionMasksType), [`VarlenMetadata`](../common/attention.md#VarlenMetadata), [`Config`](kda.md#KDA.Config), [`head_dim`](kda.md#KDA.Config.head_dim), [`inner_kda`](kda.md#KDA.Config.inner_kda), [`num_heads`](kda.md#KDA.Config.num_heads), [`beta`](kda.md#KDA.Config.beta), [`cu_seq_q`](../common/attention.md#VarlenMetadata.cu_seq_q), [`forget_a`](kda.md#KDA.Config.forget_a), [`forget_b`](kda.md#KDA.Config.forget_b), [`k_conv`](kda.md#KDA.Config.k_conv), [`k_proj`](kda.md#KDA.Config.k_proj), [`output_gate`](kda.md#KDA.Config.output_gate), [`output_norm`](kda.md#KDA.Config.output_norm), [`output_proj`](kda.md#KDA.Config.output_proj), [`q_conv`](kda.md#KDA.Config.q_conv), [`q_proj`](kda.md#KDA.Config.q_proj), [`v_conv`](kda.md#KDA.Config.v_conv), [`v_proj`](kda.md#KDA.Config.v_proj)
- used by: [`Module`](../../protocols/module.md#Module), [`_kda_config`](__init__.md#_kda_config), [`get_nparams_and_flops`](model.md#KimiK3Model.Config.get_nparams_and_flops), [`delta_attention`](model.md#KimiK3TransformerBlock.Config.delta_attention)

### <a id="KDA.Config"></a>`KDA.Config`  ·  implements/extends Config
- def: [`torchtitan/models/kimi_k3/kda.py:186`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/kda.py#L186) — documented in [kimi-k3-model](../../../../concepts/kimi-k3-model.md)
- signature: `class Config(Module.Config):`
- members:
  - <a id="KDA.Config.beta"></a>`beta` — [`L198`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/kda.py#L198)
  - <a id="KDA.Config.conv_kernel_size"></a>`conv_kernel_size` — [`L189`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/kda.py#L189)
  - <a id="KDA.Config.forget_a"></a>`forget_a` — [`L196`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/kda.py#L196)
  - <a id="KDA.Config.forget_b"></a>`forget_b` — [`L197`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/kda.py#L197)
  - <a id="KDA.Config.head_dim"></a>`head_dim` — [`L188`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/kda.py#L188) — documented in [kimi-k3-model](../../../../concepts/kimi-k3-model.md)
  - <a id="KDA.Config.inner_kda"></a>`inner_kda` — [`L200`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/kda.py#L200)
  - <a id="KDA.Config.k_conv"></a>`k_conv` — [`L194`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/kda.py#L194)
  - <a id="KDA.Config.k_proj"></a>`k_proj` — [`L191`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/kda.py#L191)
  - <a id="KDA.Config.num_heads"></a>`num_heads` — [`L187`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/kda.py#L187) — documented in [kimi-k3-model](../../../../concepts/kimi-k3-model.md)
  - <a id="KDA.Config.output_gate"></a>`output_gate` — [`L199`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/kda.py#L199)
  - <a id="KDA.Config.output_norm"></a>`output_norm` — [`L201`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/kda.py#L201)
  - <a id="KDA.Config.output_proj"></a>`output_proj` — [`L202`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/kda.py#L202)
  - <a id="KDA.Config.q_conv"></a>`q_conv` — [`L193`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/kda.py#L193)
  - <a id="KDA.Config.q_proj"></a>`q_proj` — [`L190`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/kda.py#L190)
  - <a id="KDA.Config.v_conv"></a>`v_conv` — [`L195`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/kda.py#L195)
  - <a id="KDA.Config.v_proj"></a>`v_proj` — [`L192`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/kda.py#L192)
- protocol/private: <a id="KDA.Config.__post_init__"></a>`__post_init__`[`L204`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/kda.py#L204)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`Linear`](../common/linear.md#Linear), [`Config`](../common/linear.md#Linear.Config), [`Config`](../../protocols/module.md#Module.Config), [`Conv1d`](../common/nn_modules.md#Conv1d), [`Config`](../common/nn_modules.md#Conv1d.Config), [`Config`](kda.md#KimiRMSNormGated.Config), [`KimiRMSNormGated`](kda.md#KimiRMSNormGated)
- used by: [`_kda_config`](__init__.md#_kda_config), [`get_nparams_and_flops`](model.md#KimiK3Model.Config.get_nparams_and_flops), [`from_hf`](state_dict_adapter.md#KimiK3StateDictAdapter.from_hf), [`set_kimi_k3_sharding_config`](sharding.md#set_kimi_k3_sharding_config), [`delta_attention`](model.md#KimiK3TransformerBlock.Config.delta_attention), [`beta`](kda.md#KDA.beta), [`dt_bias`](kda.md#KDA.dt_bias), [`forget_a`](kda.md#KDA.forget_a), [`forget_b`](kda.md#KDA.forget_b), [`inner_kda`](kda.md#KDA.inner_kda), [`k_conv`](kda.md#KDA.k_conv), [`k_proj`](kda.md#KDA.k_proj), [`output_gate`](kda.md#KDA.output_gate), [`output_norm`](kda.md#KDA.output_norm), [`output_proj`](kda.md#KDA.output_proj), [`q_conv`](kda.md#KDA.q_conv), [`q_proj`](kda.md#KDA.q_proj), [`v_conv`](kda.md#KDA.v_conv), [`v_proj`](kda.md#KDA.v_proj), [`num_heads`](kda.md#KDA.num_heads), [`A_log`](kda.md#KDA.A_log), [`head_dim`](kda.md#KDA.head_dim), [`__init__`](kda.md#KDA.__init__)

### <a id="KDAKernel"></a>`KDAKernel`  ·  implements/extends Module
- def: [`torchtitan/models/kimi_k3/kda.py:53`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/kda.py#L53)
- doc: Apply KDA preprocessing and the Attention Gym kernel.
- signature: `class KDAKernel(Module):`
- members:
  - <a id="KDAKernel.forward"></a>`forward(self, q_1THK: torch.Tensor, k_1THK: torch.Tensor, v_1THV: torch.Tensor, raw_gate_1THK: torch.Tensor, raw_beta_1TH: torch.Tensor, A_log_H: torch.Tensor, dt_bias_HK: torch.Tensor, *, cu_seqlens: torch.Tensor | None = None)` — [`L71`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/kda.py#L71)
  - <a id="KDAKernel.lower_bound"></a>`lower_bound` — [`L69`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/kda.py#L69)
- protocol/private: <a id="KDAKernel.__init__"></a>`__init__`[`L67`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/kda.py#L67)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`Config`](kda.md#KDAKernel.Config), [`lower_bound`](kda.md#KDAKernel.Config.lower_bound)
- used by: [`Module`](../../protocols/module.md#Module), [`_kda_config`](__init__.md#_kda_config), [`kernel`](kda.md#InnerKDA.Config.kernel)

### <a id="KDAKernel.Config"></a>`KDAKernel.Config`  ·  implements/extends Config
- def: [`torchtitan/models/kimi_k3/kda.py:57`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/kda.py#L57)
- signature: `class Config(Module.Config):`
- members:
  - <a id="KDAKernel.Config.lower_bound"></a>`lower_bound` — [`L58`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/kda.py#L58)
- protocol/private: <a id="KDAKernel.Config.__post_init__"></a>`__post_init__`[`L60`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/kda.py#L60)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`Config`](../../protocols/module.md#Module.Config)
- used by: [`_kda_config`](__init__.md#_kda_config), [`kernel`](kda.md#InnerKDA.Config.kernel), [`lower_bound`](kda.md#KDAKernel.lower_bound), [`__init__`](kda.md#KDAKernel.__init__)

### <a id="KimiRMSNormGated"></a>`KimiRMSNormGated`  ·  implements/extends Module
- def: [`torchtitan/models/kimi_k3/kda.py:29`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/kda.py#L29)
- doc: Per-head RMSNorm followed by a sigmoid output gate.
- signature: `class KimiRMSNormGated(Module):`
- members:
  - <a id="KimiRMSNormGated.forward"></a>`forward(self, x_THV: torch.Tensor, gate_THV: torch.Tensor)` — [`L42`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/kda.py#L42)
  - <a id="KimiRMSNormGated.eps"></a>`eps` — [`L39`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/kda.py#L39)
  - <a id="KimiRMSNormGated.weight"></a>`weight` — [`L40`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/kda.py#L40)
- protocol/private: <a id="KimiRMSNormGated.__init__"></a>`__init__`[`L37`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/kda.py#L37)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`Config`](kda.md#KimiRMSNormGated.Config), [`dim`](kda.md#KimiRMSNormGated.Config.dim), [`eps`](kda.md#KimiRMSNormGated.Config.eps)
- used by: [`Module`](../../protocols/module.md#Module), [`_kda_config`](__init__.md#_kda_config), [`output_norm`](kda.md#KDA.Config.output_norm)

### <a id="KimiRMSNormGated.Config"></a>`KimiRMSNormGated.Config`  ·  implements/extends Config
- def: [`torchtitan/models/kimi_k3/kda.py:33`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/kda.py#L33)
- signature: `class Config(Module.Config):`
- members:
  - <a id="KimiRMSNormGated.Config.dim"></a>`dim` — [`L34`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/kda.py#L34)
  - <a id="KimiRMSNormGated.Config.eps"></a>`eps` — [`L35`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/kda.py#L35)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`Config`](../../protocols/module.md#Module.Config)
- used by: [`_kda_config`](__init__.md#_kda_config), [`output_norm`](kda.md#KDA.Config.output_norm), [`eps`](kda.md#KimiRMSNormGated.eps), [`weight`](kda.md#KimiRMSNormGated.weight), [`__init__`](kda.md#KimiRMSNormGated.__init__)

