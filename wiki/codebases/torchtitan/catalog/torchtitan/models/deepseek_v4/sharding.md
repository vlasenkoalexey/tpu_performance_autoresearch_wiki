---
title: 'Module: torchtitan/models/deepseek_v4/sharding.py'
type: catalog
provenance: extracted
module: torchtitan/models/deepseek_v4/sharding.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.models.deepseek_v4.sharding`/
symbols:
  set_deepseek_v4_layer_sharding: set_deepseek_v4_layer_sharding().
  set_deepseek_v4_sharding_config: set_deepseek_v4_sharding_config().
  set_deepseek_v4_attention_sharding: set_deepseek_v4_attention_sharding().
  set_dsa_flex_attention_sharding: set_dsa_flex_attention_sharding().
  _replicate_weight: _replicate_weight.
  _dense_param_rep: _dense_param_rep.
  set_indexer_sharding: set_indexer_sharding().
  set_compressor_sharding: set_compressor_sharding().
  _attn_sink_placement: _attn_sink_placement.
  hc_head_input_sequence_parallel_placement: hc_head_input_sequence_parallel_placement().
  DP: DP.
  CP: CP.
  TP: TP.
  _replicated_layout: _replicated_layout.
  hc_mix_sequence_parallel_placement: hc_mix_sequence_parallel_placement().
  _act_shard0_tp_rep: _act_shard0_tp_rep.
  _GROUPED_EXPERTS_PARAM_LAYOUT._GROUPED_EXPERTS_PARAM_LAYOUT: _GROUPED_EXPERTS_PARAM_LAYOUT._GROUPED_EXPERTS_PARAM_LAYOUT.
---
# Module: [`torchtitan/models/deepseek_v4/sharding.py`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/sharding.py)

## Functions
- <a id="hc_head_input_sequence_parallel_placement"></a>`hc_head_input_sequence_parallel_placement()` — [`L54`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/sharding.py#L54)
- <a id="hc_mix_sequence_parallel_placement"></a>`hc_mix_sequence_parallel_placement()` — [`L65`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/sharding.py#L65)
- <a id="set_compressor_sharding"></a>`set_compressor_sharding(compressor_cfg)` — [`L178`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/sharding.py#L178)
- <a id="set_deepseek_v4_attention_sharding"></a>`set_deepseek_v4_attention_sharding(attention_cfg, *, enable_sp)` — [`L131`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/sharding.py#L131) — documented in [deepseek-v4-model](../../../../concepts/deepseek-v4-model.md)
- <a id="set_deepseek_v4_layer_sharding"></a>`set_deepseek_v4_layer_sharding(layer_cfg: DeepSeekV4TransformerBlock.Config, *, enable_sp: bool, enable_ep: bool)` — [`L214`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/sharding.py#L214) — documented in [deepseek-v4-model](../../../../concepts/deepseek-v4-model.md)
- <a id="set_deepseek_v4_sharding_config"></a>`set_deepseek_v4_sharding_config(config: DeepSeekV4Model.Config, *, enable_sp: bool, enable_ep: bool)` — [`L308`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/sharding.py#L308) — documented in [deepseek-v4-model](../../../../concepts/deepseek-v4-model.md)
- <a id="set_dsa_flex_attention_sharding"></a>`set_dsa_flex_attention_sharding(inner_attention_cfg)` — [`L76`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/sharding.py#L76) — documented in [deepseek-v4-model](../../../../concepts/deepseek-v4-model.md)
- <a id="set_indexer_sharding"></a>`set_indexer_sharding(indexer_cfg)` — [`L190`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/sharding.py#L190)

## Module values
- <a id="CP"></a>`CP` — [`L32`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/sharding.py#L32)
- <a id="DP"></a>`DP` — [`L31`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/sharding.py#L31)
- <a id="TP"></a>`TP` — [`L33`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/sharding.py#L33)
- <a id="_GROUPED_EXPERTS_PARAM_LAYOUT._GROUPED_EXPERTS_PARAM_LAYOUT"></a>`_GROUPED_EXPERTS_PARAM_LAYOUT` — [`L43`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/sharding.py#L43)
- <a id="_act_shard0_tp_rep"></a>`_act_shard0_tp_rep` — [`L29`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/sharding.py#L29)
- <a id="_attn_sink_placement"></a>`_attn_sink_placement` — [`L30`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/sharding.py#L30)
- <a id="_dense_param_rep"></a>`_dense_param_rep` — [`L28`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/sharding.py#L28)
- <a id="_replicate_weight"></a>`_replicate_weight` — [`L49`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/sharding.py#L49)
- <a id="_replicated_layout"></a>`_replicated_layout` — [`L34`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/sharding.py#L34) — documented in [deepseek-v4-model](../../../../concepts/deepseek-v4-model.md)

