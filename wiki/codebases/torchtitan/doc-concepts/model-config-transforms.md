---
title: Model config transforms (apply_transforms, ContextParallelTransform)
type: doc-concept
provenance: doc
source: torchtitan/config/transform/README.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T06:34:20Z}
---
# Model config transforms (apply_transforms, ContextParallelTransform)

## Definition
A **model config transform** rewrites a complete, already-built model config tree. The model
registry builds the base model (architecture, attention algorithm, attention metadata format);
transforms then replace or wrap config nodes for distributed-execution and implementation choices -
context parallelism, TP GEMM backends, MoE communication backends, quantization, LoRA. Transforms
are one supported way to maintain recipes; they are optional.

## In torchtitan (grounded)
- Base class: [`ModelConfigTransform`](../catalog/torchtitan/config/transform/base.md#ModelConfigTransform)
  - a keyword-only dataclass whose
  [`transform`](../catalog/torchtitan/config/transform/base.md#ModelConfigTransform.transform)
  rewrites the model config in place and returns the root. Ordering and exclusion are declarative:
  [`run_after`](../catalog/torchtitan/config/transform/base.md#ModelConfigTransform.run_after) and
  [`conflicts_with`](../catalog/torchtitan/config/transform/base.md#ModelConfigTransform.conflicts_with).
- [`convert_config_type`](../catalog/torchtitan/config/transform/base.md#convert_config_type)
  replaces one config implementation with a subclass of it, preserving fields and wrappers set by
  earlier transforms.
- [`apply_transforms`](../catalog/torchtitan/config/transform/apply.md#apply_transforms "torchtitan/config/transform/apply.py:L76") deep-copies
  the `Trainer.Config`, rejects conflicts, orders and applies the transforms, then re-runs
  `__post_init__` validation; the input config is unchanged on failure.
  [`transform_model_config_`](../catalog/torchtitan/config/transform/apply.md#transform_model_config_)
  is the in-place, no-copy, no-validation variant for a bare `ModelSpec`.
- The only transform shipped in `torchtitan/config/transform/` at this commit is
  [`ContextParallelTransform`](../catalog/torchtitan/config/transform/context_parallel.md#ContextParallelTransform "torchtitan/config/transform/context_parallel.py:L22"):
  it traverses every [`BaseAttention.Config`](../catalog/torchtitan/models/common/attention.md#BaseAttention.Config)
  and converts its inner attention to
  [`inner_attention`](../catalog/torchtitan/config/transform/context_parallel.md#ContextParallelTransform.inner_attention "torchtitan/config/transform/context_parallel.py:L32"),
  which must inherit [`CPInnerAttention`](../catalog/torchtitan/models/common/cp_attention.md#CPInnerAttention "torchtitan/models/common/cp_attention.py:L39")
  (e.g. [`KVAllGatherCPFlexInnerAttention`](../catalog/torchtitan/models/common/cp_attention.md#KVAllGatherCPFlexInnerAttention "torchtitan/models/common/cp_attention.py:L55"),
  [`UlyssesCPFlexInnerAttention`](../catalog/torchtitan/models/common/cp_attention.md#UlyssesCPFlexInnerAttention "torchtitan/models/common/cp_attention.py:L113")).
- **TPU lane usage:** TPU Qwen3 CP recipes set `context_parallel_degree`, force
  `spmd_backend="spmd_types"`, pick a load balancer, and call `apply_transforms` with
  `ContextParallelTransform(inner_attention=tpu_cp_inner_attention(...))`, where
  [`tpu_cp_inner_attention`](../catalog/torchtitan/experiments/tpu/cp_attention.md#tpu_cp_inner_attention)
  maps the model's attention backend to a TPU CP class such as
  [`KVAllGatherCPInnerAttention`](../catalog/torchtitan/experiments/tpu/cp_attention.md#KVAllGatherCPInnerAttention "torchtitan/experiments/tpu/cp_attention.py:L433")
  or [`UlyssesCPInnerAttention`](../catalog/torchtitan/experiments/tpu/cp_attention.md#UlyssesCPInnerAttention "torchtitan/experiments/tpu/cp_attention.py:L322").
  The upstream recipe `muse_glimmer_30b_allgather_cp8` (not in the symbol index)
  is the GPU-side example.

## Why it matters / when it applies
- **Division of labor.** `model_registry` chooses the attention *algorithm* and *metadata format*
  (e.g. `FlexInnerAttention` consumes a `BlockMask`, `VarlenInnerAttention` consumes cumulative
  sequence offsets). A CP transform only specializes that choice for distributed execution - it may
  change input sharding and preprocessing but must preserve the algorithm and metadata format. So
  "which attention kernel" and "how it is context-parallelized" are independent axes in a recipe.
- **Ordering contract.** Set all training/parallelism options first, then call `apply_transforms`
  once, because validation runs on the final config (and again in the trainer after CLI
  overrides). A transform sees only the model config - pass any parallelism value it needs as a
  transform field.
- **CP prerequisite (from code).** [`validate_context_parallel`](../catalog/torchtitan/config/validation.md#validate_context_parallel "torchtitan/config/validation.py:L20")
  rejects `context_parallel_degree > 1` unless `parallelism.spmd_backend == "spmd_types"`, which is
  why the TPU and upstream CP recipes flip the backend before transforming.
- **Dependency direction.** `torchtitan/config/transform` may import other torchtitan packages,
  never the reverse; shared types such as `CPInnerAttention` stay with the attention code and only
  the installing transform lives here.
- **Doc vs code at this commit.** The README lists quantization and LoRA as transform territory and
  uses `QuantizationTransform` / `LMHeadCastTransform` in examples, but neither class exists:
  quantization and LoRA are still applied by `ModelConfigConverter` subclasses passed to
  `model_registry(..., converters=[...])` (see [float8-training](float8-training.md)), and the
  LM-head cast is [`LMHeadCastConverter`](../catalog/torchtitan/experiments/rl/models/cast_linear.md#LMHeadCastConverter)
  in the RL experiment. Treat those examples as the intended direction, not current API.

## Connections
- Code concepts: [job-config](../concepts/job-config.md),
  [tpu-context-parallel-attention](../concepts/tpu-context-parallel-attention.md),
  [parallel-dims-and-parallelization](../concepts/parallel-dims-and-parallelization.md),
  [model-building-blocks](../concepts/model-building-blocks.md),
  [quantization](../concepts/quantization.md).
- Module catalogs: [torchtitan/config/transform/base](../catalog/torchtitan/config/transform/base.md),
  [torchtitan/config/transform/apply](../catalog/torchtitan/config/transform/apply.md),
  [torchtitan/config/transform/context_parallel](../catalog/torchtitan/config/transform/context_parallel.md),
  [torchtitan/models/common/cp_attention](../catalog/torchtitan/models/common/cp_attention.md),
  [torchtitan/experiments/tpu/cp_attention](../catalog/torchtitan/experiments/tpu/cp_attention.md).
- Related doc-concepts: [full-configuration-recipes](full-configuration-recipes.md),
  [configurable-overrides](configurable-overrides.md).

## Source
Extracted from `torchtitan/config/transform/README.md` (kept in place).
