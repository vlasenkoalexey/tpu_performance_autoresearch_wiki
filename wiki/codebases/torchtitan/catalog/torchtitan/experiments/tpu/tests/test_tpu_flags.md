---
title: 'Module: torchtitan/experiments/tpu/tests/test_tpu_flags.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/tests/test_tpu_flags.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.tests.test_tpu_flags`/
symbols:
  FormatAndParseTest.test_round_trip: FormatAndParseTest#test_round_trip().
  ExtraFlagsTest.test_extra_flags_add_to_and_override_the_config: ExtraFlagsTest#test_extra_flags_add_to_and_override_the_config().
  ExtraFlagsTest.test_environment_still_wins_over_extra_flags: ExtraFlagsTest#test_environment_still_wins_over_extra_flags().
  RemovingFlagsTest.test_removes_a_flag_the_config_sets: RemovingFlagsTest#test_removes_a_flag_the_config_sets().
  RemovingFlagsTest.test_removing_a_flag_nothing_sets_is_a_no_op: RemovingFlagsTest#test_removing_a_flag_nothing_sets_is_a_no_op().
  RemovingFlagsTest.test_removal_and_addition_in_one_value: RemovingFlagsTest#test_removal_and_addition_in_one_value().
  RemovingFlagsTest.test_environment_can_put_back_a_removed_flag: RemovingFlagsTest#test_environment_can_put_back_a_removed_flag().
  _FakeConfig: _FakeConfig#
  FlagMapCommandLineTest._parse: FlagMapCommandLineTest#_parse().
  _FakeConfig.libtpu_init_flags: _FakeConfig#libtpu_init_flags.
  ApplyInitFlagsTest.test_writes_both_environment_variables: ApplyInitFlagsTest#test_writes_both_environment_variables().
  ApplyInitFlagsTest.test_environment_wins_over_config_for_the_same_flag: ApplyInitFlagsTest#test_environment_wins_over_config_for_the_same_flag().
  ExtraFlagsTest.test_extra_flags_alone_reach_the_environment: ExtraFlagsTest#test_extra_flags_alone_reach_the_environment().
  ReplacingTheDeclaredSetTest.test_emptying_the_config_flags_applies_none: ReplacingTheDeclaredSetTest#test_emptying_the_config_flags_applies_none().
  ReplacingTheDeclaredSetTest.test_replacement_set_is_applied_verbatim: ReplacingTheDeclaredSetTest#test_replacement_set_is_applied_verbatim().
  _FakeConfig.extra_libtpu_init_flags: _FakeConfig#extra_libtpu_init_flags.
  ApplyInitFlagsTest.test_empty_config_flags_leave_the_environment_alone: ApplyInitFlagsTest#test_empty_config_flags_leave_the_environment_alone().
  MergeFlagsTest.test_later_bundles_and_overrides_win: MergeFlagsTest#test_later_bundles_and_overrides_win().
  MergeFlagsTest.test_bundles_are_not_mutated: MergeFlagsTest#test_bundles_are_not_mutated().
  MergeFlagsTest.test_values_render_as_libtpu_expects: MergeFlagsTest#test_values_render_as_libtpu_expects().
  FormatAndParseTest.test_format_renders_command_line_flags: FormatAndParseTest#test_format_renders_command_line_flags().
  FormatAndParseTest.test_parse_accepts_launcher_flag_strings: FormatAndParseTest#test_parse_accepts_launcher_flag_strings().
  FormatAndParseTest.test_parse_of_empty_string_is_empty: FormatAndParseTest#test_parse_of_empty_string_is_empty().
  FlagMapCommandLineTest._Config.libtpu_init_flags: FlagMapCommandLineTest#_Config#libtpu_init_flags.
  FlagMapCommandLineTest.test_sets_flags_the_default_does_not_have: FlagMapCommandLineTest#test_sets_flags_the_default_does_not_have().
  FlagMapCommandLineTest.test_accepts_several_flags_in_one_value: FlagMapCommandLineTest#test_accepts_several_flags_in_one_value().
  FlagMapCommandLineTest.test_accepts_the_environment_variable_spelling: FlagMapCommandLineTest#test_accepts_the_environment_variable_spelling().
  FlagMapCommandLineTest._Config: FlagMapCommandLineTest#_Config#
  _FakeConfig.xla_flags: _FakeConfig#xla_flags.
  _FakeConfig.extra_xla_flags: _FakeConfig#extra_xla_flags.
  MergeFlagsTest: MergeFlagsTest#
  FormatAndParseTest: FormatAndParseTest#
  ApplyInitFlagsTest: ApplyInitFlagsTest#
  ExtraFlagsTest: ExtraFlagsTest#
  FlagMapCommandLineTest: FlagMapCommandLineTest#
  RemovingFlagsTest: RemovingFlagsTest#
  ReplacingTheDeclaredSetTest: ReplacingTheDeclaredSetTest#
---
# Module: [`torchtitan/experiments/tpu/tests/test_tpu_flags.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_tpu_flags.py)

> **Collapsed catalog** (37 symbols) — one row per symbol with its source line; member detail omitted. See the source link above, or the curated codebase page, for depth.

- <a id="ApplyInitFlagsTest"></a>`ApplyInitFlagsTest` — [`L92`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_tpu_flags.py#L92)
- <a id="ApplyInitFlagsTest.test_empty_config_flags_leave_the_environment_alone"></a>`ApplyInitFlagsTest.test_empty_config_flags_leave_the_environment_alone` — [`L138`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_tpu_flags.py#L138)
- <a id="ApplyInitFlagsTest.test_environment_wins_over_config_for_the_same_flag"></a>`ApplyInitFlagsTest.test_environment_wins_over_config_for_the_same_flag` — [`L111`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_tpu_flags.py#L111)
- <a id="ApplyInitFlagsTest.test_writes_both_environment_variables"></a>`ApplyInitFlagsTest.test_writes_both_environment_variables` — [`L94`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_tpu_flags.py#L94)
- <a id="ExtraFlagsTest"></a>`ExtraFlagsTest` — [`L147`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_tpu_flags.py#L147)
- <a id="ExtraFlagsTest.test_environment_still_wins_over_extra_flags"></a>`ExtraFlagsTest.test_environment_still_wins_over_extra_flags` — [`L177`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_tpu_flags.py#L177)
- <a id="ExtraFlagsTest.test_extra_flags_add_to_and_override_the_config"></a>`ExtraFlagsTest.test_extra_flags_add_to_and_override_the_config` — [`L150`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_tpu_flags.py#L150)
- <a id="ExtraFlagsTest.test_extra_flags_alone_reach_the_environment"></a>`ExtraFlagsTest.test_extra_flags_alone_reach_the_environment` — [`L191`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_tpu_flags.py#L191)
- <a id="FlagMapCommandLineTest"></a>`FlagMapCommandLineTest` — [`L201`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_tpu_flags.py#L201)
- <a id="FlagMapCommandLineTest._Config"></a>`FlagMapCommandLineTest._Config` — [`L205`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_tpu_flags.py#L205)
- <a id="FlagMapCommandLineTest._Config.libtpu_init_flags"></a>`FlagMapCommandLineTest._Config.libtpu_init_flags` — [`L206`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_tpu_flags.py#L206)
- <a id="FlagMapCommandLineTest._parse"></a>`FlagMapCommandLineTest._parse` — [`L210`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_tpu_flags.py#L210)
- <a id="FlagMapCommandLineTest.test_accepts_several_flags_in_one_value"></a>`FlagMapCommandLineTest.test_accepts_several_flags_in_one_value` — [`L231`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_tpu_flags.py#L231)
- <a id="FlagMapCommandLineTest.test_accepts_the_environment_variable_spelling"></a>`FlagMapCommandLineTest.test_accepts_the_environment_variable_spelling` — [`L237`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_tpu_flags.py#L237)
- <a id="FlagMapCommandLineTest.test_sets_flags_the_default_does_not_have"></a>`FlagMapCommandLineTest.test_sets_flags_the_default_does_not_have` — [`L219`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_tpu_flags.py#L219)
- <a id="FormatAndParseTest"></a>`FormatAndParseTest` — [`L59`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_tpu_flags.py#L59)
- <a id="FormatAndParseTest.test_format_renders_command_line_flags"></a>`FormatAndParseTest.test_format_renders_command_line_flags` — [`L61`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_tpu_flags.py#L61)
- <a id="FormatAndParseTest.test_parse_accepts_launcher_flag_strings"></a>`FormatAndParseTest.test_parse_accepts_launcher_flag_strings` — [`L67`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_tpu_flags.py#L67)
- <a id="FormatAndParseTest.test_parse_of_empty_string_is_empty"></a>`FormatAndParseTest.test_parse_of_empty_string_is_empty` — [`L80`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_tpu_flags.py#L80)
- <a id="FormatAndParseTest.test_round_trip"></a>`FormatAndParseTest.test_round_trip` — [`L83`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_tpu_flags.py#L83)
- <a id="MergeFlagsTest"></a>`MergeFlagsTest` — [`L24`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_tpu_flags.py#L24)
- <a id="MergeFlagsTest.test_bundles_are_not_mutated"></a>`MergeFlagsTest.test_bundles_are_not_mutated` — [`L34`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_tpu_flags.py#L34)
- <a id="MergeFlagsTest.test_later_bundles_and_overrides_win"></a>`MergeFlagsTest.test_later_bundles_and_overrides_win` — [`L26`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_tpu_flags.py#L26)
- <a id="MergeFlagsTest.test_values_render_as_libtpu_expects"></a>`MergeFlagsTest.test_values_render_as_libtpu_expects` — [`L39`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_tpu_flags.py#L39)
- <a id="RemovingFlagsTest"></a>`RemovingFlagsTest` — [`L246`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_tpu_flags.py#L246)
- <a id="RemovingFlagsTest.test_environment_can_put_back_a_removed_flag"></a>`RemovingFlagsTest.test_environment_can_put_back_a_removed_flag` — [`L289`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_tpu_flags.py#L289)
- <a id="RemovingFlagsTest.test_removal_and_addition_in_one_value"></a>`RemovingFlagsTest.test_removal_and_addition_in_one_value` — [`L276`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_tpu_flags.py#L276)
- <a id="RemovingFlagsTest.test_removes_a_flag_the_config_sets"></a>`RemovingFlagsTest.test_removes_a_flag_the_config_sets` — [`L249`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_tpu_flags.py#L249)
- <a id="RemovingFlagsTest.test_removing_a_flag_nothing_sets_is_a_no_op"></a>`RemovingFlagsTest.test_removing_a_flag_nothing_sets_is_a_no_op` — [`L265`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_tpu_flags.py#L265)
- <a id="ReplacingTheDeclaredSetTest"></a>`ReplacingTheDeclaredSetTest` — [`L302`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_tpu_flags.py#L302)
- <a id="ReplacingTheDeclaredSetTest.test_emptying_the_config_flags_applies_none"></a>`ReplacingTheDeclaredSetTest.test_emptying_the_config_flags_applies_none` — [`L305`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_tpu_flags.py#L305)
- <a id="ReplacingTheDeclaredSetTest.test_replacement_set_is_applied_verbatim"></a>`ReplacingTheDeclaredSetTest.test_replacement_set_is_applied_verbatim` — [`L315`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_tpu_flags.py#L315)
- <a id="_FakeConfig"></a>`_FakeConfig` — [`L13`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_tpu_flags.py#L13)
- <a id="_FakeConfig.extra_libtpu_init_flags"></a>`_FakeConfig.extra_libtpu_init_flags` — [`L18`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_tpu_flags.py#L18)
- <a id="_FakeConfig.extra_xla_flags"></a>`_FakeConfig.extra_xla_flags` — [`L21`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_tpu_flags.py#L21)
- <a id="_FakeConfig.libtpu_init_flags"></a>`_FakeConfig.libtpu_init_flags` — [`L16`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_tpu_flags.py#L16)
- <a id="_FakeConfig.xla_flags"></a>`_FakeConfig.xla_flags` — [`L17`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_tpu_flags.py#L17)
