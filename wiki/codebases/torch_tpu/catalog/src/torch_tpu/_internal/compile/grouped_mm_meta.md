---
title: 'Module: src/torch_tpu/_internal/compile/grouped_mm_meta.py'
type: catalog
provenance: extracted
module: src/torch_tpu/_internal/compile/grouped_mm_meta.py
status: fresh
symbol_base: scip-python python torch_tpu 0.0.0 `src.torch_tpu._internal.compile.grouped_mm_meta`/
symbols:
  _check: _check().
  _name: _name().
  _tpu_grouped_mm_meta: _tpu_grouped_mm_meta().
  register: register().
  register._grouped_mm_meta: register()._grouped_mm_meta().
  _meta_lib._meta_lib: _meta_lib._meta_lib.
---
# Module: [`src/torch_tpu/_internal/compile/grouped_mm_meta.py`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/grouped_mm_meta.py)

## Functions
- <a id="_check"></a>`_check(cond: bool | torch.SymBool, msg: str)` — [`L31`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/grouped_mm_meta.py#L31)
- <a id="register._grouped_mm_meta"></a>`_grouped_mm_meta(self: torch.Tensor, mat2: torch.Tensor, offs: torch.Tensor | None = None, bias: torch.Tensor | None = None, out_dtype: torch.dtype | None = None)` — [`L149`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/grouped_mm_meta.py#L149)
- <a id="_name"></a>`_name(dtype: torch.dtype)` — [`L36`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/grouped_mm_meta.py#L36)
- <a id="_tpu_grouped_mm_meta"></a>`_tpu_grouped_mm_meta(self: torch.Tensor, mat2: torch.Tensor, offs: torch.Tensor | None, bias: torch.Tensor | None, out_dtype: torch.dtype | None)` — [`L40`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/grouped_mm_meta.py#L40) — Validates inputs like the TPU eager kernel; returns a contiguous output.
- <a id="register"></a>`register()` — [`L131`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/grouped_mm_meta.py#L131) — Replaces the `aten._grouped_mm.default` Meta kernel for TPU tensors.

## Module values
- <a id="_meta_lib._meta_lib"></a>`_meta_lib` — [`L28`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/grouped_mm_meta.py#L28)

