---
title: TorchTPU deferred-and-fused eager mode
type: doc-concept
provenance: doc
source: torchtitan/experiments/tpu/torch-tpu-optimization-guide.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T06:34:20Z}
---
# TorchTPU deferred-and-fused eager mode

## Definition
An execution mode between plain op-by-op dispatch and `torch.compile`: instead of dispatching each
op immediately, TorchTPU **defers** ops and lets XLA **fuse across op boundaries**, cutting per-op
dispatch overhead without a captured graph. It composes with `torch.compile`: compiled blocks still
run as compiled programs while the mode fuses the uncompiled glue around them (eager ops between
regions, anything Dynamo broke out of the graph).

## In torchtitan (grounded)
- The guide documents two enablement routes: export `TORCH_TPU_DEFER_AND_FUSE=1` before `torch_tpu`
  is first imported (read at libtpu init), or wrap a region in
  `torch_tpu._internal.execution_mode.set_eager_mode(EagerMode.DEFER_AND_FUSE)`.
- The TPU lane wires the second route into config: [`TPUConfig.eager_mode`](../catalog/torchtitan/experiments/tpu/tpu_job_config.md#TPUConfig.eager_mode)
  accepts `""` (off), `"DEFER_AND_FUSE"`, `"INTERNAL_DEFER_ALL"`, `"DEFER_NEVER"`,
  `"DEFER_NEVER_AND_LAUNCH_BLOCKING"`; [`_start_trainer`](../catalog/torchtitan/experiments/tpu/gmain.md#_start_trainer)
  wraps the whole trainer in `execution_mode.set_eager_mode(...)` when it is set on TPU.
  CLI: `--tpu_config.eager_mode=DEFER_AND_FUSE`.
- Shipped recipes enable it on top of per-block compile, e.g.
  [`llama3_8b`](../catalog/torchtitan/experiments/tpu/llama3/config_registry.md#llama3_8b),
  [`llama3_70b`](../catalog/torchtitan/experiments/tpu/llama3/config_registry.md#llama3_70b),
  [`llama3_405b`](../catalog/torchtitan/experiments/tpu/llama3/config_registry.md#llama3_405b), and
  Qwen3 / Qwen3.5 / Muse Glimmer recipes.

## Why it matters / when it applies
- **Use it** layered on `torch.compile` to shave dispatch from the eager remainder; or where code
  cannot be compiled cleanly (heavy graph breaks, data-dependent control flow); or for quick
  experiments wanting some fusion without wiring compilation.
- **Not a substitute** for compile at peak: compilation fuses into larger programs. On a model
  already covered by per-block compile it "typically adds little" - always measure.
- **Failure mode:** some patterns do not lower under fusion (e.g. certain unaligned
  dynamic-update-slice fusions fail inside libtpu). If a fusion crash appears, disable the mode for
  that model.
- `DEFER_NEVER_AND_LAUNCH_BLOCKING` is the obvious debugging setting for localizing device errors
  (inference from the enum name; the guide does not document the other modes).

**Doc vs code:** the guide lists only the env var and the context manager; it does not mention that
`tpu_config.eager_mode` is the config-native switch the recipes actually use. Note also that the
guide's "typically adds little" sits next to recipes (`llama3_8b` etc.) that enable it by default -
treat it as a per-model measured choice.

## Connections
- Code concepts: [tpu-trainer-and-job-config](../concepts/tpu-trainer-and-job-config.md),
  [trainer-and-train-loop](../concepts/trainer-and-train-loop.md)
- Module catalogs: [tpu_job_config](../catalog/torchtitan/experiments/tpu/tpu_job_config.md),
  [gmain](../catalog/torchtitan/experiments/tpu/gmain.md),
  [llama3/config_registry (tpu)](../catalog/torchtitan/experiments/tpu/llama3/config_registry.md)
- Related doc-concepts: [tpu-per-block-torch-compile](tpu-per-block-torch-compile.md),
  [tpu-dispatch-bound-mental-model](tpu-dispatch-bound-mental-model.md)

## Source
Extracted from `torchtitan/experiments/tpu/torch-tpu-optimization-guide.md` (section 4,
"Deferred-and-fused eager mode"; kept in place).
