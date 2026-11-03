---
title: 'Module: src/vllm_torchtpu/layers/adapter/fused_moe_decode.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/layers/adapter/fused_moe_decode.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.layers.adapter.fused_moe_decode`/
symbols:
  arm_fused_moe_decode: arm_fused_moe_decode().
  _gmm_layer: _gmm_layer().
  _build_op: _build_op().
  _layer: _layer().
  fused_moe_decode: fused_moe_decode().
  _admit: _admit().
  logger: logger.
  _RANK_BUFFER_START: _RANK_BUFFER_START.
  fused_moe_decode_supported: fused_moe_decode_supported().
  arm_runner_models: arm_runner_models().
  _OPS._OPS: _OPS._OPS.
  _RANK_BUFFER._RANK_BUFFER: _RANK_BUFFER._RANK_BUFFER.
  _RANK_BUFFER_INDEX._RANK_BUFFER_INDEX: _RANK_BUFFER_INDEX._RANK_BUFFER_INDEX.
  _shared_slice: _shared_slice().
  _check_vmem: _check_vmem().
  _check_same_arming_on_every_rank: _check_same_arming_on_every_rank().
  FUSED_MOE_DECODE_OP_ATTR: FUSED_MOE_DECODE_OP_ATTR.
  _SHARED_BUFFERS: _SHARED_BUFFERS.
  _RUNNER_ARMED_ATTR: _RUNNER_ARMED_ATTR.
  _build_op.fn: _build_op().fn().
  _build_op._fake: _build_op()._fake().
  _shared_mlp_is_ungated_silu: _shared_mlp_is_ungated_silu().
---
# Module: [`src/vllm_torchtpu/layers/adapter/fused_moe_decode.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/fused_moe_decode.py)

## Functions
- <a id="_admit"></a>`_admit(runner, n_ranks: int)` — [`L410`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/fused_moe_decode.py#L410) — (shared-expert tensors, expert_parallel, routed scale) for an eligible
- <a id="_build_op"></a>`_build_op(mesh, n_ranks: int, topk: int, expert_parallel: bool, max_tokens: int, shared_gated: bool = True, routed_scale: float = 1)` — [`L249`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/fused_moe_decode.py#L249)
- <a id="_check_same_arming_on_every_rank"></a>`_check_same_arming_on_every_rank(signature: tuple, what: str)` — [`L493`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/fused_moe_decode.py#L493) — Raise unless every EP rank computed the same arming signature: a rank
- <a id="_check_vmem"></a>`_check_vmem(max_tokens: int, layer, i_s: int, n_ranks: int)` — [`L477`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/fused_moe_decode.py#L477) — Refuse a token cap the kernel cannot be built for, at arming rather than
- <a id="_build_op._fake"></a>`_fake(x, *_args, **_kwargs)` — [`L333`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/fused_moe_decode.py#L333)
- <a id="_gmm_layer"></a>`_gmm_layer(x, w1, w2, w1_scale, w2_scale, shared_w1, shared_w1_scale, shared_w2, shared_w2_scale, shared_gate_weight, tw, ti, start, *, topk, shared_gated, routed_scale)` — [`L105`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/fused_moe_decode.py#L105) — Above the cap: the layer as the runner computes it with the kernel off,
- <a id="_layer"></a>`_layer(rank, x, w1, w2, w1_scale, w2_scale, shared_w1, shared_w1_scale, shared_w2, shared_w2_scale, shared_gate_weight, tw, ti, *, n_ranks, topk, expert_parallel, max_tokens, shared_gated=True, routed_scale=1)` — [`L167`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/fused_moe_decode.py#L167) — Per-rank body of the op: the kernel up to `max_tokens`, GMM MoE above.
- <a id="_shared_mlp_is_ungated_silu"></a>`_shared_mlp_is_ungated_silu(mlp)` — [`L341`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/fused_moe_decode.py#L341) — A shared expert with no gate of its own: gate_up -> SiluAndMul -> down
- <a id="_shared_slice"></a>`_shared_slice(runner)` — [`L353`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/fused_moe_decode.py#L353) — This rank's shared-expert tensors in the kernel's layout, or None. The
- <a id="arm_fused_moe_decode"></a>`arm_fused_moe_decode(model: torch.nn.Module, what: str = "model")` — [`L513`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/fused_moe_decode.py#L513) — Arm every eligible MoE layer of `model`; returns how many were armed. — documented in [distributed-parallelism-and-meshes](../../../../../concepts/distributed-parallelism-and-meshes.md)
- <a id="arm_runner_models"></a>`arm_runner_models(model_runner: Any)` — [`L652`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/fused_moe_decode.py#L652) — Arm the target model and, when it is a separate module, the drafter's
- <a id="_build_op.fn"></a>`fn(x: jax.Array, w1: jax.Array, w2: jax.Array, w1_scale: jax.Array, w2_scale: jax.Array, shared_w1: jax.Array, shared_w1_scale: jax.Array, shared_w2: jax.Array, shared_w2_scale: jax.Array, shared_gate_weight: jax.Array, tw: jax.Array, ti: jax.Array, rank: jax.Array)` — [`L283`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/fused_moe_decode.py#L283)
- <a id="fused_moe_decode"></a>`fused_moe_decode(quant_method: Any, layer: Any, x: torch.Tensor, topk_weights, topk_ids)` — [`L622`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/fused_moe_decode.py#L622) — Forward for an armed layer: the all-reduced (shared + routed) output.
- <a id="fused_moe_decode_supported"></a>`fused_moe_decode_supported(quant_method: Any)` — [`L101`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/fused_moe_decode.py#L101)

## Module values
- <a id="FUSED_MOE_DECODE_OP_ATTR"></a>`FUSED_MOE_DECODE_OP_ATTR` — [`L78`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/fused_moe_decode.py#L78)
- <a id="_OPS._OPS"></a>`_OPS` — [`L92`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/fused_moe_decode.py#L92)
- <a id="_RANK_BUFFER._RANK_BUFFER"></a>`_RANK_BUFFER` — [`L96`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/fused_moe_decode.py#L96)
- <a id="_RANK_BUFFER_INDEX._RANK_BUFFER_INDEX"></a>`_RANK_BUFFER_INDEX` — [`L98`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/fused_moe_decode.py#L98)
- <a id="_RANK_BUFFER_START"></a>`_RANK_BUFFER_START` — [`L97`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/fused_moe_decode.py#L97)
- <a id="_RUNNER_ARMED_ATTR"></a>`_RUNNER_ARMED_ATTR` — [`L79`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/fused_moe_decode.py#L79)
- <a id="_SHARED_BUFFERS"></a>`_SHARED_BUFFERS` — [`L83`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/fused_moe_decode.py#L83)
- <a id="logger"></a>`logger` — [`L76`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/fused_moe_decode.py#L76)

