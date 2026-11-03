---
title: 'Module: src/vllm_torchtpu/kernels/quantized_matmul/tuned_block_sizes.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/quantized_matmul/tuned_block_sizes.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.quantized_matmul.tuned_block_sizes`/
symbols:
  get_tuned_block_sizes: get_tuned_block_sizes().
  get_device_vmem_limit: get_device_vmem_limit().
  TunedValue: TunedValue#
  TUNED_BLOCK_SIZES.TUNED_BLOCK_SIZES: TUNED_BLOCK_SIZES.TUNED_BLOCK_SIZES.
  get_key: get_key().
  logger: logger.
  TunedKey: TunedKey#
  TunedValue.in_block_size: TunedValue#in_block_size.
  TunedValue.batch_block_size: TunedValue#batch_block_size.
  TunedValue.out_block_size: TunedValue#out_block_size.
  DEVICE_VMEM_LIMIT: DEVICE_VMEM_LIMIT.
  get_tpu_version: get_tpu_version().
  TunedValue.n_lane_multiplier: TunedValue#n_lane_multiplier.
  TUNED_BLOCK_SIZES_RAW: TUNED_BLOCK_SIZES_RAW.
  TunedKey.tpu_version: TunedKey#tpu_version.
  TunedKey.n_batch: TunedKey#n_batch.
  TunedKey.n_out: TunedKey#n_out.
  TunedKey.n_in: TunedKey#n_in.
  TunedKey.x_q_dtype: TunedKey#x_q_dtype.
  TunedKey.w_q_dtype: TunedKey#w_q_dtype.
---
# Module: [`src/vllm_torchtpu/kernels/quantized_matmul/tuned_block_sizes.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/quantized_matmul/tuned_block_sizes.py)

## Classes
### <a id="TunedKey"></a>`TunedKey`  ·  implements/extends NamedTuple
- def: [`src/vllm_torchtpu/kernels/quantized_matmul/tuned_block_sizes.py:26`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/quantized_matmul/tuned_block_sizes.py#L26)
- signature: `class TunedKey(NamedTuple):`
- members:
  - <a id="TunedKey.n_batch"></a>`n_batch` — [`L28`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/quantized_matmul/tuned_block_sizes.py#L28)
  - <a id="TunedKey.n_in"></a>`n_in` — [`L30`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/quantized_matmul/tuned_block_sizes.py#L30)
  - <a id="TunedKey.n_out"></a>`n_out` — [`L29`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/quantized_matmul/tuned_block_sizes.py#L29)
  - <a id="TunedKey.tpu_version"></a>`tpu_version` — [`L27`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/quantized_matmul/tuned_block_sizes.py#L27)
  - <a id="TunedKey.w_q_dtype"></a>`w_q_dtype` — [`L32`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/quantized_matmul/tuned_block_sizes.py#L32)
  - <a id="TunedKey.x_q_dtype"></a>`x_q_dtype` — [`L31`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/quantized_matmul/tuned_block_sizes.py#L31)
- used by: [`TUNED_BLOCK_SIZES`](tuned_block_sizes.md#TUNED_BLOCK_SIZES.TUNED_BLOCK_SIZES), [`get_key`](tuned_block_sizes.md#get_key)

### <a id="TunedValue"></a>`TunedValue`  ·  implements/extends NamedTuple
- def: [`src/vllm_torchtpu/kernels/quantized_matmul/tuned_block_sizes.py:35`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/quantized_matmul/tuned_block_sizes.py#L35)
- signature: `class TunedValue(NamedTuple):`
- members:
  - <a id="TunedValue.batch_block_size"></a>`batch_block_size` — [`L36`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/quantized_matmul/tuned_block_sizes.py#L36)
  - <a id="TunedValue.in_block_size"></a>`in_block_size` — [`L38`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/quantized_matmul/tuned_block_sizes.py#L38)
  - <a id="TunedValue.n_lane_multiplier"></a>`n_lane_multiplier` — [`L39`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/quantized_matmul/tuned_block_sizes.py#L39)
  - <a id="TunedValue.out_block_size"></a>`out_block_size` — [`L37`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/quantized_matmul/tuned_block_sizes.py#L37)
- used by: [`quantized_matmul_kernel`](blockwise_kernel.md#quantized_matmul_kernel), [`quantized_matmul_kernel`](kernel.md#quantized_matmul_kernel), [`get_kernel_name`](util.md#get_kernel_name), [`get_tuned_block_sizes`](tuned_block_sizes.md#get_tuned_block_sizes), [`TUNED_BLOCK_SIZES`](tuned_block_sizes.md#TUNED_BLOCK_SIZES.TUNED_BLOCK_SIZES)

## Functions
- <a id="get_device_vmem_limit"></a>`get_device_vmem_limit()` — [`L542`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/quantized_matmul/tuned_block_sizes.py#L542)
- <a id="get_key"></a>`get_key(n_batch: int, n_out: int, n_in: int, x_q_dtype: str, w_q_dtype: str)` — [`L563`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/quantized_matmul/tuned_block_sizes.py#L563) — Returns the key for the given parameters.
- <a id="get_tpu_version"></a>`get_tpu_version()` — [`L554`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/quantized_matmul/tuned_block_sizes.py#L554) — Returns the numeric version of the TPU, or -1 if not on TPU.
- <a id="get_tuned_block_sizes"></a>`get_tuned_block_sizes(n_batch: int, n_out: int, n_in: int, x_q_dtype: str, w_q_dtype: str)` — [`L581`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/quantized_matmul/tuned_block_sizes.py#L581) — Retrieve the tuned block sizes for the given parameters.

## Module values
- <a id="DEVICE_VMEM_LIMIT"></a>`DEVICE_VMEM_LIMIT` — [`L539`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/quantized_matmul/tuned_block_sizes.py#L539)
- <a id="TUNED_BLOCK_SIZES.TUNED_BLOCK_SIZES"></a>`TUNED_BLOCK_SIZES` — [`L535`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/quantized_matmul/tuned_block_sizes.py#L535)
- <a id="TUNED_BLOCK_SIZES_RAW"></a>`TUNED_BLOCK_SIZES_RAW` — [`L42`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/quantized_matmul/tuned_block_sizes.py#L42)
- <a id="logger"></a>`logger` — [`L23`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/quantized_matmul/tuned_block_sizes.py#L23)

