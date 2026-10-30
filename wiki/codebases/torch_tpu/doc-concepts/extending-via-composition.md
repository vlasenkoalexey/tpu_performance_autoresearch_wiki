---
title: Extending PyTorch by composition (module/function split, QAT example)
type: doc-concept
provenance: doc
source: docs/markdown/extending_modules_and_functions_via_composition.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T02:38:46Z}
---
# Extending PyTorch by composition (module/function split, QAT example)

## Definition
The doc's first rung of extending PyTorch is composition: build new behavior by combining existing PyTorch functions, and wrap it in a `torch.nn.Module` only when state (trainable parameters) must be held. It names the standard separation of concerns - modules (`nn.Linear`) own parameters, hooks and save/load, while the computation is delegated to a stateless function (`F.linear`) that takes the weights as explicit arguments. The worked example is a toy quantization-aware-training layer, `QATLinear`, whose `forward` delegates to a stateless `qat_linear(weight, data)`.

## In torch_tpu (grounded)
- Everything in the doc is upstream PyTorch; it runs on CPU with `torch.compile(backend="aot_eager")` and touches no torch_tpu symbol. On TPU the same composed functions dispatch op-by-op through the `PrivateUse1` kernels and are recorded into deferred graphs ([eager-op-dispatch](../concepts/eager-op-dispatch.md), [deferred-execution-and-materialization](../concepts/deferred-execution-and-materialization.md)), or are traced whole under `torch.compile(backend="tpu")` ([`TpuBackend.__call__`](../catalog/src/torch_tpu/_internal/compile/_backend.md#TpuBackend.__call__ "src/torch_tpu/_internal/compile/_backend.py:L654")).
- **QAT via the straight-through trick.** `qat_linear` computes `weight_qat = dequantize(*quantize(weight))` (1-bit signs times a mean-magnitude block scale) and feeds `F.linear` with `(weight_qat - weight).detach() + weight`: the forward sees quantized weights while the backward sees the identity on the master weights. Master weights stay high precision ([dtype-and-precision](../concepts/dtype-and-precision.md)).
- **Bit packing by composition.** `pack32` maps signs to bits and sums `bits * 2**arange(32)` into a `uint32` (a bitwise-or reduction written as a sum); `unpack32` shifts and masks. `pack`/`unpack` lift these over rows with `torch.vmap`.

## Why it matters / when it applies
- **Composition is the default and is fully traceable** - it compiles, differentiates and shards with no extra registration, so it is the first thing to try.
- **Its perf limit is materialized intermediates.** In this design quantize and pack are separate passes, so the binarized signs are written to HBM only to be read back for packing. The follow-up doc treats that as "a severe memory bottleneck" and replaces the pair with one fused Pallas kernel ([pallas-register-level-fusion](pallas-register-level-fusion.md)). Under `torch.compile` XLA may fuse some of this itself - inspect the HLO before reaching for a kernel.
- **Keep the computation in a stateless function.** That is what lets the same logic be decorated with `torch.compile`, swapped for a custom op later, or reused by another module without touching parameter management.
- The doc says plainly its quantization scheme is illustrative, not realistic.

## Connections
- Code concepts: [eager-op-dispatch](../concepts/eager-op-dispatch.md), [deferred-execution-and-materialization](../concepts/deferred-execution-and-materialization.md), [torch-compile-backend](../concepts/torch-compile-backend.md), [dtype-and-precision](../concepts/dtype-and-precision.md)
- Module catalogs: [src/torch_tpu/_internal/compile/_backend](../catalog/src/torch_tpu/_internal/compile/_backend.md)
- Related doc-concepts: [pytorch-extension-ladder](pytorch-extension-ladder.md), [custom-autograd-function](custom-autograd-function.md), [pallas-register-level-fusion](pallas-register-level-fusion.md), [pallas-jax-op-bridge](pallas-jax-op-bridge.md)

## Source
Extracted from `docs/markdown/extending_modules_and_functions_via_composition.md` (kept in place).
