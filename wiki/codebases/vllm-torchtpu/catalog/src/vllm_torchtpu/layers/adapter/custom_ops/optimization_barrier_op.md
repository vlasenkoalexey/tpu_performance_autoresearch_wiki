---
title: 'Module: src/vllm_torchtpu/layers/adapter/custom_ops/optimization_barrier_op.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/layers/adapter/custom_ops/optimization_barrier_op.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.layers.adapter.custom_ops.optimization_barrier_op`/
symbols:
  optimization_barrier_op: optimization_barrier_op().
  optimization_barrier: optimization_barrier().
  optimization_barrier_op._optimization_barrier: optimization_barrier_op()._optimization_barrier().
---
# Module: [`src/vllm_torchtpu/layers/adapter/custom_ops/optimization_barrier_op.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/optimization_barrier_op.py)

## Functions
- <a id="optimization_barrier_op._optimization_barrier"></a>`_optimization_barrier(x: jax.Array)` — [`L32`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/optimization_barrier_op.py#L32)
- <a id="optimization_barrier"></a>`optimization_barrier(x: torch.Tensor)` — [`L40`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/optimization_barrier_op.py#L40) — Block XLA fusion passes from fusing across ``x``.
- <a id="optimization_barrier_op"></a>`optimization_barrier_op()` — [`L29`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/optimization_barrier_op.py#L29) — Build the ``pallas::optimization_barrier`` custom op on first TPU use. — documented in [omni-diffusion-support](../../../../../../concepts/omni-diffusion-support.md)

