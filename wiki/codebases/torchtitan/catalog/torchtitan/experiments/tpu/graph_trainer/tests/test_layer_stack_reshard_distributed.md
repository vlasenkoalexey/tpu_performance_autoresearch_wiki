---
title: 'Module: torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack_reshard_distributed.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack_reshard_distributed.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.graph_trainer.tests.test_layer_stack_reshard_distributed`/
symbols:
  _build: _build().
  _flattened_moe_optim_state: _flattened_moe_optim_state().
  OptimizerStateTest.test_the_optimizer_state_is_keyed_the_same_way_in_both_layouts: OptimizerStateTest#test_the_optimizer_state_is_keyed_the_same_way_in_both_layouts().
  ReshardTest._round_trip: ReshardTest#_round_trip().
  _save_worker: _save_worker().
  _load_worker: _load_worker().
  FlattenedOptimizerStateTest.test_loading_across_the_flatten_boundary_raises: FlattenedOptimizerStateTest#test_loading_across_the_flatten_boundary_raises().
  _layer_loop: _layer_loop().
  _save_flattened_optim_worker: _save_flattened_optim_worker().
  _load_flattened_optim_worker: _load_flattened_optim_worker().
  _process_group: _process_group().
  _free_port: _free_port().
  ReshardTest.test_stacked_to_stacked: ReshardTest#test_stacked_to_stacked().
  ReshardTest.test_stacked_to_unrolled: ReshardTest#test_stacked_to_unrolled().
  ReshardTest.test_unrolled_to_stacked: ReshardTest#test_unrolled_to_stacked().
  _gathered: _gathered().
  SEED: SEED.
  ReshardTest: ReshardTest#
  OptimizerStateTest: OptimizerStateTest#
  FlattenedOptimizerStateTest: FlattenedOptimizerStateTest#
---
# Module: [`torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack_reshard_distributed.py`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack_reshard_distributed.py)

> **Collapsed catalog** (20 symbols) — one row per symbol with its source line; member detail omitted. See the source link above, or the curated codebase page, for depth.

- <a id="FlattenedOptimizerStateTest"></a>`FlattenedOptimizerStateTest` — [`L262`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack_reshard_distributed.py#L262)
- <a id="FlattenedOptimizerStateTest.test_loading_across_the_flatten_boundary_raises"></a>`FlattenedOptimizerStateTest.test_loading_across_the_flatten_boundary_raises` — [`L274`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack_reshard_distributed.py#L274)
- <a id="OptimizerStateTest"></a>`OptimizerStateTest` — [`L216`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack_reshard_distributed.py#L216)
- <a id="OptimizerStateTest.test_the_optimizer_state_is_keyed_the_same_way_in_both_layouts"></a>`OptimizerStateTest.test_the_optimizer_state_is_keyed_the_same_way_in_both_layouts` — [`L249`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack_reshard_distributed.py#L249)
- <a id="ReshardTest"></a>`ReshardTest` — [`L192`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack_reshard_distributed.py#L192)
- <a id="ReshardTest._round_trip"></a>`ReshardTest._round_trip` — [`L195`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack_reshard_distributed.py#L195)
- <a id="ReshardTest.test_stacked_to_stacked"></a>`ReshardTest.test_stacked_to_stacked` — [`L204`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack_reshard_distributed.py#L204)
- <a id="ReshardTest.test_stacked_to_unrolled"></a>`ReshardTest.test_stacked_to_unrolled` — [`L207`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack_reshard_distributed.py#L207)
- <a id="ReshardTest.test_unrolled_to_stacked"></a>`ReshardTest.test_unrolled_to_stacked` — [`L211`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack_reshard_distributed.py#L211)
- <a id="SEED"></a>`SEED` — [`L44`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack_reshard_distributed.py#L44)
- <a id="_build"></a>`_build` — [`L52`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack_reshard_distributed.py#L52)
- <a id="_flattened_moe_optim_state"></a>`_flattened_moe_optim_state` — [`L151`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack_reshard_distributed.py#L151)
- <a id="_free_port"></a>`_free_port` — [`L145`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack_reshard_distributed.py#L145)
- <a id="_gathered"></a>`_gathered` — [`L93`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack_reshard_distributed.py#L93)
- <a id="_layer_loop"></a>`_layer_loop` — [`L47`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack_reshard_distributed.py#L47)
- <a id="_load_flattened_optim_worker"></a>`_load_flattened_optim_worker` — [`L178`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack_reshard_distributed.py#L178)
- <a id="_load_worker"></a>`_load_worker` — [`L123`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack_reshard_distributed.py#L123)
- <a id="_process_group"></a>`_process_group` — [`L99`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack_reshard_distributed.py#L99)
- <a id="_save_flattened_optim_worker"></a>`_save_flattened_optim_worker` — [`L172`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack_reshard_distributed.py#L172)
- <a id="_save_worker"></a>`_save_worker` — [`L112`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack_reshard_distributed.py#L112)
