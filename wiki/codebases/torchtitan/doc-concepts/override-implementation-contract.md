---
title: Override implementation contract (sharding, checkpoint layout, custom ops under torch.compile)
type: doc-concept
provenance: doc
source: torchtitan/overrides/README.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T06:34:20Z}
---
# Override implementation contract (sharding, checkpoint layout, custom ops under torch.compile)

## Definition
A replacement module installed by an `@override` must still satisfy three contracts the rest of
the stack relies on: it must declare its own parallelism through the `Module` protocol's
`ShardingConfig`, it must keep checkpoints interoperable (or knowingly change FQNs), and any custom
kernel it wraps must be traceable by `torch.compile`. The mechanism deliberately adds no machinery
for any of these - they are the override author's responsibility.

## In torchtitan (grounded)
- **Parallelism via the Module protocol.** A replacement implements
  [`init_states`](../catalog/torchtitan/protocols/module.md#Module.init_states "torchtitan/protocols/module.py:L109") and declares a
  [`ShardingConfig`](../catalog/torchtitan/protocols/sharding.md#ShardingConfig "torchtitan/protocols/sharding.py:L60") for the states and
  activations it wants sharded; [`Module.parallelize`](../catalog/torchtitan/protocols/module.md#Module.parallelize "torchtitan/protocols/module.py:L279")
  reads it exactly as for core modules, so the override composes with TP/FSDP without
  model-specific code.
- **Fusion under TP - worked example.** [`FusedSwiGLU`](../catalog/torchtitan/overrides/fused_swiglu.md#FusedSwiGLU "torchtitan/overrides/fused_swiglu.py:L450")
  stores one `(2*hidden, dim)` [`w13`](../catalog/torchtitan/overrides/fused_swiglu.md#FusedSwiGLU.w13 "torchtitan/overrides/fused_swiglu.py:L468")
  Linear with gate/up rows **interleaved**, so sharding row axis 0 gives each TP rank matching
  slices of both projections (Megatron column-parallel layout); one GEMM replaces two. The
  distributed-GEMM variant [`DistGEMMFusedSwiGLU`](../catalog/torchtitan/overrides/fused_swiglu.md#DistGEMMFusedSwiGLU "torchtitan/overrides/fused_swiglu.py:L507")
  has its own exact override ([`dist_gemm_fused_swiglu`](../catalog/torchtitan/overrides/fused_swiglu.md#dist_gemm_fused_swiglu "torchtitan/overrides/fused_swiglu.py:L594"))
  so its communication overlap cannot be replaced accidentally by the regular fused version.
- **Checkpoint layout bridging.** `FusedSwiGLU` registers
  [`_split_w13_on_save`](../catalog/torchtitan/overrides/fused_swiglu.md#FusedSwiGLU._split_w13_on_save)
  (a `register_state_dict_post_hook`) and
  [`_merge_w13_on_load`](../catalog/torchtitan/overrides/fused_swiglu.md#FusedSwiGLU._merge_w13_on_load)
  (a `register_load_state_dict_pre_hook`), so it checkpoints stock `w1.weight` / `w3.weight` while
  training with `w13`. For mappings too complex for module hooks, a model-level
  [`BaseStateDictAdapter`](../catalog/torchtitan/protocols/state_dict_adapter.md#BaseStateDictAdapter)
  (e.g. [`Llama3StateDictAdapter`](../catalog/torchtitan/models/llama3/state_dict_adapter.md#Llama3StateDictAdapter "torchtitan/models/llama3/state_dict_adapter.py:L18"))
  remains available.
- **Custom kernels as custom ops.** [`HelionCosSinRoPE`](../catalog/torchtitan/overrides/helion_rope.md#HelionCosSinRoPE "torchtitan/overrides/helion_rope.py:L972")
  wraps fused Helion forward/backward kernels as `torch.library.custom_op`s
  ([`_helion_cossin_rope_fwd`](../catalog/torchtitan/overrides/helion_rope.md#_helion_cossin_rope_fwd "torchtitan/overrides/helion_rope.py:L520"),
  [`_helion_cossin_rope_bwd`](../catalog/torchtitan/overrides/helion_rope.md#_helion_cossin_rope_bwd "torchtitan/overrides/helion_rope.py:L550"))
  with `register_fake` and `register_autograd`, and falls back to the PyTorch RoPE when Helion or
  CUDA is unavailable. [`TritonOffsetRMSNorm`](../catalog/torchtitan/overrides/offset_rmsnorm.md#TritonOffsetRMSNorm)
  follows the same pattern ([`_triton_offset_rms_norm_op`](../catalog/torchtitan/overrides/offset_rmsnorm.md#_triton_offset_rms_norm_op "torchtitan/overrides/offset_rmsnorm.py:L175")).

## Why it matters / when it applies
- **torch.compile is on by default for the model** (`compile.components` includes `"model"`), so a
  raw kernel call graph-breaks or fails to trace. The recipe the doc prescribes:
  `torch.library.custom_op` (or `triton_op` for Triton) for a stable schema and mutation contract,
  `register_fake` for shape/dtype propagation, `register_autograd` for training, and
  `torch.library.opcheck` as the unit test. On TPU the same rule holds for Pallas kernels: they must
  be opaque, schema-carrying ops so the compiled graph stays whole (see
  [tpu-pallas-kernels](../concepts/tpu-pallas-kernels.md)).
- **Fusion changes shard math.** Any fused weight must have a row order that admits a correct shard
  on the TP axis; interleaving is the standard fix. Getting this wrong is a silent numerics bug, not
  a crash.
- **Changing parameter layout changes checkpoint FQNs** by default; bridge with the two hooks to
  stay a drop-in for stock checkpoints and HF adapters (the same mechanism the activation
  checkpoint wrapper uses to strip `_checkpoint_wrapped_module`).
- **Context parallelism is applied on the Attention module.** An override of an attention block or
  inner attention must remain compatible with that application point (see
  [model-config-transforms](model-config-transforms.md)).
- **Version pinning for external packages.** The contract is the public `Configurable.Config`
  fields of the targets, which change across releases; external override packages should pin a
  validated torchtitan range and the matching PyTorch nightly.
- **Search-friendliness.** The doc frames uniformly swappable implementations as a building block
  for automated hill-climbing over kernels and model impls - directly relevant to an
  autoresearch loop that A/Bs a kernel per layer via `fqns`.

## Connections
- Code concepts: [config-overrides](../concepts/config-overrides.md),
  [model-spec-protocols](../concepts/model-spec-protocols.md),
  [model-building-blocks](../concepts/model-building-blocks.md),
  [checkpointing](../concepts/checkpointing.md),
  [tpu-pallas-kernels](../concepts/tpu-pallas-kernels.md),
  [parallel-dims-and-parallelization](../concepts/parallel-dims-and-parallelization.md).
- Module catalogs: [torchtitan/overrides/fused_swiglu](../catalog/torchtitan/overrides/fused_swiglu.md),
  [torchtitan/overrides/helion_rope](../catalog/torchtitan/overrides/helion_rope.md),
  [torchtitan/overrides/offset_rmsnorm](../catalog/torchtitan/overrides/offset_rmsnorm.md),
  [torchtitan/protocols/module](../catalog/torchtitan/protocols/module.md),
  [torchtitan/protocols/sharding](../catalog/torchtitan/protocols/sharding.md).
- Related doc-concepts: [tpu-per-block-torch-compile](tpu-per-block-torch-compile.md), [configurable-overrides](configurable-overrides.md),
  [declarative-sharding-config](declarative-sharding-config.md).

## Source
Extracted from `torchtitan/overrides/README.md` (kept in place).
