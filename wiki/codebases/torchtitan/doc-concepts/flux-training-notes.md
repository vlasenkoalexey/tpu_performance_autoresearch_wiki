---
title: FLUX text-to-image training (per-block compile, FSDP/HSDP/CP, MXFP8)
type: doc-concept
provenance: doc
source: torchtitan/models/flux/README.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T06:34:20Z}
---
# FLUX text-to-image training (per-block compile, FSDP/HSDP/CP, MXFP8)

## Definition
TorchTitan's FLUX package showcases pre-training of the text-to-image part of FLUX. The model is a
stack of repeated `DoubleStreamBlock` and `SingleStreamBlock` transformer blocks driven by a
dedicated `FluxTrainer`, with a pretrained autoencoder and text encoders loaded from HF assets. Its
performance story is per-block `torch.compile`, FSDP/HSDP/CP, activation checkpointing, and
optional MXFP8 on Blackwell.

## In torchtitan (grounded)
- Model and trainer: [`FluxModel`](../catalog/torchtitan/models/flux/model/model.md#FluxModel "torchtitan/models/flux/model/model.py:L30"),
  [`DoubleStreamBlock`](../catalog/torchtitan/models/flux/model/layers.md#DoubleStreamBlock),
  [`SingleStreamBlock`](../catalog/torchtitan/models/flux/model/layers.md#SingleStreamBlock),
  [`FluxTrainer`](../catalog/torchtitan/models/flux/trainer.md#FluxTrainer "torchtitan/models/flux/trainer.py:L38").
- Parallelization: [`parallelize_flux`](../catalog/torchtitan/models/flux/parallelize.md#parallelize_flux "torchtitan/models/flux/parallelize.py:L52")
  with [`apply_ac`](../catalog/torchtitan/models/flux/parallelize.md#apply_ac),
  [`apply_compile`](../catalog/torchtitan/models/flux/parallelize.md#apply_compile) (each double/single
  block compiled with `fullgraph=True` on `compile.backend`),
  [`apply_fsdp`](../catalog/torchtitan/models/flux/parallelize.md#apply_fsdp) (final layer kept
  unsharded after forward to avoid an immediate re-gather), and
  [`parallelize_encoders`](../catalog/torchtitan/models/flux/parallelize.md#parallelize_encoders "torchtitan/models/flux/parallelize.py:L257");
  CP placements are declared in [`set_flux_sharding_config`](../catalog/torchtitan/models/flux/sharding.md#set_flux_sharding_config "torchtitan/models/flux/sharding.py:L61")
  (Q sequence-sharded, KV all-gathered over CP).
- Recipes: [`flux_debugmodel`](../catalog/torchtitan/models/flux/config_registry.md#flux_debugmodel "torchtitan/models/flux/config_registry.py:L55"),
  [`flux_schnell`](../catalog/torchtitan/models/flux/config_registry.md#flux_schnell "torchtitan/models/flux/config_registry.py:L186"),
  [`flux_dev`](../catalog/torchtitan/models/flux/config_registry.md#flux_dev "torchtitan/models/flux/config_registry.py:L128"),
  [`flux_schnell_mxfp8`](../catalog/torchtitan/models/flux/config_registry.md#flux_schnell_mxfp8 "torchtitan/models/flux/config_registry.py:L244"),
  [`flux_dev_mxfp8`](../catalog/torchtitan/models/flux/config_registry.md#flux_dev_mxfp8 "torchtitan/models/flux/config_registry.py:L272")
  (`MXFP8LinearConverter` over `double_blocks`, `single_blocks`, `img_in`, `txt_in`, `time_in`,
  `vector_in`, `final_layer`).
- **TPU lane:** [`TPU parallelize_flux`](../catalog/torchtitan/experiments/tpu/flux/infra/parallelize.md#parallelize_flux)
  currently delegates to the upstream implementation; the TPU registry adds
  [`flux_testmodel`](../catalog/torchtitan/experiments/tpu/flux/config_registry.md#flux_testmodel).

## Why it matters / when it applies
- **Compile granularity:** only the repeated blocks are compiled, each with `fullgraph=True`, so a
  graph break inside a block is an error rather than a silent slowdown. `compile.components`
  controls whether the model, the loss, or both are compiled (both by default).
- **Parallelism:** FSDP, HSDP, CP supported; TP and PP are TODO. Checkpoints are saved with weights
  re-sharded first: at the end of evaluation each FSDP module is resharded so saved weights match
  the training sharding.
- **MXFP8:** SM100+ only (B200/B100), torchao nightly; dimensions must be 32-aligned (Flux defaults
  are). No Flux linear opts into MXFP8 input storage (see [mxfp8-training](mxfp8-training.md)).
- **Doc vs code.** The README's custom-config example sets
  `config.model_converters = ModelConvertersContainer.Config(converters=[MXFP8Converter.Config(...)])`;
  neither `ModelConvertersContainer` nor `MXFP8Converter` exists at this commit. The shipped recipes
  instead rebuild the spec with `model_registry("flux-schnell", converters=[MXFP8LinearConverter.Config(...)])`.
  The README also uses legacy `--compile.*` CLI flags, which are frozen (see
  [full-configuration-recipes](full-configuration-recipes.md)).

## Connections
- Code concepts: [flux-diffusion-model](../concepts/flux-diffusion-model.md),
  [quantization](../concepts/quantization.md),
  [parallel-dims-and-parallelization](../concepts/parallel-dims-and-parallelization.md),
  [checkpointing](../concepts/checkpointing.md).
- Module catalogs: [torchtitan/models/flux/parallelize](../catalog/torchtitan/models/flux/parallelize.md),
  [torchtitan/models/flux/model/layers](../catalog/torchtitan/models/flux/model/layers.md),
  [torchtitan/models/flux/config_registry](../catalog/torchtitan/models/flux/config_registry.md),
  [torchtitan/experiments/tpu/flux/infra/parallelize](../catalog/torchtitan/experiments/tpu/flux/infra/parallelize.md).
- Related doc-concepts: [mxfp8-training](mxfp8-training.md),
  [model-support-overview](model-support-overview.md),
  [tpu-per-block-torch-compile](tpu-per-block-torch-compile.md).

## Source
Extracted from `torchtitan/models/flux/README.md` (kept in place).
