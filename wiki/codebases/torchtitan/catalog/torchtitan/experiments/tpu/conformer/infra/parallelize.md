---
title: 'Module: torchtitan/experiments/tpu/conformer/infra/parallelize.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/conformer/infra/parallelize.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.conformer.infra.parallelize`/
symbols:
  parallelize_conformer: parallelize_conformer().
  _determine_parallel_strategy: _determine_parallel_strategy().
  apply_compile: apply_compile().
  ParallelStrategy: ParallelStrategy#
  apply_ac: apply_ac().
  ParallelStrategy.SIMPLEFSDP: ParallelStrategy#SIMPLEFSDP.
  ParallelStrategy.DDP: ParallelStrategy#DDP.
  ParallelStrategy.DDP_W_SIMPLEFSDP: ParallelStrategy#DDP_W_SIMPLEFSDP.
  ParallelStrategy.FSDP2: ParallelStrategy#FSDP2.
  ParallelStrategy.DDP_W_FSDP2: ParallelStrategy#DDP_W_FSDP2.
  ParallelStrategy.NONE: ParallelStrategy#NONE.
---
# Module: [`torchtitan/experiments/tpu/conformer/infra/parallelize.py`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/conformer/infra/parallelize.py)

## Classes
### <a id="ParallelStrategy"></a>`ParallelStrategy`  ·  implements/extends Enum
- def: [`torchtitan/experiments/tpu/conformer/infra/parallelize.py:17`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/conformer/infra/parallelize.py#L17)
- signature: `class ParallelStrategy(enum.Enum):`
- members:
  - <a id="ParallelStrategy.DDP"></a>`DDP` — [`L22`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/conformer/infra/parallelize.py#L22)
  - <a id="ParallelStrategy.DDP_W_FSDP2"></a>`DDP_W_FSDP2` — [`L23`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/conformer/infra/parallelize.py#L23)
  - <a id="ParallelStrategy.DDP_W_SIMPLEFSDP"></a>`DDP_W_SIMPLEFSDP` — [`L24`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/conformer/infra/parallelize.py#L24)
  - <a id="ParallelStrategy.FSDP2"></a>`FSDP2` — [`L19`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/conformer/infra/parallelize.py#L19)
  - <a id="ParallelStrategy.NONE"></a>`NONE` — [`L26`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/conformer/infra/parallelize.py#L26)
  - <a id="ParallelStrategy.SIMPLEFSDP"></a>`SIMPLEFSDP` — [`L20`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/conformer/infra/parallelize.py#L20)
- used by: [`parallelize_conformer`](parallelize.md#parallelize_conformer), [`_determine_parallel_strategy`](parallelize.md#_determine_parallel_strategy)

## Functions
- <a id="_determine_parallel_strategy"></a>`_determine_parallel_strategy(parallel_dims: torchtitan.distributed.ParallelDims, train_config: torchtitan.trainer.Trainer.Config | tpu_job_config.TPUTrainerConfig)` — [`L29`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/conformer/infra/parallelize.py#L29) — Determine parallel strategy based on config.
- <a id="apply_ac"></a>`apply_ac(model: nn.Module)` — [`L246`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/conformer/infra/parallelize.py#L246) — Apply activation checkpointing.
- <a id="apply_compile"></a>`apply_compile(model: nn.Module, train_config: torchtitan.trainer.Trainer.Config)` — [`L190`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/conformer/infra/parallelize.py#L190) — Apply torch.compile to layers or whole model.
- <a id="parallelize_conformer"></a>`parallelize_conformer(model: nn.Module, parallel_dims: torchtitan.distributed.ParallelDims, train_config: torchtitan.trainer.Trainer.Config | tpu_job_config.TPUTrainerConfig)` — [`L57`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/conformer/infra/parallelize.py#L57) — Apply parallelism and activation checkpointing to Conformer.

