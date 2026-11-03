---
title: 'Module: src/vllm_torchtpu/kernels/diffusion_attention/block_sizes.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/diffusion_attention/block_sizes.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.diffusion_attention.block_sizes`/
symbols:
  detect_spec: detect_spec().
  autotune_block_sizes: autotune_block_sizes().
  spec_from_tpu_info: spec_from_tpu_info().
  _vmem_max_block_q: _vmem_max_block_q().
  V7_SPEC: V7_SPEC.
  _search_block_q: _search_block_q().
  TpuSpec.mxu_dim: TpuSpec#mxu_dim.
  tile_grid_cost: tile_grid_cost().
  TpuSpec: TpuSpec#
  TpuSpec.vmem_bytes: TpuSpec#vmem_bytes.
  TpuSpec.safe_kv_block: TpuSpec#safe_kv_block.
  TpuSpec.generation: TpuSpec#generation.
  TpuSpec.usable_vmem_fraction: TpuSpec#usable_vmem_fraction.
  TpuSpec.name: TpuSpec#name.
  TpuSpec.num_lanes: TpuSpec#num_lanes.
  _logger: _logger.
  _SAFE_KV_BLOCK_MULTIPLE: _SAFE_KV_BLOCK_MULTIPLE.
  _DEFAULT_USABLE_VMEM_FRACTION: _DEFAULT_USABLE_VMEM_FRACTION.
  _VMEM_RESERVE_BYTES: _VMEM_RESERVE_BYTES.
  _FIXED_M_KERNEL_MODES: _FIXED_M_KERNEL_MODES.
  _KNOWN_GENERATIONS: _KNOWN_GENERATIONS.
  score_tile_bytes: score_tile_bytes().
  vmem_footprint_bytes: vmem_footprint_bytes().
  _FIXED_M_VMEM_FRACTION._FIXED_M_VMEM_FRACTION: _FIXED_M_VMEM_FRACTION._FIXED_M_VMEM_FRACTION.
---
# Module: [`src/vllm_torchtpu/kernels/diffusion_attention/block_sizes.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/diffusion_attention/block_sizes.py)

## Classes
### <a id="TpuSpec"></a>`TpuSpec`
- def: [`src/vllm_torchtpu/kernels/diffusion_attention/block_sizes.py:107`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/diffusion_attention/block_sizes.py#L107)
- doc: Hardware parameters that drive the block-size derivation.
- signature: `class TpuSpec:`
- members:
  - <a id="TpuSpec.generation"></a>`generation` — [`L126`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/diffusion_attention/block_sizes.py#L126)
  - <a id="TpuSpec.mxu_dim"></a>`mxu_dim` — [`L128`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/diffusion_attention/block_sizes.py#L128)
  - <a id="TpuSpec.name"></a>`name` — [`L125`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/diffusion_attention/block_sizes.py#L125)
  - <a id="TpuSpec.num_lanes"></a>`num_lanes` — [`L131`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/diffusion_attention/block_sizes.py#L131)
  - <a id="TpuSpec.safe_kv_block"></a>`safe_kv_block` — [`L129`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/diffusion_attention/block_sizes.py#L129)
  - <a id="TpuSpec.usable_vmem_fraction"></a>`usable_vmem_fraction` — [`L130`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/diffusion_attention/block_sizes.py#L130)
  - <a id="TpuSpec.vmem_bytes"></a>`vmem_bytes` — [`L127`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/diffusion_attention/block_sizes.py#L127)
- uses (calls/refs, reference-scoped): [`_DEFAULT_USABLE_VMEM_FRACTION`](block_sizes.md#_DEFAULT_USABLE_VMEM_FRACTION)
- used by: [`detect_spec`](block_sizes.md#detect_spec), [`flash_attention_bshd`](kernel.md#flash_attention_bshd), [`autotune_block_sizes`](block_sizes.md#autotune_block_sizes), [`spec_from_tpu_info`](block_sizes.md#spec_from_tpu_info), [`_vmem_max_block_q`](block_sizes.md#_vmem_max_block_q), [`V7_SPEC`](block_sizes.md#V7_SPEC), [`_search_block_q`](block_sizes.md#_search_block_q), [`tile_grid_cost`](block_sizes.md#tile_grid_cost), [`_splash_vmem_limit_bytes`](kernel.md#_splash_vmem_limit_bytes)

## Functions
- <a id="_search_block_q"></a>`_search_block_q(seq_len: int, block_kv_compute: int, block_kv: int, head_dim: int, bytes_per_element: int, spec: TpuSpec, kv_seq_len: int | None = None)` — [`L331`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/diffusion_attention/block_sizes.py#L331) — Cost-model search for block_q over the VMEM-feasible range.
- <a id="_vmem_max_block_q"></a>`_vmem_max_block_q(seq_len: int, block_kv_compute: int, block_kv: int, head_dim: int, bytes_per_element: int, spec: TpuSpec)` — [`L260`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/diffusion_attention/block_sizes.py#L260) — Largest block_q (multiple of mxu_dim, <= seq) that fits VMEM.
- <a id="autotune_block_sizes"></a>`autotune_block_sizes(seq_len: int, head_dim: int = 128, bytes_per_element: int = 2, spec: TpuSpec | None = None, kv_seq_len: int | None = None, kernel_mode: str = "online")` — [`L384`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/diffusion_attention/block_sizes.py#L384) — Derives custom-splash block sizes for a sequence length.
- <a id="detect_spec"></a>`detect_spec()` — [`L168`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/diffusion_attention/block_sizes.py#L168) — Returns the TpuSpec for the attached accelerator.
- <a id="score_tile_bytes"></a>`score_tile_bytes(block_q: int, block_kv_compute: int, head_dim: int, block_kv: int, bytes_per_element: int = 2)` — [`L201`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/diffusion_attention/block_sizes.py#L201) — Estimates the VMEM footprint of one kernel step in bytes.
- <a id="spec_from_tpu_info"></a>`spec_from_tpu_info(info: Any)` — [`L144`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/diffusion_attention/block_sizes.py#L144) — Builds a TpuSpec from a ``get_tpu_info()`` result.
- <a id="tile_grid_cost"></a>`tile_grid_cost(seq_len: int, kv_seq_len: int, block_q: int, block_kv: int, spec: TpuSpec)` — [`L294`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/diffusion_attention/block_sizes.py#L294) — Model cost of a (block_q, block_kv) tile grid (lower is better).
- <a id="vmem_footprint_bytes"></a>`vmem_footprint_bytes(block_q: int, block_kv_compute: int, head_dim: int, block_kv: int)` — [`L230`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/diffusion_attention/block_sizes.py#L230) — Upper bound on the VMEM one kernel instance allocates, in bytes.

## Module values
- <a id="V7_SPEC"></a>`V7_SPEC` — [`L135`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/diffusion_attention/block_sizes.py#L135)
- <a id="_DEFAULT_USABLE_VMEM_FRACTION"></a>`_DEFAULT_USABLE_VMEM_FRACTION` — [`L87`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/diffusion_attention/block_sizes.py#L87)
- <a id="_FIXED_M_KERNEL_MODES"></a>`_FIXED_M_KERNEL_MODES` — [`L95`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/diffusion_attention/block_sizes.py#L95)
- <a id="_FIXED_M_VMEM_FRACTION._FIXED_M_VMEM_FRACTION"></a>`_FIXED_M_VMEM_FRACTION` — [`L99`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/diffusion_attention/block_sizes.py#L99)
- <a id="_KNOWN_GENERATIONS"></a>`_KNOWN_GENERATIONS` — [`L103`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/diffusion_attention/block_sizes.py#L103)
- <a id="_SAFE_KV_BLOCK_MULTIPLE"></a>`_SAFE_KV_BLOCK_MULTIPLE` — [`L86`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/diffusion_attention/block_sizes.py#L86)
- <a id="_VMEM_RESERVE_BYTES"></a>`_VMEM_RESERVE_BYTES` — [`L90`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/diffusion_attention/block_sizes.py#L90)
- <a id="_logger"></a>`_logger` — [`L80`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/diffusion_attention/block_sizes.py#L80)

