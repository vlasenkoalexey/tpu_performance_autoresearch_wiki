---
title: TPU device backend initialization (the "tpu" device string)
type: doc-concept
provenance: doc
source: docs/markdown/get_started_tpu.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T02:38:46Z}
---
# TPU device backend initialization (the "tpu" device string)

## Definition
The getting-started docs present TorchTPU as a drop-in device: `torch.device("tpu")` replaces `torch.device("cuda")`, tensors move with `.to("tpu")` or are created with `device="tpu"`, and results come back with `.cpu()`. The docs say the backend "must be explicitly initialized" so that the `"tpu"` string is registered with PyTorch before any tensor is moved; the porting rule is literally "change from cuda to tpu".

## In torch_tpu (grounded)
In v0.2.0 the "initialization" is not a user call - it happens on `import torch` through PyTorch's device-backend autoload, driven by [`_loader`](../catalog/src/torch_tpu/_loader.md):
- The module captures `TORCH_DEVICE_BACKEND_AUTOLOAD`, sets it to `0` while importing torch (to avoid re-entry), and [`load`](../catalog/src/torch_tpu/_loader.md#load) restores it and, if [`get_tpu_device_count`](../catalog/src/torch_tpu/_internal/utils/hardware.md#get_tpu_device_count) finds TPU chips, calls [`_init_device`](../catalog/src/torch_tpu/_loader.md#_init_device) once under a lock.
- [`_init_device_impl`](../catalog/src/torch_tpu/_loader.md#_init_device_impl) renames the `PrivateUse1` dispatch key to `"tpu"` (`torch.utils.rename_privateuse1_backend`), generates the `Tensor.is_tpu` / `Module.tpu()` convenience methods, registers the dynamo `DeviceInterface` and the `torch.tpu` device module, registers the `tpu_dist` distributed backend, and redirects `torch.compile` to the TorchTPU backend by default.
- It also emits an `[UNOPTIMIZED BUILD]` warning via [`_warn_if_unoptimized`](../catalog/src/torch_tpu/_loader.md#_warn_if_unoptimized) when the wheel was not compiled with `-c opt` - a perf trap worth checking first when numbers look wrong.
- The package import itself (`src/torch_tpu/__init__.py`) installs the PyTorch-version glue loader and configures the `libtpu` library path before the loader runs (see [python-version-support-policy](python-version-support-policy.md)).

Once registered, every ATen op on a `"tpu"` tensor dispatches through the `PrivateUse1` kernels described in [eager-op-dispatch](../concepts/eager-op-dispatch.md). `.cpu()` is a TPU->CPU copy ([`AtenCopyFrom`](../catalog/csrc/ops/copy_from/copy_from_aten_kernels.cc.md#AtenCopyFrom "csrc/ops/copy_from/copy_from_aten_kernels.cc:L232") -> [`CopyTpuToCpu`](../catalog/csrc/ops/copy_from/tpu_to_cpu.cc.md#CopyTpuToCpu "csrc/ops/copy_from/tpu_to_cpu.cc:L77")), which is the point where pending device work must be materialized.

## Why it matters / when it applies
- **Porting cost is near zero at the device-string level**, but the docs' "compute and materialize" step is the first hint that `.cpu()` / `.item()` are synchronization points; see [host-sync-avoidance-in-training-loops](host-sync-avoidance-in-training-loops.md).
- Initialization is skipped when no TPU chips are visible, so a CPU-only host imports cleanly but has no `"tpu"` device.
- The docs pin Python 3.12 and say not to install a separate PyTorch: the wheel pulls the matching CPU PyTorch, and the C++ glue is chosen per PyTorch version at import time.
- The VM tutorial notes TPU v7 and later are reachable only through GKE; the same program then runs under a pod manifest ([gke-single-device-workload-topology](gke-single-device-workload-topology.md)).

## Connections
- Code concepts: [eager-op-dispatch](../concepts/eager-op-dispatch.md), [host-device-copy](../concepts/host-device-copy.md), [deferred-execution-and-materialization](../concepts/deferred-execution-and-materialization.md), [hardware-introspection](../concepts/hardware-introspection.md), [torch-compile-backend](../concepts/torch-compile-backend.md), [pjrt-client](../concepts/pjrt-client.md)
- Module catalogs: [src/torch_tpu/_loader](../catalog/src/torch_tpu/_loader.md), [src/torch_tpu/_internal/utils/hardware](../catalog/src/torch_tpu/_internal/utils/hardware.md), [csrc/ops/copy_from/copy_from_aten_kernels.cc](../catalog/csrc/ops/copy_from/copy_from_aten_kernels.cc.md)
- Related doc-concepts: [host-sync-avoidance-in-training-loops](host-sync-avoidance-in-training-loops.md), [gke-single-device-workload-topology](gke-single-device-workload-topology.md), [python-version-support-policy](python-version-support-policy.md), [torchtpu-user-guide-map](torchtpu-user-guide-map.md), [torch-tpu-architecture-and-lowering-stack](torch-tpu-architecture-and-lowering-stack.md)

## Source
Extracted from `docs/markdown/get_started_tpu.md` and its near-duplicate `docs/markdown/1_basics_2_get_started_on_vm.md` (kept in place).
