---
title: Full configurations as code (recipes, --module/--config, frozen CLI)
type: doc-concept
provenance: doc
source: torchtitan/config/README.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T06:34:20Z}
---
# Full configurations as code (recipes, --module/--config, frozen CLI)

## Definition
A TorchTitan run is described by a **full configuration**: a Python function that returns a
complete `Trainer.Config` - the model, the parallelism degrees, and every optimization choice.
Building a run is "configuration programming" with TorchTitan components: you select the function
with `--module` (the defining module) and `--config` (the function name), and you change behavior
by writing a new function that derives from an existing one, not by adding CLI flags.

## In torchtitan (grounded)
- The root config is [`Trainer.Config`](../catalog/torchtitan/trainer.md#Trainer.Config "torchtitan/trainer.py:L76"); its
  sections include [`parallelism`](../catalog/torchtitan/trainer.md#Trainer.Config.parallelism "torchtitan/trainer.py:L114")
  ([`ParallelismConfig`](../catalog/torchtitan/config/configs.md#ParallelismConfig "torchtitan/config/configs.py:L123")),
  [`compile`](../catalog/torchtitan/trainer.md#Trainer.Config.compile)
  ([`CompileConfig`](../catalog/torchtitan/config/configs.md#CompileConfig "torchtitan/config/configs.py:L338")),
  [`dataloader`](../catalog/torchtitan/trainer.md#Trainer.Config.dataloader), and
  [`model_spec`](../catalog/torchtitan/trainer.md#Trainer.Config.model_spec "torchtitan/trainer.py:L83").
- Every component is a [`Configurable`](../catalog/torchtitan/config/configurable.md#Configurable "torchtitan/config/configurable.py:L18")
  with a nested [`Configurable.Config`](../catalog/torchtitan/config/configurable.md#Configurable.Config "torchtitan/config/configurable.py:L41")
  dataclass; [`build`](../catalog/torchtitan/config/configurable.md#Configurable.Config.build "torchtitan/config/configurable.py:L134")
  constructs the owner and
  [`traverse`](../catalog/torchtitan/config/configurable.md#Configurable.Config.traverse "torchtitan/config/configurable.py:L75") walks the
  tree (used by transforms and overrides).
- CLI parsing is [`ConfigManager`](../catalog/torchtitan/config/manager.md#ConfigManager "torchtitan/config/manager.py:L29")
  ([`parse_args`](../catalog/torchtitan/config/manager.md#ConfigManager.parse_args "torchtitan/config/manager.py:L44")); legacy
  `--section.option` flags still apply on top of the selected function.
- Recipes live in the top-level `torchtitan_recipes` package (next to, not inside, `torchtitan`).
  At this commit it holds `torchtitan_recipes/tests/` (integration-test configs, one module per
  suite, e.g. [`llama3_debugmodel_fsdp2_cp2`](../catalog/torchtitan_recipes/tests/features.md#llama3_debugmodel_fsdp2_cp2))
  and one model module, `torchtitan_recipes/muse_glimmer.py`
  (e.g. `muse_glimmer_30b_allgather_cp8` (not in the symbol index)).
- Cross-section validation lives in `torchtitan/config/validation.py`
  ([`validate_context_parallel`](../catalog/torchtitan/config/validation.md#validate_context_parallel "torchtitan/config/validation.py:L20")),
  called from [`Trainer.Config.__post_init__`](../catalog/torchtitan/trainer.md#Trainer.Config.__post_init__)
  after the per-section `__post_init__` checks.
- Job-level knobs that have no component home go in `torchtitan/config/configs.py`, e.g.
  [`TrainingConfig.num_tokens_per_microbatch_per_dp_rank`](../catalog/torchtitan/config/configs.md#TrainingConfig.num_tokens_per_microbatch_per_dp_rank "torchtitan/config/configs.py:L37").

## Why it matters / when it applies
- **Parallelism degrees are in the config, world size is not.** `NGPU` (or the TPU launcher's
  device count) must still equal the product of the degrees in the selected function. A new
  cluster shape usually means a new sharding layout and therefore a new configuration function -
  no code change.
- **The CLI is frozen.** The set of `--section.option` flags will not grow; existing flags keep
  working for backward compatibility only and are slated for removal (eventually only `--module`
  and `--config`, possibly no tyro at all). New feature knobs go in the config tree. A new field on
  a component config or in `configs.py` must be annotated `Annotated[..., tyro.conf.Suppress]` to
  stay off the CLI; anything under `model_spec` is already suppressed because `Trainer.Config.model_spec`
  carries that annotation, so model-architecture knobs are never CLI flags.
- **Recipes vs library.** `torchtitan` ships models and the classes implementing each
  optimization; `torchtitan_recipes` only picks combinations. Recipes change on a run/cluster
  schedule, so shipping one is a weaker promise than shipping a class. The repo deliberately ships
  a small set: test configs, hardware-named golden configs (reproducible from the name), and
  feature demos - not the exponential product of model x degrees x optimizations.
- **Migration in progress.** Per-model `config_registry.py` modules (selected with
  `--module <model> --config <fn>`) are the earlier location and still work; their size baselines
  (e.g. `llama3_8b`) are meant to move to `torchtitan_recipes` with no shim. At this commit the move
  has barely started (only `muse_glimmer.py` exists in `torchtitan_recipes`; the README's
  `torchtitan_recipes/llama3.py` example is illustrative). The TPU lane keeps its own per-model
  `config_registry.py` files under `torchtitan/experiments/tpu/<model>/`.
- **Editable-install gotcha.** An editable install made before `torchtitan_recipes` existed does
  not know the package; re-run `pip install -e .` if launching outside the repo root.
- Validation placement rule: single-section invariants in that section's `__post_init__`;
  cross-section invariants in `validation.py`. Set related fields before constructing/transforming
  so `__post_init__` sees the final values.

## Connections
- Code concepts: [job-config](../concepts/job-config.md),
  [trainer-and-train-loop](../concepts/trainer-and-train-loop.md),
  [config-overrides](../concepts/config-overrides.md),
  [tpu-trainer-and-job-config](../concepts/tpu-trainer-and-job-config.md).
- Module catalogs: [torchtitan/config/configs](../catalog/torchtitan/config/configs.md),
  [torchtitan/config/configurable](../catalog/torchtitan/config/configurable.md),
  [torchtitan/config/manager](../catalog/torchtitan/config/manager.md),
  [torchtitan/config/validation](../catalog/torchtitan/config/validation.md),
  [torchtitan/trainer](../catalog/torchtitan/trainer.md).
- Related doc-concepts: [model-config-transforms](model-config-transforms.md),
  [configurable-overrides](configurable-overrides.md),
  [model-folder-contract](model-folder-contract.md).

## Source
Extracted from `torchtitan/config/README.md` (kept in place).
