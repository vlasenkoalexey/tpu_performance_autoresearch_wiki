---
title: Reading a TPU trace - red flags and the ideal profile
type: doc-concept
provenance: doc
source: docs/markdown/performance_profiling.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T02:38:46Z}
---
# Reading a TPU trace - red flags and the ideal profile

## Definition
The profiling doc gives a short diagnostic vocabulary for xprof traces of TorchTPU workloads: three
red-flag patterns (large gaps between TPU ops, frequent short TPU bursts, low MXU utilization), each
with its usual cause and fix, plus a picture of the ideal profile. The error-glossary doc adds a
fourth, ATen-level signal: high `aten::copy_` / `aten::_to_copy` counts in a CPU-only
`torch.profiler` table mean host round-trips ("performance cliffs").

## In torch_tpu (grounded)
| Pattern | Doc's meaning | Doc's fix | Where it comes from in torch_tpu |
|---|---|---|---|
| Large gaps between TPU ops | host-side bottleneck: data loading, Python overhead | prefetch data, cut Python work in the loop | dispatch cost of [eager op dispatch](../concepts/eager-op-dispatch.md); synchronous host waits |
| Frequent short TPU bursts | too many graph breaks -> frequent recompilation / tiny executables | reduce `.item()` / `.cpu()`, use `torch.compile` | each host read forces materialization of the pending graph - e.g. `.item()` lands in [`AtenLocalScalarDense`](../catalog/csrc/ops/copy_from/copy_from_aten_kernels.cc.md#AtenLocalScalarDense "csrc/ops/copy_from/copy_from_aten_kernels.cc:L254"), `.cpu()` in [`CopyTpuToCpu`](../catalog/csrc/ops/copy_from/tpu_to_cpu.cc.md#CopyTpuToCpu "csrc/ops/copy_from/tpu_to_cpu.cc:L77") |
| Low MXU utilization | dims not aligned to the 128 tile | pad dims to multiples of 128 | layout/padding is decided by XLA; check shapes in the HLO dump ([hlo-and-llo-compilation-dumps](hlo-and-llo-compilation-dumps.md)) |
| Many `aten::copy_` / `aten::_to_copy` rows | CPU fallbacks / host round-trips | keep tensors on device, remove the host hop | [`AtenCopy_`](../catalog/csrc/ops/copy_from/copy_from_aten_kernels.cc.md#AtenCopy_ "csrc/ops/copy_from/copy_from_aten_kernels.cc:L268") / [`AtenCopyFrom`](../catalog/csrc/ops/copy_from/copy_from_aten_kernels.cc.md#AtenCopyFrom "csrc/ops/copy_from/copy_from_aten_kernels.cc:L232") classify the copy via [`GetCopyType`](../catalog/csrc/ops/copy_from/copy_from_aten_kernels.cc.md#GetCopyType "csrc/ops/copy_from/copy_from_aten_kernels.cc:L61") |

Why a pending graph is cut is recorded as a
[`MaterializationReason`](../catalog/csrc/eager/structured_log_buffer.h.md#MaterializationReason "csrc/eager/structured_log_buffer.h:L36")
in the eager structured log - the code-side counterpart of "short bursts".

## Why it matters / when it applies
**The ideal profile:** long continuous TPU compute blocks (the compiler fused many ops into one
executable), minimal CPU -> TPU gaps (input pipeline overlapped with compute), MXU utilization above
~60% (hardware-aligned shapes).

Perf lens / how to use it:
- Gaps and short bursts are the signature of *host-bound* eager execution; the lever is fewer sync
  points and larger fused graphs (deferred/fused eager or `torch.compile`), not kernel work.
- Short bursts can also be recompilation: a burst preceded by a long host-side compile slice
  points to cache misses (shape churn) - see
  [compilation-cache](../concepts/compilation-cache.md) and
  [dynamic-shapes-compiler](../concepts/dynamic-shapes-compiler.md).
- Low MXU utilization with continuous blocks is a shape / layout problem; check whether matmul
  dims are multiples of 128 before chasing kernels.
- `torch._dynamo.explain(model)(input)` and `TORCH_LOGS="+dynamo"` locate the graph breaks the
  trace hints at (error-glossary quick reference).

## Connections
- Code concepts: [deferred-execution-and-materialization](../concepts/deferred-execution-and-materialization.md),
  [host-device-copy](../concepts/host-device-copy.md),
  [tensor-synchronization](../concepts/tensor-synchronization.md),
  [eager-op-dispatch](../concepts/eager-op-dispatch.md),
  [compilation-cache](../concepts/compilation-cache.md),
  [torch-compile-backend](../concepts/torch-compile-backend.md),
  [profiler](../concepts/profiler.md)
- Module catalogs: [csrc/ops/copy_from/copy_from_aten_kernels.cc](../catalog/csrc/ops/copy_from/copy_from_aten_kernels.cc.md),
  [csrc/ops/copy_from/tpu_to_cpu.cc](../catalog/csrc/ops/copy_from/tpu_to_cpu.cc.md),
  [csrc/eager/structured_log_buffer.h](../catalog/csrc/eager/structured_log_buffer.h.md)
- Related doc-concepts: [graph-breaks-on-tpu](graph-breaks-on-tpu.md), [host-sync-avoidance-in-training-loops](host-sync-avoidance-in-training-loops.md), [defer-and-fuse-materialization](defer-and-fuse-materialization.md), [graph-fingerprint-and-recompilation](graph-fingerprint-and-recompilation.md), [op-fusion-and-hbm-traffic](op-fusion-and-hbm-traffic.md), [xprof-profiling-workflow](xprof-profiling-workflow.md),
  [tpu-debugging-ladder](tpu-debugging-ladder.md), [hlo-and-llo-compilation-dumps](hlo-and-llo-compilation-dumps.md)

## Source
Extracted from `docs/markdown/performance_profiling.md` (= `docs/markdown/4_debugging_and_performance_analysis_2_xprof_for_torchtpu.md`)
and section 4a of `docs/markdown/error_glossary.md` (= `docs/markdown/4_debugging_and_performance_analysis_3_getting_better_error_information.md`), all kept in place.
