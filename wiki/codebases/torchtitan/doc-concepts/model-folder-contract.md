---
title: Model folder contract (model.py, sharding.py, parallelize.py, model_registry, config_registry)
type: doc-concept
provenance: doc
source: torchtitan/models/README.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T06:34:20Z}
---
# Model folder contract (model.py, sharding.py, parallelize.py, model_registry, config_registry)

## Definition
Every model in `torchtitan/models/<name>/` (Llama 3 is the reference) follows one file layout with
one responsibility per file: single-device model code with a nested `Config`; a declarative
`sharding.py`; a `parallelize.py` that applies training techniques in a fixed order; an optional
`pipeline.py`; a `model_registry(flavor)` returning a `ModelSpec`; per-run `config_registry.py`
functions; and an HF `state_dict_adapter.py`. New models usually land under `torchtitan/experiments`
first.

## In torchtitan (grounded)
- **model.py.** Subclass a base such as [`Decoder`](../catalog/torchtitan/models/common/decoder.md#Decoder "torchtitan/models/common/decoder.py:L67")
  with a nested `Config` (from [`Decoder.Config`](../catalog/torchtitan/models/common/decoder.md#Decoder.Config "torchtitan/models/common/decoder.py:L75"));
  [`get_nparams_and_flops`](../catalog/torchtitan/protocols/model.md#BaseModel.Config.get_nparams_and_flops "torchtitan/protocols/model.py:L127")
  feeds size/throughput (MFU) reporting; [`update_from_config`](../catalog/torchtitan/protocols/model.md#BaseModel.Config.update_from_config)
  syncs from training configs (seq_len, hardware settings, and the sharding setter). Initialization
  is declarative: `param_init` dicts on every sub-config, auto-recursing
  [`Module.init_states`](../catalog/torchtitan/protocols/module.md#Module.init_states "torchtitan/protocols/module.py:L109"), and
  [`Module._init_self_buffers`](../catalog/torchtitan/protocols/module.md#Module._init_self_buffers "torchtitan/protocols/module.py:L242")
  for device-aware buffers (RoPE, MoE).
- **sharding.py.** A `set_<model>_sharding_config(config, *, enable_sp, ...)` per model, e.g.
  [`set_llama3_sharding_config`](../catalog/torchtitan/models/llama3/sharding.md#set_llama3_sharding_config "torchtitan/models/llama3/sharding.py:L25"),
  [`set_qwen3_sharding_config`](../catalog/torchtitan/models/qwen3/sharding.md#set_qwen3_sharding_config "torchtitan/models/qwen3/sharding.py:L38"),
  [`set_deepseek_v3_sharding_config`](../catalog/torchtitan/models/deepseek_v3/sharding.md#set_deepseek_v3_sharding_config "torchtitan/models/deepseek_v3/sharding.py:L44"),
  reusing helpers from `decoder_sharding.py` (see [declarative-sharding-config](declarative-sharding-config.md)).
- **parallelize.py.** e.g. [`parallelize_llama`](../catalog/torchtitan/models/llama3/parallelize.md#parallelize_llama "torchtitan/models/llama3/parallelize.py:L23");
  order: [`Module.parallelize`](../catalog/torchtitan/protocols/module.md#Module.parallelize "torchtitan/protocols/module.py:L279") ->
  activation checkpointing -> `torch.compile` -> FSDP/HSDP
  ([`apply_fsdp_to_decoder`](../catalog/torchtitan/distributed/fsdp.md#apply_fsdp_to_decoder "torchtitan/distributed/fsdp.py:L189"), which
  takes `ep_degree` / `edp_mesh` for MoE expert FSDP). Language-model CP goes through
  [`Decoder.preprocess_inputs`](../catalog/torchtitan/models/common/decoder.md#Decoder.preprocess_inputs)
  -> [`prepare_context_parallel_input`](../catalog/torchtitan/distributed/context_parallel/api.md#prepare_context_parallel_input).
- **__init__.py.** Flavor dict plus `model_registry(...)` returning a
  [`ModelSpec`](../catalog/torchtitan/protocols/model_spec.md#ModelSpec "torchtitan/protocols/model_spec.py:L33") (name, flavor, model config,
  [`parallelize_fn`](../catalog/torchtitan/protocols/model_spec.md#ModelSpec.parallelize_fn "torchtitan/protocols/model_spec.py:L45"),
  [`pipelining_fn`](../catalog/torchtitan/protocols/model_spec.md#ModelSpec.pipelining_fn "torchtitan/protocols/model_spec.py:L46"), loss
  builder, [`state_dict_adapter`](../catalog/torchtitan/protocols/model_spec.md#ModelSpec.state_dict_adapter "torchtitan/protocols/model_spec.py:L48")),
  e.g. [`llama3 model_registry`](../catalog/torchtitan/models/llama3/__init__.md#model_registry "torchtitan/models/llama3/__init__.py:L387").
- **state_dict_adapter.py.** Subclass [`BaseStateDictAdapter`](../catalog/torchtitan/protocols/state_dict_adapter.md#BaseStateDictAdapter);
  used by offline conversion scripts, by [`CheckpointManager`](../catalog/torchtitan/components/checkpointer/dcp.md#CheckpointManager "torchtitan/components/checkpointer/dcp.py:L89")
  for HF-format save/load of sharded DTensors, and by `to_hf()`.

## Why it matters / when it applies
- **Fixed technique order is a perf contract.** Declarative TP/SP first, then AC, then compile, then
  FSDP - AC and compile wrap the already-TP'd blocks, and FSDP wraps last so its unit boundaries
  align with compiled/checkpointed blocks. The TPU lane keeps its own `parallelize_fn` per model
  (e.g. [`TPU parallelize_llama`](../catalog/torchtitan/experiments/tpu/llama3/infra/parallelize.md#parallelize_llama));
  TPU recipes that rebuild a `ModelSpec` through the upstream `model_registry` must restore the TPU
  `parallelize_fn` afterwards (see `_with_float8` in [float8-training](float8-training.md)).
- **`get_nparams_and_flops` drives MFU.** Wrong FLOP accounting in a new model misreports MFU in
  every experiment that uses it.
- **Readability over sharing.** Modules are not shared across models except the most common,
  complicated ones (`torchtitan/models/common/`), so a perf change to one model's block rarely
  leaks into others.
- **Testing guidance.** Numerics: load the same checkpoint into TorchTitan and HF and compare
  outputs (validates model and adapter together). Loss: compare against a verified baseline.
- **Doc vs code.** The README links `/docs/extension.md` and `/docs/converging.md`; there is no
  `docs/` directory in this checkout (upstream-only). Its `config_registry.py` guidance is the
  legacy recipe location (see [full-configuration-recipes](full-configuration-recipes.md)).
  `model_registry` also takes `converters=` for quantization/LoRA, which the README does not mention.

## Connections
- Code concepts: [model-spec-protocols](../concepts/model-spec-protocols.md),
  [model-building-blocks](../concepts/model-building-blocks.md),
  [parallel-dims-and-parallelization](../concepts/parallel-dims-and-parallelization.md),
  [llama3-model](../concepts/llama3-model.md),
  [checkpointing](../concepts/checkpointing.md),
  [tpu-trainer-and-job-config](../concepts/tpu-trainer-and-job-config.md).
- Module catalogs: [torchtitan/protocols/model](../catalog/torchtitan/protocols/model.md),
  [torchtitan/protocols/model_spec](../catalog/torchtitan/protocols/model_spec.md),
  [torchtitan/protocols/module](../catalog/torchtitan/protocols/module.md),
  [torchtitan/models/common/decoder](../catalog/torchtitan/models/common/decoder.md),
  [torchtitan/models/llama3/parallelize](../catalog/torchtitan/models/llama3/parallelize.md).
- Related doc-concepts: [declarative-sharding-config](declarative-sharding-config.md),
  [model-support-overview](model-support-overview.md),
  [full-configuration-recipes](full-configuration-recipes.md).

## Source
Extracted from `torchtitan/models/README.md` (kept in place).
