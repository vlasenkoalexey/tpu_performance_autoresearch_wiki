---
model: qwen3-ag-jax
variants: ["8B/v6e-8"]
status: confirmed
expected_gain: "Enable seqlen=8192 by cutting HBM usage"
confidence: high
effort: S
origin: 2026-06-26-qwen3-jax-v001-splash-refuted
---

# Qwen3 JAX Gradient Checkpointing

## Statement
Rematerializing the forward pass activations during the backward pass will reduce the HBM footprint enough to allow sequence length 8192 to compile and run on a v6e TPU.

## Rationale
The `2026-06-26-qwen3-jax-v001-splash-refuted` experiment failed to compile at seqlen 8192 with an HBM OOM (used 44.80G of 31.25G HBM). Splash attention alone is not enough to fit an 8192 context length without activation rematerialization. Gradient checkpointing (remat) is a standard technique to trade compute for memory.

## Proposed experiment
1. Enable `jax.checkpoint` on the transformer blocks.
2. Run the same seqlen=8192 experiment.
3. Observe if it compiles and fits in HBM.

## Risks
Slightly increased step time due to recomputation, but this is a necessary tradeoff to fit in memory.

## Dependencies
None.
