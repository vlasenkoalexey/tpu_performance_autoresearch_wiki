---
title: 'Module: torchtitan/experiments/tpu/graph_trainer/layer_stack.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/graph_trainer/layer_stack.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.graph_trainer.layer_stack`/
symbols:
  LayerStack.run: LayerStack#run().
  _apply_stacked_layers: _apply_stacked_layers().
  LayerStack._attach_views: LayerStack#_attach_views().
  LayerStack.unregister_and_allocate: LayerStack#unregister_and_allocate().
  LayerStack.install: LayerStack#install().
  with_tpu_stacked_layers: with_tpu_stacked_layers().
  check_layers_are_stackable: check_layers_are_stackable().
  STACK_ATTR: STACK_ATTR.
  LayerStack._drop_views: LayerStack#_drop_views().
  LayerStack.scan_body: LayerStack#scan_body().
  _mangle: _mangle().
  LayerStackHolder.layer_shapes: LayerStackHolder#layer_shapes.
  LayerStackHolder: LayerStackHolder#
  LayerStack.holder: LayerStack#holder.
  LayerStackHolder.flatten_for: LayerStackHolder#flatten_for().
  _stacked_model_class: _stacked_model_class().
  LayerStackHolder.plan_shard_dims: LayerStackHolder#plan_shard_dims().
  LayerStackHolder.as_layer_shape: LayerStackHolder#as_layer_shape().
  LayerStack.names: LayerStack#names.
  LayerStack._slots: LayerStack#_slots().
  StackedLayers: StackedLayers#
  StackedLayers.forward: StackedLayers#forward().
  LayerStack.unrolled: LayerStack#unrolled().
  LayerStack.fsdp_plan: LayerStack#fsdp_plan.
  LayerStackHolder.split_meshes: LayerStackHolder#split_meshes.
  LayerStackHolder.build_split_meshes: LayerStackHolder#build_split_meshes().
  LayerStack._unregistered: LayerStack#_unregistered.
  LayerStack._views_attached: LayerStack#_views_attached.
  LayerStack.attach: LayerStack#attach().
  LayerStack.drop: LayerStack#drop().
  LayerStack.layers: LayerStack#layers.
  LayerStack: LayerStack#
  LayerStack.init_states: LayerStack#init_states().
  _stacked_model_class.__init__: _stacked_model_class().__init__().
  _stacked_model_class.get_nparams_and_flops: _stacked_model_class().get_nparams_and_flops().
  _shard_dim: _shard_dim().
  LayerStack.n_layers: LayerStack#n_layers.
  LayerStack._hidden: LayerStack#_hidden.
  LayerStack._views: LayerStack#_views.
  StackedLayers.__init__: StackedLayers#__init__().
  LayerStack.__init__: LayerStack#__init__().
  check_layers_are_stackable.spec: check_layers_are_stackable().spec().
  LayerStackHolder.can_flatten: LayerStackHolder#can_flatten().
  StackedLayers.use_scan: StackedLayers#use_scan.
  LayerStack.body: LayerStack#body().
  LayerStackHolder._fsdp_shard_dim: LayerStackHolder#_fsdp_shard_dim.
  StackedLayers.stack: StackedLayers#stack.
  __all__: __all__.
  LayerStackHolder.__init__: LayerStackHolder#__init__().
---
# Module: [`torchtitan/experiments/tpu/graph_trainer/layer_stack.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/layer_stack.py)

## Classes
### <a id="LayerStack"></a>`LayerStack`
- def: [`torchtitan/experiments/tpu/graph_trainer/layer_stack.py:393`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/layer_stack.py#L393) — documented in [tpu-graph-trainer](../../../../../concepts/tpu-graph-trainer.md)
- members:
  - <a id="LayerStack._attach_views"></a>`_attach_views(self)` — [`L495`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/layer_stack.py#L495) — Put the per-layer names back, each aliasing its row of a stack.
  - <a id="LayerStack._drop_views"></a>`_drop_views(self)` — [`L529`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/layer_stack.py#L529) — Exact inverse of ``_attach_views``.
  - <a id="LayerStack._slots"></a>`_slots(self)` — [`L421`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/layer_stack.py#L421) — Every per-layer parameter, as (row, FQN, owning module, attribute).
  - <a id="LayerStack.attach"></a>`attach(*args)` — [`L580`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/layer_stack.py#L580)
  - <a id="LayerStack.body"></a>`body(carry, params)` — [`L667`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/layer_stack.py#L667)
  - <a id="LayerStack.drop"></a>`drop(*args)` — [`L583`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/layer_stack.py#L583)
  - <a id="LayerStack.init_states"></a>`init_states(**kwargs)` — [`L576`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/layer_stack.py#L576)
  - <a id="LayerStack.install"></a>`install(self, model: nn.Module, *, use_scan: bool)` — [`L552`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/layer_stack.py#L552) — Attach the stack to the model, at the end of its ``__init__``.
  - <a id="LayerStack.run"></a>`run(self, h: torch.Tensor, *args, use_scan: bool)` — [`L625`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/layer_stack.py#L625) — Run the layers out of the stacks, one at a time or as one ``scan``.
  - <a id="LayerStack.scan_body"></a>`scan_body(carry, slices)` — [`L716`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/layer_stack.py#L716)
  - <a id="LayerStack.unregister_and_allocate"></a>`unregister_and_allocate(self)` — [`L441`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/layer_stack.py#L441) — Replace each *kind* of per-layer weight with one stacked tensor.
  - <a id="LayerStack.unrolled"></a>`unrolled(self)` — [`L481`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/layer_stack.py#L481) — Make the model look unstacked for the duration of a block.
  - <a id="LayerStack.fsdp_plan"></a>`fsdp_plan` — [`L419`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/layer_stack.py#L419)
  - <a id="LayerStack.holder"></a>`holder` — [`L405`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/layer_stack.py#L405)
  - <a id="LayerStack.layers"></a>`layers` — [`L403`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/layer_stack.py#L403)
  - <a id="LayerStack.n_layers"></a>`n_layers` — [`L406`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/layer_stack.py#L406)
  - <a id="LayerStack.names"></a>`names` — [`L408`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/layer_stack.py#L408)
- protocol/private: <a id="LayerStack.__init__"></a>`__init__`[`L402`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/layer_stack.py#L402), <a id="LayerStack._hidden"></a>`_hidden`[`L414`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/layer_stack.py#L414), <a id="LayerStack._unregistered"></a>`_unregistered`[`L410`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/layer_stack.py#L410), <a id="LayerStack._views"></a>`_views`[`L415`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/layer_stack.py#L415), <a id="LayerStack._views_attached"></a>`_views_attached`[`L411`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/layer_stack.py#L411)
- uses (calls/refs, reference-scoped): [`logger`](../../../tools/logging.md#logger), [`plan_stacked_gathers`](scan_fsdp.md#plan_stacked_gathers), [`gather_slice`](scan_fsdp.md#gather_slice), [`check_layers_are_stackable`](layer_stack.md#check_layers_are_stackable), [`_mangle`](layer_stack.md#_mangle), [`layer_shapes`](layer_stack.md#LayerStackHolder.layer_shapes), [`LayerStackHolder`](layer_stack.md#LayerStackHolder), [`scan_body_remat_window`](scan_remat_policy.md#scan_body_remat_window), [`runs_layer_loop`](../layer_loop.md#runs_layer_loop), [`ScanFSDPSpec`](scan_fsdp.md#ScanFSDPSpec), [`as_layer_shape`](layer_stack.md#LayerStackHolder.as_layer_shape), [`StackedLayers`](layer_stack.md#StackedLayers)
- used by: [`_apply_stacked_layers`](layer_stack.md#_apply_stacked_layers), [`forward`](layer_stack.md#StackedLayers.forward), [`__init__`](layer_stack.md#StackedLayers.__init__)  (1 test-only)

### <a id="LayerStackHolder"></a>`LayerStackHolder`  ·  implements/extends Module
- def: [`torchtitan/experiments/tpu/graph_trainer/layer_stack.py:184`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/layer_stack.py#L184)
- doc: `model.layer_stacks`: the stacks, and nothing else.
- signature: `class LayerStackHolder(Module):`
- members:
  - <a id="LayerStackHolder.as_layer_shape"></a>`as_layer_shape(self, name: str, layer: torch.Tensor)` — [`L323`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/layer_stack.py#L323) — Returns ``layer``, one layer of stack ``name``, in its original shape.
  - <a id="LayerStackHolder.build_split_meshes"></a>`build_split_meshes(self)` — [`L299`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/layer_stack.py#L299) — Creates the meshes ``as_layer_shape`` uses.
  - <a id="LayerStackHolder.can_flatten"></a>`can_flatten(dim1_len: int, dim2_len: int)` — [`L241`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/layer_stack.py#L241)
  - <a id="LayerStackHolder.flatten_for"></a>`flatten_for(self, degree: int)` — [`L212`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/layer_stack.py#L212) — Flattens axes 1 and 2 of stacks that can't be sharded evenly on axis 1.
  - <a id="LayerStackHolder.plan_shard_dims"></a>`plan_shard_dims(self, degree: int)` — [`L286`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/layer_stack.py#L286) — Returns the axis ``apply_simple_fsdp`` shards each stack on.
  - <a id="LayerStackHolder.layer_shapes"></a>`layer_shapes` — [`L207`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/layer_stack.py#L207)
  - <a id="LayerStackHolder.split_meshes"></a>`split_meshes` — [`L210`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/layer_stack.py#L210)
- protocol/private: <a id="LayerStackHolder.__init__"></a>`__init__`[`L203`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/layer_stack.py#L203), <a id="LayerStackHolder._fsdp_shard_dim"></a>`_fsdp_shard_dim`[`L201`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/layer_stack.py#L201)
- uses (calls/refs, reference-scoped): [`logger`](../../../tools/logging.md#logger), [`Module`](../../../protocols/module.md#Module), [`_shard_dim`](layer_stack.md#_shard_dim)
- used by: [`Module`](../../../protocols/module.md#Module), [`run`](layer_stack.md#LayerStack.run), [`_apply_stacked_layers`](layer_stack.md#_apply_stacked_layers), [`_attach_views`](layer_stack.md#LayerStack._attach_views), [`__init__`](layer_stack.md#LayerStack.__init__)  (9 test-only)

### <a id="StackedLayers"></a>`StackedLayers`  ·  implements/extends TpuLayerLoop
- def: [`torchtitan/experiments/tpu/graph_trainer/layer_stack.py:374`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/layer_stack.py#L374) — documented in [tpu-graph-trainer](../../../../../concepts/tpu-graph-trainer.md)
- doc: `model.layers`, running its layers out of the stacks.
- signature: `class StackedLayers(TpuLayerLoop):`
- members:
  - <a id="StackedLayers.forward"></a>`forward(self, h: torch.Tensor, *args)` — [`L389`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/layer_stack.py#L389)
  - <a id="StackedLayers.stack"></a>`stack` — [`L386`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/layer_stack.py#L386)
  - <a id="StackedLayers.use_scan"></a>`use_scan` — [`L387`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/layer_stack.py#L387)
- protocol/private: <a id="StackedLayers.__init__"></a>`__init__`[`L384`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/layer_stack.py#L384)
- uses (calls/refs, reference-scoped): [`run`](layer_stack.md#LayerStack.run), [`TpuLayerLoop`](../layer_loop.md#TpuLayerLoop), [`LayerStack`](layer_stack.md#LayerStack)
- used by: [`install`](layer_stack.md#LayerStack.install), [`TpuLayerLoop`](../layer_loop.md#TpuLayerLoop), [`check_scan_was_applied`](scan_guards.md#check_scan_was_applied), [`forward`](../layer_loop.md#TpuLayerLoop.forward)  (1 test-only)

## Functions
- <a id="_stacked_model_class.__init__"></a>`__init__(self, *args, **kwargs)` — [`L851`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/layer_stack.py#L851)
- <a id="_apply_stacked_layers"></a>`_apply_stacked_layers(model: nn.Module, *, use_scan: bool)` — [`L765`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/layer_stack.py#L765) — Stack the decoder layers' weights, and with ``use_scan`` run them as one.
- <a id="_mangle"></a>`_mangle(name: str)` — [`L93`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/layer_stack.py#L93)
- <a id="_shard_dim"></a>`_shard_dim(param: torch.Tensor, degree: int)` — [`L156`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/layer_stack.py#L156) — Which axis of one stack `degree` ranks should split it on.
- <a id="_stacked_model_class"></a>`_stacked_model_class(config_cls: type, use_scan: bool)` — [`L840`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/layer_stack.py#L840) — Build the ``Stacked<Model>`` subclass that stacks itself on construction.
- <a id="check_layers_are_stackable"></a>`check_layers_are_stackable(layers: nn.ModuleDict)` — [`L97`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/layer_stack.py#L97) — Every layer must match layer 0, or they cannot share a stack.
- <a id="_stacked_model_class.get_nparams_and_flops"></a>`get_nparams_and_flops(self, model: nn.Module, seq_len: int)` — [`L855`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/layer_stack.py#L855) — Count on the unstacked model this config describes.
- <a id="check_layers_are_stackable.spec"></a>`spec(layer: nn.Module)` — [`L112`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/layer_stack.py#L112)
- <a id="with_tpu_stacked_layers"></a>`with_tpu_stacked_layers(model_config: Decoder.Config, *, use_scan: bool)` — [`L884`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/layer_stack.py#L884) — Put ``model_config`` on a model that arrives already stacked.

## Module values
- <a id="STACK_ATTR"></a>`STACK_ATTR` — [`L88`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/layer_stack.py#L88)
- <a id="__all__"></a>`__all__` — [`L78`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/layer_stack.py#L78)

