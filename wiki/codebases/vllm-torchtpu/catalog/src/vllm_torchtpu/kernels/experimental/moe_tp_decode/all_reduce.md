---
title: 'Module: src/vllm_torchtpu/kernels/experimental/moe_tp_decode/all_reduce.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/experimental/moe_tp_decode/all_reduce.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.experimental.moe_tp_decode.all_reduce`/
symbols:
  standalone: standalone().
  vmem_bytes: vmem_bytes().
  scratch_shapes: scratch_shapes().
  epilogue: epilogue().
  _run_path: _run_path().
  selftest_inputs: selftest_inputs().
  AllReduceSpec: AllReduceSpec#
  AllReduceSpec.m: AllReduceSpec#m.
  _exchange: _exchange().
  selftest_row_counts: selftest_row_counts().
  kernel_name: kernel_name().
  BF16: BF16.
  AllReduceSpec.h: AllReduceSpec#h.
  make_spec: make_spec().
  AllReduceSpec.lane_groups: AllReduceSpec#lane_groups().
  AllReduceSpec.fold: AllReduceSpec#fold().
  prologue: prologue().
  AllReduceSpec.fold_rows: AllReduceSpec#fold_rows().
  selftest_ok: selftest_ok().
  AllReduceSpec.chunk: AllReduceSpec#chunk().
  _masked: _masked().
  F32: F32.
  _exchange.chunk: _exchange().chunk().
  AllReduceSpec.n: AllReduceSpec#n.
  AllReduceSpec.tile_rows: AllReduceSpec#tile_rows.
  _scratch_names: _scratch_names().
  standalone.kernel: standalone().kernel().
  epilogue._fold_path: epilogue()._fold_path().
  supported: supported().
  _send_all: _send_all().
  _sum_slots: _sum_slots().
  _fold: _fold().
  tiled_bytes: tiled_bytes().
  _exchange.slot: _exchange().slot().
  _stage_rows._all_valid: _stage_rows()._all_valid().
  _stage_rows._some_padding: _stage_rows()._some_padding().
  epilogue._zero: epilogue()._zero().
  epilogue._trim_path: epilogue()._trim_path().
  epilogue._full_path: epilogue()._full_path().
  COLLECTIVE_ID: COLLECTIVE_ID.
  _MESH: _MESH.
  AllReduceSpec.lanes: AllReduceSpec#lanes.
  _recv_all: _recv_all().
  VMEM_FRACTION: VMEM_FRACTION.
  _STANDALONE_HEADROOM: _STANDALONE_HEADROOM.
  _cols: _cols().
  _stage_rows: _stage_rows().
  _unfold: _unfold().
---
# Module: [`src/vllm_torchtpu/kernels/experimental/moe_tp_decode/all_reduce.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/moe_tp_decode/all_reduce.py)

## Classes
### <a id="AllReduceSpec"></a>`AllReduceSpec`
- def: [`src/vllm_torchtpu/kernels/experimental/moe_tp_decode/all_reduce.py:88`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/moe_tp_decode/all_reduce.py#L88)
- doc: Static geometry of one all-reduce (hashable; a jit key).
- signature: `class AllReduceSpec:`
- members:
  - <a id="AllReduceSpec.chunk"></a>`chunk(self)` — [`L98`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/moe_tp_decode/all_reduce.py#L98)
  - <a id="AllReduceSpec.fold"></a>`fold(self)` — [`L110`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/moe_tp_decode/all_reduce.py#L110)
  - <a id="AllReduceSpec.fold_rows"></a>`fold_rows(self)` — [`L106`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/moe_tp_decode/all_reduce.py#L106)
  - <a id="AllReduceSpec.lane_groups"></a>`lane_groups(self)` — [`L102`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/moe_tp_decode/all_reduce.py#L102)
  - <a id="AllReduceSpec.h"></a>`h` — [`L93`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/moe_tp_decode/all_reduce.py#L93)
  - <a id="AllReduceSpec.lanes"></a>`lanes` — [`L95`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/moe_tp_decode/all_reduce.py#L95)
  - <a id="AllReduceSpec.m"></a>`m` — [`L92`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/moe_tp_decode/all_reduce.py#L92)
  - <a id="AllReduceSpec.n"></a>`n` — [`L91`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/moe_tp_decode/all_reduce.py#L91)
  - <a id="AllReduceSpec.tile_rows"></a>`tile_rows` — [`L94`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/moe_tp_decode/all_reduce.py#L94)
- used by: [`standalone`](all_reduce.md#standalone), [`vmem_bytes`](all_reduce.md#vmem_bytes), [`scratch_shapes`](all_reduce.md#scratch_shapes), [`epilogue`](all_reduce.md#epilogue), [`selftest_inputs`](all_reduce.md#selftest_inputs), [`_selftest_op`](../../../layers/adapter/moe_tp_decode.md#_selftest_op), [`selftest_row_counts`](all_reduce.md#selftest_row_counts), [`kernel_name`](all_reduce.md#kernel_name), [`make_spec`](all_reduce.md#make_spec), [`prologue`](all_reduce.md#prologue), [`selftest_ok`](all_reduce.md#selftest_ok), [`_scratch_names`](all_reduce.md#_scratch_names), [`_SELFTEST_OPS`](../../../layers/adapter/moe_tp_decode.md#_SELFTEST_OPS._SELFTEST_OPS), [`_fold_path`](all_reduce.md#epilogue._fold_path), [`_zero`](all_reduce.md#epilogue._zero)

## Functions
- <a id="_stage_rows._all_valid"></a>`_all_valid()` — [`L221`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/moe_tp_decode/all_reduce.py#L221)
- <a id="_cols"></a>`_cols(ref, t, size)` — [`L163`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/moe_tp_decode/all_reduce.py#L163) — Column block t (traced) of width `size` of a 2-D ref view.
- <a id="_exchange"></a>`_exchange(spec, me, buf, rows, cols, s)` — [`L257`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/moe_tp_decode/all_reduce.py#L257) — All-reduce of buf ([rows, cols], in place): reduce-scatter, f32 sum,
- <a id="_fold"></a>`_fold(spec, p32)` — [`L229`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/moe_tp_decode/all_reduce.py#L229) — [tile_rows, h] f32 (rows >= n_valid zero) -> [tile_rows, h / k] f32.
- <a id="epilogue._fold_path"></a>`_fold_path()` — [`L344`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/moe_tp_decode/all_reduce.py#L344)
- <a id="epilogue._full_path"></a>`_full_path()` — [`L357`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/moe_tp_decode/all_reduce.py#L357)
- <a id="_masked"></a>`_masked(partial, nv, rows, dtype)` — [`L203`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/moe_tp_decode/all_reduce.py#L203) — partial[:rows] rounded to bf16, then in `dtype`, with rows >= nv set
- <a id="_recv_all"></a>`_recv_all(spec, me, dst_of, recv_sem)` — [`L187`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/moe_tp_decode/all_reduce.py#L187) — Wait for every other rank t's copy into my dst_of(t) (byte exact: a
- <a id="_run_path"></a>`_run_path(spec, kind, me, nv, partial, out_ref, s, barrier)` — [`L286`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/moe_tp_decode/all_reduce.py#L286) — One row path (fold / trim / full): stage, barrier wait, exchange.
- <a id="_scratch_names"></a>`_scratch_names(spec: AllReduceSpec)` — [`L129`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/moe_tp_decode/all_reduce.py#L129)
- <a id="_send_all"></a>`_send_all(spec, me, src_of, dst_of, send_sem, recv_sem)` — [`L168`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/moe_tp_decode/all_reduce.py#L168) — Start my src_of(t) -> rank t's dst_of(me) for every other rank t, the
- <a id="_stage_rows._some_padding"></a>`_some_padding()` — [`L225`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/moe_tp_decode/all_reduce.py#L225)
- <a id="_stage_rows"></a>`_stage_rows(out_ref, partial, nv)` — [`L215`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/moe_tp_decode/all_reduce.py#L215) — out_ref = partial (bf16) with rows >= nv zeroed; a full bucket skips
- <a id="_sum_slots"></a>`_sum_slots(load, count)` — [`L195`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/moe_tp_decode/all_reduce.py#L195) — f32 sum of count bf16 slots in slot (rank) order.
- <a id="epilogue._trim_path"></a>`_trim_path()` — [`L351`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/moe_tp_decode/all_reduce.py#L351)
- <a id="_unfold"></a>`_unfold(spec, q32, nv, out_ref)` — [`L243`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/moe_tp_decode/all_reduce.py#L243) — Inverse of _fold into out_ref; rows >= nv are +0.
- <a id="epilogue._zero"></a>`_zero()` — [`L336`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/moe_tp_decode/all_reduce.py#L336)
- <a id="_exchange.chunk"></a>`chunk(t)` — [`L265`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/moe_tp_decode/all_reduce.py#L265)
- <a id="epilogue"></a>`epilogue(spec: AllReduceSpec, rank, n_valid, partial, out_ref, scr)` — [`L316`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/moe_tp_decode/all_reduce.py#L316) — All-reduce `partial` ([m, h], rounded to bf16) over the n ranks into
- <a id="standalone.kernel"></a>`kernel(meta_ref, x_ref, out_ref, *scr)` — [`L371`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/moe_tp_decode/all_reduce.py#L371)
- <a id="kernel_name"></a>`kernel_name(spec: AllReduceSpec)` — [`L125`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/moe_tp_decode/all_reduce.py#L125)
- <a id="make_spec"></a>`make_spec(n: int, m: int, h: int)` — [`L114`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/moe_tp_decode/all_reduce.py#L114)
- <a id="prologue"></a>`prologue(spec: AllReduceSpec)` — [`L303`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/moe_tp_decode/all_reduce.py#L303) — Kernel entry: signal the barrier semaphore +1 on every rank, self
- <a id="scratch_shapes"></a>`scratch_shapes(spec: AllReduceSpec)` — [`L134`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/moe_tp_decode/all_reduce.py#L134) — The epilogue's scratch, in the order `epilogue` takes it.
- <a id="selftest_inputs"></a>`selftest_inputs(spec: AllReduceSpec)` — [`L398`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/moe_tp_decode/all_reduce.py#L398) — [n, m, h] f32 partials whose partial and full sums are integers exact
- <a id="selftest_ok"></a>`selftest_ok(spec: AllReduceSpec, x: np.ndarray, out, n_valid: int)` — [`L426`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/moe_tp_decode/all_reduce.py#L426) — One rank's check of an all-reduce of selftest_inputs: rows < n_valid
- <a id="selftest_row_counts"></a>`selftest_row_counts(spec: AllReduceSpec)` — [`L416`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/moe_tp_decode/all_reduce.py#L416) — One n_valid per row path: full, fold, trim (where they exist), zero.
- <a id="_exchange.slot"></a>`slot(q)` — [`L262`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/moe_tp_decode/all_reduce.py#L262)
- <a id="standalone"></a>`standalone(spec: AllReduceSpec)` — [`L364`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/moe_tp_decode/all_reduce.py#L364) — pallas_call(meta, partial) -> out running prologue and epilogue only.
- <a id="supported"></a>`supported(n: int, m: int, h: int, info)` — [`L74`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/moe_tp_decode/all_reduce.py#L74) — Whether an [m, h] partial over n ranks splits into lane-aligned column
- <a id="tiled_bytes"></a>`tiled_bytes(shape, dtype, info)` — [`L63`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/moe_tp_decode/all_reduce.py#L63) — VMEM bytes of a buffer padded to Mosaic tiles: the last dim to the lane
- <a id="vmem_bytes"></a>`vmem_bytes(spec: AllReduceSpec, info)` — [`L151`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/moe_tp_decode/all_reduce.py#L151) — Tiled bytes of the scratch plus an upper bound of the epilogue's f32

## Module values
- <a id="BF16"></a>`BF16` — [`L55`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/moe_tp_decode/all_reduce.py#L55)
- <a id="COLLECTIVE_ID"></a>`COLLECTIVE_ID` — [`L56`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/moe_tp_decode/all_reduce.py#L56)
- <a id="F32"></a>`F32` — [`L55`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/moe_tp_decode/all_reduce.py#L55)
- <a id="VMEM_FRACTION"></a>`VMEM_FRACTION` — [`L57`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/moe_tp_decode/all_reduce.py#L57)
- <a id="_MESH"></a>`_MESH` — [`L58`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/moe_tp_decode/all_reduce.py#L58)
- <a id="_STANDALONE_HEADROOM"></a>`_STANDALONE_HEADROOM` — [`L60`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/moe_tp_decode/all_reduce.py#L60)

