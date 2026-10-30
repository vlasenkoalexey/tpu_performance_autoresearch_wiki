---
title: TorchTitan-on-TPU distribution model (upstream fork + isolated TPU lane)
type: doc-concept
provenance: doc
source: README.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T06:34:20Z}
---
# TorchTitan-on-TPU distribution model (upstream fork + isolated TPU lane)

## Definition
This repository is Google's distribution of upstream TorchTitan that adds training on Cloud TPU
through the TorchTPU backend. Upstream TorchTitan is kept working as documented and is synced
regularly; everything TPU-specific (recipes, Pallas kernels, the TPU trainer and TPU parallelism
paths) is confined to one directory, `torchtitan/experiments/tpu`.

## In torchtitan (grounded)
- **Shared core (upstream):** the generic trainer [`Trainer`](../catalog/torchtitan/trainer.md#Trainer "torchtitan/trainer.py:L74"),
  its config [`Trainer.Config`](../catalog/torchtitan/trainer.md#Trainer.Config "torchtitan/trainer.py:L76"), the model
  definitions under `torchtitan/models/`, and the component library under `torchtitan/components/`.
- **TPU lane:** `torchtitan/experiments/tpu`, entered through the TPU trainer
  ([`TPUTrainer`](../catalog/torchtitan/experiments/tpu/train.md#TPUTrainer "torchtitan/experiments/tpu/train.py:L36")), with its own
  per-model recipes (`torchtitan/experiments/tpu/recipes/`), Pallas kernels
  (`torchtitan/experiments/tpu/kernels/`), and TPU variants of shared components, e.g.
  [`TpuFloat8LinearConverter`](../catalog/torchtitan/experiments/tpu/float8_converter.md#TpuFloat8LinearConverter),
  [`TPUGrainDataLoader`](../catalog/torchtitan/experiments/tpu/datasets.md#TPUGrainDataLoader), and
  TPU-only `@override` modules under `torchtitan/experiments/tpu/overrides/`.
- The README points to three entry docs inside the TPU lane: the TPU README (environment, wheel
  build, single-host and GKE multi-host runs), the recipes directory (per-model, per-topology
  configs with launch blocks), and the TorchTPU optimization guide. Those are covered by the TPU
  guide/recipe doc-concepts, not here.

## Why it matters / when it applies
- **Where to look for a perf knob.** Anything specific to TPU performance (mesh/topology, remat,
  layer looping, Pallas kernels, MoE dispatch on TPU) lives under `experiments/tpu`. The shared
  core only carries hardware-neutral mechanisms (config tree, transforms, overrides, sharding
  configs) that the TPU lane plugs into.
- **Where a change goes.** TPU changes are made in this repository under `experiments/tpu`;
  anything touching shared TorchTitan code goes upstream to pytorch/torchtitan, because this
  fork is kept in sync with it. The practical consequence for optimization work: the TPU lane
  adapts to upstream through extension points (overrides, converters, transforms, its own
  trainer subclass) rather than by patching shared code. Several TPU modules record exactly this
  adaptation, e.g. the TPU overrides note that upstream made `override()` keyword-only.
- Upstream README/docs "apply unchanged" for non-TPU usage. Note that the upstream `docs/`
  directory is not vendored in this checkout (links such as `docs/converging.md` from model
  READMEs do not resolve locally).

## Connections
- Code concepts: [trainer-and-train-loop](../concepts/trainer-and-train-loop.md),
  [tpu-trainer-and-job-config](../concepts/tpu-trainer-and-job-config.md),
  [tpu-pallas-kernels](../concepts/tpu-pallas-kernels.md),
  [config-overrides](../concepts/config-overrides.md),
  [job-config](../concepts/job-config.md).
- Module catalogs: [torchtitan/trainer](../catalog/torchtitan/trainer.md),
  [torchtitan/experiments/tpu/train](../catalog/torchtitan/experiments/tpu/train.md).
- Related doc-concepts: [tpu-recipe-matrix](tpu-recipe-matrix.md), [experiments-contribution-contract](experiments-contribution-contract.md), [full-configuration-recipes](full-configuration-recipes.md),
  [configurable-overrides](configurable-overrides.md),
  [model-support-overview](model-support-overview.md).

## Source
Extracted from `README.md` (kept in place).
