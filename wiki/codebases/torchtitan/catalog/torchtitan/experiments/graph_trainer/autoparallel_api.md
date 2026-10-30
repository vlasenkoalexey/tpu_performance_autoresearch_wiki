---
title: 'Module: torchtitan/experiments/graph_trainer/autoparallel_api.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/graph_trainer/autoparallel_api.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.graph_trainer.autoparallel_api`/
symbols:
  _wrap_autoparallel_output: _wrap_autoparallel_output().
  AutoParallelGraph.apply_placement_for_fx_module: AutoParallelGraph#apply_placement_for_fx_module().
  AutoParallelGraph.forward: AutoParallelGraph#forward().
  AutoParallelModelOutput: AutoParallelModelOutput#
  AutoParallelGraph: AutoParallelGraph#
  AutoParallelModelOutput.output_mesh: AutoParallelModelOutput#output_mesh.
  AutoParallelModelOutput.output_placements: AutoParallelModelOutput#output_placements.
  AutoParallelModelOutput.sharded_output_axis: AutoParallelModelOutput#sharded_output_axis.
  _local_tensor_with_autograd: _local_tensor_with_autograd().
  _get_raw_module_tensor: _get_raw_module_tensor().
  _contiguous_stride: _contiguous_stride().
---
# Module: [`torchtitan/experiments/graph_trainer/autoparallel_api.py`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/autoparallel_api.py)

## Classes
### <a id="AutoParallelGraph"></a>`AutoParallelGraph`
- def: [`torchtitan/experiments/graph_trainer/autoparallel_api.py:75`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/autoparallel_api.py#L75) — documented in [graph-trainer](../../../../concepts/graph-trainer.md)
- doc: AutoParallel variant for graph_trainer's `aot_fx_trace` pipeline.
- signature: `class AutoParallelGraph(AutoParallel):`
- members:
  - <a id="AutoParallelGraph.apply_placement_for_fx_module"></a>`apply_placement_for_fx_module(self, sharding_placement=None, *, compile_config: GraphTrainerCompileConfig, model_output: AutoParallelModelOutput | None = None)` — [`L78`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/autoparallel_api.py#L78) — Return an AOT-backed parallel module for graph_trainer tracing.
  - <a id="AutoParallelGraph.forward"></a>`forward(self, *args, **kwargs)` — [`L112`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/autoparallel_api.py#L112)
- uses (calls/refs, reference-scoped): [`GraphTrainerCompileConfig`](configs.md#GraphTrainerCompileConfig), [`_wrap_autoparallel_output`](autoparallel_api.md#_wrap_autoparallel_output), [`AutoParallelModelOutput`](autoparallel_api.md#AutoParallelModelOutput), [`_get_raw_module_tensor`](autoparallel_api.md#_get_raw_module_tensor), [`_local_tensor_with_autograd`](autoparallel_api.md#_local_tensor_with_autograd)
- used by: [`parallelize_autoparallel_deepseekv3`](deepseek_v3/parallelize_autoparallel.md#parallelize_autoparallel_deepseekv3), [`parallelize_autoparallel_llama`](llama3/parallelize_autoparallel.md#parallelize_autoparallel_llama)

### <a id="AutoParallelModelOutput"></a>`AutoParallelModelOutput`
- def: [`torchtitan/experiments/graph_trainer/autoparallel_api.py:24`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/autoparallel_api.py#L24)
- signature: `class AutoParallelModelOutput:`
- members:
  - <a id="AutoParallelModelOutput.output_mesh"></a>`output_mesh` — [`L25`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/autoparallel_api.py#L25)
  - <a id="AutoParallelModelOutput.output_placements"></a>`output_placements` — [`L26`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/autoparallel_api.py#L26)
  - <a id="AutoParallelModelOutput.sharded_output_axis"></a>`sharded_output_axis` — [`L27`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/autoparallel_api.py#L27)
- used by: [`parallelize_autoparallel_llama`](llama3/parallelize_autoparallel.md#parallelize_autoparallel_llama), [`_wrap_autoparallel_output`](autoparallel_api.md#_wrap_autoparallel_output), [`apply_placement_for_fx_module`](autoparallel_api.md#AutoParallelGraph.apply_placement_for_fx_module)

## Functions
- <a id="_contiguous_stride"></a>`_contiguous_stride(shape: torch.Size)` — [`L47`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/autoparallel_api.py#L47)
- <a id="_get_raw_module_tensor"></a>`_get_raw_module_tensor(module: nn.Module, fqn: str, *, is_buffer: bool)` — [`L34`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/autoparallel_api.py#L34)
- <a id="_local_tensor_with_autograd"></a>`_local_tensor_with_autograd(tensor: torch.Tensor)` — [`L30`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/autoparallel_api.py#L30)
- <a id="_wrap_autoparallel_output"></a>`_wrap_autoparallel_output(output: torch.Tensor, model_output: AutoParallelModelOutput | None)` — [`L56`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/autoparallel_api.py#L56)

