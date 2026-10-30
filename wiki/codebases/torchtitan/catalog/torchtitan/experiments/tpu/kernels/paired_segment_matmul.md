---
title: 'Module: torchtitan/experiments/tpu/kernels/paired_segment_matmul.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/kernels/paired_segment_matmul.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.kernels.paired_segment_matmul`/
symbols:
  _paired_forward: _paired_forward().
  _paired_dweight: _paired_dweight().
  _accumulate_dinput: _accumulate_dinput().
  paired_segment_matmul_pallas_2d: paired_segment_matmul_pallas_2d().
  _paired_grouped_mm_bwd: _paired_grouped_mm_bwd().
  _dinput: _dinput().
  _metadata: _metadata().
  _paired_grouped_mm_fwd: _paired_grouped_mm_fwd().
  _get_store_mask: _get_store_mask.
  _paired_forward.kernel: _paired_forward().kernel().
  _accumulate_dinput.kernel: _accumulate_dinput().kernel().
  _paired_dweight.kernel: _paired_dweight().kernel().
  _backward: _backward().
  _accumulate_dinput.row_indices: _accumulate_dinput().row_indices().
  _paired_dweight.kernel._accumulate: _paired_dweight().kernel()._accumulate().
  _make_group_metadata: _make_group_metadata.
  _get_group_size: _get_group_size.
  _validate_shapes: _validate_shapes().
  _paired_forward.lhs_indices: _paired_forward().lhs_indices().
  _paired_forward.rhs_indices: _paired_forward().rhs_indices().
  _paired_forward.out_indices: _paired_forward().out_indices().
  _accumulate_dinput.rhs_indices: _accumulate_dinput().rhs_indices().
  _paired_dweight.lhs_indices: _paired_dweight().lhs_indices().
  _paired_dweight.dout_indices: _paired_dweight().dout_indices().
  _paired_dweight.out_indices: _paired_dweight().out_indices().
  _setup_context: _setup_context().
  _accumulate_dinput.kernel._seed: _accumulate_dinput().kernel()._seed().
  _paired_dweight.kernel._zero_accumulators: _paired_dweight().kernel()._zero_accumulators().
  _paired_dweight.kernel._store_accumulators: _paired_dweight().kernel()._store_accumulators().
  __all__: __all__.
---
# Module: [`torchtitan/experiments/tpu/kernels/paired_segment_matmul.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/paired_segment_matmul.py)

## Functions
- <a id="_paired_dweight.kernel._accumulate"></a>`_accumulate()` — [`L339`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/paired_segment_matmul.py#L339)
- <a id="_accumulate_dinput"></a>`_accumulate_dinput(dout, rhs, existing, group_sizes, *, tile_m)` — [`L167`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/paired_segment_matmul.py#L167) — Return ``existing + bf16(dout @ rhs^T)`` per expert group, in place.
- <a id="_backward"></a>`_backward(ctx, grad_output1, grad_output3)` — [`L476`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/paired_segment_matmul.py#L476)
- <a id="_dinput"></a>`_dinput(dout1, dout3, rhs1, rhs3, group_sizes, *, tile_m)` — [`L254`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/paired_segment_matmul.py#L254) — dInput = dout1 @ W1^T + dout3 @ W3^T, the second term added in place.
- <a id="_metadata"></a>`_metadata(group_sizes, *, m, tile_m, groups, visit_empty_groups)` — [`L63`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/paired_segment_matmul.py#L63)
- <a id="_paired_dweight"></a>`_paired_dweight(lhs, dout1, dout3, group_sizes, *, tile_m, tile_k=0)` — [`L274`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/paired_segment_matmul.py#L274) — Traverse each expert's routed rows once to produce two weight grads.
- <a id="_paired_forward"></a>`_paired_forward(lhs, rhs1, rhs3, group_sizes, *, tile_m)` — [`L74`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/paired_segment_matmul.py#L74) — Compute the two projections from one routed-token tile load.
- <a id="_paired_grouped_mm_bwd"></a>`_paired_grouped_mm_bwd(dout1: jax.Array, dout3: jax.Array, lhs: jax.Array, rhs1: jax.Array, rhs3: jax.Array, group_sizes: jax.Array, tile_m: int, tgmm_tile_m: int, tgmm_tile_k: int)` — [`L447`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/paired_segment_matmul.py#L447)
- <a id="_paired_grouped_mm_fwd"></a>`_paired_grouped_mm_fwd(lhs: jax.Array, rhs1: jax.Array, rhs3: jax.Array, group_sizes: jax.Array, tile_m: int, tgmm_tile_m: int, tgmm_tile_k: int)` — [`L433`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/paired_segment_matmul.py#L433)
- <a id="_accumulate_dinput.kernel._seed"></a>`_seed()` — [`L196`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/paired_segment_matmul.py#L196)
- <a id="_setup_context"></a>`_setup_context(ctx, inputs, output)` — [`L467`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/paired_segment_matmul.py#L467)
- <a id="_paired_dweight.kernel._store_accumulators"></a>`_store_accumulators()` — [`L390`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/paired_segment_matmul.py#L390)
- <a id="_validate_shapes"></a>`_validate_shapes(lhs, rhs1, rhs3, group_sizes, tile_m)` — [`L36`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/paired_segment_matmul.py#L36)
- <a id="_paired_dweight.kernel._zero_accumulators"></a>`_zero_accumulators()` — [`L330`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/paired_segment_matmul.py#L330)
- <a id="_paired_dweight.dout_indices"></a>`dout_indices(n_i, k_i, grid_id, group_metadata, group_offset)` — [`L398`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/paired_segment_matmul.py#L398)
- <a id="_paired_forward.kernel"></a>`kernel(group_metadata, group_offset, lhs, rhs1, rhs3, out1, out3, acc1, acc3)` — [`L88`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/paired_segment_matmul.py#L88)
- <a id="_accumulate_dinput.kernel"></a>`kernel(group_metadata, group_offset, dout, rhs, existing, out)` — [`L186`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/paired_segment_matmul.py#L186)
- <a id="_paired_dweight.kernel"></a>`kernel(group_metadata, group_offset, lhs, dout1, dout3, out1, out3, acc1, acc3)` — [`L306`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/paired_segment_matmul.py#L306)
- <a id="_paired_forward.lhs_indices"></a>`lhs_indices(n_i, grid_id, k_i, group_metadata, group_offset)` — [`L129`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/paired_segment_matmul.py#L129)
- <a id="_paired_dweight.lhs_indices"></a>`lhs_indices(n_i, k_i, grid_id, group_metadata, group_offset)` — [`L394`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/paired_segment_matmul.py#L394)
- <a id="_paired_forward.out_indices"></a>`out_indices(n_i, grid_id, k_i, group_metadata, group_offset)` — [`L137`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/paired_segment_matmul.py#L137)
- <a id="_paired_dweight.out_indices"></a>`out_indices(n_i, k_i, grid_id, group_metadata, group_offset)` — [`L402`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/paired_segment_matmul.py#L402)
- <a id="paired_segment_matmul_pallas_2d"></a>`paired_segment_matmul_pallas_2d(lhs: torch.Tensor, rhs1: torch.Tensor, rhs3: torch.Tensor, group_sizes: torch.Tensor, *, tile_m: int = 1024, tgmm_tile_m: int = 128, tgmm_tile_k: int = 0)` — [`L495`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/paired_segment_matmul.py#L495) — Apply two equal-shaped expert projections while sharing lhs loads.
- <a id="_paired_forward.rhs_indices"></a>`rhs_indices(n_i, grid_id, k_i, group_metadata, group_offset)` — [`L133`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/paired_segment_matmul.py#L133)
- <a id="_accumulate_dinput.rhs_indices"></a>`rhs_indices(n_i, grid_id, k_i, group_metadata, group_offset)` — [`L228`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/paired_segment_matmul.py#L228)
- <a id="_accumulate_dinput.row_indices"></a>`row_indices(n_i, grid_id, k_i, group_metadata, group_offset)` — [`L224`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/paired_segment_matmul.py#L224)

## Module values
- <a id="__all__"></a>`__all__` — [`L520`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/paired_segment_matmul.py#L520)
- <a id="_get_group_size"></a>`_get_group_size` — [`L32`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/paired_segment_matmul.py#L32)
- <a id="_get_store_mask"></a>`_get_store_mask` — [`L33`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/paired_segment_matmul.py#L33)
- <a id="_make_group_metadata"></a>`_make_group_metadata` — [`L31`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/paired_segment_matmul.py#L31)

