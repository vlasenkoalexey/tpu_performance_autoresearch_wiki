---
title: 'Module: src/vllm_torchtpu/distributed/pp_wave.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/distributed/pp_wave.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.distributed.pp_wave`/
symbols:
  PPWave.settle: PPWave#settle().
  PPWave._async_loop: PPWave#_async_loop().
  PPWave.end_forward: PPWave#end_forward().
  PPWave.pending: PPWave#pending.
  PPWave._issue_queued: PPWave#_issue_queued().
  PPWave._launch_async: PPWave#_launch_async().
  PPWave.start_forward: PPWave#start_forward().
  PPWave.push: PPWave#push().
  PPWave.rank: PPWave#rank.
  PPWave.warmup: PPWave#warmup().
  PPWave._open_burst: PPWave#_open_burst().
  PPWave._launch: PPWave#_launch().
  PPWave._async_cv: PPWave#_async_cv.
  RESIDUAL: RESIDUAL.
  PPWave.zeros: PPWave#zeros.
  PPWave._launch_blocking: PPWave#_launch_blocking().
  HIDDEN_STATES: HIDDEN_STATES.
  PPWave._check_count: PPWave#_check_count().
  stage_chips: stage_chips().
  PPWave._async_idle: PPWave#_async_idle().
  PPWave.columns: PPWave#columns.
  PPWave.op: PPWave#op.
  PPWave.async_handoff: PPWave#async_handoff.
  PPWave.carried: PPWave#carried.
  PPWave.burst_launches: PPWave#burst_launches.
  PPWave.step: PPWave#step().
  PPWave._async_drained: PPWave#_async_drained.
  PPWave.forwards: PPWave#forwards.
  logger: logger.
  PPWave.last: PPWave#last.
  PPWave.drain_before_handoff: PPWave#drain_before_handoff.
  PPWave._async_queued: PPWave#_async_queued.
  PPWave._pad: PPWave#_pad().
  PPWave.__init__: PPWave#__init__().
  PPWave.size: PPWave#size.
  PPWave._async_issuing: PPWave#_async_issuing.
  PPWave._async_error: PPWave#_async_error.
  PPWave.burst_open: PPWave#burst_open.
  PPWave.column: PPWave#column.
  _flush: _flush().
  _fence: _fence().
  PPWave._async_busy: PPWave#_async_busy.
  PPWave.launches: PPWave#launches.
  PPWave.bursts: PPWave#bursts.
  PPWave.zero: PPWave#zero.
  _launch_now: _launch_now().
  PPWave: PPWave#
  PPWave.max_rows: PPWave#max_rows.
  PPWave._in_step: PPWave#_in_step.
  PPWave._async_thread: PPWave#_async_thread.
  pp_rank_flags: pp_rank_flags().
  _drain_slice: _drain_slice().
---
# Module: [`src/vllm_torchtpu/distributed/pp_wave.py`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_wave.py)

## Classes
### <a id="PPWave"></a>`PPWave`
- def: [`src/vllm_torchtpu/distributed/pp_wave.py:204`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_wave.py#L204) — documented in [distributed-parallelism-and-meshes](../../../../concepts/distributed-parallelism-and-meshes.md)
- signature: `class PPWave:`
- members:
  - <a id="PPWave._issue_queued"></a>`_issue_queued(self)` — [`L393`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_wave.py#L393) — Waits for any queued drain, issues the hand-off if the helper has not,
  - <a id="PPWave._launch_async"></a>`_launch_async(self, carried: tuple[torch.Tensor, ...])` — [`L324`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_wave.py#L324) — Flushes the outgoing tensors and queues the drain on the helper
  - <a id="PPWave._open_burst"></a>`_open_burst(self)` — [`L441`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_wave.py#L441) — Stage r's launch before its forward m is number m+r and stage 0's — documented in [tracing-annotations](../../../../concepts/tracing-annotations.md)
  - <a id="PPWave.end_forward"></a>`end_forward(self, tensors: dict[str, torch.Tensor] | None, rows: int)` — [`L479`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_wave.py#L479) — Called after the forward with its outgoing activations (None on
  - <a id="PPWave.push"></a>`push(self)` — [`L505`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_wave.py#L505) — A forward that carries nothing: the one launch this stage issues — documented in [tracing-annotations](../../../../concepts/tracing-annotations.md)
  - <a id="PPWave.settle"></a>`settle(self)` — [`L522`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_wave.py#L522) — Bring every stage to the same launch count and close the burst; — documented in [tracing-annotations](../../../../concepts/tracing-annotations.md)
  - <a id="PPWave.start_forward"></a>`start_forward(self, rows: int)` — [`L463`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_wave.py#L463) — Called before forward number m of the burst with its padded token
  - <a id="PPWave.step"></a>`step(self)` — [`L311`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_wave.py#L311) — Marks a worker-thread region that traces device ops; the helper
  - <a id="PPWave.warmup"></a>`warmup(self)` — [`L421`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_wave.py#L421) — One launch outside any burst on every device, carrying a value
  - <a id="PPWave.async_handoff"></a>`async_handoff` — [`L243`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_wave.py#L243)
  - <a id="PPWave.burst_launches"></a>`burst_launches` — [`L271`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_wave.py#L271)
  - <a id="PPWave.burst_open"></a>`burst_open` — [`L270`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_wave.py#L270)
  - <a id="PPWave.bursts"></a>`bursts` — [`L269`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_wave.py#L269)
  - <a id="PPWave.carried"></a>`carried` — [`L238`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_wave.py#L238)
  - <a id="PPWave.column"></a>`column` — [`L221`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_wave.py#L221)
  - <a id="PPWave.columns"></a>`columns` — [`L222`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_wave.py#L222)
  - <a id="PPWave.drain_before_handoff"></a>`drain_before_handoff` — [`L242`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_wave.py#L242)
  - <a id="PPWave.forwards"></a>`forwards` — [`L272`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_wave.py#L272)
  - <a id="PPWave.last"></a>`last` — [`L218`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_wave.py#L218)
  - <a id="PPWave.launches"></a>`launches` — [`L268`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_wave.py#L268)
  - <a id="PPWave.max_rows"></a>`max_rows` — [`L239`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_wave.py#L239)
  - <a id="PPWave.op"></a>`op` — [`L240`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_wave.py#L240)
  - <a id="PPWave.pending"></a>`pending` — [`L273`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_wave.py#L273)
  - <a id="PPWave.rank"></a>`rank` — [`L216`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_wave.py#L216)
  - <a id="PPWave.size"></a>`size` — [`L217`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_wave.py#L217)
  - <a id="PPWave.zero"></a>`zero` — [`L267`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_wave.py#L267)
  - <a id="PPWave.zeros"></a>`zeros` — [`L259`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_wave.py#L259)
- protocol/private: <a id="PPWave.__init__"></a>`__init__`[`L205`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_wave.py#L205), <a id="PPWave._async_busy"></a>`_async_busy`[`L253`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_wave.py#L253), <a id="PPWave._async_cv"></a>`_async_cv`[`L249`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_wave.py#L249), <a id="PPWave._async_drained"></a>`_async_drained`[`L254`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_wave.py#L254), <a id="PPWave._async_error"></a>`_async_error`[`L256`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_wave.py#L256), <a id="PPWave._async_idle"></a>`_async_idle`[`L302`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_wave.py#L302), <a id="PPWave._async_issuing"></a>`_async_issuing`[`L255`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_wave.py#L255), <a id="PPWave._async_loop"></a>`_async_loop`[`L341`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_wave.py#L341), <a id="PPWave._async_queued"></a>`_async_queued`[`L250`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_wave.py#L250), <a id="PPWave._async_thread"></a>`_async_thread`[`L258`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_wave.py#L258), <a id="PPWave._check_count"></a>`_check_count`[`L455`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_wave.py#L455), <a id="PPWave._in_step"></a>`_in_step`[`L257`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_wave.py#L257), <a id="PPWave._launch"></a>`_launch`[`L295`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_wave.py#L295), <a id="PPWave._launch_blocking"></a>`_launch_blocking`[`L287`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_wave.py#L287), <a id="PPWave._pad"></a>`_pad`[`L414`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_wave.py#L414)
- uses (calls/refs, reference-scoped): [`TraceAnnotation`](../tracing/annotation.md#TraceAnnotation), [`get_or_create_pp_mesh`](pp_shift.md#get_or_create_pp_mesh), [`get_pcp_rank`](pcp.md#get_pcp_rank), [`get_pcp_world_size`](pcp.md#get_pcp_world_size), [`RESIDUAL`](pp_wave.md#RESIDUAL), [`HIDDEN_STATES`](pp_wave.md#HIDDEN_STATES), [`pp_permute_op`](pp_shift.md#pp_permute_op), [`stage_chips`](pp_wave.md#stage_chips), [`logger`](pp_wave.md#logger), [`_fence`](pp_wave.md#_fence), [`_flush`](pp_wave.md#_flush), [`_launch_now`](pp_wave.md#_launch_now), [`_drain_slice`](pp_wave.md#_drain_slice)
- used by: [`_dummy_run`](../runner/tpu_runner.md#TPUModelRunner._dummy_run), [`capture_model`](../runner/tpu_runner.md#TPUModelRunner.capture_model), [`_pp_wave`](../runner/tpu_runner.md#TPUModelRunner._pp_wave), [`_warmup_handoff_forwards`](../runner/tpu_runner.md#TPUModelRunner._warmup_handoff_forwards), [`_warmup_mtp_prefill`](../runner/tpu_runner.md#TPUModelRunner._warmup_mtp_prefill), [`pp_push`](../runner/tpu_runner.md#TPUModelRunner.pp_push), [`pp_settle`](../runner/tpu_runner.md#TPUModelRunner.pp_settle)

## Functions
- <a id="_drain_slice"></a>`_drain_slice(fence: TpuEvent | None = None)` — [`L158`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_wave.py#L158) — Waits for local device work (or the given fence) to complete, then joins
- <a id="_fence"></a>`_fence()` — [`L195`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_wave.py#L195) — Records a device event for all work submitted so far.
- <a id="_flush"></a>`_flush(tensors: tuple[torch.Tensor, ...])` — [`L188`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_wave.py#L188) — Submits the pending ops producing ``tensors`` without blocking.
- <a id="_launch_now"></a>`_launch_now(op, carried: tuple[torch.Tensor, ...])` — [`L172`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_wave.py#L172) — Run one hand-off as its own device program, submitted immediately.
- <a id="pp_rank_flags"></a>`pp_rank_flags(parallel_config: Any)` — [`L136`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_wave.py#L136) — (is_first_stage, is_last_stage) for this worker.
- <a id="stage_chips"></a>`stage_chips()` — [`L146`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_wave.py#L146) — How many chips this worker's pipeline stage spans.

## Module values
- <a id="HIDDEN_STATES"></a>`HIDDEN_STATES` — [`L132`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_wave.py#L132)
- <a id="RESIDUAL"></a>`RESIDUAL` — [`L133`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_wave.py#L133)
- <a id="logger"></a>`logger` — [`L129`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_wave.py#L129)

