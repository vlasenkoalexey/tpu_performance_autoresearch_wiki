---
title: 'Module: src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/vllm_adapter.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/vllm_adapter.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.experimental.adaptive_fused_moe.vllm_adapter`/
symbols:
  prebuild_adaptive_fused_moe: prebuild_adaptive_fused_moe().
  fused_moe_ep_unsupported_reason: fused_moe_ep_unsupported_reason().
  _build_op: _build_op().
  run_adaptive_fused_moe: run_adaptive_fused_moe().
  prebuild_adaptive_nvfp4: prebuild_adaptive_nvfp4().
  _build_op.moe: _build_op().moe().
  adaptive_fused_moe_supported: adaptive_fused_moe_supported().
  _mesh_expert_order: _mesh_expert_order().
  logger: logger.
  _OPS._OPS: _OPS._OPS.
  _RANK_BUFFER._RANK_BUFFER: _RANK_BUFFER._RANK_BUFFER.
  _unsupported_routing_reason: _unsupported_routing_reason().
  _TILE_M: _TILE_M.
  PreparedWeights: PreparedWeights.
  FUSED_MOE_EP_OP_NAME: FUSED_MOE_EP_OP_NAME.
  FUSED_MOE_EP_OP_ATTR: FUSED_MOE_EP_OP_ATTR.
  _squeeze_channel_scale: _squeeze_channel_scale().
  _squeeze_channel_scale_checked: _squeeze_channel_scale_checked().
  run_adaptive_fused_moe.block_scale: run_adaptive_fused_moe().block_scale().
  _SMEM_OVERHEAD_BYTES: _SMEM_OVERHEAD_BYTES.
  _device_info: _device_info().
  _max_node_tokens: _max_node_tokens().
  _build_op._fake: _build_op()._fake().
---
# Module: [`src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/vllm_adapter.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/vllm_adapter.py)

## Functions
- <a id="_build_op"></a>`_build_op(mesh: Mesh, topk: int, renormalize: bool, activation: str, mesh_expert_order: tuple[int, ...] | None, weight_format: str = "fp8", rhs_qb: int | None = None, *, token_replica_groups: tuple[tuple[int, ...], ...] | None = None)` — [`L413`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/vllm_adapter.py#L413) — The op for this closure, built once per distinct closure and reused. — documented in [adaptive-fused-moe-kernel](../../../../../../concepts/adaptive-fused-moe-kernel.md)
- <a id="_device_info"></a>`_device_info()` — [`L67`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/vllm_adapter.py#L67)
- <a id="_build_op._fake"></a>`_fake(x, *_args, **_kwargs)` — [`L505`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/vllm_adapter.py#L505)
- <a id="_max_node_tokens"></a>`_max_node_tokens(ep: int, pcp: int)` — [`L71`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/vllm_adapter.py#L71)
- <a id="_mesh_expert_order"></a>`_mesh_expert_order(ep: int)` — [`L282`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/vllm_adapter.py#L282) — Which EP rank's expert block belongs at each mesh index, or None.
- <a id="_squeeze_channel_scale"></a>`_squeeze_channel_scale(scale: torch.Tensor, experts: int, channels: int)` — [`L244`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/vllm_adapter.py#L244) — Our GMM scales are 4-D ``[E, blocks, 1, N]``; the kernel takes ``[E, N]``.
- <a id="_squeeze_channel_scale_checked"></a>`_squeeze_channel_scale_checked(scale: torch.Tensor)` — [`L265`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/vllm_adapter.py#L265) — `_squeeze_channel_scale` without the shape arguments, for the hot path.
- <a id="_unsupported_routing_reason"></a>`_unsupported_routing_reason(layer: RoutedExperts)` — [`L369`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/vllm_adapter.py#L369) — Why this layer's ROUTING cannot go through the kernel, or None.
- <a id="adaptive_fused_moe_supported"></a>`adaptive_fused_moe_supported(owner: Any)` — [`L195`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/vllm_adapter.py#L195) — Only a successfully prebuilt op owns vLLM's dispatch/combine. — documented in [adaptive-fused-moe-kernel](../../../../../../concepts/adaptive-fused-moe-kernel.md)
- <a id="run_adaptive_fused_moe.block_scale"></a>`block_scale(scale)` — [`L529`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/vllm_adapter.py#L529)
- <a id="fused_moe_ep_unsupported_reason"></a>`fused_moe_ep_unsupported_reason(layer: RoutedExperts, weights: PreparedWeights, activation: str, *, weight_format: str = "fp8", rhs_qb: int | None = None)` — [`L306`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/vllm_adapter.py#L306) — Validate prepared (or meta) weights and routing before installation. — documented in [adaptive-fused-moe-kernel](../../../../../../concepts/adaptive-fused-moe-kernel.md)
- <a id="_build_op.moe"></a>`moe(x: jax.Array, w1: jax.Array, w2: jax.Array, w1_scale: jax.Array, w2_scale: jax.Array, gating: jax.Array, rank: jax.Array)` — [`L446`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/vllm_adapter.py#L446)
- <a id="prebuild_adaptive_fused_moe"></a>`prebuild_adaptive_fused_moe(layer: RoutedExperts, topk: int, renormalize: bool, activation: str, *, weights: PreparedWeights | None = None, rhs_qb: int | None = None)` — [`L81`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/vllm_adapter.py#L81) — Build the selected experimental path, raising on every refusal. — documented in [adaptive-fused-moe-kernel](../../../../../../concepts/adaptive-fused-moe-kernel.md)
- <a id="prebuild_adaptive_nvfp4"></a>`prebuild_adaptive_nvfp4(layer: RoutedExperts, activation: str, configured_block: int | None = None)` — [`L200`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/vllm_adapter.py#L200) — Validate checkpoint geometry before committing runtime requantization. — documented in [adaptive-fused-moe-kernel](../../../../../../concepts/adaptive-fused-moe-kernel.md)
- <a id="run_adaptive_fused_moe"></a>`run_adaptive_fused_moe(owner: Any, hidden_states: torch.Tensor, w1: torch.Tensor, w2: torch.Tensor, w1_scale: torch.Tensor, w2_scale: torch.Tensor, router_logits: torch.Tensor)` — [`L513`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/vllm_adapter.py#L513) — Execute a successfully prebuilt experimental op, or raise. — documented in [adaptive-fused-moe-kernel](../../../../../../concepts/adaptive-fused-moe-kernel.md)

## Module values
- <a id="FUSED_MOE_EP_OP_ATTR"></a>`FUSED_MOE_EP_OP_ATTR` — [`L62`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/vllm_adapter.py#L62)
- <a id="FUSED_MOE_EP_OP_NAME"></a>`FUSED_MOE_EP_OP_NAME` — [`L61`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/vllm_adapter.py#L61)
- <a id="PreparedWeights"></a>`PreparedWeights` — [`L56`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/vllm_adapter.py#L56)
- <a id="_OPS._OPS"></a>`_OPS` — [`L63`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/vllm_adapter.py#L63)
- <a id="_RANK_BUFFER._RANK_BUFFER"></a>`_RANK_BUFFER` — [`L64`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/vllm_adapter.py#L64)
- <a id="_SMEM_OVERHEAD_BYTES"></a>`_SMEM_OVERHEAD_BYTES` — [`L60`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/vllm_adapter.py#L60)
- <a id="_TILE_M"></a>`_TILE_M` — [`L59`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/vllm_adapter.py#L59)
- <a id="logger"></a>`logger` — [`L58`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/vllm_adapter.py#L58)

