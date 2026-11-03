---
title: 'Module: src/vllm_torchtpu/tracing/annotation.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/tracing/annotation.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.tracing.annotation`/
symbols:
  TraceAnnotation: TraceAnnotation#
  TraceAnnotation.__enter__: TraceAnnotation#__enter__().
  TraceAnnotation._rf: TraceAnnotation#_rf.
  TraceAnnotation.is_enabled: TraceAnnotation#is_enabled().
  TraceAnnotation.__exit__: TraceAnnotation#__exit__().
  is_trace_annotation_enabled: is_trace_annotation_enabled().
  TraceAnnotation.kwargs: TraceAnnotation#kwargs.
  TraceAnnotation.name: TraceAnnotation#name.
  TraceAnnotation.__init__: TraceAnnotation#__init__().
---
# Module: [`src/vllm_torchtpu/tracing/annotation.py`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/tracing/annotation.py)

## Classes
### <a id="TraceAnnotation"></a>`TraceAnnotation`  ·  implements/extends ContextDecorator
- def: [`src/vllm_torchtpu/tracing/annotation.py:27`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/tracing/annotation.py#L27) — documented in [tracing-annotations](../../../../concepts/tracing-annotations.md)
- signature: `class TraceAnnotation(contextlib.ContextDecorator):`
- members:
  - <a id="TraceAnnotation.is_enabled"></a>`is_enabled(cls)` — [`L34`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/tracing/annotation.py#L34) — documented in [tracing-annotations](../../../../concepts/tracing-annotations.md)
  - <a id="TraceAnnotation.kwargs"></a>`kwargs` — [`L30`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/tracing/annotation.py#L30) — documented in [tracing-annotations](../../../../concepts/tracing-annotations.md)
  - <a id="TraceAnnotation.name"></a>`name` — [`L29`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/tracing/annotation.py#L29) — documented in [tracing-annotations](../../../../concepts/tracing-annotations.md)
- protocol/private: <a id="TraceAnnotation.__enter__"></a>`__enter__`[`L37`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/tracing/annotation.py#L37), <a id="TraceAnnotation.__exit__"></a>`__exit__`[`L47`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/tracing/annotation.py#L47), <a id="TraceAnnotation.__init__"></a>`__init__`[`L28`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/tracing/annotation.py#L28), <a id="TraceAnnotation._rf"></a>`_rf`[`L31`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/tracing/annotation.py#L31)
- uses (calls/refs, reference-scoped): [`is_trace_annotation_enabled`](annotation.md#is_trace_annotation_enabled)
- used by: [`execute_model`](../runner/tpu_runner.md#TPUModelRunner.execute_model), [`_submit_stage3_loads`](../distributed/kv_transfer/tpu_connector.md#TPURaidenConnectorWorker._submit_stage3_loads), [`_register_stage3_request_blocks`](../distributed/kv_transfer/tpu_connector.md#TPURaidenConnectorWorker._register_stage3_request_blocks), [`_poll_finished`](../distributed/kv_transfer/tpu_connector.md#TPURaidenConnectorWorker._poll_finished), [`_register_stage3_request_row_spans`](../distributed/kv_transfer/tpu_connector.md#TPURaidenConnectorWorker._register_stage3_request_row_spans), [`start_forward`](../distributed/pp_ring.md#PPRing.start_forward), [`settle`](../distributed/pp_wave.md#PPWave.settle), [`_async_loop`](../distributed/pp_wave.md#PPWave._async_loop), [`_issue_queued`](../distributed/pp_wave.md#PPWave._issue_queued), [`_post_loop`](../distributed/pp_ring.md#PPRing._post_loop), [`push`](../distributed/pp_wave.md#PPWave.push), [`_open_burst`](../distributed/pp_wave.md#PPWave._open_burst), [`_queue_send`](../distributed/pp_ring.md#PPRing._queue_send), [`_launch_blocking`](../distributed/pp_wave.md#PPWave._launch_blocking), [`_send`](../distributed/pp_ring.md#PPRing._send), [`mask_spec_logits`](../structured_decoding/structured_decoding_manager.md#StructuredDecodingManager.mask_spec_logits), [`_wait_posted`](../distributed/pp_ring.md#PPRing._wait_posted), [`mask_logits`](../structured_decoding/structured_decoding_manager.md#StructuredDecodingManager.mask_logits)

## Functions
- <a id="is_trace_annotation_enabled"></a>`is_trace_annotation_enabled()` — [`L22`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/tracing/annotation.py#L22) — Checks whether PyTorch Kineto profiler session is active. — documented in [tracing-annotations](../../../../concepts/tracing-annotations.md)

