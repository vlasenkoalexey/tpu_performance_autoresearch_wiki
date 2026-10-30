---
title: 'Module: torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack_distributed.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack_distributed.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.graph_trainer.tests.test_layer_stack_distributed`/
symbols:
  TestLayerStackDistributed._on_devices: TestLayerStackDistributed#_on_devices().
  a_sharded_stack_gathers_and_reduces_like_unrolled: a_sharded_stack_gathers_and_reduces_like_unrolled().
  flattened_forward_matches_unrolled: flattened_forward_matches_unrolled().
  a_replicated_stack_still_sums_its_gradient: a_replicated_stack_still_sums_its_gradient().
  a_doubly_replicated_stack_sums_on_both_axes: a_doubly_replicated_stack_sums_on_both_axes().
  a_hybrid_sharded_stack_sums_over_both_axes: a_hybrid_sharded_stack_sums_over_both_axes().
  _models: _models().
  forward_matches_unrolled: forward_matches_unrolled().
  stacks_are_sharded_off_the_layer_axis: stacks_are_sharded_off_the_layer_axis().
  an_unevenly_sharded_stack_is_refused: an_unevenly_sharded_stack_is_refused().
  an_unevenly_sharded_hybrid_stack_is_refused: an_unevenly_sharded_hybrid_stack_is_refused().
  TestLayerStackDistributed.test_forward_matches_unrolled: TestLayerStackDistributed#test_forward_matches_unrolled().
  TestLayerStackDistributed.test_flattened_forward_matches_unrolled: TestLayerStackDistributed#test_flattened_forward_matches_unrolled().
  TestLayerStackDistributed.test_stacks_are_sharded_off_the_layer_axis: TestLayerStackDistributed#test_stacks_are_sharded_off_the_layer_axis().
  TestLayerStackDistributed.test_a_replicated_stack_still_sums_its_gradient: TestLayerStackDistributed#test_a_replicated_stack_still_sums_its_gradient().
  TestLayerStackDistributed.test_a_sharded_stack_gathers_and_reduces_like_unrolled: TestLayerStackDistributed#test_a_sharded_stack_gathers_and_reduces_like_unrolled().
  TestLayerStackDistributed.test_a_stack_sharded_off_dim_one_gathers_the_same_way: TestLayerStackDistributed#test_a_stack_sharded_off_dim_one_gathers_the_same_way().
  TestLayerStackDistributed.test_an_unevenly_sharded_stack_is_refused: TestLayerStackDistributed#test_an_unevenly_sharded_stack_is_refused().
  TestLayerStackDistributed.test_a_hybrid_sharded_stack_sums_over_both_axes: TestLayerStackDistributed#test_a_hybrid_sharded_stack_sums_over_both_axes().
  TestLayerStackDistributed.test_a_doubly_replicated_stack_sums_on_both_axes: TestLayerStackDistributed#test_a_doubly_replicated_stack_sums_on_both_axes().
  TestLayerStackDistributed.test_an_unevenly_sharded_hybrid_stack_is_refused: TestLayerStackDistributed#test_an_unevenly_sharded_hybrid_stack_is_refused().
  TestLayerStackDistributed: TestLayerStackDistributed#
---
# Module: [`torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack_distributed.py`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack_distributed.py)

> **Collapsed catalog** (22 symbols) — one row per symbol with its source line; member detail omitted. See the source link above, or the curated codebase page, for depth.

- <a id="TestLayerStackDistributed"></a>`TestLayerStackDistributed` — [`L393`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack_distributed.py#L393)
- <a id="TestLayerStackDistributed._on_devices"></a>`TestLayerStackDistributed._on_devices` — [`L402`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack_distributed.py#L402)
- <a id="TestLayerStackDistributed.test_a_doubly_replicated_stack_sums_on_both_axes"></a>`TestLayerStackDistributed.test_a_doubly_replicated_stack_sums_on_both_axes` — [`L436`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack_distributed.py#L436)
- <a id="TestLayerStackDistributed.test_a_hybrid_sharded_stack_sums_over_both_axes"></a>`TestLayerStackDistributed.test_a_hybrid_sharded_stack_sums_over_both_axes` — [`L433`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack_distributed.py#L433)
- <a id="TestLayerStackDistributed.test_a_replicated_stack_still_sums_its_gradient"></a>`TestLayerStackDistributed.test_a_replicated_stack_still_sums_its_gradient` — [`L416`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack_distributed.py#L416)
- <a id="TestLayerStackDistributed.test_a_sharded_stack_gathers_and_reduces_like_unrolled"></a>`TestLayerStackDistributed.test_a_sharded_stack_gathers_and_reduces_like_unrolled` — [`L419`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack_distributed.py#L419)
- <a id="TestLayerStackDistributed.test_a_stack_sharded_off_dim_one_gathers_the_same_way"></a>`TestLayerStackDistributed.test_a_stack_sharded_off_dim_one_gathers_the_same_way` — [`L422`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack_distributed.py#L422)
- <a id="TestLayerStackDistributed.test_an_unevenly_sharded_hybrid_stack_is_refused"></a>`TestLayerStackDistributed.test_an_unevenly_sharded_hybrid_stack_is_refused` — [`L439`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack_distributed.py#L439)
- <a id="TestLayerStackDistributed.test_an_unevenly_sharded_stack_is_refused"></a>`TestLayerStackDistributed.test_an_unevenly_sharded_stack_is_refused` — [`L430`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack_distributed.py#L430)
- <a id="TestLayerStackDistributed.test_flattened_forward_matches_unrolled"></a>`TestLayerStackDistributed.test_flattened_forward_matches_unrolled` — [`L410`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack_distributed.py#L410)
- <a id="TestLayerStackDistributed.test_forward_matches_unrolled"></a>`TestLayerStackDistributed.test_forward_matches_unrolled` — [`L407`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack_distributed.py#L407)
- <a id="TestLayerStackDistributed.test_stacks_are_sharded_off_the_layer_axis"></a>`TestLayerStackDistributed.test_stacks_are_sharded_off_the_layer_axis` — [`L413`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack_distributed.py#L413)
- <a id="_models"></a>`_models` — [`L46`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack_distributed.py#L46)
- <a id="a_doubly_replicated_stack_sums_on_both_axes"></a>`a_doubly_replicated_stack_sums_on_both_axes` — [`L231`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack_distributed.py#L231)
- <a id="a_hybrid_sharded_stack_sums_over_both_axes"></a>`a_hybrid_sharded_stack_sums_over_both_axes` — [`L280`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack_distributed.py#L280)
- <a id="a_replicated_stack_still_sums_its_gradient"></a>`a_replicated_stack_still_sums_its_gradient` — [`L136`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack_distributed.py#L136)
- <a id="a_sharded_stack_gathers_and_reduces_like_unrolled"></a>`a_sharded_stack_gathers_and_reduces_like_unrolled` — [`L171`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack_distributed.py#L171)
- <a id="an_unevenly_sharded_hybrid_stack_is_refused"></a>`an_unevenly_sharded_hybrid_stack_is_refused` — [`L359`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack_distributed.py#L359)
- <a id="an_unevenly_sharded_stack_is_refused"></a>`an_unevenly_sharded_stack_is_refused` — [`L329`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack_distributed.py#L329)
- <a id="flattened_forward_matches_unrolled"></a>`flattened_forward_matches_unrolled` — [`L66`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack_distributed.py#L66)
- <a id="forward_matches_unrolled"></a>`forward_matches_unrolled` — [`L58`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack_distributed.py#L58)
- <a id="stacks_are_sharded_off_the_layer_axis"></a>`stacks_are_sharded_off_the_layer_axis` — [`L123`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack_distributed.py#L123)
