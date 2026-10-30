---
title: 'Module: csrc/common/version.h'
type: catalog
provenance: extracted
module: csrc/common/version.h
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  Version: Version#
  Version.Version: Version#Version(9a95852f3bf83270).
  Version.Max: Version#Max(48049361b16284bf).
  AbslStringify: AbslStringify(9f5e69576f765108).
  Version.kStable: Version#kStable.
  Version.dev_: Version#dev_.
  Version.patch_: Version#patch_.
  Version.minor_: Version#minor_.
  Version.major_: Version#major_.
  operator: '`operator<=>`(a878bd2ff6005bd5).'
---
# Module: [`csrc/common/version.h`](../../../../../../raw/code/torch_tpu/csrc/common/version.h)

## Classes
### <a id="Version"></a>`Version`
- def: [`csrc/common/version.h:39`](../../../../../../raw/code/torch_tpu/csrc/common/version.h#L39)
- doc: A release version of the form `<major>.<minor>.<patch>[.dev<build>]`, e.g.
- signature: `class Version`
- members:
  - <a id="Version.Max"></a>`Max()` — [`L45`](../../../../../../raw/code/torch_tpu/csrc/common/version.h#L45) — Returns a version that is greater than or equal to every other version.
  - <a id="Version.Version"></a>`Version(int major, int minor, int patch, int64_t dev = kStable)` — [`L62`](../../../../../../raw/code/torch_tpu/csrc/common/version.h#L62) — `dev` is the build number of a pre-release; omit it for a stable release.
  - <a id="Version.dev_"></a>`dev_` — [`L92`](../../../../../../raw/code/torch_tpu/csrc/common/version.h#L92) — `int64_t` because timestamp-based dev builds use 12 digits (YYYYMMDDHHMM),
  - <a id="Version.kStable"></a>`kStable` — [`L42`](../../../../../../raw/code/torch_tpu/csrc/common/version.h#L42) — The `dev` value of a stable release.
  - <a id="Version.major_"></a>`major_` — [`L87`](../../../../../../raw/code/torch_tpu/csrc/common/version.h#L87) — The declaration order determines the ordering of `operator<=>`.
  - <a id="Version.minor_"></a>`minor_` — [`L88`](../../../../../../raw/code/torch_tpu/csrc/common/version.h#L88)
  - <a id="Version.patch_"></a>`patch_` — [`L89`](../../../../../../raw/code/torch_tpu/csrc/common/version.h#L89)
- uses (calls/refs, reference-scoped): [`Parse`](version.cc.md#Version.Parse), [`DieOnNegativeComponent`](version.cc.md#Version.DieOnNegativeComponent)
- used by: [`SetLibtpuVersion`](libtpu_version.cc.md#SetLibtpuVersion), [`Parse`](version.cc.md#Version.Parse), [`GetLibtpuVersionString`](libtpu_version.cc.md#GetLibtpuVersionString), [`ParseOptionalComponent`](version.cc.md#ParseOptionalComponent), [`ResetLibtpuVersionForTesting`](libtpu_version.cc.md#ResetLibtpuVersionForTesting), [`TestBody`](libtpu_version_test.cc.md#LibtpuVersionTest_ResetLibtpuVersionForTesting_Test.TestBody), [`TestBody`](libtpu_version_test.cc.md#LibtpuVersionTest_SetAndGetVersion_Test.TestBody), [`TestBody`](libtpu_version_test.cc.md#LibtpuVersionTest_SetEmptyVersion_Test.TestBody), [`TestBody`](libtpu_version_test.cc.md#LibtpuVersionTest_StableVersionPrecedenceOverNightly_Test.TestBody), [`TestBody`](libtpu_version_test.cc.md#LibtpuVersionTest_CompareVersion_Test.TestBody), [`TestBody`](libtpu_version_test.cc.md#LibtpuVersionTest_InitialValueIsUnsetInFreshProcess_Test.TestBody), [`TestBody`](libtpu_version_test.cc.md#LibtpuVersionTest_PaddingZerosForFirstThreeComponents_Test.TestBody), [`TestBody`](libtpu_version_test.cc.md#LibtpuVersionTest_TimestampDevVersion_Test.TestBody), [`TestBody`](version_test.cc.md#VersionTest_ParseRejectsMalformedVersion_Test.TestBody), [`TestBody`](version_test.cc.md#VersionTest_ParseRejectsOverflow_Test.TestBody), [`AbslStringify`](version.h.md#AbslStringify), [`TestBody`](version_test.cc.md#VersionTest_ParseIgnoresSuffix_Test.TestBody), [`TestBody`](version_test.cc.md#VersionTest_ParseTimestampDevVersionBeyondInt32_Test.TestBody), [`TestBody`](version_test.cc.md#VersionTest_Parse_Test.TestBody), [`TestBody`](version_test.cc.md#VersionTest_MaxIsGreaterThanOrEqualToEveryVersion_Test.TestBody), [`TestBody`](version_test.cc.md#VersionTest_Stringify_Test.TestBody), [`TestBody`](version_test.cc.md#VersionDeathTest_ConstructorDiesOnNegativeComponents_Test.TestBody), [`TestBody`](version_test.cc.md#VersionTest_ComparesComponentByComponent_Test.TestBody), [`TestBody`](version_test.cc.md#VersionTest_StableRanksAboveDevBuildsOfSameRelease_Test.TestBody), [`parsed_version`](libtpu_version.cc.md#LibtpuVersionState.parsed_version), [`version`](libtpu_version.cc.md#LibtpuVersionState.version), [`DieOnNegativeComponent`](version.cc.md#Version.DieOnNegativeComponent), [`operator<=>`](version.h.md#operator)

## Functions
- <a id="AbslStringify"></a>`AbslStringify(Sink& sink, const Version& version)` — [`L72`](../../../../../../raw/code/torch_tpu/csrc/common/version.h#L72)
- <a id="operator"></a>`operator<=>(const Version&, const Version&)` — [`L69`](../../../../../../raw/code/torch_tpu/csrc/common/version.h#L69)

