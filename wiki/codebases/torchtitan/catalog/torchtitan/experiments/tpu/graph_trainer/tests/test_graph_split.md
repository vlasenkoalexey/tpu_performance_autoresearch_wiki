---
title: 'Module: torchtitan/experiments/tpu/graph_trainer/tests/test_graph_split.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/graph_trainer/tests/test_graph_split.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.graph_trainer.tests.test_graph_split`/
symbols:
  GraphSplitTest.test_view_layer_boundaries_offload_and_split_by_layer: GraphSplitTest#test_view_layer_boundaries_offload_and_split_by_layer().
  GraphSplitTest.test_forward_backward_split_preserves_values_mutations_and_ordering: GraphSplitTest#test_forward_backward_split_preserves_values_mutations_and_ordering().
  GraphSplitTest.test_cpu_offload_ops_are_compiled_inside_layer_children: GraphSplitTest#test_cpu_offload_ops_are_compiled_inside_layer_children().
  GraphSplitTest.test_forward_backward_boundary_edge_cases: GraphSplitTest#test_forward_backward_boundary_edge_cases().
  GraphSplitTest.test_cpu_reload_prefetch_distance_counts_executables: GraphSplitTest#test_cpu_reload_prefetch_distance_counts_executables().
  GraphSplitTest.test_partition_layouts_reuse_one_simple_fsdp_trace: GraphSplitTest#test_partition_layouts_reuse_one_simple_fsdp_trace().
  GraphSplitTest._trace_simple_fsdp: GraphSplitTest#_trace_simple_fsdp().
  GraphSplitTest._trace_cpu_offload_graph: GraphSplitTest#_trace_cpu_offload_graph().
  GraphSplitTest.test_unsplit_forward_still_donates_persistent_host_slot: GraphSplitTest#test_unsplit_forward_still_donates_persistent_host_slot().
  GraphSplitTest._apply_passes_and_split: GraphSplitTest#_apply_passes_and_split().
  GraphSplitTest._trace_toy_model: GraphSplitTest#_trace_toy_model().
  GraphSplitTest.test_backward_fsdp_pipeline_keeps_bf16_reduce_cast_with_wait: GraphSplitTest#test_backward_fsdp_pipeline_keeps_bf16_reduce_cast_with_wait().
  GraphSplitTest._build_toy_model: GraphSplitTest#_build_toy_model().
  _ToyTransformer: _ToyTransformer#
  _ToyTransformer.forward: _ToyTransformer#forward().
  GraphSplitTest.test_child_boundaries_order_inputs_by_last_read_and_outputs_by_depth: GraphSplitTest#test_child_boundaries_order_inputs_by_last_read_and_outputs_by_depth().
  GraphSplitTest._assert_collective_chains_are_atomic: GraphSplitTest#_assert_collective_chains_are_atomic().
  GraphSplitTest.targets: GraphSplitTest#targets().
  _BufferMutatingToyTransformer: _BufferMutatingToyTransformer#
  _BufferMutatingToyTransformer.__init__: _BufferMutatingToyTransformer#__init__().
  _BufferMutatingToyTransformer.forward: _BufferMutatingToyTransformer#forward().
  _OffloadToyTransformer.forward: _OffloadToyTransformer#forward().
  _ViewOutputLayer.forward: _ViewOutputLayer#forward().
  _ToyTransformer.layers: _ToyTransformer#layers.
  _OffloadToyTransformer: _OffloadToyTransformer#
  _OffloadToyTransformer.layers: _OffloadToyTransformer#layers.
  GraphSplitTest.step: GraphSplitTest#step().
  GraphSplitTest.fn: GraphSplitTest#fn().
  _ToyTransformer.__init__: _ToyTransformer#__init__().
  _ViewOutputLayer: _ViewOutputLayer#
  _ViewOutputLayer.linear: _ViewOutputLayer#linear.
  _OffloadToyTransformer.__init__: _OffloadToyTransformer#__init__().
  _ViewOutputLayer.__init__: _ViewOutputLayer#__init__().
  GraphSplitTest: GraphSplitTest#
---
# Module: [`torchtitan/experiments/tpu/graph_trainer/tests/test_graph_split.py`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_graph_split.py)

> **Collapsed catalog** (34 symbols) — one row per symbol with its source line; member detail omitted. See the source link above, or the curated codebase page, for depth.

- <a id="GraphSplitTest"></a>`GraphSplitTest` — [`L103`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_graph_split.py#L103)
- <a id="GraphSplitTest._apply_passes_and_split"></a>`GraphSplitTest._apply_passes_and_split` — [`L136`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_graph_split.py#L136)
- <a id="GraphSplitTest._assert_collective_chains_are_atomic"></a>`GraphSplitTest._assert_collective_chains_are_atomic` — [`L195`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_graph_split.py#L195)
- <a id="GraphSplitTest._build_toy_model"></a>`GraphSplitTest._build_toy_model` — [`L105`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_graph_split.py#L105)
- <a id="GraphSplitTest._trace_cpu_offload_graph"></a>`GraphSplitTest._trace_cpu_offload_graph` — [`L388`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_graph_split.py#L388)
- <a id="GraphSplitTest._trace_simple_fsdp"></a>`GraphSplitTest._trace_simple_fsdp` — [`L156`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_graph_split.py#L156)
- <a id="GraphSplitTest._trace_toy_model"></a>`GraphSplitTest._trace_toy_model` — [`L111`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_graph_split.py#L111)
- <a id="GraphSplitTest.fn"></a>`GraphSplitTest.fn` — [`L555`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_graph_split.py#L555)
- <a id="GraphSplitTest.step"></a>`GraphSplitTest.step` — [`L121`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_graph_split.py#L121)
- <a id="GraphSplitTest.targets"></a>`GraphSplitTest.targets` — [`L428`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_graph_split.py#L428)
- <a id="GraphSplitTest.test_backward_fsdp_pipeline_keeps_bf16_reduce_cast_with_wait"></a>`GraphSplitTest.test_backward_fsdp_pipeline_keeps_bf16_reduce_cast_with_wait` — [`L793`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_graph_split.py#L793)
- <a id="GraphSplitTest.test_child_boundaries_order_inputs_by_last_read_and_outputs_by_depth"></a>`GraphSplitTest.test_child_boundaries_order_inputs_by_last_read_and_outputs_by_depth` — [`L549`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_graph_split.py#L549)
- <a id="GraphSplitTest.test_cpu_offload_ops_are_compiled_inside_layer_children"></a>`GraphSplitTest.test_cpu_offload_ops_are_compiled_inside_layer_children` — [`L407`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_graph_split.py#L407)
- <a id="GraphSplitTest.test_cpu_reload_prefetch_distance_counts_executables"></a>`GraphSplitTest.test_cpu_reload_prefetch_distance_counts_executables` — [`L583`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_graph_split.py#L583)
- <a id="GraphSplitTest.test_forward_backward_boundary_edge_cases"></a>`GraphSplitTest.test_forward_backward_boundary_edge_cases` — [`L319`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_graph_split.py#L319)
- <a id="GraphSplitTest.test_forward_backward_split_preserves_values_mutations_and_ordering"></a>`GraphSplitTest.test_forward_backward_split_preserves_values_mutations_and_ordering` — [`L209`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_graph_split.py#L209)
- <a id="GraphSplitTest.test_partition_layouts_reuse_one_simple_fsdp_trace"></a>`GraphSplitTest.test_partition_layouts_reuse_one_simple_fsdp_trace` — [`L659`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_graph_split.py#L659)
- <a id="GraphSplitTest.test_unsplit_forward_still_donates_persistent_host_slot"></a>`GraphSplitTest.test_unsplit_forward_still_donates_persistent_host_slot` — [`L614`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_graph_split.py#L614)
- <a id="GraphSplitTest.test_view_layer_boundaries_offload_and_split_by_layer"></a>`GraphSplitTest.test_view_layer_boundaries_offload_and_split_by_layer` — [`L510`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_graph_split.py#L510)
- <a id="_BufferMutatingToyTransformer"></a>`_BufferMutatingToyTransformer` — [`L63`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_graph_split.py#L63)
- <a id="_BufferMutatingToyTransformer.__init__"></a>`_BufferMutatingToyTransformer.__init__` — [`L65`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_graph_split.py#L65)
- <a id="_BufferMutatingToyTransformer.forward"></a>`_BufferMutatingToyTransformer.forward` — [`L69`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_graph_split.py#L69)
- <a id="_OffloadToyTransformer"></a>`_OffloadToyTransformer` — [`L77`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_graph_split.py#L77)
- <a id="_OffloadToyTransformer.__init__"></a>`_OffloadToyTransformer.__init__` — [`L79`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_graph_split.py#L79)
- <a id="_OffloadToyTransformer.forward"></a>`_OffloadToyTransformer.forward` — [`L86`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_graph_split.py#L86)
- <a id="_OffloadToyTransformer.layers"></a>`_OffloadToyTransformer.layers` — [`L81`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_graph_split.py#L81)
- <a id="_ToyTransformer"></a>`_ToyTransformer` — [`L48`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_graph_split.py#L48)
- <a id="_ToyTransformer.__init__"></a>`_ToyTransformer.__init__` — [`L50`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_graph_split.py#L50)
- <a id="_ToyTransformer.forward"></a>`_ToyTransformer.forward` — [`L56`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_graph_split.py#L56)
- <a id="_ToyTransformer.layers"></a>`_ToyTransformer.layers` — [`L52`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_graph_split.py#L52)
- <a id="_ViewOutputLayer"></a>`_ViewOutputLayer` — [`L92`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_graph_split.py#L92)
- <a id="_ViewOutputLayer.__init__"></a>`_ViewOutputLayer.__init__` — [`L95`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_graph_split.py#L95)
- <a id="_ViewOutputLayer.forward"></a>`_ViewOutputLayer.forward` — [`L99`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_graph_split.py#L99)
- <a id="_ViewOutputLayer.linear"></a>`_ViewOutputLayer.linear` — [`L97`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_graph_split.py#L97)
