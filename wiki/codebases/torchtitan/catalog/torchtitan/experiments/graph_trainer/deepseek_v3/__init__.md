---
title: 'Module: torchtitan/experiments/graph_trainer/deepseek_v3/__init__.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/graph_trainer/deepseek_v3/__init__.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.graph_trainer.deepseek_v3`/
symbols:
  model_registry: model_registry().
  _parallelize_fn: _parallelize_fn().
  _post_optimizer_build_fn: _post_optimizer_build_fn().
---
# Module: [`torchtitan/experiments/graph_trainer/deepseek_v3/__init__.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/deepseek_v3/__init__.py)

## Functions
- <a id="_parallelize_fn"></a>`_parallelize_fn(model, *, compile_config, **kwargs)` — [`L21`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/deepseek_v3/__init__.py#L21)
- <a id="_post_optimizer_build_fn"></a>`_post_optimizer_build_fn(optimizers, model_parts, parallel_dims)` — [`L31`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/deepseek_v3/__init__.py#L31) — Register MoE load-balancing and aux-loss step pre-hooks.
- <a id="model_registry"></a>`model_registry(flavor: str, *, seq_len: int | None = None, attn_backend: str = "flex", moe_comm_backend: str = "standard", non_blocking_capacity_factor: float | None = None)` — [`L37`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/deepseek_v3/__init__.py#L37)

