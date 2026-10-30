---
title: 'Module: torchtitan/experiments/tpu/transformers_modeling_backend/parallelize.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/transformers_modeling_backend/parallelize.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.transformers_modeling_backend.parallelize`/
symbols:
  parallelize_hf_transformers_tpu: parallelize_hf_transformers_tpu().
  _defer_parametrization_during_init: _defer_parametrization_during_init().
  _defer_parametrization_during_init.init_states: _defer_parametrization_during_init().init_states().
---
# Module: [`torchtitan/experiments/tpu/transformers_modeling_backend/parallelize.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/parallelize.py)

## Functions
- <a id="_defer_parametrization_during_init"></a>`_defer_parametrization_during_init(model: nn.Module)` — [`L44`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/parallelize.py#L44) — Let the HF backend tie its weights after SimpleFSDP has wrapped it.
- <a id="_defer_parametrization_during_init.init_states"></a>`init_states(*args, **kwargs)` — [`L65`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/parallelize.py#L65)
- <a id="parallelize_hf_transformers_tpu"></a>`parallelize_hf_transformers_tpu(model: nn.Module, *, parallel_dims: torchtitan.distributed.ParallelDims, training: torchtitan.config.TrainingConfig, parallelism: torchtitan.config.ParallelismConfig, compile_config: torchtitan.config.CompileConfig, ac_config, dump_folder: str, tpu_compile_mode: str = "layer", **kwargs)` — [`L72`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/parallelize.py#L72) — Apply TP/AC/compile via the backend, then SimpleFSDP data parallelism.

