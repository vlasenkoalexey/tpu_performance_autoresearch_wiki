---
title: 'Module: src/vllm_torchtpu/executors/kv_block_override.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/executors/kv_block_override.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.executors.kv_block_override`/
symbols:
  reconcile_num_gpu_blocks_override: reconcile_num_gpu_blocks_override().
  logger: logger.
  _NUM_BLOCKS_OVERRIDE_TOL: _NUM_BLOCKS_OVERRIDE_TOL.
  _NUM_BLOCKS_OVERRIDE_REL_TOL: _NUM_BLOCKS_OVERRIDE_REL_TOL.
---
# Module: [`src/vllm_torchtpu/executors/kv_block_override.py`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/executors/kv_block_override.py)

## Functions
- <a id="reconcile_num_gpu_blocks_override"></a>`reconcile_num_gpu_blocks_override(worker_overrides: list[int | None], workers_per_stage: int | None = None)` — [`L39`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/executors/kv_block_override.py#L39) — Return the agreed block-count override, or None if no worker set one.

## Module values
- <a id="_NUM_BLOCKS_OVERRIDE_REL_TOL"></a>`_NUM_BLOCKS_OVERRIDE_REL_TOL` — [`L36`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/executors/kv_block_override.py#L36)
- <a id="_NUM_BLOCKS_OVERRIDE_TOL"></a>`_NUM_BLOCKS_OVERRIDE_TOL` — [`L35`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/executors/kv_block_override.py#L35)
- <a id="logger"></a>`logger` — [`L33`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/executors/kv_block_override.py#L33)

