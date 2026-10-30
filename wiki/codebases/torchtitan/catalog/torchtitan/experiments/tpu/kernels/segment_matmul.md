---
title: 'Module: torchtitan/experiments/tpu/kernels/segment_matmul.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/kernels/segment_matmul.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.kernels.segment_matmul`/
symbols:
  _get_ops: _get_ops().
  segment_matmul_pallas_2d: segment_matmul_pallas_2d().
  _build_ragged_dot_kernels: _build_ragged_dot_kernels().
  _FWD_OP: _FWD_OP.
  _BWD_OP: _BWD_OP.
  _RaggedDotAutograd.forward: _RaggedDotAutograd#forward().
  _RaggedDotAutograd.backward: _RaggedDotAutograd#backward().
  _build_ragged_dot_kernels.fwd_op: _build_ragged_dot_kernels().fwd_op().
  _build_ragged_dot_kernels.bwd_op: _build_ragged_dot_kernels().bwd_op().
  _RaggedDotAutograd: _RaggedDotAutograd#
---
# Module: [`torchtitan/experiments/tpu/kernels/segment_matmul.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/segment_matmul.py)

## Classes
### <a id="_RaggedDotAutograd"></a>`_RaggedDotAutograd`
- def: [`torchtitan/experiments/tpu/kernels/segment_matmul.py:80`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/segment_matmul.py#L80)
- doc: Autograd Function for grouped matmul with TENSOR `group_sizes`.
- signature: `class _RaggedDotAutograd(torch.autograd.Function):`
- members:
  - <a id="_RaggedDotAutograd.backward"></a>`backward(ctx, grad_output)` — [`L90`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/segment_matmul.py#L90)
  - <a id="_RaggedDotAutograd.forward"></a>`forward(ctx, lhs, rhs, group_sizes)` — [`L84`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/segment_matmul.py#L84)
- uses (calls/refs, reference-scoped): [`_get_ops`](segment_matmul.md#_get_ops)
- used by: [`segment_matmul_pallas_2d`](segment_matmul.md#segment_matmul_pallas_2d)

## Functions
- <a id="_build_ragged_dot_kernels"></a>`_build_ragged_dot_kernels()` — [`L17`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/segment_matmul.py#L17) — Build forward + backward Pallas megablox kernels with TENSOR group_sizes.
- <a id="_get_ops"></a>`_get_ops()` — [`L73`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/segment_matmul.py#L73)
- <a id="_build_ragged_dot_kernels.bwd_op"></a>`bwd_op(dout: jax.Array, lhs: jax.Array, rhs: jax.Array, group_sizes: jax.Array)` — [`L39`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/segment_matmul.py#L39)
- <a id="_build_ragged_dot_kernels.fwd_op"></a>`fwd_op(lhs: jax.Array, rhs: jax.Array, group_sizes: jax.Array)` — [`L31`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/segment_matmul.py#L31)
- <a id="segment_matmul_pallas_2d"></a>`segment_matmul_pallas_2d(lhs: torch.Tensor, rhs: torch.Tensor, group_sizes: torch.Tensor)` — [`L100`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/segment_matmul.py#L100) — Per-track ragged dot. ``group_sizes`` is a TPU int32 tensor (no .tolist()).

## Module values
- <a id="_BWD_OP"></a>`_BWD_OP` — [`L70`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/segment_matmul.py#L70)
- <a id="_FWD_OP"></a>`_FWD_OP` — [`L70`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/segment_matmul.py#L70)

