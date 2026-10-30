---
title: 'Module: torchtitan/experiments/graph_trainer/deepseek_v3/parallelize_autoparallel.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/graph_trainer/deepseek_v3/parallelize_autoparallel.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.graph_trainer.deepseek_v3.parallelize_autoparallel`/
symbols:
  parallelize_autoparallel_deepseekv3: parallelize_autoparallel_deepseekv3().
  parallelize_autoparallel_deepseekv3.input_fn: parallelize_autoparallel_deepseekv3().input_fn().
  _preserve_moe_attributes: _preserve_moe_attributes().
  _preserve_moe_attributes.get_moe_modules: _preserve_moe_attributes().get_moe_modules().
  _load_autoparallel_dsv3_dependency: _load_autoparallel_dsv3_dependency().
  _set_torchtitan_fields: _set_torchtitan_fields().
---
# Module: [`torchtitan/experiments/graph_trainer/deepseek_v3/parallelize_autoparallel.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/deepseek_v3/parallelize_autoparallel.py)

## Functions
- <a id="_load_autoparallel_dsv3_dependency"></a>`_load_autoparallel_dsv3_dependency()` — [`L41`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/deepseek_v3/parallelize_autoparallel.py#L41) — Load the temporary AutoParallel DSv3 integration dependency.
- <a id="_preserve_moe_attributes"></a>`_preserve_moe_attributes(original_model, parallel_model)` — [`L66`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/deepseek_v3/parallelize_autoparallel.py#L66) — Preserve MoE attributes (moe_enabled, load_balance_coeff) from original.
- <a id="_set_torchtitan_fields"></a>`_set_torchtitan_fields(parallel_model)` — [`L58`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/deepseek_v3/parallelize_autoparallel.py#L58)
- <a id="_preserve_moe_attributes.get_moe_modules"></a>`get_moe_modules(model)` — [`L69`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/deepseek_v3/parallelize_autoparallel.py#L69)
- <a id="parallelize_autoparallel_deepseekv3.input_fn"></a>`input_fn()` — [`L163`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/deepseek_v3/parallelize_autoparallel.py#L163)
- <a id="parallelize_autoparallel_deepseekv3"></a>`parallelize_autoparallel_deepseekv3(model, *, parallel_dims: ParallelDims, training: TrainingConfig, parallelism: ParallelismConfig, compile_config: GraphTrainerCompileConfig, ac_config: ActivationCheckpointingConfig, dump_folder: str)` — [`L91`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/deepseek_v3/parallelize_autoparallel.py#L91) — Apply AutoParallelGraph SPMD sharding to DeepSeek V3. — documented in [graph-trainer](../../../../../concepts/graph-trainer.md)

