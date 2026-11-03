---
title: 'Module: src/vllm_torchtpu/kernels/mla/v2/transpose.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/mla/v2/transpose.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.mla.v2.transpose`/
symbols:
  xpose_pipeline: xpose_pipeline().
  logger: logger.
  identity_fn_generator: identity_fn_generator().
  xpose_full: xpose_full().
  get_reshape_dimension: get_reshape_dimension().
  pin_vmem_custom_call: pin_vmem_custom_call().
  prev_closest_valid_divisor: prev_closest_valid_divisor().
  xpose_pipeline.get_grid_index: xpose_pipeline().get_grid_index().
  xpose_full.xpose_kernel: xpose_full().xpose_kernel().
  get_reshape_dimension._reshape: get_reshape_dimension()._reshape().
  identity_fn_generator.identity: identity_fn_generator().identity().
  xpose_pipeline.xpose_kernel: xpose_pipeline().xpose_kernel().
---
# Module: [`src/vllm_torchtpu/kernels/mla/v2/transpose.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/transpose.py)

## Functions
- <a id="get_reshape_dimension._reshape"></a>`_reshape(inp)` — [`L93`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/transpose.py#L93)
- <a id="xpose_pipeline.get_grid_index"></a>`get_grid_index(i: int, j: int, input_grid: bool)` — [`L245`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/transpose.py#L245)
- <a id="get_reshape_dimension"></a>`get_reshape_dimension(shape, reshape_axes, dtype=jnp.float32)` — [`L90`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/transpose.py#L90)
- <a id="identity_fn_generator.identity"></a>`identity(*arg)` — [`L102`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/transpose.py#L102)
- <a id="identity_fn_generator"></a>`identity_fn_generator(num_scalars: int = 0)` — [`L99`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/transpose.py#L99) — Method to copy input content into outputs.
- <a id="pin_vmem_custom_call"></a>`pin_vmem_custom_call(input_tensor: jax.Array, num_scalars: int = 0)` — [`L121`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/transpose.py#L121) — Prefetches buffers to VMEM.
- <a id="prev_closest_valid_divisor"></a>`prev_closest_valid_divisor(number: int, divider: int, multiple_of: int = 1)` — [`L55`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/transpose.py#L55) — Finds the largest divisor of 'number' that is <= 'divider' and divisible
- <a id="xpose_full"></a>`xpose_full(input, *, transpose_axes)` — [`L34`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/transpose.py#L34)
- <a id="xpose_full.xpose_kernel"></a>`xpose_kernel(input_ref, output_ref)` — [`L35`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/transpose.py#L35)
- <a id="xpose_pipeline.xpose_kernel"></a>`xpose_kernel(input_ref, output_ref)` — [`L177`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/transpose.py#L177)
- <a id="xpose_pipeline"></a>`xpose_pipeline(input: jax.Array, *, transpose_axes: Sequence[int], n_tile: int = 128, m_tile: int = 128, parallel_axis: int = 0, pipeline_axis: int = 1, vmem_limit_bytes: int | None = None)` — [`L150`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/transpose.py#L150) — Double buffer transpose custom call implementation.

## Module values
- <a id="logger"></a>`logger` — [`L26`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/transpose.py#L26)

