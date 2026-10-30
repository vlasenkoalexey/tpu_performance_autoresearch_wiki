---
title: 'Module: csrc/common/compilation_cache_test_utils.cc'
type: catalog
provenance: extracted
module: csrc/common/compilation_cache_test_utils.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  CreateDummyExecutable: CreateDummyExecutable(889c023c5416c17).
  MakeDummyDynamicMetadata: MakeDummyDynamicMetadata(4229665a43d86dbd).
  IsCompatible: '`$anonymous_namespace_csrc/common/compilation_cache_test_utils.cc`/IsCompatible(fc840bc1ba28179e).'
---
# Module: [`csrc/common/compilation_cache_test_utils.cc`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache_test_utils.cc)

## Functions
- <a id="CreateDummyExecutable"></a>`CreateDummyExecutable(xla::PjRtClient& client, UniqueCompileOptions compile_options)` — [`L55`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache_test_utils.cc#L55) — Compiles a trivial identity computation with `client`. Matches the
- <a id="IsCompatible"></a>`IsCompatible(absl::Span<const Shape> input_shapes, absl::Span<const Shape> output_shapes)` — [`L40`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache_test_utils.cc#L40)
- <a id="MakeDummyDynamicMetadata"></a>`MakeDummyDynamicMetadata()` — [`L48`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache_test_utils.cc#L48) — Returns dummy unbounded dynamic execution metadata whose compatibility check

