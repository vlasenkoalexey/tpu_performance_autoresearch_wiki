---
title: 'Module: csrc/common/libtpu_version.cc'
type: catalog
provenance: extracted
module: csrc/common/libtpu_version.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  SetLibtpuVersion: SetLibtpuVersion(c8024318075daf50).
  GetLibtpuVersion: GetLibtpuVersion(48049361b16284bf).
  GetLibtpuVersionString: GetLibtpuVersionString(424609d755dfbb5b).
  ResetLibtpuVersionForTesting: ResetLibtpuVersionForTesting(49f6e7a06ebc5aa8).
  LibtpuVersionState.parsed_version: '`$anonymous_namespace_csrc/common/libtpu_version.cc`/LibtpuVersionState#parsed_version.'
  LibtpuVersionState.version: '`$anonymous_namespace_csrc/common/libtpu_version.cc`/LibtpuVersionState#version.'
  GetState: '`$anonymous_namespace_csrc/common/libtpu_version.cc`/GetState(28f102ad836bdcea).'
  LibtpuVersionState: '`$anonymous_namespace_csrc/common/libtpu_version.cc`/LibtpuVersionState#'
  LibtpuVersionState.mutex: '`$anonymous_namespace_csrc/common/libtpu_version.cc`/LibtpuVersionState#mutex.'
---
# Module: [`csrc/common/libtpu_version.cc`](../../../../../../raw/code/torch_tpu/csrc/common/libtpu_version.cc)

## Classes
### <a id="LibtpuVersionState"></a>`LibtpuVersionState`
- def: [`csrc/common/libtpu_version.cc:33`](../../../../../../raw/code/torch_tpu/csrc/common/libtpu_version.cc#L33)
- signature: `struct LibtpuVersionState`
- members:
  - <a id="LibtpuVersionState.mutex"></a>`mutex` — [`L34`](../../../../../../raw/code/torch_tpu/csrc/common/libtpu_version.cc#L34)
  - <a id="LibtpuVersionState.parsed_version"></a>`parsed_version` — [`L36`](../../../../../../raw/code/torch_tpu/csrc/common/libtpu_version.cc#L36)
  - <a id="LibtpuVersionState.version"></a>`version` — [`L35`](../../../../../../raw/code/torch_tpu/csrc/common/libtpu_version.cc#L35)
- uses (calls/refs, reference-scoped): [`Version`](version.h.md#Version), [`Max`](version.h.md#Version.Max)
- used by: [`SetLibtpuVersion`](libtpu_version.cc.md#SetLibtpuVersion), [`GetLibtpuVersion`](libtpu_version.cc.md#GetLibtpuVersion), [`GetLibtpuVersionString`](libtpu_version.cc.md#GetLibtpuVersionString), [`ResetLibtpuVersionForTesting`](libtpu_version.cc.md#ResetLibtpuVersionForTesting), [`GetState`](libtpu_version.cc.md#GetState)

## Functions
- <a id="GetLibtpuVersion"></a>`GetLibtpuVersion()` — [`L72`](../../../../../../raw/code/torch_tpu/csrc/common/libtpu_version.cc#L72) — Returns the libtpu version set via SetLibtpuVersion, for gating features on
- <a id="GetLibtpuVersionString"></a>`GetLibtpuVersionString()` — [`L66`](../../../../../../raw/code/torch_tpu/csrc/common/libtpu_version.cc#L66) — Returns the libtpu version string set via SetLibtpuVersion, or std::nullopt
- <a id="GetState"></a>`GetState()` — [`L39`](../../../../../../raw/code/torch_tpu/csrc/common/libtpu_version.cc#L39)
- <a id="ResetLibtpuVersionForTesting"></a>`ResetLibtpuVersionForTesting()` — [`L78`](../../../../../../raw/code/torch_tpu/csrc/common/libtpu_version.cc#L78) — Resets the libtpu version state to uninitialized (std::nullopt).
- <a id="SetLibtpuVersion"></a>`SetLibtpuVersion(std::string_view version)` — [`L46`](../../../../../../raw/code/torch_tpu/csrc/common/libtpu_version.cc#L46) — Sets the libtpu version string.

