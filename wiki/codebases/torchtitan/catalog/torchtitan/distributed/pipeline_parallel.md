---
title: 'Module: torchtitan/distributed/pipeline_parallel.py'
type: catalog
provenance: extracted
module: torchtitan/distributed/pipeline_parallel.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.distributed.pipeline_parallel`/
symbols:
  pipeline_llm: pipeline_llm().
  pipeline_with_first_stage_modules: pipeline_with_first_stage_modules().
  _get_pipeline_metadata: _get_pipeline_metadata().
  _build_pipeline_schedule: _build_pipeline_schedule().
  _build_get_mesh_callback: _build_get_mesh_callback().
  _pipeline_module_split: _pipeline_module_split().
  _split_module: _split_module().
  _generate_llm_fqn_per_model_part: _generate_llm_fqn_per_model_part().
  _build_get_mesh_callback._get_mesh: _build_get_mesh_callback()._get_mesh().
  _get_pp_rank_to_stage_indices_mapping: _get_pp_rank_to_stage_indices_mapping().
  _build_pipeline_schedule._scalar_loss_fn: _build_pipeline_schedule()._scalar_loss_fn().
  __all__: __all__.
---
# Module: [`torchtitan/distributed/pipeline_parallel.py`](../../../../../../raw/code/torchtitan/torchtitan/distributed/pipeline_parallel.py)

## Functions
- <a id="_build_get_mesh_callback"></a>`_build_get_mesh_callback(parallel_dims: ParallelDims)` — [`L41`](../../../../../../raw/code/torchtitan/torchtitan/distributed/pipeline_parallel.py#L41) — Build a callback that resolves a DeviceMesh from dimension names.
- <a id="_build_pipeline_schedule"></a>`_build_pipeline_schedule(*, parallelism: ParallelismConfig, num_microbatches: int, stages: list[PipelineStage], loss_fn: Callable, backward_requires_autograd: bool = True)` — [`L267`](../../../../../../raw/code/torchtitan/torchtitan/distributed/pipeline_parallel.py#L267) — Builds a pipeline schedule for the given job configuration and stages.
- <a id="_generate_llm_fqn_per_model_part"></a>`_generate_llm_fqn_per_model_part(num_stages: int, num_layers: int, input_weight: int = 1, output_weight: int = 1)` — [`L357`](../../../../../../raw/code/torchtitan/torchtitan/distributed/pipeline_parallel.py#L357) — Programmatically generates module names per model part, focused on LLM models.
- <a id="_build_get_mesh_callback._get_mesh"></a>`_get_mesh(mesh_dim_names: tuple[str, ...], mesh_layout: _MeshLayout | None)` — [`L54`](../../../../../../raw/code/torchtitan/torchtitan/distributed/pipeline_parallel.py#L54)
- <a id="_get_pipeline_metadata"></a>`_get_pipeline_metadata(parallel_dims: ParallelDims, parallelism: ParallelismConfig, model_config: BaseModel.Config)` — [`L194`](../../../../../../raw/code/torchtitan/torchtitan/distributed/pipeline_parallel.py#L194) — Determine the number of virtual stages and the number of layers in the model. — documented in [parallel-dims-and-parallelization](../../../concepts/parallel-dims-and-parallelization.md)
- <a id="_get_pp_rank_to_stage_indices_mapping"></a>`_get_pp_rank_to_stage_indices_mapping(pp_rank: int, pp_degree, pp_schedule: str, num_stages: int)` — [`L532`](../../../../../../raw/code/torchtitan/torchtitan/distributed/pipeline_parallel.py#L532) — Returns a mapping from PP rank to stage indices for the given pipeline schedule.
- <a id="_pipeline_module_split"></a>`_pipeline_module_split(whole_model: nn.Module, pp_mesh: DeviceMesh, pp_schedule: str, device: torch.device, module_names_per_stage: list[list[str]], get_mesh: Callable | None = None)` — [`L572`](../../../../../../raw/code/torchtitan/torchtitan/distributed/pipeline_parallel.py#L572) — Create pipeline stages based on specified module names for each stage.
- <a id="_build_pipeline_schedule._scalar_loss_fn"></a>`_scalar_loss_fn(*args: object, **kwargs: object)` — [`L318`](../../../../../../raw/code/torchtitan/torchtitan/distributed/pipeline_parallel.py#L318)
- <a id="_split_module"></a>`_split_module(whole_model: nn.Module, module_names: list[str])` — [`L470`](../../../../../../raw/code/torchtitan/torchtitan/distributed/pipeline_parallel.py#L470) — Splits a whole model into a module based on the specified module names.
- <a id="pipeline_llm"></a>`pipeline_llm(model: nn.Module, *, parallel_dims: ParallelDims, training: TrainingConfig, parallelism: ParallelismConfig, compile_config: CompileConfig, ac_config: ActivationCheckpointingConfig, dump_folder: str, device: torch.device, model_config: BaseModel.Config, parallelize_fn: ParallelizeFunction, loss_fn: LossFunction)` — [`L65`](../../../../../../raw/code/torchtitan/torchtitan/distributed/pipeline_parallel.py#L65) — documented in [parallel-dims-and-parallelization](../../../concepts/parallel-dims-and-parallelization.md)
- <a id="pipeline_with_first_stage_modules"></a>`pipeline_with_first_stage_modules(model: nn.Module, *, first_stage_module_fqns: Sequence[str], parallel_dims: ParallelDims, parallelism: ParallelismConfig, model_config: BaseModel.Config, **kwargs)` — [`L144`](../../../../../../raw/code/torchtitan/torchtitan/distributed/pipeline_parallel.py#L144) — Co-locate additional model modules with the first pipeline stage. — documented in [parallel-dims-and-parallelization](../../../concepts/parallel-dims-and-parallelization.md)

## Module values
- <a id="__all__"></a>`__all__` — [`L38`](../../../../../../raw/code/torchtitan/torchtitan/distributed/pipeline_parallel.py#L38)

