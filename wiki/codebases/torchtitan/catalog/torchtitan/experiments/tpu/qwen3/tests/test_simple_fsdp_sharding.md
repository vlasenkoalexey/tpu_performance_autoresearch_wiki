---
title: 'Module: torchtitan/experiments/tpu/qwen3/tests/test_simple_fsdp_sharding.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/qwen3/tests/test_simple_fsdp_sharding.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.qwen3.tests.test_simple_fsdp_sharding`/
symbols:
  _model: _model().
  _parallel_dims: _parallel_dims().
  SimpleFSDPShardingTest.test_plans_an_axis_per_stack_when_layers_are_stacked: SimpleFSDPShardingTest#test_plans_an_axis_per_stack_when_layers_are_stacked().
  SimpleFSDPShardingTest.test_graph_trainer_configures_shard_dims_before_simple_fsdp: SimpleFSDPShardingTest#test_graph_trainer_configures_shard_dims_before_simple_fsdp().
  SimpleFSDPShardingTest.test_uses_hidden_axis_when_leading_axis_is_uneven: SimpleFSDPShardingTest#test_uses_hidden_axis_when_leading_axis_is_uneven().
  SimpleFSDPShardingTest.test_keeps_default_axis_when_leading_axis_is_even: SimpleFSDPShardingTest#test_keeps_default_axis_when_leading_axis_is_even().
  SimpleFSDPShardingTest.test_native_w2_uses_its_tile_aligned_trailing_axis: SimpleFSDPShardingTest#test_native_w2_uses_its_tile_aligned_trailing_axis().
  SimpleFSDPShardingTest.test_finds_experts_beneath_layer_wrappers: SimpleFSDPShardingTest#test_finds_experts_beneath_layer_wrappers().
  SimpleFSDPShardingTest.test_rejects_an_empty_expert_module_when_nothing_is_stacked: SimpleFSDPShardingTest#test_rejects_an_empty_expert_module_when_nothing_is_stacked().
  SimpleFSDPShardingTest.test_rejects_when_hidden_axis_is_not_divisible: SimpleFSDPShardingTest#test_rejects_when_hidden_axis_is_not_divisible().
  SimpleFSDPShardingTest.test_uses_hidden_axis_when_vocabulary_is_uneven: SimpleFSDPShardingTest#test_uses_hidden_axis_when_vocabulary_is_uneven().
  _wrapped_model: _wrapped_model().
  SimpleFSDPShardingTest: SimpleFSDPShardingTest#
---
# Module: [`torchtitan/experiments/tpu/qwen3/tests/test_simple_fsdp_sharding.py`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/tests/test_simple_fsdp_sharding.py)

> **Collapsed catalog** (13 symbols) — one row per symbol with its source line; member detail omitted. See the source link above, or the curated codebase page, for depth.

- <a id="SimpleFSDPShardingTest"></a>`SimpleFSDPShardingTest` — [`L65`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/tests/test_simple_fsdp_sharding.py#L65)
- <a id="SimpleFSDPShardingTest.test_finds_experts_beneath_layer_wrappers"></a>`SimpleFSDPShardingTest.test_finds_experts_beneath_layer_wrappers` — [`L93`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/tests/test_simple_fsdp_sharding.py#L93)
- <a id="SimpleFSDPShardingTest.test_graph_trainer_configures_shard_dims_before_simple_fsdp"></a>`SimpleFSDPShardingTest.test_graph_trainer_configures_shard_dims_before_simple_fsdp` — [`L145`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/tests/test_simple_fsdp_sharding.py#L145)
- <a id="SimpleFSDPShardingTest.test_keeps_default_axis_when_leading_axis_is_even"></a>`SimpleFSDPShardingTest.test_keeps_default_axis_when_leading_axis_is_even` — [`L74`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/tests/test_simple_fsdp_sharding.py#L74)
- <a id="SimpleFSDPShardingTest.test_native_w2_uses_its_tile_aligned_trailing_axis"></a>`SimpleFSDPShardingTest.test_native_w2_uses_its_tile_aligned_trailing_axis` — [`L81`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/tests/test_simple_fsdp_sharding.py#L81)
- <a id="SimpleFSDPShardingTest.test_plans_an_axis_per_stack_when_layers_are_stacked"></a>`SimpleFSDPShardingTest.test_plans_an_axis_per_stack_when_layers_are_stacked` — [`L103`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/tests/test_simple_fsdp_sharding.py#L103)
- <a id="SimpleFSDPShardingTest.test_rejects_an_empty_expert_module_when_nothing_is_stacked"></a>`SimpleFSDPShardingTest.test_rejects_an_empty_expert_module_when_nothing_is_stacked` — [`L124`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/tests/test_simple_fsdp_sharding.py#L124)
- <a id="SimpleFSDPShardingTest.test_rejects_when_hidden_axis_is_not_divisible"></a>`SimpleFSDPShardingTest.test_rejects_when_hidden_axis_is_not_divisible` — [`L131`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/tests/test_simple_fsdp_sharding.py#L131)
- <a id="SimpleFSDPShardingTest.test_uses_hidden_axis_when_leading_axis_is_uneven"></a>`SimpleFSDPShardingTest.test_uses_hidden_axis_when_leading_axis_is_uneven` — [`L67`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/tests/test_simple_fsdp_sharding.py#L67)
- <a id="SimpleFSDPShardingTest.test_uses_hidden_axis_when_vocabulary_is_uneven"></a>`SimpleFSDPShardingTest.test_uses_hidden_axis_when_vocabulary_is_uneven` — [`L137`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/tests/test_simple_fsdp_sharding.py#L137)
- <a id="_model"></a>`_model` — [`L26`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/tests/test_simple_fsdp_sharding.py#L26)
- <a id="_parallel_dims"></a>`_parallel_dims` — [`L53`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/tests/test_simple_fsdp_sharding.py#L53)
- <a id="_wrapped_model"></a>`_wrapped_model` — [`L45`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/tests/test_simple_fsdp_sharding.py#L45)
