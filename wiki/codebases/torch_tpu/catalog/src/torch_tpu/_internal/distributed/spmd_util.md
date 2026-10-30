---
title: 'Module: src/torch_tpu/_internal/distributed/spmd_util.py'
type: catalog
provenance: extracted
module: src/torch_tpu/_internal/distributed/spmd_util.py
status: fresh
symbol_base: scip-python python torch_tpu 0.0.0 `src.torch_tpu._internal.distributed.spmd_util`/
symbols:
  spmd_safe.wrapper: spmd_safe().wrapper().
  spmd_safe: spmd_safe().
  _synchronize_tensors: _synchronize_tensors().
  _F: _F.
  SPMD_SAFE_METADATA_KEY: SPMD_SAFE_METADATA_KEY.
---
# Module: [`src/torch_tpu/_internal/distributed/spmd_util.py`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/spmd_util.py)

## Functions
- <a id="_synchronize_tensors"></a>`_synchronize_tensors(args, kwargs)` — [`L31`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/spmd_util.py#L31)
- <a id="spmd_safe"></a>`spmd_safe(func: _F)` — [`L45`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/spmd_util.py#L45) — Marks a function as SPMD-safe, i.e. run identically on every rank.
- <a id="spmd_safe.wrapper"></a>`wrapper(*args: Any, **kwargs: Any)` — [`L79`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/spmd_util.py#L79)

## Module values
- <a id="SPMD_SAFE_METADATA_KEY"></a>`SPMD_SAFE_METADATA_KEY` — [`L28`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/spmd_util.py#L28)
- <a id="_F"></a>`_F` — [`L26`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/spmd_util.py#L26)

