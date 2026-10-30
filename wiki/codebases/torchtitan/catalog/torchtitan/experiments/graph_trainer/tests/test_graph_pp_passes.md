---
title: 'Module: torchtitan/experiments/graph_trainer/tests/test_graph_pp_passes.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/graph_trainer/tests/test_graph_pp_passes.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.graph_trainer.tests.test_graph_pp_passes`/
symbols:
  _trace_dsv3_moe_block_stage: _trace_dsv3_moe_block_stage().
  GraphPPFSDPCollectiveSplitDsv3Test.test_real_dsv3_moe_block_fsdp_split_reconstructs_graphs: GraphPPFSDPCollectiveSplitDsv3Test#test_real_dsv3_moe_block_fsdp_split_reconstructs_graphs().
  GraphPPPartitionTest.test_real_dsv3_moe_block_partition_matches_joint_graph: GraphPPPartitionTest#test_real_dsv3_moe_block_partition_matches_joint_graph().
  GraphPPSplitDiDwTest.test_real_dsv3_moe_block_split_reconstructs_backward: GraphPPSplitDiDwTest#test_real_dsv3_moe_block_split_reconstructs_backward().
  GraphPPPartitionFSDPTest.test_real_dsv3_moe_block_fsdp_partition_matches_joint_graph: GraphPPPartitionFSDPTest#test_real_dsv3_moe_block_fsdp_partition_matches_joint_graph().
  GraphPPPartitionTest.test_partition_saves_backward_passthrough_placeholders: GraphPPPartitionTest#test_partition_saves_backward_passthrough_placeholders().
  _GraphPPDsv3FSDPTest._setup: _GraphPPDsv3FSDPTest#_setup().
  GraphPPFSDPCollectiveSplitTest.test_forward_split_extracts_unshard_and_replicated_params: GraphPPFSDPCollectiveSplitTest#test_forward_split_extracts_unshard_and_replicated_params().
  _backward_args_from_partition: _backward_args_from_partition().
  _Dsv3MoeBlockTrace.traced: _Dsv3MoeBlockTrace#traced.
  GraphPPFSDPCollectiveSplitTest.test_backward_split_extracts_reduce_grad_epilogues: GraphPPFSDPCollectiveSplitTest#test_backward_split_extracts_reduce_grad_epilogues().
  _boxed_run: _boxed_run().
  GraphPPSplitDiDwTest.test_real_dsv3_moe_block_without_input_grad_skips_split: GraphPPSplitDiDwTest#test_real_dsv3_moe_block_without_input_grad_skips_split().
  GraphPPFSDPCollectiveSplitTest.test_forward_split_no_fsdp_is_noop: GraphPPFSDPCollectiveSplitTest#test_forward_split_no_fsdp_is_noop().
  GraphPPFSDPCollectiveSplitTest.test_forward_pattern_matches_reshard_force_save_pattern: GraphPPFSDPCollectiveSplitTest#test_forward_pattern_matches_reshard_force_save_pattern().
  _Dsv3MoeBlockTrace.num_param_grad_values: _Dsv3MoeBlockTrace#num_param_grad_values.
  GraphPPPartitionTest.test_invalid_backward_only_input_indices_raise: GraphPPPartitionTest#test_invalid_backward_only_input_indices_raise().
  GraphPPFSDPCollectiveSplitTest.test_backward_split_no_fsdp_is_noop_and_validates_grad_count: GraphPPFSDPCollectiveSplitTest#test_backward_split_no_fsdp_is_noop_and_validates_grad_count().
  _Dsv3MoeBlockTrace.flat_inputs: _Dsv3MoeBlockTrace#flat_inputs.
  _stable_flex_attention_compile_config: _stable_flex_attention_compile_config().
  GraphPPPartitionTest.test_backward_only_input_required_by_forward_raises: GraphPPPartitionTest#test_backward_only_input_required_by_forward_raises().
  GraphPPPartitionTest.test_forward_mutation_of_backward_only_input_raises: GraphPPPartitionTest#test_forward_mutation_of_backward_only_input_raises().
  _assert_tensor_sequence_equal: _assert_tensor_sequence_equal().
  _GraphPPDsv3FSDPTest: _GraphPPDsv3FSDPTest#
  _call_targets: _call_targets().
  _make_forward_graph_with_unshard_and_replicated_param: _make_forward_graph_with_unshard_and_replicated_param().
  _make_forward_graph_without_wait: _make_forward_graph_without_wait().
  _make_backward_graph_with_reduce_grad_epilogues: _make_backward_graph_with_reduce_grad_epilogues().
  _Dsv3MoeBlockTrace.output_grad: _Dsv3MoeBlockTrace#output_grad.
  _FAKE_PG: _FAKE_PG.
  _make_graph_module: _make_graph_module().
  GraphPPFSDPCollectiveSplitTest.test_forward_split_requires_wait_after_all_gather: GraphPPFSDPCollectiveSplitTest#test_forward_split_requires_wait_after_all_gather().
  GraphPPPartitionTest.stage_step: GraphPPPartitionTest#stage_step().
  _make_forward_graph_without_fsdp: _make_forward_graph_without_fsdp().
  _make_backward_graph_without_fsdp: _make_backward_graph_without_fsdp().
  GraphPPPartitionFSDPTest: GraphPPPartitionFSDPTest#
  GraphPPFSDPCollectiveSplitDsv3Test: GraphPPFSDPCollectiveSplitDsv3Test#
  _Dsv3MoeBlockTrace: _Dsv3MoeBlockTrace#
  _Dsv3MoeBlockTrace.num_flat_param_values: _Dsv3MoeBlockTrace#num_flat_param_values.
  _GraphPPDsv3FSDPTest.parallel_dims: _GraphPPDsv3FSDPTest#parallel_dims.
  _trace_dsv3_moe_block_stage.stage_step: _trace_dsv3_moe_block_stage().stage_step().
  _GraphPPDsv3FSDPTest.world_size: _GraphPPDsv3FSDPTest#world_size().
  _placeholder_names: _placeholder_names().
  GraphPPPartitionTest: GraphPPPartitionTest#
  GraphPPSplitDiDwTest: GraphPPSplitDiDwTest#
  GraphPPFSDPCollectiveSplitTest: GraphPPFSDPCollectiveSplitTest#
---
# Module: [`torchtitan/experiments/graph_trainer/tests/test_graph_pp_passes.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_graph_pp_passes.py)

> **Collapsed catalog** (46 symbols) — one row per symbol with its source line; member detail omitted. See the source link above, or the curated codebase page, for depth.

- <a id="GraphPPFSDPCollectiveSplitDsv3Test"></a>`GraphPPFSDPCollectiveSplitDsv3Test` — [`L767`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_graph_pp_passes.py#L767)
- <a id="GraphPPFSDPCollectiveSplitDsv3Test.test_real_dsv3_moe_block_fsdp_split_reconstructs_graphs"></a>`GraphPPFSDPCollectiveSplitDsv3Test.test_real_dsv3_moe_block_fsdp_split_reconstructs_graphs` — [`L768`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_graph_pp_passes.py#L768)
- <a id="GraphPPFSDPCollectiveSplitTest"></a>`GraphPPFSDPCollectiveSplitTest` — [`L655`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_graph_pp_passes.py#L655)
- <a id="GraphPPFSDPCollectiveSplitTest.test_backward_split_extracts_reduce_grad_epilogues"></a>`GraphPPFSDPCollectiveSplitTest.test_backward_split_extracts_reduce_grad_epilogues` — [`L720`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_graph_pp_passes.py#L720)
- <a id="GraphPPFSDPCollectiveSplitTest.test_backward_split_no_fsdp_is_noop_and_validates_grad_count"></a>`GraphPPFSDPCollectiveSplitTest.test_backward_split_no_fsdp_is_noop_and_validates_grad_count` — [`L756`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_graph_pp_passes.py#L756)
- <a id="GraphPPFSDPCollectiveSplitTest.test_forward_pattern_matches_reshard_force_save_pattern"></a>`GraphPPFSDPCollectiveSplitTest.test_forward_pattern_matches_reshard_force_save_pattern` — [`L656`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_graph_pp_passes.py#L656)
- <a id="GraphPPFSDPCollectiveSplitTest.test_forward_split_extracts_unshard_and_replicated_params"></a>`GraphPPFSDPCollectiveSplitTest.test_forward_split_extracts_unshard_and_replicated_params` — [`L666`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_graph_pp_passes.py#L666)
- <a id="GraphPPFSDPCollectiveSplitTest.test_forward_split_no_fsdp_is_noop"></a>`GraphPPFSDPCollectiveSplitTest.test_forward_split_no_fsdp_is_noop` — [`L697`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_graph_pp_passes.py#L697)
- <a id="GraphPPFSDPCollectiveSplitTest.test_forward_split_requires_wait_after_all_gather"></a>`GraphPPFSDPCollectiveSplitTest.test_forward_split_requires_wait_after_all_gather` — [`L711`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_graph_pp_passes.py#L711)
- <a id="GraphPPPartitionFSDPTest"></a>`GraphPPPartitionFSDPTest` — [`L432`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_graph_pp_passes.py#L432)
- <a id="GraphPPPartitionFSDPTest.test_real_dsv3_moe_block_fsdp_partition_matches_joint_graph"></a>`GraphPPPartitionFSDPTest.test_real_dsv3_moe_block_fsdp_partition_matches_joint_graph` — [`L433`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_graph_pp_passes.py#L433)
- <a id="GraphPPPartitionTest"></a>`GraphPPPartitionTest` — [`L265`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_graph_pp_passes.py#L265)
- <a id="GraphPPPartitionTest.stage_step"></a>`GraphPPPartitionTest.stage_step` — [`L304`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_graph_pp_passes.py#L304)
- <a id="GraphPPPartitionTest.test_backward_only_input_required_by_forward_raises"></a>`GraphPPPartitionTest.test_backward_only_input_required_by_forward_raises` — [`L368`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_graph_pp_passes.py#L368)
- <a id="GraphPPPartitionTest.test_forward_mutation_of_backward_only_input_raises"></a>`GraphPPPartitionTest.test_forward_mutation_of_backward_only_input_raises` — [`L388`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_graph_pp_passes.py#L388)
- <a id="GraphPPPartitionTest.test_invalid_backward_only_input_indices_raise"></a>`GraphPPPartitionTest.test_invalid_backward_only_input_indices_raise` — [`L344`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_graph_pp_passes.py#L344)
- <a id="GraphPPPartitionTest.test_partition_saves_backward_passthrough_placeholders"></a>`GraphPPPartitionTest.test_partition_saves_backward_passthrough_placeholders` — [`L303`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_graph_pp_passes.py#L303)
- <a id="GraphPPPartitionTest.test_real_dsv3_moe_block_partition_matches_joint_graph"></a>`GraphPPPartitionTest.test_real_dsv3_moe_block_partition_matches_joint_graph` — [`L266`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_graph_pp_passes.py#L266)
- <a id="GraphPPSplitDiDwTest"></a>`GraphPPSplitDiDwTest` — [`L464`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_graph_pp_passes.py#L464)
- <a id="GraphPPSplitDiDwTest.test_real_dsv3_moe_block_split_reconstructs_backward"></a>`GraphPPSplitDiDwTest.test_real_dsv3_moe_block_split_reconstructs_backward` — [`L465`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_graph_pp_passes.py#L465)
- <a id="GraphPPSplitDiDwTest.test_real_dsv3_moe_block_without_input_grad_skips_split"></a>`GraphPPSplitDiDwTest.test_real_dsv3_moe_block_without_input_grad_skips_split` — [`L510`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_graph_pp_passes.py#L510)
- <a id="_Dsv3MoeBlockTrace"></a>`_Dsv3MoeBlockTrace` — [`L56`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_graph_pp_passes.py#L56)
- <a id="_Dsv3MoeBlockTrace.flat_inputs"></a>`_Dsv3MoeBlockTrace.flat_inputs` — [`L58`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_graph_pp_passes.py#L58)
- <a id="_Dsv3MoeBlockTrace.num_flat_param_values"></a>`_Dsv3MoeBlockTrace.num_flat_param_values` — [`L61`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_graph_pp_passes.py#L61)
- <a id="_Dsv3MoeBlockTrace.num_param_grad_values"></a>`_Dsv3MoeBlockTrace.num_param_grad_values` — [`L60`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_graph_pp_passes.py#L60)
- <a id="_Dsv3MoeBlockTrace.output_grad"></a>`_Dsv3MoeBlockTrace.output_grad` — [`L59`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_graph_pp_passes.py#L59)
- <a id="_Dsv3MoeBlockTrace.traced"></a>`_Dsv3MoeBlockTrace.traced` — [`L57`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_graph_pp_passes.py#L57)
- <a id="_FAKE_PG"></a>`_FAKE_PG` — [`L526`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_graph_pp_passes.py#L526)
- <a id="_GraphPPDsv3FSDPTest"></a>`_GraphPPDsv3FSDPTest` — [`L414`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_graph_pp_passes.py#L414)
- <a id="_GraphPPDsv3FSDPTest._setup"></a>`_GraphPPDsv3FSDPTest._setup` — [`L419`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_graph_pp_passes.py#L419)
- <a id="_GraphPPDsv3FSDPTest.parallel_dims"></a>`_GraphPPDsv3FSDPTest.parallel_dims` — [`L420`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_graph_pp_passes.py#L420)
- <a id="_GraphPPDsv3FSDPTest.world_size"></a>`_GraphPPDsv3FSDPTest.world_size` — [`L416`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_graph_pp_passes.py#L416)
- <a id="_assert_tensor_sequence_equal"></a>`_assert_tensor_sequence_equal` — [`L248`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_graph_pp_passes.py#L248)
- <a id="_backward_args_from_partition"></a>`_backward_args_from_partition` — [`L220`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_graph_pp_passes.py#L220)
- <a id="_boxed_run"></a>`_boxed_run` — [`L216`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_graph_pp_passes.py#L216)
- <a id="_call_targets"></a>`_call_targets` — [`L529`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_graph_pp_passes.py#L529)
- <a id="_make_backward_graph_with_reduce_grad_epilogues"></a>`_make_backward_graph_with_reduce_grad_epilogues` — [`L617`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_graph_pp_passes.py#L617)
- <a id="_make_backward_graph_without_fsdp"></a>`_make_backward_graph_without_fsdp` — [`L647`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_graph_pp_passes.py#L647)
- <a id="_make_forward_graph_with_unshard_and_replicated_param"></a>`_make_forward_graph_with_unshard_and_replicated_param` — [`L544`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_graph_pp_passes.py#L544)
- <a id="_make_forward_graph_without_fsdp"></a>`_make_forward_graph_without_fsdp` — [`L595`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_graph_pp_passes.py#L595)
- <a id="_make_forward_graph_without_wait"></a>`_make_forward_graph_without_wait` — [`L604`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_graph_pp_passes.py#L604)
- <a id="_make_graph_module"></a>`_make_graph_module` — [`L537`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_graph_pp_passes.py#L537)
- <a id="_placeholder_names"></a>`_placeholder_names` — [`L533`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_graph_pp_passes.py#L533)
- <a id="_stable_flex_attention_compile_config"></a>`_stable_flex_attention_compile_config` — [`L65`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_graph_pp_passes.py#L65)
- <a id="_trace_dsv3_moe_block_stage"></a>`_trace_dsv3_moe_block_stage` — [`L84`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_graph_pp_passes.py#L84)
- <a id="_trace_dsv3_moe_block_stage.stage_step"></a>`_trace_dsv3_moe_block_stage.stage_step` — [`L161`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_graph_pp_passes.py#L161)
