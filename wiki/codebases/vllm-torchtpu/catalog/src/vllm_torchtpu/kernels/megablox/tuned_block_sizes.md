---
title: 'Module: src/vllm_torchtpu/kernels/megablox/tuned_block_sizes.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/megablox/tuned_block_sizes.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.megablox.tuned_block_sizes`/
symbols:
  get_tuned_block_sizes: get_tuned_block_sizes().
  logger: logger.
  get_default_gmm_block_sizes: get_default_gmm_block_sizes().
  round_up_to_multiple_of_128_within_limit: round_up_to_multiple_of_128_within_limit().
  TUNED_BLOCK_SIZES: TUNED_BLOCK_SIZES.
---
# Module: [`src/vllm_torchtpu/kernels/megablox/tuned_block_sizes.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/tuned_block_sizes.py)

## Functions
- <a id="get_default_gmm_block_sizes"></a>`get_default_gmm_block_sizes(m: int, k: int, n: int, g: int)` — [`L321`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/tuned_block_sizes.py#L321) — Heuristic-based defaults for GMM tiling.
- <a id="get_tuned_block_sizes"></a>`get_tuned_block_sizes(m: int, k: int, n: int, num_total_groups: int, num_current_groups: int, lhs_dtype: str, rhs_dtype: str, quant_block_size: int)` — [`L361`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/tuned_block_sizes.py#L361) — Retrieves optimized (TM, TK, TN) tiling parameters for the GMM kernel.
- <a id="round_up_to_multiple_of_128_within_limit"></a>`round_up_to_multiple_of_128_within_limit(x: int, limit: int)` — [`L287`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/tuned_block_sizes.py#L287) — Rounds the given integer `x` up to the nearest multiple of 128, without

## Module values
- <a id="TUNED_BLOCK_SIZES"></a>`TUNED_BLOCK_SIZES` — [`L32`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/tuned_block_sizes.py#L32)
- <a id="logger"></a>`logger` — [`L17`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/tuned_block_sizes.py#L17)

