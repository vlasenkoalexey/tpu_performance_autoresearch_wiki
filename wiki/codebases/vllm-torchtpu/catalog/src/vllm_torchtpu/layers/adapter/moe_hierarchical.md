---
title: 'Module: src/vllm_torchtpu/layers/adapter/moe_hierarchical.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/layers/adapter/moe_hierarchical.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.layers.adapter.moe_hierarchical`/
symbols:
  hierarchical_moe_parallel_config: hierarchical_moe_parallel_config().
  hierarchical_split_or_none: hierarchical_split_or_none().
  align_ep_weight_filter: align_ep_weight_filter().
  logger: logger.
  hierarchical_moe_parallel_config.patched_make: hierarchical_moe_parallel_config().patched_make().
  _filter_patched: _filter_patched.
  align_ep_weight_filter.chip_aware: align_ep_weight_filter().chip_aware().
---
# Module: [`src/vllm_torchtpu/layers/adapter/moe_hierarchical.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/moe_hierarchical.py)

## Functions
- <a id="align_ep_weight_filter"></a>`align_ep_weight_filter()` — [`L61`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/moe_hierarchical.py#L61) — Teach ``--enable-ep-weight-filter`` the chip-block expert ownership.
- <a id="align_ep_weight_filter.chip_aware"></a>`chip_aware(num_experts: int, ep_size: int, ep_rank: int, placement: str = "linear")` — [`L76`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/moe_hierarchical.py#L76)
- <a id="hierarchical_moe_parallel_config"></a>`hierarchical_moe_parallel_config()` — [`L94`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/moe_hierarchical.py#L94) — Make ``FusedMoE`` built inside this context manager use the chip-aware split.
- <a id="hierarchical_split_or_none"></a>`hierarchical_split_or_none()` — [`L28`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/moe_hierarchical.py#L28) — ``(ep_size, ep_rank, tp_size, tp_rank)``, or ``None`` to stay flat. — documented in [distributed-parallelism-and-meshes](../../../../../concepts/distributed-parallelism-and-meshes.md)
- <a id="hierarchical_moe_parallel_config.patched_make"></a>`patched_make(*args, **kwargs)` — [`L107`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/moe_hierarchical.py#L107)

## Module values
- <a id="_filter_patched"></a>`_filter_patched` — [`L58`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/moe_hierarchical.py#L58)
- <a id="logger"></a>`logger` — [`L25`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/moe_hierarchical.py#L25)

