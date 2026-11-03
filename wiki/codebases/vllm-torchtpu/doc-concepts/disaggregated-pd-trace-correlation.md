---
title: Profiling disaggregated prefill/decode (Raiden3 KV transfer trace markers)
type: doc-concept
provenance: doc
source: docs/developers_guide/profiling/disaggregated.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-11-03T02:35:38Z}
---
# Profiling disaggregated prefill/decode (Raiden3 KV transfer trace markers)

## Definition
In prefill/decode (PD) disaggregation, prompt ingestion runs on a **prefill** set of TPU
pods (`kv_producer`) and generation on a separate **decode** set (`kv_consumer`),
connected by the native Raiden3 KV transfer engine. Each side has its own workers and
its own profiler, so one disaggregated request appears in two independent traces.
vllm-torchtpu correlates them by emitting named trace annotations that carry the shared
Raiden transfer `uuid` and `request_id`. The doc marks the workflow experimental.

## In vllm-torchtpu (grounded)
- Connector: [`TPURaidenConnector`](../catalog/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.md#TPURaidenConnector)
  with its worker half
  [`TPURaidenConnectorWorker`](../catalog/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.md#TPURaidenConnectorWorker)
  (`vllm_torchtpu.distributed.kv_transfer.tpu_connector`).
- Annotation helper: [`TraceAnnotation`](../catalog/src/vllm_torchtpu/tracing/annotation.md#TraceAnnotation)
  wraps `torch.profiler.record_function` only while a profiler session is active, and
  encodes kwargs into the event name as `name#k=v,...#` - which is why searching the
  Trace Viewer for a `uuid` finds both sides.

| Role | Annotation | Metadata | Emitted in |
|---|---|---|---|
| Prefill | `KV_Cache_Prefill_Register_Blocks` | uuid, request_id, num_tokens, num_blocks | [`_register_stage3_request_blocks`](../catalog/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.md#TPURaidenConnectorWorker._register_stage3_request_blocks), [`_register_stage3_request_row_spans`](../catalog/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.md#TPURaidenConnectorWorker._register_stage3_request_row_spans) |
| Prefill | `KV_Cache_Prefill_Send_Complete` | uuid, request_id, num_tokens | [`_poll_finished`](../catalog/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.md#TPURaidenConnectorWorker._poll_finished) (producer release) |
| Decode | `KV_Cache_Decode_Submit_Load` | uuid, request_id, source_req_id, num_tokens, num_blocks | [`_submit_stage3_loads`](../catalog/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.md#TPURaidenConnectorWorker._submit_stage3_loads) |
| Decode | `KV_Cache_Decode_Recv_Complete` | uuid, request_id, source_req_id, num_tokens, `reshard_e2e_latency_ms` | [`_poll_finished`](../catalog/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.md#TPURaidenConnectorWorker._poll_finished) |

- Env vars the doc sets on both deployments:
  [`TPU_USE_RAIDEN_KV_CACHE_MANAGER`](../catalog/src/vllm_torchtpu/envs.md#TPU_USE_RAIDEN_KV_CACHE_MANAGER)`=1`,
  [`TPU_KV_RESHARD_TRANSPORT`](../catalog/src/vllm_torchtpu/envs.md#TPU_KV_RESHARD_TRANSPORT)`=raiden`
  (default `zmq`),
  [`TPU_RAIDEN_RESHARD_IMPL`](../catalog/src/vllm_torchtpu/envs.md#TPU_RAIDEN_RESHARD_IMPL)`=store`
  (default `controller`), plus `USE_PHASED_PROFILER=true` (optional).

## Workflow (from the doc)
1. Deploy both sides with `--profiler-config` writing to a mounted persistent volume
   and `--kv-transfer-config '{"kv_connector": "TPURaidenConnector",
   "kv_connector_module_path": "vllm_torchtpu.distributed.kv_transfer.tpu_connector",
   "kv_role": "kv_producer" | "kv_consumer", "kv_port": 14579}'`. Reference manifests:
   `docs/developers_guide/examples/raiden_pd_prefill.yaml` (v6e 2x2, PCP=4, TP=1) and
   `raiden_pd_decode.yaml` (v6e 2x2, DP=4, TP=1).
2. Arm `/start_profile` on **both** services, send the prefill request with
   `kv_transfer_params: {do_remote_decode: true}` and `max_tokens: 1`, pass the returned
   `kv_transfer_params` (uuid, source controller address, block ids) to the decode
   request, then `/stop_profile` on both.
3. With phased profiling the prefill pod writes `prefill_only/` and the decode pod
   `decode_only/`; copy both out and open them together in XProf, searching for the
   shared uuid.

## Why it matters / when it applies
- PD disaggregation trades transfer latency for phase isolation; the
  `reshard_e2e_latency_ms` field on `KV_Cache_Decode_Recv_Complete` and the gap between
  `Submit_Load` and `Recv_Complete` put the KV-transfer cost directly on the decode
  timeline, next to the decode steps it delays.
- Hybrid models (Mamba/GDN state blocks) transfer state spans alongside KV blocks, so
  the same markers cover them.
- Annotations are free when no profiler is active (`TraceAnnotation` checks
  `torch.autograd._profiler_enabled()`).

## Connections
- Code concepts: [kv-transfer-and-disaggregated-serving](../concepts/kv-transfer-and-disaggregated-serving.md),
  [tracing-annotations](../concepts/tracing-annotations.md),
  [kv-cache-layout-and-hbm-budget](../concepts/kv-cache-layout-and-hbm-budget.md),
  [host-offload](../concepts/host-offload.md)
- Module catalogs: [kv_transfer/tpu_connector](../catalog/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.md),
  [tracing/annotation](../catalog/src/vllm_torchtpu/tracing/annotation.md),
  [envs](../catalog/src/vllm_torchtpu/envs.md)
- Related doc-concepts: [phased-profiler](phased-profiler.md),
  [server-side-profiling-and-trace-options](server-side-profiling-and-trace-options.md),
  [multi-rank-trace-capture](multi-rank-trace-capture.md)

## Source
Extracted from `docs/developers_guide/profiling/disaggregated.md` (kept in place).
