---
title: TPU vs CPU numerical parity checking
type: doc-concept
provenance: doc
source: docs/markdown/numerical_parity.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T02:38:46Z}
---
# TPU vs CPU numerical parity checking

## Definition
Outputs of a model ported to TPU differ slightly from a CPU reference by design: TPUs are bf16-native,
emulate `float32` matmuls with multiple bf16 passes, use a systolic array whose accumulation order and
rounding differ from sequential CPU loops, and XLA fuses ops (e.g. multiply-add) so intermediate
rounding points move. The doc's parity workflow isolates that hardware drift from real bugs:
identical weights, identical dtype, then `torch.testing.assert_close` on the TPU result moved to CPU.

## In torch_tpu (grounded)
The doc is user-level and names no torch_tpu internals; the code-side levers that change the drift
are documented elsewhere and are the ones to check when a parity test fails:
- the matmul precision mode - [`PyPushPrecision`](../catalog/csrc/ops/precision_context.cc.md#PyPushPrecision "csrc/ops/precision_context.cc:L45")
  via `torch.tpu.precision`, or the global set by `torch.set_float32_matmul_precision`
  ([matmul-precision-modes](matmul-precision-modes.md));
- excess precision inside fused graphs - [`SetAllowExcessPrecision`](../catalog/csrc/common/excess_precision.cc.md#SetAllowExcessPrecision "csrc/common/excess_precision.cc:L54")
  ([excess-precision](excess-precision.md));
- explicit wide accumulators - `out_dtype=` matmul overloads such as
  [`AtenBmmDtype`](../catalog/csrc/ops/bmm/bmm_aten_kernels.cc.md#AtenBmmDtype)
  ([mxu-bf16-arithmetic](mxu-bf16-arithmetic.md)).

## Why it matters / when it applies
**Workflow** (verification only, not part of training):
1. Build the model on CPU; build an identical model on `tpu`.
2. Copy weights: `model_tpu.load_state_dict(model_cpu.state_dict())` - mandatory.
3. Cast both to the **same** dtype (e.g. `torch.bfloat16`); bf16-vs-fp32 always mismatches.
4. Compare `torch.testing.assert_close(out_tpu.cpu(), out_cpu)`; repeat for
   `model.weight.grad` after `loss.backward()`.

**Reading a failure report.** `Mismatched elements` as a percentage plus the greatest absolute /
relative difference and its index. The doc's heuristic: a high mismatch percentage (> ~70%)
usually indicates systematic precision loss from compiler fusion rather than a logic bug, while the
max abs/rel numbers are what you size `atol` / `rtol` from. Baseline tolerances are PyTorch's
defaults; bf16 drift on TPU may exceed them.

**Perf lens.** This is the semantics gate for any optimization experiment: a speedup that moves
outputs beyond the bf16 drift band (or changes which elements mismatch systematically) needs a
precision explanation before it can count. Raising matmul precision to make parity pass costs MXU
passes - prefer `out_dtype` accumulators or tolerances sized from the bf16 reference.

> [!warning] Two torch_tpu docs disagree on accumulator width
> `numerical_parity.md` says MXU accumulators "may operate in BFloat16" depending on TPU generation,
> while `precision_management.md` states the MXU accumulates bf16 products in `float32`. The code
> does not settle this (accumulation happens inside XLA/libtpu); treat the precision doc's f32
> accumulation as the documented behaviour for current generations.

## Connections
- Code concepts: [dtype-and-precision](../concepts/dtype-and-precision.md),
  [deferred-execution-and-materialization](../concepts/deferred-execution-and-materialization.md),
  [host-device-copy](../concepts/host-device-copy.md)
- Module catalogs: [csrc/ops/precision_context.cc](../catalog/csrc/ops/precision_context.cc.md),
  [csrc/common/excess_precision.cc](../catalog/csrc/common/excess_precision.cc.md)
- Related doc-concepts: [matmul-precision-modes](matmul-precision-modes.md),
  [mxu-bf16-arithmetic](mxu-bf16-arithmetic.md), [excess-precision](excess-precision.md)

## Source
Extracted from `docs/markdown/numerical_parity.md` (kept in place).
