---
title: 'Module: torchtitan/distributed/compile.py'
type: catalog
provenance: extracted
module: torchtitan/distributed/compile.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.distributed.compile`/
symbols:
  apply_compile: apply_compile().
  _maybe_enable_async_tp: _maybe_enable_async_tp().
  _maybe_regional_inductor_backend: _maybe_regional_inductor_backend().
  maybe_regional_inductor: maybe_regional_inductor().
  _regional_inductor_enabled._regional_inductor_enabled: _regional_inductor_enabled._regional_inductor_enabled.
---
# Module: [`torchtitan/distributed/compile.py`](../../../../../../raw/code/torchtitan/torchtitan/distributed/compile.py)

## Functions
- <a id="_maybe_enable_async_tp"></a>`_maybe_enable_async_tp(compile_config: CompileConfig, tp_mesh: DeviceMesh | None)` — [`L75`](../../../../../../raw/code/torchtitan/torchtitan/distributed/compile.py#L75) — Configure Inductor's async TP pass for the provided TP mesh.
- <a id="_maybe_regional_inductor_backend"></a>`_maybe_regional_inductor_backend(model: nn.Module, backend: str)` — [`L99`](../../../../../../raw/code/torchtitan/torchtitan/distributed/compile.py#L99) — Wrap the ``aot_eager`` backend so inductor-only flex regions are scooped out.
- <a id="apply_compile"></a>`apply_compile(model: nn.Module, *, compile_config: CompileConfig, parallel_dims: ParallelDims)` — [`L39`](../../../../../../raw/code/torchtitan/torchtitan/distributed/compile.py#L39) — Apply torch.compile to each TransformerBlock, which makes compilation efficient due to — documented in [parallel-dims-and-parallelization](../../../concepts/parallel-dims-and-parallelization.md)
- <a id="maybe_regional_inductor"></a>`maybe_regional_inductor(inductor_configs: dict)` — [`L137`](../../../../../../raw/code/torchtitan/torchtitan/distributed/compile.py#L137) — Context manager that marks the wrapped region for ``regional_inductor``.

## Module values
- <a id="_regional_inductor_enabled._regional_inductor_enabled"></a>`_regional_inductor_enabled` — [`L36`](../../../../../../raw/code/torchtitan/torchtitan/distributed/compile.py#L36)

