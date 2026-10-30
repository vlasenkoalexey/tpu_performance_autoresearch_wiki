---
title: 'Module: torchtitan/experiments/rl/models/vllm_worker.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/rl/models/vllm_worker.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.rl.models.vllm_worker`/
symbols:
  TorchTitanGPUModelRunner: TorchTitanGPUModelRunner#
  TorchTitanGPUWorker.init_device: TorchTitanGPUWorker#init_device().
  TorchTitanGPUModelRunner._pad_for_sequence_parallelism: TorchTitanGPUModelRunner#_pad_for_sequence_parallelism().
  TorchTitanGPUWorker: TorchTitanGPUWorker#
---
# Module: [`torchtitan/experiments/rl/models/vllm_worker.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/vllm_worker.py)

## Classes
### <a id="TorchTitanGPUModelRunner"></a>`TorchTitanGPUModelRunner`
- def: [`torchtitan/experiments/rl/models/vllm_worker.py:15`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/vllm_worker.py#L15)
- doc: V1 runner that pads batches for dense and expert sequence parallelism.
- signature: `class TorchTitanGPUModelRunner(GPUModelRunner):`
- protocol/private: <a id="TorchTitanGPUModelRunner._pad_for_sequence_parallelism"></a>`_pad_for_sequence_parallelism`[`L18`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/vllm_worker.py#L18)
- used by: [`init_device`](vllm_worker.md#TorchTitanGPUWorker.init_device)  (1 test-only)

### <a id="TorchTitanGPUWorker"></a>`TorchTitanGPUWorker`
- def: [`torchtitan/experiments/rl/models/vllm_worker.py:29`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/vllm_worker.py#L29)
- doc: V1 worker that constructs `TorchTitanGPUModelRunner`.
- signature: `class TorchTitanGPUWorker(GPUWorker):`
- members:
  - <a id="TorchTitanGPUWorker.init_device"></a>`init_device(self)` — [`L32`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/vllm_worker.py#L32)
- uses (calls/refs, reference-scoped): [`TorchTitanGPUModelRunner`](vllm_worker.md#TorchTitanGPUModelRunner)

