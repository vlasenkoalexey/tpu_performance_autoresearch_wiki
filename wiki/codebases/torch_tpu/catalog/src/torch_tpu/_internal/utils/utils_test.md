---
title: 'Module: src/torch_tpu/_internal/utils/utils_test.py'
type: catalog
provenance: extracted
module: src/torch_tpu/_internal/utils/utils_test.py
status: fresh
symbol_base: scip-python python torch_tpu 0.0.0 `src.torch_tpu._internal.utils.utils_test`/
symbols:
  fwd: fwd().
  bwd: bwd().
  AllTest.assert_logs_equal: AllTest#assert_logs_equal().
  AllTest.device: AllTest#device.
  AllTest.test_model_shlo_dyn: AllTest#test_model_shlo_dyn().
  AllTest.test_model_shlo: AllTest#test_model_shlo().
  AllTest.test_activation_tracer_on_zero_child_module_creates_log: AllTest#test_activation_tracer_on_zero_child_module_creates_log().
  AllTest.test_activation_tracer_on_one_child_module_creates_log: AllTest#test_activation_tracer_on_one_child_module_creates_log().
  AllTest.test_activation_tracer_on_complex_module_creates_log: AllTest#test_activation_tracer_on_complex_module_creates_log().
  AllTest.test_activation_tracer_on_zero_child_module_backward_call_creates_log: AllTest#test_activation_tracer_on_zero_child_module_backward_call_creates_log().
  AllTest.test_activation_tracer_on_one_child_module_backward_call_creates_log: AllTest#test_activation_tracer_on_one_child_module_backward_call_creates_log().
  AllTest.test_activation_tracer_on_complex_module_backward_call_creates_log: AllTest#test_activation_tracer_on_complex_module_backward_call_creates_log().
  AllTest.test_assert_close_with_callable_atol_success: AllTest#test_assert_close_with_callable_atol_success().
  AllTest.test_assert_close_with_callable_atol_failure: AllTest#test_assert_close_with_callable_atol_failure().
  AllTest.test_function_shlo: AllTest#test_function_shlo().
  AllTest.test_function_list_inputs: AllTest#test_function_list_inputs().
  AllTest.test_print_multiple_tensor_inputs: AllTest#test_print_multiple_tensor_inputs().
  AllTest.test_op_tracer_as_decorator: AllTest#test_op_tracer_as_decorator().
  AllTest.test_op_tracer_as_wrapper: AllTest#test_op_tracer_as_wrapper().
  AllTest.test_aten_count: AllTest#test_aten_count().
  DummyWithLogits.logits: DummyWithLogits#logits.
  DummyWithLastHiddenState.last_hidden_state: DummyWithLastHiddenState#last_hidden_state.
  DummyWithSample.sample: DummyWithSample#sample.
  DummyWithWaveform.waveform: DummyWithWaveform#waveform.
  DummyWithAudio.audio: DummyWithAudio#audio.
  DummyWithSequences.sequences: DummyWithSequences#sequences.
  DummyWithLossAndLogits.logits: DummyWithLossAndLogits#logits.
  AllTest.foo: AllTest#foo().
  AllTest.f: AllTest#f().
  AllTest.test_model_shlo_dyn.AddModule: AllTest#test_model_shlo_dyn().AddModule#
  AllTest.test_model_shlo.RoundModule: AllTest#test_model_shlo().RoundModule#
  AllTest.test_print_multiple_tensor_inputs.MultiModule: AllTest#test_print_multiple_tensor_inputs().MultiModule#
  AllTest.test_aten_count.MultiModule: AllTest#test_aten_count().MultiModule#
  AllTest.assert_events_equal: AllTest#assert_events_equal().
  AllTest.test_get_primary_tensor_output.DummyWithLogits: AllTest#test_get_primary_tensor_output().DummyWithLogits#
  AllTest.test_get_primary_tensor_output.DummyWithLastHiddenState: AllTest#test_get_primary_tensor_output().DummyWithLastHiddenState#
  AllTest.test_get_primary_tensor_output.DummyWithSample: AllTest#test_get_primary_tensor_output().DummyWithSample#
  AllTest.test_get_primary_tensor_output.DummyWithWaveform: AllTest#test_get_primary_tensor_output().DummyWithWaveform#
  AllTest.test_get_primary_tensor_output.DummyWithAudio: AllTest#test_get_primary_tensor_output().DummyWithAudio#
  AllTest.test_get_primary_tensor_output.DummyWithSequences: AllTest#test_get_primary_tensor_output().DummyWithSequences#
  AllTest.test_get_primary_tensor_output.DummyWithLossAndLogits: AllTest#test_get_primary_tensor_output().DummyWithLossAndLogits#
  AllTest: AllTest#
  AllTest.setUp: AllTest#setUp().
  AllTest.test_compare_strict_mode: AllTest#test_compare_strict_mode().
  AllTest.test_compare_loose_mode: AllTest#test_compare_loose_mode().
  AllTest.test_check_value_loose_mode_raises_value_error: AllTest#test_check_value_loose_mode_raises_value_error().
  AllTest.test_compute_optimal_tolerances_case1_expected_le_1: AllTest#test_compute_optimal_tolerances_case1_expected_le_1().
  AllTest.test_compute_optimal_tolerances_case2_expected_gt_1: AllTest#test_compute_optimal_tolerances_case2_expected_gt_1().
  AllTest.test_compute_optimal_tolerances_mixed_and_zero: AllTest#test_compute_optimal_tolerances_mixed_and_zero().
  AllTest.test_compute_optimal_tolerances_boundary_exact_one: AllTest#test_compute_optimal_tolerances_boundary_exact_one().
  AllTest.test_compute_optimal_tolerances_bfloat16_precision: AllTest#test_compute_optimal_tolerances_bfloat16_precision().
  AllTest.test_compute_optimal_tolerances_unmatched_nan_handling: AllTest#test_compute_optimal_tolerances_unmatched_nan_handling().
  AllTest.test_compute_optimal_tolerances_matching_nan_handling: AllTest#test_compute_optimal_tolerances_matching_nan_handling().
  AllTest.test_compute_optimal_tolerances_upward_rounding: AllTest#test_compute_optimal_tolerances_upward_rounding().
  AllTest.test_compute_optimal_tolerances_inf_handling: AllTest#test_compute_optimal_tolerances_inf_handling().
  AllTest.test_compute_optimal_tolerances_multi_run: AllTest#test_compute_optimal_tolerances_multi_run().
  AllTest.test_compute_optimal_tolerances_sequence_nan_propagation: AllTest#test_compute_optimal_tolerances_sequence_nan_propagation().
  AllTest.test_compute_optimal_tolerances_multi_run_nan_propagation: AllTest#test_compute_optimal_tolerances_multi_run_nan_propagation().
  AllTest.test_compute_optimal_tolerances_sequence_mismatch: AllTest#test_compute_optimal_tolerances_sequence_mismatch().
  AllTest.test_model_shlo_dyn.AddModule.forward: AllTest#test_model_shlo_dyn().AddModule#forward().
  AllTest.test_model_shlo.RoundModule.forward: AllTest#test_model_shlo().RoundModule#forward().
  AllTest.test_input_metadata: AllTest#test_input_metadata().
  AllTest.test_format_tensor: AllTest#test_format_tensor().
  AllTest.test_print_multiple_tensor_inputs.MultiModule.forward: AllTest#test_print_multiple_tensor_inputs().MultiModule#forward().
  AllTest.test_op_tracer_as_context_manager: AllTest#test_op_tracer_as_context_manager().
  AllTest.test_aten_count.MultiModule.forward: AllTest#test_aten_count().MultiModule#forward().
  AllTest.test_print_tensor_summary: AllTest#test_print_tensor_summary().
  AllTest.test_print_tensor_summary_on_empty_tensor: AllTest#test_print_tensor_summary_on_empty_tensor().
  AllTest.test_print_tensor_summary_no_data: AllTest#test_print_tensor_summary_no_data().
  AllTest.test_get_primary_tensor_output: AllTest#test_get_primary_tensor_output().
  AllTest.test_get_primary_tensor_output.DummyWithLogits.__init__: AllTest#test_get_primary_tensor_output().DummyWithLogits#__init__().
  AllTest.test_get_primary_tensor_output.DummyWithLastHiddenState.__init__: AllTest#test_get_primary_tensor_output().DummyWithLastHiddenState#__init__().
  AllTest.test_get_primary_tensor_output.DummyWithSample.__init__: AllTest#test_get_primary_tensor_output().DummyWithSample#__init__().
  AllTest.test_get_primary_tensor_output.DummyWithWaveform.__init__: AllTest#test_get_primary_tensor_output().DummyWithWaveform#__init__().
  AllTest.test_get_primary_tensor_output.DummyWithAudio.__init__: AllTest#test_get_primary_tensor_output().DummyWithAudio#__init__().
  AllTest.test_get_primary_tensor_output.DummyWithSequences.__init__: AllTest#test_get_primary_tensor_output().DummyWithSequences#__init__().
  AllTest.test_get_primary_tensor_output.DummyWithLossAndLogits.__init__: AllTest#test_get_primary_tensor_output().DummyWithLossAndLogits#__init__().
  DummyWithLossAndLogits.loss: DummyWithLossAndLogits#loss.
  AllTest.test_get_torch_version: AllTest#test_get_torch_version().
---
# Module: [`src/torch_tpu/_internal/utils/utils_test.py`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils_test.py)

> **Collapsed catalog** (79 symbols) — one row per symbol with its source line; member detail omitted. See the source link above, or the curated codebase page, for depth.

- <a id="AllTest"></a>`AllTest` — [`L84`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils_test.py#L84)
- <a id="AllTest.assert_events_equal"></a>`AllTest.assert_events_equal` — [`L481`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils_test.py#L481)
- <a id="AllTest.assert_logs_equal"></a>`AllTest.assert_logs_equal` — [`L462`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils_test.py#L462)
- <a id="AllTest.device"></a>`AllTest.device` — [`L89`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils_test.py#L89)
- <a id="AllTest.f"></a>`AllTest.f` — [`L387`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils_test.py#L387)
- <a id="AllTest.foo"></a>`AllTest.foo` — [`L301`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils_test.py#L301)
- <a id="AllTest.setUp"></a>`AllTest.setUp` — [`L87`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils_test.py#L87)
- <a id="AllTest.test_activation_tracer_on_complex_module_backward_call_creates_log"></a>`AllTest.test_activation_tracer_on_complex_module_backward_call_creates_log` — [`L670`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils_test.py#L670)
- <a id="AllTest.test_activation_tracer_on_complex_module_creates_log"></a>`AllTest.test_activation_tracer_on_complex_module_creates_log` — [`L558`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils_test.py#L558)
- <a id="AllTest.test_activation_tracer_on_one_child_module_backward_call_creates_log"></a>`AllTest.test_activation_tracer_on_one_child_module_backward_call_creates_log` — [`L634`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils_test.py#L634)
- <a id="AllTest.test_activation_tracer_on_one_child_module_creates_log"></a>`AllTest.test_activation_tracer_on_one_child_module_creates_log` — [`L534`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils_test.py#L534)
- <a id="AllTest.test_activation_tracer_on_zero_child_module_backward_call_creates_log"></a>`AllTest.test_activation_tracer_on_zero_child_module_backward_call_creates_log` — [`L612`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils_test.py#L612)
- <a id="AllTest.test_activation_tracer_on_zero_child_module_creates_log"></a>`AllTest.test_activation_tracer_on_zero_child_module_creates_log` — [`L517`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils_test.py#L517)
- <a id="AllTest.test_assert_close_with_callable_atol_failure"></a>`AllTest.test_assert_close_with_callable_atol_failure` — [`L274`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils_test.py#L274)
- <a id="AllTest.test_assert_close_with_callable_atol_success"></a>`AllTest.test_assert_close_with_callable_atol_success` — [`L267`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils_test.py#L267)
- <a id="AllTest.test_aten_count"></a>`AllTest.test_aten_count` — [`L420`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils_test.py#L420)
- <a id="AllTest.test_aten_count.MultiModule"></a>`AllTest.test_aten_count.MultiModule` — [`L423`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils_test.py#L423)
- <a id="AllTest.test_aten_count.MultiModule.forward"></a>`AllTest.test_aten_count.MultiModule.forward` — [`L425`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils_test.py#L425)
- <a id="AllTest.test_check_value_loose_mode_raises_value_error"></a>`AllTest.test_check_value_loose_mode_raises_value_error` — [`L128`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils_test.py#L128)
- <a id="AllTest.test_compare_loose_mode"></a>`AllTest.test_compare_loose_mode` — [`L111`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils_test.py#L111)
- <a id="AllTest.test_compare_strict_mode"></a>`AllTest.test_compare_strict_mode` — [`L91`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils_test.py#L91)
- <a id="AllTest.test_compute_optimal_tolerances_bfloat16_precision"></a>`AllTest.test_compute_optimal_tolerances_bfloat16_precision` — [`L170`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils_test.py#L170)
- <a id="AllTest.test_compute_optimal_tolerances_boundary_exact_one"></a>`AllTest.test_compute_optimal_tolerances_boundary_exact_one` — [`L162`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils_test.py#L162)
- <a id="AllTest.test_compute_optimal_tolerances_case1_expected_le_1"></a>`AllTest.test_compute_optimal_tolerances_case1_expected_le_1` — [`L137`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils_test.py#L137)
- <a id="AllTest.test_compute_optimal_tolerances_case2_expected_gt_1"></a>`AllTest.test_compute_optimal_tolerances_case2_expected_gt_1` — [`L145`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils_test.py#L145)
- <a id="AllTest.test_compute_optimal_tolerances_inf_handling"></a>`AllTest.test_compute_optimal_tolerances_inf_handling` — [`L204`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils_test.py#L204)
- <a id="AllTest.test_compute_optimal_tolerances_matching_nan_handling"></a>`AllTest.test_compute_optimal_tolerances_matching_nan_handling` — [`L186`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils_test.py#L186)
- <a id="AllTest.test_compute_optimal_tolerances_mixed_and_zero"></a>`AllTest.test_compute_optimal_tolerances_mixed_and_zero` — [`L153`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils_test.py#L153)
- <a id="AllTest.test_compute_optimal_tolerances_multi_run"></a>`AllTest.test_compute_optimal_tolerances_multi_run` — [`L211`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils_test.py#L211)
- <a id="AllTest.test_compute_optimal_tolerances_multi_run_nan_propagation"></a>`AllTest.test_compute_optimal_tolerances_multi_run_nan_propagation` — [`L231`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils_test.py#L231)
- <a id="AllTest.test_compute_optimal_tolerances_sequence_mismatch"></a>`AllTest.test_compute_optimal_tolerances_sequence_mismatch` — [`L244`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils_test.py#L244)
- <a id="AllTest.test_compute_optimal_tolerances_sequence_nan_propagation"></a>`AllTest.test_compute_optimal_tolerances_sequence_nan_propagation` — [`L224`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils_test.py#L224)
- <a id="AllTest.test_compute_optimal_tolerances_unmatched_nan_handling"></a>`AllTest.test_compute_optimal_tolerances_unmatched_nan_handling` — [`L179`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils_test.py#L179)
- <a id="AllTest.test_compute_optimal_tolerances_upward_rounding"></a>`AllTest.test_compute_optimal_tolerances_upward_rounding` — [`L194`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils_test.py#L194)
- <a id="AllTest.test_format_tensor"></a>`AllTest.test_format_tensor` — [`L352`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils_test.py#L352)
- <a id="AllTest.test_function_list_inputs"></a>`AllTest.test_function_list_inputs` — [`L315`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils_test.py#L315)
- <a id="AllTest.test_function_shlo"></a>`AllTest.test_function_shlo` — [`L300`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils_test.py#L300)
- <a id="AllTest.test_get_primary_tensor_output"></a>`AllTest.test_get_primary_tensor_output` — [`L725`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils_test.py#L725)
- <a id="AllTest.test_get_primary_tensor_output.DummyWithAudio"></a>`AllTest.test_get_primary_tensor_output.DummyWithAudio` — [`L761`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils_test.py#L761)
- <a id="AllTest.test_get_primary_tensor_output.DummyWithAudio.__init__"></a>`AllTest.test_get_primary_tensor_output.DummyWithAudio.__init__` — [`L763`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils_test.py#L763)
- <a id="AllTest.test_get_primary_tensor_output.DummyWithLastHiddenState"></a>`AllTest.test_get_primary_tensor_output.DummyWithLastHiddenState` — [`L738`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils_test.py#L738)
- <a id="AllTest.test_get_primary_tensor_output.DummyWithLastHiddenState.__init__"></a>`AllTest.test_get_primary_tensor_output.DummyWithLastHiddenState.__init__` — [`L740`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils_test.py#L740)
- <a id="AllTest.test_get_primary_tensor_output.DummyWithLogits"></a>`AllTest.test_get_primary_tensor_output.DummyWithLogits` — [`L731`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils_test.py#L731)
- <a id="AllTest.test_get_primary_tensor_output.DummyWithLogits.__init__"></a>`AllTest.test_get_primary_tensor_output.DummyWithLogits.__init__` — [`L733`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils_test.py#L733)
- <a id="AllTest.test_get_primary_tensor_output.DummyWithLossAndLogits"></a>`AllTest.test_get_primary_tensor_output.DummyWithLossAndLogits` — [`L775`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils_test.py#L775)
- <a id="AllTest.test_get_primary_tensor_output.DummyWithLossAndLogits.__init__"></a>`AllTest.test_get_primary_tensor_output.DummyWithLossAndLogits.__init__` — [`L777`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils_test.py#L777)
- <a id="AllTest.test_get_primary_tensor_output.DummyWithSample"></a>`AllTest.test_get_primary_tensor_output.DummyWithSample` — [`L747`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils_test.py#L747)
- <a id="AllTest.test_get_primary_tensor_output.DummyWithSample.__init__"></a>`AllTest.test_get_primary_tensor_output.DummyWithSample.__init__` — [`L749`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils_test.py#L749)
- <a id="AllTest.test_get_primary_tensor_output.DummyWithSequences"></a>`AllTest.test_get_primary_tensor_output.DummyWithSequences` — [`L768`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils_test.py#L768)
- <a id="AllTest.test_get_primary_tensor_output.DummyWithSequences.__init__"></a>`AllTest.test_get_primary_tensor_output.DummyWithSequences.__init__` — [`L770`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils_test.py#L770)
- <a id="AllTest.test_get_primary_tensor_output.DummyWithWaveform"></a>`AllTest.test_get_primary_tensor_output.DummyWithWaveform` — [`L754`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils_test.py#L754)
- <a id="AllTest.test_get_primary_tensor_output.DummyWithWaveform.__init__"></a>`AllTest.test_get_primary_tensor_output.DummyWithWaveform.__init__` — [`L756`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils_test.py#L756)
- <a id="AllTest.test_get_torch_version"></a>`AllTest.test_get_torch_version` — [`L811`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils_test.py#L811)
- <a id="AllTest.test_input_metadata"></a>`AllTest.test_input_metadata` — [`L327`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils_test.py#L327)
- <a id="AllTest.test_model_shlo"></a>`AllTest.test_model_shlo` — [`L282`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils_test.py#L282)
- <a id="AllTest.test_model_shlo.RoundModule"></a>`AllTest.test_model_shlo.RoundModule` — [`L283`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils_test.py#L283)
- <a id="AllTest.test_model_shlo.RoundModule.forward"></a>`AllTest.test_model_shlo.RoundModule.forward` — [`L285`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils_test.py#L285)
- <a id="AllTest.test_model_shlo_dyn"></a>`AllTest.test_model_shlo_dyn` — [`L250`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils_test.py#L250)
- <a id="AllTest.test_model_shlo_dyn.AddModule"></a>`AllTest.test_model_shlo_dyn.AddModule` — [`L252`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils_test.py#L252)
- <a id="AllTest.test_model_shlo_dyn.AddModule.forward"></a>`AllTest.test_model_shlo_dyn.AddModule.forward` — [`L254`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils_test.py#L254)
- <a id="AllTest.test_op_tracer_as_context_manager"></a>`AllTest.test_op_tracer_as_context_manager` — [`L410`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils_test.py#L410)
- <a id="AllTest.test_op_tracer_as_decorator"></a>`AllTest.test_op_tracer_as_decorator` — [`L382`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils_test.py#L382)
- <a id="AllTest.test_op_tracer_as_wrapper"></a>`AllTest.test_op_tracer_as_wrapper` — [`L396`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils_test.py#L396)
- <a id="AllTest.test_print_multiple_tensor_inputs"></a>`AllTest.test_print_multiple_tensor_inputs` — [`L370`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils_test.py#L370)
- <a id="AllTest.test_print_multiple_tensor_inputs.MultiModule"></a>`AllTest.test_print_multiple_tensor_inputs.MultiModule` — [`L371`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils_test.py#L371)
- <a id="AllTest.test_print_multiple_tensor_inputs.MultiModule.forward"></a>`AllTest.test_print_multiple_tensor_inputs.MultiModule.forward` — [`L373`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils_test.py#L373)
- <a id="AllTest.test_print_tensor_summary"></a>`AllTest.test_print_tensor_summary` — [`L437`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils_test.py#L437)
- <a id="AllTest.test_print_tensor_summary_no_data"></a>`AllTest.test_print_tensor_summary_no_data` — [`L452`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils_test.py#L452)
- <a id="AllTest.test_print_tensor_summary_on_empty_tensor"></a>`AllTest.test_print_tensor_summary_on_empty_tensor` — [`L446`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils_test.py#L446)
- <a id="DummyWithAudio.audio"></a>`DummyWithAudio.audio` — [`L764`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils_test.py#L764)
- <a id="DummyWithLastHiddenState.last_hidden_state"></a>`DummyWithLastHiddenState.last_hidden_state` — [`L741`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils_test.py#L741)
- <a id="DummyWithLogits.logits"></a>`DummyWithLogits.logits` — [`L734`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils_test.py#L734)
- <a id="DummyWithLossAndLogits.logits"></a>`DummyWithLossAndLogits.logits` — [`L779`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils_test.py#L779)
- <a id="DummyWithLossAndLogits.loss"></a>`DummyWithLossAndLogits.loss` — [`L778`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils_test.py#L778)
- <a id="DummyWithSample.sample"></a>`DummyWithSample.sample` — [`L750`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils_test.py#L750)
- <a id="DummyWithSequences.sequences"></a>`DummyWithSequences.sequences` — [`L771`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils_test.py#L771)
- <a id="DummyWithWaveform.waveform"></a>`DummyWithWaveform.waveform` — [`L757`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils_test.py#L757)
- <a id="bwd"></a>`bwd` — [`L53`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils_test.py#L53)
- <a id="fwd"></a>`fwd` — [`L28`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils_test.py#L28)
