---
title: 'Module: src/vllm_torchtpu/layers/adapter/custom_ops/kda_attention_op.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/layers/adapter/custom_ops/kda_attention_op.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.layers.adapter.custom_ops.kda_attention_op`/
symbols:
  _pooled_kda_core: _pooled_kda_core().
  build_kimi_pooled_kda_op: build_kimi_pooled_kda_op().
  build_kimi_dispatched_kda_op: build_kimi_dispatched_kda_op().
  _build_fused_core.fused_core: _build_fused_core().fused_core().
  _build_fused_core.fused_core.run_kernel: _build_fused_core().fused_core().run_kernel().
  _build_fused_core: _build_fused_core().
  logger: logger.
  _guard_kda_verify_window: _guard_kda_verify_window().
  _short_conv_tokens: _short_conv_tokens().
  build_kimi_pooled_kda_op.pooled_core: build_kimi_pooled_kda_op().pooled_core().
  _VerifyWindowResult: _VerifyWindowResult.
  kimi_short_conv_scan: kimi_short_conv_scan().
  _token_sequence_ids: _token_sequence_ids().
  _gated_output_norm: _gated_output_norm().
  _check_kda_abi: _check_kda_abi().
  build_kimi_dispatched_kda_op._fake_dispatched: build_kimi_dispatched_kda_op()._fake_dispatched().
  build_kimi_dispatched_kda_op.dispatched_impl: build_kimi_dispatched_kda_op().dispatched_impl().
  build_kimi_pooled_kda_op._fake_pooled: build_kimi_pooled_kda_op()._fake_pooled().
  build_kimi_pooled_kda_op.pooled_impl: build_kimi_pooled_kda_op().pooled_impl().
---
# Module: [`src/vllm_torchtpu/layers/adapter/custom_ops/kda_attention_op.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/kda_attention_op.py)

## Functions
- <a id="_build_fused_core"></a>`_build_fused_core(lower_bound: float | None, eps: float, num_spec_tokens: int = 0)` — [`L322`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/kda_attention_op.py#L322) — The same op, on the fused conv1d + GDN v3 kernel. — documented in [custom-ops](../../../../../../concepts/custom-ops.md)
- <a id="_check_kda_abi"></a>`_check_kda_abi(mixed_qkv: jax.Array, raw_gate: jax.Array, beta: jax.Array, output_gate: jax.Array, recurrent_state: jax.Array, a_log: jax.Array, dt_bias: jax.Array, norm_weight: jax.Array, query_start_loc: jax.Array, state_indices: jax.Array, seq_lens: jax.Array)` — [`L264`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/kda_attention_op.py#L264) — Validate the shared KDA operand contract; return the shape tuple.
- <a id="build_kimi_dispatched_kda_op._fake_dispatched"></a>`_fake_dispatched(mixed_qkv, _raw_gate, _beta, _output_gate, conv_state, recurrent_state, *args, **kwargs)` — [`L465`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/kda_attention_op.py#L465)
- <a id="build_kimi_pooled_kda_op._fake_pooled"></a>`_fake_pooled(mixed_qkv, _raw_gate, _beta, _output_gate, pool, _conv_weight, a_log, _dt_bias, norm_weight, *args, **kwargs)` — [`L833`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/kda_attention_op.py#L833)
- <a id="_gated_output_norm"></a>`_gated_output_norm(output: jax.Array, output_gate: jax.Array, norm_weight: jax.Array, eps: float, activation_dtype)` — [`L250`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/kda_attention_op.py#L250) — Per-head ``o_norm`` followed by the sigmoid output gate.
- <a id="_guard_kda_verify_window"></a>`_guard_kda_verify_window(num_window_reqs: jax.Array, run_verify_window: Callable[[], _VerifyWindowResult], skip_verify_window: Callable[[], _VerifyWindowResult])` — [`L44`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/kda_attention_op.py#L44) — Skip KDA verification when the device-side window is empty.
- <a id="_pooled_kda_core"></a>`_pooled_kda_core(mixed_qkv: jax.Array, raw_gate: jax.Array, beta: jax.Array, output_gate: jax.Array, pool: jax.Array, conv_weight: jax.Array, a_log: jax.Array, dt_bias: jax.Array, norm_weight: jax.Array, query_start_loc: jax.Array, state_indices: jax.Array, seq_lens: jax.Array, distribution: jax.Array, window_distribution: jax.Array | None = None, slot_read_offsets: jax.Array | None = None, ckpt_indices: jax.Array | None = None, *, lower_bound: float | None, eps: float, pool_block_tokens: int, conv_shard_heads: int | None = None, num_spec_tokens: int = 0)` — [`L528`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/kda_attention_op.py#L528) — documented in [custom-ops](../../../../../../concepts/custom-ops.md)
- <a id="_short_conv_tokens"></a>`_short_conv_tokens(x: jax.Array, conv_state: jax.Array, conv_weight: jax.Array, query_start_loc: jax.Array, state_indices: jax.Array, seq_lens: jax.Array, first_seq: jax.Array, first_token: jax.Array, total_tokens: jax.Array)` — [`L154`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/kda_attention_op.py#L154) — The loop-free convolution body. See ``kimi_short_conv_scan``.
- <a id="_token_sequence_ids"></a>`_token_sequence_ids(query_start_loc: jax.Array, num_tokens: int, num_seqs: int)` — [`L53`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/kda_attention_op.py#L53) — Map each token row to the 0-indexed sequence that owns it.
- <a id="build_kimi_dispatched_kda_op"></a>`build_kimi_dispatched_kda_op(prefix: str, *, lower_bound: float | None, eps: float, state_dim_first: bool, num_spec_tokens: int = 0)` — [`L450`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/kda_attention_op.py#L450) — Build fused KDA with separately guarded speculative and prefill segments. — documented in [custom-ops](../../../../../../concepts/custom-ops.md)
- <a id="build_kimi_pooled_kda_op"></a>`build_kimi_pooled_kda_op(prefix: str, *, lower_bound: float | None, eps: float, vllm_config: VllmConfig, num_spec_tokens: int = 0)` — [`L736`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/kda_attention_op.py#L736) — Build the KDA op that reads and writes its state through the pool. — documented in [custom-ops](../../../../../../concepts/custom-ops.md)
- <a id="build_kimi_dispatched_kda_op.dispatched_impl"></a>`dispatched_impl(mixed_qkv: torch.Tensor, raw_gate: torch.Tensor, beta: torch.Tensor, output_gate: torch.Tensor, conv_state: torch.Tensor, recurrent_state: torch.Tensor, conv_weight: torch.Tensor, a_log: torch.Tensor, dt_bias: torch.Tensor, norm_weight: torch.Tensor, query_start_loc: torch.Tensor, state_indices: torch.Tensor, seq_lens: torch.Tensor, distribution: torch.Tensor, window_distribution: torch.Tensor, slot_read_offsets: torch.Tensor)` — [`L485`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/kda_attention_op.py#L485)
- <a id="_build_fused_core.fused_core"></a>`fused_core(mixed_qkv: jax.Array, raw_gate: jax.Array, beta: jax.Array, output_gate: jax.Array, conv_state: jax.Array, recurrent_state: jax.Array, conv_weight: jax.Array, a_log: jax.Array, dt_bias: jax.Array, norm_weight: jax.Array, query_start_loc: jax.Array, state_indices: jax.Array, seq_lens: jax.Array, distribution: jax.Array, window_distribution: jax.Array | None = None, slot_read_offsets: jax.Array | None = None)` — [`L335`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/kda_attention_op.py#L335) — documented in [custom-ops](../../../../../../concepts/custom-ops.md)
- <a id="kimi_short_conv_scan"></a>`kimi_short_conv_scan(x: jax.Array, conv_state: jax.Array, conv_weight: jax.Array, query_start_loc: jax.Array, state_indices: jax.Array, seq_lens: jax.Array, start_seq: jax.Array | int | None = None)` — [`L83`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/kda_attention_op.py#L83) — Kimi short convolution over a ragged batch, without a token loop.
- <a id="build_kimi_pooled_kda_op.pooled_core"></a>`pooled_core(mixed_qkv: jax.Array, raw_gate: jax.Array, beta: jax.Array, output_gate: jax.Array, pool: jax.Array, conv_weight: jax.Array, a_log: jax.Array, dt_bias: jax.Array, norm_weight: jax.Array, query_start_loc: jax.Array, state_indices: jax.Array, seq_lens: jax.Array, distribution: jax.Array, window_distribution: jax.Array | None = None, slot_read_offsets: jax.Array | None = None, ckpt_indices: jax.Array | None = None)` — [`L775`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/kda_attention_op.py#L775)
- <a id="build_kimi_pooled_kda_op.pooled_impl"></a>`pooled_impl(mixed_qkv: torch.Tensor, raw_gate: torch.Tensor, beta: torch.Tensor, output_gate: torch.Tensor, pool: torch.Tensor, conv_weight: torch.Tensor, a_log: torch.Tensor, dt_bias: torch.Tensor, norm_weight: torch.Tensor, query_start_loc: torch.Tensor, state_indices: torch.Tensor, seq_lens: torch.Tensor, distribution: torch.Tensor, window_distribution: torch.Tensor | None = None, slot_read_offsets: torch.Tensor | None = None, ckpt_indices: torch.Tensor | None = None)` — [`L855`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/kda_attention_op.py#L855)
- <a id="_build_fused_core.fused_core.run_kernel"></a>`run_kernel(conv_in, rec_in, *, batched_only=False, prefill_only=False)` — [`L384`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/kda_attention_op.py#L384) — documented in [custom-ops](../../../../../../concepts/custom-ops.md)

## Module values
- <a id="_VerifyWindowResult"></a>`_VerifyWindowResult` — [`L41`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/kda_attention_op.py#L41)
- <a id="logger"></a>`logger` — [`L39`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/kda_attention_op.py#L39)

