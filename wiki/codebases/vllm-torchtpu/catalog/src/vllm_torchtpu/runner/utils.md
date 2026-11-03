---
title: 'Module: src/vllm_torchtpu/runner/utils.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/runner/utils.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.runner.utils`/
symbols:
  PhaseBasedProfiler._start_profiling: PhaseBasedProfiler#_start_profiling().
  determine_phase_from_batch_composition_stats: determine_phase_from_batch_composition_stats().
  logger: logger.
  PhaseBasedProfiler.inference_phase_seen: PhaseBasedProfiler#inference_phase_seen.
  InferencePhase: InferencePhase#
  PhaseBasedProfiler._merge_profile_directories: PhaseBasedProfiler#_merge_profile_directories().
  PhaseBasedProfiler._canonical_dst_ts: PhaseBasedProfiler#_canonical_dst_ts.
  PhaseBasedProfiler._finish_current_phase: PhaseBasedProfiler#_finish_current_phase().
  PhaseBasedProfiler.step: PhaseBasedProfiler#step().
  PhaseBasedProfiler._step_or_stop_profiling: PhaseBasedProfiler#_step_or_stop_profiling().
  PhaseBasedProfiler.__init__: PhaseBasedProfiler#__init__().
  relayout_rope_caches: relayout_rope_caches().
  relayout_hash_tables: relayout_hash_tables().
  PhaseBasedProfiler.profile_dir_with_phase_suffix: PhaseBasedProfiler#profile_dir_with_phase_suffix.
  PhaseBasedProfiler.current_phase: PhaseBasedProfiler#current_phase.
  HASH_IGNORED_ADDITIONAL_CONFIG_KEYS: HASH_IGNORED_ADDITIONAL_CONFIG_KEYS.
  PhaseBasedProfiler._write_batch_composition_stats_to_file_helper: PhaseBasedProfiler#_write_batch_composition_stats_to_file_helper().
  _install_entry_layout_pin: _install_entry_layout_pin().
  PhaseBasedProfiler.profiling_n_steps_left: PhaseBasedProfiler#profiling_n_steps_left.
  PhaseBasedProfiler.profile_context: PhaseBasedProfiler#profile_context.
  PhaseBasedProfiler._resolve_canonical_dst_ts: PhaseBasedProfiler#_resolve_canonical_dst_ts().
  PhaseBasedProfiler.finish: PhaseBasedProfiler#finish().
  _install_entry_layout_pin._call_with_pinned_layouts: _install_entry_layout_pin()._call_with_pinned_layouts().
  _to_row_major: _to_row_major().
  PhaseBasedProfiler.num_decode_steps_to_skip: PhaseBasedProfiler#num_decode_steps_to_skip.
  PhaseBasedProfiler.worker_rank: PhaseBasedProfiler#worker_rank.
  get_batch_composition_stats: get_batch_composition_stats().
  InferencePhase.DECODE_HEAVY: InferencePhase#DECODE_HEAVY.
  InferencePhase.PREFILL_ONLY: InferencePhase#PREFILL_ONLY.
  InferencePhase.DECODE_ONLY: InferencePhase#DECODE_ONLY.
  PhaseBasedProfiler.decode_steps_skipped: PhaseBasedProfiler#decode_steps_skipped.
  PhaseBasedProfiler.decode_kv_len_threshold: PhaseBasedProfiler#decode_kv_len_threshold.
  PhaseBasedProfiler.prefill_kv_len_threshold: PhaseBasedProfiler#prefill_kv_len_threshold.
  PhaseBasedProfiler.standard_opts: PhaseBasedProfiler#standard_opts.
  _entry_pin_installed: _entry_pin_installed.
  _PINNED_ENTRY_LAYOUTS._PINNED_ENTRY_LAYOUTS: _PINNED_ENTRY_LAYOUTS._PINNED_ENTRY_LAYOUTS.
  BALANCED_RATIO_THRESHOLD: BALANCED_RATIO_THRESHOLD.
  PHASED_PROFILER_NUM_STEPS_TO_PROFILE_FOR: PHASED_PROFILER_NUM_STEPS_TO_PROFILE_FOR.
  PHASED_PROFILER_DECODE_ONLY_KV_LEN_THRESHOLD: PHASED_PROFILER_DECODE_ONLY_KV_LEN_THRESHOLD.
  PHASED_PROFILER_PREFILL_ONLY_KV_LEN_THRESHOLD: PHASED_PROFILER_PREFILL_ONLY_KV_LEN_THRESHOLD.
  PHASED_PROFILER_DECODE_ONLY_KV_LEN_THRESHOLD_KEY: PHASED_PROFILER_DECODE_ONLY_KV_LEN_THRESHOLD_KEY.
  PHASED_PROFILER_PREFILL_ONLY_KV_LEN_THRESHOLD_KEY: PHASED_PROFILER_PREFILL_ONLY_KV_LEN_THRESHOLD_KEY.
  InferencePhase.PREFILL_HEAVY: InferencePhase#PREFILL_HEAVY.
  InferencePhase.BALANCED: InferencePhase#BALANCED.
  PhaseBasedProfiler.profile_dir: PhaseBasedProfiler#profile_dir.
  PREFILL_HEAVY_RATIO_THRESHOLD: PREFILL_HEAVY_RATIO_THRESHOLD.
  DECODE_HEAVY_RATIO_THRESHOLD: DECODE_HEAVY_RATIO_THRESHOLD.
  PHASED_PROFILER_NUM_DECODE_STEPS_TO_SKIP: PHASED_PROFILER_NUM_DECODE_STEPS_TO_SKIP.
  InferencePhase.AMBIGUOUS: InferencePhase#AMBIGUOUS.
  PhaseBasedProfiler: PhaseBasedProfiler#
  PhaseBasedProfiler.num_steps_to_profile_for: PhaseBasedProfiler#num_steps_to_profile_for.
  PhaseBasedProfiler.advanced_opts: PhaseBasedProfiler#advanced_opts.
  PhaseBasedProfiler.world_size: PhaseBasedProfiler#world_size.
  MIN_NUM_SEQS: MIN_NUM_SEQS.
---
# Module: [`src/vllm_torchtpu/runner/utils.py`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/utils.py)

## Classes
### <a id="InferencePhase"></a>`InferencePhase`  ·  implements/extends Enum
- def: [`src/vllm_torchtpu/runner/utils.py:63`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/utils.py#L63)
- signature: `class InferencePhase(Enum):`
- members:
  - <a id="InferencePhase.AMBIGUOUS"></a>`AMBIGUOUS` — [`L67`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/utils.py#L67)
  - <a id="InferencePhase.BALANCED"></a>`BALANCED` — [`L66`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/utils.py#L66)
  - <a id="InferencePhase.DECODE_HEAVY"></a>`DECODE_HEAVY` — [`L65`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/utils.py#L65)
  - <a id="InferencePhase.DECODE_ONLY"></a>`DECODE_ONLY` — [`L69`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/utils.py#L69)
  - <a id="InferencePhase.PREFILL_HEAVY"></a>`PREFILL_HEAVY` — [`L64`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/utils.py#L64)
  - <a id="InferencePhase.PREFILL_ONLY"></a>`PREFILL_ONLY` — [`L68`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/utils.py#L68)
- used by: [`_start_profiling`](utils.md#PhaseBasedProfiler._start_profiling), [`determine_phase_from_batch_composition_stats`](utils.md#determine_phase_from_batch_composition_stats), [`inference_phase_seen`](utils.md#PhaseBasedProfiler.inference_phase_seen)

### <a id="PhaseBasedProfiler"></a>`PhaseBasedProfiler`
- def: [`src/vllm_torchtpu/runner/utils.py:160`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/utils.py#L160)
- doc: Implements a phase-based profiler for PyTorch/XLA, profiling different
- signature: `class PhaseBasedProfiler:`
- members:
  - <a id="PhaseBasedProfiler._finish_current_phase"></a>`_finish_current_phase(self)` — [`L343`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/utils.py#L343) — Closes out the phase capture in progress, if any.
  - <a id="PhaseBasedProfiler._merge_profile_directories"></a>`_merge_profile_directories(self)` — [`L367`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/utils.py#L367) — Consolidates phase trace artifacts.
  - <a id="PhaseBasedProfiler._resolve_canonical_dst_ts"></a>`_resolve_canonical_dst_ts(self, phase_dir: str)` — [`L245`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/utils.py#L245) — Resolve the canonical destination timestamp for this phase.
  - <a id="PhaseBasedProfiler._start_profiling"></a>`_start_profiling(self, batch_composition_stats: dict)` — [`L249`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/utils.py#L249) — Starts profiling if the current phase is unseen.
  - <a id="PhaseBasedProfiler._step_or_stop_profiling"></a>`_step_or_stop_profiling(self, batch_composition_stats: dict)` — [`L335`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/utils.py#L335) — Steps or stops the profiler.
  - <a id="PhaseBasedProfiler._write_batch_composition_stats_to_file_helper"></a>`_write_batch_composition_stats_to_file_helper(self, batch_composition_stats: dict)` — [`L226`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/utils.py#L226) — Writes the batch composition stats to a file.
  - <a id="PhaseBasedProfiler.finish"></a>`finish(self)` — [`L358`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/utils.py#L358) — Force-stops a phase capture in progress.
  - <a id="PhaseBasedProfiler.step"></a>`step(self, batch_composition_stats: dict)` — [`L387`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/utils.py#L387) — Steps the profiler and logs batch composition stats.
  - <a id="PhaseBasedProfiler.advanced_opts"></a>`advanced_opts` — [`L191`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/utils.py#L191)
  - <a id="PhaseBasedProfiler.current_phase"></a>`current_phase` — [`L200`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/utils.py#L200)
  - <a id="PhaseBasedProfiler.decode_kv_len_threshold"></a>`decode_kv_len_threshold` — [`L186`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/utils.py#L186)
  - <a id="PhaseBasedProfiler.decode_steps_skipped"></a>`decode_steps_skipped` — [`L183`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/utils.py#L183)
  - <a id="PhaseBasedProfiler.inference_phase_seen"></a>`inference_phase_seen` — [`L193`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/utils.py#L193)
  - <a id="PhaseBasedProfiler.num_decode_steps_to_skip"></a>`num_decode_steps_to_skip` — [`L182`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/utils.py#L182)
  - <a id="PhaseBasedProfiler.num_steps_to_profile_for"></a>`num_steps_to_profile_for` — [`L179`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/utils.py#L179)
  - <a id="PhaseBasedProfiler.prefill_kv_len_threshold"></a>`prefill_kv_len_threshold` — [`L189`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/utils.py#L189)
  - <a id="PhaseBasedProfiler.profile_context"></a>`profile_context` — [`L203`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/utils.py#L203)
  - <a id="PhaseBasedProfiler.profile_dir"></a>`profile_dir` — [`L192`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/utils.py#L192)
  - <a id="PhaseBasedProfiler.profile_dir_with_phase_suffix"></a>`profile_dir_with_phase_suffix` — [`L178`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/utils.py#L178)
  - <a id="PhaseBasedProfiler.profiling_n_steps_left"></a>`profiling_n_steps_left` — [`L177`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/utils.py#L177)
  - <a id="PhaseBasedProfiler.standard_opts"></a>`standard_opts` — [`L190`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/utils.py#L190)
  - <a id="PhaseBasedProfiler.worker_rank"></a>`worker_rank` — [`L201`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/utils.py#L201)
  - <a id="PhaseBasedProfiler.world_size"></a>`world_size` — [`L202`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/utils.py#L202)
- protocol/private: <a id="PhaseBasedProfiler.__init__"></a>`__init__`[`L165`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/utils.py#L165), <a id="PhaseBasedProfiler._canonical_dst_ts"></a>`_canonical_dst_ts`[`L204`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/utils.py#L204)
- uses (calls/refs, reference-scoped): [`determine_phase_from_batch_composition_stats`](utils.md#determine_phase_from_batch_composition_stats), [`logger`](utils.md#logger), [`resolve_canonical_dst_ts`](../profiler_trace.md#resolve_canonical_dst_ts), [`InferencePhase`](utils.md#InferencePhase), [`clear_canonical_ts_marker`](../profiler_trace.md#clear_canonical_ts_marker), [`merge_rank_capture`](../profiler_trace.md#merge_rank_capture), [`DECODE_HEAVY`](utils.md#InferencePhase.DECODE_HEAVY), [`DECODE_ONLY`](utils.md#InferencePhase.DECODE_ONLY), [`PREFILL_ONLY`](utils.md#InferencePhase.PREFILL_ONLY), [`rank_capture_dir`](../profiler_trace.md#rank_capture_dir), [`BALANCED`](utils.md#InferencePhase.BALANCED), [`PHASED_PROFILER_DECODE_ONLY_KV_LEN_THRESHOLD`](utils.md#PHASED_PROFILER_DECODE_ONLY_KV_LEN_THRESHOLD), [`PHASED_PROFILER_NUM_STEPS_TO_PROFILE_FOR`](utils.md#PHASED_PROFILER_NUM_STEPS_TO_PROFILE_FOR), [`PHASED_PROFILER_PREFILL_ONLY_KV_LEN_THRESHOLD`](utils.md#PHASED_PROFILER_PREFILL_ONLY_KV_LEN_THRESHOLD), [`PREFILL_HEAVY`](utils.md#InferencePhase.PREFILL_HEAVY), [`PHASED_PROFILER_NUM_DECODE_STEPS_TO_SKIP`](utils.md#PHASED_PROFILER_NUM_DECODE_STEPS_TO_SKIP)
- used by: [`execute_model`](tpu_runner.md#TPUModelRunner.execute_model), [`start_phased_profiling`](tpu_runner.md#TPUModelRunner.start_phased_profiling), [`stop_phased_profiling`](tpu_runner.md#TPUModelRunner.stop_phased_profiling)

## Functions
- <a id="_install_entry_layout_pin._call_with_pinned_layouts"></a>`_call_with_pinned_layouts(self, graph_module, example_inputs, *args, **kwargs)` — [`L507`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/utils.py#L507)
- <a id="_install_entry_layout_pin"></a>`_install_entry_layout_pin()` — [`L498`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/utils.py#L498) — Make the compiler pin entry layouts for buffers in the registry.
- <a id="_to_row_major"></a>`_to_row_major(tensor: torch.Tensor)` — [`L417`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/utils.py#L417) — Return `tensor` re-materialized on its device with a `{1,0}` layout.
- <a id="determine_phase_from_batch_composition_stats"></a>`determine_phase_from_batch_composition_stats(batch_composition_stats: dict[str, Any])` — [`L72`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/utils.py#L72) — Determines the inference phase based on the batch composition stats.
- <a id="get_batch_composition_stats"></a>`get_batch_composition_stats(batch_id: int, input_batch: Any, total_num_scheduled_tokens: int, num_reqs: int, padded_total_num_scheduled_tokens: int, scheduler_output: VllmSchedulerOutput)` — [`L96`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/utils.py#L96) — Logs batch composition stats and returns them as a dict.
- <a id="relayout_hash_tables"></a>`relayout_hash_tables(model: torch.nn.Module)` — [`L470`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/utils.py#L470) — Re-materialize every MOE hash-routing table row-major.
- <a id="relayout_rope_caches"></a>`relayout_rope_caches(model: torch.nn.Module)` — [`L440`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/utils.py#L440) — Re-materialize every rope cache with a row-major device layout.

## Module values
- <a id="BALANCED_RATIO_THRESHOLD"></a>`BALANCED_RATIO_THRESHOLD` — [`L37`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/utils.py#L37)
- <a id="DECODE_HEAVY_RATIO_THRESHOLD"></a>`DECODE_HEAVY_RATIO_THRESHOLD` — [`L36`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/utils.py#L36)
- <a id="HASH_IGNORED_ADDITIONAL_CONFIG_KEYS"></a>`HASH_IGNORED_ADDITIONAL_CONFIG_KEYS` — [`L55`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/utils.py#L55)
- <a id="MIN_NUM_SEQS"></a>`MIN_NUM_SEQS` — [`L33`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/utils.py#L33)
- <a id="PHASED_PROFILER_DECODE_ONLY_KV_LEN_THRESHOLD"></a>`PHASED_PROFILER_DECODE_ONLY_KV_LEN_THRESHOLD` — [`L40`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/utils.py#L40)
- <a id="PHASED_PROFILER_DECODE_ONLY_KV_LEN_THRESHOLD_KEY"></a>`PHASED_PROFILER_DECODE_ONLY_KV_LEN_THRESHOLD_KEY` — [`L45`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/utils.py#L45)
- <a id="PHASED_PROFILER_NUM_DECODE_STEPS_TO_SKIP"></a>`PHASED_PROFILER_NUM_DECODE_STEPS_TO_SKIP` — [`L39`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/utils.py#L39)
- <a id="PHASED_PROFILER_NUM_STEPS_TO_PROFILE_FOR"></a>`PHASED_PROFILER_NUM_STEPS_TO_PROFILE_FOR` — [`L38`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/utils.py#L38)
- <a id="PHASED_PROFILER_PREFILL_ONLY_KV_LEN_THRESHOLD"></a>`PHASED_PROFILER_PREFILL_ONLY_KV_LEN_THRESHOLD` — [`L41`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/utils.py#L41)
- <a id="PHASED_PROFILER_PREFILL_ONLY_KV_LEN_THRESHOLD_KEY"></a>`PHASED_PROFILER_PREFILL_ONLY_KV_LEN_THRESHOLD_KEY` — [`L48`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/utils.py#L48)
- <a id="PREFILL_HEAVY_RATIO_THRESHOLD"></a>`PREFILL_HEAVY_RATIO_THRESHOLD` — [`L35`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/utils.py#L35)
- <a id="_PINNED_ENTRY_LAYOUTS._PINNED_ENTRY_LAYOUTS"></a>`_PINNED_ENTRY_LAYOUTS` — [`L413`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/utils.py#L413)
- <a id="_entry_pin_installed"></a>`_entry_pin_installed` — [`L414`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/utils.py#L414)
- <a id="logger"></a>`logger` — [`L31`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/utils.py#L31)

