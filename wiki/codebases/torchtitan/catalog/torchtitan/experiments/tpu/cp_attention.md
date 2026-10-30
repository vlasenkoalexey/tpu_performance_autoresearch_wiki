---
title: 'Module: torchtitan/experiments/tpu/cp_attention.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/cp_attention.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.cp_attention`/
symbols:
  KVAllGatherCPInnerAttention.forward: KVAllGatherCPInnerAttention#forward().
  UlyssesCPInnerAttention.forward: UlyssesCPInnerAttention#forward().
  validate_tpu_context_parallel: validate_tpu_context_parallel().
  KVAllGatherCPScaledDotProductInnerAttention: KVAllGatherCPScaledDotProductInnerAttention#
  reorder_sequence: reorder_sequence().
  KVAllGatherCPInnerAttention.cp_shard: KVAllGatherCPInnerAttention#cp_shard().
  KVAllGatherCPVarlenInnerAttention: KVAllGatherCPVarlenInnerAttention#
  KVAllGatherCPInnerAttention: KVAllGatherCPInnerAttention#
  _CP_INNER_ATTENTIONS: _CP_INNER_ATTENTIONS.
  UlyssesCPScaledDotProductInnerAttention: UlyssesCPScaledDotProductInnerAttention#
  tpu_cp_inner_attention: tpu_cp_inner_attention().
  revert_tpu_context_parallel: revert_tpu_context_parallel().
  KVAllGatherCPInnerAttention._maybe_cache_cp_rank: KVAllGatherCPInnerAttention#_maybe_cache_cp_rank().
  install_tpu_cp_patches: install_tpu_cp_patches().
  _CP_RANK_CACHE._CP_RANK_CACHE: _CP_RANK_CACHE._CP_RANK_CACHE.
  KVAllGatherCPInnerAttention._full_sequence_segment_ids_all_gather: KVAllGatherCPInnerAttention#_full_sequence_segment_ids_all_gather().
  _TOKEN_DIM: _TOKEN_DIM.
  KVAllGatherCPScaledDotProductInnerAttention.Config: KVAllGatherCPScaledDotProductInnerAttention#Config#
  UlyssesCPInnerAttention: UlyssesCPInnerAttention#
  KVAllGatherCPInnerAttention.local_forward: KVAllGatherCPInnerAttention#local_forward().
  KVAllGatherCPInnerAttention._get_cp_rank_tensor: KVAllGatherCPInnerAttention#_get_cp_rank_tensor().
  _orig_segment_ids_from_positions: _orig_segment_ids_from_positions.
  _full_sequence_segment_ids: _full_sequence_segment_ids().
  UlyssesCPScaledDotProductInnerAttention.Config: UlyssesCPScaledDotProductInnerAttention#Config#
  UlyssesCPVarlenInnerAttention: UlyssesCPVarlenInnerAttention#
  KVAllGatherCPVarlenInnerAttention.Config: KVAllGatherCPVarlenInnerAttention#Config#
  _patch_segment_ids_from_positions: _patch_segment_ids_from_positions().
  KVAllGatherCPInnerAttention.__init__: KVAllGatherCPInnerAttention#__init__().
  _all_gather_kv: _all_gather_kv().
  _TPUCPInnerAttention: _TPUCPInnerAttention#
  UlyssesCPInnerAttention.cp_shard: UlyssesCPInnerAttention#cp_shard().
  _wait: _wait().
  _normalize_cp_device: _normalize_cp_device().
  _cache_cp_rank_for_mesh: _cache_cp_rank_for_mesh().
  _tracing: _tracing().
  _all_to_all: _all_to_all().
  _repeat_kv_heads: _repeat_kv_heads().
  _TPUCPInnerAttention.set_local_attention: _TPUCPInnerAttention#set_local_attention().
  _HEAD_DIM: _HEAD_DIM.
  KVAllGatherCPInnerAttention._uses_sliding_window: KVAllGatherCPInnerAttention#_uses_sliding_window().
  UlyssesCPVarlenInnerAttention.Config: UlyssesCPVarlenInnerAttention#Config#
  _type_checking: _type_checking().
  tpu_cp_load_balancer: tpu_cp_load_balancer().
  _cp_segment_ids_from_positions: _cp_segment_ids_from_positions().
  UlyssesCPInnerAttention.local_forward: UlyssesCPInnerAttention#local_forward().
  _TPUCPInnerAttention._local_attn_override: _TPUCPInnerAttention#_local_attn_override.
  CPStrategy: CPStrategy.
  KVAllGatherCPInnerAttention.init_weights: KVAllGatherCPInnerAttention#init_weights().
  _validate_heads: _validate_heads().
  _validate_sequence_lengths: _validate_sequence_lengths().
  _patched: _patched.
  _AllGatherKV.forward: _AllGatherKV#forward().
  _AllGatherKV.backward: _AllGatherKV#backward().
  _TPUCPInnerAttention.extra_repr: _TPUCPInnerAttention#extra_repr().
  UlyssesCPInnerAttention.__init__: UlyssesCPInnerAttention#__init__().
  KVAllGatherCPInnerAttention._init_self_buffers: KVAllGatherCPInnerAttention#_init_self_buffers().
  KVAllGatherCPScaledDotProductInnerAttention.Config.allow_reference_attention: KVAllGatherCPScaledDotProductInnerAttention#Config#allow_reference_attention.
  _AllGatherKV: _AllGatherKV#
  install_tpu_cp_patches.resolve_flattened: install_tpu_cp_patches().resolve_flattened().
  __all__: __all__.
  KVAllGatherCPScaledDotProductInnerAttention.Config.reduce_dtype: KVAllGatherCPScaledDotProductInnerAttention#Config#reduce_dtype.
  KVAllGatherCPVarlenInnerAttention.Config.reduce_dtype: KVAllGatherCPVarlenInnerAttention#Config#reduce_dtype.
  KVAllGatherCPVarlenInnerAttention.Config.allow_reference_attention: KVAllGatherCPVarlenInnerAttention#Config#allow_reference_attention.
---
# Module: [`torchtitan/experiments/tpu/cp_attention.py`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/cp_attention.py)

## Classes
### <a id="KVAllGatherCPInnerAttention"></a>`KVAllGatherCPInnerAttention`  ·  implements/extends _TPUCPInnerAttention
- def: [`torchtitan/experiments/tpu/cp_attention.py:433`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/cp_attention.py#L433) — documented in [tpu-context-parallel-attention](../../../../concepts/tpu-context-parallel-attention.md)
- doc: MaxText-style load-balanced KV All-Gather CP mixin for inner attention.
- signature: `class KVAllGatherCPInnerAttention(_TPUCPInnerAttention):`
- members:
  - <a id="KVAllGatherCPInnerAttention._full_sequence_segment_ids_all_gather"></a>`_full_sequence_segment_ids_all_gather(self, positions: torch.Tensor, group: Any, bsz: int, q_seq_len: int)` — [`L689`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/cp_attention.py#L689) — All-gather sharded ``positions`` and return contiguous ``(B, S)`` ``segment_ids``. — documented in [tpu-context-parallel-attention](../../../../concepts/tpu-context-parallel-attention.md)
  - <a id="KVAllGatherCPInnerAttention.cp_shard"></a>`cp_shard(cls, input_dict: dict[str, Any], input_shardings: dict[str, Any] | None, cp_mesh: Any, load_balancer_type: str | None, ptrr_mask_key: str | None)` — [`L498`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/cp_attention.py#L498) — documented in [tpu-context-parallel-attention](../../../../concepts/tpu-context-parallel-attention.md)
  - <a id="KVAllGatherCPInnerAttention.forward"></a>`forward(self, q_THK: torch.Tensor, k_THK: torch.Tensor, v_THV: torch.Tensor, **kwargs)` — [`L712`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/cp_attention.py#L712) — documented in [tpu-context-parallel-attention](../../../../concepts/tpu-context-parallel-attention.md)
  - <a id="KVAllGatherCPInnerAttention.init_weights"></a>`init_weights(self, **kwargs)` — [`L457`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/cp_attention.py#L457)
  - <a id="KVAllGatherCPInnerAttention.local_forward"></a>`local_forward(self, q: torch.Tensor, k: torch.Tensor, v: torch.Tensor, *, scale: float | None = None, enable_gqa: bool = False, is_causal: bool = True, segment_ids: torch.Tensor | None = None, cp_rank: torch.Tensor | None = None, **kwargs)` — [`L590`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/cp_attention.py#L590) — Reference attention for CPU, tests and short sequences. — documented in [tpu-context-parallel-attention](../../../../concepts/tpu-context-parallel-attention.md)
- protocol/private: <a id="KVAllGatherCPInnerAttention.__init__"></a>`__init__`[`L436`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/cp_attention.py#L436), <a id="KVAllGatherCPInnerAttention._get_cp_rank_tensor"></a>`_get_cp_rank_tensor`[`L477`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/cp_attention.py#L477), <a id="KVAllGatherCPInnerAttention._init_self_buffers"></a>`_init_self_buffers`[`L450`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/cp_attention.py#L450), <a id="KVAllGatherCPInnerAttention._maybe_cache_cp_rank"></a>`_maybe_cache_cp_rank`[`L462`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/cp_attention.py#L462), <a id="KVAllGatherCPInnerAttention._uses_sliding_window"></a>`_uses_sliding_window`[`L682`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/cp_attention.py#L682)
- uses (calls/refs, reference-scoped): [`logger`](../../tools/logging.md#logger), [`TORCH_DTYPE_MAP`](../../config/__init__.md#TORCH_DTYPE_MAP), [`MeshAxisName`](../../distributed/parallel_dims.md#MeshAxisName), [`ScaledDotProductInnerAttention`](../../models/common/attention.md#ScaledDotProductInnerAttention), [`VarlenInnerAttention`](../../models/common/attention.md#VarlenInnerAttention), [`KVAllGatherCPScaledDotProductInnerAttention`](cp_attention.md#KVAllGatherCPScaledDotProductInnerAttention), [`reorder_sequence`](cp_attention.md#reorder_sequence), [`prepare_context_parallel_input`](../../distributed/context_parallel/api.md#prepare_context_parallel_input), [`CP`](../../distributed/parallel_dims.md#MeshAxisName.CP), [`KVAllGatherCPVarlenInnerAttention`](cp_attention.md#KVAllGatherCPVarlenInnerAttention), [`get_unflatten_seq_len`](unflatten_shim.md#get_unflatten_seq_len), [`_CP_RANK_CACHE`](cp_attention.md#_CP_RANK_CACHE._CP_RANK_CACHE), [`_TOKEN_DIM`](cp_attention.md#_TOKEN_DIM), [`_cp_shard_dims`](../../distributed/context_parallel/api.md#_cp_shard_dims), [`_orig_segment_ids_from_positions`](cp_attention.md#_orig_segment_ids_from_positions), [`_patch_segment_ids_from_positions`](cp_attention.md#_patch_segment_ids_from_positions), [`_TPUCPInnerAttention`](cp_attention.md#_TPUCPInnerAttention), [`_all_gather_kv`](cp_attention.md#_all_gather_kv), [`spmd_mesh_group`](../../distributed/spmd_types.md#spmd_mesh_group), [`window_size`](../../models/common/attention.md#VarlenInnerAttention.window_size), [`_wait`](cp_attention.md#_wait), [`_cache_cp_rank_for_mesh`](cp_attention.md#_cache_cp_rank_for_mesh), [`_normalize_cp_device`](cp_attention.md#_normalize_cp_device), [`_tracing`](cp_attention.md#_tracing), [`set_local_attention`](cp_attention.md#_TPUCPInnerAttention.set_local_attention), [`_type_checking`](cp_attention.md#_type_checking), [`_local_attn_override`](cp_attention.md#_TPUCPInnerAttention._local_attn_override)
- used by: [`validate_tpu_context_parallel`](cp_attention.md#validate_tpu_context_parallel), [`KVAllGatherCPScaledDotProductInnerAttention`](cp_attention.md#KVAllGatherCPScaledDotProductInnerAttention), [`KVAllGatherCPVarlenInnerAttention`](cp_attention.md#KVAllGatherCPVarlenInnerAttention), [`cp_shard`](../../models/common/cp_attention.md#CPInnerAttention.cp_shard), [`_TPUCPInnerAttention`](cp_attention.md#_TPUCPInnerAttention)  (6 test-only)

### <a id="KVAllGatherCPScaledDotProductInnerAttention"></a>`KVAllGatherCPScaledDotProductInnerAttention`  ·  implements/extends KVAllGatherCPInnerAttention, ScaledDotProductInnerAttention
- def: [`torchtitan/experiments/tpu/cp_attention.py:872`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/cp_attention.py#L872) — documented in [tpu-context-parallel-attention](../../../../concepts/tpu-context-parallel-attention.md)
- signature: `class KVAllGatherCPScaledDotProductInnerAttention(KVAllGatherCPInnerAttention, ScaledDotProductInnerAttention):`
- uses (calls/refs, reference-scoped): [`ScaledDotProductInnerAttention`](../../models/common/attention.md#ScaledDotProductInnerAttention), [`KVAllGatherCPInnerAttention`](cp_attention.md#KVAllGatherCPInnerAttention)
- used by: [`ScaledDotProductInnerAttention`](../../models/common/attention.md#ScaledDotProductInnerAttention), [`KVAllGatherCPInnerAttention`](cp_attention.md#KVAllGatherCPInnerAttention), [`_CP_INNER_ATTENTIONS`](cp_attention.md#_CP_INNER_ATTENTIONS)  (9 test-only)

### <a id="KVAllGatherCPScaledDotProductInnerAttention.Config"></a>`KVAllGatherCPScaledDotProductInnerAttention.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/tpu/cp_attention.py:877`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/cp_attention.py#L877)
- signature: `class Config(ScaledDotProductInnerAttention.Config):`
- members:
  - <a id="KVAllGatherCPScaledDotProductInnerAttention.Config.allow_reference_attention"></a>`allow_reference_attention` — [`L879`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/cp_attention.py#L879) — ---
  - <a id="KVAllGatherCPScaledDotProductInnerAttention.Config.reduce_dtype"></a>`reduce_dtype` — [`L878`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/cp_attention.py#L878)
- uses (calls/refs, reference-scoped): [`ScaledDotProductInnerAttention`](../../models/common/attention.md#ScaledDotProductInnerAttention), [`Config`](../../models/common/attention.md#ScaledDotProductInnerAttention.Config)
- used by: (6 test-only callers)

### <a id="KVAllGatherCPVarlenInnerAttention"></a>`KVAllGatherCPVarlenInnerAttention`  ·  implements/extends KVAllGatherCPInnerAttention, VarlenInnerAttention
- def: [`torchtitan/experiments/tpu/cp_attention.py:883`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/cp_attention.py#L883) — documented in [tpu-context-parallel-attention](../../../../concepts/tpu-context-parallel-attention.md)
- signature: `class KVAllGatherCPVarlenInnerAttention(KVAllGatherCPInnerAttention, VarlenInnerAttention):`
- uses (calls/refs, reference-scoped): [`VarlenInnerAttention`](../../models/common/attention.md#VarlenInnerAttention), [`KVAllGatherCPInnerAttention`](cp_attention.md#KVAllGatherCPInnerAttention)
- used by: [`VarlenInnerAttention`](../../models/common/attention.md#VarlenInnerAttention), [`KVAllGatherCPInnerAttention`](cp_attention.md#KVAllGatherCPInnerAttention), [`_CP_INNER_ATTENTIONS`](cp_attention.md#_CP_INNER_ATTENTIONS)  (5 test-only)

### <a id="KVAllGatherCPVarlenInnerAttention.Config"></a>`KVAllGatherCPVarlenInnerAttention.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/tpu/cp_attention.py:888`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/cp_attention.py#L888)
- signature: `class Config(VarlenInnerAttention.Config):`
- members:
  - <a id="KVAllGatherCPVarlenInnerAttention.Config.allow_reference_attention"></a>`allow_reference_attention` — [`L890`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/cp_attention.py#L890) — ---
  - <a id="KVAllGatherCPVarlenInnerAttention.Config.reduce_dtype"></a>`reduce_dtype` — [`L889`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/cp_attention.py#L889)
- uses (calls/refs, reference-scoped): [`VarlenInnerAttention`](../../models/common/attention.md#VarlenInnerAttention), [`Config`](../../models/common/attention.md#VarlenInnerAttention.Config)
- used by: (4 test-only callers)

### <a id="UlyssesCPInnerAttention"></a>`UlyssesCPInnerAttention`  ·  implements/extends _TPUCPInnerAttention
- def: [`torchtitan/experiments/tpu/cp_attention.py:322`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/cp_attention.py#L322) — documented in [tpu-context-parallel-attention](../../../../concepts/tpu-context-parallel-attention.md)
- doc: Ulysses (all-to-all) CP mixin for any single-device inner attention.
- signature: `class UlyssesCPInnerAttention(_TPUCPInnerAttention):`
- members:
  - <a id="UlyssesCPInnerAttention.cp_shard"></a>`cp_shard(cls, input_dict: dict[str, Any], input_shardings: dict[str, Any] | None, cp_mesh: Any, load_balancer_type: str | None, ptrr_mask_key: str | None)` — [`L332`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/cp_attention.py#L332)
  - <a id="UlyssesCPInnerAttention.forward"></a>`forward(self, q_THK: torch.Tensor, k_THK: torch.Tensor, v_THV: torch.Tensor, **kwargs)` — [`L379`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/cp_attention.py#L379)
  - <a id="UlyssesCPInnerAttention.local_forward"></a>`local_forward(self, q_THK, k_THK, v_THV, **kwargs)` — [`L363`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/cp_attention.py#L363) — The wrapped single-device inner attention.
- protocol/private: <a id="UlyssesCPInnerAttention.__init__"></a>`__init__`[`L325`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/cp_attention.py#L325)
- uses (calls/refs, reference-scoped): [`MeshAxisName`](../../distributed/parallel_dims.md#MeshAxisName), [`ScaledDotProductInnerAttention`](../../models/common/attention.md#ScaledDotProductInnerAttention), [`VarlenInnerAttention`](../../models/common/attention.md#VarlenInnerAttention), [`prepare_context_parallel_input`](../../distributed/context_parallel/api.md#prepare_context_parallel_input), [`CP`](../../distributed/parallel_dims.md#MeshAxisName.CP), [`UlyssesCPScaledDotProductInnerAttention`](cp_attention.md#UlyssesCPScaledDotProductInnerAttention), [`_TOKEN_DIM`](cp_attention.md#_TOKEN_DIM), [`_orig_segment_ids_from_positions`](cp_attention.md#_orig_segment_ids_from_positions), [`UlyssesCPVarlenInnerAttention`](cp_attention.md#UlyssesCPVarlenInnerAttention), [`_full_sequence_segment_ids`](cp_attention.md#_full_sequence_segment_ids), [`_patch_segment_ids_from_positions`](cp_attention.md#_patch_segment_ids_from_positions), [`_TPUCPInnerAttention`](cp_attention.md#_TPUCPInnerAttention), [`spmd_mesh_group`](../../distributed/spmd_types.md#spmd_mesh_group), [`_all_to_all`](cp_attention.md#_all_to_all), [`_repeat_kv_heads`](cp_attention.md#_repeat_kv_heads), [`set_local_attention`](cp_attention.md#_TPUCPInnerAttention.set_local_attention), [`_HEAD_DIM`](cp_attention.md#_HEAD_DIM), [`_type_checking`](cp_attention.md#_type_checking), [`_local_attn_override`](cp_attention.md#_TPUCPInnerAttention._local_attn_override)
- used by: [`validate_tpu_context_parallel`](cp_attention.md#validate_tpu_context_parallel), [`UlyssesCPScaledDotProductInnerAttention`](cp_attention.md#UlyssesCPScaledDotProductInnerAttention), [`UlyssesCPVarlenInnerAttention`](cp_attention.md#UlyssesCPVarlenInnerAttention), [`cp_shard`](../../models/common/cp_attention.md#CPInnerAttention.cp_shard), [`_TPUCPInnerAttention`](cp_attention.md#_TPUCPInnerAttention)  (3 test-only)

### <a id="UlyssesCPScaledDotProductInnerAttention"></a>`UlyssesCPScaledDotProductInnerAttention`  ·  implements/extends ScaledDotProductInnerAttention, UlyssesCPInnerAttention
- def: [`torchtitan/experiments/tpu/cp_attention.py:854`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/cp_attention.py#L854) — documented in [tpu-context-parallel-attention](../../../../concepts/tpu-context-parallel-attention.md)
- signature: `class UlyssesCPScaledDotProductInnerAttention(UlyssesCPInnerAttention, ScaledDotProductInnerAttention):`
- uses (calls/refs, reference-scoped): [`ScaledDotProductInnerAttention`](../../models/common/attention.md#ScaledDotProductInnerAttention), [`UlyssesCPInnerAttention`](cp_attention.md#UlyssesCPInnerAttention)
- used by: [`ScaledDotProductInnerAttention`](../../models/common/attention.md#ScaledDotProductInnerAttention), [`_CP_INNER_ATTENTIONS`](cp_attention.md#_CP_INNER_ATTENTIONS), [`UlyssesCPInnerAttention`](cp_attention.md#UlyssesCPInnerAttention)  (6 test-only)

### <a id="UlyssesCPScaledDotProductInnerAttention.Config"></a>`UlyssesCPScaledDotProductInnerAttention.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/tpu/cp_attention.py:859`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/cp_attention.py#L859)
- signature: `class Config(ScaledDotProductInnerAttention.Config):`
- uses (calls/refs, reference-scoped): [`ScaledDotProductInnerAttention`](../../models/common/attention.md#ScaledDotProductInnerAttention), [`Config`](../../models/common/attention.md#ScaledDotProductInnerAttention.Config)
- used by: (6 test-only callers)

### <a id="UlyssesCPVarlenInnerAttention"></a>`UlyssesCPVarlenInnerAttention`  ·  implements/extends UlyssesCPInnerAttention, VarlenInnerAttention
- def: [`torchtitan/experiments/tpu/cp_attention.py:863`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/cp_attention.py#L863) — documented in [tpu-context-parallel-attention](../../../../concepts/tpu-context-parallel-attention.md)
- signature: `class UlyssesCPVarlenInnerAttention(UlyssesCPInnerAttention, VarlenInnerAttention):`
- uses (calls/refs, reference-scoped): [`VarlenInnerAttention`](../../models/common/attention.md#VarlenInnerAttention), [`UlyssesCPInnerAttention`](cp_attention.md#UlyssesCPInnerAttention)
- used by: [`VarlenInnerAttention`](../../models/common/attention.md#VarlenInnerAttention), [`_CP_INNER_ATTENTIONS`](cp_attention.md#_CP_INNER_ATTENTIONS), [`UlyssesCPInnerAttention`](cp_attention.md#UlyssesCPInnerAttention)  (2 test-only)

### <a id="UlyssesCPVarlenInnerAttention.Config"></a>`UlyssesCPVarlenInnerAttention.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/tpu/cp_attention.py:868`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/cp_attention.py#L868)
- signature: `class Config(VarlenInnerAttention.Config):`
- uses (calls/refs, reference-scoped): [`VarlenInnerAttention`](../../models/common/attention.md#VarlenInnerAttention), [`Config`](../../models/common/attention.md#VarlenInnerAttention.Config)
- used by: (1 test-only callers)

### <a id="_AllGatherKV"></a>`_AllGatherKV`
- def: [`torchtitan/experiments/tpu/cp_attention.py:164`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/cp_attention.py#L164)
- doc: Traceable All-Gather in forward and dtype-controlled Reduce-Scatter in backward.
- signature: `class _AllGatherKV(torch.autograd.Function):`
- members:
  - <a id="_AllGatherKV.backward"></a>`backward(ctx, grad_out: torch.Tensor)` — [`L182`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/cp_attention.py#L182)
  - <a id="_AllGatherKV.forward"></a>`forward(ctx, x: torch.Tensor, group: Any, seq_dim: int, reduce_dtype: torch.dtype)` — [`L168`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/cp_attention.py#L168)
- uses (calls/refs, reference-scoped): [`_wait`](cp_attention.md#_wait)
- used by: [`_all_gather_kv`](cp_attention.md#_all_gather_kv)

### <a id="_TPUCPInnerAttention"></a>`_TPUCPInnerAttention`  ·  implements/extends CPInnerAttention
- def: [`torchtitan/experiments/tpu/cp_attention.py:303`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/cp_attention.py#L303) — documented in [tpu-context-parallel-attention](../../../../concepts/tpu-context-parallel-attention.md)
- doc: Shared base for TPU CP inner attentions with pluggable local attention.
- signature: `class _TPUCPInnerAttention(CPInnerAttention):`
- members:
  - <a id="_TPUCPInnerAttention.extra_repr"></a>`extra_repr(self)` — [`L318`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/cp_attention.py#L318)
  - <a id="_TPUCPInnerAttention.set_local_attention"></a>`set_local_attention(self, local_attn: Callable[..., torch.Tensor] | None)` — [`L312`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/cp_attention.py#L312) — Replaces the local attention kernel, e.g. with TPU splash attention.
- protocol/private: <a id="_TPUCPInnerAttention._local_attn_override"></a>`_local_attn_override`[`L306`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/cp_attention.py#L306)
- uses (calls/refs, reference-scoped): [`CPInnerAttention`](../../models/common/cp_attention.md#CPInnerAttention), [`KVAllGatherCPInnerAttention`](cp_attention.md#KVAllGatherCPInnerAttention), [`UlyssesCPInnerAttention`](cp_attention.md#UlyssesCPInnerAttention)
- used by: [`forward`](cp_attention.md#KVAllGatherCPInnerAttention.forward), [`forward`](cp_attention.md#UlyssesCPInnerAttention.forward), [`CPInnerAttention`](../../models/common/cp_attention.md#CPInnerAttention), [`KVAllGatherCPInnerAttention`](cp_attention.md#KVAllGatherCPInnerAttention), [`UlyssesCPInnerAttention`](cp_attention.md#UlyssesCPInnerAttention), [`__init__`](cp_attention.md#KVAllGatherCPInnerAttention.__init__), [`__init__`](cp_attention.md#UlyssesCPInnerAttention.__init__)  (5 test-only)

## Functions
- <a id="_all_gather_kv"></a>`_all_gather_kv(x: torch.Tensor, group: Any, *, seq_dim: int = _TOKEN_DIM, reduce_dtype: torch.dtype = torch.float32)` — [`L188`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/cp_attention.py#L188) — All-gathers ``x`` from ``S(seq_dim)`` to ``R`` with ``reduce_dtype`` backward RS.
- <a id="_all_to_all"></a>`_all_to_all(x: torch.Tensor, group: Any, *, src_dim: int, dst_dim: int)` — [`L141`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/cp_attention.py#L141) — Reshards ``x`` from ``S(src_dim)`` to ``S(dst_dim)`` over ``group``.
- <a id="_cache_cp_rank_for_mesh"></a>`_cache_cp_rank_for_mesh(cp_mesh: DeviceMesh)` — [`L108`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/cp_attention.py#L108)
- <a id="_cp_segment_ids_from_positions"></a>`_cp_segment_ids_from_positions(positions: torch.Tensor)` — [`L266`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/cp_attention.py#L266) — Returns precomputed full-sequence ``segment_ids`` when sharded by ``cp_shard``.
- <a id="_full_sequence_segment_ids"></a>`_full_sequence_segment_ids(positions: torch.Tensor, group: Any)` — [`L290`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/cp_attention.py#L290) — Fallback packed-document ``segment_ids`` when ``cp_shard`` was not used.
- <a id="_normalize_cp_device"></a>`_normalize_cp_device(device: torch.device | str)` — [`L84`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/cp_attention.py#L84) — Returns a canonical ``torch.device`` for ``_CP_RANK_CACHE`` keys.
- <a id="_patch_segment_ids_from_positions"></a>`_patch_segment_ids_from_positions()` — [`L274`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/cp_attention.py#L274) — Patches ``Decoder`` to reuse full-sequence ``segment_ids`` from ``cp_shard``.
- <a id="_repeat_kv_heads"></a>`_repeat_kv_heads(x: torch.Tensor, cp: int)` — [`L245`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/cp_attention.py#L245) — Repeats KV heads so that each of the ``cp`` head shards gets one.
- <a id="_tracing"></a>`_tracing()` — [`L120`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/cp_attention.py#L120)
- <a id="_type_checking"></a>`_type_checking()` — [`L116`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/cp_attention.py#L116)
- <a id="_validate_heads"></a>`_validate_heads(fqn: str, attn: Any, tp: int, cp: int, strategy: CPStrategy)` — [`L942`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/cp_attention.py#L942)
- <a id="_validate_sequence_lengths"></a>`_validate_sequence_lengths(strategy: CPStrategy, cp: int, training: Any, splash_attention_kernel: Any | None)` — [`L974`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/cp_attention.py#L974) — Checks the sequence lengths a strategy can shard (and Splash can tile).
- <a id="_wait"></a>`_wait(x: torch.Tensor)` — [`L128`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/cp_attention.py#L128) — Waits on a functional collective's result exactly once.
- <a id="install_tpu_cp_patches"></a>`install_tpu_cp_patches()` — [`L1144`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/cp_attention.py#L1144) — Lets FSDP2 shard over ``(dp_shard, cp)`` on torch without spmd_types FSDP.
- <a id="reorder_sequence"></a>`reorder_sequence(tensor: torch.Tensor, cp_size: int, seq_dim: int = 1, to_contiguous: bool = False)` — [`L207`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/cp_attention.py#L207) — Reorders ``tensor`` along ``seq_dim`` between contiguous and head-tail CP order. — documented in [tpu-context-parallel-attention](../../../../concepts/tpu-context-parallel-attention.md)
- <a id="install_tpu_cp_patches.resolve_flattened"></a>`resolve_flattened(parallel_dims)` — [`L1166`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/cp_attention.py#L1166)
- <a id="revert_tpu_context_parallel"></a>`revert_tpu_context_parallel(model: Any)` — [`L1124`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/cp_attention.py#L1124) — Swaps TPU CP inner attentions back to their single-device versions.
- <a id="tpu_cp_inner_attention"></a>`tpu_cp_inner_attention(base: type[Any], strategy: CPStrategy)` — [`L911`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/cp_attention.py#L911) — Returns the TPU CP inner attention for ``base`` under ``strategy``.
- <a id="tpu_cp_load_balancer"></a>`tpu_cp_load_balancer(strategy: CPStrategy)` — [`L932`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/cp_attention.py#L932) — Returns the ``context_parallel_load_balancer`` that ``strategy`` needs.
- <a id="validate_tpu_context_parallel"></a>`validate_tpu_context_parallel(model: Any, parallelism: Any, *, training: Any | None = None, splash_attention_kernel: Any | None = None)` — [`L1050`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/cp_attention.py#L1050) — Checks TPU CP attention against the parallelism config. — documented in [tpu-context-parallel-attention](../../../../concepts/tpu-context-parallel-attention.md)

## Module values
- <a id="CPStrategy"></a>`CPStrategy` — [`L894`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/cp_attention.py#L894)
- <a id="_CP_INNER_ATTENTIONS"></a>`_CP_INNER_ATTENTIONS` — [`L897`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/cp_attention.py#L897)
- <a id="_CP_RANK_CACHE._CP_RANK_CACHE"></a>`_CP_RANK_CACHE` — [`L81`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/cp_attention.py#L81)
- <a id="_HEAD_DIM"></a>`_HEAD_DIM` — [`L76`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/cp_attention.py#L76)
- <a id="_TOKEN_DIM"></a>`_TOKEN_DIM` — [`L75`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/cp_attention.py#L75)
- <a id="__all__"></a>`__all__` — [`L60`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/cp_attention.py#L60)
- <a id="_orig_segment_ids_from_positions"></a>`_orig_segment_ids_from_positions` — [`L263`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/cp_attention.py#L263)
- <a id="_patched"></a>`_patched` — [`L1141`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/cp_attention.py#L1141)

