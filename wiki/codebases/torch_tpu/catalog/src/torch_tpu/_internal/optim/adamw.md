---
title: 'Module: src/torch_tpu/_internal/optim/adamw.py'
type: catalog
provenance: extracted
module: src/torch_tpu/_internal/optim/adamw.py
status: fresh
symbol_base: scip-python python torch_tpu 0.0.0 `src.torch_tpu._internal.optim.adamw`/AdamW#
symbols:
  AdamW.step: step().
  AdamW.__init__: __init__().
  AdamW: ''
  AdamW._eager_init_state: _eager_init_state().
  AdamW._my_init_group: _my_init_group().
---
# Module: [`src/torch_tpu/_internal/optim/adamw.py`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optim/adamw.py)

## Classes
### <a id="AdamW"></a>`AdamW`
- def: [`src/torch_tpu/_internal/optim/adamw.py:26`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optim/adamw.py#L26)
- doc: A TPU-friendly AdamW optimizer.
- signature: `class AdamW(torch.optim.AdamW):`
- members:
  - <a id="AdamW.step"></a>`step(self, closure=None)` — [`L172`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optim/adamw.py#L172)
- protocol/private: <a id="AdamW.__init__"></a>`__init__`[`L48`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optim/adamw.py#L48), <a id="AdamW._eager_init_state"></a>`_eager_init_state`[`L52`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optim/adamw.py#L52), <a id="AdamW._my_init_group"></a>`_my_init_group`[`L90`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optim/adamw.py#L90)
- uses (calls/refs, reference-scoped): [`use_grad_for_differentiable`](patch.md#use_grad_for_differentiable)
- used by: [`AdamW`](__init__.md#AdamW)

