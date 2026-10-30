---
title: Matmul precision modes (DEFAULT / HIGH / HIGHEST)
type: doc-concept
provenance: doc
source: docs/markdown/precision_management.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T02:38:46Z}
---
# Matmul precision modes (DEFAULT / HIGH / HIGHEST)

## Definition
TorchTPU exposes the StableHLO `dot_general` precision config as `torch.tpu.Precision`, with three
modes that trade MXU passes for accuracy on `float32` matmuls: `DEFAULT` (1 pass, only the first 8
significand bits are multiplied), `HIGH` (3 passes, ~16 bits) and `HIGHEST` (6 passes, all 24 bits,
full `float32`). The mode is selected locally with the `torch.tpu.precision(mode)` context manager
or globally through `torch.set_float32_matmul_precision`.

## In torch_tpu (grounded)
- **Python surface.** [`precision`](../catalog/src/torch_tpu/_internal/precision/precision.md#precision)
  (owning module `src/torch_tpu/_internal/precision/precision.py`) validates the mode and pushes /
  pops it around the block. `Precision` itself is a pybind11 enum bound in
  `csrc/internal/precision/precision_impl.cc`. The context manager inserts an explicit
  `torch._dynamo.graph_break`, so inside `torch.compile` the surrounding frame falls back to eager
  (and errors under `fullgraph=True`) - in v0.2.0 the mode is not traceable.
- **Global knob.** At import, `torch_tpu._loader` monkey-patches
  `torch.set_float32_matmul_precision` (inside
  [`_init_device_impl`](../catalog/src/torch_tpu/_loader.md#_init_device_impl)): `"medium"` ->
  `DEFAULT`, `"high"` -> `HIGH`, `"highest"` -> `HIGHEST`, stored by
  [`PySetGlobalPrecision`](../catalog/csrc/ops/precision_context.cc.md#PySetGlobalPrecision "csrc/ops/precision_context.cc:L37")
  and read back by
  [`PyGetGlobalPrecision`](../catalog/csrc/ops/precision_context.cc.md#PyGetGlobalPrecision "csrc/ops/precision_context.cc:L41").
- **Local stack.** [`PyPushPrecision`](../catalog/csrc/ops/precision_context.cc.md#PyPushPrecision "csrc/ops/precision_context.cc:L45")
  / [`PyPopPrecision`](../catalog/csrc/ops/precision_context.cc.md#PyPopPrecision "csrc/ops/precision_context.cc:L49")
  push a per-thread `PrecisionContextState`; a pushed value overrides the global one.
- **Where kernels consume it.** Every matmul-class kernel (mm, bmm, addmm, baddbmm, dot, SDPA, flash
  attention, GRU, ...) calls
  [`GetAndAddPrecisionTo`](../catalog/csrc/ops/precision_context.cc.md#GetAndAddPrecisionTo "csrc/ops/precision_context.cc:L76"),
  which both returns the effective precision for the StableHLO builder **and writes it into the
  op's [`OpParamCacheKeys`](../catalog/csrc/common/cache_key.h.md#OpParamCacheKeys)**. A precision
  change therefore produces a distinct compilation-cache entry rather than silently reusing a
  kernel compiled for another mode. When the global precision is not `DEFAULT`, a one-time
  `kPerformance` warning suggests `torch.set_float32_matmul_precision('medium')`.

## Why it matters / when it applies
- The MXU natively multiplies `bfloat16` and accumulates in `float32`; a `float32` matmul at
  `DEFAULT` is computed in a single bf16 pass. `HIGH`/`HIGHEST` emulate more significand bits by
  splitting each `float32` into a sum of 3 bf16 terms and expanding the product (Henry, Tang,
  Heinecke, arXiv 1904.06376); 3 of the 9 cross products always underflow, giving the 6-pass
  `HIGHEST` mode. See [MXU bf16 arithmetic](mxu-bf16-arithmetic.md).
- Theoretical cost is 3x / 6x MXU work, but the doc notes this rarely materializes: modern
  bf16-weight models have large contracting dims where accumulation noise dominates, and older
  `float32` models are usually HBM-bound, so the extra passes fill otherwise idle MXU cycles.
- Perf lens: for a hypothesis about matmul throughput, first check whether the run sets a non-default
  global precision (the warning above is the tell); `HIGHEST` on a compute-bound model can cost
  up to 6x on the affected dots. Changing mode mid-run forces recompiles (new cache keys).
- Precision may vary across TPU generations - the StableHLO-to-ISA lowering is not fully specified.

## Connections
- Code concepts: [dtype-and-precision](../concepts/dtype-and-precision.md),
  [compilation-cache-key](../concepts/compilation-cache-key.md),
  [context-states-and-execution-modes](../concepts/context-states-and-execution-modes.md),
  [scaled-dot-product-attention](../concepts/scaled-dot-product-attention.md),
  [torch-compile-backend](../concepts/torch-compile-backend.md)
- Module catalogs: [csrc/ops/precision_context.cc](../catalog/csrc/ops/precision_context.cc.md),
  [src/torch_tpu/_internal/precision/precision](../catalog/src/torch_tpu/_internal/precision/precision.md),
  [src/torch_tpu/_loader](../catalog/src/torch_tpu/_loader.md)
- Related doc-concepts: [global-and-local-knobs](global-and-local-knobs.md), [mxu-bf16-arithmetic](mxu-bf16-arithmetic.md),
  [excess-precision](excess-precision.md), [tpu-cpu-numerical-parity](tpu-cpu-numerical-parity.md)

## Source
Extracted from `docs/markdown/precision_management.md` (kept in place).
