---
title: One-bit quantize-and-pack and popcount quantized sum (JAX-backed custom op)
type: doc-concept
provenance: doc
source: docs/markdown/quantized_sum.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T02:38:46Z}
---
# One-bit quantize-and-pack and popcount quantized sum (JAX-backed custom op)

## Definition
Two companion notebooks build a toy one-bit quantization format on TorchTPU. `quant.md` is the
baseline: quantize a tensor to signs plus one scale (`scale = mean(|x|)`, `sign(x)` with zeros
mapped to +1), then pack each row of 32 signs into one `uint32`, all under
`torch.compile(backend="tpu")`. `quantized_sum.md` then computes the sum of a packed tensor
**without unpacking**: each set bit is `+scale`, each clear bit `-scale`, so
`sum = (2 * popcount - total_bits) * scale`. Popcount is not an ATen op, so it is supplied as a
custom op implemented in JAX (`jax.lax.population_count`, which lowers 1:1 to StableHLO `popcnt`)
and registered with `torch.tpu.pallas.jax_op` - a "custom op via JAX, without Pallas".

## In torch_tpu (grounded)
- **Packing in plain PyTorch.** `pack32` computes `sum((x == 1).to(uint32) * 2**arange(32), dtype=uint32)`;
  with distinct powers of two the sum is a bitwise-OR reduction. It reaches the reduction kernels
  (e.g. [`AtenSumIntListOut`](../catalog/csrc/ops/reductions/sum_aten_kernels.cc.md#AtenSumIntListOut "csrc/ops/reductions/sum_aten_kernels.cc:L36"))
  and is batched with `torch.vmap(pack32)`. The compiled variant drops the size / dtype / value
  asserts of the eager version "to avoid compilation errors on TPU" - data-dependent asserts need
  the value on the host.
- **JAX as a custom op.** [`jax_op`](../catalog/src/torch_tpu/_internal/pallas/pallas.md#jax_op)
  (owning module `src/torch_tpu/_internal/pallas/pallas.py`, experimental) takes a namespaced name
  (`"test_example::popcount"`) and a JAX function, wraps it with
  [`custom_jax_kernel`](../catalog/src/torch_tpu/_internal/pallas/pallas.md#custom_jax_kernel "src/torch_tpu/_internal/pallas/pallas.py:L1399"),
  and registers a `torch.library.custom_op` whose fake (meta) kernel
  [`fake_fn`](../catalog/src/torch_tpu/_internal/pallas/pallas.md#jax_op.dec.fake_fn "src/torch_tpu/_internal/pallas/pallas.py:L1650")
  is derived automatically from the exported JAX function (symbolic dims are rejected by that
  default fake). Callers cannot tell the op is JAX-backed; the op composes with `torch.compile`
  without a graph break.
- **Verifying the lowering.** With HLO dumps on, the JAX body appears as a nested computation with
  a `popcnt` instruction in `module_NNNN.tt_jit_custom_kernel.before_optimizations.txt` (see
  [hlo-and-llo-compilation-dumps](hlo-and-llo-compilation-dumps.md)).

## Why it matters / when it applies
- **Why JAX instead of C++.** `jax.lax` maps nearly 1:1 onto StableHLO, so any StableHLO op that
  ATen lacks (`popcnt`, `approx_max_k`, ...) can be emitted from Python without writing a C++ HLO
  kernel (the C++ route is "forthcoming" in the docs). JAX and TorchTPU compile to the same HLO.
- **Differentiability.** `population_count` has no gradient, so this op is inference-only. For a
  trainable JAX-backed op, the doc points to `test_jax_dot_grad_for_backwards()` in the Pallas tests,
  which uses `jax.jvp` / `jax.grad` to generate the backward.
- **Perf lens.** Operating on packed bits keeps the data 32x smaller in HBM and turns a reduction
  over 32 floats into one integer popcount per word - the general pattern for low-bit formats on
  TPU, where the win is bandwidth. Packing itself is a reduction over a broadcasted power-of-two
  vector; inspect the HLO / LLO to confirm XLA fuses it rather than materializing the
  `[rows, 32]` intermediate.

## Connections
- Code concepts: [pallas-custom-kernels](../concepts/pallas-custom-kernels.md),
  [reductions](../concepts/reductions.md),
  [torch-compile-backend](../concepts/torch-compile-backend.md),
  [python-ops](../concepts/python-ops.md)
- Module catalogs: [src/torch_tpu/_internal/pallas/pallas](../catalog/src/torch_tpu/_internal/pallas/pallas.md),
  [csrc/ops/reductions/sum_aten_kernels.cc](../catalog/csrc/ops/reductions/sum_aten_kernels.cc.md)
- Related doc-concepts: [pallas-jax-op-bridge](pallas-jax-op-bridge.md),
  [extending-via-composition](extending-via-composition.md) (origin of the one-bit `QATLinear`
  format), [pytorch-extension-ladder](pytorch-extension-ladder.md),
  [hlo-and-llo-compilation-dumps](hlo-and-llo-compilation-dumps.md)

## Source
Extracted from `docs/markdown/quantized_sum.md` and `docs/markdown/quant.md` (both kept in place).
