---
title: 'Module: torchtitan/config/transform/base.py'
type: catalog
provenance: extracted
module: torchtitan/config/transform/base.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.config.transform.base`/
symbols:
  ModelConfigTransform: ModelConfigTransform#
  ModelConfigTransform.transform: ModelConfigTransform#transform().
  convert_config_type: convert_config_type().
  ModelConfigTransform.run_after: ModelConfigTransform#run_after.
  ModelConfigTransform.conflicts_with: ModelConfigTransform#conflicts_with.
  __all__: __all__.
---
# Module: [`torchtitan/config/transform/base.py`](../../../../../../../raw/code/torchtitan/torchtitan/config/transform/base.py)

## Classes
### <a id="ModelConfigTransform"></a>`ModelConfigTransform`  ·  implements/extends ABC
- def: [`torchtitan/config/transform/base.py:18`](../../../../../../../raw/code/torchtitan/torchtitan/config/transform/base.py#L18)
- doc: A feature that rewrites a completed model config tree.
- signature: `class ModelConfigTransform(ABC):`
- members:
  - <a id="ModelConfigTransform.transform"></a>`transform(self, model: Module.Config)` — [`L29`](../../../../../../../raw/code/torchtitan/torchtitan/config/transform/base.py#L29) — Rewrite ``model`` and return its root.
  - <a id="ModelConfigTransform.conflicts_with"></a>`conflicts_with` — [`L26`](../../../../../../../raw/code/torchtitan/torchtitan/config/transform/base.py#L26)
  - <a id="ModelConfigTransform.run_after"></a>`run_after` — [`L25`](../../../../../../../raw/code/torchtitan/torchtitan/config/transform/base.py#L25)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`Config`](../../protocols/module.md#Module.Config), [`ContextParallelTransform`](context_parallel.md#ContextParallelTransform), [`transform`](context_parallel.md#ContextParallelTransform.transform)
- used by: [`apply_transforms`](apply.md#apply_transforms), [`ContextParallelTransform`](context_parallel.md#ContextParallelTransform), [`transform_model_config_`](apply.md#transform_model_config_), [`_ordered`](apply.md#_ordered), [`_reject_conflicts`](apply.md#_reject_conflicts)

## Functions
- <a id="convert_config_type"></a>`convert_config_type(existing: Module.Config, replacement: type[Module])` — [`L37`](../../../../../../../raw/code/torchtitan/torchtitan/config/transform/base.py#L37) — Build ``replacement``'s config from ``existing``, keeping its fields.

## Module values
- <a id="__all__"></a>`__all__` — [`L15`](../../../../../../../raw/code/torchtitan/torchtitan/config/transform/base.py#L15)

