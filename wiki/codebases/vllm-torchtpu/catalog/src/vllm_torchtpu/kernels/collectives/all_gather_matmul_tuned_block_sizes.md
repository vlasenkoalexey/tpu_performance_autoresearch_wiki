---
title: 'Module: src/vllm_torchtpu/kernels/collectives/all_gather_matmul_tuned_block_sizes.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/collectives/all_gather_matmul_tuned_block_sizes.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.collectives.all_gather_matmul_tuned_block_sizes`/
symbols:
  get_tuned_block_sizes: get_tuned_block_sizes().
  get_key: get_key().
  TUNED_BLOCK_SIZES: TUNED_BLOCK_SIZES.
  get_tpu_version: get_tpu_version().
---
# Module: [`src/vllm_torchtpu/kernels/collectives/all_gather_matmul_tuned_block_sizes.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/collectives/all_gather_matmul_tuned_block_sizes.py)

## Functions
- <a id="get_key"></a>`get_key(m, n, k, dtype, tp_size)` — [`L51`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/collectives/all_gather_matmul_tuned_block_sizes.py#L51) — Returns the key for the given parameters.
- <a id="get_tpu_version"></a>`get_tpu_version()` — [`L40`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/collectives/all_gather_matmul_tuned_block_sizes.py#L40) — Returns the numeric version of the TPU, or -1 if not on TPU.
- <a id="get_tuned_block_sizes"></a>`get_tuned_block_sizes(m, n, k, dtype_name, tp_size)` — [`L69`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/collectives/all_gather_matmul_tuned_block_sizes.py#L69) — Returns the tuned block sizes for the given parameters.

## Module values
- <a id="TUNED_BLOCK_SIZES"></a>`TUNED_BLOCK_SIZES` — [`L28`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/collectives/all_gather_matmul_tuned_block_sizes.py#L28)

