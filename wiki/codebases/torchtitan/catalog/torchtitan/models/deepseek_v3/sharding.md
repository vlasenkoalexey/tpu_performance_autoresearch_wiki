---
title: 'Module: torchtitan/models/deepseek_v3/sharding.py'
type: catalog
provenance: extracted
module: torchtitan/models/deepseek_v3/sharding.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.models.deepseek_v3.sharding`/
symbols:
  _set_deepseek_v3_layer_sharding: _set_deepseek_v3_layer_sharding().
  _set_deepseek_v3_mtp_sharding: _set_deepseek_v3_mtp_sharding().
  set_deepseek_v3_sharding_config: set_deepseek_v3_sharding_config().
  _GROUPED_EXPERTS_PARAM_LAYOUT._GROUPED_EXPERTS_PARAM_LAYOUT: _GROUPED_EXPERTS_PARAM_LAYOUT._GROUPED_EXPERTS_PARAM_LAYOUT.
---
# Module: [`torchtitan/models/deepseek_v3/sharding.py`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/sharding.py)

## Functions
- <a id="_set_deepseek_v3_layer_sharding"></a>`_set_deepseek_v3_layer_sharding(layer_cfg: DeepSeekV3TransformerBlock.Config, *, enable_sp: bool, enable_ep: bool)` — [`L74`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/sharding.py#L74) — Set sharding on one DeepSeek V3 transformer layer. — documented in [deepseek-v3-model](../../../../concepts/deepseek-v3-model.md)
- <a id="_set_deepseek_v3_mtp_sharding"></a>`_set_deepseek_v3_mtp_sharding(config, *, enable_sp: bool, enable_ep: bool)` — [`L155`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/sharding.py#L155) — documented in [deepseek-v3-model](../../../../concepts/deepseek-v3-model.md)
- <a id="set_deepseek_v3_sharding_config"></a>`set_deepseek_v3_sharding_config(config: DeepSeekV3Model.Config, *, enable_sp: bool, enable_ep: bool)` — [`L44`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/sharding.py#L44) — Fill ``sharding_config`` on all DeepSeek V3 sub-configs. — documented in [deepseek-v3-model](../../../../concepts/deepseek-v3-model.md)

## Module values
- <a id="_GROUPED_EXPERTS_PARAM_LAYOUT._GROUPED_EXPERTS_PARAM_LAYOUT"></a>`_GROUPED_EXPERTS_PARAM_LAYOUT` — [`L37`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/sharding.py#L37)

