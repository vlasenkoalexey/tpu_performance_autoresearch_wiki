---
title: 'Module: src/vllm_torchtpu/layers/adapter/cp_attention.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/layers/adapter/cp_attention.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.layers.adapter.cp_attention`/
symbols:
  build_dcp_kernels: build_dcp_kernels().
  forward_with_dcp: forward_with_dcp().
  _pallas_rpa_kernel_dcp: _pallas_rpa_kernel_dcp().
  _build_dcp_kernel_op: _build_dcp_kernel_op().
  _alloc_instance_id: _alloc_instance_id().
  _DCP_KERNEL_REGISTRY._DCP_KERNEL_REGISTRY: _DCP_KERNEL_REGISTRY._DCP_KERNEL_REGISTRY.
  _DCP_KERNEL_INSTANCE_COUNTER: _DCP_KERNEL_INSTANCE_COUNTER.
  merge_attn_results: merge_attn_results().
  _fake_dcp: _fake_dcp().
  _build_dcp_kernel_op.kernel_impl: _build_dcp_kernel_op().kernel_impl().
---
# Module: [`src/vllm_torchtpu/layers/adapter/cp_attention.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/cp_attention.py)

## Functions
- <a id="_alloc_instance_id"></a>`_alloc_instance_id()` — [`L152`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/cp_attention.py#L152)
- <a id="_build_dcp_kernel_op"></a>`_build_dcp_kernel_op(op_name: str, fn)` — [`L166`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/cp_attention.py#L166) — Wrap fn (a _pallas_rpa_kernel_dcp partial) as a callable kernel.
- <a id="_fake_dcp"></a>`_fake_dcp(kv_cache: torch.Tensor, query: torch.Tensor, *args, **kwargs)` — [`L159`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/cp_attention.py#L159)
- <a id="_pallas_rpa_kernel_dcp"></a>`_pallas_rpa_kernel_dcp(kv_cache: jax.Array, query: jax.Array, key: jax.Array, value: jax.Array, seq_lens: jax.Array, block_tables: jax.Array, query_start_loc: jax.Array, request_distribution: jax.Array, q_scale: float | None, k_scale: float | None, v_scale: float | None, *, sliding_window: int | None, sm_scale: float | None = None, soft_cap: float | None = None, cp_group_size: int, cp_rank_val: int, attention_scope: _batched_rpa_configs.AttentionScope, kv_layout: _batched_rpa_configs.KVLayout = _batched_rpa_configs.KVLayout.HEAD_ALONG_SUBLANE, decode_query_size: int = 1)` — [`L80`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/cp_attention.py#L80) — One DCP pass (CACHE_ONLY or NEW_TOKENS_ONLY). Returns (new_kv_cache,
- <a id="build_dcp_kernels"></a>`build_dcp_kernels(sliding_window: int | None, sm_scale: float, logits_soft_cap: float | None, q_scale: float | None, k_scale: float | None, v_scale: float | None, cp_group_size: int, cp_rank: int, kv_layout: _batched_rpa_configs.KVLayout = _batched_rpa_configs.KVLayout.HEAD_ALONG_SUBLANE, decode_query_size: int = 1)` — [`L189`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/cp_attention.py#L189) — Build and cache the CACHE_ONLY and NEW_TOKENS_ONLY jax_ops. — documented in [batched-ragged-paged-attention-kernel](../../../../../concepts/batched-ragged-paged-attention-kernel.md)
- <a id="forward_with_dcp"></a>`forward_with_dcp(*, layer, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor, kv_cache: torch.Tensor, attn_metadata, sliding_window: int | None, sm_scale: float, logits_soft_cap: float | None, kv_cache_quantized_dtype, dcp_world_size: int, dcp_rank: int, kv_layout: _batched_rpa_configs.KVLayout = _batched_rpa_configs.KVLayout.HEAD_ALONG_SUBLANE, decode_query_size: int = 1)` — [`L274`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/cp_attention.py#L274) — Two-pass DCP attention forward. — documented in [batched-ragged-paged-attention-kernel](../../../../../concepts/batched-ragged-paged-attention-kernel.md)
- <a id="_build_dcp_kernel_op.kernel_impl"></a>`kernel_impl(kv_cache, *args, **kwargs)` — [`L181`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/cp_attention.py#L181)
- <a id="merge_attn_results"></a>`merge_attn_results(out_a: torch.Tensor, lse_a: torch.Tensor, out_b: torch.Tensor, lse_b: torch.Tensor)` — [`L45`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/cp_attention.py#L45) — Numerically stable LSE-weighted combination of two partial attentions.

## Module values
- <a id="_DCP_KERNEL_INSTANCE_COUNTER"></a>`_DCP_KERNEL_INSTANCE_COUNTER` — [`L149`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/cp_attention.py#L149)
- <a id="_DCP_KERNEL_REGISTRY._DCP_KERNEL_REGISTRY"></a>`_DCP_KERNEL_REGISTRY` — [`L148`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/cp_attention.py#L148)

