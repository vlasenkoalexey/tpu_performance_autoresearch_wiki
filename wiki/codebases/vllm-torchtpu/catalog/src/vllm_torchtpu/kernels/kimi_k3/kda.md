---
title: 'Module: src/vllm_torchtpu/kernels/kimi_k3/kda.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/kimi_k3/kda.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.kimi_k3.kda`/
symbols:
  ragged_kda: ragged_kda().
  ragged_kda.step: ragged_kda().step().
  kda_step: kda_step().
---
# Module: [`src/vllm_torchtpu/kernels/kimi_k3/kda.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/kda.py)

## Functions
- <a id="kda_step"></a>`kda_step(query: jax.Array, key: jax.Array, value: jax.Array, raw_gate: jax.Array, beta: jax.Array, output_gate: jax.Array, state: jax.Array, decay: jax.Array, dt_bias: jax.Array, norm_weight: jax.Array, *, lower_bound: float | None, eps: float)` — [`L22`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/kda.py#L22) — One fp32 KDA recurrence step, shared by the kernel and tests.
- <a id="ragged_kda"></a>`ragged_kda(mixed_qkv: jax.Array, raw_gate: jax.Array, beta: jax.Array, output_gate: jax.Array, recurrent_state: jax.Array, a_log: jax.Array, dt_bias: jax.Array, norm_weight: jax.Array, query_start_loc: jax.Array, state_indices: jax.Array, seq_lens: jax.Array, *, lower_bound: float | None, eps: float)` — [`L72`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/kda.py#L72) — Run KDA over flattened ragged requests and update their recurrent state. — documented in [kimi-k3-kernels](../../../../../concepts/kimi-k3-kernels.md)
- <a id="ragged_kda.step"></a>`step(state, inputs)` — [`L136`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/kda.py#L136) — documented in [kimi-k3-kernels](../../../../../concepts/kimi-k3-kernels.md)

