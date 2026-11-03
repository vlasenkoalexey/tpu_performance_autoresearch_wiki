---
title: 'Module: src/vllm_torchtpu/layers/adapter/custom_ops/mamba_state_copy_op.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/layers/adapter/custom_ops/mamba_state_copy_op.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.layers.adapter.custom_ops.mamba_state_copy_op`/
symbols:
  copy_mamba_state_rows: copy_mamba_state_rows().
  _row_copy_fn: _row_copy_fn().
  copy_mamba_state_blocks: copy_mamba_state_blocks().
  copy_pool_blocks: copy_pool_blocks.
  _copy_op: _copy_op.
  _copy_fn: _copy_fn().
  _row_copy_fn._rows_fn: _row_copy_fn()._rows_fn().
  _fake_copy: _fake_copy().
  _copy_step_budget_bytes: _copy_step_budget_bytes().
  _row_copy_step_rows: _row_copy_step_rows().
  _row_copy_fn.run: _row_copy_fn().run().
---
# Module: [`src/vllm_torchtpu/layers/adapter/custom_ops/mamba_state_copy_op.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mamba_state_copy_op.py)

## Functions
- <a id="_copy_fn"></a>`_copy_fn(pool: jax.Array, src: jax.Array, dst: jax.Array)` — [`L34`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mamba_state_copy_op.py#L34)
- <a id="_copy_step_budget_bytes"></a>`_copy_step_budget_bytes()` — [`L77`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mamba_state_copy_op.py#L77) — Returns the per-step VMEM byte budget for `copy_blocks`.
- <a id="_fake_copy"></a>`_fake_copy(pool: torch.Tensor, src: torch.Tensor, dst: torch.Tensor)` — [`L46`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mamba_state_copy_op.py#L46)
- <a id="_row_copy_fn"></a>`_row_copy_fn(num_pools: int, split: int, step_rows: int)` — [`L103`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mamba_state_copy_op.py#L103) — Compiles the whole-row copy `pool[dst[i]] = pool[src[i]]` for one geometry.
- <a id="_row_copy_step_rows"></a>`_row_copy_step_rows(rows: int, kernel_block_bytes: int, budget_bytes: int)` — [`L87`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mamba_state_copy_op.py#L87) — Returns the largest divisor of `rows` whose blocks fit in `budget_bytes`.
- <a id="_row_copy_fn._rows_fn"></a>`_rows_fn(pool: jax.Array, src: jax.Array, dst: jax.Array)` — [`L115`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mamba_state_copy_op.py#L115)
- <a id="copy_mamba_state_blocks"></a>`copy_mamba_state_blocks(pools: list[torch.Tensor], src: torch.Tensor, dst: torch.Tensor)` — [`L54`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mamba_state_copy_op.py#L54) — ``pool[dst[i]] = pool[src[i]]`` on every pool, as one program. — documented in [custom-ops](../../../../../../concepts/custom-ops.md)
- <a id="copy_mamba_state_rows"></a>`copy_mamba_state_rows(pool: torch.Tensor, src: torch.Tensor, dst: torch.Tensor, num_pools: int, split: int)` — [`L141`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mamba_state_copy_op.py#L141) — Copies whole manager-block rows in place within the merged block-major pool.
- <a id="_row_copy_fn.run"></a>`run(pool: torch.Tensor, src: torch.Tensor, dst: torch.Tensor)` — [`L133`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mamba_state_copy_op.py#L133)

## Module values
- <a id="_copy_op"></a>`_copy_op` — [`L41`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mamba_state_copy_op.py#L41)
- <a id="copy_pool_blocks"></a>`copy_pool_blocks` — [`L74`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mamba_state_copy_op.py#L74) — documented in [custom-ops](../../../../../../concepts/custom-ops.md)

