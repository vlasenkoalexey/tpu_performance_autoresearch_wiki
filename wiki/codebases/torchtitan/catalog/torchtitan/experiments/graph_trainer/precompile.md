---
title: 'Module: torchtitan/experiments/graph_trainer/precompile.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/graph_trainer/precompile.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.graph_trainer.precompile`/
symbols:
  compute_config_fingerprint: compute_config_fingerprint().
  PrecompiledFxTraceArtifact.to_traced_result: PrecompiledFxTraceArtifact#to_traced_result().
  PrecompiledFxTraceArtifact.from_traced_result: PrecompiledFxTraceArtifact#from_traced_result().
  precompile_fx_trace_load: precompile_fx_trace_load().
  precompile_fx_trace_save: precompile_fx_trace_save().
  get_spmd_precompile_meshes: get_spmd_precompile_meshes().
  flatten_runtime_inputs: flatten_runtime_inputs().
  PrecompiledFxTraceArtifact: PrecompiledFxTraceArtifact#
  ConfigFingerprint: ConfigFingerprint.
  _FX_TRACE_ARTIFACT_KEY: _FX_TRACE_ARTIFACT_KEY.
  PrecompiledFxTraceArtifact.config_fingerprint: PrecompiledFxTraceArtifact#config_fingerprint.
  _validate_config_fingerprint: _validate_config_fingerprint().
  PrecompiledFxTraceArtifact.input_subclass_layouts: PrecompiledFxTraceArtifact#input_subclass_layouts.
  PrecompiledFxTraceArtifact.output_subclass_layouts: PrecompiledFxTraceArtifact#output_subclass_layouts.
  PrecompiledFxTraceArtifact.serialized_gm: PrecompiledFxTraceArtifact#serialized_gm.
  PrecompiledFxTraceArtifact.state_fqns: PrecompiledFxTraceArtifact#state_fqns.
  PrecompiledFxTraceArtifact.num_flat_inputs: PrecompiledFxTraceArtifact#num_flat_inputs.
  _register_coor_ops: _register_coor_ops().
  PrecompiledFxTraceArtifact.num_flat_outputs: PrecompiledFxTraceArtifact#num_flat_outputs.
  PrecompiledFxTraceArtifact.output_spec: PrecompiledFxTraceArtifact#output_spec.
  PrecompiledFxTraceArtifact.tensor_input_indices: PrecompiledFxTraceArtifact#tensor_input_indices.
  PrecompiledFxTraceArtifact.num_optimizer_state_inputs: PrecompiledFxTraceArtifact#num_optimizer_state_inputs.
  PrecompiledFxTraceArtifact.num_runtime_mesh_inputs: PrecompiledFxTraceArtifact#num_runtime_mesh_inputs.
---
# Module: [`torchtitan/experiments/graph_trainer/precompile.py`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/precompile.py)

## Classes
### <a id="PrecompiledFxTraceArtifact"></a>`PrecompiledFxTraceArtifact`
- def: [`torchtitan/experiments/graph_trainer/precompile.py:191`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/precompile.py#L191) — documented in [graph-trainer](../../../../concepts/graph-trainer.md)
- doc: Serialized form of a TracedResult for aot_fx_trace precompilation.
- signature: `class PrecompiledFxTraceArtifact:`
- members:
  - <a id="PrecompiledFxTraceArtifact.from_traced_result"></a>`from_traced_result(cls, traced_result: TracedResult, config_fingerprint: ConfigFingerprint | None = None)` — [`L221`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/precompile.py#L221) — Create an artifact from a TracedResult by serializing its GraphModule. — documented in [graph-trainer](../../../../concepts/graph-trainer.md)
  - <a id="PrecompiledFxTraceArtifact.to_traced_result"></a>`to_traced_result(self, example_inputs: tuple[Any, ...])` — [`L268`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/precompile.py#L268) — Deserialize back into a TracedResult.
  - <a id="PrecompiledFxTraceArtifact.config_fingerprint"></a>`config_fingerprint` — [`L215`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/precompile.py#L215)
  - <a id="PrecompiledFxTraceArtifact.input_subclass_layouts"></a>`input_subclass_layouts` — [`L205`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/precompile.py#L205)
  - <a id="PrecompiledFxTraceArtifact.num_flat_inputs"></a>`num_flat_inputs` — [`L204`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/precompile.py#L204)
  - <a id="PrecompiledFxTraceArtifact.num_flat_outputs"></a>`num_flat_outputs` — [`L206`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/precompile.py#L206)
  - <a id="PrecompiledFxTraceArtifact.num_optimizer_state_inputs"></a>`num_optimizer_state_inputs` — [`L217`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/precompile.py#L217)
  - <a id="PrecompiledFxTraceArtifact.num_runtime_mesh_inputs"></a>`num_runtime_mesh_inputs` — [`L218`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/precompile.py#L218)
  - <a id="PrecompiledFxTraceArtifact.output_spec"></a>`output_spec` — [`L208`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/precompile.py#L208)
  - <a id="PrecompiledFxTraceArtifact.output_subclass_layouts"></a>`output_subclass_layouts` — [`L207`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/precompile.py#L207)
  - <a id="PrecompiledFxTraceArtifact.serialized_gm"></a>`serialized_gm` — [`L202`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/precompile.py#L202)
  - <a id="PrecompiledFxTraceArtifact.state_fqns"></a>`state_fqns` — [`L203`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/precompile.py#L203)
  - <a id="PrecompiledFxTraceArtifact.tensor_input_indices"></a>`tensor_input_indices` — [`L209`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/precompile.py#L209)
- uses (calls/refs, reference-scoped): [`gm`](make_fx_tracer.md#TracedResult.gm), [`example_inputs`](make_fx_tracer.md#TracedResult.example_inputs), [`TracedResult`](make_fx_tracer.md#TracedResult), [`SubclassLayout`](make_fx_tracer.md#SubclassLayout), [`output_subclass_layouts`](make_fx_tracer.md#TracedResult.output_subclass_layouts), [`graph_state`](make_fx_tracer.md#TracedResult.graph_state), [`state_fqns`](make_fx_tracer.md#TracedResult.state_fqns), [`input_subclass_layouts`](make_fx_tracer.md#TracedResult.input_subclass_layouts), [`ConfigFingerprint`](precompile.md#ConfigFingerprint), [`mappings`](make_fx_tracer.md#GraphStateSpec.mappings), [`num_flat_outputs`](make_fx_tracer.md#TracedResult.num_flat_outputs), [`output_spec`](make_fx_tracer.md#TracedResult.output_spec), [`user_inputs_spec`](make_fx_tracer.md#TracedResult.user_inputs_spec), [`num_runtime_mesh_inputs`](make_fx_tracer.md#TracedResult.num_runtime_mesh_inputs), [`tensor_input_indices`](make_fx_tracer.md#TracedResult.tensor_input_indices), [`num_flat_inputs`](make_fx_tracer.md#TracedResult.num_flat_inputs), [`num_optimizer_state_inputs`](make_fx_tracer.md#TracedResult.num_optimizer_state_inputs), [`_node_metadata_key_filter_distributed`](inductor_passes.md#_node_metadata_key_filter_distributed), [`_register_coor_ops`](precompile.md#_register_coor_ops)
- used by: [`precompile_fx_trace_load`](precompile.md#precompile_fx_trace_load), [`precompile_fx_trace_save`](precompile.md#precompile_fx_trace_save)  (5 test-only)

## Functions
- <a id="_register_coor_ops"></a>`_register_coor_ops()` — [`L128`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/precompile.py#L128) — Register CooR custom ops required for tracing and deserialization.
- <a id="_validate_config_fingerprint"></a>`_validate_config_fingerprint(artifact_fingerprint: ConfigFingerprint, expected_fingerprint: ConfigFingerprint)` — [`L145`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/precompile.py#L145) — Validate that artifact and current config fingerprints match.
- <a id="compute_config_fingerprint"></a>`compute_config_fingerprint(model: torch.nn.Module, compile_config: GraphTrainerCompileConfig, parallel_dims: ParallelDims)` — [`L73`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/precompile.py#L73) — Compute a fingerprint that captures everything affecting the compiled output: — documented in [graph-trainer](../../../../concepts/graph-trainer.md)
- <a id="flatten_runtime_inputs"></a>`flatten_runtime_inputs(module: torch.nn.Module, args: tuple[Any, ...], kwargs: dict[str, Any], precompile_meshes: list[DeviceMesh] | None = None)` — [`L37`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/precompile.py#L37) — Flatten live model state, meshes, and call inputs for a precompiled graph.
- <a id="get_spmd_precompile_meshes"></a>`get_spmd_precompile_meshes(parallel_dims: ParallelDims)` — [`L53`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/precompile.py#L53) — Return SPMD meshes that must be registered as runtime graph inputs.
- <a id="precompile_fx_trace_load"></a>`precompile_fx_trace_load(storage: StorageAdapter, expected_fingerprint: ConfigFingerprint, example_inputs: tuple[Any, ...])` — [`L335`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/precompile.py#L335) — Load a precompiled aot_fx_trace artifact.
- <a id="precompile_fx_trace_save"></a>`precompile_fx_trace_save(traced_result: TracedResult, storage: StorageAdapter, config_fingerprint: ConfigFingerprint | None = None)` — [`L308`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/precompile.py#L308) — Serialize a traced and compiled FX graph artifact and save it.

## Module values
- <a id="ConfigFingerprint"></a>`ConfigFingerprint` — [`L34`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/precompile.py#L34)
- <a id="_FX_TRACE_ARTIFACT_KEY"></a>`_FX_TRACE_ARTIFACT_KEY` — [`L187`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/precompile.py#L187)

