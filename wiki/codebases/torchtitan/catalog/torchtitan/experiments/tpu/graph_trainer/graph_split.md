---
title: 'Module: torchtitan/experiments/tpu/graph_trainer/graph_split.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/graph_trainer/graph_split.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.graph_trainer.graph_split`/
symbols:
  GraphSplitter.split_and_compile: GraphSplitter#split_and_compile().
  split_backward_graph_by_layer: split_backward_graph_by_layer().
  split_forward_backward_graph: split_forward_backward_graph().
  GraphSplitter.from_trainer_config: GraphSplitter#from_trainer_config().
  split_forward_graph_by_layer: split_forward_graph_by_layer().
  SplitForwardBackwardModule.forward: SplitForwardBackwardModule#forward().
  SplitForwardBackwardModule._initialize_host_donors: SplitForwardBackwardModule#_initialize_host_donors().
  PartitionedGraph.module: PartitionedGraph#module.
  SplitForwardBackwardGraph.module: SplitForwardBackwardGraph#module.
  SplitForwardBackwardGraph.backward_graph: SplitForwardBackwardGraph#backward_graph.
  _materialize_partitioned_graph: _materialize_partitioned_graph().
  _collect_backward_fsdp_owners: _collect_backward_fsdp_owners().
  SplitForwardBackwardGraph.forward_graph: SplitForwardBackwardGraph#forward_graph.
  GraphSplitter: GraphSplitter#
  GraphSplitter.config: GraphSplitter#config.
  _collect_collective_chains: _collect_collective_chains().
  PartitionedGraph.partition_map: PartitionedGraph#partition_map.
  PartitionedGraph.collective_layer_to_partition: PartitionedGraph#collective_layer_to_partition.
  _collective_producer: _collective_producer().
  PartitionedGraph.layer_to_partition: PartitionedGraph#layer_to_partition.
  GraphSplitter.enabled: GraphSplitter#enabled.
  SplitForwardBackwardModule.host_donor_specs: SplitForwardBackwardModule#host_donor_specs.
  SplitForwardBackwardGraph.forward_example_inputs: SplitForwardBackwardGraph#forward_example_inputs.
  split_forward_backward_graph.make_available_to_backward: split_forward_backward_graph().make_available_to_backward().
  SplitForwardBackwardModule.forward_graph: SplitForwardBackwardModule#forward_graph.
  _group_nodes_by_layer: _group_nodes_by_layer().
  _order_child_boundaries: _order_child_boundaries().
  split_forward_backward_graph.add_forward_dependencies: split_forward_backward_graph().add_forward_dependencies().
  SplitForwardBackwardModule.num_direct_forward_outputs: SplitForwardBackwardModule#num_direct_forward_outputs.
  SplitForwardBackwardModule._host_donors: SplitForwardBackwardModule#_host_donors.
  PartitionedGraph: PartitionedGraph#
  _is_getitem: _is_getitem().
  _is_collective: _is_collective().
  _enqueue_forward_graph_outputs: _enqueue_forward_graph_outputs().
  _as_tuple: _as_tuple().
  SplitForwardBackwardModule.backward_graph: SplitForwardBackwardModule#backward_graph.
  SplitForwardBackwardModule.host_donor_output_positions: SplitForwardBackwardModule#host_donor_output_positions.
  SplitForwardBackwardGraph.backward_example_inputs: SplitForwardBackwardGraph#backward_example_inputs.
  SplitForwardBackwardGraph.residual_nodes: SplitForwardBackwardGraph#residual_nodes.
  SplitForwardBackwardModule.__init__: SplitForwardBackwardModule#__init__().
  _synchronize_tpu: _synchronize_tpu().
  SplitForwardBackwardModule: SplitForwardBackwardModule#
  SplitForwardBackwardGraph: SplitForwardBackwardGraph#
  GraphSplitter.n_layers: GraphSplitter#n_layers.
  _is_spmd_region_marker: _is_spmd_region_marker().
  _body_nodes: _body_nodes().
  _assign_partition: _assign_partition().
  SplitForwardBackwardModule.forward_output_positions: SplitForwardBackwardModule#forward_output_positions.
  SplitForwardBackwardModule.backward_output_positions: SplitForwardBackwardModule#backward_output_positions.
  SplitForwardBackwardModule.constant_outputs: SplitForwardBackwardModule#constant_outputs.
  SplitForwardBackwardModule.num_residual_outputs: SplitForwardBackwardModule#num_residual_outputs.
  SplitForwardBackwardModule.num_outputs: SplitForwardBackwardModule#num_outputs.
  _preserves_numel: _preserves_numel().
  _validate_backward_partitions: _validate_backward_partitions().
  split_backward_graph_by_layer.collective_partition: split_backward_graph_by_layer().collective_partition().
  __all__: __all__.
---
# Module: [`torchtitan/experiments/tpu/graph_trainer/graph_split.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/graph_split.py)

## Classes
### <a id="GraphSplitter"></a>`GraphSplitter`
- def: [`torchtitan/experiments/tpu/graph_trainer/graph_split.py:254`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/graph_split.py#L254) — documented in [tpu-graph-trainer](../../../../../concepts/tpu-graph-trainer.md)
- doc: Validate, partition, and compile one GraphTrainer trace.
- signature: `class GraphSplitter:`
- members:
  - <a id="GraphSplitter.from_trainer_config"></a>`from_trainer_config(cls, config: TpuGraphTrainer.Config, *, optimizer_in_graph: bool)` — [`L262`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/graph_split.py#L262) — documented in [tpu-graph-trainer](../../../../../concepts/tpu-graph-trainer.md)
  - <a id="GraphSplitter.split_and_compile"></a>`split_and_compile(self, traced: TracedResult)` — [`L328`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/graph_split.py#L328) — Split one transformed joint graph and compile its child executables.
  - <a id="GraphSplitter.config"></a>`config` — [`L258`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/graph_split.py#L258)
  - <a id="GraphSplitter.enabled"></a>`enabled` — [`L257`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/graph_split.py#L257)
  - <a id="GraphSplitter.n_layers"></a>`n_layers` — [`L259`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/graph_split.py#L259)
- uses (calls/refs, reference-scoped): [`model_spec`](../../../trainer.md#Trainer.Config.model_spec), [`model`](../../../protocols/model_spec.md#ModelSpec.model), [`gm`](../../graph_trainer/make_fx_tracer.md#TracedResult.gm), [`compile`](tpu_graph_trainer.md#TpuGraphTrainer.Config.compile), [`TpuGraphTrainer`](tpu_graph_trainer.md#TpuGraphTrainer), [`Config`](tpu_graph_trainer.md#TpuGraphTrainer.Config), [`example_inputs`](../../graph_trainer/make_fx_tracer.md#TracedResult.example_inputs), [`split_backward_graph_by_layer`](graph_split.md#split_backward_graph_by_layer), [`split_forward_backward_graph`](graph_split.md#split_forward_backward_graph), [`split_forward_graph_by_layer`](graph_split.md#split_forward_graph_by_layer), [`TracedResult`](../../graph_trainer/make_fx_tracer.md#TracedResult), [`graph_split`](config.md#TpuGraphTrainerCompileConfig.graph_split), [`thread_host_offload_donors`](split_cpu_offload.md#thread_host_offload_donors), [`module`](graph_split.md#PartitionedGraph.module), [`tpu_backend_compile_pass`](tpu_backend_pass.md#tpu_backend_compile_pass), [`fsdp_barrier_policy`](config.md#TpuGraphTrainerCompileConfig.fsdp_barrier_policy), [`module`](graph_split.md#SplitForwardBackwardGraph.module), [`backward_graph`](graph_split.md#SplitForwardBackwardGraph.backward_graph), [`forward_graph`](graph_split.md#SplitForwardBackwardGraph.forward_graph), [`backward_partition_mode`](config.md#GraphSplitterConfig.backward_partition_mode), [`tpu_backend_compile_partitioned_pass`](tpu_backend_pass.md#tpu_backend_compile_partitioned_pass), [`enabled`](config.md#GraphSplitterConfig.enabled), [`forward_layers_per_executable`](config.md#GraphSplitterConfig.forward_layers_per_executable), [`host_donor_specs`](graph_split.md#SplitForwardBackwardModule.host_donor_specs), [`backward_layers_per_executable`](config.md#GraphSplitterConfig.backward_layers_per_executable), [`cpu_offload_prefetch_executables`](config.md#GraphSplitterConfig.cpu_offload_prefetch_executables), [`forward_example_inputs`](graph_split.md#SplitForwardBackwardGraph.forward_example_inputs), [`precompile_artifact_dir`](../../graph_trainer/configs.md#GraphTrainerCompileConfig.precompile_artifact_dir), [`forward_graph`](graph_split.md#SplitForwardBackwardModule.forward_graph), [`GraphSplitterConfig`](config.md#GraphSplitterConfig), [`backward_example_inputs`](graph_split.md#SplitForwardBackwardGraph.backward_example_inputs), [`backward_graph`](graph_split.md#SplitForwardBackwardModule.backward_graph), [`host_donor_output_positions`](graph_split.md#SplitForwardBackwardModule.host_donor_output_positions), [`donate_internal_buffers`](config.md#GraphSplitterConfig.donate_internal_buffers), [`forward_isolate_prefix`](config.md#GraphSplitterConfig.forward_isolate_prefix)
- used by: [`_make_fx_forward_backward_step`](tpu_graph_trainer.md#TpuGraphTrainer._make_fx_forward_backward_step), [`_graph_splitter`](tpu_graph_trainer.md#TpuGraphTrainer._graph_splitter)  (6 test-only)

### <a id="PartitionedGraph"></a>`PartitionedGraph`
- def: [`torchtitan/experiments/tpu/graph_trainer/graph_split.py:246`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/graph_split.py#L246)
- signature: `class PartitionedGraph:`
- members:
  - <a id="PartitionedGraph.collective_layer_to_partition"></a>`collective_layer_to_partition` — [`L250`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/graph_split.py#L250)
  - <a id="PartitionedGraph.layer_to_partition"></a>`layer_to_partition` — [`L249`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/graph_split.py#L249)
  - <a id="PartitionedGraph.module"></a>`module` — [`L247`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/graph_split.py#L247)
  - <a id="PartitionedGraph.partition_map"></a>`partition_map` — [`L248`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/graph_split.py#L248)
- used by: [`split_and_compile`](graph_split.md#GraphSplitter.split_and_compile), [`split_backward_graph_by_layer`](graph_split.md#split_backward_graph_by_layer), [`split_forward_graph_by_layer`](graph_split.md#split_forward_graph_by_layer), [`_materialize_partitioned_graph`](graph_split.md#_materialize_partitioned_graph)  (6 test-only)

### <a id="SplitForwardBackwardGraph"></a>`SplitForwardBackwardGraph`
- def: [`torchtitan/experiments/tpu/graph_trainer/graph_split.py:236`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/graph_split.py#L236) — documented in [tpu-graph-trainer](../../../../../concepts/tpu-graph-trainer.md)
- signature: `class SplitForwardBackwardGraph:`
- members:
  - <a id="SplitForwardBackwardGraph.backward_example_inputs"></a>`backward_example_inputs` — [`L241`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/graph_split.py#L241)
  - <a id="SplitForwardBackwardGraph.backward_graph"></a>`backward_graph` — [`L239`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/graph_split.py#L239)
  - <a id="SplitForwardBackwardGraph.forward_example_inputs"></a>`forward_example_inputs` — [`L240`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/graph_split.py#L240)
  - <a id="SplitForwardBackwardGraph.forward_graph"></a>`forward_graph` — [`L238`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/graph_split.py#L238)
  - <a id="SplitForwardBackwardGraph.module"></a>`module` — [`L237`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/graph_split.py#L237)
  - <a id="SplitForwardBackwardGraph.residual_nodes"></a>`residual_nodes` — [`L242`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/graph_split.py#L242)
- uses (calls/refs, reference-scoped): [`SplitForwardBackwardModule`](graph_split.md#SplitForwardBackwardModule)
- used by: [`split_and_compile`](graph_split.md#GraphSplitter.split_and_compile), [`split_forward_backward_graph`](graph_split.md#split_forward_backward_graph)  (7 test-only)

### <a id="SplitForwardBackwardModule"></a>`SplitForwardBackwardModule`
- def: [`torchtitan/experiments/tpu/graph_trainer/graph_split.py:102`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/graph_split.py#L102)
- signature: `class SplitForwardBackwardModule(nn.Module):`
- members:
  - <a id="SplitForwardBackwardModule._initialize_host_donors"></a>`_initialize_host_donors(self, flat_program_inputs: tuple[Any, ...])` — [`L133`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/graph_split.py#L133) — Create one persistent pinned-host tensor per offloaded activation.
  - <a id="SplitForwardBackwardModule.forward"></a>`forward(self, *flat_inputs: Any)` — [`L185`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/graph_split.py#L185)
  - <a id="SplitForwardBackwardModule.backward_graph"></a>`backward_graph` — [`L120`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/graph_split.py#L120)
  - <a id="SplitForwardBackwardModule.backward_output_positions"></a>`backward_output_positions` — [`L122`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/graph_split.py#L122)
  - <a id="SplitForwardBackwardModule.constant_outputs"></a>`constant_outputs` — [`L123`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/graph_split.py#L123)
  - <a id="SplitForwardBackwardModule.forward_graph"></a>`forward_graph` — [`L119`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/graph_split.py#L119)
  - <a id="SplitForwardBackwardModule.forward_output_positions"></a>`forward_output_positions` — [`L121`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/graph_split.py#L121)
  - <a id="SplitForwardBackwardModule.host_donor_output_positions"></a>`host_donor_output_positions` — [`L128`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/graph_split.py#L128)
  - <a id="SplitForwardBackwardModule.host_donor_specs"></a>`host_donor_specs` — [`L127`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/graph_split.py#L127)
  - <a id="SplitForwardBackwardModule.num_direct_forward_outputs"></a>`num_direct_forward_outputs` — [`L124`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/graph_split.py#L124)
  - <a id="SplitForwardBackwardModule.num_outputs"></a>`num_outputs` — [`L126`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/graph_split.py#L126)
  - <a id="SplitForwardBackwardModule.num_residual_outputs"></a>`num_residual_outputs` — [`L125`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/graph_split.py#L125)
- protocol/private: <a id="SplitForwardBackwardModule.__init__"></a>`__init__`[`L104`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/graph_split.py#L104), <a id="SplitForwardBackwardModule._host_donors"></a>`_host_donors`[`L131`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/graph_split.py#L131)
- uses (calls/refs, reference-scoped): [`logger`](../../../tools/logging.md#logger), [`HostDonorSpec`](split_cpu_offload.md#HostDonorSpec), [`_enqueue_forward_graph_outputs`](graph_split.md#_enqueue_forward_graph_outputs), [`_as_tuple`](graph_split.md#_as_tuple), [`_synchronize_tpu`](graph_split.md#_synchronize_tpu), [`dtype`](split_cpu_offload.md#HostDonorSpec.dtype), [`initialize_pinned_host_buffer`](split_cpu_offload.md#initialize_pinned_host_buffer), [`shape`](split_cpu_offload.md#HostDonorSpec.shape), [`stride`](split_cpu_offload.md#HostDonorSpec.stride)
- used by: [`split_and_compile`](graph_split.md#GraphSplitter.split_and_compile), [`split_forward_backward_graph`](graph_split.md#split_forward_backward_graph), [`module`](graph_split.md#SplitForwardBackwardGraph.module)  (2 test-only)

## Functions
- <a id="_as_tuple"></a>`_as_tuple(value: Any)` — [`L94`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/graph_split.py#L94)
- <a id="_assign_partition"></a>`_assign_partition(partition_map: dict[torch.fx.Node, int], nodes: set[torch.fx.Node], partition: int, owner: str)` — [`L531`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/graph_split.py#L531)
- <a id="_body_nodes"></a>`_body_nodes(gm: torch.fx.GraphModule)` — [`L509`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/graph_split.py#L509)
- <a id="_collect_backward_fsdp_owners"></a>`_collect_backward_fsdp_owners(gm: torch.fx.GraphModule, *, n_layers: int, collective_chains: dict[torch.fx.Node, set[torch.fx.Node]])` — [`L804`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/graph_split.py#L804)
- <a id="_collect_collective_chains"></a>`_collect_collective_chains(gm: torch.fx.GraphModule)` — [`L432`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/graph_split.py#L432) — Collect indivisible collective and FSDP dtype-conversion chains.
- <a id="_collective_producer"></a>`_collective_producer(node: torch.fx.Node)` — [`L402`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/graph_split.py#L402)
- <a id="_enqueue_forward_graph_outputs"></a>`_enqueue_forward_graph_outputs(values: list[torch.Tensor])` — [`L88`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/graph_split.py#L88)
- <a id="_group_nodes_by_layer"></a>`_group_nodes_by_layer(nodes: list[torch.fx.Node], *, excluded: set[torch.fx.Node] | None = None)` — [`L517`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/graph_split.py#L517)
- <a id="_is_collective"></a>`_is_collective(node: torch.fx.Node)` — [`L415`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/graph_split.py#L415)
- <a id="_is_getitem"></a>`_is_getitem(node: torch.fx.Node)` — [`L395`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/graph_split.py#L395)
- <a id="_is_spmd_region_marker"></a>`_is_spmd_region_marker(node: torch.fx.Node, marker: str)` — [`L424`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/graph_split.py#L424)
- <a id="_materialize_partitioned_graph"></a>`_materialize_partitioned_graph(gm: torch.fx.GraphModule, partition_map: dict[torch.fx.Node, int], layer_nodes: dict[int, set[torch.fx.Node]], collective_layer_to_partition: dict[str, dict[int, int]] | None = None)` — [`L604`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/graph_split.py#L604)
- <a id="_order_child_boundaries"></a>`_order_child_boundaries(parent: torch.fx.GraphModule)` — [`L547`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/graph_split.py#L547) — Order each child's inputs by last read and outputs by first availability.
- <a id="_preserves_numel"></a>`_preserves_numel(view: torch.fx.Node)` — [`L648`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/graph_split.py#L648)
- <a id="_synchronize_tpu"></a>`_synchronize_tpu(values: list[torch.Tensor], *, wait: bool)` — [`L81`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/graph_split.py#L81) — Synchronize lazily so host-only graph-split tests need no TorchTPU.
- <a id="_validate_backward_partitions"></a>`_validate_backward_partitions(partition_map: dict[torch.fx.Node, int], collective_chains: dict[torch.fx.Node, set[torch.fx.Node]])` — [`L830`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/graph_split.py#L830)
- <a id="split_forward_backward_graph.add_forward_dependencies"></a>`add_forward_dependencies(node: torch.fx.Node)` — [`L1106`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/graph_split.py#L1106)
- <a id="split_backward_graph_by_layer.collective_partition"></a>`collective_partition(kind: str, layer_id: int)` — [`L930`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/graph_split.py#L930)
- <a id="split_forward_backward_graph.make_available_to_backward"></a>`make_available_to_backward(node: torch.fx.Node)` — [`L1036`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/graph_split.py#L1036)
- <a id="split_backward_graph_by_layer"></a>`split_backward_graph_by_layer(gm: torch.fx.GraphModule, *, n_layers: int, layers_per_executable: int = 1, pipeline_collectives: bool = False, cpu_offload_prefetch_executables: int = 0)` — [`L852`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/graph_split.py#L852) — Split backward by layer, optionally pipelining complete FSDP AG/RS pairs.
- <a id="split_forward_backward_graph"></a>`split_forward_backward_graph(gm: torch.fx.GraphModule, example_inputs: tuple[Any, ...])` — [`L1004`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/graph_split.py#L1004) — Partition a make_fx joint graph using ``autograd_backward`` metadata. — documented in [tpu-graph-trainer](../../../../../concepts/tpu-graph-trainer.md)
- <a id="split_forward_graph_by_layer"></a>`split_forward_graph_by_layer(gm: torch.fx.GraphModule, layers_per_executable: int, *, isolate_prefix: bool = False)` — [`L660`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/graph_split.py#L660) — Split forward into ascending, complete transformer-layer ranges.

## Module values
- <a id="__all__"></a>`__all__` — [`L1200`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/graph_split.py#L1200)

