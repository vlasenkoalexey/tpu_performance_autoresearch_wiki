---
title: Experiments folder contract (core vs experiments)
type: doc-concept
provenance: doc
source: torchtitan/experiments/README.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T06:34:20Z}
---
# Experiments folder contract (core vs experiments)

## Definition
`torchtitan/experiments/` hosts optional, independently owned experiments - a new model architecture with its parallelization functions, or an enhancement to the infrastructure. Everything outside `experiments/` is "core". The contract is that the dependency is **one-way** (experiments import core, never the reverse), each experiment reuses core extension points instead of copy-pasting, and an experiment may carry its own dependencies and tests but not vendor-proprietary kernels.

## In torchtitan (grounded)
- An experiment plugs into core through a new [`ModelSpec`](../catalog/torchtitan/protocols/model_spec.md#ModelSpec) and the core [`Trainer`](../catalog/torchtitan/trainer.md#Trainer) (or a subclass of it), which is exactly what the lanes in this fork do: [`GraphTrainer`](../catalog/torchtitan/experiments/graph_trainer/trainer.md#GraphTrainer), [`FaultTolerantTrainer`](../catalog/torchtitan/experiments/torchft/trainer.md#FaultTolerantTrainer), [`TransformersBackendConfig`](../catalog/torchtitan/experiments/transformers_modeling_backend/config_registry.md#TransformersBackendConfig) all extend `Trainer` / `Trainer.Config`.
- `--module <name>` resolution: [`ConfigManager`](../catalog/torchtitan/config/manager.md#ConfigManager) unions the core model list with [`_supported_experiments`](../catalog/torchtitan/experiments/__init__.md#_supported_experiments) and searches `torchtitan.models`, then `torchtitan.experiments`, then `torchtitan.experiments.rl.examples` for a `config_registry`. Adding an experiment therefore means registering its module name there.

## Why it matters / when it applies
- The one-way rule is what lets the TPU backend (`experiments/tpu`) and the JAX lane live in this fork without touching core: core development is never blocked by an experiment breaking.
- Contributors are expected to justify an experiment with performance and loss-convergence reports, and experiments are removed when stale or once their findings are upstreamed.
- The "no vendor-specific kernels in a proprietary language" rule is why kernel-heavy lanes keep kernels as dependencies (the TPU lane's Pallas kernels are open-source JAX/Pallas, see [tpu-pallas-kernels](../concepts/tpu-pallas-kernels.md)).

**Doc vs code at this commit:**
- The README's "Current experiments" table lists only graph_trainer, torchft, transformers_modeling_backend and rl. It omits `jax/` and `tpu/`, the two TPU lanes this fork exists for (both have their own entry points rather than a `--module` registration).
- `_supported_experiments` still lists `autoparallel.llama3` and `autoparallel.local_map_deepseek_v3`, but there is no `experiments/autoparallel/` directory; AutoParallel now lives inside graph_trainer (see [graph-trainer-autoparallel](graph-trainer-autoparallel.md)).
- The README points at `docs/extension.md` for the extension-point list; there is no top-level `docs/` directory in this checkout.

## Connections
- Code concepts: [model-spec-protocols](../concepts/model-spec-protocols.md), [trainer-and-train-loop](../concepts/trainer-and-train-loop.md), [job-config](../concepts/job-config.md), [graph-trainer](../concepts/graph-trainer.md), [jax-lane](../concepts/jax-lane.md), [rl-training](../concepts/rl-training.md), [tpu-trainer-and-job-config](../concepts/tpu-trainer-and-job-config.md)
- Module catalogs: [protocols/model_spec](../catalog/torchtitan/protocols/model_spec.md), [config/manager](../catalog/torchtitan/config/manager.md), [experiments/__init__](../catalog/torchtitan/experiments/__init__.md)
- Related doc-concepts: [graph-trainer-full-step-graph-capture](graph-trainer-full-step-graph-capture.md), [jax-flax-nnx-lane](jax-flax-nnx-lane.md), [titanrl-architecture](titanrl-architecture.md), [torchft-replica-group-fault-tolerance](torchft-replica-group-fault-tolerance.md), [transformers-modeling-backend](transformers-modeling-backend.md)

## Source
Extracted from `torchtitan/experiments/README.md` (kept in place).
