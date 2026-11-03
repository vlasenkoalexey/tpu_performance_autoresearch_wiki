---
title: 'Module: src/vllm_torchtpu/kernels/ragged_paged_attention/v3/util.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/ragged_paged_attention/v3/util.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.ragged_paged_attention.v3.util`/
symbols:
  align_to: align_to().
  get_dtype_packing: get_dtype_packing().
  cdiv: cdiv().
  next_power_of_2: next_power_of_2().
  get_tpu_version: get_tpu_version().
  get_dtype_bitwidth: get_dtype_bitwidth().
---
# Module: [`src/vllm_torchtpu/kernels/ragged_paged_attention/v3/util.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/util.py)

## Functions
- <a id="align_to"></a>`align_to(x, a)` — [`L25`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/util.py#L25)
- <a id="cdiv"></a>`cdiv(a, b)` — [`L20`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/util.py#L20)
- <a id="get_dtype_bitwidth"></a>`get_dtype_bitwidth(dtype)` — [`L29`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/util.py#L29)
- <a id="get_dtype_packing"></a>`get_dtype_packing(dtype)` — [`L33`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/util.py#L33) — documented in [ragged-paged-attention-kernel](../../../../../../concepts/ragged-paged-attention-kernel.md)
- <a id="get_tpu_version"></a>`get_tpu_version()` — [`L53`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/util.py#L53) — Returns the numeric version of the TPU, or -1 if not on TPU. — documented in [ragged-paged-attention-kernel](../../../../../../concepts/ragged-paged-attention-kernel.md)
- <a id="next_power_of_2"></a>`next_power_of_2(x: int)` — [`L38`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/util.py#L38) — Finds the smallest power of 2 >= x using bit manipulation. — documented in [ragged-paged-attention-kernel](../../../../../../concepts/ragged-paged-attention-kernel.md)

