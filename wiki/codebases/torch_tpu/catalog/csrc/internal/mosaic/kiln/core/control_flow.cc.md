---
title: 'Module: csrc/internal/mosaic/kiln/core/control_flow.cc'
type: catalog
provenance: extracted
module: csrc/internal/mosaic/kiln/core/control_flow.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/kiln/
symbols:
  If: If(223c9639b047ca9b).
  For: For(cabc373acf624fed).
  ToIndex: '`$anonymous_namespace_csrc/internal/mosaic/kiln/core/control_flow.cc`/ToIndex(300f125df43bc8c2).'
---
# Module: [`csrc/internal/mosaic/kiln/core/control_flow.cc`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/control_flow.cc)

## Functions
- <a id="For"></a>`For(IndexArg lower, IndexArg upper, absl::FunctionRef<void(Scalar)> body)` — [`L64`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/control_flow.cc#L64) — documented in [kiln-kernel-dsl](../../../../../../concepts/kiln-kernel-dsl.md)
- `If(Cond cond, absl::FunctionRef<void()> then_body, absl::FunctionRef<void()> else_body)` — [`L52`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/control_flow.cc#L52)
- <a id="If"></a>`If(Cond cond, absl::FunctionRef<void()> then_body)` — [`L43`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/control_flow.cc#L43) — Structured control flow inside a kernel body. — documented in [kiln-kernel-dsl](../../../../../../concepts/kiln-kernel-dsl.md)
- <a id="ToIndex"></a>`ToIndex(mlir::ImplicitLocOpBuilder& b, const IndexArg& arg)` — [`L33`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/control_flow.cc#L33)

