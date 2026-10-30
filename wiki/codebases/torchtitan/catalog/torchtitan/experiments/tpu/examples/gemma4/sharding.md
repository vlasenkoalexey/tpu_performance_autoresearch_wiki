---
title: 'Module: torchtitan/experiments/tpu/examples/gemma4/sharding.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/examples/gemma4/sharding.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.examples.gemma4.sharding`/
symbols:
  _set_gemma4_layer_sharding: _set_gemma4_layer_sharding().
  set_gemma4_sharding_config: set_gemma4_sharding_config().
  _GROUPED_EXPERTS_PARAM_LAYOUT._GROUPED_EXPERTS_PARAM_LAYOUT: _GROUPED_EXPERTS_PARAM_LAYOUT._GROUPED_EXPERTS_PARAM_LAYOUT.
---
# Module: [`torchtitan/experiments/tpu/examples/gemma4/sharding.py`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/sharding.py)

## Functions
- <a id="_set_gemma4_layer_sharding"></a>`_set_gemma4_layer_sharding(layer_cfg: Gemma4TransformerBlock.Config, *, enable_sp: bool, enable_ep: bool)` — [`L51`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/sharding.py#L51) — Set sharding on one Gemma4 transformer layer.
- <a id="set_gemma4_sharding_config"></a>`set_gemma4_sharding_config(config: Gemma4Model.Config, *, enable_sp: bool, enable_ep: bool)` — [`L37`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/sharding.py#L37) — Fill ``sharding_config`` on all Gemma4 sub-configs.

## Module values
- <a id="_GROUPED_EXPERTS_PARAM_LAYOUT._GROUPED_EXPERTS_PARAM_LAYOUT"></a>`_GROUPED_EXPERTS_PARAM_LAYOUT` — [`L30`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/sharding.py#L30)

