---
title: 'Module: torchtitan/experiments/tpu/layer_loop.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/layer_loop.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.layer_loop`/
symbols:
  builds_layer_loop: builds_layer_loop().
  tpu_model_class: tpu_model_class().
  TpuLayerLoop: TpuLayerLoop#
  _forward: _forward().
  runs_layer_loop: runs_layer_loop().
  TpuLayerLoop.forward: TpuLayerLoop#forward().
  model_subclass: model_subclass().
  __all__: __all__.
---
# Module: [`torchtitan/experiments/tpu/layer_loop.py`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/layer_loop.py)

## Classes
### <a id="TpuLayerLoop"></a>`TpuLayerLoop`  ·  implements/extends ModuleDict
- def: [`torchtitan/experiments/tpu/layer_loop.py:33`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/layer_loop.py#L33) — documented in [tpu-layer-loop-remat-and-layouts](../../../../concepts/tpu-layer-loop-remat-and-layouts.md)
- doc: `model.layers`, as a container that runs its own layers.
- signature: `class TpuLayerLoop(ModuleDict):`
- members:
  - <a id="TpuLayerLoop.forward"></a>`forward(self, h: torch.Tensor, *args)` — [`L41`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/layer_loop.py#L41)
- uses (calls/refs, reference-scoped): [`ModuleDict`](../../protocols/module.md#ModuleDict), [`StackedLayers`](graph_trainer/layer_stack.md#StackedLayers), [`forward`](graph_trainer/layer_stack.md#StackedLayers.forward)  (2 test-only)
- used by: [`ModuleDict`](../../protocols/module.md#ModuleDict), [`_forward`](layer_loop.md#_forward), [`StackedLayers`](graph_trainer/layer_stack.md#StackedLayers)  (3 test-only)

## Functions
- <a id="_forward"></a>`_forward(self, tokens: torch.Tensor, positions: torch.Tensor | None = None, attention_masks: AttentionMasksType | None = None)` — [`L47`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/layer_loop.py#L47) — Runs the decoder: embeddings, the layers, the final norm, the LM head.
- <a id="builds_layer_loop"></a>`builds_layer_loop(model_config: Decoder.Config)` — [`L92`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/layer_loop.py#L92) — Whether ``model_config.build()`` would satisfy :func:`runs_layer_loop`. — documented in [tpu-layer-loop-remat-and-layouts](../../../../concepts/tpu-layer-loop-remat-and-layouts.md)
- <a id="model_subclass"></a>`model_subclass(model_cls: type, config_cls: type, name: str, *, config_body: dict | None = None, **body)` — [`L100`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/layer_loop.py#L100) — Subclasses ``model_cls``, giving the subclass a ``Config`` of its own.
- <a id="runs_layer_loop"></a>`runs_layer_loop(model: torch.nn.Module)` — [`L87`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/layer_loop.py#L87) — Whether ``model`` hands its layers to ``model.layers`` to run. — documented in [tpu-layer-loop-remat-and-layouts](../../../../concepts/tpu-layer-loop-remat-and-layouts.md)
- <a id="tpu_model_class"></a>`tpu_model_class(config_cls: type)` — [`L127`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/layer_loop.py#L127) — Builds the ``Tpu<Model>`` subclass whose ``forward`` is ``_forward``.

## Module values
- <a id="__all__"></a>`__all__` — [`L24`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/layer_loop.py#L24)

