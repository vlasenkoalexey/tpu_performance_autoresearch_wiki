---
title: 'Module: torchtitan/config/transform/apply.py'
type: catalog
provenance: extracted
module: torchtitan/config/transform/apply.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.config.transform.apply`/
symbols:
  apply_transforms: apply_transforms().
  transform_model_config_: transform_model_config_().
  _ordered: _ordered().
  _reject_conflicts: _reject_conflicts().
  __all__: __all__.
---
# Module: [`torchtitan/config/transform/apply.py`](../../../../../../../raw/code/torchtitan/torchtitan/config/transform/apply.py)

## Functions
- <a id="_ordered"></a>`_ordered(transforms: list[ModelConfigTransform])` — [`L23`](../../../../../../../raw/code/torchtitan/torchtitan/config/transform/apply.py#L23) — Stable-sort transforms by their ``run_after`` declarations.
- <a id="_reject_conflicts"></a>`_reject_conflicts(transforms: list[ModelConfigTransform])` — [`L49`](../../../../../../../raw/code/torchtitan/torchtitan/config/transform/apply.py#L49)
- <a id="apply_transforms"></a>`apply_transforms(config: Trainer.Config, transforms: list[ModelConfigTransform])` — [`L76`](../../../../../../../raw/code/torchtitan/torchtitan/config/transform/apply.py#L76) — Apply every transform to a copy of ``config`` and return it. — documented in [job-config](../../../../concepts/job-config.md)
- <a id="transform_model_config_"></a>`transform_model_config_(model: Module.Config, transforms: list[ModelConfigTransform])` — [`L61`](../../../../../../../raw/code/torchtitan/torchtitan/config/transform/apply.py#L61) — Apply every transform to ``model`` and return the rewritten root.

## Module values
- <a id="__all__"></a>`__all__` — [`L20`](../../../../../../../raw/code/torchtitan/torchtitan/config/transform/apply.py#L20)

