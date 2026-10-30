---
title: ATen and c10d ops as the IR TorchTPU lowers (and how to see them)
type: doc-concept
provenance: doc
source: docs/markdown/background_on_aten_ops.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T02:38:46Z}
---
# ATen and c10d ops as the IR TorchTPU lowers (and how to see them)

## Definition
Beyond functions and modules, PyTorch has a third class of callable: **ops**. Every high-level call is converted into **ATen** ops ("A Tensor Library") or, for inter-device communication, **c10d** ops; together these thousands of ops form PyTorch's intermediate representation. The doc's example: `torch.nn.Linear.forward` calls `torch.nn.functional.linear`, which becomes `at::addmm(bias, input, weight.t())` - i.e. the ATen ops `aten.t.default` and `aten.addmm.default`. To see the ATen sequence for any code, turn on AOT graph logging (`torch._logging.set_logs(aot_graphs=True)`) and run it under `torch.compile(backend="aot_eager")`; the log prints each op with dtype, shape and strides (e.g. `t: "f32[64, 64][1, 64]cpu" = torch.ops.aten.t.default(primals_1)`). The exercise answers show `torch.where(... > 0.1, ... <= 0.9)` lowering to `aten.gt.Scalar` and `aten.le.Scalar`.

## In torch_tpu (grounded)
- ATen is exactly the layer TorchTPU implements: each ATen op registered for the `"tpu"` device has a C++ kernel that builds StableHLO and enters [`DispatchOp`](../catalog/csrc/eager/op_dispatcher.h.md#DispatchOp). For the doc's examples: `addmm` -> [`AtenAddmmOut`](../catalog/csrc/ops/addmm/addmm_aten_kernels.cc.md#AtenAddmmOut); `gt.Scalar` / `le.Scalar` -> [`AtenGtScalarOut`](../catalog/csrc/ops/binary_aten_kernels.cc.md#AtenGtScalarOut) / [`AtenLeScalarOut`](../catalog/csrc/ops/binary_aten_kernels.cc.md#AtenLeScalarOut), which share [`AtenComparisonScalarOutHelper`](../catalog/csrc/ops/binary_aten_kernels.cc.md#AtenComparisonScalarOutHelper) and wrap the Python scalar (`0.1`, `0.9`) in a [`PromotedScalar`](../catalog/csrc/common/cache_key.h.md#PromotedScalar), so changing the threshold does not change the compiled graph. `t` is a view op, handled by view decomposition rather than a compute kernel.
- Each kernel is tagged with an [`OpName`](../catalog/csrc/ops/op_names.h.md#OpName); that name is part of the graph fingerprint and shows up in compiled module names and HLO metadata.
- c10d ops are implemented by the `tpu_dist` process group, [`ProcessGroupTpu`](../catalog/csrc/distributed/process_group_tpu.h.md#ProcessGroupTpu).
- The same ATen-level IR drives both execution paths: eager dispatch per op, and under `torch.compile` the AOT-autograd FX graph of ATen ops handed to [`TpuBackend.__call__`](../catalog/src/torch_tpu/_internal/compile/_backend.md#TpuBackend.__call__).

## Why it matters / when it applies
- The ATen sequence (not the Python source) is what TorchTPU fingerprints and compiles. Reading the `aot_graphs` log tells you which kernels a model actually hits, which ops are decomposed, and where views/transposes appear - the starting point for asking "which TorchTPU kernel is slow?"
- The `[strides]` in the log matter on TPU: non-contiguous views become explicit slice/transpose work after view decomposition.
- An op that has no TPU kernel either decomposes into supported ATen ops or falls back to CPU (`enable_cpu_fallback`, see [eager-execution-modes.md](eager-execution-modes.md)) - the latter costs host round-trips.
- The `aot_eager` trick runs on CPU, so the op inventory can be gathered without a TPU.

## Connections
- Code concepts: [aten-kernel-authoring](../concepts/aten-kernel-authoring.md), [eager-op-dispatch](../concepts/eager-op-dispatch.md), [op-names-and-python-context](../concepts/op-names-and-python-context.md), [view-decomposition](../concepts/view-decomposition.md), [stablehlo-op-builder](../concepts/stablehlo-op-builder.md), [process-group-and-collectives](../concepts/process-group-and-collectives.md), [torch-compile-backend](../concepts/torch-compile-backend.md), [python-ops](../concepts/python-ops.md)
- Module catalogs: [csrc/eager/op_dispatcher.h](../catalog/csrc/eager/op_dispatcher.h.md), [csrc/ops/addmm/addmm_aten_kernels.cc](../catalog/csrc/ops/addmm/addmm_aten_kernels.cc.md), [csrc/ops/binary_aten_kernels.cc](../catalog/csrc/ops/binary_aten_kernels.cc.md), [csrc/ops/op_names.h](../catalog/csrc/ops/op_names.h.md), [csrc/distributed/process_group_tpu.h](../catalog/csrc/distributed/process_group_tpu.h.md)
- Related doc-concepts: [torch-tpu-architecture-and-lowering-stack.md](torch-tpu-architecture-and-lowering-stack.md), [xla-lowering-stablehlo-hlo-llo.md](xla-lowering-stablehlo-hlo-llo.md), [extending-via-composition.md](extending-via-composition.md), [custom-autograd-function.md](custom-autograd-function.md), [graph-fingerprint-and-recompilation.md](graph-fingerprint-and-recompilation.md)

## Source
Extracted from `docs/markdown/background_on_aten_ops.md` (kept in place).
