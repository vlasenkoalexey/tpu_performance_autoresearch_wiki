---
title: 'Module: torchtitan/experiments/tpu/qwen3_5/gated_delta.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/qwen3_5/gated_delta.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.qwen3_5.gated_delta`/
symbols:
  TpuGatedDeltaNet.forward: TpuGatedDeltaNet#forward().
  TpuInnerGatedDeltaNet.forward: TpuInnerGatedDeltaNet#forward().
  _causal_conv: _causal_conv().
  TpuGatedDeltaKernel.Config: TpuGatedDeltaKernel#Config#
  TpuInnerGatedDeltaNet.Config: TpuInnerGatedDeltaNet#Config#
  TpuGatedDeltaNet.Config: TpuGatedDeltaNet#Config#
  chunked_gated_delta: chunked_gated_delta().
  TpuInnerGatedDeltaNet: TpuInnerGatedDeltaNet#
  TpuInnerGatedDeltaNet.causal_conv: TpuInnerGatedDeltaNet#causal_conv().
  TpuGatedDeltaNet: TpuGatedDeltaNet#
  TpuGatedDeltaKernel.__init__: TpuGatedDeltaKernel#__init__().
  TpuGatedDeltaKernel.forward: TpuGatedDeltaKernel#forward().
  TpuGatedDeltaKernel: TpuGatedDeltaKernel#
  _l2norm: _l2norm().
  TpuGatedDeltaKernel.chunk_size: TpuGatedDeltaKernel#chunk_size.
  _same_segment: _same_segment().
  TpuGatedDeltaKernel.Config.chunk_size: TpuGatedDeltaKernel#Config#chunk_size.
---
# Module: [`torchtitan/experiments/tpu/qwen3_5/gated_delta.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3_5/gated_delta.py)

## Classes
### <a id="TpuGatedDeltaKernel"></a>`TpuGatedDeltaKernel`  ·  implements/extends GatedDeltaKernel
- def: [`torchtitan/experiments/tpu/qwen3_5/gated_delta.py:209`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3_5/gated_delta.py#L209)
- doc: `GatedDeltaKernel` running `chunked_gated_delta` on `[B, S]` rows.
- signature: `class TpuGatedDeltaKernel(GatedDeltaKernel):`
- members:
  - <a id="TpuGatedDeltaKernel.forward"></a>`forward(self, xq_BSHK: torch.Tensor, xk_BSHK: torch.Tensor, xv_BSHV: torch.Tensor, g_BSH: torch.Tensor, beta_BSH: torch.Tensor, *, cu_seqlens: torch.Tensor | None = None, segment_ids_BS: torch.Tensor | None = None)` — [`L220`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3_5/gated_delta.py#L220) — Runs the recurrence, restarting it at every ``segment_ids_BS`` change.
  - <a id="TpuGatedDeltaKernel.chunk_size"></a>`chunk_size` — [`L218`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3_5/gated_delta.py#L218)
- protocol/private: <a id="TpuGatedDeltaKernel.__init__"></a>`__init__`[`L216`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3_5/gated_delta.py#L216)
- uses (calls/refs, reference-scoped): [`GatedDeltaKernel`](../../../models/qwen3_5/gdn.md#GatedDeltaKernel), [`Config`](gated_delta.md#TpuGatedDeltaKernel.Config), [`chunked_gated_delta`](gated_delta.md#chunked_gated_delta), [`__init__`](../../../models/qwen3_5/gdn.md#GatedDeltaKernel.__init__), [`chunk_size`](gated_delta.md#TpuGatedDeltaKernel.Config.chunk_size)
- used by: [`use_tpu_modules`](__init__.md#use_tpu_modules), [`GatedDeltaKernel`](../../../models/qwen3_5/gdn.md#GatedDeltaKernel), [`forward`](../../../models/qwen3_5/gdn.md#GatedDeltaKernel.forward)

### <a id="TpuGatedDeltaKernel.Config"></a>`TpuGatedDeltaKernel.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/tpu/qwen3_5/gated_delta.py:213`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3_5/gated_delta.py#L213)
- signature: `class Config(GatedDeltaKernel.Config):`
- members:
  - <a id="TpuGatedDeltaKernel.Config.chunk_size"></a>`chunk_size` — [`L214`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3_5/gated_delta.py#L214)
- uses (calls/refs, reference-scoped): [`GatedDeltaKernel`](../../../models/qwen3_5/gdn.md#GatedDeltaKernel), [`Config`](../../../models/qwen3_5/gdn.md#GatedDeltaKernel.Config)
- used by: [`use_tpu_modules`](__init__.md#use_tpu_modules), [`__init__`](gated_delta.md#TpuGatedDeltaKernel.__init__), [`chunk_size`](gated_delta.md#TpuGatedDeltaKernel.chunk_size)

### <a id="TpuGatedDeltaNet"></a>`TpuGatedDeltaNet`  ·  implements/extends GatedDeltaNet
- def: [`torchtitan/experiments/tpu/qwen3_5/gated_delta.py:336`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3_5/gated_delta.py#L336)
- doc: `GatedDeltaNet` that passes `positions` to its inner module.
- signature: `class TpuGatedDeltaNet(GatedDeltaNet):`
- members:
  - <a id="TpuGatedDeltaNet.forward"></a>`forward(self, x_TD: torch.Tensor, attention_masks: VarlenMetadata | None = None, positions: torch.Tensor | None = None)` — [`L351`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3_5/gated_delta.py#L351)
- uses (calls/refs, reference-scoped): [`VarlenMetadata`](../../../models/common/attention.md#VarlenMetadata), [`GatedDeltaNet`](../../../models/qwen3_5/gdn.md#GatedDeltaNet), [`value_head_dim`](../../../models/qwen3_5/gdn.md#GatedDeltaNet.value_head_dim), [`conv_v`](../../../models/qwen3_5/gdn.md#GatedDeltaNet.conv_v), [`conv_k`](../../../models/qwen3_5/gdn.md#GatedDeltaNet.conv_k), [`conv_q`](../../../models/qwen3_5/gdn.md#GatedDeltaNet.conv_q), [`cu_seq_q`](../../../models/common/attention.md#VarlenMetadata.cu_seq_q), [`in_proj_a`](../../../models/qwen3_5/gdn.md#GatedDeltaNet.in_proj_a), [`in_proj_b`](../../../models/qwen3_5/gdn.md#GatedDeltaNet.in_proj_b), [`in_proj_k`](../../../models/qwen3_5/gdn.md#GatedDeltaNet.in_proj_k), [`in_proj_q`](../../../models/qwen3_5/gdn.md#GatedDeltaNet.in_proj_q), [`in_proj_v`](../../../models/qwen3_5/gdn.md#GatedDeltaNet.in_proj_v), [`in_proj_z`](../../../models/qwen3_5/gdn.md#GatedDeltaNet.in_proj_z), [`inner_gated_delta_net`](../../../models/qwen3_5/gdn.md#GatedDeltaNet.inner_gated_delta_net), [`norm`](../../../models/qwen3_5/gdn.md#GatedDeltaNet.norm), [`out_proj`](../../../models/qwen3_5/gdn.md#GatedDeltaNet.out_proj), [`key_head_dim`](../../../models/qwen3_5/gdn.md#GatedDeltaNet.key_head_dim), [`A_log`](../../../models/qwen3_5/gdn.md#GatedDeltaNet.A_log), [`dt_bias`](../../../models/qwen3_5/gdn.md#GatedDeltaNet.dt_bias)
- used by: [`use_tpu_modules`](__init__.md#use_tpu_modules), [`forward`](../../../models/qwen3_5/gdn.md#GatedDeltaNet.forward), [`GatedDeltaNet`](../../../models/qwen3_5/gdn.md#GatedDeltaNet)  (1 test-only)

### <a id="TpuGatedDeltaNet.Config"></a>`TpuGatedDeltaNet.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/tpu/qwen3_5/gated_delta.py:348`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3_5/gated_delta.py#L348)
- signature: `class Config(GatedDeltaNet.Config):`
- uses (calls/refs, reference-scoped): [`GatedDeltaNet`](../../../models/qwen3_5/gdn.md#GatedDeltaNet), [`Config`](../../../models/qwen3_5/gdn.md#GatedDeltaNet.Config)
- used by: [`use_tpu_modules`](__init__.md#use_tpu_modules)  (1 test-only)

### <a id="TpuInnerGatedDeltaNet"></a>`TpuInnerGatedDeltaNet`  ·  implements/extends InnerGatedDeltaNet
- def: [`torchtitan/experiments/tpu/qwen3_5/gated_delta.py:253`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3_5/gated_delta.py#L253)
- doc: `InnerGatedDeltaNet` that convolves each `[B, S]` row on its own.
- signature: `class TpuInnerGatedDeltaNet(InnerGatedDeltaNet):`
- members:
  - <a id="TpuInnerGatedDeltaNet.causal_conv"></a>`causal_conv(x_BSC: torch.Tensor, weight_C1W: torch.Tensor, head_dim: int)` — [`L311`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3_5/gated_delta.py#L311)
  - <a id="TpuInnerGatedDeltaNet.forward"></a>`forward(self, query_TC: torch.Tensor, key_TC: torch.Tensor, value_TC: torch.Tensor, a_TH: torch.Tensor, b_TH: torch.Tensor, conv_q_weight_C1W: torch.Tensor, conv_k_weight_C1W: torch.Tensor, conv_v_weight_C1W: torch.Tensor, A_log_H: torch.Tensor, dt_bias_H: torch.Tensor, cu_seqlens: torch.Tensor, *, key_head_dim: int, value_head_dim: int, positions: torch.Tensor | None = None)` — [`L265`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3_5/gated_delta.py#L265)
- uses (calls/refs, reference-scoped): [`segment_ids_from_positions`](../../../models/common/attention.md#segment_ids_from_positions), [`unflatten_tensor`](../unflatten_shim.md#unflatten_tensor), [`InnerGatedDeltaNet`](../../../models/qwen3_5/gdn.md#InnerGatedDeltaNet), [`_causal_conv`](gated_delta.md#_causal_conv), [`kernel`](../../../models/qwen3_5/gdn.md#InnerGatedDeltaNet.kernel)
- used by: [`use_tpu_modules`](__init__.md#use_tpu_modules), [`InnerGatedDeltaNet`](../../../models/qwen3_5/gdn.md#InnerGatedDeltaNet), [`forward`](../../../models/qwen3_5/gdn.md#InnerGatedDeltaNet.forward)  (1 test-only)

### <a id="TpuInnerGatedDeltaNet.Config"></a>`TpuInnerGatedDeltaNet.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/tpu/qwen3_5/gated_delta.py:262`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3_5/gated_delta.py#L262)
- signature: `class Config(InnerGatedDeltaNet.Config):`
- uses (calls/refs, reference-scoped): [`InnerGatedDeltaNet`](../../../models/qwen3_5/gdn.md#InnerGatedDeltaNet), [`Config`](../../../models/qwen3_5/gdn.md#InnerGatedDeltaNet.Config)
- used by: [`use_tpu_modules`](__init__.md#use_tpu_modules)  (1 test-only)

## Functions
- <a id="_causal_conv"></a>`_causal_conv(x_BSC: torch.Tensor, weight_C1W: torch.Tensor, segment_ids_BS: torch.Tensor | None = None)` — [`L48`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3_5/gated_delta.py#L48) — Depthwise causal ``conv1d`` on ``[B, S, C]`` via shifted slices.
- <a id="_l2norm"></a>`_l2norm(x: torch.Tensor, eps: float = 0.000001)` — [`L34`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3_5/gated_delta.py#L34)
- <a id="_same_segment"></a>`_same_segment(segment_ids_BS: torch.Tensor, shift: int)` — [`L38`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3_5/gated_delta.py#L38) — ``[B, S]``: whether token ``s - shift`` is in the document of token ``s``.
- <a id="chunked_gated_delta"></a>`chunked_gated_delta(q: torch.Tensor, k: torch.Tensor, v: torch.Tensor, g: torch.Tensor, beta: torch.Tensor, chunk_size: int = 64, segment_ids: torch.Tensor | None = None)` — [`L90`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3_5/gated_delta.py#L90) — Chunked gated delta rule in PyTorch (FLA ``chunk_gdn`` math).

