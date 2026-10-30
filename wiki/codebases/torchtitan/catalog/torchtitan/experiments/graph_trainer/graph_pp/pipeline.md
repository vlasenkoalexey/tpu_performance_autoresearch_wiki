---
title: 'Module: torchtitan/experiments/graph_trainer/graph_pp/pipeline.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/graph_trainer/graph_pp/pipeline.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.graph_trainer.graph_pp.pipeline`/
symbols:
  graph_pipeline_llm: graph_pipeline_llm().
  _validate_graph_pp_config: _validate_graph_pp_config().
---
# Module: [`torchtitan/experiments/graph_trainer/graph_pp/pipeline.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/pipeline.py)

## Functions
- <a id="_validate_graph_pp_config"></a>`_validate_graph_pp_config(*, compile_config: GraphTrainerCompileConfig, parallelism: ParallelismConfig)` — [`L40`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/pipeline.py#L40)
- <a id="graph_pipeline_llm"></a>`graph_pipeline_llm(model: nn.Module, *, parallel_dims: ParallelDims, training: TrainingConfig, parallelism: ParallelismConfig, compile_config: GraphTrainerCompileConfig, ac_config: ActivationCheckpointingConfig, dump_folder: str, device: torch.device, model_config: BaseModel.Config, parallelize_fn: ParallelizeFunction, loss_fn: LossFunction)` — [`L66`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/pipeline.py#L66) — Build a GraphPP pipeline schedule for GraphTrainer. — documented in [graph-trainer](../../../../../concepts/graph-trainer.md)

