---
title: 'Module: torchtitan/experiments/rl/tests/test_generator.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/rl/tests/test_generator.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.rl.tests.test_generator`/
symbols:
  test_qwen36_27b_config_applies_offset_rmsnorm_to_both_actors: test_qwen36_27b_config_applies_offset_rmsnorm_to_both_actors().
  test_vllm_uneven_decode_tp_padding: test_vllm_uneven_decode_tp_padding().
  test_process_finished_requests_releases_dp_router_load.main: test_process_finished_requests_releases_dp_router_load().main().
  test_process_finished_requests_resolves_future_with_completion.main: test_process_finished_requests_resolves_future_with_completion().main().
  _generator: _generator().
  test_build_sampling_params_matches_contract: test_build_sampling_params_matches_contract().
  test_batch_invariant_requires_prefix_cache_reset: test_batch_invariant_requires_prefix_cache_reset().
  test_expert_sequence_parallel_padding_filters_cudagraph_sizes: test_expert_sequence_parallel_padding_filters_cudagraph_sizes().
  test_inference_parallelism_propagates_dense_sequence_parallelism: test_inference_parallelism_propagates_dense_sequence_parallelism().
  _dispatcher: _dispatcher().
  test_build_sampling_params_seed_and_stop_default_to_none: test_build_sampling_params_seed_and_stop_default_to_none().
  test_reset_running_requests_requires_prefix_cache_reset: test_reset_running_requests_requires_prefix_cache_reset().
  test_process_finished_requests_noop_on_nonzero_tp_rank: test_process_finished_requests_noop_on_nonzero_tp_rank().
  test_metric_timing_math_and_prefix_override: test_metric_timing_math_and_prefix_override().
  test_decode_metrics_absent_for_single_generated_token: test_decode_metrics_absent_for_single_generated_token().
  test_expert_sequence_parallel_padding_rejects_no_valid_cudagraph_sizes: test_expert_sequence_parallel_padding_rejects_no_valid_cudagraph_sizes().
  test_expert_sequence_parallel_padding_disabled_without_ep: test_expert_sequence_parallel_padding_disabled_without_ep().
  test_cudagraph_full_mode_no_compile: test_cudagraph_full_mode_no_compile().
  test_cudagraph_decode_only_capture_sizes_cover_max_num_seqs: test_cudagraph_decode_only_capture_sizes_cover_max_num_seqs().
  test_cudagraph_full_mode_extends_capture_sizes_to_chunk: test_cudagraph_full_mode_extends_capture_sizes_to_chunk().
  test_inference_parallelism_disables_dense_sequence_parallelism: test_inference_parallelism_disables_dense_sequence_parallelism().
  _request_output: _request_output().
  test_trainer_requires_prefix_cache_reset_when_hotswap_off: test_trainer_requires_prefix_cache_reset_when_hotswap_off().
  test_cudagraph_disabled_preserves_sequence_parallel_config: test_cudagraph_disabled_preserves_sequence_parallel_config().
  test_expert_sequence_parallel_padding_keeps_small_cudagraph_batches: test_expert_sequence_parallel_padding_keeps_small_cudagraph_batches().
  test_cudagraph_default_mode_is_full_decode_only: test_cudagraph_default_mode_is_full_decode_only().
  test_cudagraph_rejects_nonpositive_max_num_seqs: test_cudagraph_rejects_nonpositive_max_num_seqs().
  test_sequence_parallel_padding_rounds_runner_tokens: test_sequence_parallel_padding_rounds_runner_tokens().
  _PARALLELISM: _PARALLELISM.
  _FakeEngine.renderer: _FakeEngine#renderer.
  _FakeEngine.add_request: _FakeEngine#add_request().
  test_process_finished_requests_resolves_future_with_completion: test_process_finished_requests_resolves_future_with_completion().
  test_process_finished_requests_releases_dp_router_load: test_process_finished_requests_releases_dp_router_load().
  _sample: _sample().
  _FakeRenderer: _FakeRenderer#
  _FakeEngine: _FakeEngine#
  _FakeEngine.add_requests: _FakeEngine#add_requests.
  _FakeRenderer.render_cmpl: _FakeRenderer#render_cmpl().
  _FakeEngine.__init__: _FakeEngine#__init__().
---
# Module: [`torchtitan/experiments/rl/tests/test_generator.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_generator.py)

> **Collapsed catalog** (39 symbols) — one row per symbol with its source line; member detail omitted. See the source link above, or the curated codebase page, for depth.

- <a id="_FakeEngine"></a>`_FakeEngine` — [`L71`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_generator.py#L71)
- <a id="_FakeEngine.__init__"></a>`_FakeEngine.__init__` — [`L72`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_generator.py#L72)
- <a id="_FakeEngine.add_request"></a>`_FakeEngine.add_request` — [`L76`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_generator.py#L76)
- <a id="_FakeEngine.add_requests"></a>`_FakeEngine.add_requests` — [`L73`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_generator.py#L73)
- <a id="_FakeEngine.renderer"></a>`_FakeEngine.renderer` — [`L74`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_generator.py#L74)
- <a id="_FakeRenderer"></a>`_FakeRenderer` — [`L57`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_generator.py#L57)
- <a id="_FakeRenderer.render_cmpl"></a>`_FakeRenderer.render_cmpl` — [`L60`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_generator.py#L60)
- <a id="_PARALLELISM"></a>`_PARALLELISM` — [`L276`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_generator.py#L276)
- <a id="_dispatcher"></a>`_dispatcher` — [`L118`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_generator.py#L118)
- <a id="_generator"></a>`_generator` — [`L104`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_generator.py#L104)
- <a id="_request_output"></a>`_request_output` — [`L88`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_generator.py#L88)
- <a id="_sample"></a>`_sample` — [`L80`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_generator.py#L80)
- <a id="test_batch_invariant_requires_prefix_cache_reset"></a>`test_batch_invariant_requires_prefix_cache_reset` — [`L279`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_generator.py#L279)
- <a id="test_build_sampling_params_matches_contract"></a>`test_build_sampling_params_matches_contract` — [`L212`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_generator.py#L212)
- <a id="test_build_sampling_params_seed_and_stop_default_to_none"></a>`test_build_sampling_params_seed_and_stop_default_to_none` — [`L234`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_generator.py#L234)
- <a id="test_cudagraph_decode_only_capture_sizes_cover_max_num_seqs"></a>`test_cudagraph_decode_only_capture_sizes_cover_max_num_seqs` — [`L454`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_generator.py#L454)
- <a id="test_cudagraph_default_mode_is_full_decode_only"></a>`test_cudagraph_default_mode_is_full_decode_only` — [`L431`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_generator.py#L431)
- <a id="test_cudagraph_disabled_preserves_sequence_parallel_config"></a>`test_cudagraph_disabled_preserves_sequence_parallel_config` — [`L341`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_generator.py#L341)
- <a id="test_cudagraph_full_mode_extends_capture_sizes_to_chunk"></a>`test_cudagraph_full_mode_extends_capture_sizes_to_chunk` — [`L467`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_generator.py#L467)
- <a id="test_cudagraph_full_mode_no_compile"></a>`test_cudagraph_full_mode_no_compile` — [`L443`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_generator.py#L443)
- <a id="test_cudagraph_rejects_nonpositive_max_num_seqs"></a>`test_cudagraph_rejects_nonpositive_max_num_seqs` — [`L479`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_generator.py#L479)
- <a id="test_decode_metrics_absent_for_single_generated_token"></a>`test_decode_metrics_absent_for_single_generated_token` — [`L262`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_generator.py#L262)
- <a id="test_expert_sequence_parallel_padding_disabled_without_ep"></a>`test_expert_sequence_parallel_padding_disabled_without_ep` — [`L393`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_generator.py#L393)
- <a id="test_expert_sequence_parallel_padding_filters_cudagraph_sizes"></a>`test_expert_sequence_parallel_padding_filters_cudagraph_sizes` — [`L353`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_generator.py#L353)
- <a id="test_expert_sequence_parallel_padding_keeps_small_cudagraph_batches"></a>`test_expert_sequence_parallel_padding_keeps_small_cudagraph_batches` — [`L370`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_generator.py#L370)
- <a id="test_expert_sequence_parallel_padding_rejects_no_valid_cudagraph_sizes"></a>`test_expert_sequence_parallel_padding_rejects_no_valid_cudagraph_sizes` — [`L381`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_generator.py#L381)
- <a id="test_inference_parallelism_disables_dense_sequence_parallelism"></a>`test_inference_parallelism_disables_dense_sequence_parallelism` — [`L508`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_generator.py#L508)
- <a id="test_inference_parallelism_propagates_dense_sequence_parallelism"></a>`test_inference_parallelism_propagates_dense_sequence_parallelism` — [`L488`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_generator.py#L488)
- <a id="test_metric_timing_math_and_prefix_override"></a>`test_metric_timing_math_and_prefix_override` — [`L246`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_generator.py#L246)
- <a id="test_process_finished_requests_noop_on_nonzero_tp_rank"></a>`test_process_finished_requests_noop_on_nonzero_tp_rank` — [`L174`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_generator.py#L174)
- <a id="test_process_finished_requests_releases_dp_router_load"></a>`test_process_finished_requests_releases_dp_router_load` — [`L184`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_generator.py#L184)
- <a id="test_process_finished_requests_releases_dp_router_load.main"></a>`test_process_finished_requests_releases_dp_router_load.main` — [`L185`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_generator.py#L185)
- <a id="test_process_finished_requests_resolves_future_with_completion"></a>`test_process_finished_requests_resolves_future_with_completion` — [`L135`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_generator.py#L135)
- <a id="test_process_finished_requests_resolves_future_with_completion.main"></a>`test_process_finished_requests_resolves_future_with_completion.main` — [`L136`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_generator.py#L136)
- <a id="test_qwen36_27b_config_applies_offset_rmsnorm_to_both_actors"></a>`test_qwen36_27b_config_applies_offset_rmsnorm_to_both_actors` — [`L319`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_generator.py#L319)
- <a id="test_reset_running_requests_requires_prefix_cache_reset"></a>`test_reset_running_requests_requires_prefix_cache_reset` — [`L288`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_generator.py#L288)
- <a id="test_sequence_parallel_padding_rounds_runner_tokens"></a>`test_sequence_parallel_padding_rounds_runner_tokens` — [`L410`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_generator.py#L410)
- <a id="test_trainer_requires_prefix_cache_reset_when_hotswap_off"></a>`test_trainer_requires_prefix_cache_reset_when_hotswap_off` — [`L297`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_generator.py#L297)
- <a id="test_vllm_uneven_decode_tp_padding"></a>`test_vllm_uneven_decode_tp_padding` — [`L515`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_generator.py#L515)
