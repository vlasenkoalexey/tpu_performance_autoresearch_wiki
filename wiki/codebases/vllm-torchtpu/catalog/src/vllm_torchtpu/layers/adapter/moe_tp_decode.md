---
title: 'Module: src/vllm_torchtpu/layers/adapter/moe_tp_decode.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/layers/adapter/moe_tp_decode.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.layers.adapter.moe_tp_decode`/
symbols:
  _admit: _admit().
  arm: arm().
  _selftest: _selftest().
  _topology: _topology().
  moe_tp_decode_forward: moe_tp_decode_forward().
  _op_body.body: _op_body().body().
  _selftest_op: _selftest_op().
  _tp_chain: _tp_chain().
  _get_op: _get_op().
  _shared_slice: _shared_slice().
  moe_tp_decode_supported: moe_tp_decode_supported().
  _Topology.mesh_index: _Topology#mesh_index.
  _op_body: _op_body().
  _SELFTEST_OPS._SELFTEST_OPS: _SELFTEST_OPS._SELFTEST_OPS.
  _Topology.mesh: _Topology#mesh.
  logger: logger.
  _rank_tensor: _rank_tensor().
  _OpStatics: _OpStatics#
  _OPS._OPS: _OPS._OPS.
  _RANK_BUFFER._RANK_BUFFER: _RANK_BUFFER._RANK_BUFFER.
  _Admitted.statics: _Admitted#statics.
  _check_ranks_agree: _check_ranks_agree().
  _OP_ATTR: _OP_ATTR.
  _SELFTEST_DONE: _SELFTEST_DONE.
  _Topology: _Topology#
  _OpStatics.topk: _OpStatics#topk.
  _BUFFERS: _BUFFERS.
  _OpStatics.routed_scale: _OpStatics#routed_scale.
  _Admitted: _Admitted#
  _gather: _gather().
  SELFTEST_TIMEOUT_S: SELFTEST_TIMEOUT_S.
  _SUM_FLOOR: _SUM_FLOOR.
  _OpStatics.activation: _OpStatics#activation.
  _OpStatics.use_sparse_core: _OpStatics#use_sparse_core.
  _OpStatics.onehot_threshold: _OpStatics#onehot_threshold.
  _Admitted.shared: _Admitted#shared.
  _Admitted.rows: _Admitted#rows.
  _Admitted.hidden: _Admitted#hidden.
  _sds: _sds().
  _get_op.fn: _get_op().fn().
  _selftest_op.body: _selftest_op().body().
  _selftest_op.fn: _selftest_op().fn().
---
# Module: [`src/vllm_torchtpu/layers/adapter/moe_tp_decode.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/moe_tp_decode.py)

## Classes
### <a id="_Admitted"></a>`_Admitted`
- def: [`src/vllm_torchtpu/layers/adapter/moe_tp_decode.py:103`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/moe_tp_decode.py#L103)
- signature: `class _Admitted:`
- members:
  - <a id="_Admitted.hidden"></a>`hidden` — [`L106`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/moe_tp_decode.py#L106)
  - <a id="_Admitted.rows"></a>`rows` — [`L105`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/moe_tp_decode.py#L105)
  - <a id="_Admitted.shared"></a>`shared` — [`L104`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/moe_tp_decode.py#L104)
  - <a id="_Admitted.statics"></a>`statics` — [`L107`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/moe_tp_decode.py#L107)
- uses (calls/refs, reference-scoped): [`_OpStatics`](moe_tp_decode.md#_OpStatics)
- used by: [`_admit`](moe_tp_decode.md#_admit)

### <a id="_OpStatics"></a>`_OpStatics`
- def: [`src/vllm_torchtpu/layers/adapter/moe_tp_decode.py:94`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/moe_tp_decode.py#L94)
- signature: `class _OpStatics:`
- members:
  - <a id="_OpStatics.activation"></a>`activation` — [`L97`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/moe_tp_decode.py#L97)
  - <a id="_OpStatics.onehot_threshold"></a>`onehot_threshold` — [`L99`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/moe_tp_decode.py#L99)
  - <a id="_OpStatics.routed_scale"></a>`routed_scale` — [`L96`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/moe_tp_decode.py#L96)
  - <a id="_OpStatics.topk"></a>`topk` — [`L95`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/moe_tp_decode.py#L95)
  - <a id="_OpStatics.use_sparse_core"></a>`use_sparse_core` — [`L98`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/moe_tp_decode.py#L98)
- used by: [`_admit`](moe_tp_decode.md#_admit), [`body`](moe_tp_decode.md#_op_body.body), [`_get_op`](moe_tp_decode.md#_get_op), [`_op_body`](moe_tp_decode.md#_op_body), [`statics`](moe_tp_decode.md#_Admitted.statics)

### <a id="_Topology"></a>`_Topology`
- def: [`src/vllm_torchtpu/layers/adapter/moe_tp_decode.py:88`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/moe_tp_decode.py#L88)
- signature: `class _Topology:`
- members:
  - <a id="_Topology.mesh"></a>`mesh` — [`L89`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/moe_tp_decode.py#L89)
  - <a id="_Topology.mesh_index"></a>`mesh_index` — [`L90`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/moe_tp_decode.py#L90)
- used by: [`arm`](moe_tp_decode.md#arm), [`_selftest`](moe_tp_decode.md#_selftest), [`_topology`](moe_tp_decode.md#_topology)

## Functions
- <a id="_admit"></a>`_admit(runner, n_ranks: int)` — [`L177`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/moe_tp_decode.py#L177) — What arming needs for this runner, or why it keeps the usual path. — documented in [quantization-methods](../../../../../concepts/quantization-methods.md)
- <a id="_check_ranks_agree"></a>`_check_ranks_agree(entry: dict)` — [`L501`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/moe_tp_decode.py#L501) — Raise unless every TP rank arms the same layers with the same statics
- <a id="_gather"></a>`_gather(obj)` — [`L491`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/moe_tp_decode.py#L491) — all_gather_object over the TP group's CPU group.
- <a id="_get_op"></a>`_get_op(mesh, statics: _OpStatics)` — [`L358`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/moe_tp_decode.py#L358) — One jax_op per distinct closure; built at arming, never in a trace.
- <a id="_op_body"></a>`_op_body(statics: _OpStatics, n_ranks: int, axis: str)` — [`L328`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/moe_tp_decode.py#L328) — The op's per-rank body under shard_map over `axis`: the fused kernel at
- <a id="_rank_tensor"></a>`_rank_tensor(device: torch.device, mesh_index: int)` — [`L458`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/moe_tp_decode.py#L458) — This rank's mesh index as int32 [1, 1] data (one tensor per process), so
- <a id="_sds"></a>`_sds(t: torch.Tensor)` — [`L115`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/moe_tp_decode.py#L115)
- <a id="_selftest"></a>`_selftest(topo: _Topology, buckets, device)` — [`L467`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/moe_tp_decode.py#L467) — Run the kernel's all-reduce alone for every armed (rows, hidden) and row
- <a id="_selftest_op"></a>`_selftest_op(mesh, spec: all_reduce.AllReduceSpec)` — [`L422`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/moe_tp_decode.py#L422)
- <a id="_shared_slice"></a>`_shared_slice(runner)` — [`L141`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/moe_tp_decode.py#L141) — This rank's shared-expert tensors (w13 [D, 2Fs], s13 [2Fs], w2 [Fs, D],
- <a id="_topology"></a>`_topology()` — [`L121`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/moe_tp_decode.py#L121) — The op's 1-D mesh over the TP group and this rank's index in it, or a — documented in [distributed-parallelism-and-meshes](../../../../../concepts/distributed-parallelism-and-meshes.md)
- <a id="_tp_chain"></a>`_tp_chain(x, scores, bias, is_pad, w13, w2, s13, s2, sw13, ss13, sw2, ss2, st)` — [`L290`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/moe_tp_decode.py#L290) — This rank's partial as the unarmed TP path computes it: select_experts
- <a id="arm"></a>`arm(model: torch.nn.Module, draft_model: torch.nn.Module | None = None)` — [`L519`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/moe_tp_decode.py#L519) — Arm every admitted MoE layer of `model` and of `draft_model` (the MTP — documented in [speculative-decoding](../../../../../concepts/speculative-decoding.md)
- <a id="_op_body.body"></a>`body(x, scores, bias, pad_mask, w13, w2, s13, s2, sw13, ss13, sw2, ss2, rank)` — [`L333`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/moe_tp_decode.py#L333)
- <a id="_selftest_op.body"></a>`body(x, rank, n_valid)` — [`L430`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/moe_tp_decode.py#L430)
- <a id="_get_op.fn"></a>`fn(x: jax.Array, scores: jax.Array, bias: jax.Array, pad_mask: jax.Array, w13: jax.Array, w2: jax.Array, s13: jax.Array, s2: jax.Array, sw13: jax.Array, ss13: jax.Array, sw2: jax.Array, ss2: jax.Array, rank: jax.Array)` — [`L375`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/moe_tp_decode.py#L375)
- <a id="_selftest_op.fn"></a>`fn(x: jax.Array, rank: jax.Array, n_valid: jax.Array)` — [`L438`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/moe_tp_decode.py#L438)
- <a id="moe_tp_decode_forward"></a>`moe_tp_decode_forward(quant_method: Any, layer: Any, x: torch.Tensor, router_logits: torch.Tensor)` — [`L600`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/moe_tp_decode.py#L600) — Forward of an armed layer: shared + routed_scaling_factor * routed,
- <a id="moe_tp_decode_supported"></a>`moe_tp_decode_supported(quant_method: Any)` — [`L110`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/moe_tp_decode.py#L110) — Whether arming gave this layer's quant method the op.

## Module values
- <a id="SELFTEST_TIMEOUT_S"></a>`SELFTEST_TIMEOUT_S` — [`L78`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/moe_tp_decode.py#L78)
- <a id="_BUFFERS"></a>`_BUFFERS` — [`L68`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/moe_tp_decode.py#L68)
- <a id="_OPS._OPS"></a>`_OPS` — [`L81`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/moe_tp_decode.py#L81)
- <a id="_OP_ATTR"></a>`_OP_ATTR` — [`L64`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/moe_tp_decode.py#L64)
- <a id="_RANK_BUFFER._RANK_BUFFER"></a>`_RANK_BUFFER` — [`L83`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/moe_tp_decode.py#L83)
- <a id="_SELFTEST_DONE"></a>`_SELFTEST_DONE` — [`L84`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/moe_tp_decode.py#L84)
- <a id="_SELFTEST_OPS._SELFTEST_OPS"></a>`_SELFTEST_OPS` — [`L82`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/moe_tp_decode.py#L82)
- <a id="_SUM_FLOOR"></a>`_SUM_FLOOR` — [`L79`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/moe_tp_decode.py#L79)
- <a id="logger"></a>`logger` — [`L62`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/moe_tp_decode.py#L62)

