---
title: 'Module: torchtitan/experiments/tpu/graph_trainer/qwen3.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/graph_trainer/qwen3.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.graph_trainer.qwen3`/
symbols:
  parallelize_qwen3: parallelize_qwen3().
  to_graph_trainer_model_spec: to_graph_trainer_model_spec().
  model_registry: model_registry().
  with_maxtext_flops: with_maxtext_flops().
  MaxTextTpuGraphTrainerQwen3Model.Config: MaxTextTpuGraphTrainerQwen3Model#Config#
  MaxTextTpuGraphTrainerQwen3Model: MaxTextTpuGraphTrainerQwen3Model#
  MaxTextTpuGraphTrainerQwen3Model.Config.get_nparams_and_flops: MaxTextTpuGraphTrainerQwen3Model#Config#get_nparams_and_flops().
---
# Module: [`torchtitan/experiments/tpu/graph_trainer/qwen3.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/qwen3.py)

## Classes
### <a id="MaxTextTpuGraphTrainerQwen3Model"></a>`MaxTextTpuGraphTrainerQwen3Model`  ·  implements/extends GraphTrainerQwen3Model
- def: [`torchtitan/experiments/tpu/graph_trainer/qwen3.py:33`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/qwen3.py#L33)
- doc: GraphTrainer Qwen3 that reports MaxText FLOPs.
- signature: `class MaxTextTpuGraphTrainerQwen3Model(GraphTrainerQwen3Model):`
- uses (calls/refs, reference-scoped): [`GraphTrainerQwen3Model`](../../graph_trainer/qwen3/model.md#GraphTrainerQwen3Model)
- used by: [`GraphTrainerQwen3Model`](../../graph_trainer/qwen3/model.md#GraphTrainerQwen3Model), [`with_maxtext_flops`](qwen3.md#with_maxtext_flops)  (2 test-only)

### <a id="MaxTextTpuGraphTrainerQwen3Model.Config"></a>`MaxTextTpuGraphTrainerQwen3Model.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/tpu/graph_trainer/qwen3.py:42`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/qwen3.py#L42)
- signature: `class Config(GraphTrainerQwen3Model.Config):`
- members:
  - <a id="MaxTextTpuGraphTrainerQwen3Model.Config.get_nparams_and_flops"></a>`get_nparams_and_flops(self, model: nn.Module, seq_len: int)` — [`L43`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/qwen3.py#L43)
- uses (calls/refs, reference-scoped): [`get_maxtext_decoder_nparams_and_flops`](../mfu_flops.md#get_maxtext_decoder_nparams_and_flops), [`GraphTrainerQwen3Model`](../../graph_trainer/qwen3/model.md#GraphTrainerQwen3Model), [`Config`](../../graph_trainer/qwen3/model.md#GraphTrainerQwen3Model.Config)
- used by: [`with_maxtext_flops`](qwen3.md#with_maxtext_flops)  (2 test-only)

## Functions
- <a id="model_registry"></a>`model_registry(flavor: str)` — [`L85`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/qwen3.py#L85)
- <a id="parallelize_qwen3"></a>`parallelize_qwen3(model: GraphTrainerQwen3Model, *, training: TrainingConfig, parallel_dims: ParallelDims, **kwargs)` — [`L62`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/qwen3.py#L62) — Apply the TPU uneven-FSDP policy before setup.
- <a id="to_graph_trainer_model_spec"></a>`to_graph_trainer_model_spec(model_spec: ModelSpec)` — [`L92`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/qwen3.py#L92) — Convert an already-specialized Qwen spec to its TPU graph counterpart.
- <a id="with_maxtext_flops"></a>`with_maxtext_flops(config: GraphTrainerQwen3Model.Config)` — [`L49`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/qwen3.py#L49) — Return ``config`` unchanged except that it reports MaxText FLOPs.

