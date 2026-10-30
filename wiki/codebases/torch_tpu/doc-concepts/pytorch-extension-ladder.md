---
title: The extension ladder (composition -> autograd.Function -> custom op -> Pallas kernel)
type: doc-concept
provenance: doc
source: docs/markdown/extending_modules_and_functions_via_composition.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T02:38:46Z}
---
# The extension ladder (composition -> autograd.Function -> custom op -> Pallas kernel)

## Definition
Read together, the four "extending PyTorch" docs describe an ordered ladder for adding functionality to a TorchTPU model, each rung trading convenience for control. One running example (1-bit quantize + bit-pack, inspired by DeepSeek-V3 activation quantization) threads through them, so the motivation for climbing each rung is explicit.

| Rung | Mechanism | What you control | Cost / when to climb |
|---|---|---|---|
| 1. Composition | Existing torch functions inside a stateless function; `nn.Module` only for state | Nothing below ATen | Default. Climb when intermediates hit HBM ([extending-via-composition](extending-via-composition.md)) |
| 2. `torch.autograd.Function` | Custom `forward`/`backward` from existing ops | The gradient formula | For gradient rewrites only; not for wrapping opaque kernels in PT2 ([custom-autograd-function](custom-autograd-function.md)) |
| 3. Custom op via `jax_op` | JAX function registered as `torch.library.custom_op` with auto fake kernel | An opaque op boundary that compiles and traces | Needed for any kernel outside ATen ([pallas-jax-op-bridge](pallas-jax-op-bridge.md)) |
| 4. Pallas kernel inside the op | `pl.pallas_call` body over VMEM refs | Memory hierarchy (HBM/VMEM/registers), fusion | Only after profiling a baseline ([pallas-register-level-fusion](pallas-register-level-fusion.md)) |

## In torch_tpu (grounded)
Rungs 1-2 are upstream PyTorch and need no torch_tpu API. Rungs 3-4 go through [`jax_op`](../catalog/src/torch_tpu/_internal/pallas/pallas.md#jax_op) (public `torch.tpu.pallas.jax_op`, experimental): it wraps the JAX function in a [`JaxCallable`](../catalog/src/torch_tpu/_internal/pallas/pallas.md#JaxCallable "src/torch_tpu/_internal/pallas/pallas.py:L930"), registers a fake kernel ([`jax_op.dec.fake_fn`](../catalog/src/torch_tpu/_internal/pallas/pallas.md#jax_op.dec.fake_fn "src/torch_tpu/_internal/pallas/pallas.py:L1650")) so dynamo and AOTAutograd can trace it, and at run time inlines the exported StableHLO/Mosaic module into the deferred eager graph via [`CallCustomKernel`](../catalog/csrc/ops/custom_kernels.cc.md#CallCustomKernel). Gradients for rung 3-4 ops are attached with `CustomOpDef.register_autograd`, using a second `jax_op` for the backward kernel.

## Why it matters / when it applies
- **Stop at the lowest rung that meets the perf target.** Each step up adds code that must be kept numerically equal to a reference; the docs keep the composition version as the correctness oracle for the fused kernel.
- **The perf motivation for rung 4 is memory traffic**, not FLOPs: a fused kernel removes a materialized intermediate between two memory-bound passes.
- **All rungs remain `torch.compile`-compatible** on the TPU backend; rung 3 is the boundary where the user, not ATen, owns the shape function (static output shapes by default).
- The docs run rungs 1-2 with `backend="aot_eager"` on CPU as teaching examples; on TPU the backend is `"tpu"` ([torch-compile-backend](../concepts/torch-compile-backend.md)).

## Connections
- Code concepts: [pallas-custom-kernels](../concepts/pallas-custom-kernels.md), [python-ops](../concepts/python-ops.md), [aten-kernel-authoring](../concepts/aten-kernel-authoring.md), [torch-compile-backend](../concepts/torch-compile-backend.md), [eager-op-dispatch](../concepts/eager-op-dispatch.md), [kiln-kernel-dsl](../concepts/kiln-kernel-dsl.md)
- Module catalogs: [src/torch_tpu/_internal/pallas/pallas](../catalog/src/torch_tpu/_internal/pallas/pallas.md), [csrc/ops/custom_kernels.cc](../catalog/csrc/ops/custom_kernels.cc.md)
- Related doc-concepts: [extending-via-composition](extending-via-composition.md), [custom-autograd-function](custom-autograd-function.md), [pallas-jax-op-bridge](pallas-jax-op-bridge.md), [pallas-register-level-fusion](pallas-register-level-fusion.md)

## Source
Synthesized from `docs/markdown/extending_modules_and_functions_via_composition.md`, `docs/markdown/customizing_autograd_via_torch_autograd_function.md`, `docs/markdown/custom_pallas_kernel.md` (= `docs/markdown/3_practical_examples_4_adding_custom_kernels_using_pallas.md`) and `docs/markdown/custom_ops_via_pallas.md` (kept in place).
