---
title: 'Module: torchtitan/experiments/tpu/model_annotator.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/model_annotator.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.model_annotator`/
symbols:
  wrap_model: wrap_model().
  wrap_model.make_pre_hook: wrap_model().make_pre_hook().
  wrap_model.make_post_hook: wrap_model().make_post_hook().
  wrap_model.make_pre_hook.pre_hook: wrap_model().make_pre_hook().pre_hook().
  wrap_model.make_post_hook.post_hook: wrap_model().make_post_hook().post_hook().
---
# Module: [`torchtitan/experiments/tpu/model_annotator.py`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/model_annotator.py)

## Functions
- <a id="wrap_model.make_post_hook"></a>`make_post_hook()` — [`L28`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/model_annotator.py#L28)
- <a id="wrap_model.make_pre_hook"></a>`make_pre_hook(mod_name, scope)` — [`L19`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/model_annotator.py#L19)
- <a id="wrap_model.make_post_hook.post_hook"></a>`post_hook(mod, *args)` — [`L29`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/model_annotator.py#L29)
- <a id="wrap_model.make_pre_hook.pre_hook"></a>`pre_hook(mod, *args)` — [`L20`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/model_annotator.py#L20)
- <a id="wrap_model"></a>`wrap_model(model: torch.nn.Module)` — [`L7`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/model_annotator.py#L7) — Wraps all submodules with hooks to add JAX profiler annotations.

