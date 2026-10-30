---
title: 'Module: torchtitan/experiments/tpu/examples/mamba2/kernels/mamba2_pallas.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/examples/mamba2/kernels/mamba2_pallas.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.examples.mamba2.kernels.mamba2_pallas`/
symbols:
  ssd_chunk_scan_pallas: ssd_chunk_scan_pallas().
  exc: exc.
  _pallas_ssd_fwd: _pallas_ssd_fwd.
  ssd_scan_pure_jax: ssd_scan_pure_jax().
  ssd_scan_pallas_jax: ssd_scan_pallas_jax().
  ssd_scan_bwd_jax: ssd_scan_bwd_jax().
  _pallas_ssd_bwd: _pallas_ssd_bwd.
  ssd_scan_pallas_jax.scan_batch_head: ssd_scan_pallas_jax().scan_batch_head().
  ssd_scan_bwd_jax.surrogate: ssd_scan_bwd_jax().surrogate().
  _backward: _backward().
  _pallas_ssd_op: _pallas_ssd_op.
  ssd_fused_chunk_kernel: ssd_fused_chunk_kernel().
  _execute_xla_scan: _execute_xla_scan().
  ssd_scan_pallas_jax.scan_head: ssd_scan_pallas_jax().scan_head().
  ssd_scan_pure_jax.scan_fn: ssd_scan_pure_jax().scan_fn().
  _setup_context: _setup_context().
---
# Module: [`torchtitan/experiments/tpu/examples/mamba2/kernels/mamba2_pallas.py`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba2/kernels/mamba2_pallas.py)

## Functions
- <a id="_backward"></a>`_backward(ctx, d_out)` — [`L235`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba2/kernels/mamba2_pallas.py#L235)
- <a id="_execute_xla_scan"></a>`_execute_xla_scan(x_hf: torch.Tensor, dt_hf: torch.Tensor, a_log: torch.Tensor, b_hf: torch.Tensor, c_hf: torch.Tensor, chunk_size: int)` — [`L335`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba2/kernels/mamba2_pallas.py#L335) — Vectorized TPU XLA scan fallback executing parallel chunk matrix multiplications.
- <a id="_setup_context"></a>`_setup_context(ctx, inputs, output)` — [`L230`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba2/kernels/mamba2_pallas.py#L230)
- <a id="ssd_scan_pallas_jax.scan_batch_head"></a>`scan_batch_head(x_bh, dt_bh, a_log_h, b_bh, c_bh)` — [`L111`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba2/kernels/mamba2_pallas.py#L111)
- <a id="ssd_scan_pure_jax.scan_fn"></a>`scan_fn(carry_state, inputs)` — [`L169`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba2/kernels/mamba2_pallas.py#L169)
- <a id="ssd_scan_pallas_jax.scan_head"></a>`scan_head(carry, inputs)` — [`L105`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba2/kernels/mamba2_pallas.py#L105)
- <a id="ssd_chunk_scan_pallas"></a>`ssd_chunk_scan_pallas(x: torch.Tensor, dt: torch.Tensor, a_log: torch.Tensor, b: torch.Tensor, c: torch.Tensor, d: Optional[torch.Tensor] = None, chunk_size: int = 64)` — [`L251`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba2/kernels/mamba2_pallas.py#L251) — Executes the fused Pallas TPU SSD scan with PyTorch tensor interface.
- <a id="ssd_fused_chunk_kernel"></a>`ssd_fused_chunk_kernel(x_ref, dt_ref, a_log_ref, b_ref, c_ref, prev_s_ref, out_ref, next_s_ref)` — [`L26`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba2/kernels/mamba2_pallas.py#L26) — Fused Pallas kernel for a single SSD chunk in TPU VMEM.
- <a id="ssd_scan_bwd_jax"></a>`ssd_scan_bwd_jax(x: jax.Array, dt: jax.Array, a_log: jax.Array, b: jax.Array, c: jax.Array, d_out: jax.Array)` — [`L195`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba2/kernels/mamba2_pallas.py#L195) — JAX backward pass for Mamba-2 SSD scan computing exact parameter gradients.
- <a id="ssd_scan_pallas_jax"></a>`ssd_scan_pallas_jax(x: jax.Array, dt: jax.Array, a_log: jax.Array, b: jax.Array, c: jax.Array)` — [`L84`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba2/kernels/mamba2_pallas.py#L84) — JAX entry point executing fused Pallas SSD scan over all chunks.
- <a id="ssd_scan_pure_jax"></a>`ssd_scan_pure_jax(x: jax.Array, dt: jax.Array, a_log: jax.Array, b: jax.Array, c: jax.Array)` — [`L131`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba2/kernels/mamba2_pallas.py#L131) — Pure JAX SSD chunk scan with native XLA TPU lowering and reverse AD support.
- <a id="ssd_scan_bwd_jax.surrogate"></a>`surrogate(x_l, dt_l, a_log_l, b_l, c_l)` — [`L204`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba2/kernels/mamba2_pallas.py#L204)

## Module values
- <a id="_pallas_ssd_bwd"></a>`_pallas_ssd_bwd` — [`L225`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba2/kernels/mamba2_pallas.py#L225)
- <a id="_pallas_ssd_fwd"></a>`_pallas_ssd_fwd` — [`L221`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba2/kernels/mamba2_pallas.py#L221)
- <a id="_pallas_ssd_op"></a>`_pallas_ssd_op` — [`L241`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba2/kernels/mamba2_pallas.py#L241)
- <a id="exc"></a>`exc` — [`L242`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba2/kernels/mamba2_pallas.py#L242)

