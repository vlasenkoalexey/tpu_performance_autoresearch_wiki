---
title: 'Module: torchtitan/models/gpt_oss/parallelize.py'
type: catalog
provenance: extracted
module: torchtitan/models/gpt_oss/parallelize.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.models.gpt_oss.parallelize`/
symbols:
  parallelize_gptoss: parallelize_gptoss().
  _raise_dynamo_recompile_limit: _raise_dynamo_recompile_limit().
  _has_sliding_window_attention: _has_sliding_window_attention().
---
# Module: [`torchtitan/models/gpt_oss/parallelize.py`](../../../../../../../raw/code/torchtitan/torchtitan/models/gpt_oss/parallelize.py)

## Functions
- <a id="_has_sliding_window_attention"></a>`_has_sliding_window_attention(model: GptOssModel)` — [`L46`](../../../../../../../raw/code/torchtitan/torchtitan/models/gpt_oss/parallelize.py#L46) — documented in [gpt-oss-model](../../../../concepts/gpt-oss-model.md)
- <a id="_raise_dynamo_recompile_limit"></a>`_raise_dynamo_recompile_limit(model: GptOssModel)` — [`L28`](../../../../../../../raw/code/torchtitan/torchtitan/models/gpt_oss/parallelize.py#L28) — documented in [gpt-oss-model](../../../../concepts/gpt-oss-model.md)
- <a id="parallelize_gptoss"></a>`parallelize_gptoss(model: GptOssModel, *, parallel_dims: ParallelDims, training: TrainingConfig, parallelism: ParallelismConfig, compile_config: CompileConfig, ac_config: ActivationCheckpointingConfig, dump_folder: str, skip_dp: bool = False)` — [`L58`](../../../../../../../raw/code/torchtitan/torchtitan/models/gpt_oss/parallelize.py#L58) — documented in [gpt-oss-model](../../../../concepts/gpt-oss-model.md)

