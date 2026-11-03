---
title: 'Module: src/vllm_torchtpu/distributed/sharded_jax_op.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/distributed/sharded_jax_op.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.distributed.sharded_jax_op`/
symbols:
  sharded_jax_op: sharded_jax_op().
  _build_sharded_callable_cls: _build_sharded_callable_cls().
  _sharded_output_placeholders: _sharded_output_placeholders().
  _SHARDED_CALLABLE_CLS: _SHARDED_CALLABLE_CLS.
  logger: logger.
  sharded_jax_op.fake_fn: sharded_jax_op().fake_fn().
  _STOCK_PLACEHOLDER_LINE: _STOCK_PLACEHOLDER_LINE.
  _SHARDED_PLACEHOLDER_LINE: _SHARDED_PLACEHOLDER_LINE.
  _placeholder: _placeholder().
---
# Module: [`src/vllm_torchtpu/distributed/sharded_jax_op.py`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/sharded_jax_op.py)

## Functions
- <a id="_build_sharded_callable_cls"></a>`_build_sharded_callable_cls()` — [`L97`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/sharded_jax_op.py#L97) — A ``JaxCallable`` whose ``__call__`` is the installed one, minus the
- <a id="_placeholder"></a>`_placeholder(aval, spec, mesh)` — [`L71`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/sharded_jax_op.py#L71) — One output tensor, shaped by ``spec`` rather than by the aval.
- <a id="_sharded_output_placeholders"></a>`_sharded_output_placeholders(lowered, mesh)` — [`L55`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/sharded_jax_op.py#L55) — Torch placeholders sized for this rank's shard of each output.
- <a id="sharded_jax_op.fake_fn"></a>`fake_fn(*args, **kwargs)` — [`L206`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/sharded_jax_op.py#L206)
- <a id="sharded_jax_op"></a>`sharded_jax_op(name: str, fn: Callable[..., object], *, mesh: jax.sharding.Mesh, input_partition_specs: Sequence[PartitionSpec], output_partition_specs: Any, donate_argnums: Sequence[int] | None = None)` — [`L135`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/sharded_jax_op.py#L135) — A torch custom op for ``fn`` run as an SPMD program over ``mesh``. — documented in [distributed-parallelism-and-meshes](../../../../concepts/distributed-parallelism-and-meshes.md)

## Module values
- <a id="_SHARDED_CALLABLE_CLS"></a>`_SHARDED_CALLABLE_CLS` — [`L132`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/sharded_jax_op.py#L132)
- <a id="_SHARDED_PLACEHOLDER_LINE"></a>`_SHARDED_PLACEHOLDER_LINE` — [`L50`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/sharded_jax_op.py#L50)
- <a id="_STOCK_PLACEHOLDER_LINE"></a>`_STOCK_PLACEHOLDER_LINE` — [`L47`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/sharded_jax_op.py#L47)
- <a id="logger"></a>`logger` — [`L45`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/sharded_jax_op.py#L45)

