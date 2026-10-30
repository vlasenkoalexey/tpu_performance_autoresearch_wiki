---
title: 'Module: torchtitan/experiments/graph_trainer/graph_utils.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/graph_trainer/graph_utils.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.graph_trainer.graph_utils`/
symbols:
  CompiledModule.forward: CompiledModule#forward().
  joint_graph_builder: joint_graph_builder().
  CompiledModule.inner: CompiledModule#inner.
  CompiledModule._overrides: CompiledModule#_overrides.
  export_joint: export_joint().
  CompiledModule.__getattr__: CompiledModule#__getattr__().
  CompiledModule.joint_graph_module: CompiledModule#joint_graph_module.
  CompiledModule: CompiledModule#
  CompiledModule.__init__: CompiledModule#__init__().
  CompiledModule.__setattr__: CompiledModule#__setattr__().
  CompiledModule.__delattr__: CompiledModule#__delattr__().
  CompiledModule.init_states: CompiledModule#init_states().
  CompiledModule.state_dict: CompiledModule#state_dict().
  CompiledModule.load_state_dict: CompiledModule#load_state_dict().
  CompiledModule.named_parameters: CompiledModule#named_parameters().
  CompiledModule.parameters: CompiledModule#parameters().
  CompiledModule.precompiled_fn: CompiledModule#precompiled_fn.
  aot_export_joint_with_descriptors_alone: aot_export_joint_with_descriptors_alone().
  joint_graph_builder.wrapper_fn: joint_graph_builder().wrapper_fn().
  CompiledModule.parallel_dims: CompiledModule#parallel_dims.
  CompiledModule.joint_graph_builder: CompiledModule#joint_graph_builder.
  CompiledModule.parallelize_inputs: CompiledModule#parallelize_inputs.
---
# Module: [`torchtitan/experiments/graph_trainer/graph_utils.py`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_utils.py)

## Classes
### <a id="CompiledModule"></a>`CompiledModule`  ·  implements/extends Module
- def: [`torchtitan/experiments/graph_trainer/graph_utils.py:173`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_utils.py#L173) — documented in [graph-trainer](../../../../concepts/graph-trainer.md)
- signature: `class CompiledModule(Module):`
- members:
  - <a id="CompiledModule.forward"></a>`forward(self, *args, **kwargs)` — [`L241`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_utils.py#L241)
  - <a id="CompiledModule.init_states"></a>`init_states(self, *, buffer_device: torch.device | None = None)` — [`L218`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_utils.py#L218)
  - <a id="CompiledModule.load_state_dict"></a>`load_state_dict(self, *args, **kwargs)` — [`L232`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_utils.py#L232)
  - <a id="CompiledModule.named_parameters"></a>`named_parameters(self, *args, **kwargs)` — [`L235`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_utils.py#L235)
  - <a id="CompiledModule.parameters"></a>`parameters(self, *args, **kwargs)` — [`L238`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_utils.py#L238)
  - <a id="CompiledModule.state_dict"></a>`state_dict(self, *args, **kwargs)` — [`L229`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_utils.py#L229)
  - <a id="CompiledModule.inner"></a>`inner` — [`L184`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_utils.py#L184)
  - <a id="CompiledModule.joint_graph_builder"></a>`joint_graph_builder` — [`L187`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_utils.py#L187)
  - <a id="CompiledModule.joint_graph_module"></a>`joint_graph_module` — [`L188`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_utils.py#L188)
  - <a id="CompiledModule.parallel_dims"></a>`parallel_dims` — [`L185`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_utils.py#L185)
  - <a id="CompiledModule.parallelize_inputs"></a>`parallelize_inputs` — [`L191`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_utils.py#L191)
  - <a id="CompiledModule.precompiled_fn"></a>`precompiled_fn` — [`L189`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_utils.py#L189)
- protocol/private: <a id="CompiledModule.__delattr__"></a>`__delattr__`[`L212`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_utils.py#L212), <a id="CompiledModule.__getattr__"></a>`__getattr__`[`L195`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_utils.py#L195), <a id="CompiledModule.__init__"></a>`__init__`[`L174`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_utils.py#L174), <a id="CompiledModule.__setattr__"></a>`__setattr__`[`L206`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_utils.py#L206), <a id="CompiledModule._overrides"></a>`_overrides`[`L193`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_utils.py#L193)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`ParallelDims`](../../distributed/parallel_dims.md#ParallelDims)
- used by: [`Module`](../../protocols/module.md#Module), [`init_states`](../../protocols/module.md#Module.init_states)

## Functions
- <a id="aot_export_joint_with_descriptors_alone"></a>`aot_export_joint_with_descriptors_alone(model, args, kwargs=None)` — [`L80`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_utils.py#L80) — Export joint forward-backward graph with AOT Autograd.
- <a id="export_joint"></a>`export_joint(model, args, kwargs=None, dump_folder: str | None = None, precompile: bool = False)` — [`L32`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_utils.py#L32) — Export joint forward-backward graph with AOT Autograd.
- <a id="joint_graph_builder"></a>`joint_graph_builder(model: torch.nn.Module, model_args: tuple, model_kwargs: dict, fw_compiler: Callable | None = None, bw_compiler: Callable | None = None, joint_custom_passes: list[Callable] | None = None, dump_folder: str | None = None, compile_config: CompileConfig | None = None, serializable: bool = False, on_compile: Callable[[Any, TreeSpec | None], None] | None = None)` — [`L104`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_utils.py#L104) — Build a joint forward-backward graph for the model with optional custom compilers.
- <a id="joint_graph_builder.wrapper_fn"></a>`wrapper_fn(args, kwargs)` — [`L161`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_utils.py#L161)

