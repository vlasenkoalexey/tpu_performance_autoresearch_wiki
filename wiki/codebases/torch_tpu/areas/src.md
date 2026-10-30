---
title: 'Area: src'
type: area
area: 'src'
description: 'Python package of torch_tpu: device registration and public API, the torch.compile backend and its static/dynamic compilers, FX passes, distributed launchers, Pallas bridge, optimizers, profiler and hardware helpers.'
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T02:38:46Z}
---
# Area: `src`

## Purpose
`src/torch_tpu/` is the Python face of torch_tpu. Importing it (through PyTorch's device-backend autoload) loads the C++ extension, registers the `tpu` device module and the lazy public API under `torch.tpu`, and patches the few upstream entry points that need TPU-specific behavior. Most user-facing performance knobs that are not environment variables live here.

The largest unit is the torch.compile backend ([torch-compile-backend](../concepts/torch-compile-backend.md)): `TpuBackend` captures an FX graph, runs the FX rewrites in [fx-graph-passes](../concepts/fx-graph-passes.md), splits graphs at collectives unless ranks are proven identical, and compiles through the C++ [compiled-mode](../concepts/compiled-mode.md). Symbolic shapes go through the bucketed [dynamic-shapes-compiler](../concepts/dynamic-shapes-compiler.md). Around it sit the distributed launchers and SPMD helpers ([distributed-launchers-and-spmd](../concepts/distributed-launchers-and-spmd.md)), the JAX/Pallas custom-kernel bridge ([pallas-custom-kernels](../concepts/pallas-custom-kernels.md)), TPU-aware optimizers ([python-optimizers](../concepts/python-optimizers.md)), Python ops such as splash attention and scaled matmul ([python-ops](../concepts/python-ops.md)), hardware and API-lifecycle utilities ([hardware-introspection](../concepts/hardware-introspection.md)) and the xprof/Kineto profiler integration ([profiler](../concepts/profiler.md)).

## How the units connect
- The compile stack is layered: [torch-compile-backend](../concepts/torch-compile-backend.md) picks the static or the [dynamic-shapes-compiler](../concepts/dynamic-shapes-compiler.md), both apply [fx-graph-passes](../concepts/fx-graph-passes.md), and both lower through the C++ [compiled-mode](../concepts/compiled-mode.md) and [compilation-cache](../concepts/compilation-cache.md).
- [distributed-launchers-and-spmd](../concepts/distributed-launchers-and-spmd.md) feeds the compile stack: its handshake is what lets the backend skip splitting graphs at collectives; the collectives themselves are C++ ([process-group-and-collectives](../concepts/process-group-and-collectives.md)).
- [python-optimizers](../concepts/python-optimizers.md) either trace into the graph (hyperparameters frozen) or call the [fused-optimizer-kernels](../concepts/fused-optimizer-kernels.md); [python-ops](../concepts/python-ops.md) and [pallas-custom-kernels](../concepts/pallas-custom-kernels.md) are the two ways to bring a JAX/Pallas kernel into a torch program.
- **Small units without their own page**: the package root (`_loader.py`, versioned `.so` loading, tcmalloc check), `_internal/` (device module, env helpers, public-API table, streams, warnings), `_internal/sync` (`torch.tpu.synchronize` -> [tensor-synchronization](../concepts/tensor-synchronization.md)), `_internal/precision` (-> [dtype-and-precision](../concepts/dtype-and-precision.md)), `_internal/profiler` (-> [profiler](../concepts/profiler.md)), `_internal/export`, `_internal/optim` and `_internal/performance`.

## Units
Units of `src/` with their own mechanism page (pinned in `config/torch_tpu.md`); the package root, `_internal/` and the small `_internal/*` units are catalog-only and summarized above. Module map: [catalog/index.md](../catalog/index.md).

| Unit | Page |
|---|---|
| `src/torch_tpu/_internal/compile` | [torch-compile-backend](../concepts/torch-compile-backend.md) |
| `src/torch_tpu/_internal/compile/dynamic` | [dynamic-shapes-compiler](../concepts/dynamic-shapes-compiler.md) |
| `src/torch_tpu/_internal/compile/fx_passes` | [fx-graph-passes](../concepts/fx-graph-passes.md) |
| `src/torch_tpu/_internal/distributed` | [distributed-launchers-and-spmd](../concepts/distributed-launchers-and-spmd.md) |
| `src/torch_tpu/_internal/pallas` | [pallas-custom-kernels](../concepts/pallas-custom-kernels.md) |
| `src/torch_tpu/_internal/optimizers` | [python-optimizers](../concepts/python-optimizers.md) |
| `src/torch_tpu/_internal/ops` | [python-ops](../concepts/python-ops.md) |
| `src/torch_tpu/_internal/utils` | [hardware-introspection](../concepts/hardware-introspection.md) |
