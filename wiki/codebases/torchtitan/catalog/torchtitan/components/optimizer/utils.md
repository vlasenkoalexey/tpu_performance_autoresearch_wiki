---
title: 'Module: torchtitan/components/optimizer/utils.py'
type: catalog
provenance: extracted
module: torchtitan/components/optimizer/utils.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.components.optimizer.utils`/
symbols:
  get_flat_optim_state_dict: get_flat_optim_state_dict().
  init_optim_state: init_optim_state().
  load_flat_optim_state_dict: load_flat_optim_state_dict().
  _flatten_state_nested: _flatten_state_nested().
  _unflatten_optim_state_dict: _unflatten_optim_state_dict().
  _optim_state_dict_to_fqn_keys: _optim_state_dict_to_fqn_keys().
  _reconstruct_nested: _reconstruct_nested().
  __all__: __all__.
---
# Module: [`torchtitan/components/optimizer/utils.py`](../../../../../../../raw/code/torchtitan/torchtitan/components/optimizer/utils.py)

## Functions
- <a id="_flatten_state_nested"></a>`_flatten_state_nested(state: dict[str, Any], prefix: str, out: dict[str, Any])` — [`L208`](../../../../../../../raw/code/torchtitan/torchtitan/components/optimizer/utils.py#L208) — Flatten a (possibly nested) per-param state dict into dotted keys. — documented in [optimizers-and-lr-schedulers](../../../../concepts/optimizers-and-lr-schedulers.md)
- <a id="_optim_state_dict_to_fqn_keys"></a>`_optim_state_dict_to_fqn_keys(optim_sd: dict[str, Any])` — [`L123`](../../../../../../../raw/code/torchtitan/torchtitan/components/optimizer/utils.py#L123) — Re-key an optimizer state dict from integer param ids to FQNs.
- <a id="_reconstruct_nested"></a>`_reconstruct_nested(flat_sd: dict[str, Any], prefix: str)` — [`L220`](../../../../../../../raw/code/torchtitan/torchtitan/components/optimizer/utils.py#L220) — Rebuild the nested dict stored under ``prefix`` in a flat state dict.
- <a id="_unflatten_optim_state_dict"></a>`_unflatten_optim_state_dict(optim: torch.optim.Optimizer, flat_sd: dict[str, Any])` — [`L157`](../../../../../../../raw/code/torchtitan/torchtitan/components/optimizer/utils.py#L157) — Rebuild an integer-keyed optimizer state dict from a flat, FQN-keyed one.
- <a id="get_flat_optim_state_dict"></a>`get_flat_optim_state_dict(optim: torch.optim.Optimizer)` — [`L88`](../../../../../../../raw/code/torchtitan/torchtitan/components/optimizer/utils.py#L88) — Return a flat, FQN-keyed optimizer state dict ready for DCP. — documented in [optimizers-and-lr-schedulers](../../../../concepts/optimizers-and-lr-schedulers.md)
- <a id="init_optim_state"></a>`init_optim_state(optim: torch.optim.Optimizer)` — [`L29`](../../../../../../../raw/code/torchtitan/torchtitan/components/optimizer/utils.py#L29) — Materialize optimizer state by running one zero-gradient, zero-lr step. — documented in [optimizers-and-lr-schedulers](../../../../concepts/optimizers-and-lr-schedulers.md)
- <a id="load_flat_optim_state_dict"></a>`load_flat_optim_state_dict(optim: torch.optim.Optimizer, flat_sd: dict[str, Any])` — [`L110`](../../../../../../../raw/code/torchtitan/torchtitan/components/optimizer/utils.py#L110) — Load a flat, FQN-keyed optimizer state dict into ``optim``. — documented in [optimizers-and-lr-schedulers](../../../../concepts/optimizers-and-lr-schedulers.md)

## Module values
- <a id="__all__"></a>`__all__` — [`L22`](../../../../../../../raw/code/torchtitan/torchtitan/components/optimizer/utils.py#L22)

