---
title: 'Module: torchtitan/experiments/graph_trainer/inductor_passes.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/graph_trainer/inductor_passes.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.graph_trainer.inductor_passes`/
symbols:
  regional_inductor_pass: regional_inductor_pass().
  full_inductor_compilation_pass: full_inductor_compilation_pass().
  standalone_inductor_compilation_pass: standalone_inductor_compilation_pass().
  annotate_flex_attention_for_regional_inductor_pass: annotate_flex_attention_for_regional_inductor_pass().
  _node_metadata_key_filter_distributed: _node_metadata_key_filter_distributed().
  _get_fake_mode_from_gm: _get_fake_mode_from_gm().
  _ops_filter_with_distributed: _ops_filter_with_distributed().
  _wrap_compiled_artifact_as_graph_module: _wrap_compiled_artifact_as_graph_module().
  _copy_graph_with_used_placeholders: _copy_graph_with_used_placeholders().
  _migrate_cpu_get_attrs_to_cuda: _migrate_cpu_get_attrs_to_cuda().
---
# Module: [`torchtitan/experiments/graph_trainer/inductor_passes.py`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/inductor_passes.py)

## Functions
- <a id="_copy_graph_with_used_placeholders"></a>`_copy_graph_with_used_placeholders(gm: torch.fx.GraphModule, example_inputs: tuple)` — [`L97`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/inductor_passes.py#L97)
- <a id="_get_fake_mode_from_gm"></a>`_get_fake_mode_from_gm(gm: torch.fx.GraphModule)` — [`L60`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/inductor_passes.py#L60)
- <a id="_migrate_cpu_get_attrs_to_cuda"></a>`_migrate_cpu_get_attrs_to_cuda(gm: torch.fx.GraphModule)` — [`L316`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/inductor_passes.py#L316) — Move CPU constant tensor get_attrs to CUDA so cudagraph capture works.
- <a id="_node_metadata_key_filter_distributed"></a>`_node_metadata_key_filter_distributed(key: str)` — [`L47`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/inductor_passes.py#L47) — Metadata key filter for regional_inductor with distributed ops.
- <a id="_ops_filter_with_distributed"></a>`_ops_filter_with_distributed(name: str)` — [`L26`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/inductor_passes.py#L26) — Ops filter that allows distributed collective ops for serialization.
- <a id="_wrap_compiled_artifact_as_graph_module"></a>`_wrap_compiled_artifact_as_graph_module(root: torch.fx.GraphModule, compiled_fn, used_placeholder_indices: list[int])` — [`L71`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/inductor_passes.py#L71)
- <a id="annotate_flex_attention_for_regional_inductor_pass"></a>`annotate_flex_attention_for_regional_inductor_pass(gm: torch.fx.GraphModule, example_inputs: tuple | None = None, *, flex_compile_config: dict | None, mask_compile_config: dict | None = None)` — [`L251`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/inductor_passes.py#L251) — Tag flex attention HOPs with compile_with_inductor for regional_inductor.
- <a id="full_inductor_compilation_pass"></a>`full_inductor_compilation_pass(gm: torch.fx.GraphModule, example_inputs: tuple, *, boxed_codegen: bool = False, inductor_configs=None)` — [`L329`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/inductor_passes.py#L329) — Compile the whole graph as one ``regional_inductor`` region.
- <a id="regional_inductor_pass"></a>`regional_inductor_pass(gm: torch.fx.GraphModule, example_inputs: tuple, *, serializable: bool = False, boxed_codegen: bool = False)` — [`L170`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/inductor_passes.py#L170) — Compile tagged graph regions with ``regional_inductor``.
- <a id="standalone_inductor_compilation_pass"></a>`standalone_inductor_compilation_pass(gm: torch.fx.GraphModule, example_inputs: tuple, *, inductor_configs=None)` — [`L124`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/inductor_passes.py#L124) — Compile the whole graph with one direct Inductor invocation.

