---
title: 'Module: csrc/common/symbol_stage.h'
type: catalog
provenance: extracted
module: csrc/common/symbol_stage.h
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  SymbolStage: SymbolStage#
  SymbolStage.InternalImplementation: SymbolStage#InternalImplementation(b355d831ef0be7b).
  SymbolStage.Experimental: SymbolStage#Experimental(b355d831ef0be7b).
  SymbolStage.is_deprecated: SymbolStage#is_deprecated(3482b152b9333168).
  SymbolStage.is_internal_implementation: SymbolStage#is_internal_implementation(3482b152b9333168).
  SymbolStage.is_experimental: SymbolStage#is_experimental(3482b152b9333168).
  SymbolStage.InternalApi: SymbolStage#InternalApi(b355d831ef0be7b).
  SymbolStage.Stable: SymbolStage#Stable(b355d831ef0be7b).
  SymbolStage.is_stable: SymbolStage#is_stable(3482b152b9333168).
  SymbolStage.Deprecated: SymbolStage#Deprecated(a922fae37d09b562).
  SymbolStage.is_internal_api: SymbolStage#is_internal_api(3482b152b9333168).
  SymbolStage.version: SymbolStage#version(2f333c6a651e039a).
  SymbolStage.Stage: SymbolStage#Stage#
  SymbolStage.SymbolStage: SymbolStage#SymbolStage(375144242a649417).
  SymbolStage.stage_: SymbolStage#stage_.
  operator: '`operator==`(806d3869de1ee672).'
  SymbolStage.Stage.kDeprecated: SymbolStage#Stage#kDeprecated.
  SymbolStage.version_: SymbolStage#version_.
  SymbolStage.Stage.kInternalImplementation: SymbolStage#Stage#kInternalImplementation.
  SymbolStage.Stage.kInternalApi: SymbolStage#Stage#kInternalApi.
  SymbolStage.Stage.kExperimental: SymbolStage#Stage#kExperimental.
  SymbolStage.Stage.kStable: SymbolStage#Stage#kStable.
---
# Module: [`csrc/common/symbol_stage.h`](../../../../../../raw/code/torch_tpu/csrc/common/symbol_stage.h)

## Classes
### <a id="SymbolStage"></a>`SymbolStage`
- def: [`csrc/common/symbol_stage.h:40`](../../../../../../raw/code/torch_tpu/csrc/common/symbol_stage.h#L40)
- doc: Represents the stability and visibility stage of a TorchTPU symbol.
- signature: `class SymbolStage`
- members:
  - <a id="SymbolStage.Deprecated"></a>`Deprecated(std::string_view version)` — [`L78`](../../../../../../raw/code/torch_tpu/csrc/common/symbol_stage.h#L78)
  - <a id="SymbolStage.Experimental"></a>`Experimental()` — [`L74`](../../../../../../raw/code/torch_tpu/csrc/common/symbol_stage.h#L74)
  - <a id="SymbolStage.InternalApi"></a>`InternalApi()` — [`L71`](../../../../../../raw/code/torch_tpu/csrc/common/symbol_stage.h#L71)
  - <a id="SymbolStage.InternalImplementation"></a>`InternalImplementation()` — [`L68`](../../../../../../raw/code/torch_tpu/csrc/common/symbol_stage.h#L68) — Factory methods.
  - <a id="SymbolStage.Stable"></a>`Stable()` — [`L77`](../../../../../../raw/code/torch_tpu/csrc/common/symbol_stage.h#L77)
  - `SymbolStage(Stage stage, std::string_view version)` — [`L105`](../../../../../../raw/code/torch_tpu/csrc/common/symbol_stage.h#L105) — Constructor for kDeprecated stage with the given version string_view.
  - <a id="SymbolStage.SymbolStage"></a>`SymbolStage(Stage stage)` — [`L94`](../../../../../../raw/code/torch_tpu/csrc/common/symbol_stage.h#L94) — Constructor for non-deprecated stages: kInternalImplementation,
  - <a id="SymbolStage.is_deprecated"></a>`is_deprecated()` — [`L59`](../../../../../../raw/code/torch_tpu/csrc/common/symbol_stage.h#L59)
  - <a id="SymbolStage.is_experimental"></a>`is_experimental()` — [`L53`](../../../../../../raw/code/torch_tpu/csrc/common/symbol_stage.h#L53)
  - <a id="SymbolStage.is_internal_api"></a>`is_internal_api()` — [`L50`](../../../../../../raw/code/torch_tpu/csrc/common/symbol_stage.h#L50)
  - <a id="SymbolStage.is_internal_implementation"></a>`is_internal_implementation()` — [`L47`](../../../../../../raw/code/torch_tpu/csrc/common/symbol_stage.h#L47)
  - <a id="SymbolStage.is_stable"></a>`is_stable()` — [`L56`](../../../../../../raw/code/torch_tpu/csrc/common/symbol_stage.h#L56)
  - <a id="SymbolStage.version"></a>`version()` — [`L43`](../../../../../../raw/code/torch_tpu/csrc/common/symbol_stage.h#L43) — Observers
  - <a id="SymbolStage.stage_"></a>`stage_` — [`L117`](../../../../../../raw/code/torch_tpu/csrc/common/symbol_stage.h#L117)
  - <a id="SymbolStage.version_"></a>`version_` — [`L118`](../../../../../../raw/code/torch_tpu/csrc/common/symbol_stage.h#L118)
- uses (calls/refs, reference-scoped): [`Stage`](symbol_stage.h.md#SymbolStage.Stage), [`kDeprecated`](symbol_stage.h.md#SymbolStage.Stage.kDeprecated), [`kInternalImplementation`](symbol_stage.h.md#SymbolStage.Stage.kInternalImplementation), [`kExperimental`](symbol_stage.h.md#SymbolStage.Stage.kExperimental), [`kInternalApi`](symbol_stage.h.md#SymbolStage.Stage.kInternalApi), [`kStable`](symbol_stage.h.md#SymbolStage.Stage.kStable)
- used by: [`kEnvVarToStage`](env_vars.h.md#kEnvVarToStage), [`GetEnvOnce`](env_vars.h.md#GetEnvOnce), [`kDeprecatedStage`](symbol_stage_test.cc.md#kDeprecatedStage), [`kSymbolStages`](symbol_stage_test.cc.md#kSymbolStages), [`kInternalImplementationStage`](symbol_stage_test.cc.md#kInternalImplementationStage), [`kExperimentalStage`](symbol_stage_test.cc.md#kExperimentalStage), [`kInternalApiStage`](symbol_stage_test.cc.md#kInternalApiStage), [`kStableStage`](symbol_stage_test.cc.md#kStableStage), [`TestBody`](symbol_stage_test.cc.md#SymbolStageTest_DeprecatedStage_Test.TestBody), [`TestBody`](symbol_stage_test.cc.md#SymbolStageTest_ExperimentalStage_Test.TestBody), [`TestBody`](symbol_stage_test.cc.md#SymbolStageTest_InternalApiStage_Test.TestBody), [`TestBody`](symbol_stage_test.cc.md#SymbolStageTest_InternalImplementationStage_Test.TestBody), [`TestBody`](symbol_stage_test.cc.md#SymbolStageTest_StableStage_Test.TestBody), [`TestBody`](symbol_stage_test.cc.md#SymbolStageTest_EqualityComparison_Test.TestBody), [`operator==`](symbol_stage.h.md#operator)

### <a id="SymbolStage.Stage"></a>`SymbolStage.Stage`
- def: [`csrc/common/symbol_stage.h:83`](../../../../../../raw/code/torch_tpu/csrc/common/symbol_stage.h#L83)
- signature: `enum class Stage`
- members:
  - <a id="SymbolStage.Stage.kDeprecated"></a>`kDeprecated` — [`L88`](../../../../../../raw/code/torch_tpu/csrc/common/symbol_stage.h#L88)
  - <a id="SymbolStage.Stage.kExperimental"></a>`kExperimental` — [`L86`](../../../../../../raw/code/torch_tpu/csrc/common/symbol_stage.h#L86)
  - <a id="SymbolStage.Stage.kInternalApi"></a>`kInternalApi` — [`L85`](../../../../../../raw/code/torch_tpu/csrc/common/symbol_stage.h#L85)
  - <a id="SymbolStage.Stage.kInternalImplementation"></a>`kInternalImplementation` — [`L84`](../../../../../../raw/code/torch_tpu/csrc/common/symbol_stage.h#L84)
  - <a id="SymbolStage.Stage.kStable"></a>`kStable` — [`L87`](../../../../../../raw/code/torch_tpu/csrc/common/symbol_stage.h#L87)
- used by: [`InternalImplementation`](symbol_stage.h.md#SymbolStage.InternalImplementation), [`Experimental`](symbol_stage.h.md#SymbolStage.Experimental), [`is_deprecated`](symbol_stage.h.md#SymbolStage.is_deprecated), [`is_experimental`](symbol_stage.h.md#SymbolStage.is_experimental), [`is_internal_implementation`](symbol_stage.h.md#SymbolStage.is_internal_implementation), [`InternalApi`](symbol_stage.h.md#SymbolStage.InternalApi), [`Stable`](symbol_stage.h.md#SymbolStage.Stable), [`is_stable`](symbol_stage.h.md#SymbolStage.is_stable), [`Deprecated`](symbol_stage.h.md#SymbolStage.Deprecated), [`is_internal_api`](symbol_stage.h.md#SymbolStage.is_internal_api), [`SymbolStage`](symbol_stage.h.md#SymbolStage.SymbolStage), [`stage_`](symbol_stage.h.md#SymbolStage.stage_), [`SymbolStage`](symbol_stage.h.md#SymbolStage.SymbolStage)

## Functions
- <a id="operator"></a>`operator==(const SymbolStage& lhs, const SymbolStage& rhs)` — [`L64`](../../../../../../raw/code/torch_tpu/csrc/common/symbol_stage.h#L64) — Equality comparison

