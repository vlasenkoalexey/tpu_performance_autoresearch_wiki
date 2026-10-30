---
title: 'Module: torchtitan/experiments/tpu/graph_trainer/tests/test_scan_fsdp_shard_dim.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/graph_trainer/tests/test_scan_fsdp_shard_dim.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.graph_trainer.tests.test_scan_fsdp_shard_dim`/
symbols:
  TestShardDimPicker.test_subtile_two_d_gather_and_scatter_fold_minor_axis_to_align_tiles: TestShardDimPicker#test_subtile_two_d_gather_and_scatter_fold_minor_axis_to_align_tiles().
  TestFlattenedStacks.test_axes_one_and_two_are_flattened: TestFlattenedStacks#test_axes_one_and_two_are_flattened().
  TestFlattenedStacks.test_layer_view_hsdp: TestFlattenedStacks#test_layer_view_hsdp().
  Q235_STACKS: Q235_STACKS.
  _sharded_holder: _sharded_holder().
  TestQ235Placements.test_hsdp_plans_off_the_shard_axis_not_the_whole_mesh: TestQ235Placements#test_hsdp_plans_off_the_shard_axis_not_the_whole_mesh().
  TestShardDimPicker.test_fold_survives_strides_that_change_between_trace_and_replay: TestShardDimPicker#test_fold_survives_strides_that_change_between_trace_and_replay().
  TestFlattenedStacks.test_an_already_sharded_stack_is_left_unflattened: TestFlattenedStacks#test_an_already_sharded_stack_is_left_unflattened().
  _holder: _holder().
  TestShardDimPicker.test_configure_simple_fsdp_shard_dims_allows_narrow_hidden_axis_for_replication: TestShardDimPicker#test_configure_simple_fsdp_shard_dims_allows_narrow_hidden_axis_for_replication().
  TestFlattenedStacks.test_layer_view_writes_land_in_the_stack: TestFlattenedStacks#test_layer_view_writes_land_in_the_stack().
  _fake_pg: _fake_pg().
  _pick: _pick().
  N_LAYERS: N_LAYERS.
  TestShardDimPicker.test_the_layer_axis_is_never_chosen: TestShardDimPicker#test_the_layer_axis_is_never_chosen().
  TestQ235Placements.test_an_already_distributed_parameter_is_refused: TestQ235Placements#test_an_already_distributed_parameter_is_refused().
  TestFlattenedStacks.test_nothing_is_flattened_while_num_experts_divides: TestFlattenedStacks#test_nothing_is_flattened_while_num_experts_divides().
  FLATTENED: FLATTENED.
  _shard: _shard().
  TestShardDimPicker.test_dim_one_is_kept_whenever_it_divides: TestShardDimPicker#test_dim_one_is_kept_whenever_it_divides().
  TestShardDimPicker.test_every_expert_stack_takes_the_same_axis_at_512_ranks: TestShardDimPicker#test_every_expert_stack_takes_the_same_axis_at_512_ranks().
  TestShardDimPicker.test_an_expert_stack_moves_off_num_experts_past_128_ranks: TestShardDimPicker#test_an_expert_stack_moves_off_num_experts_past_128_ranks().
  TestShardDimPicker.test_a_gather_off_dim_zero_is_transposed_onto_dim_zero: TestShardDimPicker#test_a_gather_off_dim_zero_is_transposed_onto_dim_zero().
  TestQ235Placements.test_a_dict_places_exactly_like_the_int_it_repeats: TestQ235Placements#test_a_dict_places_exactly_like_the_int_it_repeats().
  TestFlattenedStacks.test_a_shard_spanning_two_experts_is_not_flattened: TestFlattenedStacks#test_a_shard_spanning_two_experts_is_not_flattened().
  TestFlattenedStacks.test_reflattening: TestFlattenedStacks#test_reflattening().
  TestQ235Placements.placements: TestQ235Placements#placements().
  TestShardDimPicker.fake_all_gather: TestShardDimPicker#fake_all_gather().
  TestFlattenedStacks._flattened: TestFlattenedStacks#_flattened().
  TestShardDimPicker.fake_reduce_scatter: TestShardDimPicker#fake_reduce_scatter().
  TestShardDimPicker: TestShardDimPicker#
  TestQ235Placements: TestQ235Placements#
  TestFlattenedStacks: TestFlattenedStacks#
---
# Module: [`torchtitan/experiments/tpu/graph_trainer/tests/test_scan_fsdp_shard_dim.py`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_scan_fsdp_shard_dim.py)

> **Collapsed catalog** (33 symbols) — one row per symbol with its source line; member detail omitted. See the source link above, or the curated codebase page, for depth.

- <a id="FLATTENED"></a>`FLATTENED` — [`L52`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_scan_fsdp_shard_dim.py#L52)
- <a id="N_LAYERS"></a>`N_LAYERS` — [`L38`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_scan_fsdp_shard_dim.py#L38)
- <a id="Q235_STACKS"></a>`Q235_STACKS` — [`L41`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_scan_fsdp_shard_dim.py#L41)
- <a id="TestFlattenedStacks"></a>`TestFlattenedStacks` — [`L359`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_scan_fsdp_shard_dim.py#L359)
- <a id="TestFlattenedStacks._flattened"></a>`TestFlattenedStacks._flattened` — [`L362`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_scan_fsdp_shard_dim.py#L362)
- <a id="TestFlattenedStacks.test_a_shard_spanning_two_experts_is_not_flattened"></a>`TestFlattenedStacks.test_a_shard_spanning_two_experts_is_not_flattened` — [`L393`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_scan_fsdp_shard_dim.py#L393)
- <a id="TestFlattenedStacks.test_an_already_sharded_stack_is_left_unflattened"></a>`TestFlattenedStacks.test_an_already_sharded_stack_is_left_unflattened` — [`L409`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_scan_fsdp_shard_dim.py#L409)
- <a id="TestFlattenedStacks.test_axes_one_and_two_are_flattened"></a>`TestFlattenedStacks.test_axes_one_and_two_are_flattened` — [`L371`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_scan_fsdp_shard_dim.py#L371)
- <a id="TestFlattenedStacks.test_layer_view_hsdp"></a>`TestFlattenedStacks.test_layer_view_hsdp` — [`L425`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_scan_fsdp_shard_dim.py#L425)
- <a id="TestFlattenedStacks.test_layer_view_writes_land_in_the_stack"></a>`TestFlattenedStacks.test_layer_view_writes_land_in_the_stack` — [`L449`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_scan_fsdp_shard_dim.py#L449)
- <a id="TestFlattenedStacks.test_nothing_is_flattened_while_num_experts_divides"></a>`TestFlattenedStacks.test_nothing_is_flattened_while_num_experts_divides` — [`L365`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_scan_fsdp_shard_dim.py#L365)
- <a id="TestFlattenedStacks.test_reflattening"></a>`TestFlattenedStacks.test_reflattening` — [`L399`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_scan_fsdp_shard_dim.py#L399)
- <a id="TestQ235Placements"></a>`TestQ235Placements` — [`L315`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_scan_fsdp_shard_dim.py#L315)
- <a id="TestQ235Placements.placements"></a>`TestQ235Placements.placements` — [`L321`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_scan_fsdp_shard_dim.py#L321)
- <a id="TestQ235Placements.test_a_dict_places_exactly_like_the_int_it_repeats"></a>`TestQ235Placements.test_a_dict_places_exactly_like_the_int_it_repeats` — [`L318`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_scan_fsdp_shard_dim.py#L318)
- <a id="TestQ235Placements.test_an_already_distributed_parameter_is_refused"></a>`TestQ235Placements.test_an_already_distributed_parameter_is_refused` — [`L329`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_scan_fsdp_shard_dim.py#L329)
- <a id="TestQ235Placements.test_hsdp_plans_off_the_shard_axis_not_the_whole_mesh"></a>`TestQ235Placements.test_hsdp_plans_off_the_shard_axis_not_the_whole_mesh` — [`L346`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_scan_fsdp_shard_dim.py#L346)
- <a id="TestShardDimPicker"></a>`TestShardDimPicker` — [`L102`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_scan_fsdp_shard_dim.py#L102)
- <a id="TestShardDimPicker.fake_all_gather"></a>`TestShardDimPicker.fake_all_gather` — [`L134`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_scan_fsdp_shard_dim.py#L134)
- <a id="TestShardDimPicker.fake_reduce_scatter"></a>`TestShardDimPicker.fake_reduce_scatter` — [`L160`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_scan_fsdp_shard_dim.py#L160)
- <a id="TestShardDimPicker.test_a_gather_off_dim_zero_is_transposed_onto_dim_zero"></a>`TestShardDimPicker.test_a_gather_off_dim_zero_is_transposed_onto_dim_zero` — [`L126`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_scan_fsdp_shard_dim.py#L126)
- <a id="TestShardDimPicker.test_an_expert_stack_moves_off_num_experts_past_128_ranks"></a>`TestShardDimPicker.test_an_expert_stack_moves_off_num_experts_past_128_ranks` — [`L120`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_scan_fsdp_shard_dim.py#L120)
- <a id="TestShardDimPicker.test_configure_simple_fsdp_shard_dims_allows_narrow_hidden_axis_for_replication"></a>`TestShardDimPicker.test_configure_simple_fsdp_shard_dims_allows_narrow_hidden_axis_for_replication` — [`L200`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_scan_fsdp_shard_dim.py#L200)
- <a id="TestShardDimPicker.test_dim_one_is_kept_whenever_it_divides"></a>`TestShardDimPicker.test_dim_one_is_kept_whenever_it_divides` — [`L105`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_scan_fsdp_shard_dim.py#L105)
- <a id="TestShardDimPicker.test_every_expert_stack_takes_the_same_axis_at_512_ranks"></a>`TestShardDimPicker.test_every_expert_stack_takes_the_same_axis_at_512_ranks` — [`L112`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_scan_fsdp_shard_dim.py#L112)
- <a id="TestShardDimPicker.test_fold_survives_strides_that_change_between_trace_and_replay"></a>`TestShardDimPicker.test_fold_survives_strides_that_change_between_trace_and_replay` — [`L144`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_scan_fsdp_shard_dim.py#L144)
- <a id="TestShardDimPicker.test_subtile_two_d_gather_and_scatter_fold_minor_axis_to_align_tiles"></a>`TestShardDimPicker.test_subtile_two_d_gather_and_scatter_fold_minor_axis_to_align_tiles` — [`L241`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_scan_fsdp_shard_dim.py#L241)
- <a id="TestShardDimPicker.test_the_layer_axis_is_never_chosen"></a>`TestShardDimPicker.test_the_layer_axis_is_never_chosen` — [`L192`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_scan_fsdp_shard_dim.py#L192)
- <a id="_fake_pg"></a>`_fake_pg` — [`L62`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_scan_fsdp_shard_dim.py#L62)
- <a id="_holder"></a>`_holder` — [`L70`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_scan_fsdp_shard_dim.py#L70)
- <a id="_pick"></a>`_pick` — [`L57`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_scan_fsdp_shard_dim.py#L57)
- <a id="_shard"></a>`_shard` — [`L80`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_scan_fsdp_shard_dim.py#L80)
- <a id="_sharded_holder"></a>`_sharded_holder` — [`L90`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_scan_fsdp_shard_dim.py#L90)
