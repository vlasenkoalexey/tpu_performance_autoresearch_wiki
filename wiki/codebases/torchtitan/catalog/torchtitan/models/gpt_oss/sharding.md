---
title: 'Module: torchtitan/models/gpt_oss/sharding.py'
type: catalog
provenance: extracted
module: torchtitan/models/gpt_oss/sharding.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.models.gpt_oss.sharding`/
symbols:
  _set_gpt_oss_layer_sharding: _set_gpt_oss_layer_sharding().
  scaled_bias_rowwise_config: scaled_bias_rowwise_config().
  set_gpt_oss_sharding_config: set_gpt_oss_sharding_config().
  _GPT_OSS_EXPERTS_PARAM_LAYOUT._GPT_OSS_EXPERTS_PARAM_LAYOUT: _GPT_OSS_EXPERTS_PARAM_LAYOUT._GPT_OSS_EXPERTS_PARAM_LAYOUT.
---
# Module: [`torchtitan/models/gpt_oss/sharding.py`](../../../../../../../raw/code/torchtitan/torchtitan/models/gpt_oss/sharding.py)

## Functions
- <a id="_set_gpt_oss_layer_sharding"></a>`_set_gpt_oss_layer_sharding(layer_cfg: GptOssTransformerBlock.Config, *, enable_sp: bool, enable_ep: bool)` — [`L78`](../../../../../../../raw/code/torchtitan/torchtitan/models/gpt_oss/sharding.py#L78) — Set sharding on one GPT-OSS transformer layer. — documented in [gpt-oss-model](../../../../concepts/gpt-oss-model.md)
- <a id="scaled_bias_rowwise_config"></a>`scaled_bias_rowwise_config(*, output_sp: bool)` — [`L38`](../../../../../../../raw/code/torchtitan/torchtitan/models/gpt_oss/sharding.py#L38) — documented in [gpt-oss-model](../../../../concepts/gpt-oss-model.md)
- <a id="set_gpt_oss_sharding_config"></a>`set_gpt_oss_sharding_config(config: GptOssModel.Config, *, enable_sp: bool, enable_ep: bool)` — [`L58`](../../../../../../../raw/code/torchtitan/torchtitan/models/gpt_oss/sharding.py#L58) — Fill ``sharding_config`` on all GPT-OSS sub-configs. — documented in [gpt-oss-model](../../../../concepts/gpt-oss-model.md)

## Module values
- <a id="_GPT_OSS_EXPERTS_PARAM_LAYOUT._GPT_OSS_EXPERTS_PARAM_LAYOUT"></a>`_GPT_OSS_EXPERTS_PARAM_LAYOUT` — [`L30`](../../../../../../../raw/code/torchtitan/torchtitan/models/gpt_oss/sharding.py#L30)

