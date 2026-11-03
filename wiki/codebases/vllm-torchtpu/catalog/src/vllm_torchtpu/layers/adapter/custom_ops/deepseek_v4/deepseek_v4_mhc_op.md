---
title: 'Module: src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_mhc_op.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_mhc_op.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.layers.adapter.custom_ops.deepseek_v4.deepseek_v4_mhc_op`/
symbols:
  get_mhc_ops: get_mhc_ops().
  _mhc_pre_op: _mhc_pre_op().
  _mhc_fused_post_pre_op: _mhc_fused_post_pre_op().
  get_mhc_post_op: get_mhc_post_op().
  ATTN_DATA_AXIS: ATTN_DATA_AXIS.
  _mhc_op_cache._mhc_op_cache: _mhc_op_cache._mhc_op_cache.
  _gate_suffix: _gate_suffix().
  _name_float: _name_float().
  MHCOps: MHCOps#
  _mhc_pre_jax: _mhc_pre_jax().
  _mhc_post_jax: _mhc_post_jax().
  _mhc_fused_post_pre_jax: _mhc_fused_post_pre_jax().
  _fake_mhc_pre: _fake_mhc_pre().
  _fake_mhc_fused_post_pre: _fake_mhc_fused_post_pre().
  MHCOps.fused: MHCOps#fused.
  _fake_pre_outputs: _fake_pre_outputs().
  MHCOps.pre: MHCOps#pre.
  _fake_mhc_post: _fake_mhc_post().
  MHCOps.post: MHCOps#post.
---
# Module: [`src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_mhc_op.py`](../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_mhc_op.py)

## Classes
### <a id="MHCOps"></a>`MHCOps`  ·  implements/extends NamedTuple
- def: [`src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_mhc_op.py:271`](../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_mhc_op.py#L271)
- doc: The three registered mHC ops for one set of gate constants.
- signature: `class MHCOps(NamedTuple):`
- members:
  - <a id="MHCOps.fused"></a>`fused` — [`L290`](../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_mhc_op.py#L290)
  - <a id="MHCOps.post"></a>`post` — [`L291`](../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_mhc_op.py#L291)
  - <a id="MHCOps.pre"></a>`pre` — [`L289`](../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_mhc_op.py#L289)
- used by: [`forward`](../../../../models/vllm/deepseek_v4/model.md#DeepseekV4DecoderLayer.forward), [`get_mhc_ops`](deepseek_v4_mhc_op.md#get_mhc_ops), [`mhc_ops`](../../../../models/vllm/deepseek_v4/model.md#DeepseekV4DecoderLayer.mhc_ops), [`hc_pre`](../../../../models/vllm/deepseek_v4/model.md#DeepseekV4DecoderLayer.hc_pre)

## Functions
- <a id="_fake_mhc_fused_post_pre"></a>`_fake_mhc_fused_post_pre(x, residual, post_layer_mix, comb_res_mix, fn, hc_scale, hc_base, *args, **kwargs)` — [`L166`](../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_mhc_op.py#L166) — Abstract implementation for PyTorch Dynamo graph tracing.
- <a id="_fake_mhc_post"></a>`_fake_mhc_post(x, residual, post_layer_mix, comb_res_mix, *args, **kwargs)` — [`L161`](../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_mhc_op.py#L161) — Abstract implementation for PyTorch Dynamo graph tracing.
- <a id="_fake_mhc_pre"></a>`_fake_mhc_pre(residual, fn, hc_scale, hc_base, *args, **kwargs)` — [`L156`](../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_mhc_op.py#L156) — Abstract implementation for PyTorch Dynamo graph tracing.
- <a id="_fake_pre_outputs"></a>`_fake_pre_outputs(residual: torch.Tensor)` — [`L135`](../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_mhc_op.py#L135) — (post_mix, comb_mix, layer_input) placeholders for Dynamo tracing.
- <a id="_gate_suffix"></a>`_gate_suffix(rms_eps: float, hc_pre_eps: float, hc_sinkhorn_eps: float, hc_post_mult_value: float, sinkhorn_repeat: int)` — [`L51`](../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_mhc_op.py#L51) — The gate constants are baked into the traced op, so they name it.
- <a id="_mhc_fused_post_pre_jax"></a>`_mhc_fused_post_pre_jax(x: jax.Array, residual: jax.Array, post_layer_mix: jax.Array, comb_res_mix: jax.Array, fn: jax.Array, hc_scale: jax.Array, hc_base: jax.Array, *, rms_eps: float, hc_pre_eps: float, hc_sinkhorn_eps: float, hc_post_mult_value: float, sinkhorn_repeat: int)` — [`L103`](../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_mhc_op.py#L103) — One layer's post and the next layer's pre as a single kernel.
- <a id="_mhc_fused_post_pre_op"></a>`_mhc_fused_post_pre_op(rms_eps: float, hc_pre_eps: float, hc_sinkhorn_eps: float, hc_post_mult_value: float, sinkhorn_repeat: int)` — [`L233`](../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_mhc_op.py#L233) — documented in [custom-ops](../../../../../../../concepts/custom-ops.md)
- <a id="_mhc_post_jax"></a>`_mhc_post_jax(x: jax.Array, residual: jax.Array, post_layer_mix: jax.Array, comb_res_mix: jax.Array)` — [`L93`](../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_mhc_op.py#L93) — Recombine the sublayer output into the mHC residual streams.
- <a id="_mhc_pre_jax"></a>`_mhc_pre_jax(residual: jax.Array, fn: jax.Array, hc_scale: jax.Array, hc_base: jax.Array, *, rms_eps: float, hc_pre_eps: float, hc_sinkhorn_eps: float, hc_post_mult_value: float, sinkhorn_repeat: int)` — [`L67`](../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_mhc_op.py#L67) — Mix GEMM + stream collapse in Pallas, gates/Sinkhorn in XLA.
- <a id="_mhc_pre_op"></a>`_mhc_pre_op(rms_eps: float, hc_pre_eps: float, hc_sinkhorn_eps: float, hc_post_mult_value: float, sinkhorn_repeat: int)` — [`L173`](../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_mhc_op.py#L173) — documented in [custom-ops](../../../../../../../concepts/custom-ops.md)
- <a id="_name_float"></a>`_name_float(value: float)` — [`L46`](../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_mhc_op.py#L46) — A float rendered so it is safe inside a torch op name.
- <a id="get_mhc_ops"></a>`get_mhc_ops(rms_eps: float, hc_pre_eps: float, hc_sinkhorn_eps: float, hc_post_mult_value: float, sinkhorn_repeat: int)` — [`L294`](../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_mhc_op.py#L294) — Build (or fetch) every mHC op for these gate constants. — documented in [custom-ops](../../../../../../../concepts/custom-ops.md)
- <a id="get_mhc_post_op"></a>`get_mhc_post_op()` — [`L208`](../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_mhc_op.py#L208) — The ``post`` op alone, for callers that settle a deferred post. — documented in [custom-ops](../../../../../../../concepts/custom-ops.md)

## Module values
- <a id="ATTN_DATA_AXIS"></a>`ATTN_DATA_AXIS` — [`L41`](../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_mhc_op.py#L41) — documented in [custom-ops](../../../../../../../concepts/custom-ops.md)
- <a id="_mhc_op_cache._mhc_op_cache"></a>`_mhc_op_cache` — [`L43`](../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_mhc_op.py#L43) — documented in [custom-ops](../../../../../../../concepts/custom-ops.md)

