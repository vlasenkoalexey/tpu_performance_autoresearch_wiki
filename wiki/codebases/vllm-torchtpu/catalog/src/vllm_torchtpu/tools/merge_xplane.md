---
title: 'Module: src/vllm_torchtpu/tools/merge_xplane.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/tools/merge_xplane.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.tools.merge_xplane`/
symbols:
  main: main().
  merge_session: merge_session().
  _make_session: _make_session().
  discover_sessions: discover_sessions().
  _tag_host_cpu_plane: _tag_host_cpu_plane().
  _rewrite_plane_name: _rewrite_plane_name().
  Capture.label: Capture#label().
  _delimited: _delimited().
  Session.captures: Session#captures.
  Session.output_name: Session#output_name().
  Capture.rank: Capture#rank.
  Session.default_output_dir: Session#default_output_dir().
  Session.missing_ranks: Session#missing_ranks().
  Session.directory: Session#directory.
  _format_size: _format_size().
  Capture: Capture#
  Session: Session#
  Session.label: Session#label.
  Session.timestamp: Session#timestamp.
  _phase_dir: _phase_dir().
  _rank_of: _rank_of().
  _session_identity: _session_identity().
  _TRACE_SUFFIX: _TRACE_SUFFIX.
  Capture.path: Capture#path.
  Capture.slot: Capture#slot.
  MergeResult.size: MergeResult#size.
  MergeResult.deduplicated: MergeResult#deduplicated.
  _METADATA_PLANE: _METADATA_PLANE.
  _HOST_CPU_PLANE: _HOST_CPU_PLANE.
  _varint: _varint().
  _is_within: _is_within().
  discover_sessions.normalized: discover_sessions().normalized().
  MergeResult: MergeResult#
  MergeResult.path: MergeResult#path.
  MergeResult.planes: MergeResult#planes.
  MergeResult.planes_read: MergeResult#planes_read.
  _PREFIX_ID_RE: _PREFIX_ID_RE.
  _RANK_PREFIX_RE: _RANK_PREFIX_RE.
  _XSPACE_PLANES_FIELD: _XSPACE_PLANES_FIELD.
  _XSPACE_ERRORS_FIELD: _XSPACE_ERRORS_FIELD.
  _XSPACE_WARNINGS_FIELD: _XSPACE_WARNINGS_FIELD.
  _XSPACE_HOSTNAMES_FIELD: _XSPACE_HOSTNAMES_FIELD.
  _WIRE_TYPE_LENGTH_DELIMITED: _WIRE_TYPE_LENGTH_DELIMITED.
  _next_stat_metadata_id: _next_stat_metadata_id().
  _is_inside_session_dir: _is_inside_session_dir().
  _parse_args: _parse_args().
---
# Module: [`src/vllm_torchtpu/tools/merge_xplane.py`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/tools/merge_xplane.py)

## Classes
### <a id="Capture"></a>`Capture`
- def: [`src/vllm_torchtpu/tools/merge_xplane.py:81`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/tools/merge_xplane.py#L81)
- doc: One worker's trace file.
- signature: `class Capture:`
- members:
  - <a id="Capture.label"></a>`label(self)` — [`L93`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/tools/merge_xplane.py#L93) — Human-readable tag used in merged plane and line names.
  - <a id="Capture.path"></a>`path` — [`L84`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/tools/merge_xplane.py#L84)
  - <a id="Capture.rank"></a>`rank` — [`L85`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/tools/merge_xplane.py#L85)
  - <a id="Capture.slot"></a>`slot` — [`L90`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/tools/merge_xplane.py#L90)
- used by: [`main`](merge_xplane.md#main), [`merge_session`](merge_xplane.md#merge_session), [`_make_session`](merge_xplane.md#_make_session), [`_rewrite_plane_name`](merge_xplane.md#_rewrite_plane_name), [`_tag_host_cpu_plane`](merge_xplane.md#_tag_host_cpu_plane), [`captures`](merge_xplane.md#Session.captures), [`missing_ranks`](merge_xplane.md#Session.missing_ranks)

### <a id="MergeResult"></a>`MergeResult`
- def: [`src/vllm_torchtpu/tools/merge_xplane.py:381`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/tools/merge_xplane.py#L381)
- doc: What one merge produced.
- signature: `class MergeResult:`
- members:
  - <a id="MergeResult.deduplicated"></a>`deduplicated` — [`L393`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/tools/merge_xplane.py#L393)
  - <a id="MergeResult.path"></a>`path` — [`L389`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/tools/merge_xplane.py#L389)
  - <a id="MergeResult.planes"></a>`planes` — [`L391`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/tools/merge_xplane.py#L391)
  - <a id="MergeResult.planes_read"></a>`planes_read` — [`L392`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/tools/merge_xplane.py#L392)
  - <a id="MergeResult.size"></a>`size` — [`L390`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/tools/merge_xplane.py#L390)
- used by: [`main`](merge_xplane.md#main), [`merge_session`](merge_xplane.md#merge_session)

### <a id="Session"></a>`Session`
- def: [`src/vllm_torchtpu/tools/merge_xplane.py:99`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/tools/merge_xplane.py#L99)
- doc: One capture session: every rank's trace from a single profile window.
- signature: `class Session:`
- members:
  - <a id="Session.default_output_dir"></a>`default_output_dir(self)` — [`L113`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/tools/merge_xplane.py#L113) — Where the merged file goes when the caller named no destination.
  - <a id="Session.missing_ranks"></a>`missing_ranks(self)` — [`L128`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/tools/merge_xplane.py#L128) — Ranks absent from an otherwise contiguous 0..N-1 set.
  - <a id="Session.output_name"></a>`output_name(self)` — [`L108`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/tools/merge_xplane.py#L108)
  - <a id="Session.captures"></a>`captures` — [`L105`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/tools/merge_xplane.py#L105)
  - <a id="Session.directory"></a>`directory` — [`L104`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/tools/merge_xplane.py#L104)
  - <a id="Session.label"></a>`label` — [`L102`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/tools/merge_xplane.py#L102)
  - <a id="Session.timestamp"></a>`timestamp` — [`L103`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/tools/merge_xplane.py#L103)
- uses (calls/refs, reference-scoped): [`rank`](merge_xplane.md#Capture.rank), [`Capture`](merge_xplane.md#Capture), [`_phase_dir`](merge_xplane.md#_phase_dir), [`_TRACE_SUFFIX`](merge_xplane.md#_TRACE_SUFFIX)
- used by: [`main`](merge_xplane.md#main), [`merge_session`](merge_xplane.md#merge_session), [`_make_session`](merge_xplane.md#_make_session), [`discover_sessions`](merge_xplane.md#discover_sessions)

## Functions
- <a id="_delimited"></a>`_delimited(field_number: int, payload: bytes)` — [`L153`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/tools/merge_xplane.py#L153) — Encode one length-delimited field, ready to append to a message.
- <a id="_format_size"></a>`_format_size(num_bytes: int)` — [`L481`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/tools/merge_xplane.py#L481) — Human-readable size, staying in MB so totals stay comparable.
- <a id="_is_inside_session_dir"></a>`_is_inside_session_dir(directory: str)` — [`L470`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/tools/merge_xplane.py#L470) — True if `directory` sits within a `plugins/profile/` capture session.
- <a id="_is_within"></a>`_is_within(path: str, ancestor: str)` — [`L233`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/tools/merge_xplane.py#L233)
- <a id="_make_session"></a>`_make_session(directory: str, paths: list[str])` — [`L199`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/tools/merge_xplane.py#L199)
- <a id="_next_stat_metadata_id"></a>`_next_stat_metadata_id(plane)` — [`L298`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/tools/merge_xplane.py#L298) — Return an unused key for `plane.stat_metadata`.
- <a id="_parse_args"></a>`_parse_args(argv: list[str] | None)` — [`L494`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/tools/merge_xplane.py#L494)
- <a id="_phase_dir"></a>`_phase_dir(session_dir: str)` — [`L170`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/tools/merge_xplane.py#L170) — The directory holding `plugins/`, or None if this is not a session dir.
- <a id="_rank_of"></a>`_rank_of(path: str)` — [`L165`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/tools/merge_xplane.py#L165)
- <a id="_rewrite_plane_name"></a>`_rewrite_plane_name(plane, capture: Capture, local_to_global: dict[tuple[str, int], int], next_id_per_prefix: dict[str, int])` — [`L350`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/tools/merge_xplane.py#L350) — Rename one plane so it stays distinct once ranks are combined.
- <a id="_session_identity"></a>`_session_identity(directory: str)` — [`L186`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/tools/merge_xplane.py#L186) — Derive a (label, timestamp) pair from a session directory path.
- <a id="_tag_host_cpu_plane"></a>`_tag_host_cpu_plane(plane, capture: Capture)` — [`L307`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/tools/merge_xplane.py#L307) — Make one rank's host-CPU plane distinguishable in the merged file.
- <a id="_varint"></a>`_varint(value: int)` — [`L140`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/tools/merge_xplane.py#L140) — Encode `value` as a protobuf base-128 varint.
- <a id="discover_sessions"></a>`discover_sessions(paths: list[str], *, skip: tuple[str, ...] = ())` — [`L239`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/tools/merge_xplane.py#L239) — Group the trace files under `paths` into capture sessions.
- <a id="main"></a>`main(argv: list[str] | None = None)` — [`L529`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/tools/merge_xplane.py#L529)
- <a id="merge_session"></a>`merge_session(session: Session, output_path: str)` — [`L396`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/tools/merge_xplane.py#L396) — Merge `session` into `output_path`.
- <a id="discover_sessions.normalized"></a>`normalized(path: str)` — [`L282`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/tools/merge_xplane.py#L282)

## Module values
- <a id="_HOST_CPU_PLANE"></a>`_HOST_CPU_PLANE` — [`L77`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/tools/merge_xplane.py#L77)
- <a id="_METADATA_PLANE"></a>`_METADATA_PLANE` — [`L76`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/tools/merge_xplane.py#L76)
- <a id="_PREFIX_ID_RE"></a>`_PREFIX_ID_RE` — [`L59`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/tools/merge_xplane.py#L59)
- <a id="_RANK_PREFIX_RE"></a>`_RANK_PREFIX_RE` — [`L63`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/tools/merge_xplane.py#L63)
- <a id="_TRACE_SUFFIX"></a>`_TRACE_SUFFIX` — [`L65`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/tools/merge_xplane.py#L65)
- <a id="_WIRE_TYPE_LENGTH_DELIMITED"></a>`_WIRE_TYPE_LENGTH_DELIMITED` — [`L74`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/tools/merge_xplane.py#L74)
- <a id="_XSPACE_ERRORS_FIELD"></a>`_XSPACE_ERRORS_FIELD` — [`L70`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/tools/merge_xplane.py#L70)
- <a id="_XSPACE_HOSTNAMES_FIELD"></a>`_XSPACE_HOSTNAMES_FIELD` — [`L72`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/tools/merge_xplane.py#L72)
- <a id="_XSPACE_PLANES_FIELD"></a>`_XSPACE_PLANES_FIELD` — [`L69`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/tools/merge_xplane.py#L69)
- <a id="_XSPACE_WARNINGS_FIELD"></a>`_XSPACE_WARNINGS_FIELD` — [`L71`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/tools/merge_xplane.py#L71)

