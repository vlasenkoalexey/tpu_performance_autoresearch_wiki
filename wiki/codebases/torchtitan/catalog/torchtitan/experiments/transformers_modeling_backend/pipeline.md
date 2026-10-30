---
title: 'Module: torchtitan/experiments/transformers_modeling_backend/pipeline.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/transformers_modeling_backend/pipeline.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.transformers_modeling_backend.pipeline`/
symbols:
  pipeline_hf_transformers: pipeline_hf_transformers().
  pipeline_module_split._build_stage_from_modules: pipeline_module_split()._build_stage_from_modules().
  pipeline_module_split: pipeline_module_split().
  generate_llm_fqn_per_model_part: generate_llm_fqn_per_model_part().
  pipeline_module_split._get_stage_indices: pipeline_module_split()._get_stage_indices().
---
# Module: [`torchtitan/experiments/transformers_modeling_backend/pipeline.py`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/pipeline.py)

## Functions
- <a id="pipeline_module_split._build_stage_from_modules"></a>`_build_stage_from_modules(stage_idx: int, module_names: list[str], num_stages: int)` — [`L191`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/pipeline.py#L191)
- <a id="pipeline_module_split._get_stage_indices"></a>`_get_stage_indices()` — [`L253`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/pipeline.py#L253) — Compute the stage ids for the stages that will run on this pp rank
- <a id="generate_llm_fqn_per_model_part"></a>`generate_llm_fqn_per_model_part(num_stages: int, num_layers: int, input_weight: int = 1, output_weight: int = 1)` — [`L39`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/pipeline.py#L39) — Programmatically generates module names model part, focused on LLMs models.
- <a id="pipeline_hf_transformers"></a>`pipeline_hf_transformers(model: nn.Module, parallel_dims: ParallelDims, *, training: TrainingConfig, parallelism: ParallelismConfig, compile_config: CompileConfig, ac_config: ActivationCheckpointingConfig, dump_folder: str, device: torch.device, model_config: BaseModel.Config, parallelize_fn: ParallelizeFunction, loss_fn: LossFunction)` — [`L290`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/pipeline.py#L290)
- <a id="pipeline_module_split"></a>`pipeline_module_split(whole_model: nn.Module, pp_mesh: DeviceMesh, pp_schedule: str, device: torch.device, module_names_per_stage: list[list[str]], get_mesh: Callable | None = None)` — [`L148`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/pipeline.py#L148) — This API creates pipeline stages based on specified module names for each stage.

