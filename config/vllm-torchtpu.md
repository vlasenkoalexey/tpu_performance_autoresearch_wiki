---
slug: vllm-torchtpu
repo: raw/code/vllm-torchtpu
acquire: submodule
# vllm-project/vllm-torchtpu main HEAD (2026-11-02): the vLLM TPU platform plugin built on TorchTPU (torch_tpu).
ref: bf318e424febf494c5a1d6cb0104038548888c4b
wiki_subdir: codebases
source_type: code
languages: [python]
index_shards: ["src/vllm_torchtpu/*"]
catalog: full   # per-module catalog pages, like the other silos in this wiki (citations link to them)
agenda: subsystems
# The repo-root modules are seeded explicitly (kv-cache-layout-and-hbm-budget); the root and kernels/ helper units are dropped.
agenda_exclude:
  - src/vllm_torchtpu
  - src/vllm_torchtpu/kernels
coverage_collapse: ["tests/**", "tests_omni/**", "**/test_*.py", "**/*_test.py", "scripts/**"]
docs: ["README.md", "docs/**/*.md"]
synthesis_focus: "TPU inference performance - how the vLLM platform plugin maps the v1 engine onto TorchTPU: model runner and graph capture/compilation, KV-cache layout and paged/ragged attention kernels, MoE and quantized matmul kernels, the megakernel, speculative decoding, sampling, distributed (TP/EP/DP, disaggregated prefill/decode, multihost), host offload, and the env vars and configs that control them"
---

## Concepts
<!-- Discovery-driven: the subsystem planner proposes the units; entries here pin, rename and add. -->
- **kv-cache-layout-and-hbm-budget** - seeds: `MaterializedKVCache`, `materialize_kv_cache_tensors`, `allocate_raw_kv_cache_tensors`, `materialize_shared_attention_cache`, `build_kernel_block_size_by_group_id`, `BlockMajorPoolLayout`, `unified_block_major_enabled`, `normalize_kv_cache_specs_for_tpu`, `PooledGDNStateLayout`, `derive_pooled_gdn_state_layout`, `GqaPaddingSpec`, `compute_padded_gqa_heads`, `HbmBudget`, `compute_hbm_budget`, `estimate_kv_connector_hbm_reserve`, `set_libtpu_flag_default`, `patch_default_model_loader_page_cache`, `patch_moe_expert_write_staging`
- **tpu-model-runner** - seeds: (subsystem: src/vllm_torchtpu/runner)
- **tpu-schedulers** - seeds: (subsystem: src/vllm_torchtpu/core)
- **tpu-platform** - seeds: (subsystem: src/vllm_torchtpu/platforms)
- **compilation-and-graph-capture** - seeds: (subsystem: src/vllm_torchtpu/compilation)
- **attention-and-layer-core** - seeds: (subsystem: src/vllm_torchtpu/layers/core)
- **vllm-layer-adapters** - seeds: (subsystem: src/vllm_torchtpu/layers/adapter)
- **quantization-methods** - seeds: (subsystem: src/vllm_torchtpu/layers/adapter/quantization)
- **custom-ops** - seeds: (subsystem: src/vllm_torchtpu/layers/adapter/custom_ops)
- **ragged-paged-attention-kernel** - seeds: (subsystem: src/vllm_torchtpu/kernels/ragged_paged_attention)
- **batched-ragged-paged-attention-kernel** - seeds: (subsystem: src/vllm_torchtpu/kernels/experimental/batched_rpa)
- **pcp-streaming-rpa-kernel** - seeds: (subsystem: src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa)
- **mla-attention-kernels** - seeds: (subsystem: src/vllm_torchtpu/kernels/mla)
- **fused-moe-kernels** - seeds: (subsystem: src/vllm_torchtpu/kernels/fused_moe)
- **adaptive-fused-moe-kernel** - seeds: (subsystem: src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe)
- **gated-deltanet-kernels** - seeds: (subsystem: src/vllm_torchtpu/kernels/gdn)
- **gdn-pcp-fused-kernel** - seeds: (subsystem: src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused)
- **sparsecore-ragged-gather-scatter** - seeds: (subsystem: src/vllm_torchtpu/kernels/sparse_core)
- **deepseek-v4-compress-and-store-kernel** - seeds: (subsystem: src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store)
- **deepseek-v4-streamindex-topk-kernel** - seeds: (subsystem: src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk)
- **kimi-k3-kernels** - seeds: (subsystem: src/vllm_torchtpu/kernels/kimi_k3)
- **megakernel** - seeds: (subsystem: src/vllm_torchtpu/megakernel)
- **megakernel-pool** - seeds: (subsystem: src/vllm_torchtpu/megakernel/pool)
- **distributed-parallelism-and-meshes** - seeds: `ChipTopology`, `get_chip_topology`, `hierarchical_moe_split`, `get_or_create_dcp_mesh`, `get_dcp_group_layout`, `cp_lse_ag_out_rs`, `build_ep_mesh`, `ep_rank_order`, `ep_sorted_gather_group`, `ep_token_replica_groups`, `get_intra_chip_group`, `CpGroupLayout`, `get_cp_group_layout`, `get_stage_mesh`, `install_pallas_shape_conversion`, `get_or_create_pcp_mesh`, `get_pcp_group_layout`, `all_gather_equal_tokens`, `resolve_pcp_topology_order`, `patch_executor_for_pp_ring`, `patch_executor_for_pp_wave`, `PPRing`, `PPWave`, `get_or_create_pp_mesh`, `pp_permute_op`, `sharded_jax_op`, `TpuDeviceCommunicator`, `prepare_mp_multihost_env`
- **kv-transfer-and-disaggregated-serving** - seeds: (subsystem: src/vllm_torchtpu/distributed/kv_transfer)
- **host-offload** - seeds: (subsystem: src/vllm_torchtpu/offload)
- **speculative-decoding** - seeds: (subsystem: src/vllm_torchtpu/spec_decode)
- **vllm-model-patches** - seeds: (subsystem: src/vllm_torchtpu/models/vllm)
- **deepseek-v4-model** - seeds: (subsystem: src/vllm_torchtpu/models/vllm/deepseek_v4)
- **kimi-k3-model** - seeds: (subsystem: src/vllm_torchtpu/models/vllm/kimi_k3)
- **omni-diffusion-support** - seeds: (subsystem: src/vllm_torchtpu/omni)
- **tracing-annotations** - seeds: (subsystem: src/vllm_torchtpu/tracing)
- **model-export-and-rust-launcher** - seeds: (subsystem: src/vllm_torchtpu/experimental)
