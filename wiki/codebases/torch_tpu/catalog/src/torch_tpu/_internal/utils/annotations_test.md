---
title: 'Module: src/torch_tpu/_internal/utils/annotations_test.py'
type: catalog
provenance: extracted
module: src/torch_tpu/_internal/utils/annotations_test.py
status: fresh
symbol_base: scip-python python torch_tpu 0.0.0 `src.torch_tpu._internal.utils.annotations_test`/
symbols:
  AnnotationsTest.sample_func: AnnotationsTest#sample_func().
  internal_or_experimental: internal_or_experimental.
  experimental: experimental.
  AnnotationsTest.forbidden: AnnotationsTest#forbidden().
  AnnotationsTest.test_explicit_class_member_decoration: AnnotationsTest#test_explicit_class_member_decoration().
  AnnotationsTest.test_experimental_enum_class_metadata_and_members.SampleEnum.BAR: AnnotationsTest#test_experimental_enum_class_metadata_and_members().SampleEnum#BAR.
  SampleClass.x: SampleClass#x.
  AnnotationsTest.legacy_func: AnnotationsTest#legacy_func().
  AnnotationsTest.test_experimental_class_metadata_and_warning.SampleClass: AnnotationsTest#test_experimental_class_metadata_and_warning().SampleClass#
  AnnotationsTest.test_experimental_enum_class_metadata_and_members.SampleEnum: AnnotationsTest#test_experimental_enum_class_metadata_and_members().SampleEnum#
  AnnotationsTest.test_internal_function_silent_for_framework_callers: AnnotationsTest#test_internal_function_silent_for_framework_callers().
  AnnotationsTest.test_explicit_class_member_decoration.ServiceClass: AnnotationsTest#test_explicit_class_member_decoration().ServiceClass#
  AnnotationsTest.test_internal_class_raises_for_user_caller.SampleClass: AnnotationsTest#test_internal_class_raises_for_user_caller().SampleClass#
  AnnotationsTest.stable_func: AnnotationsTest#stable_func().
  AnnotationsTest.test_deprecated_class_metadata_and_warning.LegacyClass: AnnotationsTest#test_deprecated_class_metadata_and_warning().LegacyClass#
  AnnotationsTest.exp_func: AnnotationsTest#exp_func().
  deprecated: deprecated.
  forbid_in_torch_compile: forbid_in_torch_compile.
  AnnotationsTest.test_experimental_multiple_functions_independent_warnings: AnnotationsTest#test_experimental_multiple_functions_independent_warnings().
  AnnotationsTest.dummy_one: AnnotationsTest#dummy_one().
  AnnotationsTest.dummy_two: AnnotationsTest#dummy_two().
  AnnotationsTest.test_experimental_class_metadata_and_warning: AnnotationsTest#test_experimental_class_metadata_and_warning().
  AnnotationsTest.test_stage_warning_from_user_getattr: AnnotationsTest#test_stage_warning_from_user_getattr().
  AnnotationsTest.mock_module_getattr: AnnotationsTest#mock_module_getattr().
  AnnotationsTest.test_attach_stage_metadata_with_func_target: AnnotationsTest#test_attach_stage_metadata_with_func_target().
  AnnotationsTest._call_from_module: AnnotationsTest#_call_from_module().
  AnnotationsTest.test_warning_suppressed_for_framework_callers: AnnotationsTest#test_warning_suppressed_for_framework_callers().
  AnnotationsTest.test_non_strict_internal_class_warns_for_user_caller.SampleClass: AnnotationsTest#test_non_strict_internal_class_warns_for_user_caller().SampleClass#
  AnnotationsTest.calculate: AnnotationsTest#calculate().
  AnnotationsTest.func_one: AnnotationsTest#func_one().
  AnnotationsTest.func_two: AnnotationsTest#func_two().
  AnnotationsTest.test_experimental_class_metadata_and_warning.SampleClass.unannotated_method: AnnotationsTest#test_experimental_class_metadata_and_warning().SampleClass#unannotated_method().
  AnnotationsTest.test_explicit_class_member_decoration.ServiceClass.experimental_method: AnnotationsTest#test_explicit_class_member_decoration().ServiceClass#experimental_method().
  AnnotationsTest.test_explicit_class_member_decoration.ServiceClass.legacy_method: AnnotationsTest#test_explicit_class_member_decoration().ServiceClass#legacy_method().
  AnnotationsTest.test_forbid_in_torch_compile_class_raises_only_when_compiled.Forbidden: AnnotationsTest#test_forbid_in_torch_compile_class_raises_only_when_compiled().Forbidden#
  _reset_warn_once: _reset_warn_once().
  AnnotationsTest.test_experimental_first_call_triggers_warning: AnnotationsTest#test_experimental_first_call_triggers_warning().
  AnnotationsTest.test_experimental_subsequent_calls_suppress_warning: AnnotationsTest#test_experimental_subsequent_calls_suppress_warning().
  AnnotationsTest.test_experimental_function_traces_under_torch_compile: AnnotationsTest#test_experimental_function_traces_under_torch_compile().
  AnnotationsTest.test_stable_metadata_no_warning: AnnotationsTest#test_stable_metadata_no_warning().
  AnnotationsTest.test_deprecated_metadata_and_warning: AnnotationsTest#test_deprecated_metadata_and_warning().
  AnnotationsTest.test_deprecated_class_metadata_and_warning: AnnotationsTest#test_deprecated_class_metadata_and_warning().
  AnnotationsTest.test_real_api_stream_context_warns_once_without_internal_warnings: AnnotationsTest#test_real_api_stream_context_warns_once_without_internal_warnings().
  AnnotationsTest.test_pep562_module_getattr_resolution_and_suppression: AnnotationsTest#test_pep562_module_getattr_resolution_and_suppression().
  AnnotationsTest.test_internal_or_experimental_is_experimental_when_not_internal: AnnotationsTest#test_internal_or_experimental_is_experimental_when_not_internal().
  AnnotationsTest.test_internal_or_experimental_internal_function_metadata: AnnotationsTest#test_internal_or_experimental_internal_function_metadata().
  AnnotationsTest.test_internal_function_raises_for_user_caller: AnnotationsTest#test_internal_function_raises_for_user_caller().
  AnnotationsTest.test_internal_function_without_prefer_raises: AnnotationsTest#test_internal_function_without_prefer_raises().
  AnnotationsTest.test_non_strict_internal_function_warns_once_for_user_caller: AnnotationsTest#test_non_strict_internal_function_warns_once_for_user_caller().
  AnnotationsTest.test_non_strict_internal_function_without_prefer_warns: AnnotationsTest#test_non_strict_internal_function_without_prefer_warns().
  AnnotationsTest.test_internal_or_experimental_is_experimental_when_not_internal_and_strict: AnnotationsTest#test_internal_or_experimental_is_experimental_when_not_internal_and_strict().
  AnnotationsTest.test_internal_apis_allowed_for_testing: AnnotationsTest#test_internal_apis_allowed_for_testing().
  AnnotationsTest.test_internal_or_experimental_validates_arguments: AnnotationsTest#test_internal_or_experimental_validates_arguments().
  AnnotationsTest.test_internal_function_traces_under_torch_compile: AnnotationsTest#test_internal_function_traces_under_torch_compile().
  AnnotationsTest.test_real_api_internal_device_count_raises: AnnotationsTest#test_real_api_internal_device_count_raises().
  AnnotationsTest.test_forbid_in_torch_compile_function_raises_only_when_compiled: AnnotationsTest#test_forbid_in_torch_compile_function_raises_only_when_compiled().
  AnnotationsTest.test_forbid_in_torch_compile_class_raises_only_when_compiled: AnnotationsTest#test_forbid_in_torch_compile_class_raises_only_when_compiled().
  AnnotationsTest.test_forbid_in_torch_compile_appends_docstring: AnnotationsTest#test_forbid_in_torch_compile_appends_docstring().
  AnnotationsTest.test_forbid_in_torch_compile_without_docstring: AnnotationsTest#test_forbid_in_torch_compile_without_docstring().
  AnnotationsTest.test_forbid_in_torch_compile_invalid_reason_raises: AnnotationsTest#test_forbid_in_torch_compile_invalid_reason_raises().
  stable: stable.
  AnnotationsTest.test_experimental_enum_class_metadata_and_members.SampleEnum.FOO: AnnotationsTest#test_experimental_enum_class_metadata_and_members().SampleEnum#FOO.
  AnnotationsTest.test_stage_warning_from_user_getattr.UserModule: AnnotationsTest#test_stage_warning_from_user_getattr().UserModule#
  SampleClass.val: SampleClass#val.
  AnnotationsTest.test_explicit_class_member_decoration.ServiceClass.unannotated_method: AnnotationsTest#test_explicit_class_member_decoration().ServiceClass#unannotated_method().
  AnnotationsTest.test_stage_warning_from_user_getattr.UserModule.__getattr__: AnnotationsTest#test_stage_warning_from_user_getattr().UserModule#__getattr__().
  AnnotationsTest.test_attach_stage_metadata_with_func_target.SampleClass: AnnotationsTest#test_attach_stage_metadata_with_func_target().SampleClass#
  AnnotationsTest.test_attach_stage_metadata_with_func_target.SampleClass.sample_classmethod: AnnotationsTest#test_attach_stage_metadata_with_func_target().SampleClass#sample_classmethod().
  AnnotationsTest: AnnotationsTest#
  AnnotationsTest.test_stage_enum: AnnotationsTest#test_stage_enum().
  AnnotationsTest.test_experimental_invalid_reason_raises: AnnotationsTest#test_experimental_invalid_reason_raises().
  AnnotationsTest.test_deprecated_invalid_args_raises: AnnotationsTest#test_deprecated_invalid_args_raises().
  AnnotationsTest.test_experimental_class_metadata_and_warning.SampleClass.__init__: AnnotationsTest#test_experimental_class_metadata_and_warning().SampleClass#__init__().
  AnnotationsTest.test_deprecated_class_metadata_and_warning.LegacyClass.__init__: AnnotationsTest#test_deprecated_class_metadata_and_warning().LegacyClass#__init__().
  AnnotationsTest.test_experimental_enum_class_metadata_and_members: AnnotationsTest#test_experimental_enum_class_metadata_and_members().
  AnnotationsTest.test_annotated_real_api_get_amp_supported_dtype: AnnotationsTest#test_annotated_real_api_get_amp_supported_dtype().
  AnnotationsTest.test_annotated_real_api_initial_seed: AnnotationsTest#test_annotated_real_api_initial_seed().
  AnnotationsTest.test_annotated_real_api_manual_seed: AnnotationsTest#test_annotated_real_api_manual_seed().
  AnnotationsTest.test_annotated_real_enum_class_api_precision: AnnotationsTest#test_annotated_real_enum_class_api_precision().
  AnnotationsTest.test_annotated_real_api_property_default_generators: AnnotationsTest#test_annotated_real_api_property_default_generators().
  AnnotationsTest.test_static_class_attributes_bypass_getattr_and_warnings: AnnotationsTest#test_static_class_attributes_bypass_getattr_and_warnings().
  AnnotationsTest.test_annotated_real_api_enum_class_precision: AnnotationsTest#test_annotated_real_api_enum_class_precision().
  AnnotationsTest.test_annotated_real_api_property_allow_excess_precision: AnnotationsTest#test_annotated_real_api_property_allow_excess_precision().
  AnnotationsTest.test_internal_class_raises_for_user_caller: AnnotationsTest#test_internal_class_raises_for_user_caller().
  AnnotationsTest.test_internal_class_raises_for_user_caller.SampleClass.__init__: AnnotationsTest#test_internal_class_raises_for_user_caller().SampleClass#__init__().
  AnnotationsTest.test_non_strict_internal_class_warns_for_user_caller: AnnotationsTest#test_non_strict_internal_class_warns_for_user_caller().
  AnnotationsTest.test_non_strict_internal_class_warns_for_user_caller.SampleClass.__init__: AnnotationsTest#test_non_strict_internal_class_warns_for_user_caller().SampleClass#__init__().
  AnnotationsTest.test_parse_version: AnnotationsTest#test_parse_version().
  AnnotationsTest.test_device_module_apis_with_torch_accelerator_equivalents: AnnotationsTest#test_device_module_apis_with_torch_accelerator_equivalents().
  AnnotationsTest.test_real_api_torch_accelerator_set_stream_works: AnnotationsTest#test_real_api_torch_accelerator_set_stream_works().
  AnnotationsTest.test_forbid_in_torch_compile_class_raises_only_when_compiled.Forbidden.__enter__: AnnotationsTest#test_forbid_in_torch_compile_class_raises_only_when_compiled().Forbidden#__enter__().
  AnnotationsTest.test_forbid_in_torch_compile_class_raises_only_when_compiled.Forbidden.__exit__: AnnotationsTest#test_forbid_in_torch_compile_class_raises_only_when_compiled().Forbidden#__exit__().
---
# Module: [`src/torch_tpu/_internal/utils/annotations_test.py`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations_test.py)

> **Collapsed catalog** (92 symbols) — one row per symbol with its source line; member detail omitted. See the source link above, or the curated codebase page, for depth.

- <a id="AnnotationsTest"></a>`AnnotationsTest` — [`L54`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations_test.py#L54)
- <a id="AnnotationsTest._call_from_module"></a>`AnnotationsTest._call_from_module` — [`L668`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations_test.py#L668)
- <a id="AnnotationsTest.calculate"></a>`AnnotationsTest.calculate` — [`L1176`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations_test.py#L1176)
- <a id="AnnotationsTest.dummy_one"></a>`AnnotationsTest.dummy_one` — [`L213`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations_test.py#L213)
- <a id="AnnotationsTest.dummy_two"></a>`AnnotationsTest.dummy_two` — [`L219`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations_test.py#L219)
- <a id="AnnotationsTest.exp_func"></a>`AnnotationsTest.exp_func` — [`L679`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations_test.py#L679)
- <a id="AnnotationsTest.forbidden"></a>`AnnotationsTest.forbidden` — [`L1152`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations_test.py#L1152)
- <a id="AnnotationsTest.func_one"></a>`AnnotationsTest.func_one` — [`L141`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations_test.py#L141)
- <a id="AnnotationsTest.func_two"></a>`AnnotationsTest.func_two` — [`L145`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations_test.py#L145)
- <a id="AnnotationsTest.legacy_func"></a>`AnnotationsTest.legacy_func` — [`L181`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations_test.py#L181)
- <a id="AnnotationsTest.mock_module_getattr"></a>`AnnotationsTest.mock_module_getattr` — [`L589`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations_test.py#L589)
- <a id="AnnotationsTest.sample_func"></a>`AnnotationsTest.sample_func` — [`L75`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations_test.py#L75)
- <a id="AnnotationsTest.stable_func"></a>`AnnotationsTest.stable_func` — [`L163`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations_test.py#L163)
- <a id="AnnotationsTest.test_annotated_real_api_enum_class_precision"></a>`AnnotationsTest.test_annotated_real_api_enum_class_precision` — [`L470`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations_test.py#L470)
- <a id="AnnotationsTest.test_annotated_real_api_get_amp_supported_dtype"></a>`AnnotationsTest.test_annotated_real_api_get_amp_supported_dtype` — [`L368`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations_test.py#L368)
- <a id="AnnotationsTest.test_annotated_real_api_initial_seed"></a>`AnnotationsTest.test_annotated_real_api_initial_seed` — [`L380`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations_test.py#L380)
- <a id="AnnotationsTest.test_annotated_real_api_manual_seed"></a>`AnnotationsTest.test_annotated_real_api_manual_seed` — [`L395`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations_test.py#L395)
- <a id="AnnotationsTest.test_annotated_real_api_property_allow_excess_precision"></a>`AnnotationsTest.test_annotated_real_api_property_allow_excess_precision` — [`L537`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations_test.py#L537)
- <a id="AnnotationsTest.test_annotated_real_api_property_default_generators"></a>`AnnotationsTest.test_annotated_real_api_property_default_generators` — [`L428`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations_test.py#L428)
- <a id="AnnotationsTest.test_annotated_real_enum_class_api_precision"></a>`AnnotationsTest.test_annotated_real_enum_class_api_precision` — [`L407`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations_test.py#L407)
- <a id="AnnotationsTest.test_attach_stage_metadata_with_func_target"></a>`AnnotationsTest.test_attach_stage_metadata_with_func_target` — [`L634`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations_test.py#L634)
- <a id="AnnotationsTest.test_attach_stage_metadata_with_func_target.SampleClass"></a>`AnnotationsTest.test_attach_stage_metadata_with_func_target.SampleClass` — [`L637`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations_test.py#L637)
- <a id="AnnotationsTest.test_attach_stage_metadata_with_func_target.SampleClass.sample_classmethod"></a>`AnnotationsTest.test_attach_stage_metadata_with_func_target.SampleClass.sample_classmethod` — [`L640`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations_test.py#L640)
- <a id="AnnotationsTest.test_deprecated_class_metadata_and_warning"></a>`AnnotationsTest.test_deprecated_class_metadata_and_warning` — [`L275`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations_test.py#L275)
- <a id="AnnotationsTest.test_deprecated_class_metadata_and_warning.LegacyClass"></a>`AnnotationsTest.test_deprecated_class_metadata_and_warning.LegacyClass` — [`L279`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations_test.py#L279)
- <a id="AnnotationsTest.test_deprecated_class_metadata_and_warning.LegacyClass.__init__"></a>`AnnotationsTest.test_deprecated_class_metadata_and_warning.LegacyClass.__init__` — [`L281`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations_test.py#L281)
- <a id="AnnotationsTest.test_deprecated_invalid_args_raises"></a>`AnnotationsTest.test_deprecated_invalid_args_raises` — [`L222`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations_test.py#L222)
- <a id="AnnotationsTest.test_deprecated_metadata_and_warning"></a>`AnnotationsTest.test_deprecated_metadata_and_warning` — [`L177`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations_test.py#L177)
- <a id="AnnotationsTest.test_device_module_apis_with_torch_accelerator_equivalents"></a>`AnnotationsTest.test_device_module_apis_with_torch_accelerator_equivalents` — [`L1092`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations_test.py#L1092)
- <a id="AnnotationsTest.test_experimental_class_metadata_and_warning"></a>`AnnotationsTest.test_experimental_class_metadata_and_warning` — [`L240`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations_test.py#L240)
- <a id="AnnotationsTest.test_experimental_class_metadata_and_warning.SampleClass"></a>`AnnotationsTest.test_experimental_class_metadata_and_warning.SampleClass` — [`L244`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations_test.py#L244)
- <a id="AnnotationsTest.test_experimental_class_metadata_and_warning.SampleClass.__init__"></a>`AnnotationsTest.test_experimental_class_metadata_and_warning.SampleClass.__init__` — [`L246`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations_test.py#L246)
- <a id="AnnotationsTest.test_experimental_class_metadata_and_warning.SampleClass.unannotated_method"></a>`AnnotationsTest.test_experimental_class_metadata_and_warning.SampleClass.unannotated_method` — [`L249`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations_test.py#L249)
- <a id="AnnotationsTest.test_experimental_enum_class_metadata_and_members"></a>`AnnotationsTest.test_experimental_enum_class_metadata_and_members` — [`L341`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations_test.py#L341)
- <a id="AnnotationsTest.test_experimental_enum_class_metadata_and_members.SampleEnum"></a>`AnnotationsTest.test_experimental_enum_class_metadata_and_members.SampleEnum` — [`L345`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations_test.py#L345)
- <a id="AnnotationsTest.test_experimental_enum_class_metadata_and_members.SampleEnum.BAR"></a>`AnnotationsTest.test_experimental_enum_class_metadata_and_members.SampleEnum.BAR` — [`L347`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations_test.py#L347)
- <a id="AnnotationsTest.test_experimental_enum_class_metadata_and_members.SampleEnum.FOO"></a>`AnnotationsTest.test_experimental_enum_class_metadata_and_members.SampleEnum.FOO` — [`L346`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations_test.py#L346)
- <a id="AnnotationsTest.test_experimental_first_call_triggers_warning"></a>`AnnotationsTest.test_experimental_first_call_triggers_warning` — [`L71`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations_test.py#L71)
- <a id="AnnotationsTest.test_experimental_function_traces_under_torch_compile"></a>`AnnotationsTest.test_experimental_function_traces_under_torch_compile` — [`L110`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations_test.py#L110)
- <a id="AnnotationsTest.test_experimental_invalid_reason_raises"></a>`AnnotationsTest.test_experimental_invalid_reason_raises` — [`L208`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations_test.py#L208)
- <a id="AnnotationsTest.test_experimental_multiple_functions_independent_warnings"></a>`AnnotationsTest.test_experimental_multiple_functions_independent_warnings` — [`L137`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations_test.py#L137)
- <a id="AnnotationsTest.test_experimental_subsequent_calls_suppress_warning"></a>`AnnotationsTest.test_experimental_subsequent_calls_suppress_warning` — [`L93`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations_test.py#L93)
- <a id="AnnotationsTest.test_explicit_class_member_decoration"></a>`AnnotationsTest.test_explicit_class_member_decoration` — [`L300`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations_test.py#L300)
- <a id="AnnotationsTest.test_explicit_class_member_decoration.ServiceClass"></a>`AnnotationsTest.test_explicit_class_member_decoration.ServiceClass` — [`L304`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations_test.py#L304)
- <a id="AnnotationsTest.test_explicit_class_member_decoration.ServiceClass.experimental_method"></a>`AnnotationsTest.test_explicit_class_member_decoration.ServiceClass.experimental_method` — [`L307`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations_test.py#L307)
- <a id="AnnotationsTest.test_explicit_class_member_decoration.ServiceClass.legacy_method"></a>`AnnotationsTest.test_explicit_class_member_decoration.ServiceClass.legacy_method` — [`L311`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations_test.py#L311)
- <a id="AnnotationsTest.test_explicit_class_member_decoration.ServiceClass.unannotated_method"></a>`AnnotationsTest.test_explicit_class_member_decoration.ServiceClass.unannotated_method` — [`L314`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations_test.py#L314)
- <a id="AnnotationsTest.test_forbid_in_torch_compile_appends_docstring"></a>`AnnotationsTest.test_forbid_in_torch_compile_appends_docstring` — [`L1188`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations_test.py#L1188)
- <a id="AnnotationsTest.test_forbid_in_torch_compile_class_raises_only_when_compiled"></a>`AnnotationsTest.test_forbid_in_torch_compile_class_raises_only_when_compiled` — [`L1164`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations_test.py#L1164)
- <a id="AnnotationsTest.test_forbid_in_torch_compile_class_raises_only_when_compiled.Forbidden"></a>`AnnotationsTest.test_forbid_in_torch_compile_class_raises_only_when_compiled.Forbidden` — [`L1168`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations_test.py#L1168)
- <a id="AnnotationsTest.test_forbid_in_torch_compile_class_raises_only_when_compiled.Forbidden.__enter__"></a>`AnnotationsTest.test_forbid_in_torch_compile_class_raises_only_when_compiled.Forbidden.__enter__` — [`L1170`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations_test.py#L1170)
- <a id="AnnotationsTest.test_forbid_in_torch_compile_class_raises_only_when_compiled.Forbidden.__exit__"></a>`AnnotationsTest.test_forbid_in_torch_compile_class_raises_only_when_compiled.Forbidden.__exit__` — [`L1173`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations_test.py#L1173)
- <a id="AnnotationsTest.test_forbid_in_torch_compile_function_raises_only_when_compiled"></a>`AnnotationsTest.test_forbid_in_torch_compile_function_raises_only_when_compiled` — [`L1148`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations_test.py#L1148)
- <a id="AnnotationsTest.test_forbid_in_torch_compile_invalid_reason_raises"></a>`AnnotationsTest.test_forbid_in_torch_compile_invalid_reason_raises` — [`L1219`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations_test.py#L1219)
- <a id="AnnotationsTest.test_forbid_in_torch_compile_without_docstring"></a>`AnnotationsTest.test_forbid_in_torch_compile_without_docstring` — [`L1206`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations_test.py#L1206)
- <a id="AnnotationsTest.test_internal_apis_allowed_for_testing"></a>`AnnotationsTest.test_internal_apis_allowed_for_testing` — [`L928`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations_test.py#L928)
- <a id="AnnotationsTest.test_internal_class_raises_for_user_caller"></a>`AnnotationsTest.test_internal_class_raises_for_user_caller` — [`L961`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations_test.py#L961)
- <a id="AnnotationsTest.test_internal_class_raises_for_user_caller.SampleClass"></a>`AnnotationsTest.test_internal_class_raises_for_user_caller.SampleClass` — [`L969`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations_test.py#L969)
- <a id="AnnotationsTest.test_internal_class_raises_for_user_caller.SampleClass.__init__"></a>`AnnotationsTest.test_internal_class_raises_for_user_caller.SampleClass.__init__` — [`L971`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations_test.py#L971)
- <a id="AnnotationsTest.test_internal_function_raises_for_user_caller"></a>`AnnotationsTest.test_internal_function_raises_for_user_caller` — [`L758`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations_test.py#L758)
- <a id="AnnotationsTest.test_internal_function_silent_for_framework_callers"></a>`AnnotationsTest.test_internal_function_silent_for_framework_callers` — [`L878`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations_test.py#L878)
- <a id="AnnotationsTest.test_internal_function_traces_under_torch_compile"></a>`AnnotationsTest.test_internal_function_traces_under_torch_compile` — [`L1043`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations_test.py#L1043)
- <a id="AnnotationsTest.test_internal_function_without_prefer_raises"></a>`AnnotationsTest.test_internal_function_without_prefer_raises` — [`L788`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations_test.py#L788)
- <a id="AnnotationsTest.test_internal_or_experimental_internal_function_metadata"></a>`AnnotationsTest.test_internal_or_experimental_internal_function_metadata` — [`L738`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations_test.py#L738)
- <a id="AnnotationsTest.test_internal_or_experimental_is_experimental_when_not_internal"></a>`AnnotationsTest.test_internal_or_experimental_is_experimental_when_not_internal` — [`L708`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations_test.py#L708)
- <a id="AnnotationsTest.test_internal_or_experimental_is_experimental_when_not_internal_and_strict"></a>`AnnotationsTest.test_internal_or_experimental_is_experimental_when_not_internal_and_strict` — [`L855`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations_test.py#L855)
- <a id="AnnotationsTest.test_internal_or_experimental_validates_arguments"></a>`AnnotationsTest.test_internal_or_experimental_validates_arguments` — [`L1022`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations_test.py#L1022)
- <a id="AnnotationsTest.test_non_strict_internal_class_warns_for_user_caller"></a>`AnnotationsTest.test_non_strict_internal_class_warns_for_user_caller` — [`L994`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations_test.py#L994)
- <a id="AnnotationsTest.test_non_strict_internal_class_warns_for_user_caller.SampleClass"></a>`AnnotationsTest.test_non_strict_internal_class_warns_for_user_caller.SampleClass` — [`L1003`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations_test.py#L1003)
- <a id="AnnotationsTest.test_non_strict_internal_class_warns_for_user_caller.SampleClass.__init__"></a>`AnnotationsTest.test_non_strict_internal_class_warns_for_user_caller.SampleClass.__init__` — [`L1005`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations_test.py#L1005)
- <a id="AnnotationsTest.test_non_strict_internal_function_warns_once_for_user_caller"></a>`AnnotationsTest.test_non_strict_internal_function_warns_once_for_user_caller` — [`L805`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations_test.py#L805)
- <a id="AnnotationsTest.test_non_strict_internal_function_without_prefer_warns"></a>`AnnotationsTest.test_non_strict_internal_function_without_prefer_warns` — [`L832`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations_test.py#L832)
- <a id="AnnotationsTest.test_parse_version"></a>`AnnotationsTest.test_parse_version` — [`L1081`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations_test.py#L1081)
- <a id="AnnotationsTest.test_pep562_module_getattr_resolution_and_suppression"></a>`AnnotationsTest.test_pep562_module_getattr_resolution_and_suppression` — [`L572`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations_test.py#L572)
- <a id="AnnotationsTest.test_real_api_internal_device_count_raises"></a>`AnnotationsTest.test_real_api_internal_device_count_raises` — [`L1117`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations_test.py#L1117)
- <a id="AnnotationsTest.test_real_api_stream_context_warns_once_without_internal_warnings"></a>`AnnotationsTest.test_real_api_stream_context_warns_once_without_internal_warnings` — [`L552`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations_test.py#L552)
- <a id="AnnotationsTest.test_real_api_torch_accelerator_set_stream_works"></a>`AnnotationsTest.test_real_api_torch_accelerator_set_stream_works` — [`L1134`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations_test.py#L1134)
- <a id="AnnotationsTest.test_stable_metadata_no_warning"></a>`AnnotationsTest.test_stable_metadata_no_warning` — [`L159`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations_test.py#L159)
- <a id="AnnotationsTest.test_stage_enum"></a>`AnnotationsTest.test_stage_enum` — [`L60`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations_test.py#L60)
- <a id="AnnotationsTest.test_stage_warning_from_user_getattr"></a>`AnnotationsTest.test_stage_warning_from_user_getattr` — [`L506`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations_test.py#L506)
- <a id="AnnotationsTest.test_stage_warning_from_user_getattr.UserModule"></a>`AnnotationsTest.test_stage_warning_from_user_getattr.UserModule` — [`L511`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations_test.py#L511)
- <a id="AnnotationsTest.test_stage_warning_from_user_getattr.UserModule.__getattr__"></a>`AnnotationsTest.test_stage_warning_from_user_getattr.UserModule.__getattr__` — [`L513`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations_test.py#L513)
- <a id="AnnotationsTest.test_static_class_attributes_bypass_getattr_and_warnings"></a>`AnnotationsTest.test_static_class_attributes_bypass_getattr_and_warnings` — [`L460`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations_test.py#L460)
- <a id="AnnotationsTest.test_warning_suppressed_for_framework_callers"></a>`AnnotationsTest.test_warning_suppressed_for_framework_callers` — [`L675`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations_test.py#L675)
- <a id="SampleClass.val"></a>`SampleClass.val` — [`L247`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations_test.py#L247)
- <a id="SampleClass.x"></a>`SampleClass.x` — [`L972`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations_test.py#L972)
- <a id="_reset_warn_once"></a>`_reset_warn_once` — [`L40`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations_test.py#L40)
- <a id="deprecated"></a>`deprecated` — [`L35`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations_test.py#L35)
- <a id="experimental"></a>`experimental` — [`L33`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations_test.py#L33)
- <a id="forbid_in_torch_compile"></a>`forbid_in_torch_compile` — [`L37`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations_test.py#L37)
- <a id="internal_or_experimental"></a>`internal_or_experimental` — [`L36`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations_test.py#L36)
- <a id="stable"></a>`stable` — [`L34`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations_test.py#L34)
