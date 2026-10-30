---
title: 'Module: csrc/common/compilation_test_helper.h'
type: catalog
provenance: extracted
module: csrc/common/compilation_test_helper.h
status: fresh
symbol_base: cxx . . $ torch_tpu/ScopedCompilerOptionOverrides#
symbols:
  ScopedCompilerOptionOverrides.ScopedCompilerOptionOverrides: ScopedCompilerOptionOverrides(b8ba863c07a5b26f).
  ScopedCompilerOptionOverrides: ''
  ScopedCompilerOptionOverrides.-ScopedCompilerOptionOverrides: '`~ScopedCompilerOptionOverrides`(ced63f7c635d850d).'
---
# Module: [`csrc/common/compilation_test_helper.h`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_test_helper.h)

## Classes
### <a id="ScopedCompilerOptionOverrides"></a>`ScopedCompilerOptionOverrides`
- def: [`csrc/common/compilation_test_helper.h:33`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_test_helper.h#L33)
- doc: An RAII wrapper for managing compiler option overrides within a scope.
- signature: `class ScopedCompilerOptionOverrides`
- members:
  - <a id="ScopedCompilerOptionOverrides.ScopedCompilerOptionOverrides"></a>`ScopedCompilerOptionOverrides(CompilerOptionOverrides overrides)` — [`L35`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_test_helper.h#L35)
  - <a id="ScopedCompilerOptionOverrides.-ScopedCompilerOptionOverrides"></a>`~ScopedCompilerOptionOverrides()` — [`L40`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_test_helper.h#L40)
- uses (calls/refs, reference-scoped): [`PopCompilerOptionOverrides`](compilation.cc.md#PopCompilerOptionOverrides), [`CompilerOptionOverrides`](compilation_spec.h.md#CompilerOptionOverrides), [`PushCompilerOptionOverrides`](compilation.cc.md#PushCompilerOptionOverrides)
- used by: [`TestBody`](compilation_parse_xla_options_test.cc.md#MakeCompilerOptionsTest_ParsesXlaOptions_Test.TestBody), [`TestBody`](compilation_parse_xla_options_test.cc.md#MakeCompilerOptionsTest_PythonContextManagerOverridesEnvVar_Test.TestBody), [`TestBody`](compile_options_key_test.cc.md#CompileOptionsKeyTest_EnvOptionOverrides_Test.TestBody), [`TestBody`](compile_options_key_test.cc.md#CompileOptionsKeyTest_ThreadLocalContextOverrides_Test.TestBody), [`TestBody`](compile_options_key_test.cc.md#CompileOptionsKeyTest_XlaExecutionEffortLevelOverrides_Test.TestBody), [`TestBody`](compilation_test.cc.md#MakeCompilerOptionsTest_CompilerOptionOverrides_Test.TestBody)

