---
title: 'Module: torchtitan/overrides/fused_mla.py'
type: catalog
provenance: extracted
module: torchtitan/overrides/fused_mla.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.overrides.fused_mla`/
symbols:
  FusedMLAAttention.forward: FusedMLAAttention#forward().
  fused_mla: fused_mla().
  fused_mla_kv: fused_mla_kv().
  FusedMLAAttention.__init__: FusedMLAAttention#__init__().
  fused_mla_q: fused_mla_q().
  FusedMLAAttention.Config: FusedMLAAttention#Config#
  _to_local: _to_local().
  _FusedMLAQ.forward: _FusedMLAQ#forward().
  _FusedMLAQ.backward: _FusedMLAQ#backward().
  _fused_mla_q_rope_op: _fused_mla_q_rope_op().
  _fused_mla_k_rope_op: _fused_mla_k_rope_op().
  _fused_mla_kv_backward_op: _fused_mla_kv_backward_op().
  _resolve_positions: _resolve_positions().
  FusedMLAAttention: FusedMLAAttention#
  _fused_mla_k_rope_op_fake: _fused_mla_k_rope_op_fake().
  _fused_mla_kv_backward_op_fake: _fused_mla_kv_backward_op_fake().
  _FusedMLAKV.forward: _FusedMLAKV#forward().
  _FusedMLAKV.backward: _FusedMLAKV#backward().
  _to_local_for_mutation: _to_local_for_mutation().
  _from_local: _from_local().
  _fused_q_rope_kernel: _fused_q_rope_kernel().
  _fused_k_rope_kernel: _fused_k_rope_kernel().
  _fused_kv_backward_kernel: _fused_kv_backward_kernel().
  _FusedMLAQ: _FusedMLAQ#
  _FusedMLAKV: _FusedMLAKV#
  __all__: __all__.
  _FusedMLAQ.spmd_typecheck: _FusedMLAQ#spmd_typecheck().
  _FusedMLAKV.spmd_typecheck: _FusedMLAKV#spmd_typecheck().
---
# Module: [`torchtitan/overrides/fused_mla.py`](../../../../../../raw/code/torchtitan/torchtitan/overrides/fused_mla.py)

## Classes
### <a id="FusedMLAAttention"></a>`FusedMLAAttention`  ·  implements/extends Attention
- def: [`torchtitan/overrides/fused_mla.py:803`](../../../../../../raw/code/torchtitan/torchtitan/overrides/fused_mla.py#L803)
- doc: Stock DeepSeek-V3 attention with fused MLA tensor assembly.
- signature: `class FusedMLAAttention(Attention):`
- members:
  - <a id="FusedMLAAttention.forward"></a>`forward(self, x: torch.Tensor, attention_masks: AttentionMasksType, positions: torch.Tensor | None = None)` — [`L818`](../../../../../../raw/code/torchtitan/torchtitan/overrides/fused_mla.py#L818) — documented in [config-overrides](../../../concepts/config-overrides.md)
- protocol/private: <a id="FusedMLAAttention.__init__"></a>`__init__`[`L810`](../../../../../../raw/code/torchtitan/torchtitan/overrides/fused_mla.py#L810)
- uses (calls/refs, reference-scoped): [`get_spmd_backend`](../distributed/utils.md#get_spmd_backend), [`ComplexRoPE`](../models/common/rope.md#ComplexRoPE), [`AttentionMasksType`](../models/common/attention.md#AttentionMasksType), [`forward`](../models/deepseek_v3/model.md#Attention.forward), [`Attention`](../models/deepseek_v3/model.md#Attention), [`softmax_scale`](../models/deepseek_v3/model.md#Attention.softmax_scale), [`wq`](../models/deepseek_v3/model.md#Attention.wq), [`rope`](../models/deepseek_v3/model.md#Attention.rope), [`qk_nope_head_dim`](../models/deepseek_v3/model.md#Attention.qk_nope_head_dim), [`v_head_dim`](../models/deepseek_v3/model.md#Attention.v_head_dim), [`fused_mla_kv`](fused_mla.md#fused_mla_kv), [`inner_attention`](../models/deepseek_v3/model.md#Attention.inner_attention), [`_maybe_check_max_pos`](../models/common/rope.md#_maybe_check_max_pos), [`qk_head_dim`](../models/deepseek_v3/model.md#Attention.qk_head_dim), [`fused_mla_q`](fused_mla.md#fused_mla_q), [`Config`](fused_mla.md#FusedMLAAttention.Config), [`wkv_b`](../models/deepseek_v3/model.md#Attention.wkv_b), [`wq_b`](../models/deepseek_v3/model.md#Attention.wq_b), [`kv_norm`](../models/deepseek_v3/model.md#Attention.kv_norm), [`q_norm`](../models/deepseek_v3/model.md#Attention.q_norm), [`wkv_a`](../models/deepseek_v3/model.md#Attention.wkv_a), [`wo`](../models/deepseek_v3/model.md#Attention.wo), [`wq_a`](../models/deepseek_v3/model.md#Attention.wq_a), [`q_lora_rank`](../models/deepseek_v3/model.md#Attention.q_lora_rank), [`qk_rope_head_dim`](../models/deepseek_v3/model.md#Attention.qk_rope_head_dim), [`kv_lora_rank`](../models/deepseek_v3/model.md#Attention.kv_lora_rank), [`__init__`](../models/deepseek_v3/model.md#Attention.__init__)
- used by: [`forward`](../models/deepseek_v3/model.md#Attention.forward), [`Attention`](../models/deepseek_v3/model.md#Attention), [`fused_mla`](fused_mla.md#fused_mla)

### <a id="FusedMLAAttention.Config"></a>`FusedMLAAttention.Config`  ·  implements/extends Config
- def: [`torchtitan/overrides/fused_mla.py:807`](../../../../../../raw/code/torchtitan/torchtitan/overrides/fused_mla.py#L807)
- signature: `class Config(Attention.Config):`
- uses (calls/refs, reference-scoped): [`Attention`](../models/deepseek_v3/model.md#Attention), [`Config`](../models/deepseek_v3/model.md#Attention.Config)
- used by: [`fused_mla`](fused_mla.md#fused_mla), [`__init__`](fused_mla.md#FusedMLAAttention.__init__)

### <a id="_FusedMLAKV"></a>`_FusedMLAKV`
- def: [`torchtitan/overrides/fused_mla.py:668`](../../../../../../raw/code/torchtitan/torchtitan/overrides/fused_mla.py#L668)
- signature: `class _FusedMLAKV(torch.autograd.Function):`
- members:
  - <a id="_FusedMLAKV.backward"></a>`backward(ctx, grad_k: torch.Tensor, grad_v: torch.Tensor)` — [`L709`](../../../../../../raw/code/torchtitan/torchtitan/overrides/fused_mla.py#L709)
  - <a id="_FusedMLAKV.forward"></a>`forward(ctx, kv: torch.Tensor, k_pe: torch.Tensor, rope_cache_real: torch.Tensor, positions: torch.Tensor, q_nope_dim: int)` — [`L690`](../../../../../../raw/code/torchtitan/torchtitan/overrides/fused_mla.py#L690)
  - <a id="_FusedMLAKV.spmd_typecheck"></a>`spmd_typecheck(outputs: tuple[torch.Tensor, torch.Tensor], *, kv: torch.Tensor, k_pe: torch.Tensor, rope_cache_real: torch.Tensor, positions: torch.Tensor)` — [`L670`](../../../../../../raw/code/torchtitan/torchtitan/overrides/fused_mla.py#L670)
- uses (calls/refs, reference-scoped): [`_fused_mla_k_rope_op`](fused_mla.md#_fused_mla_k_rope_op), [`_fused_mla_kv_backward_op`](fused_mla.md#_fused_mla_kv_backward_op)
- used by: [`fused_mla_kv`](fused_mla.md#fused_mla_kv)

### <a id="_FusedMLAQ"></a>`_FusedMLAQ`
- def: [`torchtitan/overrides/fused_mla.py:612`](../../../../../../raw/code/torchtitan/torchtitan/overrides/fused_mla.py#L612)
- signature: `class _FusedMLAQ(torch.autograd.Function):`
- members:
  - <a id="_FusedMLAQ.backward"></a>`backward(ctx, grad_q: torch.Tensor)` — [`L651`](../../../../../../raw/code/torchtitan/torchtitan/overrides/fused_mla.py#L651)
  - <a id="_FusedMLAQ.forward"></a>`forward(ctx, q: torch.Tensor, rope_cache_real: torch.Tensor, positions: torch.Tensor, q_nope_dim: int)` — [`L629`](../../../../../../raw/code/torchtitan/torchtitan/overrides/fused_mla.py#L629)
  - <a id="_FusedMLAQ.spmd_typecheck"></a>`spmd_typecheck(output: torch.Tensor, *, q: torch.Tensor, rope_cache_real: torch.Tensor, positions: torch.Tensor)` — [`L614`](../../../../../../raw/code/torchtitan/torchtitan/overrides/fused_mla.py#L614)
- uses (calls/refs, reference-scoped): [`_fused_mla_q_rope_op`](fused_mla.md#_fused_mla_q_rope_op), [`_to_local_for_mutation`](fused_mla.md#_to_local_for_mutation)
- used by: [`fused_mla_q`](fused_mla.md#fused_mla_q)

## Functions
- <a id="_from_local"></a>`_from_local(local: torch.Tensor, spec: torch.Tensor)` — [`L738`](../../../../../../raw/code/torchtitan/torchtitan/overrides/fused_mla.py#L738)
- <a id="_fused_k_rope_kernel"></a>`_fused_k_rope_kernel(kv, k_pe, rope_cache, positions, k, KV_STRIDE_B: tl.constexpr, KV_STRIDE_L: tl.constexpr, KV_STRIDE_H: tl.constexpr, KV_STRIDE_D: tl.constexpr, KPE_STRIDE_B: tl.constexpr, KPE_STRIDE_L: tl.constexpr, KPE_STRIDE_D: tl.constexpr, CACHE_STRIDE_M: tl.constexpr, CACHE_STRIDE_P: tl.constexpr, CACHE_STRIDE_R: tl.constexpr, POS_STRIDE_B: tl.constexpr, POS_STRIDE_L: tl.constexpr, K_STRIDE_B: tl.constexpr, K_STRIDE_L: tl.constexpr, K_STRIDE_H: tl.constexpr, K_STRIDE_D: tl.constexpr, SEQ_LEN: tl.constexpr, N_HEADS: tl.constexpr, NUM_HEAD_BLOCKS: tl.constexpr, Q_NOPE_DIM: tl.constexpr, ROPE_DIM: tl.constexpr, BLOCK_H: tl.constexpr, BLOCK_D: tl.constexpr, BLOCK_PAIRS: tl.constexpr)` — [`L172`](../../../../../../raw/code/torchtitan/torchtitan/overrides/fused_mla.py#L172)
- <a id="_fused_kv_backward_kernel"></a>`_fused_kv_backward_kernel(grad_k, grad_v, rope_cache, positions, grad_kv, grad_k_pe, GK_STRIDE_B: tl.constexpr, GK_STRIDE_L: tl.constexpr, GK_STRIDE_H: tl.constexpr, GK_STRIDE_D: tl.constexpr, GV_STRIDE_B: tl.constexpr, GV_STRIDE_L: tl.constexpr, GV_STRIDE_H: tl.constexpr, GV_STRIDE_D: tl.constexpr, CACHE_STRIDE_M: tl.constexpr, CACHE_STRIDE_P: tl.constexpr, CACHE_STRIDE_R: tl.constexpr, POS_STRIDE_B: tl.constexpr, POS_STRIDE_L: tl.constexpr, GKV_STRIDE_B: tl.constexpr, GKV_STRIDE_L: tl.constexpr, GKV_STRIDE_H: tl.constexpr, GKV_STRIDE_D: tl.constexpr, GKPE_STRIDE_B: tl.constexpr, GKPE_STRIDE_L: tl.constexpr, GKPE_STRIDE_D: tl.constexpr, SEQ_LEN: tl.constexpr, N_HEADS: tl.constexpr, Q_NOPE_DIM: tl.constexpr, ROPE_DIM: tl.constexpr, V_DIM: tl.constexpr, BLOCK_H: tl.constexpr, BLOCK_D: tl.constexpr, BLOCK_PAIRS: tl.constexpr, ROUND_BF16_SUM: tl.constexpr, ROUND_FP16_SUM: tl.constexpr)` — [`L269`](../../../../../../raw/code/torchtitan/torchtitan/overrides/fused_mla.py#L269)
- <a id="_fused_mla_k_rope_op"></a>`_fused_mla_k_rope_op(kv: torch.Tensor, k_pe: torch.Tensor, rope_cache_real: torch.Tensor, positions: torch.Tensor, q_nope_dim: int)` — [`L452`](../../../../../../raw/code/torchtitan/torchtitan/overrides/fused_mla.py#L452)
- <a id="_fused_mla_k_rope_op_fake"></a>`_fused_mla_k_rope_op_fake(kv: torch.Tensor, k_pe: torch.Tensor, rope_cache_real: torch.Tensor, positions: torch.Tensor, q_nope_dim: int)` — [`L506`](../../../../../../raw/code/torchtitan/torchtitan/overrides/fused_mla.py#L506)
- <a id="_fused_mla_kv_backward_op"></a>`_fused_mla_kv_backward_op(grad_k: torch.Tensor, grad_v: torch.Tensor, rope_cache_real: torch.Tensor, positions: torch.Tensor, q_nope_dim: int, rope_dim: int)` — [`L525`](../../../../../../raw/code/torchtitan/torchtitan/overrides/fused_mla.py#L525)
- <a id="_fused_mla_kv_backward_op_fake"></a>`_fused_mla_kv_backward_op_fake(grad_k: torch.Tensor, grad_v: torch.Tensor, rope_cache_real: torch.Tensor, positions: torch.Tensor, q_nope_dim: int, rope_dim: int)` — [`L590`](../../../../../../raw/code/torchtitan/torchtitan/overrides/fused_mla.py#L590)
- <a id="_fused_mla_q_rope_op"></a>`_fused_mla_q_rope_op(q: torch.Tensor, rope_cache_real: torch.Tensor, positions: torch.Tensor, q_nope_dim: int, inverse: bool)` — [`L407`](../../../../../../raw/code/torchtitan/torchtitan/overrides/fused_mla.py#L407)
- <a id="_fused_q_rope_kernel"></a>`_fused_q_rope_kernel(q, rope_cache, positions, Q_STRIDE_B: tl.constexpr, Q_STRIDE_L: tl.constexpr, Q_STRIDE_H: tl.constexpr, Q_STRIDE_D: tl.constexpr, CACHE_STRIDE_M: tl.constexpr, CACHE_STRIDE_P: tl.constexpr, CACHE_STRIDE_R: tl.constexpr, POS_STRIDE_B: tl.constexpr, POS_STRIDE_L: tl.constexpr, SEQ_LEN: tl.constexpr, N_HEADS: tl.constexpr, NUM_HEAD_BLOCKS: tl.constexpr, Q_NOPE_DIM: tl.constexpr, ROPE_DIM: tl.constexpr, BLOCK_H: tl.constexpr, BLOCK_PAIRS: tl.constexpr, INVERSE: tl.constexpr)` — [`L86`](../../../../../../raw/code/torchtitan/torchtitan/overrides/fused_mla.py#L86)
- <a id="_resolve_positions"></a>`_resolve_positions(positions: torch.Tensor | None, reference: torch.Tensor)` — [`L749`](../../../../../../raw/code/torchtitan/torchtitan/overrides/fused_mla.py#L749) — documented in [config-overrides](../../../concepts/config-overrides.md)
- <a id="_to_local"></a>`_to_local(tensor: torch.Tensor)` — [`L722`](../../../../../../raw/code/torchtitan/torchtitan/overrides/fused_mla.py#L722)
- <a id="_to_local_for_mutation"></a>`_to_local_for_mutation(tensor: torch.Tensor)` — [`L726`](../../../../../../raw/code/torchtitan/torchtitan/overrides/fused_mla.py#L726)
- <a id="fused_mla"></a>`fused_mla(cfg: Attention.Config)` — [`L899`](../../../../../../raw/code/torchtitan/torchtitan/overrides/fused_mla.py#L899) — documented in [config-overrides](../../../concepts/config-overrides.md)
- <a id="fused_mla_kv"></a>`fused_mla_kv(kv: torch.Tensor, k_pe: torch.Tensor, rope_cache: torch.Tensor, positions: torch.Tensor | None, q_nope_dim: int)` — [`L780`](../../../../../../raw/code/torchtitan/torchtitan/overrides/fused_mla.py#L780) — Materialize K and expose V with a fused custom backward. — documented in [config-overrides](../../../concepts/config-overrides.md)
- <a id="fused_mla_q"></a>`fused_mla_q(q: torch.Tensor, rope_cache: torch.Tensor, positions: torch.Tensor | None, q_nope_dim: int)` — [`L766`](../../../../../../raw/code/torchtitan/torchtitan/overrides/fused_mla.py#L766) — Apply ComplexRoPE in place to Q's positional tail. — documented in [config-overrides](../../../concepts/config-overrides.md)

## Module values
- <a id="__all__"></a>`__all__` — [`L77`](../../../../../../raw/code/torchtitan/torchtitan/overrides/fused_mla.py#L77)

