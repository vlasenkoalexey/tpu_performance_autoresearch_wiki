---
title: 'Module: src/torch_tpu/_internal/optim/patch.py'
type: catalog
provenance: extracted
module: src/torch_tpu/_internal/optim/patch.py
status: fresh
symbol_base: scip-python python torch_tpu 0.0.0 `src.torch_tpu._internal.optim.patch`/
symbols:
  patch_optimizer_graph_breaks: patch_optimizer_graph_breaks().
  _patch_closure_chain: _patch_closure_chain().
  unpatch_optimizer_graph_breaks: unpatch_optimizer_graph_breaks().
  _original_use_grad_for_differentiable: _original_use_grad_for_differentiable.
  use_grad_for_differentiable: use_grad_for_differentiable().
  patch_optimizer_graph_breaks.get_all_subclasses: patch_optimizer_graph_breaks().get_all_subclasses().
  _original_class_steps: _original_class_steps.
  _closure_restorations: _closure_restorations.
  _get_wrapped_function: _get_wrapped_function().
  use_grad_for_differentiable.wrapper: use_grad_for_differentiable().wrapper().
---
# Module: [`src/torch_tpu/_internal/optim/patch.py`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optim/patch.py)

## Functions
- <a id="_get_wrapped_function"></a>`_get_wrapped_function(use_grad_fn)` — [`L53`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optim/patch.py#L53) — Retrieves the immediate function wrapped by the _use_grad decorator.
- <a id="_patch_closure_chain"></a>`_patch_closure_chain(method, patched_decorator_fn)` — [`L66`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optim/patch.py#L66) — Recursively traverses closure cells to find and replace _use_grad wrapper.
- <a id="patch_optimizer_graph_breaks.get_all_subclasses"></a>`get_all_subclasses(cls)` — [`L129`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optim/patch.py#L129)
- <a id="patch_optimizer_graph_breaks"></a>`patch_optimizer_graph_breaks()` — [`L112`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optim/patch.py#L112) — Monkey-patches PyTorch optimizers to avoid graph breaks.
- <a id="unpatch_optimizer_graph_breaks"></a>`unpatch_optimizer_graph_breaks()` — [`L170`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optim/patch.py#L170) — Restores the original PyTorch optimizer decorator and class methods.
- <a id="use_grad_for_differentiable"></a>`use_grad_for_differentiable(func)` — [`L27`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optim/patch.py#L27) — A safe decorator for step() that replaces _use_grad_for_differentiable.
- <a id="use_grad_for_differentiable.wrapper"></a>`wrapper(*args, **kwargs)` — [`L40`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optim/patch.py#L40)

## Module values
- <a id="_closure_restorations"></a>`_closure_restorations` — [`L24`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optim/patch.py#L24)
- <a id="_original_class_steps"></a>`_original_class_steps` — [`L23`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optim/patch.py#L23)
- <a id="_original_use_grad_for_differentiable"></a>`_original_use_grad_for_differentiable` — [`L22`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optim/patch.py#L22)

