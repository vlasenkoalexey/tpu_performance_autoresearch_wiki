---
title: 'Module: src/vllm_torchtpu/distributed/kv_transfer/tpu_connector_stats.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/distributed/kv_transfer/tpu_connector_stats.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.distributed.kv_transfer.tpu_connector_stats`/
symbols:
  TpuKVConnectorPromMetrics.observe: TpuKVConnectorPromMetrics#observe().
  TpuKVConnectorStats.data: TpuKVConnectorStats#data.
  TpuKVConnectorPromMetrics._get_raiden_metric_definitions: TpuKVConnectorPromMetrics#_get_raiden_metric_definitions().
  TpuKVConnectorStats: TpuKVConnectorStats#
  TpuKVConnectorStats.clone_and_reset: TpuKVConnectorStats#clone_and_reset().
  TpuKVConnectorStats.num_successful_transfers: TpuKVConnectorStats#num_successful_transfers().
  TpuKVConnectorStats.__post_init__: TpuKVConnectorStats#__post_init__().
  TpuKVConnectorStats.reduce: TpuKVConnectorStats#reduce().
  TpuKVConnectorStats.record_prefill_queue_length: TpuKVConnectorStats#record_prefill_queue_length().
  TpuKVConnectorStats.record_decode_queue_length: TpuKVConnectorStats#record_decode_queue_length().
  TpuKVConnectorStats.is_empty: TpuKVConnectorStats#is_empty().
  logger: logger.
  TpuKVConnectorStats.record_d2h_transfer: TpuKVConnectorStats#record_d2h_transfer().
  TpuKVConnectorStats.record_h2d_transfer: TpuKVConnectorStats#record_h2d_transfer().
  TpuKVConnectorStats.record_kv_pull: TpuKVConnectorStats#record_kv_pull().
  TpuKVConnectorStats.record_mb_transferred: TpuKVConnectorStats#record_mb_transferred().
  TpuKVConnectorStats.record_failed_transfer: TpuKVConnectorStats#record_failed_transfer().
  TpuKVConnectorStats.record_runner_timings: TpuKVConnectorStats#record_runner_timings().
  TpuKVConnectorPromMetrics.runner_cpu_issue: TpuKVConnectorPromMetrics#runner_cpu_issue.
  TpuKVConnectorPromMetrics.runner_device_elapsed: TpuKVConnectorPromMetrics#runner_device_elapsed.
  TpuKVConnectorPromMetrics.dynamic_metrics: TpuKVConnectorPromMetrics#dynamic_metrics.
  TpuKVConnectorStats.aggregate: TpuKVConnectorStats#aggregate().
  METRIC_TYPE_HISTOGRAM: METRIC_TYPE_HISTOGRAM.
  METRIC_TYPE_COUNTER: METRIC_TYPE_COUNTER.
  METRIC_TYPE_GAUGE: METRIC_TYPE_GAUGE.
  RUNNER_TIMING_BUCKETS_SECONDS: RUNNER_TIMING_BUCKETS_SECONDS.
  TpuKVConnectorStats.reset: TpuKVConnectorStats#reset().
  TpuKVConnectorPromMetrics: TpuKVConnectorPromMetrics#
  DEFAULT_LABEL_VALUE: DEFAULT_LABEL_VALUE.
  TpuKVConnectorPromMetrics.tpu_histogram_d2h_transfer_time: TpuKVConnectorPromMetrics#tpu_histogram_d2h_transfer_time.
  TpuKVConnectorPromMetrics.tpu_histogram_h2d_transfer_time: TpuKVConnectorPromMetrics#tpu_histogram_h2d_transfer_time.
  TpuKVConnectorPromMetrics.tpu_histogram_kv_pull_time: TpuKVConnectorPromMetrics#tpu_histogram_kv_pull_time.
  TpuKVConnectorPromMetrics.tpu_histogram_kv_megabytes_transferred: TpuKVConnectorPromMetrics#tpu_histogram_kv_megabytes_transferred.
  TpuKVConnectorPromMetrics.counter_tpu_num_failed_transfers: TpuKVConnectorPromMetrics#counter_tpu_num_failed_transfers.
  TpuKVConnectorPromMetrics.gauge_tpu_prefill_queue_length: TpuKVConnectorPromMetrics#gauge_tpu_prefill_queue_length.
  TpuKVConnectorPromMetrics.gauge_tpu_decode_queue_length: TpuKVConnectorPromMetrics#gauge_tpu_decode_queue_length.
  TpuKVConnectorPromMetrics.__init__: TpuKVConnectorPromMetrics#__init__().
---
# Module: [`src/vllm_torchtpu/distributed/kv_transfer/tpu_connector_stats.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector_stats.py)

## Classes
### <a id="TpuKVConnectorPromMetrics"></a>`TpuKVConnectorPromMetrics`
- def: [`src/vllm_torchtpu/distributed/kv_transfer/tpu_connector_stats.py:207`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector_stats.py#L207)
- signature: `class TpuKVConnectorPromMetrics(KVConnectorPromMetrics):`
- members:
  - <a id="TpuKVConnectorPromMetrics.observe"></a>`observe(self, transfer_stats_data: dict[str, Any], engine_idx: int = 0)` — [`L393`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector_stats.py#L393)
  - <a id="TpuKVConnectorPromMetrics.counter_tpu_num_failed_transfers"></a>`counter_tpu_num_failed_transfers` — [`L303`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector_stats.py#L303)
  - <a id="TpuKVConnectorPromMetrics.dynamic_metrics"></a>`dynamic_metrics` — [`L325`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector_stats.py#L325)
  - <a id="TpuKVConnectorPromMetrics.gauge_tpu_decode_queue_length"></a>`gauge_tpu_decode_queue_length` — [`L321`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector_stats.py#L321)
  - <a id="TpuKVConnectorPromMetrics.gauge_tpu_prefill_queue_length"></a>`gauge_tpu_prefill_queue_length` — [`L312`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector_stats.py#L312)
  - <a id="TpuKVConnectorPromMetrics.runner_cpu_issue"></a>`runner_cpu_issue` — [`L284`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector_stats.py#L284)
  - <a id="TpuKVConnectorPromMetrics.runner_device_elapsed"></a>`runner_device_elapsed` — [`L292`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector_stats.py#L292)
  - <a id="TpuKVConnectorPromMetrics.tpu_histogram_d2h_transfer_time"></a>`tpu_histogram_d2h_transfer_time` — [`L240`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector_stats.py#L240)
  - <a id="TpuKVConnectorPromMetrics.tpu_histogram_h2d_transfer_time"></a>`tpu_histogram_h2d_transfer_time` — [`L250`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector_stats.py#L250)
  - <a id="TpuKVConnectorPromMetrics.tpu_histogram_kv_megabytes_transferred"></a>`tpu_histogram_kv_megabytes_transferred` — [`L280`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector_stats.py#L280)
  - <a id="TpuKVConnectorPromMetrics.tpu_histogram_kv_pull_time"></a>`tpu_histogram_kv_pull_time` — [`L259`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector_stats.py#L259)
- protocol/private: <a id="TpuKVConnectorPromMetrics.__init__"></a>`__init__`[`L208`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector_stats.py#L208), <a id="TpuKVConnectorPromMetrics._get_raiden_metric_definitions"></a>`_get_raiden_metric_definitions`[`L329`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector_stats.py#L329)
- uses (calls/refs, reference-scoped): [`parse_raiden_metric_key`](raiden/telemetry_utils.md#parse_raiden_metric_key), [`get_raiden_telemetry_module`](../utils.md#get_raiden_telemetry_module), [`configure_raiden_telemetry`](../utils.md#configure_raiden_telemetry), [`normalize_raiden_metric_name`](raiden/telemetry_utils.md#normalize_raiden_metric_name), [`logger`](tpu_connector_stats.md#logger), [`METRIC_TYPE_COUNTER`](tpu_connector_stats.md#METRIC_TYPE_COUNTER), [`METRIC_TYPE_GAUGE`](tpu_connector_stats.md#METRIC_TYPE_GAUGE), [`METRIC_TYPE_HISTOGRAM`](tpu_connector_stats.md#METRIC_TYPE_HISTOGRAM), [`RUNNER_TIMING_BUCKETS_SECONDS`](tpu_connector_stats.md#RUNNER_TIMING_BUCKETS_SECONDS), [`DEFAULT_LABEL_VALUE`](tpu_connector_stats.md#DEFAULT_LABEL_VALUE)
- used by: [`build_prom_metrics`](tpu_connector.md#TPUConnector.build_prom_metrics)

### <a id="TpuKVConnectorStats"></a>`TpuKVConnectorStats`
- def: [`src/vllm_torchtpu/distributed/kv_transfer/tpu_connector_stats.py:71`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector_stats.py#L71) — documented in [kv-transfer-and-disaggregated-serving](../../../../../concepts/kv-transfer-and-disaggregated-serving.md)
- doc: Container for transfer performance metrics
- signature: `class TpuKVConnectorStats(KVConnectorStats):`
- members:
  - <a id="TpuKVConnectorStats.aggregate"></a>`aggregate(self, other: KVConnectorStats)` — [`L134`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector_stats.py#L134)
  - <a id="TpuKVConnectorStats.clone_and_reset"></a>`clone_and_reset(self)` — [`L129`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector_stats.py#L129)
  - <a id="TpuKVConnectorStats.is_empty"></a>`is_empty(self)` — [`L197`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector_stats.py#L197)
  - <a id="TpuKVConnectorStats.num_successful_transfers"></a>`num_successful_transfers(self)` — [`L203`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector_stats.py#L203)
  - <a id="TpuKVConnectorStats.record_d2h_transfer"></a>`record_d2h_transfer(self, d2h_transfer_time)` — [`L79`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector_stats.py#L79) — Record a D2H transfer operation.
  - <a id="TpuKVConnectorStats.record_decode_queue_length"></a>`record_decode_queue_length(self, decode_queue_length: int)` — [`L103`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector_stats.py#L103) — Record the decode (load) queue length.
  - <a id="TpuKVConnectorStats.record_failed_transfer"></a>`record_failed_transfer(self)` — [`L95`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector_stats.py#L95) — Record a failed KV transfer operation.
  - <a id="TpuKVConnectorStats.record_h2d_transfer"></a>`record_h2d_transfer(self, h2d_transfer_time)` — [`L83`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector_stats.py#L83) — Record a H2D transfer operation.
  - <a id="TpuKVConnectorStats.record_kv_pull"></a>`record_kv_pull(self, kv_pull_time)` — [`L87`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector_stats.py#L87) — Record a KV pull operation.
  - <a id="TpuKVConnectorStats.record_mb_transferred"></a>`record_mb_transferred(self, mb_transferred)` — [`L91`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector_stats.py#L91) — Record a successful KV transfer operation.
  - <a id="TpuKVConnectorStats.record_prefill_queue_length"></a>`record_prefill_queue_length(self, prefill_queue_length: int)` — [`L99`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector_stats.py#L99) — Record the prefill (send) queue length.
  - <a id="TpuKVConnectorStats.record_runner_timings"></a>`record_runner_timings(self, cpu_samples: list[tuple[str, str, float]], device_samples: list[tuple[str, str, float]])` — [`L107`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector_stats.py#L107)
  - <a id="TpuKVConnectorStats.reduce"></a>`reduce(self)` — [`L144`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector_stats.py#L144)
  - <a id="TpuKVConnectorStats.reset"></a>`reset(self)` — [`L115`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector_stats.py#L115)
  - <a id="TpuKVConnectorStats.data"></a>`data` — [`L117`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector_stats.py#L117)
- protocol/private: <a id="TpuKVConnectorStats.__post_init__"></a>`__post_init__`[`L74`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector_stats.py#L74)
- used by: [`_coord_rank0_pull`](zmq_shm_base.md#ZmqShmKvConnectorBase._coord_rank0_pull), [`_coord_scatter_shard`](zmq_shm_base.md#ZmqShmKvConnectorBase._coord_scatter_shard), [`_coord_rank0_build_pull_response`](zmq_shm_base.md#ZmqShmKvConnectorBase._coord_rank0_build_pull_response), [`_coord_stage_wait_worker`](zmq_shm_base.md#ZmqShmKvConnectorBase._coord_stage_wait_worker), [`transfer_stats`](zmq_shm_base.md#ZmqShmKvConnectorBase.transfer_stats), [`get_kv_connector_stats`](tpu_connector.md#TPURaidenConnectorWorker.get_kv_connector_stats), [`transfer_stats`](tpu_connector.md#TPURaidenConnectorWorker.transfer_stats), [`get_kv_connector_stats`](zmq_shm_base.md#ZmqShmKvConnectorBase.get_kv_connector_stats), [`get_finished_kv_transfers`](../../runner/tpu_runner.md#TPUModelRunner.get_finished_kv_transfers), [`_get_raiden_stats`](tpu_connector.md#TPURaidenConnectorWorker._get_raiden_stats), [`build_kv_connector_stats`](tpu_connector.md#TPUConnector.build_kv_connector_stats)

## Module values
- <a id="DEFAULT_LABEL_VALUE"></a>`DEFAULT_LABEL_VALUE` — [`L46`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector_stats.py#L46)
- <a id="METRIC_TYPE_COUNTER"></a>`METRIC_TYPE_COUNTER` — [`L42`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector_stats.py#L42)
- <a id="METRIC_TYPE_GAUGE"></a>`METRIC_TYPE_GAUGE` — [`L43`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector_stats.py#L43)
- <a id="METRIC_TYPE_HISTOGRAM"></a>`METRIC_TYPE_HISTOGRAM` — [`L41`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector_stats.py#L41)
- <a id="RUNNER_TIMING_BUCKETS_SECONDS"></a>`RUNNER_TIMING_BUCKETS_SECONDS` — [`L47`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector_stats.py#L47)
- <a id="logger"></a>`logger` — [`L38`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector_stats.py#L38)

