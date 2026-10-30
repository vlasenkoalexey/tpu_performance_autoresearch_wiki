---
title: 'Module: torchtitan/experiments/graph_trainer/custom_codegen.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/graph_trainer/custom_codegen.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.graph_trainer.custom_codegen`/
symbols:
  _CodegenGraphModule._setup_custom_codegen: _CodegenGraphModule#_setup_custom_codegen().
  _CodegenGraphModule._code_path: _CodegenGraphModule#_code_path.
  _CodegenGraphModule._subgraph_modules: _CodegenGraphModule#_subgraph_modules.
  _CodegenGraphModule._generate_wrapper_code: _CodegenGraphModule#_generate_wrapper_code().
  _CodegenGraphModule._generate_profiled_forward: _CodegenGraphModule#_generate_profiled_forward().
  _CodegenGraphModule._reload_forward_from_disk: _CodegenGraphModule#_reload_forward_from_disk().
  _CodegenGraphModule._check_file_modified: _CodegenGraphModule#_check_file_modified().
  custom_codegen_pass: custom_codegen_pass().
  _CodegenGraphModule.forward: _CodegenGraphModule#forward.
  _CodegenGraphModule: _CodegenGraphModule#
  _CodegenGraphModule._code_mtime: _CodegenGraphModule#_code_mtime.
  _CodegenGraphModule._generate_subgraph_functions: _CodegenGraphModule#_generate_subgraph_functions().
  _CodegenGraphModule._get_profiler_label: _CodegenGraphModule#_get_profiler_label().
  _CodegenGraphModule.collect_nodes: _CodegenGraphModule#collect_nodes().
  _CodegenGraphModule._compute_hash: _CodegenGraphModule#_compute_hash().
  _CodegenGraphModule._get_graph_module_code: _CodegenGraphModule#_get_graph_module_code().
  _CodegenGraphModule._code_hash: _CodegenGraphModule#_code_hash.
  _CodegenGraphModule._python_code_globals: _CodegenGraphModule#_python_code_globals.
  _CodegenGraphModule._format_args_tuple: _CodegenGraphModule#_format_args_tuple().
  _CodegenGraphModule._trace_structured_codegen: _CodegenGraphModule#_trace_structured_codegen().
  _CodegenGraphModule.forward_wrapper: _CodegenGraphModule#forward_wrapper().
  _CodegenGraphModule.__getstate__: _CodegenGraphModule#__getstate__().
  _CodegenGraphModule._extract_imports: _CodegenGraphModule#_extract_imports().
  _CodegenGraphModule._write_code_atomically: _CodegenGraphModule#_write_code_atomically().
  _CodegenGraphModule._get_rank_suffix: _CodegenGraphModule#_get_rank_suffix().
  _CodegenGraphModule._codegen_dir: _CodegenGraphModule#_codegen_dir.
  _CodegenGraphModule._custom_codegen_initialized: _CodegenGraphModule#_custom_codegen_initialized.
  _CodegenGraphModule._root: _CodegenGraphModule#_root.
  _CodegenGraphModule._find_forward_boundaries: _CodegenGraphModule#_find_forward_boundaries().
  _CodegenGraphModule._get_op_name: _CodegenGraphModule#_get_op_name().
  _CodegenGraphModule._get_stack_trace_summary: _CodegenGraphModule#_get_stack_trace_summary().
  _CodegenGraphModule.__init__: _CodegenGraphModule#__init__().
  _CodegenGraphModule.recompile: _CodegenGraphModule#recompile().
---
# Module: [`torchtitan/experiments/graph_trainer/custom_codegen.py`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/custom_codegen.py)

## Classes
### <a id="_CodegenGraphModule"></a>`_CodegenGraphModule`
- def: [`torchtitan/experiments/graph_trainer/custom_codegen.py:24`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/custom_codegen.py#L24)
- doc: GraphModule that saves generated code to disk with two-path profiling support.
- signature: `class _CodegenGraphModule(torch.fx.GraphModule):`
- members:
  - <a id="_CodegenGraphModule.__getstate__"></a>`__getstate__(self)` — [`L558`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/custom_codegen.py#L558) — When pickling we just pickle the underlying root module since it's
  - <a id="_CodegenGraphModule._check_file_modified"></a>`_check_file_modified(self)` — [`L530`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/custom_codegen.py#L530) — Check if the code file has been modified since last load.
  - <a id="_CodegenGraphModule._compute_hash"></a>`_compute_hash(content: str)` — [`L42`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/custom_codegen.py#L42) — Compute SHA256 hash of content for change detection.
  - <a id="_CodegenGraphModule._extract_imports"></a>`_extract_imports(self, code: str)` — [`L130`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/custom_codegen.py#L130) — Extract import statements from code.
  - <a id="_CodegenGraphModule._find_forward_boundaries"></a>`_find_forward_boundaries(self, code: str)` — [`L138`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/custom_codegen.py#L138) — Use AST to find forward function's start and end line numbers.
  - <a id="_CodegenGraphModule._format_args_tuple"></a>`_format_args_tuple(self, args: tuple)` — [`L375`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/custom_codegen.py#L375) — Prepare args as a tuple expression for _RecordFunctionFast.
  - <a id="_CodegenGraphModule._generate_profiled_forward"></a>`_generate_profiled_forward(self, code: str | None = None, graph: torch.fx.Graph | None = None)` — [`L284`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/custom_codegen.py#L284) — Generate _forward_profiled with _RecordFunctionFast wrapping each op.
  - <a id="_CodegenGraphModule._generate_subgraph_functions"></a>`_generate_subgraph_functions(self, subgraph_name: str, subgraph: torch.fx.GraphModule)` — [`L237`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/custom_codegen.py#L237) — Generate module-level functions for a subgraph module.
  - <a id="_CodegenGraphModule._generate_wrapper_code"></a>`_generate_wrapper_code(self)` — [`L156`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/custom_codegen.py#L156) — Generate wrapper code with dual-path profiling.
  - <a id="_CodegenGraphModule._get_graph_module_code"></a>`_get_graph_module_code(gm: torch.fx.GraphModule)` — [`L79`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/custom_codegen.py#L79) — Extract source code from a GraphModule.
  - <a id="_CodegenGraphModule._get_op_name"></a>`_get_op_name(self, node: torch.fx.Node)` — [`L357`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/custom_codegen.py#L357) — Extract readable operation name from node.
  - <a id="_CodegenGraphModule._get_profiler_label"></a>`_get_profiler_label(self, node: torch.fx.Node)` — [`L367`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/custom_codegen.py#L367) — Generate profiler label: 'node_name: op_name (file:line)'.
  - <a id="_CodegenGraphModule._get_rank_suffix"></a>`_get_rank_suffix()` — [`L72`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/custom_codegen.py#L72) — Returns rank suffix for distributed setups, empty string otherwise.
  - <a id="_CodegenGraphModule._get_stack_trace_summary"></a>`_get_stack_trace_summary(self, node: torch.fx.Node)` — [`L394`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/custom_codegen.py#L394) — Extract filename:line from node stack trace for profiling labels.
  - <a id="_CodegenGraphModule._reload_forward_from_disk"></a>`_reload_forward_from_disk(self)` — [`L458`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/custom_codegen.py#L458) — Load or reload the forward method from disk file.
  - <a id="_CodegenGraphModule._setup_custom_codegen"></a>`_setup_custom_codegen(self)` — [`L418`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/custom_codegen.py#L418) — Generate code, save to disk, and load forward method.
  - <a id="_CodegenGraphModule._trace_structured_codegen"></a>`_trace_structured_codegen(self, code: str)` — [`L443`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/custom_codegen.py#L443) — Send generated code to tlparse via trace_structured.
  - <a id="_CodegenGraphModule._write_code_atomically"></a>`_write_code_atomically(path: str, content: str)` — [`L49`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/custom_codegen.py#L49) — Atomically write to avoid race conditions in distributed setups.
  - <a id="_CodegenGraphModule.collect_nodes"></a>`collect_nodes(item)` — [`L379`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/custom_codegen.py#L379) — Recursively collect fx.Node names from nested structures.
  - <a id="_CodegenGraphModule.forward_wrapper"></a>`forward_wrapper(self, *args, **kwargs)` — [`L503`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/custom_codegen.py#L503)
  - <a id="_CodegenGraphModule.recompile"></a>`recompile(self)` — [`L554`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/custom_codegen.py#L554) — Recompile graph from IR.
  - <a id="_CodegenGraphModule.forward"></a>`forward` — [`L513`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/custom_codegen.py#L513)
- protocol/private: <a id="_CodegenGraphModule.__init__"></a>`__init__`[`L98`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/custom_codegen.py#L98), <a id="_CodegenGraphModule._code_hash"></a>`_code_hash`[`L109`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/custom_codegen.py#L109), <a id="_CodegenGraphModule._code_mtime"></a>`_code_mtime`[`L495`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/custom_codegen.py#L495), <a id="_CodegenGraphModule._code_path"></a>`_code_path`[`L108`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/custom_codegen.py#L108), <a id="_CodegenGraphModule._codegen_dir"></a>`_codegen_dir`[`L107`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/custom_codegen.py#L107), <a id="_CodegenGraphModule._custom_codegen_initialized"></a>`_custom_codegen_initialized`[`L111`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/custom_codegen.py#L111), <a id="_CodegenGraphModule._python_code_globals"></a>`_python_code_globals`[`L110`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/custom_codegen.py#L110), <a id="_CodegenGraphModule._root"></a>`_root`[`L128`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/custom_codegen.py#L128), <a id="_CodegenGraphModule._subgraph_modules"></a>`_subgraph_modules`[`L112`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/custom_codegen.py#L112)
- uses (calls/refs, reference-scoped): [`logger`](../../tools/logging.md#logger)
- used by: [`custom_codegen_pass`](custom_codegen.md#custom_codegen_pass)  (4 test-only)

## Functions
- <a id="custom_codegen_pass"></a>`custom_codegen_pass(gm: torch.fx.GraphModule, example_inputs: list[Any] | None = None, *, codegen_dir: str | None = None)` — [`L564`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/custom_codegen.py#L564) — Save generated code to disk with dual-path profiling.

