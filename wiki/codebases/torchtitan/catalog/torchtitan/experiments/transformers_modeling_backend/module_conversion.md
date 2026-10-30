---
title: 'Module: torchtitan/experiments/transformers_modeling_backend/module_conversion.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/transformers_modeling_backend/module_conversion.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.transformers_modeling_backend.module_conversion`/
symbols:
  convert_hf_to_module: convert_hf_to_module().
  _make_module_class: _make_module_class().
  _module_class_cache._module_class_cache: _module_class_cache._module_class_cache.
---
# Module: [`torchtitan/experiments/transformers_modeling_backend/module_conversion.py`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/module_conversion.py)

## Functions
- <a id="_make_module_class"></a>`_make_module_class(nn_cls: type)` — [`L29`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/module_conversion.py#L29) — Create a class inheriting from both Module and nn_cls.
- <a id="convert_hf_to_module"></a>`convert_hf_to_module(model: nn.Module)` — [`L42`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/module_conversion.py#L42) — Convert all plain nn.Module children to Module protocol instances.

## Module values
- <a id="_module_class_cache._module_class_cache"></a>`_module_class_cache` — [`L26`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/module_conversion.py#L26)

