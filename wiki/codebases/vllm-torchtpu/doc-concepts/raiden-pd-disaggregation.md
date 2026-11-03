---
title: Prefill/decode disaggregation with the Raiden KV connector
type: doc-concept
provenance: doc
source: docs/user_guide/disaggregated_serving.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-11-03T02:35:38Z}
---
# Prefill/decode disaggregation with the Raiden KV connector

## Definition
P/D disaggregation runs compute-bound **prefill** (`kv_role="kv_producer"`) and
HBM-bandwidth-bound **decode** (`kv_role="kv_consumer"`) on separate TPU engine pools,
so long prefills no longer stall ongoing decodes (no TPOT spikes) and each pool can use
its own parallelism layout. The guide describes two connectors: the **Raiden**
connector - a PJRT DMA/RDMA engine (via `tpu_sync`) coordinated by a central controller
(`examples/disagg/run_raiden_controller.py`), which supports **heterogeneous resharding**
(e.g. prefill `PCP=4, TP=2` -> decode `DP=8, TP=1`) - and a lighter host TCP /
side-channel connector for functional and single-host testing. A production deployment
is four parts: controller, prefill pool, decode pool, and a proxy router
(`examples/disagg/toy_proxy_server.py`) that sends a `max_tokens=1` request to prefill
and forwards the request plus KV transfer params to decode.

## In vllm-torchtpu (grounded)
- Connector classes (all in `distributed/kv_transfer/tpu_connector.py`):
  [`TPUConnector`](../catalog/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.md#TPUConnector)
  (host TCP/side-channel; ports from [`get_kv_transfer_port`](../catalog/src/vllm_torchtpu/distributed/utils.md#get_kv_transfer_port)
  and [`get_side_channel_port`](../catalog/src/vllm_torchtpu/distributed/utils.md#get_side_channel_port)),
  and [`TPURaidenConnector`](../catalog/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.md#TPURaidenConnector)
  (a `TPUConnector` with Raiden forced on) whose roles are
  [`TPURaidenConnectorScheduler`](../catalog/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.md#TPURaidenConnectorScheduler)
  and [`TPURaidenConnectorWorker`](../catalog/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.md#TPURaidenConnectorWorker).
  [`TPUMultiConnector`](../catalog/src/vllm_torchtpu/distributed/kv_transfer/tpu_multi_connector.md#TPUMultiConnector)
  combines Raiden P/D with host offload
  ([`TPURaidenOffloadingConnector`](../catalog/src/vllm_torchtpu/offload/raiden_connector.md#TPURaidenOffloadingConnector));
  children must be listed explicitly. All three names are registered with vLLM's
  connector factory by [`_register_tpu_kv_connectors`](../catalog/src/vllm_torchtpu/platforms/tpu_platform.md#_register_tpu_kv_connectors).
- Raiden env vars: [`TPU_USE_RAIDEN_KV_CACHE_MANAGER`](../catalog/src/vllm_torchtpu/envs.md#TPU_USE_RAIDEN_KV_CACHE_MANAGER)
  (Raiden-compatible block layout/manager; also makes `env_override` preset a 16 GiB
  premapped DMA buffer so KV copies avoid libtpu's slow staged path),
  [`TPU_RAIDEN_CONTROLLER_ADDRESS`](../catalog/src/vllm_torchtpu/envs.md#TPU_RAIDEN_CONTROLLER_ADDRESS),
  [`TPU_RAIDEN_JOB_NAME`](../catalog/src/vllm_torchtpu/envs.md#TPU_RAIDEN_JOB_NAME),
  [`TPU_RAIDEN_ENGINE_ID`](../catalog/src/vllm_torchtpu/envs.md#TPU_RAIDEN_ENGINE_ID),
  [`TPU_RAIDEN_TRANSFER_PARALLELISM`](../catalog/src/vllm_torchtpu/envs.md#TPU_RAIDEN_TRANSFER_PARALLELISM)
  (DMA streams, [`TPURaidenConnectorWorker._raiden_transfer_parallelism`](../catalog/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.md#TPURaidenConnectorWorker._raiden_transfer_parallelism)),
  [`TPU_RAIDEN_RESHARD_IMPL`](../catalog/src/vllm_torchtpu/envs.md#TPU_RAIDEN_RESHARD_IMPL)
  ([`_reshard_store_mode`](../catalog/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.md#_reshard_store_mode)),
  [`TPU_KV_RESHARD_TRANSPORT`](../catalog/src/vllm_torchtpu/envs.md#TPU_KV_RESHARD_TRANSPORT)
  ([`_use_raiden_stage3_transport`](../catalog/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.md#_use_raiden_stage3_transport)),
  and the per-model admission switch [`TPU_RAIDEN_QWEN35_ADMISSION`](../catalog/src/vllm_torchtpu/envs.md#TPU_RAIDEN_QWEN35_ADMISSION)
  used in the guide's launches (read by
  [`TPURaidenConnectorWorker.register_runner`](../catalog/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.md#TPURaidenConnectorWorker.register_runner)).
- Example launchers: `examples/disagg/launch_qwen35_disagg_multihost.sh`,
  `launch_dsv4_disagg_multihost.sh`, `run_qwen35_raiden_pcp8_dp8_live_pair.sh`, and the
  GKE JobSet manifests `qwen3.5-397b-1p1d.yaml` / `kimi-k3-1p1d-4dp8tp.yaml` under
  `.buildkite/kubernetes/manifests/workloads/`.

## Doc-vs-code disagreements
- The guide's `--kv-transfer-config` uses `"kv_connector": "TpuRaidenConnector"` with
  `"kv_connector_module_path": "vllm_torchtpu.distributed.kv_transfer.raiden.raiden_connector"`.
  Neither exists at this commit: the class is `TPURaidenConnector` in
  `vllm_torchtpu.distributed.kv_transfer.tpu_connector` (the form every example script
  and manifest uses), and `distributed/kv_transfer/raiden/` has no `raiden_connector.py`.
- `TPU_RAIDEN_RESHARD_IMPL` alternatives are `controller` / `store` (in-engine
  KVCacheStore on rank 0), not `controller` / `host`.
- `TPU_KV_RESHARD_TRANSPORT` alternatives are `zmq` / `raiden`, not `zmq` / `tcp`.
- The supported-models feature table names `TpuRaidenConnector` too; same caveat.

## Why it matters / when it applies
- Disaggregation is the main tail-latency lever for mixed long-prompt traffic and lets
  prefill use PCP (TTFT) while decode uses DP + EP (throughput) on the same model.
- Resharding cost is in the transfer path; `TPU_RAIDEN_TRANSFER_PARALLELISM` and the
  premapped buffer pool govern KV transfer bandwidth.
- Raiden is the only connector family accepted together with pipeline parallelism
  ([pipeline-parallel-stage-handoff](pipeline-parallel-stage-handoff.md)).
- Decode-side capacity eviction behavior is a separate contract:
  [decode-capacity-preemption-abort](decode-capacity-preemption-abort.md).

## Connections
- Code concepts: [kv-transfer-and-disaggregated-serving](../concepts/kv-transfer-and-disaggregated-serving.md), [host-offload](../concepts/host-offload.md), [kv-cache-layout-and-hbm-budget](../concepts/kv-cache-layout-and-hbm-budget.md), [tpu-schedulers](../concepts/tpu-schedulers.md)
- Module catalogs: [tpu_connector](../catalog/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.md), [tpu_multi_connector](../catalog/src/vllm_torchtpu/distributed/kv_transfer/tpu_multi_connector.md), [offload/raiden_connector](../catalog/src/vllm_torchtpu/offload/raiden_connector.md), [distributed/utils](../catalog/src/vllm_torchtpu/distributed/utils.md)
- Related doc-concepts: [decode-capacity-preemption-abort](decode-capacity-preemption-abort.md), [context-parallelism-pcp-dcp](context-parallelism-pcp-dcp.md), [env-var-reference-by-subsystem](env-var-reference-by-subsystem.md), [composable-6d-parallelism](composable-6d-parallelism.md)

## Source
Extracted from `docs/user_guide/disaggregated_serving.md` (sections 1-3, 5-6, kept in
place).
