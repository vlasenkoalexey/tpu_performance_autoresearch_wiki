---
title: 'Module: src/torch_tpu/_internal/sync/sync.py'
type: catalog
provenance: extracted
module: src/torch_tpu/_internal/sync/sync.py
status: fresh
symbol_base: scip-python python torch_tpu 0.0.0 `src.torch_tpu._internal.sync.sync`/
symbols:
  dump_computation_graphviz: dump_computation_graphviz().
  dump_computation_mlir: dump_computation_mlir().
  synchronize: synchronize.
  _dump_computation: _dump_computation().
  computation_graphviz: computation_graphviz().
  computation_mlir: computation_mlir().
  is_materializing: is_materializing.
  is_materialized: is_materialized.
---
# Module: [`src/torch_tpu/_internal/sync/sync.py`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/sync/sync.py)

## Functions
- <a id="_dump_computation"></a>`_dump_computation(str_to_dump: str, file_name: str)` — [`L31`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/sync/sync.py#L31) — Dumps a string to a file.
- <a id="computation_graphviz"></a>`computation_graphviz(*tensors: list[torch.Tensor] | tuple[torch.Tensor, ...])` — [`L54`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/sync/sync.py#L54) — Returns a graphviz compatible representation of the aten traversal of the given tensors.
- <a id="computation_mlir"></a>`computation_mlir(*tensors: list[torch.Tensor] | tuple[torch.Tensor, ...])` — [`L64`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/sync/sync.py#L64) — Returns a MLIR representation of the aten traversal of the given tensors.
- <a id="dump_computation_graphviz"></a>`dump_computation_graphviz(tensors: list[torch.Tensor], file_name: str)` — [`L44`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/sync/sync.py#L44) — Dumps a graphviz compatible representation of the aten traversal of the given tensors, to a file_name.
- <a id="dump_computation_mlir"></a>`dump_computation_mlir(tensors: list[torch.Tensor], file_name: str)` — [`L49`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/sync/sync.py#L49) — Dumps a graphviz compatible representation of the aten traversal of the given tensors, to a file_name.

## Module values
- <a id="is_materialized"></a>`is_materialized` — [`L28`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/sync/sync.py#L28)
- <a id="is_materializing"></a>`is_materializing` — [`L27`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/sync/sync.py#L27)
- <a id="synchronize"></a>`synchronize` — [`L26`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/sync/sync.py#L26)

