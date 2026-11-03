---
title: Multi-host execution backends (mp TCPStore rendezvous vs Ray)
type: doc-concept
provenance: doc
source: docs/user_guide/multihost.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-11-03T02:35:38Z}
---
# Multi-host execution backends (mp TCPStore rendezvous vs Ray)

## Definition
When a deployment spans several TPU VM hosts of one pod slice (e.g. v7x-16/32/64,
v6e-16), every torch_tpu process must know the whole ICI mesh before workers start.
vllm-torchtpu offers two backends, chosen by `TPU_MULTIHOST_BACKEND`: the default
**`mp`** backend, where each host runs its own `vllm serve` and a short
`torch.distributed` `TCPStore` rendezvous exchanges host addresses (no Ray), and the
**`ray`** backend, where one driver on the head node schedules Ray workers across the
cluster. The `mp` backend has two launch modes: **Mode A** (`--nnodes N`, TP/PP/PCP
spanning hosts; host 0 serves HTTP, others `--headless`) and **Mode B** (multi-host
DP: `--data-parallel-size` wider than `--data-parallel-size-local`, each host passing
its `--data-parallel-start-rank`).

## In vllm-torchtpu (grounded)
- Backend selection: [`TPU_MULTIHOST_BACKEND`](../catalog/src/vllm_torchtpu/envs.md#TPU_MULTIHOST_BACKEND)
  (`""`, `mp` or `ray`; anything else raises) is read in
  [`TpuPlatform.check_and_update_config`](../catalog/src/vllm_torchtpu/platforms/tpu_platform.md#TpuPlatform.check_and_update_config).
  An unset value still means `mp` whenever `--nnodes > 1` is passed.
- Mode A bootstrap: [`prepare_mp_multihost_env`](../catalog/src/vllm_torchtpu/distributed/tpu_mp_multihost.md#prepare_mp_multihost_env)
  runs the rendezvous ([`_rendezvous_host_ips`](../catalog/src/vllm_torchtpu/distributed/tpu_mp_multihost.md#_rendezvous_host_ips),
  host 0 is the store master, port from [`_rendezvous_port`](../catalog/src/vllm_torchtpu/distributed/tpu_mp_multihost.md#_rendezvous_port)
  = [`TORCH_TPU_MP_RENDEZVOUS_PORT`](../catalog/src/vllm_torchtpu/envs.md#TORCH_TPU_MP_RENDEZVOUS_PORT)
  or the coordination port + 1) and writes `TORCH_TPU_SLICEBUILDER_ADDRESSES` (one
  `ip:port` per worker, ports from [`TORCH_TPU_BASE_PORT`](../catalog/src/vllm_torchtpu/envs.md#TORCH_TPU_BASE_PORT))
  and `TORCH_TPU_TOPOLOGY` (from [`get_tpu_multihost_topology`](../catalog/src/vllm_torchtpu/platforms/tpu_platform.md#get_tpu_multihost_topology)),
  then forces [`TpuMultiprocExecutor`](../catalog/src/vllm_torchtpu/executors/tpu_multiproc_executor.md#TpuMultiprocExecutor).
  A shared xprof session id rides along so multi-host profiler traces merge.
- Mode B bootstrap: [`prepare_mp_multihost_dp_env`](../catalog/src/vllm_torchtpu/distributed/tpu_mp_multihost.md#prepare_mp_multihost_dp_env)
  does the same for the host's slice of DP ranks.
- Why it runs in the platform hook (from the module docstring): the headless node's
  `run_headless()` uses vanilla vLLM `MultiprocExecutor`, so the TPU executor's init
  never runs there; `check_and_update_config` fires identically on leader and headless
  nodes during `VllmConfig` construction - matching the doc's "during VllmConfig
  initialization" claim.
- Ray backend: [`RayDistributedExecutor`](../catalog/src/vllm_torchtpu/executors/ray_distributed_executor.md#RayDistributedExecutor)
  (and [`RayDistributedExecutorV2`](../catalog/src/vllm_torchtpu/executors/ray_distributed_executor_v2.md#RayDistributedExecutorV2))
  build the same slice-builder address list from Ray actors
  ([`RayDistributedExecutor._init_workers_ray`](../catalog/src/vllm_torchtpu/executors/ray_distributed_executor.md#RayDistributedExecutor._init_workers_ray));
  env vars listed in [`TpuPlatform.additional_env_vars`](../catalog/src/vllm_torchtpu/platforms/tpu_platform.md#TpuPlatform.additional_env_vars)
  are forwarded to the workers. Cluster setup on GCE is scripted in
  `scripts/multihost/` (the doc includes `examples/multihost/README.md`).

## Why it matters / when it applies
- Needed whenever `DP * TP * PP * PCP` exceeds one host's logical devices (8 on a
  4-chip v7x host). The doc's examples serve Qwen3.5-397B with TP16+EP over two hosts
  (Mode A) or DP16+EP with 8 local ranks per host (Mode B).
- `mp` avoids a Ray cluster and its scheduling overhead; Ray remains for GCE
  deployments that already run one.
- Port collisions are a common multi-host failure: the slice-builder base port, the
  rendezvous port and vLLM's own coordination port are all distinct knobs, and none of
  them join the compile cache key.

## Connections
- Code concepts: [distributed-parallelism-and-meshes](../concepts/distributed-parallelism-and-meshes.md), [tpu-platform](../concepts/tpu-platform.md)
- Module catalogs: [tpu_mp_multihost](../catalog/src/vllm_torchtpu/distributed/tpu_mp_multihost.md), [tpu_multiproc_executor](../catalog/src/vllm_torchtpu/executors/tpu_multiproc_executor.md), [ray_distributed_executor](../catalog/src/vllm_torchtpu/executors/ray_distributed_executor.md), [tpu_platform](../catalog/src/vllm_torchtpu/platforms/tpu_platform.md)
- Related doc-concepts: [composable-6d-parallelism](composable-6d-parallelism.md), [dp-ep-moe-layouts](dp-ep-moe-layouts.md), [env-var-reference-by-subsystem](env-var-reference-by-subsystem.md)

## Source
Extracted from `docs/user_guide/multihost.md` (kept in place).
