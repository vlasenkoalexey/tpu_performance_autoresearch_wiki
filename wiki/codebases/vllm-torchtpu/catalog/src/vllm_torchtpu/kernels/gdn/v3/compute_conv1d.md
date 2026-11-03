---
title: 'Module: src/vllm_torchtpu/kernels/gdn/v3/compute_conv1d.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/gdn/v3/compute_conv1d.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.gdn.v3.compute_conv1d`/
symbols:
  causal_conv1d: causal_conv1d().
---
# Module: [`src/vllm_torchtpu/kernels/gdn/v3/compute_conv1d.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/compute_conv1d.py)

## Functions
- <a id="causal_conv1d"></a>`causal_conv1d(real_sizes: jax.Array, lhs: jax.Array, conv_weight: jax.Array, conv_bias: jax.Array | None, cfg: config.GDNConfig)` — [`L21`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/compute_conv1d.py#L21) — Perform causal Conv1D. Returns Conv1D output and convolution states. — documented in [gated-deltanet-kernels](../../../../../../concepts/gated-deltanet-kernels.md)

