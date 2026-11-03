---
title: 'Module: src/vllm_torchtpu/kernels/gdn/v3/compute_kda.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/gdn/v3/compute_kda.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.gdn.v3.compute_kda`/
symbols:
  recurrent_kda: recurrent_kda().
  chunked_kda: chunked_kda().
  chunked_kda_per_seq: chunked_kda_per_seq().
  recurrent_kda_per_seq: recurrent_kda_per_seq().
  activate_gate: activate_gate().
  _l2_norm_f32: _l2_norm_f32().
---
# Module: [`src/vllm_torchtpu/kernels/gdn/v3/compute_kda.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/compute_kda.py)

## Functions
- <a id="_l2_norm_f32"></a>`_l2_norm_f32(x: jax.Array, eps: float = 0.000001)` — [`L29`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/compute_kda.py#L29) — L2-normalize along the last dim, accumulating in float32.
- <a id="activate_gate"></a>`activate_gate(a: jax.Array, a_log: jax.Array, dt_bias: jax.Array, cfg: config.GDNConfig)` — [`L42`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/compute_kda.py#L42) — Turn the raw gate `a` into a per-channel log-decay.
- <a id="chunked_kda"></a>`chunked_kda(real_sizes: jax.Array, q_large: jax.Array, k_large: jax.Array, v_large: jax.Array, b_large: jax.Array, a_large: jax.Array, state_prev: jax.Array, a_log: jax.Array, dt_bias: jax.Array, cfg: config.GDNConfig)` — [`L301`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/compute_kda.py#L301) — documented in [gated-deltanet-kernels](../../../../../../concepts/gated-deltanet-kernels.md)
- <a id="chunked_kda_per_seq"></a>`chunked_kda_per_seq(q_large: jax.Array, k_large: jax.Array, v_large: jax.Array, gating_log: jax.Array, beta: jax.Array, state_prev: jax.Array, cfg: config.GDNConfig)` — [`L66`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/compute_kda.py#L66) — documented in [gated-deltanet-kernels](../../../../../../concepts/gated-deltanet-kernels.md)
- <a id="recurrent_kda"></a>`recurrent_kda(real_sizes: jax.Array, q_compact: jax.Array, k_compact: jax.Array, v_compact: jax.Array, b_compact: jax.Array, a_compact: jax.Array, state_prev: jax.Array, a_log: jax.Array, dt_bias: jax.Array, cfg: config.GDNConfig)` — [`L425`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/compute_kda.py#L425) — documented in [gated-deltanet-kernels](../../../../../../concepts/gated-deltanet-kernels.md)
- <a id="recurrent_kda_per_seq"></a>`recurrent_kda_per_seq(q: jax.Array, k: jax.Array, v: jax.Array, gating_decay: jax.Array, beta: jax.Array, state: jax.Array, cfgs: config.GDNConfig)` — [`L362`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/compute_kda.py#L362) — Run the token recurrence and retain one state per verify position.

