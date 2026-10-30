---
title: MXU bf16 arithmetic and output accumulator dtype (out_dtype)
type: doc-concept
provenance: doc
source: docs/markdown/precision_management.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T02:38:46Z}
---
# MXU bf16 arithmetic and output accumulator dtype (out_dtype)

## Definition
The TPU Matrix Multiply Unit (MXU) takes `bfloat16` inputs (8 bits of significand; v7x also takes
`fp8`) and accumulates in `float32`. Input and output formats therefore differ, which the doc calls
the root of two confusing behaviours: *excess precision* (results carry more bits than the input
dtype implies) and *less-than-expected precision* (a `float32` matmul is only bf16-accurate in one
pass). Vector units are different: they operate on the full 23-bit `float32` mantissa (not always
strictly IEEE 754, e.g. subnormals). The `out_dtype=` argument on matmul ops lets the caller keep the
wide accumulator instead of rounding back to the input dtype.

## In torch_tpu (grounded)
- **`out_dtype` overloads.** `torch.bmm(a, b, out_dtype=torch.float32)` dispatches to
  [`AtenBmmDtype`](../catalog/csrc/ops/bmm/bmm_aten_kernels.cc.md#AtenBmmDtype) (owning module
  `csrc/ops/bmm/bmm_aten_kernels.cc`), which builds the StableHLO dot with a `float32` result type
  directly from the bf16 operands - the accumulator value is returned instead of being rounded.
  `torch.mm(..., out_dtype=...)` goes to
  [`AtenMmDtype`](../catalog/csrc/ops/mm/mm_aten_kernels.cc.md#AtenMmDtype); note the mm path
  converts both operands to the target dtype before the dot, so it is an `f32 x f32` dot whose
  MXU cost then depends on the active [precision mode](matmul-precision-modes.md). `addmm` /
  `baddbmm` have equivalent `...Dtype` kernels
  ([`AtenAddmmDtype`](../catalog/csrc/ops/addmm/addmm_aten_kernels.cc.md#AtenAddmmDtype),
  [`AtenBaddbmmDtype`](../catalog/csrc/ops/baddbmm/baddbmm_aten_kernels.cc.md#AtenBaddbmmDtype)).
- **Precision per dot.** All of these read the current precision through
  [`GetAndAddPrecisionTo`](../catalog/csrc/ops/precision_context.cc.md#GetAndAddPrecisionTo "csrc/ops/precision_context.cc:L76"),
  so the precision mode, the output dtype and the operand dtypes are all part of the kernel's cache
  key.
- **Multi-pass f32.** The 3-pass / 6-pass emulation is not implemented in torch_tpu itself - it is
  how XLA lowers a StableHLO dot with `HIGH` / `HIGHEST` precision config to bf16 MXU passes.

## Why it matters / when it applies
- **bf16 split.** A `float32` significand (24 bits) is three bf16 significands; `(a+b+c)(d+e+f)`
  expands to 9 bf16 products, of which Med x Low, Low x Med and Low x Low always underflow in
  `float32` - hence 6 passes for full `float32` (`HIGHEST`), 3 for `HIGH`, 1 for `DEFAULT`.
- **Why accumulate in f32.** bf16 machine epsilon is `2**-7` (~0.8%); accumulating a long
  contracting dimension in bf16 would compound that per add. The f32 accumulator plays the role
  of IEEE guard/round/sticky bits.
- **When f32 matmul precision matters.** Rarely for modern models (bf16 weights; inference almost
  never hits f32 matmuls). It matters for older f32-trained models and parity checks; there the
  extra passes are often hidden because such models are HBM-bound (idle MXU cycles).
- **Bitwise validation recipe.** The doc's test builds bf16 identity matrices scaled by
  `1 + 2**-6` and `1 + 2**-7`; their product has bit 13 set only if the f32 accumulator value is
  kept. Eager execution and `allow_excess_precision = False` drop bit 13;
  `allow_excess_precision = True` under `torch.compile` may keep it. See
  [excess-precision](excess-precision.md).
- Perf lens: `out_dtype=torch.float32` on bmm is the cheap way to get f32 accumulation (one MXU
  pass, no operand upcast); upcasting operands to f32 and running at `DEFAULT` is *not* more
  accurate than bf16 inputs, and at `HIGHEST` costs up to 6x MXU work.

## Connections
- Code concepts: [dtype-and-precision](../concepts/dtype-and-precision.md),
  [stablehlo-op-builder](../concepts/stablehlo-op-builder.md),
  [aten-kernel-authoring](../concepts/aten-kernel-authoring.md),
  [mosaic-matmul](../concepts/mosaic-matmul.md)
- Module catalogs: [csrc/ops/bmm/bmm_aten_kernels.cc](../catalog/csrc/ops/bmm/bmm_aten_kernels.cc.md),
  [csrc/ops/mm/mm_aten_kernels.cc](../catalog/csrc/ops/mm/mm_aten_kernels.cc.md),
  [csrc/ops/precision_context.cc](../catalog/csrc/ops/precision_context.cc.md)
- Related doc-concepts: [matmul-precision-modes](matmul-precision-modes.md),
  [excess-precision](excess-precision.md), [tpu-cpu-numerical-parity](tpu-cpu-numerical-parity.md)

## Source
Extracted from `docs/markdown/precision_management.md` (kept in place).
