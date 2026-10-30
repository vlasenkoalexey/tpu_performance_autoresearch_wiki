---
title: 'Module: torchtitan/models/qwen3/sharding.py'
type: catalog
provenance: extracted
module: torchtitan/models/qwen3/sharding.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.models.qwen3.sharding`/
symbols:
  _set_qwen3_layer_sharding: _set_qwen3_layer_sharding().
  set_qwen3_sharding_config: set_qwen3_sharding_config().
  _GROUPED_EXPERTS_PARAM_LAYOUT._GROUPED_EXPERTS_PARAM_LAYOUT: _GROUPED_EXPERTS_PARAM_LAYOUT._GROUPED_EXPERTS_PARAM_LAYOUT.
---
# Module: [`torchtitan/models/qwen3/sharding.py`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3/sharding.py)

## Functions
- <a id="_set_qwen3_layer_sharding"></a>`_set_qwen3_layer_sharding(layer_cfg: Qwen3TransformerBlock.Config, *, enable_sp: bool, enable_ep: bool)` — [`L60`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3/sharding.py#L60) — Set sharding on one Qwen3 transformer layer. — documented in [qwen3-model](../../../../concepts/qwen3-model.md)
- <a id="set_qwen3_sharding_config"></a>`set_qwen3_sharding_config(config: Qwen3Model.Config, *, enable_sp: bool, enable_ep: bool)` — [`L38`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3/sharding.py#L38) — Fill ``sharding_config`` on all Qwen3 sub-configs. — documented in [qwen3-model](../../../../concepts/qwen3-model.md)

## Module values
- <a id="_GROUPED_EXPERTS_PARAM_LAYOUT._GROUPED_EXPERTS_PARAM_LAYOUT"></a>`_GROUPED_EXPERTS_PARAM_LAYOUT` — [`L31`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3/sharding.py#L31)

