---
title: 'Module: src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/kernel.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/kernel.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.experimental.gdn_pcp_fused.kernel`/
symbols:
  inner_kernel: inner_kernel().
---
# Module: [`src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/kernel.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/kernel.py)

## Functions
- <a id="inner_kernel"></a>`inner_kernel(qkv_slot_ref: jax.Ref, b_slot_ref: jax.Ref, a_slot_ref: jax.Ref, conv_state_in_slot_ref: jax.Ref, recurrent_in_slot_ref: jax.Ref, out_slot_ref: jax.Ref, conv_state_out_slot_ref: jax.Ref, recurrent_out_slot_ref: jax.Ref, metadata_ref: memory_ref.MetadataRef, weights_ref: memory_ref.WeightRefs, carry_conv_scratch_ref: jax.Ref | None, carry_recurrent_scratch_ref: jax.Ref | None, *, cfg: config.GDNConfig, p_id: jax.Array | None = None)` — [`L37`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/kernel.py#L37) — Orchestrates computation of Conv1D and GDN for a single tile. — documented in [gdn-pcp-fused-kernel](../../../../../../concepts/gdn-pcp-fused-kernel.md)

