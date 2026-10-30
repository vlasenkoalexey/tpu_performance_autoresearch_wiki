---
title: 'Module: torchtitan/experiments/tpu/graph_trainer/tpu_backend_pass.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/graph_trainer/tpu_backend_pass.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.graph_trainer.tpu_backend_pass`/
symbols:
  construct_tpu_transform_passes: construct_tpu_transform_passes().
  _annotate_internal_donations: _annotate_internal_donations().
  construct_tpu_pass_pipeline: construct_tpu_pass_pipeline().
  tpu_backend_compile_pass: tpu_backend_compile_pass().
  tpu_backend_compile_partitioned_pass: tpu_backend_compile_partitioned_pass().
  _donatable_input_positions: _donatable_input_positions().
  _producer_output_storage: _producer_output_storage().
  register: register().
  PASS_PIPELINE_REGISTRY.PASS_PIPELINE_REGISTRY: PASS_PIPELINE_REGISTRY.PASS_PIPELINE_REGISTRY.
  _tensor_storage_id: _tensor_storage_id().
  _submodule_outputs: _submodule_outputs().
  _ensure_optimization_barrier_fake: _ensure_optimization_barrier_fake().
  tpu_backend_compile_partitioned_pass.compile_submodule: tpu_backend_compile_partitioned_pass().compile_submodule().
  tpu_backend_compile_pass._compiled_forward: tpu_backend_compile_pass()._compiled_forward().
  _import_static_compiler: _import_static_compiler().
  _optimization_barrier_fake: _optimization_barrier_fake().
  _restore_pinned_host_compile_inputs: _restore_pinned_host_compile_inputs().
  __all__: __all__.
---
# Module: [`torchtitan/experiments/tpu/graph_trainer/tpu_backend_pass.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tpu_backend_pass.py)

## Functions
- <a id="_annotate_internal_donations"></a>`_annotate_internal_donations(gm: torch.fx.GraphModule, *, donate_internal_buffers: bool = True)` — [`L186`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tpu_backend_pass.py#L186) — Annotate forced donors and safe last-use boundaries between children.
- <a id="tpu_backend_compile_pass._compiled_forward"></a>`_compiled_forward(*flat_inputs)` — [`L387`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tpu_backend_pass.py#L387)
- <a id="_donatable_input_positions"></a>`_donatable_input_positions(parent: torch.fx.GraphModule, call: torch.fx.Node, last_use_by_storage: dict[int, int], node_order: dict[torch.fx.Node, int], protected_storages: set[int])` — [`L141`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tpu_backend_pass.py#L141) — Select child inputs whose storage is dead after this parent-graph call.
- <a id="_ensure_optimization_barrier_fake"></a>`_ensure_optimization_barrier_fake()` — [`L81`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tpu_backend_pass.py#L81)
- <a id="_import_static_compiler"></a>`_import_static_compiler()` — [`L53`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tpu_backend_pass.py#L53) — Lazy import so this module is safe to import across environments.
- <a id="_optimization_barrier_fake"></a>`_optimization_barrier_fake(inputs: list[torch.Tensor])` — [`L59`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tpu_backend_pass.py#L59)
- <a id="_producer_output_storage"></a>`_producer_output_storage(parent: torch.fx.GraphModule, source: torch.fx.Node)` — [`L107`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tpu_backend_pass.py#L107) — Resolve a parent-graph value to the storage produced by a split child.
- <a id="_restore_pinned_host_compile_inputs"></a>`_restore_pinned_host_compile_inputs(gm: torch.fx.GraphModule, example_inputs: tuple)` — [`L400`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tpu_backend_pass.py#L400) — Represent AO host inputs as TPU tensors in PJRT pinned-host memory.
- <a id="_submodule_outputs"></a>`_submodule_outputs(submodule: torch.fx.GraphModule)` — [`L96`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tpu_backend_pass.py#L96)
- <a id="_tensor_storage_id"></a>`_tensor_storage_id(value: Any)` — [`L90`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tpu_backend_pass.py#L90)
- <a id="tpu_backend_compile_partitioned_pass.compile_submodule"></a>`compile_submodule(submodule: torch.fx.GraphModule, submodule_inputs: list[torch.Tensor], *, module_name: str | None = None)` — [`L484`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tpu_backend_pass.py#L484)
- <a id="construct_tpu_pass_pipeline"></a>`construct_tpu_pass_pipeline(traced_result: TracedResult, config: GraphTrainer.Config)` — [`L647`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tpu_backend_pass.py#L647) — Build the normal unsplit pipeline: joint transforms, then compilation. — documented in [tpu-graph-trainer](../../../../../concepts/tpu-graph-trainer.md)
- <a id="construct_tpu_transform_passes"></a>`construct_tpu_transform_passes(traced_result: TracedResult, config: GraphTrainer.Config)` — [`L523`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tpu_backend_pass.py#L523) — Build transforms that must run on the complete joint FX graph. — documented in [graph-trainer](../../../../../concepts/graph-trainer.md)
- <a id="register"></a>`register()` — [`L664`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tpu_backend_pass.py#L664) — Ensure the 'tpu' pipeline is registered.
- <a id="tpu_backend_compile_partitioned_pass"></a>`tpu_backend_compile_partitioned_pass(gm: torch.fx.GraphModule, example_inputs: tuple, *, is_fwd: bool = True, donate_internal_buffers: bool = False)` — [`L462`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tpu_backend_pass.py#L462) — Discover child inputs and compile each split GraphModule independently.
- <a id="tpu_backend_compile_pass"></a>`tpu_backend_compile_pass(gm: torch.fx.GraphModule, example_inputs: tuple, *, is_fwd: bool = True, donated_input_positions: tuple[int, ...] = ())` — [`L298`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tpu_backend_pass.py#L298) — Terminal pass in the TPU graph pipeline: lowers gm into a static XLA binary.

## Module values
- <a id="PASS_PIPELINE_REGISTRY.PASS_PIPELINE_REGISTRY"></a>`PASS_PIPELINE_REGISTRY` — [`L659`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tpu_backend_pass.py#L659)
- <a id="__all__"></a>`__all__` — [`L669`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tpu_backend_pass.py#L669)

