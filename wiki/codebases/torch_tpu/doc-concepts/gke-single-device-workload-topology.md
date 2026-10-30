---
title: GKE workload topology and launch environment (TORCH_TPU_TOPOLOGY)
type: doc-concept
provenance: doc
source: docs/markdown/1_basics_3_get_started_on_gke.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T02:38:46Z}
---
# GKE workload topology and launch environment (TORCH_TPU_TOPOLOGY)

## Definition
TPU v7 and later are reachable only through GKE, so the same single-device program from the VM tutorial is shipped as a container and submitted as a Kubernetes `Job` (or `JobSet` for multi-host) through Kueue. The doc's key mental model is the split between the **GKE topology** (the node selector `cloud.google.com/gke-tpu-topology: 2x2x1` - one host with 4 v7 chips / 8 TensorCores) and the **TorchTPU topology** the process is told to use, `TORCH_TPU_TOPOLOGY="1,1,1,1"` - one process driving one core while the other devices on the host are ignored.

## In torch_tpu (grounded)
- `TORCH_TPU_TOPOLOGY` is a registered env var, [`kTorchTpuTopologyEnvVar`](../catalog/csrc/common/env_vars.h.md#kTorchTpuTopologyEnvVar), commented "Set by Torch TPU specific launchers". It is read once (memoized) via [`GetEnvOnce`](../catalog/csrc/common/env_vars.h.md#GetEnvOnce) and is required by slicebuilder discovery when building the distributed worker configuration ([process-group-and-collectives](../concepts/process-group-and-collectives.md)).
- On the Python side, [`set_tpu_launch_env`](../catalog/src/torch_tpu/_internal/distributed/distributed.md#set_tpu_launch_env) decides `TORCH_TPU_TOPOLOGY`, `TORCH_TPU_SLICEBUILDER_ADDRESSES` and `TORCH_TPU_XPROF_SESSION_ID` in the parent process before any launcher spawns ranks. [`_parse_topology`](../catalog/src/torch_tpu/_internal/distributed/distributed.md#_parse_topology) accepts `x` or `,` separators, keeps the first three dims as the (Mx, My, Mz) chip mesh and drops extra trailing dims such as cores per chip - so the doc's 4-value `"1,1,1,1"` is a 1x1x1 chip mesh plus a per-chip core count of 1.
- The manifest also exports `TPU_LAUNCH_BLOCKING=1`. The variable TorchTPU actually reads is `TORCH_TPU_LAUNCH_BLOCKING` ([`kTorchTpuLaunchBlockingEnvVar`](../catalog/csrc/common/env_vars.h.md#kTorchTpuLaunchBlockingEnvVar)), which [`GetDefaultEagerMode`](../catalog/csrc/eager/eager_mode.cc.md#GetDefaultEagerMode) maps to `EagerMode::kDeferNeverAndLaunchBlocking` (the CUDA_LAUNCH_BLOCKING analogue). The unprefixed name appears only in the example manifests and docs, so as written it does not switch TorchTPU's eager mode in v0.2.0 (nothing in the torch_tpu tree reads it) - an easy misread when debugging or benchmarking.

## Why it matters / when it applies
- **Topology is a performance and correctness input, not a label.** The GKE selector determines which chips the pod gets; `TORCH_TPU_TOPOLOGY` determines what mesh TorchTPU builds. Running one process on one core of a 4-chip host leaves 7/8 of the hardware idle - fine for a smoke test, wrong for benchmarking. For multi-host jobs the externally supplied topology is also used to derive topologically contiguous `NODE_RANK`s.
- **Launch-blocking mode serializes every op** (no deferral, synchronous launch). Use it only for debugging; leaving it on in a perf run measures dispatch latency, not the model.
- Kueue mechanics from the doc: a universal `LocalQueue lq` admits into `ClusterQueue tpu-cluster-queue` in cohort `tpu-shared-reservation`; Kueue maps the pod's topology node selector to a `ResourceFlavor` (`rf-4chip` ... `rf-64chip`) and keeps the job suspended until cohort quota is reserved.
- The default image is a nightly `torch-tpu:nightly-latest`; rebuilding (`docker/build_image_multistage.sh`) is only needed after local changes to torch_tpu or its examples.

## Multi-process slices: one process per TensorCore (from the GKE TPUv7 distributed doc)
The follow-up doc `docs/markdown/1_basics_5_distributed_on_gke.md` runs the manual tensor-parallel example on the whole host instead of one core:
- **Single host (4 chips / 8 devices).** The node selector stays `cloud.google.com/gke-tpu-slice-topology: 2x2x1`, but the pod sets `TORCH_TPU_TOPOLOGY="2,2,1,2"` - a 2x2x1 chip mesh with 2 cores per chip - because TorchTPU launches **one process per TPU core**. [`_parse_topology`](../catalog/src/torch_tpu/_internal/distributed/distributed.md#_parse_topology) keeps the 2x2x1 chip bounds (the 4th value is the per-chip core count) for host ranking. The container runs `eval $(python3 -m torch.tpu.distributed)` (which fills `TORCH_TPU_SLICEBUILDER_ADDRESSES`, `WORLD_SIZE` etc. via [`set_tpu_launch_env`](../catalog/src/torch_tpu/_internal/distributed/distributed.md#set_tpu_launch_env) without overwriting the pinned topology) and then `torch.distributed.run --nproc_per_node=$WORLD_SIZE` - the same flow as on a VM ([torchrun-launch-and-tpu-dist-ddp](torchrun-launch-and-tpu-dist-ddp.md)). Manifest: `examples/tensor_parallel/torchtpu_singlehost_slice_job.yaml` (a Kubernetes `Job`, with the image and node pool patched in by `sed`).
- **Multi-host (64 chips / 128 devices).** `examples/tensor_parallel/torchtpu_multihost_slice_jobset.yaml` is a `JobSet` over a `4x4x4` slice with `TORCH_TPU_TOPOLOGY="4,4,4,2"`. Supplying the full-slice topology from outside is what lets `set_tpu_launch_env` give each host a `NODE_RANK` ordered by its physical coordinates ([`_calculate_topological_node_rank`](../catalog/src/torch_tpu/_internal/distributed/distributed.md#_calculate_topological_node_rank)), so ranks are topologically contiguous - which matters for collective locality.
- The doc's example exports `TPU_LAUNCH_BLOCKING=1` too (see above: not the variable TorchTPU reads). It refers to the worker as `dtp_worker.py`; in v0.2.0 the script `launch_singlehost.sh` actually launches `tp_worker.py` with `--nproc_per_node=8`.

## Connections
- Code concepts: [distributed-launchers-and-spmd](../concepts/distributed-launchers-and-spmd.md), [process-group-and-collectives](../concepts/process-group-and-collectives.md), [context-states-and-execution-modes](../concepts/context-states-and-execution-modes.md), [hardware-introspection](../concepts/hardware-introspection.md), [pjrt-client](../concepts/pjrt-client.md)
- Module catalogs: [csrc/common/env_vars.h](../catalog/csrc/common/env_vars.h.md), [src/torch_tpu/_internal/distributed/distributed](../catalog/src/torch_tpu/_internal/distributed/distributed.md), [csrc/eager/eager_mode.cc](../catalog/csrc/eager/eager_mode.cc.md)
- Related doc-concepts: [tpu-device-backend-initialization](tpu-device-backend-initialization.md), [global-and-local-knobs](global-and-local-knobs.md), [torchrun-launch-and-tpu-dist-ddp](torchrun-launch-and-tpu-dist-ddp.md), [spmd-lockstep-and-collective-fusion](spmd-lockstep-and-collective-fusion.md), [eager-execution-modes](eager-execution-modes.md)

## Source
Extracted from `docs/markdown/1_basics_3_get_started_on_gke.md` and (multi-process slices section) `docs/markdown/1_basics_5_distributed_on_gke.md` (kept in place). The `TPU_LAUNCH_BLOCKING` vs `TORCH_TPU_LAUNCH_BLOCKING` discrepancy was checked against `csrc/common/env_vars.h` and `csrc/eager/eager_mode.cc` at v0.2.0.
