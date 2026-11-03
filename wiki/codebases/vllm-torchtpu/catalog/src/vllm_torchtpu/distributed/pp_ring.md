---
title: 'Module: src/vllm_torchtpu/distributed/pp_ring.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/distributed/pp_ring.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.distributed.pp_ring`/
symbols:
  PPRing.start_forward: PPRing#start_forward().
  PPRing.warmup: PPRing#warmup().
  PPRing._zero_residuals: PPRing#_zero_residuals.
  PPRing.end_forward: PPRing#end_forward().
  PPRing.begin_step: PPRing#begin_step().
  PPRing._post_loop: PPRing#_post_loop().
  PPRing._send_loop: PPRing#_send_loop().
  PPRing._post: PPRing#_post().
  PPRing.rank: PPRing#rank.
  PPRing._cv: PPRing#_cv.
  PPRing._queue_send: PPRing#_queue_send().
  PPRing.close: PPRing#close().
  PPRing.columns: PPRing#columns.
  PPRing._send: PPRing#_send().
  PPRing.carried: PPRing#carried.
  PPRing._has_room: PPRing#_has_room().
  PPRing._raise_post_failure: PPRing#_raise_post_failure().
  PPRing.transfers: PPRing#transfers.
  PPRing._to_post: PPRing#_to_post.
  PPRing._raise_send_failure: PPRing#_raise_send_failure().
  hbm_reserve_bytes: hbm_reserve_bytes().
  PPRing.next: PPRing#next.
  PPRing._sends: PPRing#_sends.
  PPRing._post_stops: PPRing#_post_stops().
  PPRing.prev: PPRing#prev.
  PPRing._wait_posted: PPRing#_wait_posted().
  check_ring_receives: check_ring_receives().
  PPRing._tag: PPRing#_tag().
  PPRing._raise_send_failure_locked: PPRing#_raise_send_failure_locked().
  PPRing._error: PPRing#_error.
  PPRing._check_rows: PPRing#_check_rows().
  PPRing._posted: PPRing#_posted.
  logger: logger.
  PPRing.__init__: PPRing#__init__().
  PPRing.template: PPRing#template.
  PPRing._thread: PPRing#_thread.
  PPRing._post_thread: PPRing#_post_thread.
  PPRing.last: PPRing#last.
  PPRing.global_rank: PPRing#global_rank.
  PPRing: PPRing#
  PPRing.posted_through: PPRing#posted_through.
  PPRing._current: PPRing#_current.
  PPRing._closing: PPRing#_closing.
  ring_receives_posted: ring_receives_posted().
  PPRing.column: PPRing#column.
  _MAX_RECEIVES: _MAX_RECEIVES.
  hbm_reserve_bytes.row_bytes: hbm_reserve_bytes().row_bytes().
  PPRing.size: PPRing#size.
  PPRing.device: PPRing#device.
  PPRing.depth: PPRing#depth.
  PPRing.landed_through: PPRing#landed_through.
  PPRing._post_error: PPRing#_post_error.
  _LIBTPU_REQUIREMENT: _LIBTPU_REQUIREMENT.
  PPRing.max_rows: PPRing#max_rows.
  _TAG_SPAN: _TAG_SPAN.
  _first_and_last: _first_and_last().
  PPRing.forwards: PPRing#forwards.
  PPRing.sent: PPRing#sent.
  PPRing.drain_before_handoff: PPRing#drain_before_handoff.
  PPRing.step: PPRing#step().
  PPRing.push: PPRing#push().
  PPRing.settle: PPRing#settle().
---
# Module: [`src/vllm_torchtpu/distributed/pp_ring.py`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_ring.py)

## Classes
### <a id="PPRing"></a>`PPRing`
- def: [`src/vllm_torchtpu/distributed/pp_ring.py:188`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_ring.py#L188) — documented in [distributed-parallelism-and-meshes](../../../../concepts/distributed-parallelism-and-meshes.md)
- signature: `class PPRing:`
- members:
  - <a id="PPRing._has_room"></a>`_has_room(self, transfer: int)` — [`L433`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_ring.py#L433) — Whether posting ``transfer`` keeps at most _MAX_RECEIVES receive
  - <a id="PPRing._post"></a>`_post(self, transfer: int, rows: int)` — [`L297`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_ring.py#L297) — Posts the receives of one transfer of ``rows`` rows and returns
  - <a id="PPRing._post_stops"></a>`_post_stops(self)` — [`L440`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_ring.py#L440) — Whether the posting thread stops: the ring closes, or its send
  - <a id="PPRing._send"></a>`_send(self, transfer: int, outgoing: tuple[torch.Tensor, ...], fence: TpuEvent)` — [`L592`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_ring.py#L592) — Sends one transfer once its tensors are computed and returns when — documented in [tracing-annotations](../../../../concepts/tracing-annotations.md)
  - <a id="PPRing._wait_posted"></a>`_wait_posted(self, landing: Future[tuple[torch.Tensor, ...]])` — [`L481`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_ring.py#L481) — Waits until the posting thread has posted a transfer's receives
  - <a id="PPRing.begin_step"></a>`begin_step(self, rows_per_forward: list[int])` — [`L403`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_ring.py#L403) — Called before the first forward of a scheduler step with the
  - <a id="PPRing.close"></a>`close(self)` — [`L653`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_ring.py#L653) — Drops the receives still queued, whose forwards will not run,
  - <a id="PPRing.end_forward"></a>`end_forward(self, tensors: dict[str, torch.Tensor] | None, rows: int)` — [`L538`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_ring.py#L538) — Called after the forward with its outgoing activations (None on
  - <a id="PPRing.push"></a>`push(self)` — [`L646`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_ring.py#L646) — Does nothing: every forward moves on as soon as it is done, and
  - <a id="PPRing.settle"></a>`settle(self)` — [`L650`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_ring.py#L650) — Does nothing: no stage holds launches for the others to match.
  - <a id="PPRing.start_forward"></a>`start_forward(self, rows: int)` — [`L495`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_ring.py#L495) — Called before each forward with its padded token count. Returns — documented in [tracing-annotations](../../../../concepts/tracing-annotations.md)
  - <a id="PPRing.step"></a>`step(self)` — [`L344`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_ring.py#L344) — Marks a runner call that traces device ops. The helper threads
  - <a id="PPRing.warmup"></a>`warmup(self)` — [`L349`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_ring.py#L349) — One small transfer of every carried tensor from each device to
  - <a id="PPRing.carried"></a>`carried` — [`L234`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_ring.py#L234)
  - <a id="PPRing.column"></a>`column` — [`L214`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_ring.py#L214)
  - <a id="PPRing.columns"></a>`columns` — [`L215`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_ring.py#L215)
  - <a id="PPRing.depth"></a>`depth` — [`L238`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_ring.py#L238)
  - <a id="PPRing.device"></a>`device` — [`L236`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_ring.py#L236)
  - <a id="PPRing.drain_before_handoff"></a>`drain_before_handoff` — [`L191`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_ring.py#L191)
  - <a id="PPRing.forwards"></a>`forwards` — [`L246`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_ring.py#L246)
  - <a id="PPRing.global_rank"></a>`global_rank` — [`L211`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_ring.py#L211)
  - <a id="PPRing.landed_through"></a>`landed_through` — [`L245`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_ring.py#L245)
  - <a id="PPRing.last"></a>`last` — [`L207`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_ring.py#L207)
  - <a id="PPRing.max_rows"></a>`max_rows` — [`L237`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_ring.py#L237)
  - <a id="PPRing.next"></a>`next` — [`L213`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_ring.py#L213)
  - <a id="PPRing.posted_through"></a>`posted_through` — [`L242`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_ring.py#L242)
  - <a id="PPRing.prev"></a>`prev` — [`L212`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_ring.py#L212)
  - <a id="PPRing.rank"></a>`rank` — [`L205`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_ring.py#L205)
  - <a id="PPRing.sent"></a>`sent` — [`L247`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_ring.py#L247)
  - <a id="PPRing.size"></a>`size` — [`L206`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_ring.py#L206)
  - <a id="PPRing.template"></a>`template` — [`L235`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_ring.py#L235)
  - <a id="PPRing.transfers"></a>`transfers` — [`L240`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_ring.py#L240)
- protocol/private: <a id="PPRing.__init__"></a>`__init__`[`L193`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_ring.py#L193), <a id="PPRing._check_rows"></a>`_check_rows`[`L319`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_ring.py#L319), <a id="PPRing._closing"></a>`_closing`[`L257`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_ring.py#L257), <a id="PPRing._current"></a>`_current`[`L252`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_ring.py#L252), <a id="PPRing._cv"></a>`_cv`[`L255`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_ring.py#L255), <a id="PPRing._error"></a>`_error`[`L258`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_ring.py#L258), <a id="PPRing._post_error"></a>`_post_error`[`L265`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_ring.py#L265), <a id="PPRing._post_loop"></a>`_post_loop`[`L445`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_ring.py#L445), <a id="PPRing._post_thread"></a>`_post_thread`[`L266`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_ring.py#L266), <a id="PPRing._posted"></a>`_posted`[`L250`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_ring.py#L250), <a id="PPRing._queue_send"></a>`_queue_send`[`L573`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_ring.py#L573), <a id="PPRing._raise_post_failure"></a>`_raise_post_failure`[`L336`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_ring.py#L336), <a id="PPRing._raise_send_failure"></a>`_raise_send_failure`[`L326`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_ring.py#L326), <a id="PPRing._raise_send_failure_locked"></a>`_raise_send_failure_locked`[`L330`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_ring.py#L330), <a id="PPRing._send_loop"></a>`_send_loop`[`L613`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_ring.py#L613), <a id="PPRing._sends"></a>`_sends`[`L256`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_ring.py#L256), <a id="PPRing._tag"></a>`_tag`[`L294`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_ring.py#L294), <a id="PPRing._thread"></a>`_thread`[`L259`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_ring.py#L259), <a id="PPRing._to_post"></a>`_to_post`[`L262`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_ring.py#L262), <a id="PPRing._zero_residuals"></a>`_zero_residuals`[`L276`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_ring.py#L276)
- uses (calls/refs, reference-scoped): [`TraceAnnotation`](../tracing/annotation.md#TraceAnnotation), [`get_pcp_rank`](pcp.md#get_pcp_rank), [`get_pcp_world_size`](pcp.md#get_pcp_world_size), [`RESIDUAL`](pp_wave.md#RESIDUAL), [`HIDDEN_STATES`](pp_wave.md#HIDDEN_STATES), [`check_ring_receives`](pp_ring.md#check_ring_receives), [`logger`](pp_ring.md#logger), [`_fence`](pp_wave.md#_fence), [`_flush`](pp_wave.md#_flush), [`_MAX_RECEIVES`](pp_ring.md#_MAX_RECEIVES), [`_LIBTPU_REQUIREMENT`](pp_ring.md#_LIBTPU_REQUIREMENT), [`_TAG_SPAN`](pp_ring.md#_TAG_SPAN), [`_first_and_last`](pp_ring.md#_first_and_last)
- used by: [`execute_model`](../runner/tpu_runner.md#TPUModelRunner.execute_model), [`capture_model`](../runner/tpu_runner.md#TPUModelRunner.capture_model), [`_pp_wave`](../runner/tpu_runner.md#TPUModelRunner._pp_wave)

## Functions
- <a id="_first_and_last"></a>`_first_and_last(x: torch.Tensor)` — [`L182`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_ring.py#L182) — Reads a received tensor's first and last element on the host; the
- <a id="check_ring_receives"></a>`check_ring_receives(stages: int, depth: int, carried: int = 1)` — [`L141`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_ring.py#L141) — Raises ValueError when a device could have more receives posted than
- <a id="hbm_reserve_bytes"></a>`hbm_reserve_bytes(max_rows: int, template: dict[str, tuple[tuple[int, ...], torch.dtype]], depth: int, zero_residual_rows: int)` — [`L154`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_ring.py#L154) — An upper bound on the device memory a stage's ring holds beyond the
- <a id="ring_receives_posted"></a>`ring_receives_posted(stages: int, depth: int, carried: int = 1)` — [`L118`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_ring.py#L118) — The most receive calls a device of a ``stages``-stage ring of
- <a id="hbm_reserve_bytes.row_bytes"></a>`row_bytes(key: str)` — [`L169`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_ring.py#L169)

## Module values
- <a id="_LIBTPU_REQUIREMENT"></a>`_LIBTPU_REQUIREMENT` — [`L105`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_ring.py#L105)
- <a id="_MAX_RECEIVES"></a>`_MAX_RECEIVES` — [`L115`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_ring.py#L115)
- <a id="_TAG_SPAN"></a>`_TAG_SPAN` — [`L103`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_ring.py#L103)
- <a id="logger"></a>`logger` — [`L100`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_ring.py#L100)

