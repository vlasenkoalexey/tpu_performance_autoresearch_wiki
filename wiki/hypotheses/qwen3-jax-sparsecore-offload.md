---
title: "Qwen3 jax — SparseCore collective offload"
type: hypothesis
model: qwen3-cc-jax
variants: ["8B/v6e-8"]
status: refuted
expected_gain: "3-5% throughput / MFU"
confidence: high
effort: S
origin: 2026-06-02-qwen3-jax-v035-maxtext-ce-s8k-bs3
created: 2026-06-02
updated: 2026-06-02
---

# Qwen3 jax — SparseCore collective offload

*Hypothesis*: Offloading the FSDP collectives (all-gather, reduce-scatter, and all-reduce) from the TensorCore onto the SparseCore (by setting `xla_tpu_enable_sparse_core_collective_offload_{all_reduce,reduce_scatter,all_gather}=true`) will reclaim valuable TensorCore cycles for matmul computation, increasing training throughput.

*Rationale*: This matches the [Llama 3 playbook](../../experiments/llama3_8B_autoresearch_optimization/README.md) breakthrough where offloading all three collectives delivered a **+3.4%** throughput lift. At batch size 3, we are compute-and-collectives bound, so clearing TC cycles of communication overhead is highly promising.

*Proposed experiment*: Apply the SparseCore offload XLA flags on top of the `v035` configuration and measure the throughput and step time delta.

*Falsification criterion*: Step time does not decrease, or compilation fails/hangs → refuted.

---

## Result

Refuted by [2026-06-02-qwen3-jax-v036-sc-bs3](../experiments/qwen3_ag_autoresearch_optimization/jax/experiments/2026-06-02-qwen3-jax-v036-sc-bs3.md). Offloading all three collectives resulted in a minor throughput and step time regression (-0.6% / +23.3ms), because JAX's default collective scheduling/pipelining is already extremely efficient at overlapping communication with compute, and moving them to SparseCore introduced transfer and latency overhead that outweighed any savings.

