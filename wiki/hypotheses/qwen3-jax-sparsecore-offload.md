---
title: "Qwen3 jax — SparseCore collective offload"
type: hypothesis
model: qwen3-cc-jax
variants: ["8B/v6e-8"]
status: refuted
expected_gain: "3-5% throughput (relay FSDP collectives off the TensorCore)"
confidence: medium
effort: S
origin: 2026-06-02-qwen3-jax-v6e8-baseline
created: 2026-06-02
updated: 2026-06-02
---

# Qwen3 jax — SparseCore collective offload

*Hypothesis*: Enabling `xla_tpu_enable_sparse_core_collective_offload_{all_reduce,reduce_scatter,all_gather}=true`
(via `LIBTPU_INIT_ARGS`) relays the FSDP collectives off the TensorCore onto the
SparseCore, freeing TC cycles for matmul and lifting throughput — flag-only, no
code change.

*Mechanism*: The [baseline profile](../experiments/qwen3_cc_autoresearch_optimization/jax/experiments/2026-06-02-qwen3-jax-v6e8-baseline.md)
shows the FSDP collective (`collective-permute-done`) at **21.7%** of the step.
SparseCore offload was the +3.4% lever on the llama3 jax lane (exp 27/28).

*Predicted signal*: the collective op's TC time-share drops; tok/s/chip rises a
few percent; MXU util rises slightly.

*Falsification criterion*: no throughput change beyond noise (flag inert on this
libtpu/shape) or a regression → refuted.
