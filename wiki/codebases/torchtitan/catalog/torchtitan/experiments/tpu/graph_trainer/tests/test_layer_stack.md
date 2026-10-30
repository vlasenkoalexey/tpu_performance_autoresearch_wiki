---
title: 'Module: torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.graph_trainer.tests.test_layer_stack`/
symbols:
  _build: _build().
  TestQwen3._moe_config_with_global_batch_aux_loss: TestQwen3#_moe_config_with_global_batch_aux_loss().
  _moe_config: _moe_config().
  _toy_layer: _toy_layer().
  _config: _config().
  TOKENS: TOKENS.
  TestQwen3.test_scan_gradients_match_the_loop_with_global_batch_aux_loss: TestQwen3#test_scan_gradients_match_the_loop_with_global_batch_aux_loss().
  TestQwen3._build: TestQwen3#_build().
  TestLayerStack.test_the_body_gathers_in_the_compute_dtype: TestLayerStack#test_the_body_gathers_in_the_compute_dtype().
  TestLayerStack.test_the_optimizer_sees_each_stack_once: TestLayerStack#test_the_optimizer_sees_each_stack_once().
  _toy_layers: _toy_layers().
  TestStackable._moe_model: TestStackable#_moe_model().
  SEQ_LEN: SEQ_LEN.
  TestLayerStack.test_the_body_recomputes_its_gather_in_backward: TestLayerStack#test_the_body_recomputes_its_gather_in_backward().
  TestLayerStack.test_scan_gradients_match_the_loop: TestLayerStack#test_scan_gradients_match_the_loop().
  TestStackable.test_identical_layers_are_stackable: TestStackable#test_identical_layers_are_stackable().
  TestStackable.test_a_differing_parameter_set_names_the_layer_and_the_parameter: TestStackable#test_a_differing_parameter_set_names_the_layer_and_the_parameter().
  TestStackable.test_a_same_named_parameter_shows_what_differs: TestStackable#test_a_same_named_parameter_shows_what_differs().
  TestStackable.test_a_differing_buffer_is_rejected: TestStackable#test_a_differing_buffer_is_rejected().
  TestStackable.test_meta_buffers_are_compared_by_shape_only: TestStackable#test_meta_buffers_are_compared_by_shape_only().
  _layer_loop: _layer_loop().
  TestLayerStack.test_module_tree_is_unchanged: TestLayerStack#test_module_tree_is_unchanged().
  TestLayerStack.test_each_weight_is_a_parameter_exactly_once: TestLayerStack#test_each_weight_is_a_parameter_exactly_once().
  TestLayerStack.test_stacks_are_sharded_off_the_layer_axis: TestLayerStack#test_stacks_are_sharded_off_the_layer_axis().
  TestLayerStack.test_forward_matches_unrolled: TestLayerStack#test_forward_matches_unrolled().
  TestLayerStack.test_scan_forward_matches_the_loop: TestLayerStack#test_scan_forward_matches_the_loop().
  TestLayerStack.test_building_a_scan_refuses_without_the_backward_patch: TestLayerStack#test_building_a_scan_refuses_without_the_backward_patch().
  TestLayerStack.test_loads_an_unrolled_checkpoint: TestLayerStack#test_loads_an_unrolled_checkpoint().
  TestLayerStack.test_plan_shard_dims_prefers_8_row_tile_aligned_axis_for_2d_weights: TestLayerStack#test_plan_shard_dims_prefers_8_row_tile_aligned_axis_for_2d_weights().
  TestStackable.test_moe_layers_are_refused: TestStackable#test_moe_layers_are_refused().
  TestStackable.test_moe_layers_without_load_balancing_are_stackable: TestStackable#test_moe_layers_without_load_balancing_are_stackable().
  TestQwen3.test_scan_forward_matches_the_loop: TestQwen3#test_scan_forward_matches_the_loop().
  TestQwen3._pair: TestQwen3#_pair().
  TestLayerStack.test_state_dict_is_identical: TestLayerStack#test_state_dict_is_identical().
  TestLayerStack.test_init_differs_per_row: TestLayerStack#test_init_differs_per_row().
  TestLayerStack.test_refuses_load_state_dict_with_assign: TestLayerStack#test_refuses_load_state_dict_with_assign().
  TestQwen3.test_layer_weights_are_identical: TestQwen3#test_layer_weights_are_identical().
  SEED: SEED.
  _REAL_ROPE_OVERRIDE: _REAL_ROPE_OVERRIDE.
  _DISCARDED_TOKEN_COUNTER_OVERRIDE: _DISCARDED_TOKEN_COUNTER_OVERRIDE.
  TestLayerStack.not_the_method: TestLayerStack#not_the_method().
  TestLayerStack.capture: TestLayerStack#capture().
  TestLayerStack: TestLayerStack#
  TestLayerStack.setUp: TestLayerStack#setUp().
  TestLayerStack.tearDown: TestLayerStack#tearDown().
  TestStackable: TestStackable#
  TestQwen3: TestQwen3#
  TestQwen3.setUp: TestQwen3#setUp().
  TestQwen3.tearDown: TestQwen3#tearDown().
---
# Module: [`torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack.py`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack.py)

> **Collapsed catalog** (49 symbols) — one row per symbol with its source line; member detail omitted. See the source link above, or the curated codebase page, for depth.

- <a id="SEED"></a>`SEED` — [`L55`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack.py#L55)
- <a id="SEQ_LEN"></a>`SEQ_LEN` — [`L53`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack.py#L53)
- <a id="TOKENS"></a>`TOKENS` — [`L54`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack.py#L54)
- <a id="TestLayerStack"></a>`TestLayerStack` — [`L195`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack.py#L195)
- <a id="TestLayerStack.capture"></a>`TestLayerStack.capture` — [`L337`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack.py#L337)
- <a id="TestLayerStack.not_the_method"></a>`TestLayerStack.not_the_method` — [`L315`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack.py#L315)
- <a id="TestLayerStack.setUp"></a>`TestLayerStack.setUp` — [`L196`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack.py#L196)
- <a id="TestLayerStack.tearDown"></a>`TestLayerStack.tearDown` — [`L208`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack.py#L208)
- <a id="TestLayerStack.test_building_a_scan_refuses_without_the_backward_patch"></a>`TestLayerStack.test_building_a_scan_refuses_without_the_backward_patch` — [`L311`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack.py#L311)
- <a id="TestLayerStack.test_each_weight_is_a_parameter_exactly_once"></a>`TestLayerStack.test_each_weight_is_a_parameter_exactly_once` — [`L258`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack.py#L258)
- <a id="TestLayerStack.test_forward_matches_unrolled"></a>`TestLayerStack.test_forward_matches_unrolled` — [`L291`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack.py#L291)
- <a id="TestLayerStack.test_init_differs_per_row"></a>`TestLayerStack.test_init_differs_per_row` — [`L226`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack.py#L226)
- <a id="TestLayerStack.test_loads_an_unrolled_checkpoint"></a>`TestLayerStack.test_loads_an_unrolled_checkpoint` — [`L445`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack.py#L445)
- <a id="TestLayerStack.test_module_tree_is_unchanged"></a>`TestLayerStack.test_module_tree_is_unchanged` — [`L244`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack.py#L244)
- <a id="TestLayerStack.test_plan_shard_dims_prefers_8_row_tile_aligned_axis_for_2d_weights"></a>`TestLayerStack.test_plan_shard_dims_prefers_8_row_tile_aligned_axis_for_2d_weights` — [`L473`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack.py#L473)
- <a id="TestLayerStack.test_refuses_load_state_dict_with_assign"></a>`TestLayerStack.test_refuses_load_state_dict_with_assign` — [`L460`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack.py#L460)
- <a id="TestLayerStack.test_scan_forward_matches_the_loop"></a>`TestLayerStack.test_scan_forward_matches_the_loop` — [`L300`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack.py#L300)
- <a id="TestLayerStack.test_scan_gradients_match_the_loop"></a>`TestLayerStack.test_scan_gradients_match_the_loop` — [`L359`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack.py#L359)
- <a id="TestLayerStack.test_stacks_are_sharded_off_the_layer_axis"></a>`TestLayerStack.test_stacks_are_sharded_off_the_layer_axis` — [`L281`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack.py#L281)
- <a id="TestLayerStack.test_state_dict_is_identical"></a>`TestLayerStack.test_state_dict_is_identical` — [`L212`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack.py#L212)
- <a id="TestLayerStack.test_the_body_gathers_in_the_compute_dtype"></a>`TestLayerStack.test_the_body_gathers_in_the_compute_dtype` — [`L387`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack.py#L387)
- <a id="TestLayerStack.test_the_body_recomputes_its_gather_in_backward"></a>`TestLayerStack.test_the_body_recomputes_its_gather_in_backward` — [`L324`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack.py#L324)
- <a id="TestLayerStack.test_the_optimizer_sees_each_stack_once"></a>`TestLayerStack.test_the_optimizer_sees_each_stack_once` — [`L419`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack.py#L419)
- <a id="TestQwen3"></a>`TestQwen3` — [`L609`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack.py#L609)
- <a id="TestQwen3._build"></a>`TestQwen3._build` — [`L637`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack.py#L637)
- <a id="TestQwen3._moe_config_with_global_batch_aux_loss"></a>`TestQwen3._moe_config_with_global_batch_aux_loss` — [`L686`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack.py#L686)
- <a id="TestQwen3._pair"></a>`TestQwen3._pair` — [`L653`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack.py#L653)
- <a id="TestQwen3.setUp"></a>`TestQwen3.setUp` — [`L619`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack.py#L619)
- <a id="TestQwen3.tearDown"></a>`TestQwen3.tearDown` — [`L633`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack.py#L633)
- <a id="TestQwen3.test_layer_weights_are_identical"></a>`TestQwen3.test_layer_weights_are_identical` — [`L660`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack.py#L660)
- <a id="TestQwen3.test_scan_forward_matches_the_loop"></a>`TestQwen3.test_scan_forward_matches_the_loop` — [`L676`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack.py#L676)
- <a id="TestQwen3.test_scan_gradients_match_the_loop_with_global_batch_aux_loss"></a>`TestQwen3.test_scan_gradients_match_the_loop_with_global_batch_aux_loss` — [`L707`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack.py#L707)
- <a id="TestStackable"></a>`TestStackable` — [`L521`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack.py#L521)
- <a id="TestStackable._moe_model"></a>`TestStackable._moe_model` — [`L589`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack.py#L589)
- <a id="TestStackable.test_a_differing_buffer_is_rejected"></a>`TestStackable.test_a_differing_buffer_is_rejected` — [`L568`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack.py#L568)
- <a id="TestStackable.test_a_differing_parameter_set_names_the_layer_and_the_parameter"></a>`TestStackable.test_a_differing_parameter_set_names_the_layer_and_the_parameter` — [`L535`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack.py#L535)
- <a id="TestStackable.test_a_same_named_parameter_shows_what_differs"></a>`TestStackable.test_a_same_named_parameter_shows_what_differs` — [`L550`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack.py#L550)
- <a id="TestStackable.test_identical_layers_are_stackable"></a>`TestStackable.test_identical_layers_are_stackable` — [`L529`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack.py#L529)
- <a id="TestStackable.test_meta_buffers_are_compared_by_shape_only"></a>`TestStackable.test_meta_buffers_are_compared_by_shape_only` — [`L582`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack.py#L582)
- <a id="TestStackable.test_moe_layers_are_refused"></a>`TestStackable.test_moe_layers_are_refused` — [`L596`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack.py#L596)
- <a id="TestStackable.test_moe_layers_without_load_balancing_are_stackable"></a>`TestStackable.test_moe_layers_without_load_balancing_are_stackable` — [`L602`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack.py#L602)
- <a id="_DISCARDED_TOKEN_COUNTER_OVERRIDE"></a>`_DISCARDED_TOKEN_COUNTER_OVERRIDE` — [`L66`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack.py#L66)
- <a id="_REAL_ROPE_OVERRIDE"></a>`_REAL_ROPE_OVERRIDE` — [`L62`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack.py#L62)
- <a id="_build"></a>`_build` — [`L124`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack.py#L124)
- <a id="_config"></a>`_config` — [`L77`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack.py#L77)
- <a id="_layer_loop"></a>`_layer_loop` — [`L72`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack.py#L72)
- <a id="_moe_config"></a>`_moe_config` — [`L94`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack.py#L94)
- <a id="_toy_layer"></a>`_toy_layer` — [`L506`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack.py#L506)
- <a id="_toy_layers"></a>`_toy_layers` — [`L517`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack.py#L517)
