---
title: 'Module: src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/vmem_ldst.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/vmem_ldst.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.experimental.gdn_pcp_fused.vmem_ldst`/
symbols:
  load_and_select_states: load_and_select_states().
  load_activation_as_large: load_activation_as_large().
  load_activation_as_compact: load_activation_as_compact().
  load_strided_heads: load_strided_heads().
  load_compact_heads: load_compact_heads().
  load_compact_to_large: load_compact_to_large().
---
# Module: [`src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/vmem_ldst.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/vmem_ldst.py)

## Functions
- <a id="load_activation_as_compact"></a>`load_activation_as_compact(qkv_vreg: jax.Array, qkv_vmem_ref: jax.Ref, b_vmem_ref: jax.Ref, a_vmem_ref: jax.Ref, cfgs: config.GDNConfig)` — [`L181`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/vmem_ldst.py#L181) — Load activations from VMEM as a compact layout. — documented in [gdn-pcp-fused-kernel](../../../../../../concepts/gdn-pcp-fused-kernel.md)
- <a id="load_activation_as_large"></a>`load_activation_as_large(qkv_vreg: jax.Array, qkv_vmem_ref: jax.Ref, b_vmem_ref: jax.Ref, a_vmem_ref: jax.Ref, cfgs: config.GDNConfig)` — [`L207`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/vmem_ldst.py#L207) — Load activations from VMEM as a large layout. — documented in [gdn-pcp-fused-kernel](../../../../../../concepts/gdn-pcp-fused-kernel.md)
- <a id="load_and_select_states"></a>`load_and_select_states(metadata_ref: memory_ref.MetadataRef, p_id: jax.Array, conv_state_in_slot_ref: jax.Ref, recurrent_in_slot_ref: jax.Ref, carry_conv_scratch_ref: jax.Ref | None, carry_recurrent_scratch_ref: jax.Ref | None, cfg: config.GDNConfig)` — [`L101`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/vmem_ldst.py#L101) — Load correct states from HBM or prior tile, and masks invalid states. — documented in [gdn-pcp-fused-kernel](../../../../../../concepts/gdn-pcp-fused-kernel.md)
- <a id="load_compact_heads"></a>`load_compact_heads(vmem_ref: jax.Ref, num_heads: int, head_dim: int, dim_offset: int = 0)` — [`L59`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/vmem_ldst.py#L59) — Use contiguous slices to split heads along the last dim and stack.
- <a id="load_compact_to_large"></a>`load_compact_to_large(vmem_ref: jax.Ref)` — [`L81`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/vmem_ldst.py#L81) — Use strided load to convert compact to large layout without transpose.
- <a id="load_strided_heads"></a>`load_strided_heads(vmem_ref: jax.Ref, num_heads: int, head_dim: int, lane_offset: int = 0)` — [`L29`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/vmem_ldst.py#L29) — Use strided LDST to split heads along the last dim and transpose.

