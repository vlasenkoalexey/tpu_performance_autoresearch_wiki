---
title: 'Module: torchtitan/experiments/tpu/kernels/linear_softmax_ce_softcap_kernel.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/kernels/linear_softmax_ce_softcap_kernel.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.kernels.linear_softmax_ce_softcap_kernel`/
symbols:
  Array: Array.
  Real: Real.
  _get_heuristic_config: _get_heuristic_config().
  linear_softmax_cross_entropy_loss_fwd_pallas_mosaic_tpu: linear_softmax_cross_entropy_loss_fwd_pallas_mosaic_tpu().
  linear_softmax_cross_entropy_loss_bwd_pallas_mosaic_tpu: linear_softmax_cross_entropy_loss_bwd_pallas_mosaic_tpu().
  linear_softmax_cross_entropy_loss_forward_pallas_kernel: linear_softmax_cross_entropy_loss_forward_pallas_kernel().
  linear_softmax_cross_entropy_loss_backward_pallas_kernel: linear_softmax_cross_entropy_loss_backward_pallas_kernel().
  linear_softmax_cross_entropy_loss_fwd_cost_estimate: linear_softmax_cross_entropy_loss_fwd_cost_estimate().
  linear_softmax_cross_entropy_loss_bwd_cost_estimate: linear_softmax_cross_entropy_loss_bwd_cost_estimate().
  linear_softmax_cross_entropy_loss_forward_pallas_kernel.fwd_kernel: linear_softmax_cross_entropy_loss_forward_pallas_kernel().fwd_kernel().
  linear_softmax_cross_entropy_loss_backward_pallas_kernel.bwd_kernel: linear_softmax_cross_entropy_loss_backward_pallas_kernel().bwd_kernel().
  validate_inputs: validate_inputs().
  linear_softmax_cross_entropy_loss_backward_pallas_kernel.bwd_kernel.bwd_pipeline: linear_softmax_cross_entropy_loss_backward_pallas_kernel().bwd_kernel().bwd_pipeline().
  get_heuristic_fwd_config: get_heuristic_fwd_config().
  get_heuristic_bwd_config: get_heuristic_bwd_config().
  _transform_suffix: _transform_suffix().
  linear_softmax_cross_entropy_loss_backward_pallas_kernel.bwd_kernel.bwd_pipeline.compute_s: linear_softmax_cross_entropy_loss_backward_pallas_kernel().bwd_kernel().bwd_pipeline().compute_s().
  Integer: Integer.
  Config: Config#
  _bytes: _bytes().
  linear_softmax_cross_entropy_loss_forward_pallas_kernel.fwd_kernel.fwd_pipeline: linear_softmax_cross_entropy_loss_forward_pallas_kernel().fwd_kernel().fwd_pipeline().
  _get_vmem_limit_bytes: _get_vmem_limit_bytes().
  _has_logit_transform: _has_logit_transform().
  linear_softmax_cross_entropy_loss_forward_pallas_kernel.fwd_kernel.fwd_pipeline.accumulate_loss: linear_softmax_cross_entropy_loss_forward_pallas_kernel().fwd_kernel().fwd_pipeline().accumulate_loss().
  linear_softmax_cross_entropy_loss_backward_pallas_kernel.bwd_kernel.bwd_pipeline.init_w_grad: linear_softmax_cross_entropy_loss_backward_pallas_kernel().bwd_kernel().bwd_pipeline().init_w_grad().
  linear_softmax_cross_entropy_loss_backward_pallas_kernel.bwd_kernel.bwd_pipeline.init_x_grad: linear_softmax_cross_entropy_loss_backward_pallas_kernel().bwd_kernel().bwd_pipeline().init_x_grad().
  linear_softmax_cross_entropy_loss_backward_pallas_kernel.bwd_kernel.bwd_pipeline.accumulate_w_grad: linear_softmax_cross_entropy_loss_backward_pallas_kernel().bwd_kernel().bwd_pipeline().accumulate_w_grad().
  linear_softmax_cross_entropy_loss_backward_pallas_kernel.bwd_kernel.bwd_pipeline.accumulate_x_grad: linear_softmax_cross_entropy_loss_backward_pallas_kernel().bwd_kernel().bwd_pipeline().accumulate_x_grad().
  Scalar: Scalar.
  partial: partial.
  _get_heuristic_config.is_mc_compatible: _get_heuristic_config().is_mc_compatible().
  calculate_xw_tiled: calculate_xw_tiled().
  linear_softmax_cross_entropy_loss_backward_pallas_kernel.bwd_kernel.bwd_pipeline.get_clean_x: linear_softmax_cross_entropy_loss_backward_pallas_kernel().bwd_kernel().bwd_pipeline().get_clean_x().
  linear_softmax_cross_entropy_loss_backward_pallas_kernel.bwd_kernel.bwd_pipeline.get_clean_w_vm1: linear_softmax_cross_entropy_loss_backward_pallas_kernel().bwd_kernel().bwd_pipeline().get_clean_w_vm1().
  Config.b_block_size: Config#b_block_size.
  Config.h_block_size: Config#h_block_size.
  Config.v_block_size: Config#v_block_size.
  _calculate_fwd_vmem_bytes: _calculate_fwd_vmem_bytes().
  _calculate_bwd_vmem_bytes: _calculate_bwd_vmem_bytes().
  _logit_transform: _logit_transform().
  _logit_transform_with_derivative: _logit_transform_with_derivative().
  reduce: reduce.
  calculate_xw_tiled.init_xw: calculate_xw_tiled().init_xw().
  calculate_xw_tiled.accumulate_xw: calculate_xw_tiled().accumulate_xw().
  linear_softmax_cross_entropy_loss_forward_pallas_kernel.fwd_kernel.fwd_pipeline.init_lse: linear_softmax_cross_entropy_loss_forward_pallas_kernel().fwd_kernel().fwd_pipeline().init_lse().
  linear_softmax_cross_entropy_loss_forward_pallas_kernel.fwd_kernel.fwd_pipeline.perform_loss_reduction: linear_softmax_cross_entropy_loss_forward_pallas_kernel().fwd_kernel().fwd_pipeline().perform_loss_reduction().
  linear_softmax_cross_entropy_loss_backward_pallas_kernel.bwd_kernel.bwd_pipeline.w_read: linear_softmax_cross_entropy_loss_backward_pallas_kernel().bwd_kernel().bwd_pipeline().w_read().
  linear_softmax_cross_entropy_loss_backward_pallas_kernel.bwd_kernel.bwd_pipeline.x_read: linear_softmax_cross_entropy_loss_backward_pallas_kernel().bwd_kernel().bwd_pipeline().x_read().
  linear_softmax_cross_entropy_loss_backward_pallas_kernel.bwd_kernel.bwd_pipeline.wait_grads: linear_softmax_cross_entropy_loss_backward_pallas_kernel().bwd_kernel().bwd_pipeline().wait_grads().
---
# Module: [`torchtitan/experiments/tpu/kernels/linear_softmax_ce_softcap_kernel.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/linear_softmax_ce_softcap_kernel.py)

## Classes
### <a id="Config"></a>`Config`
- def: [`torchtitan/experiments/tpu/kernels/linear_softmax_ce_softcap_kernel.py:61`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/linear_softmax_ce_softcap_kernel.py#L61)
- doc: The configuration specific for the Pallas Mosaic TPU kernel.
- signature: `class Config:`
- members:
  - <a id="Config.b_block_size"></a>`b_block_size` — [`L70`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/linear_softmax_ce_softcap_kernel.py#L70)
  - <a id="Config.h_block_size"></a>`h_block_size` — [`L71`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/linear_softmax_ce_softcap_kernel.py#L71)
  - <a id="Config.v_block_size"></a>`v_block_size` — [`L72`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/linear_softmax_ce_softcap_kernel.py#L72)
- used by: [`_get_heuristic_config`](linear_softmax_ce_softcap_kernel.md#_get_heuristic_config), [`get_heuristic_bwd_config`](linear_softmax_ce_softcap_kernel.md#get_heuristic_bwd_config), [`get_heuristic_fwd_config`](linear_softmax_ce_softcap_kernel.md#get_heuristic_fwd_config)

## Functions
- <a id="_bytes"></a>`_bytes(tensor: jt.Array | jax.ShapeDtypeStruct)` — [`L498`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/linear_softmax_ce_softcap_kernel.py#L498) — Computes total bytes of a tensor or ShapeDtypeStruct.
- <a id="_calculate_bwd_vmem_bytes"></a>`_calculate_bwd_vmem_bytes(b_block_size: int, h_block_size: int, v_block_size: int, dtype: jnp.dtype = jnp.float32)` — [`L103`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/linear_softmax_ce_softcap_kernel.py#L103) — Calculates VMEM memory usage in bytes for the backward kernel.
- <a id="_calculate_fwd_vmem_bytes"></a>`_calculate_fwd_vmem_bytes(b_block_size: int, h_block_size: int, v_block_size: int, dtype: jnp.dtype = jnp.float32)` — [`L75`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/linear_softmax_ce_softcap_kernel.py#L75) — Calculates VMEM memory usage in bytes for the forward kernel.
- <a id="_get_heuristic_config"></a>`_get_heuristic_config(b_dim: int, h_dim: int, v_dim: int, *, is_bwd: bool = False, dtype: jnp.dtype = jnp.float32, vmem_limit_bytes: int | None = None)` — [`L142`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/linear_softmax_ce_softcap_kernel.py#L142) — Calculates heuristic config based on VMEM size, dtype, and divisibility. — documented in [tpu-pallas-kernels](../../../../../concepts/tpu-pallas-kernels.md)
- <a id="_get_vmem_limit_bytes"></a>`_get_vmem_limit_bytes()` — [`L138`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/linear_softmax_ce_softcap_kernel.py#L138)
- <a id="_has_logit_transform"></a>`_has_logit_transform(soft_cap: float | None, output_multiplier: float)` — [`L394`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/linear_softmax_ce_softcap_kernel.py#L394) — Whether the transform is anything other than the identity.
- <a id="_logit_transform"></a>`_logit_transform(z, soft_cap: float | None, output_multiplier: float)` — [`L399`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/linear_softmax_ce_softcap_kernel.py#L399) — ``z -> logits`` as ``SoftCappedLinear.forward`` applies it (fp32).
- <a id="_logit_transform_with_derivative"></a>`_logit_transform_with_derivative(z, soft_cap: float | None, output_multiplier: float)` — [`L406`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/linear_softmax_ce_softcap_kernel.py#L406) — Returns ``(logits, d logits / d z)`` for the backward pass.
- <a id="_transform_suffix"></a>`_transform_suffix(soft_cap: float | None, output_multiplier: float)` — [`L416`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/linear_softmax_ce_softcap_kernel.py#L416) — Kernel-name suffix; empty for the identity so upstream names are kept.
- <a id="linear_softmax_cross_entropy_loss_forward_pallas_kernel.fwd_kernel.fwd_pipeline.accumulate_loss"></a>`accumulate_loss()` — [`L816`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/linear_softmax_ce_softcap_kernel.py#L816)
- <a id="linear_softmax_cross_entropy_loss_backward_pallas_kernel.bwd_kernel.bwd_pipeline.accumulate_w_grad"></a>`accumulate_w_grad()` — [`L1426`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/linear_softmax_ce_softcap_kernel.py#L1426)
- <a id="linear_softmax_cross_entropy_loss_backward_pallas_kernel.bwd_kernel.bwd_pipeline.accumulate_x_grad"></a>`accumulate_x_grad()` — [`L1439`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/linear_softmax_ce_softcap_kernel.py#L1439)
- <a id="calculate_xw_tiled.accumulate_xw"></a>`accumulate_xw()` — [`L489`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/linear_softmax_ce_softcap_kernel.py#L489)
- <a id="linear_softmax_cross_entropy_loss_backward_pallas_kernel.bwd_kernel"></a>`bwd_kernel(dout_hbm_ref, x_hbm_ref, labels_hbm_ref, w_hbm_ref, lse_hbm_ref, x_grad_hbm_ref, w_grad_hbm_ref, xw_scratch_ref, x_grad_tile_ref, w_grad_tile_ref, x_read_sem, w_read_sem, x_write_sem, w_write_sem)` — [`L1127`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/linear_softmax_ce_softcap_kernel.py#L1127)
- <a id="linear_softmax_cross_entropy_loss_backward_pallas_kernel.bwd_kernel.bwd_pipeline"></a>`bwd_pipeline(dout_ref, x_ref, labels_ref, w_v_ref, w_vm1_ref, lse_ref, x_grad_hbm_ref, w_grad_hbm_ref, xw_scratch_ref, x_grad_tile_ref, w_grad_tile_ref, x_read_sem, w_read_sem, x_write_sem, w_write_sem)` — [`L1145`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/linear_softmax_ce_softcap_kernel.py#L1145)
- <a id="calculate_xw_tiled"></a>`calculate_xw_tiled(x_ref, w_ref, xw_tiled, b_index, h_index, v_index, num_b_blocks, num_h_blocks, num_v_blocks, b_dim, h_dim, v_dim, preferred_element_type: jnp.dtype)` — [`L425`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/linear_softmax_ce_softcap_kernel.py#L425) — Calculates xw_tiled += x@w for forward/backward kernel common logic.
- <a id="linear_softmax_cross_entropy_loss_backward_pallas_kernel.bwd_kernel.bwd_pipeline.compute_s"></a>`compute_s()` — [`L1192`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/linear_softmax_ce_softcap_kernel.py#L1192)
- <a id="linear_softmax_cross_entropy_loss_forward_pallas_kernel.fwd_kernel"></a>`fwd_kernel(x_hbm_ref, labels_hbm_ref, w_hbm_ref, loss_hbm_ref, lse_hbm_ref, xw_tiled_ref)` — [`L770`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/linear_softmax_ce_softcap_kernel.py#L770)
- <a id="linear_softmax_cross_entropy_loss_forward_pallas_kernel.fwd_kernel.fwd_pipeline"></a>`fwd_pipeline(x_ref, labels_ref, w_ref, loss_ref, lse_ref, xw_tiled)` — [`L778`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/linear_softmax_ce_softcap_kernel.py#L778)
- <a id="linear_softmax_cross_entropy_loss_backward_pallas_kernel.bwd_kernel.bwd_pipeline.get_clean_w_vm1"></a>`get_clean_w_vm1()` — [`L1371`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/linear_softmax_ce_softcap_kernel.py#L1371) — Zeros out out-of-bounds padding elements in w_vm1_ref in VMEM.
- <a id="linear_softmax_cross_entropy_loss_backward_pallas_kernel.bwd_kernel.bwd_pipeline.get_clean_x"></a>`get_clean_x()` — [`L1345`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/linear_softmax_ce_softcap_kernel.py#L1345) — Zeros out out-of-bounds padding elements in x_ref in VMEM.
- <a id="get_heuristic_bwd_config"></a>`get_heuristic_bwd_config(b_dim: int, h_dim: int, v_dim: int, dtype: jnp.dtype = jnp.float32, vmem_limit_bytes: int | None = None)` — [`L333`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/linear_softmax_ce_softcap_kernel.py#L333) — Returns heuristic config for backward pass based on VMEM size and dtype. — documented in [tpu-pallas-kernels](../../../../../concepts/tpu-pallas-kernels.md)
- <a id="get_heuristic_fwd_config"></a>`get_heuristic_fwd_config(b_dim: int, h_dim: int, v_dim: int, dtype: jnp.dtype = jnp.float32, vmem_limit_bytes: int | None = None)` — [`L315`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/linear_softmax_ce_softcap_kernel.py#L315) — Returns heuristic config for forward pass based on VMEM size and dtype. — documented in [tpu-pallas-kernels](../../../../../concepts/tpu-pallas-kernels.md)
- <a id="linear_softmax_cross_entropy_loss_forward_pallas_kernel.fwd_kernel.fwd_pipeline.init_lse"></a>`init_lse()` — [`L810`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/linear_softmax_ce_softcap_kernel.py#L810)
- <a id="linear_softmax_cross_entropy_loss_backward_pallas_kernel.bwd_kernel.bwd_pipeline.init_w_grad"></a>`init_w_grad()` — [`L1404`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/linear_softmax_ce_softcap_kernel.py#L1404)
- <a id="linear_softmax_cross_entropy_loss_backward_pallas_kernel.bwd_kernel.bwd_pipeline.init_x_grad"></a>`init_x_grad()` — [`L1415`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/linear_softmax_ce_softcap_kernel.py#L1415)
- <a id="calculate_xw_tiled.init_xw"></a>`init_xw()` — [`L480`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/linear_softmax_ce_softcap_kernel.py#L480)
- <a id="_get_heuristic_config.is_mc_compatible"></a>`is_mc_compatible(v: int)` — [`L255`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/linear_softmax_ce_softcap_kernel.py#L255)
- <a id="linear_softmax_cross_entropy_loss_backward_pallas_kernel"></a>`linear_softmax_cross_entropy_loss_backward_pallas_kernel(dout, x, labels, w, lse, *, b_dim: int, h_dim: int, v_dim: int, preferred_element_type: jnp.dtype, b_block_size: int, h_block_size: int, v_block_size: int, soft_cap: float | None = None, output_multiplier: float = 1)` — [`L1023`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/linear_softmax_ce_softcap_kernel.py#L1023) — Pallas kernel for the backward pass of Linear Softmax Cross-Entropy Loss.
- <a id="linear_softmax_cross_entropy_loss_bwd_cost_estimate"></a>`linear_softmax_cross_entropy_loss_bwd_cost_estimate(dout: Real[Array, ""] | Real[Array, B] | jax.ShapeDtypeStruct, x: Real[Array, "B H"] | jax.ShapeDtypeStruct, labels: Integer[Array, B] | jax.ShapeDtypeStruct, w: Real[Array, "H V"] | jax.ShapeDtypeStruct, lse: Real[Array, B] | jax.ShapeDtypeStruct, out_type: Sequence[jax.ShapeDtypeStruct] | None = None)` — [`L583`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/linear_softmax_ce_softcap_kernel.py#L583) — Calculates the theoretical hardware cost estimate for the backward pass kernel.
- <a id="linear_softmax_cross_entropy_loss_bwd_pallas_mosaic_tpu"></a>`linear_softmax_cross_entropy_loss_bwd_pallas_mosaic_tpu(dout: Real[Array, ""] | Real[Array, B], lse: Real[Array, B], x: Real[Array, "B H"], labels: Integer[Array, B], w: Real[Array, "H V"], *, b_block_size: int = 1024, h_block_size: int = 512, v_block_size: int = 2048, reduction: Literal["sum", "mean", "none"] = "sum", preferred_element_type: jnp.dtype = jnp.float32, soft_cap: float | None = None, output_multiplier: float = 1)` — [`L1551`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/linear_softmax_ce_softcap_kernel.py#L1551) — Pallas kernel implementation of Linear Softmax Cross-Entropy Loss backward.
- <a id="linear_softmax_cross_entropy_loss_forward_pallas_kernel"></a>`linear_softmax_cross_entropy_loss_forward_pallas_kernel(x, labels, w, *, reduction: Literal["sum", "mean", "none"], h_dim: int, v_dim: int, preferred_element_type: jnp.dtype, b_block_size: int, h_block_size: int, v_block_size: int, soft_cap: float | None = None, output_multiplier: float = 1)` — [`L675`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/linear_softmax_ce_softcap_kernel.py#L675) — Pallas kernel for the forward pass of Linear Softmax Cross-Entropy Loss.
- <a id="linear_softmax_cross_entropy_loss_fwd_cost_estimate"></a>`linear_softmax_cross_entropy_loss_fwd_cost_estimate(x: Real[Array, "B H"] | jax.ShapeDtypeStruct, labels: Integer[Array, B] | jax.ShapeDtypeStruct, w: Real[Array, "H V"] | jax.ShapeDtypeStruct, out_type: Sequence[jax.ShapeDtypeStruct] | None = None)` — [`L503`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/linear_softmax_ce_softcap_kernel.py#L503) — Calculates the theoretical hardware cost estimate for the forward pass kernel.
- <a id="linear_softmax_cross_entropy_loss_fwd_pallas_mosaic_tpu"></a>`linear_softmax_cross_entropy_loss_fwd_pallas_mosaic_tpu(x: Real[Array, "B H"], labels: Integer[Array, B], w: Real[Array, "H V"], *, b_block_size: int = 1024, h_block_size: int = 512, v_block_size: int = 2048, reduction: Literal["sum", "mean", "none"] = "sum", preferred_element_type: jnp.dtype = jnp.float32, soft_cap: float | None = None, output_multiplier: float = 1)` — [`L940`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/linear_softmax_ce_softcap_kernel.py#L940) — The pallas kernel implementation of linear softmax cross-entropy loss.
- <a id="linear_softmax_cross_entropy_loss_forward_pallas_kernel.fwd_kernel.fwd_pipeline.perform_loss_reduction"></a>`perform_loss_reduction()` — [`L870`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/linear_softmax_ce_softcap_kernel.py#L870)
- <a id="validate_inputs"></a>`validate_inputs(x: Real[Array, "B H"], labels: Real[Array, "B V"], w: Real[Array, "H V"], b_block_size: int, h_block_size: int, v_block_size: int)` — [`L351`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/linear_softmax_ce_softcap_kernel.py#L351) — Validates the inputs to the kernels.
- <a id="linear_softmax_cross_entropy_loss_backward_pallas_kernel.bwd_kernel.bwd_pipeline.w_read"></a>`w_read()` — [`L1341`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/linear_softmax_ce_softcap_kernel.py#L1341)
- <a id="linear_softmax_cross_entropy_loss_backward_pallas_kernel.bwd_kernel.bwd_pipeline.wait_grads"></a>`wait_grads()` — [`L1452`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/linear_softmax_ce_softcap_kernel.py#L1452)
- <a id="linear_softmax_cross_entropy_loss_backward_pallas_kernel.bwd_kernel.bwd_pipeline.x_read"></a>`x_read()` — [`L1398`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/linear_softmax_ce_softcap_kernel.py#L1398)

## Module values
- <a id="Array"></a>`Array` — [`L51`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/linear_softmax_ce_softcap_kernel.py#L51)
- <a id="Integer"></a>`Integer` — [`L52`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/linear_softmax_ce_softcap_kernel.py#L52)
- <a id="Real"></a>`Real` — [`L53`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/linear_softmax_ce_softcap_kernel.py#L53)
- <a id="Scalar"></a>`Scalar` — [`L54`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/linear_softmax_ce_softcap_kernel.py#L54)
- <a id="partial"></a>`partial` — [`L56`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/linear_softmax_ce_softcap_kernel.py#L56)
- <a id="reduce"></a>`reduce` — [`L57`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/linear_softmax_ce_softcap_kernel.py#L57)

