---
title: 'Module: src/vllm_torchtpu/distributed/utils.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/distributed/utils.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.distributed.utils`/
symbols:
  get_p2p_wait_pull_timeout: get_p2p_wait_pull_timeout().
  get_raiden_telemetry_module: get_raiden_telemetry_module().
  get_kv_ports: get_kv_ports().
  get_raiden_inline_load: get_raiden_inline_load().
  configure_raiden_telemetry: configure_raiden_telemetry().
  get_kv_ips: get_kv_ips().
  get_stage3_registration_wait_s: get_stage3_registration_wait_s().
  set_node_kv_ip_port: set_node_kv_ip_port().
  get_kv_transfer_port: get_kv_transfer_port().
  get_node_id: get_node_id().
  get_raiden_registry_ttl_s: get_raiden_registry_ttl_s().
  get_stage3_deferred_submit_enabled: get_stage3_deferred_submit_enabled().
  get_ipc_socket_path: get_ipc_socket_path().
  logger: logger.
  get_side_channel_port: get_side_channel_port().
  get_transfer_channel_number: get_transfer_channel_number().
  get_stage3_register_ahead_enabled: get_stage3_register_ahead_enabled().
  get_kv_shm_pool_gb: get_kv_shm_pool_gb().
  _get_kv_transfer_namespace: _get_kv_transfer_namespace().
  _NODES_KV_IP_PORT: _NODES_KV_IP_PORT.
  get_host_ip: get_host_ip().
  get_kv_coord_executor_max_workers: get_kv_coord_executor_max_workers().
  get_kv_channel_executor_max_workers: get_kv_channel_executor_max_workers().
  get_stage3_status_probe_s: get_stage3_status_probe_s().
  get_stage3_test_registration_delay_s: get_stage3_test_registration_delay_s().
  get_kv_stage_wait_timeout_secs: get_kv_stage_wait_timeout_secs().
  get_kv_stage_waiter_pool_size: get_kv_stage_waiter_pool_size().
  get_shm_name: get_shm_name().
  get_kv_warmup_enabled: get_kv_warmup_enabled().
  get_kv_latency_log_interval: get_kv_latency_log_interval().
  get_kv_pin_shm: get_kv_pin_shm().
  get_use_raiden_connector: get_use_raiden_connector().
  get_raiden_transfer_num_slots: get_raiden_transfer_num_slots().
  get_raiden_pool_staging_leases: get_raiden_pool_staging_leases().
  _RAIDEN_TELEMETRY_MODULE: _RAIDEN_TELEMETRY_MODULE.
  _RAIDEN_TELEMETRY_IMPORT_ATTEMPTED: _RAIDEN_TELEMETRY_IMPORT_ATTEMPTED.
  _RAIDEN_TELEMETRY_CONFIGURED: _RAIDEN_TELEMETRY_CONFIGURED.
  _RAIDEN_REGISTRY_TTL_MIN_DELTA_S: _RAIDEN_REGISTRY_TTL_MIN_DELTA_S.
---
# Module: [`src/vllm_torchtpu/distributed/utils.py`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/utils.py)

## Functions
- <a id="_get_kv_transfer_namespace"></a>`_get_kv_transfer_namespace()` — [`L193`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/utils.py#L193)
- <a id="configure_raiden_telemetry"></a>`configure_raiden_telemetry(backends: list[str] | set[str] | None = None)` — [`L313`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/utils.py#L313) — Configures TPU Raiden C++ telemetry backends if available.
- <a id="get_host_ip"></a>`get_host_ip()` — [`L46`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/utils.py#L46) — Use `VLLM_HOST_IP` if set, otherwise use default network interface IP.
- <a id="get_ipc_socket_path"></a>`get_ipc_socket_path(node_id: int, dp_rank: int = 0)` — [`L206`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/utils.py#L206) — Per-host intra-process IPC endpoint used between rank-0 coordinator
- <a id="get_kv_channel_executor_max_workers"></a>`get_kv_channel_executor_max_workers()` — [`L83`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/utils.py#L83) — Channel-level pull executor size.
- <a id="get_kv_coord_executor_max_workers"></a>`get_kv_coord_executor_max_workers()` — [`L74`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/utils.py#L74) — Request-level pull executor size.
- <a id="get_kv_ips"></a>`get_kv_ips()` — [`L31`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/utils.py#L31)
- <a id="get_kv_latency_log_interval"></a>`get_kv_latency_log_interval()` — [`L237`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/utils.py#L237) — How often (seconds) to log aggregated KV transfer latency stats.
- <a id="get_kv_pin_shm"></a>`get_kv_pin_shm()` — [`L243`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/utils.py#L243) — Whether to mlock(2) the KV shm pool at startup.
- <a id="get_kv_ports"></a>`get_kv_ports()` — [`L39`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/utils.py#L39)
- <a id="get_kv_shm_pool_gb"></a>`get_kv_shm_pool_gb()` — [`L183`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/utils.py#L183) — Total GB budget for the per-host shared-memory KV staging pool.
- <a id="get_kv_stage_wait_timeout_secs"></a>`get_kv_stage_wait_timeout_secs()` — [`L163`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/utils.py#L163) — Per-entry deadline for the async-D2H ``future.wait()`` in the stage
- <a id="get_kv_stage_waiter_pool_size"></a>`get_kv_stage_waiter_pool_size()` — [`L174`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/utils.py#L174) — Worker count for the stage waiter pool. 0 = auto (4).
- <a id="get_kv_transfer_port"></a>`get_kv_transfer_port()` — [`L51`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/utils.py#L51)
- <a id="get_kv_warmup_enabled"></a>`get_kv_warmup_enabled()` — [`L228`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/utils.py#L228) — Whether to pre-compile KV gather/scatter XLA executables at startup.
- <a id="get_node_id"></a>`get_node_id()` — [`L59`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/utils.py#L59)
- <a id="get_p2p_wait_pull_timeout"></a>`get_p2p_wait_pull_timeout()` — [`L92`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/utils.py#L92) — KV-cache transfer timeout in seconds.
- <a id="get_raiden_inline_load"></a>`get_raiden_inline_load()` — [`L287`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/utils.py#L287) — Load remote KV before the first forward instead of a no-forward step.
- <a id="get_raiden_pool_staging_leases"></a>`get_raiden_pool_staging_leases()` — [`L271`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/utils.py#L271) — Concurrent pool-reshard transfers to provision bounded host staging for.
- <a id="get_raiden_registry_ttl_s"></a>`get_raiden_registry_ttl_s()` — [`L102`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/utils.py#L102) — TTL, in seconds, for the raiden reshard store's request-block
- <a id="get_raiden_telemetry_module"></a>`get_raiden_telemetry_module()` — [`L297`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/utils.py#L297) — Gets and caches the TPU Raiden C++ extension module.
- <a id="get_raiden_transfer_num_slots"></a>`get_raiden_transfer_num_slots()` — [`L263`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/utils.py#L263) — Override for Raiden-owned per-rank host staging slots.
- <a id="get_shm_name"></a>`get_shm_name(node_id: int, dp_rank: int = 0)` — [`L217`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/utils.py#L217) — Name for the per-host SharedMemory block.
- <a id="get_side_channel_port"></a>`get_side_channel_port()` — [`L55`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/utils.py#L55)
- <a id="get_stage3_deferred_submit_enabled"></a>`get_stage3_deferred_submit_enabled()` — [`L130`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/utils.py#L130) — Per-step deferred re-attempt for Stage-3 loads whose producer
- <a id="get_stage3_register_ahead_enabled"></a>`get_stage3_register_ahead_enabled()` — [`L120`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/utils.py#L120) — Whether a PCP, TP or DP Stage-3 producer publishes a request's send
- <a id="get_stage3_registration_wait_s"></a>`get_stage3_registration_wait_s()` — [`L146`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/utils.py#L146) — Total budget for deferred Stage-3 submit re-attempts, bounded by the
- <a id="get_stage3_status_probe_s"></a>`get_stage3_status_probe_s()` — [`L110`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/utils.py#L110) — Interval, in seconds, at which a Stage-3 producer worker probes the
- <a id="get_stage3_test_registration_delay_s"></a>`get_stage3_test_registration_delay_s()` — [`L156`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/utils.py#L156) — TEST-ONLY fault injection: delay the producer's Stage-3 request-block
- <a id="get_transfer_channel_number"></a>`get_transfer_channel_number()` — [`L64`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/utils.py#L64) — Parallel TCP stream count for the coord-mode KV wire transfer.
- <a id="get_use_raiden_connector"></a>`get_use_raiden_connector()` — [`L253`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/utils.py#L253) — Whether TPUConnector should use the opt-in Raiden backend.
- <a id="set_node_kv_ip_port"></a>`set_node_kv_ip_port(ip_port: tuple[int, str, int])` — [`L25`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/utils.py#L25)

## Module values
- <a id="_NODES_KV_IP_PORT"></a>`_NODES_KV_IP_PORT` — [`L22`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/utils.py#L22)
- <a id="_RAIDEN_REGISTRY_TTL_MIN_DELTA_S"></a>`_RAIDEN_REGISTRY_TTL_MIN_DELTA_S` — [`L99`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/utils.py#L99)
- <a id="_RAIDEN_TELEMETRY_CONFIGURED"></a>`_RAIDEN_TELEMETRY_CONFIGURED` — [`L293`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/utils.py#L293)
- <a id="_RAIDEN_TELEMETRY_IMPORT_ATTEMPTED"></a>`_RAIDEN_TELEMETRY_IMPORT_ATTEMPTED` — [`L294`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/utils.py#L294)
- <a id="_RAIDEN_TELEMETRY_MODULE"></a>`_RAIDEN_TELEMETRY_MODULE` — [`L292`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/utils.py#L292)
- <a id="logger"></a>`logger` — [`L19`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/utils.py#L19)

