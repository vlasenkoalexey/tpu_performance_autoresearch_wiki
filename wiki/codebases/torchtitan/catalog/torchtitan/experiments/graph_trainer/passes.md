---
title: 'Module: torchtitan/experiments/graph_trainer/passes.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/graph_trainer/passes.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.graph_trainer.passes`/
symbols:
  compile_time_passes: compile_time_passes().
  apply_graph_passes: apply_graph_passes().
  final_inductor_compile_passes: final_inductor_compile_passes().
  construct_default_graph_passes: construct_default_graph_passes().
  async_tensor_parallel_pass: async_tensor_parallel_pass().
  _filter_disabled_passes: _filter_disabled_passes().
  construct_mandatory_graph_passes: construct_mandatory_graph_passes().
  _get_pass_name: _get_pass_name().
  c10d: c10d.
  _tensor_parallel_degree: _tensor_parallel_degree().
---
# Module: [`torchtitan/experiments/graph_trainer/passes.py`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/passes.py)

## Functions
- <a id="_filter_disabled_passes"></a>`_filter_disabled_passes(passes: list[Callable], disable_names: list[str])` — [`L469`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/passes.py#L469) — Remove passes whose names exactly match any entry in ``disable_names``.
- <a id="_get_pass_name"></a>`_get_pass_name(pass_fn: Callable)` — [`L461`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/passes.py#L461)
- <a id="_tensor_parallel_degree"></a>`_tensor_parallel_degree(config, parallel_dims=None)` — [`L138`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/passes.py#L138) — Return TP degree from ``ParallelDims`` when available, else config.
- <a id="apply_graph_passes"></a>`apply_graph_passes(gm: torch.fx.GraphModule, example_inputs: tuple, passes: list[Callable], *, compile_config: GraphTrainerCompileConfig | None = None, respect_disable_passes: bool = True)` — [`L487`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/passes.py#L487) — Apply graph passes to the traced fwd+bwd graph.
- <a id="async_tensor_parallel_pass"></a>`async_tensor_parallel_pass(gm: torch.fx.GraphModule, example_inputs: tuple)` — [`L100`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/passes.py#L100) — Pipeline TP collectives with matmuls via symmetric memory.
- <a id="compile_time_passes"></a>`compile_time_passes(traced_result: TracedResult, config: GraphTrainer.Config, *, use_cudagraph: bool = False, parallel_dims=None, include_inductor: bool = True, include_mandatory_normalization: bool = True)` — [`L150`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/passes.py#L150) — Cleanup, FlexInnerAttention annotation, and regional_inductor passes.
- <a id="construct_default_graph_passes"></a>`construct_default_graph_passes(traced_result: TracedResult, config: GraphTrainer.Config, *, parallel_dims=None)` — [`L420`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/passes.py#L420) — Build the pass list for the aot_fx_trace path.
- <a id="construct_mandatory_graph_passes"></a>`construct_mandatory_graph_passes()` — [`L145`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/passes.py#L145) — Return correctness passes that run even when optional passes are disabled.
- <a id="final_inductor_compile_passes"></a>`final_inductor_compile_passes(compile_config: GraphTrainerCompileConfig, *, use_cudagraph: bool = False, boxed_codegen: bool = False)` — [`L362`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/passes.py#L362) — Return the terminal Inductor passes for a traced graph.

## Module values
- <a id="c10d"></a>`c10d` — [`L97`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/passes.py#L97)

