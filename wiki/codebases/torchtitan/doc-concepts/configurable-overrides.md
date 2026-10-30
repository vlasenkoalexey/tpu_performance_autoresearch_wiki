---
title: Configurable override mechanism (@override, override.imports, per-node claims)
type: doc-concept
provenance: doc
source: torchtitan/overrides/README.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T06:34:20Z}
---
# Configurable override mechanism (@override, override.imports, per-node claims)

## Definition
The override mechanism swaps any `Configurable` in a `Trainer.Config` tree - a model component,
optimizer, loss, dataloader - for an alternative implementation **without editing in-repo code**,
by importing a module that registers an override factory. It exists for hardware-specific kernels,
larger fused regions (e.g. a whole `MoE.Config` replaced by a fused dispatch-compute-combine), and
cheap team experimentation. It is explicitly *not* an operator-override API: ops are replaced via
PyTorch custom operators wrapped in a `Module`.

## In torchtitan (grounded)
- The whole mechanism is `torchtitan/config/override.py`:
  [`override`](../catalog/torchtitan/config/override.md#override "torchtitan/config/override.py:L175") (decorator registering a factory
  against a `target` config class, with optional `fqns` globs, `description`, `exact`),
  [`Override`](../catalog/torchtitan/config/override.md#Override),
  [`OverrideConfig`](../catalog/torchtitan/config/override.md#OverrideConfig "torchtitan/config/override.py:L61") with its
  [`imports`](../catalog/torchtitan/config/override.md#OverrideConfig.imports "torchtitan/config/override.py:L62") list,
  [`derive`](../catalog/torchtitan/config/override.md#derive "torchtitan/config/override.py:L249"),
  [`apply_overrides`](../catalog/torchtitan/config/override.md#apply_overrides "torchtitan/config/override.py:L448"), and
  [`clear_overrides`](../catalog/torchtitan/config/override.md#clear_overrides). CLI entries with
  JSON kwargs are parsed by [`parse_cli_imports`](../catalog/torchtitan/config/override.md#parse_cli_imports).
- The trainer holds the field [`Trainer.Config.override`](../catalog/torchtitan/trainer.md#Trainer.Config.override)
  and calls `apply_overrides` in [`Trainer.__init__`](../catalog/torchtitan/trainer.md#Trainer.__init__)
  after `model_config.update_from_config(...)` (which sets sharding config on the pre-override
  modules) and before any component is built.
- The model config is reachable because [`ModelSpec.traverse`](../catalog/torchtitan/protocols/model_spec.md#ModelSpec.traverse)
  exposes `ModelSpec.model` to [`Configurable.Config.traverse`](../catalog/torchtitan/config/configurable.md#Configurable.Config.traverse "torchtitan/config/configurable.py:L75");
  claims are gathered on the original tree by
  [`_collect_claims`](../catalog/torchtitan/config/override.md#_collect_claims "torchtitan/config/override.py:L386") before any mutation.
- In-repo examples (`torchtitan/overrides/`):
  [`fused_swiglu`](../catalog/torchtitan/overrides/fused_swiglu.md#fused_swiglu "torchtitan/overrides/fused_swiglu.py:L585") /
  [`dist_gemm_fused_swiglu`](../catalog/torchtitan/overrides/fused_swiglu.md#dist_gemm_fused_swiglu "torchtitan/overrides/fused_swiglu.py:L594"),
  [`helion_cos_sin_rope`](../catalog/torchtitan/overrides/helion_rope.md#helion_cos_sin_rope "torchtitan/overrides/helion_rope.py:L1041"),
  [`triton_offset_rmsnorm`](../catalog/torchtitan/overrides/offset_rmsnorm.md#triton_offset_rmsnorm "torchtitan/overrides/offset_rmsnorm.py:L343"), and
  [`fused_mla`](../catalog/torchtitan/overrides/fused_mla.md#fused_mla "torchtitan/overrides/fused_mla.py:L899") (DeepSeek-V3 MLA Q/KV assembly).
- **TPU lane overrides** (`torchtitan/experiments/tpu/overrides/`), appended to
  `config.override.imports` by the TPU recipes:
  [`tpu_real_arithmetic_complex_rope`](../catalog/torchtitan/experiments/tpu/overrides/real_rope.md#tpu_real_arithmetic_complex_rope)
  (ComplexRoPE with the complex multiply written as real arithmetic, bit-identical, no complex
  views of grad-requiring tensors),
  [`tpu_activation_dtype_cossin_rope`](../catalog/torchtitan/experiments/tpu/overrides/bf16_rope.md#tpu_activation_dtype_cossin_rope)
  (cos/sin RoPE in the activation dtype),
  [`fused_loss_lm_head`](../catalog/torchtitan/experiments/tpu/overrides/fused_loss.md#fused_loss_lm_head) /
  [`fused_loss_soft_capped_lm_head`](../catalog/torchtitan/experiments/tpu/overrides/fused_loss.md#fused_loss_soft_capped_lm_head)
  (defer the LM-head projection into a TPU fused cross-entropy; `fqns=["model_spec.model.lm_head"]`,
  `exact=True`), and
  [`tpu_discarded_token_counter`](../catalog/torchtitan/experiments/tpu/overrides/discarded_token_counter.md#tpu_discarded_token_counter)
  (MoE).

## Why it matters / when it applies
- **Explicit, scoped opt-in.** Nothing applies unless listed in `override.imports`, and each entry
  names exactly one factory as `module.function` - no hardware auto-detection, never the whole
  global table. An entry may carry kwargs (`(path, {...})` in Python, `path={"k": v}` JSON on the
  CLI) so two config trees can tune the same override differently.
- **Per-instance targeting, per-node conflicts.** `fqns` globs (`*` crosses `.`) select which
  matched nodes are claimed; FQNs are full paths from the `Trainer.Config` root
  (`model_spec.model.layers.0.feed_forward`, `optimizer`). Two overrides conflict only if they claim
  the same node or one claims an ancestor of the other's node - so different kernels on different
  layers, or A/B per layer, compose. Overlapping parent/child claims are an error rather than a
  silent choice. `exact=True` stops subclass configs from being claimed.
- **Order-independent application.** Claims are collected on the original tree and replacements are
  never re-traversed; every replacement is logged (`[Override] name: fqn Old.Config -> New.Config`),
  which is the first thing to check when verifying an override actually fired.
- **Converters run first.** In-repo converters (Float8, LoRA, MXFP8, NVFP4 via
  `ModelConfigConverter`) run inside `model_registry()`; overrides see the post-converter tree.
  `Linear.Config` and `GroupedExperts.Config` may already be rewritten by a converter, so target
  them by location with `fqns`. Converters are for core transforms that preserve guaranteed
  properties (e.g. batch invariance); overrides promise nothing about core properties.
- **Use `derive`, not hand-copying.** `derive(cfg, NewConfig, **deltas)` copies shared fields so a
  field added to the target later is not silently dropped to its default.
- **TPU composability example.** The TPU `bld_layout` pass swaps built module classes instead of
  claiming config nodes precisely so it composes with the RoPE overrides; a block-level override
  would be rejected as an ancestor claim.
- **Doc vs code.** The README's code map lists only `fused_swiglu.py` and `helion_rope.py`; the
  directory also ships `fused_mla.py`, `offset_rmsnorm.py`, and `moe_token_dispatcher.py`. The
  `override()` docstring describes `fqns` as bare module FQNs (`layers.0.feed_forward`), but the
  traversal used for matching starts at the `Trainer.Config` root, so the README's full-path form
  (`model_spec.model.layers.0.feed_forward`) is what actually matches - as the TPU fused-loss
  override's `model_spec.model.lm_head` selector shows.

## Connections
- Code concepts: [config-overrides](../concepts/config-overrides.md),
  [job-config](../concepts/job-config.md),
  [model-building-blocks](../concepts/model-building-blocks.md),
  [tpu-pallas-kernels](../concepts/tpu-pallas-kernels.md),
  [tpu-layer-loop-remat-and-layouts](../concepts/tpu-layer-loop-remat-and-layouts.md),
  [quantization](../concepts/quantization.md).
- Module catalogs: [torchtitan/config/override](../catalog/torchtitan/config/override.md),
  [torchtitan/overrides/fused_swiglu](../catalog/torchtitan/overrides/fused_swiglu.md),
  [torchtitan/overrides/helion_rope](../catalog/torchtitan/overrides/helion_rope.md),
  [torchtitan/overrides/fused_mla](../catalog/torchtitan/overrides/fused_mla.md),
  [torchtitan/experiments/tpu/overrides/fused_loss](../catalog/torchtitan/experiments/tpu/overrides/fused_loss.md),
  [torchtitan/experiments/tpu/overrides/real_rope](../catalog/torchtitan/experiments/tpu/overrides/real_rope.md).
- Related doc-concepts: [tpu-fused-linear-cross-entropy](tpu-fused-linear-cross-entropy.md), [tpu-moe-kernel-switches](tpu-moe-kernel-switches.md), [override-implementation-contract](override-implementation-contract.md),
  [model-config-transforms](model-config-transforms.md),
  [full-configuration-recipes](full-configuration-recipes.md),
  [float8-training](float8-training.md).

## Source
Extracted from `torchtitan/overrides/README.md` (kept in place).
