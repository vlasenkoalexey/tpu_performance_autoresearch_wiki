---
title: "MaxText Qwen3-8B v6e-8 reference baseline @ seq8192"
type: experiment
hypothesis: qwen3-maxtext-reference-baseline
model: qwen3-cc-maxtext
variant: "8B/v6e-8"
commit: 9f1820b47
status: in_progress
tags: [qwen3-cc, maxtext, v6e-8, reference, baseline, seq8192]
created: 2026-06-02
updated: 2026-06-02
---

# MaxText Qwen3-8B v6e-8 reference baseline @ seq8192

## Hypothesis under test

**Hypothesis**: Upstream MaxText running `qwen3-8b.yml` on v6e-8 at the proven dense-8B recipe tuning
(seq8192, bs3, remat-custom + decoder/proj offloads, splash `sa_block_*=2048` + fused bwd, HOST_OFFLOAD +
SparseCore-offload + DISABLE_COLLECTIVE_MATMUL XLA stack) establishes the **reference-ceiling MFU** for
Qwen3-8B — the apples-to-apples number our hand-tuned jax (30.4% @ seq8192) and torchax (19.2%) lanes are
measured against. Expectation (by analogy to MaxText Llama-3.1-8B = 44.6% on this cluster): ~40–45% MFU.

**Mechanism**: `benchmark_runner xpk --model_name=qwen3_8b_8192_ref --base_docker_image=maxtext_base_image`
from the `tpu-recipes-v0.1.4` worktree (config mirrors `llama3_1-8b-8192-no-collective-matmul`; only
`model_type` differs → `qwen3-8b`, which adds QK-norm via the model YAML).

**Predicted signal**: steady-state TFLOP/s/device → MFU in the ~40–45% range; clean 20-step run; monotone
loss on synthetic data; xplane profile captured (steps 11–15).

**Falsification criterion**: this is a reference-establishment baseline — verdict `supported` if it runs
clean and yields a stable MFU number (the number itself is the deliverable, not a beat-the-frontier test).
`invalid` if it crashes (config/tokenizer/shape error) before steady state.

## Setup
(populated on completion — actual benchmark_runner command, workload name, tuning params, XLA flags)
## Baseline comparison
(populated on completion — vs jax 30.4% @ seq8192, torchax 19.2%, llama3-maxtext 44.6%)
## Results
(populated on completion)
## Profile
(populated on completion)
## Verdict
(populated on completion)

## Next hypotheses
(populated on completion)
