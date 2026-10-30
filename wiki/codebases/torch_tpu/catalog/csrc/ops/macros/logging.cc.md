---
title: 'Module: csrc/ops/macros/logging.cc'
type: catalog
provenance: extracted
module: csrc/ops/macros/logging.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/internal/
symbols:
  ParseArgTypesOrEmpty: ParseArgTypesOrEmpty(d5e5e2fe05cac1e9).
  NormalizePrettyFunctionTypeName.Regex: NormalizePrettyFunctionTypeName(6ccff4770ff7ddc3).Regex#
  NormalizePrettyFunctionTypeName: NormalizePrettyFunctionTypeName(6ccff4770ff7ddc3).
  FindTypeEnd: FindTypeEnd(32b27946a8db50ca).
---
# Module: [`csrc/ops/macros/logging.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/macros/logging.cc)

## Classes
### <a id="NormalizePrettyFunctionTypeName.Regex"></a>`NormalizePrettyFunctionTypeName.Regex`
- def: [`csrc/ops/macros/logging.cc:69`](../../../../../../../raw/code/torch_tpu/csrc/ops/macros/logging.cc#L69)
- doc: Replace type aliases with their underlying types.
- signature: `using Regex = const absl::NoDestructor<std::regex>`
- uses (calls/refs, reference-scoped): (none in-repo)

## Functions
- <a id="FindTypeEnd"></a>`FindTypeEnd(std::string_view args_str)` — [`L33`](../../../../../../../raw/code/torch_tpu/csrc/ops/macros/logging.cc#L33) — Given a string of comma-separated types, returns the index of the end of the
- <a id="NormalizePrettyFunctionTypeName"></a>`NormalizePrettyFunctionTypeName(std::string_view type_name)` — [`L59`](../../../../../../../raw/code/torch_tpu/csrc/ops/macros/logging.cc#L59) — Normalizes a type name parsed from __PRETTY_FUNCTION__.
- <a id="ParseArgTypesOrEmpty"></a>`ParseArgTypesOrEmpty(const std::string_view func_sig)` — [`L150`](../../../../../../../raw/code/torch_tpu/csrc/ops/macros/logging.cc#L150) — Parses and normalizes the argument types from a C++ function signature — documented in [aten-kernel-authoring](../../../../concepts/aten-kernel-authoring.md)
- `ParseArgTypesOrEmpty(const std::string_view func_sig)` — [`L150`](../../../../../../../raw/code/torch_tpu/csrc/ops/macros/logging.cc#L150) — Parses and normalizes the argument types from a C++ function signature

