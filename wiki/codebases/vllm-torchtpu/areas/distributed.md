---
title: 'Area: src/vllm_torchtpu/distributed'
type: area
area: 'src/vllm_torchtpu/distributed'
description: 'Process groups, op-local JAX meshes and transport for multi-device TPU serving: 6D parallelism (TP/DP/PP/EP/PCP/DCP), pipeline-stage hand-off, multi-host bootstrap, and the KV-transfer connector for prefill/decode disaggregation.'
updated: 2026-11-03
generated: {by: wikify/0.4.1, at: 2026-11-03T02:35:38Z}
---
# Area: `src/vllm_torchtpu/distributed`

## Purpose
This area is everything that crosses a device boundary. The model runner is deliberately single-device (one worker process per TPU device), so cross-rank work goes through two routes that this area provides. The first is ordinary `torch.distributed` collectives between ranks. The second is op-local JAX meshes over vLLM's EP, PCP and DCP process groups, so that one Pallas kernel can `shard_map` over several devices and fuse its transport (remote DMA, ring passes) into the kernel. [distributed-parallelism-and-meshes](../concepts/distributed-parallelism-and-meshes.md) owns that design: device order, mesh construction, `sharded_jax_op`, and the pipeline-parallel hand-off.

Its entry points are called from almost everywhere (124 outside callers for the core unit): the layer adapters and kernels ask it for mesh axes and op-local meshes, the platform and worker call its multi-host bootstrap, and the runner calls its pipeline-stage push/settle. The second unit, [kv-transfer-and-disaggregated-serving](../concepts/kv-transfer-and-disaggregated-serving.md), is the vLLM v1 KV connector that moves a prompt's KV cache (and recurrent GDN/Mamba state) from a prefill engine to a decode engine over one of three transports.

For TPU inference performance this is where collective placement is decided: whether a reduce-scatter is exposed or fused into a kernel, whether a ring uses ICI-adjacent chips, and how P/D disaggregation keeps long prefills from stalling decode steps.

## How the units connect
- [distributed-parallelism-and-meshes](../concepts/distributed-parallelism-and-meshes.md) (`distributed/`): `ep_mesh.py`, `pcp.py`, `dcp.py` build the op-local meshes; `chip_topology.py`, `mesh_utils.py`, `pcp_rank_order.py` decide device order; `sharded_jax_op.py` wraps a mesh-spanning JAX function as a torch custom op; the `pp_*.py` modules implement the pipeline-stage hand-off; `tpu_communicator.py` does EP dispatch/combine across data-parallel engines, `intra_chip.py` builds a process group over the cores of one physical chip (collectives stay on-package, so sharding a weight across a chip's cores can pay off), and `tpu_mp_multihost.py` bootstraps multi-host runs without Ray.
- [kv-transfer-and-disaggregated-serving](../concepts/kv-transfer-and-disaggregated-serving.md) (`distributed/kv_transfer/`) sits on top: it reads the KV pool layout and mesh geometry from the core unit to plan byte spans across heterogeneous producer and consumer meshes.

Kernels that consume these meshes include the [fused MoE kernels](../concepts/fused-moe-kernels.md), the [PCP streaming attention kernel](../concepts/pcp-streaming-rpa-kernel.md) and the [DSv4 StreamIndex top-k](../concepts/deepseek-v4-streamindex-topk-kernel.md) (DCP).

<!-- area:auto:begin -->
## Units
2 planned unit(s) in `src/vllm_torchtpu/distributed`; deep units have their own mechanism page, the rest are sections below.

| Unit | Modules | Symbols | Callers outside | Entry points | Page |
|---|---|---|---|---|---|
| `src/vllm_torchtpu/distributed/kv_transfer` | 15 | 945 | 10 | [`RaidenSendOutcome`](../catalog/src/vllm_torchtpu/distributed/kv_transfer/raiden_pd_completion.md#RaidenSendOutcome "src/vllm_torchtpu/distributed/kv_transfer/raiden_pd_completion.py:L70"), [`KVSaveNanCheck`](../catalog/src/vllm_torchtpu/distributed/kv_transfer/kv_save_nan_check.md#KVSaveNanCheck "src/vllm_torchtpu/distributed/kv_transfer/kv_save_nan_check.py:L63"), [`record`](../catalog/src/vllm_torchtpu/distributed/kv_transfer/kv_save_nan_check.md#KVSaveNanCheck.record "src/vllm_torchtpu/distributed/kv_transfer/kv_save_nan_check.py:L76") | [kv-transfer-and-disaggregated-serving](../concepts/kv-transfer-and-disaggregated-serving.md) |
| `src/vllm_torchtpu/distributed` | 17 | 313 | 124 | [`get_p2p_wait_pull_timeout`](../catalog/src/vllm_torchtpu/distributed/utils.md#get_p2p_wait_pull_timeout "src/vllm_torchtpu/distributed/utils.py:L92"), [`EP_AXIS_NAME`](../catalog/src/vllm_torchtpu/distributed/ep_mesh.md#EP_AXIS_NAME "src/vllm_torchtpu/distributed/ep_mesh.py:L56"), [`sharded_jax_op`](../catalog/src/vllm_torchtpu/distributed/sharded_jax_op.md#sharded_jax_op "src/vllm_torchtpu/distributed/sharded_jax_op.py:L135") | [distributed-parallelism-and-meshes](../concepts/distributed-parallelism-and-meshes.md) |

<!-- area:auto:end -->
