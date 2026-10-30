---
title: 'Area: torchtitan/experiments'
type: area
area: 'torchtitan/experiments'
description: 'Experimental lanes of torchtitan: the TorchTPU backend (experiments/tpu), the JAX lane, the graph trainer and RL.'
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T06:34:20Z}
---
# Area: `torchtitan/experiments`

Hand-written area page: wikify's planner treats `experiments/` as non-library and proposes no units for it, so its units are pinned explicitly in `config/torchtitan.md` and listed here.

## Purpose
`torchtitan/experiments/` holds the lanes that are not part of the core trainer. The most important for this wiki is `experiments/tpu`, the TorchTPU backend: a TPU trainer and config layer with libtpu/XLA flag maps ([tpu-trainer-and-job-config](../concepts/tpu-trainer-and-job-config.md)), TPU MoE dispatch and grouped experts ([tpu-moe-dispatch-and-grouped-experts](../concepts/tpu-moe-dispatch-and-grouped-experts.md)), context-parallel attention ([tpu-context-parallel-attention](../concepts/tpu-context-parallel-attention.md)), layer loop / scan, remat policies and layouts ([tpu-layer-loop-remat-and-layouts](../concepts/tpu-layer-loop-remat-and-layouts.md)), Pallas/Tokamax kernels for splash attention, grouped matmul and fused cross-entropy ([tpu-pallas-kernels](../concepts/tpu-pallas-kernels.md)), and the TPU graph trainer with scan, graph splitting and FSDP scheduling passes ([tpu-graph-trainer](../concepts/tpu-graph-trainer.md)). Alongside it sit a JAX lane ([jax-lane](../concepts/jax-lane.md)), the upstream graph trainer ([graph-trainer](../concepts/graph-trainer.md)) and RL training ([rl-training](../concepts/rl-training.md), GPU-only).

## How the units connect
- The TPU lane reuses the core models ([model-building-blocks](../concepts/model-building-blocks.md), family pages) and replaces kernels and `parallelize_fn` at build time; the TPU graph trainer extends [graph-trainer](../concepts/graph-trainer.md).
- `experiments/tpu` subpackages without their own page (catalog-only): per-model TPU recipes (`qwen3`, `llama3`, `deepseek_v3`, `qwen3_5`, `muse_glimmer`, `flux`), `compiled_optimizers` (separately compiled AdamW step), `overrides`, `conformer`, `examples` (Mamba long-context), `rl_nc_ray`, `transformers_modeling_backend`. `experiments/torchft` and `experiments/transformers_modeling_backend` are catalog-only too.
- Module map: [catalog/index.md](../catalog/index.md).
