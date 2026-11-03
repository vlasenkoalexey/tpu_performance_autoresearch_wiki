---
title: 'Module: src/vllm_torchtpu/kernels/megablox/moe_onehot_unpermute.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/megablox/moe_onehot_unpermute.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.megablox.moe_onehot_unpermute`/
symbols:
  can_use_blockwise_onehot_unpermute: can_use_blockwise_onehot_unpermute().
  _ROUTE_BLOCK_SIZE: _ROUTE_BLOCK_SIZE.
  blockwise_onehot_unpermute: blockwise_onehot_unpermute().
  _pipeline_body: _pipeline_body().
  _kernel: _kernel().
  _explicit_vmem_bytes: _explicit_vmem_bytes().
  _accumulate_route_block: _accumulate_route_block().
  _validate_inputs: _validate_inputs().
  _VMEM_WORKSPACE_MARGIN_BYTES: _VMEM_WORKSPACE_MARGIN_BYTES.
  _make_route_block_selector: _make_route_block_selector().
---
# Module: [`src/vllm_torchtpu/kernels/megablox/moe_onehot_unpermute.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/moe_onehot_unpermute.py)

## Functions
- <a id="_accumulate_route_block"></a>`_accumulate_route_block(route_rows: jax.Array, owner_ref: jax.Array, token_ids: jax.Array, route_weights: jax.Array, route_valid: jax.Array, route_row_valid: jax.Array, *, num_tokens: int)` — [`L92`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/moe_onehot_unpermute.py#L92) — Accumulate one contiguous BF16 route block into its token owners.
- <a id="_explicit_vmem_bytes"></a>`_explicit_vmem_bytes(route_capacity: int, hidden_size: int, num_tokens: int)` — [`L29`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/moe_onehot_unpermute.py#L29) — Size of the explicitly allocated VMEM buffers used by the kernel.
- <a id="_kernel"></a>`_kernel(valid_count_ref: jax.Array, token_indices_sorted_ref: jax.Array, topk_weights_sorted_ref: jax.Array, route_hbm_ref: jax.Array, owner_out_ref: jax.Array, owner_ref: jax.Array, store_ref: jax.Array, owner_store_sem_ref: jax.Array, *, route_capacity: int, hidden_size: int, num_tokens: int)` — [`L166`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/moe_onehot_unpermute.py#L166) — Stream valid standard-GMM2 rows from HBM and combine token owners.
- <a id="_make_route_block_selector"></a>`_make_route_block_selector(token_ids: jax.Array, route_weights: jax.Array, route_valid: jax.Array, *, num_tokens: int)` — [`L75`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/moe_onehot_unpermute.py#L75) — Build a token-by-route selector for one contiguous route block.
- <a id="_pipeline_body"></a>`_pipeline_body(route_block_ref: jax.Array, owner_ref: jax.Array, *, token_indices_sorted_ref: jax.Array, topk_weights_sorted_ref: jax.Array, valid_count_ref: jax.Array, route_capacity: int, num_tokens: int)` — [`L128`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/moe_onehot_unpermute.py#L128) — Accumulate one HBM-streamed route block into a VMEM owner buffer.
- <a id="_validate_inputs"></a>`_validate_inputs(route_output: jax.Array, token_indices_sorted: jax.Array, topk_weights_sorted: jax.Array, valid_count: jax.Array, *, num_tokens: int)` — [`L226`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/moe_onehot_unpermute.py#L226)
- <a id="blockwise_onehot_unpermute"></a>`blockwise_onehot_unpermute(route_output: jax.Array, token_indices_sorted: jax.Array, topk_weights_sorted: jax.Array, valid_count: jax.Array, *, num_tokens: int)` — [`L256`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/moe_onehot_unpermute.py#L256) — Combine the existing output one-hot in 128-route HBM blocks.
- <a id="can_use_blockwise_onehot_unpermute"></a>`can_use_blockwise_onehot_unpermute(route_output: jax.Array, token_indices_sorted: jax.Array, topk_weights_sorted: jax.Array, valid_count: jax.Array, *, num_tokens: int)` — [`L37`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/moe_onehot_unpermute.py#L37) — Return whether this one-hot shape satisfies kernel safety constraints.

## Module values
- <a id="_ROUTE_BLOCK_SIZE"></a>`_ROUTE_BLOCK_SIZE` — [`L25`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/moe_onehot_unpermute.py#L25)
- <a id="_VMEM_WORKSPACE_MARGIN_BYTES"></a>`_VMEM_WORKSPACE_MARGIN_BYTES` — [`L26`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/megablox/moe_onehot_unpermute.py#L26)

