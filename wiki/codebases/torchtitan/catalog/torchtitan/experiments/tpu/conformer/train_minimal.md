---
title: 'Module: torchtitan/experiments/tpu/conformer/train_minimal.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/conformer/train_minimal.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.conformer.train_minimal`/
symbols:
  start_trainer: start_trainer().
  logger: logger.
  TORCH_DTYPE_MAP: TORCH_DTYPE_MAP.
  ParallelDims: ParallelDims.
  train_step: train_step().
  build_random_dataloader: build_random_dataloader().
---
# Module: [`torchtitan/experiments/tpu/conformer/train_minimal.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/conformer/train_minimal.py)

## Functions
- <a id="build_random_dataloader"></a>`build_random_dataloader(train_config, vocab_size, device)` — [`L114`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/conformer/train_minimal.py#L114)
- <a id="start_trainer"></a>`start_trainer(train_config: TPUTrainerConfig)` — [`L144`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/conformer/train_minimal.py#L144) — documented in [debug-and-profiling-tools](../../../../../concepts/debug-and-profiling-tools.md)
- <a id="train_step"></a>`train_step(model: torch.nn.Module, inputs: torch.Tensor, targets: torch.Tensor, optimizer: torch.optim.Optimizer, loss_fn, materialize_forward_before_backward: bool = False, use_ctc: bool = False, use_jax_ctc: bool = False, output_lengths: torch.Tensor = None, target_lengths: torch.Tensor = None)` — [`L47`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/conformer/train_minimal.py#L47) — Single training step.

## Module values
- <a id="ParallelDims"></a>`ParallelDims` — [`L38`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/conformer/train_minimal.py#L38)
- <a id="TORCH_DTYPE_MAP"></a>`TORCH_DTYPE_MAP` — [`L37`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/conformer/train_minimal.py#L37)
- <a id="logger"></a>`logger` — [`L39`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/conformer/train_minimal.py#L39)

