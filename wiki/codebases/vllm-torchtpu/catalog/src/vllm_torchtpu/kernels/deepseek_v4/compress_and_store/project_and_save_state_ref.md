---
title: 'Module: src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/project_and_save_state_ref.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/project_and_save_state_ref.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.deepseek_v4.compress_and_store.project_and_save_state_ref`/
symbols:
  ref_wkv_proj_and_save_state: ref_wkv_proj_and_save_state().
---
# Module: [`src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/project_and_save_state_ref.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/project_and_save_state_ref.py)

## Functions
- <a id="ref_wkv_proj_and_save_state"></a>`ref_wkv_proj_and_save_state(hidden_states: jax.Array, wkv_wgate: jax.Array, ape: jax.Array, positions: jax.Array, slot_mapping: jax.Array, cache: jax.Array, state_block_size: int, head_dim: int, compress_ratio: int, overlap: bool)` — [`L19`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/project_and_save_state_ref.py#L19) — Golden JAX reference for Kernel 1 (proj + save state).

