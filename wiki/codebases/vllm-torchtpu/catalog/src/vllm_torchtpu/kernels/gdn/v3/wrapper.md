---
title: 'Module: src/vllm_torchtpu/kernels/gdn/v3/wrapper.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/gdn/v3/wrapper.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.gdn.v3.wrapper`/
symbols:
  fused_conv1d_gdn.call_kernel: fused_conv1d_gdn().call_kernel().
  inner_kernel: inner_kernel().
  fused_conv1d_gdn: fused_conv1d_gdn().
  outer_kernel: outer_kernel().
  logger: logger.
  outer_kernel._run: outer_kernel()._run().
---
# Module: [`src/vllm_torchtpu/kernels/gdn/v3/wrapper.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/wrapper.py)

## Functions
- <a id="outer_kernel._run"></a>`_run(allocations)` — [`L289`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/wrapper.py#L289)
- <a id="fused_conv1d_gdn.call_kernel"></a>`call_kernel(in_states: jax.Array | tuple[jax.Array, jax.Array], in_act: jax.Array | None, mode: config.GDNMode)` — [`L631`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/wrapper.py#L631) — documented in [gated-deltanet-kernels](../../../../../../concepts/gated-deltanet-kernels.md)
- <a id="fused_conv1d_gdn"></a>`fused_conv1d_gdn(qkv: jax.Array, b: jax.Array, a: jax.Array, states: jax.Array | tuple[jax.Array, jax.Array], conv_weight: jax.Array, conv_bias: jax.Array | None, a_log: jax.Array, dt_bias: jax.Array, query_start_loc: jax.Array, state_indices: jax.Array, distribution: jax.Array, seq_lens: jax.Array, read_offsets: jax.Array | None = None, ckpt_indices: jax.Array | None = None, *, n_kq: int, n_v: int, d_k: int, d_v: int, kernel_size: int, attention_mode: config.AttentionMode = config.AttentionMode.GDN, gate_lower_bound: float | None = None, recurrent_dtype: jnp.dtype | None = None, conv_dtype: jnp.dtype | None = None, num_spec_tokens: int = 0, batched_only: bool = False, prefill_only: bool = False, zero_initialize_out: bool = True, compute_precision: jnp.dtype = jnp.float32.dtype, kernel_act_dtype: jnp.dtype = jnp.float32.dtype, kernel_conv_weight_dtype: jnp.dtype = jnp.float32.dtype, decode_tile_size: int = 4, mixed_tile_size: int = 64)` — [`L333`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/wrapper.py#L333) — Perform conv1d and gdn in a single fused kernel. — documented in [custom-ops](../../../../../../concepts/custom-ops.md)
- <a id="inner_kernel"></a>`inner_kernel(qkv_slot_ref: jax.Ref, b_slot_ref: jax.Ref, a_slot_ref: jax.Ref, conv_state_in_slot_ref: jax.Ref, recurrent_in_slot_ref: jax.Ref, out_slot_ref: jax.Ref, conv_state_out_slot_ref: jax.Ref, recurrent_out_slot_ref: jax.Ref, metadata_ref: memory_ref.MetadataRef, weights_ref: memory_ref.WeightRefs, carry_conv_scratch_ref: jax.Ref | None, carry_recurrent_scratch_ref: jax.Ref | None, *, cfg: config.GDNConfig, p_id: jax.Array | None = None)` — [`L38`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/wrapper.py#L38) — Orchestrates computation of Conv1D and GDN for a single tile. — documented in [gated-deltanet-kernels](../../../../../../concepts/gated-deltanet-kernels.md)
- <a id="outer_kernel"></a>`outer_kernel(metadata_ref: memory_ref.MetadataRef, qkv_ref: jax.Array, b_ref: jax.Array, a_ref: jax.Array, states_ref: jax.Array | tuple[jax.Array, jax.Array], _: jax.Array, weights_ref: memory_ref.WeightRefs, out_ref: jax.Array, states_out_ref: jax.Array | tuple[jax.Array, jax.Array], carry_conv_scratch_ref: jax.Array | None, carry_recurrent_scratch_ref: jax.Array | None, *, cfg: config.GDNConfig)` — [`L211`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/wrapper.py#L211) — Setup memory allocations and emit pipeline for running inner_kernel. — documented in [gated-deltanet-kernels](../../../../../../concepts/gated-deltanet-kernels.md)

## Module values
- <a id="logger"></a>`logger` — [`L35`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/wrapper.py#L35)

