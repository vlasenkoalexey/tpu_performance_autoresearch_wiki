---
title: Anatomy of a TorchTPU error (C++ error trace, TORCH_SHOW_CPP_STACKTRACES)
type: doc-concept
provenance: doc
source: docs/markdown/error_glossary.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T02:38:46Z}
---
# Anatomy of a TorchTPU error (C++ error trace, TORCH_SHOW_CPP_STACKTRACES)

## Definition
A TorchTPU failure surfaces in Python as a `RuntimeError` whose text can carry three layers: the
**Python traceback** (your line), the **C++ error trace** (where TorchTPU's C++ first detected the
error and how it propagated - its topmost entry is the deepest, failing check, e.g.
`ValidateTensorByteSize`) and the **captured traceback** (the dispatcher path, e.g.
`THPVariable_ones` -> `at::native::ones` -> `AtenEmptyMemoryFormat`). By default open-source builds
show only the Python layer; setting `TORCH_SHOW_CPP_STACKTRACES=1` **before importing torch** adds
the other two.

## In torch_tpu (grounded)
- **Env read, once.** [`TorchShowCppStacktraces`](../catalog/csrc/common/status_builder.cc.md#TorchShowCppStacktraces)
  reads [`kTorchShowCppStacktracesEnvVar`](../catalog/csrc/common/env_vars.h.md#kTorchShowCppStacktracesEnvVar)
  through the memoized env helper; the effective switch defaults to off in OSS builds and on in
  Google-internal builds. Because it is memoized, setting it after the first error check has run
  has no effect - hence "before importing torch".
- **Building the trace.** Errors are `absl::Status` values built with
  [`StatusBuilder`](../catalog/csrc/common/status_builder.h.md#StatusBuilder "csrc/common/status_builder.h:L63");
  each propagation hop calls
  [`MaybeAddCppSourceLoc`](../catalog/csrc/common/status_builder.cc.md#MaybeAddCppSourceLoc "csrc/common/status_builder.cc:L148"),
  which (only when stack traces are enabled) appends `file:line: function()` to a status payload.
  The payload is rendered as "C++ error trace (starting from the origin)".
- **Crossing into Python.** [`TranslateToC10ErrorAndThrow`](../catalog/csrc/common/error_utils.cc.md#TranslateToC10ErrorAndThrow "csrc/common/error_utils.cc:L1223")
  converts the status into a c10 exception that PyTorch turns into the Python `RuntimeError`;
  [`TtError`](../catalog/csrc/common/error_utils.h.md#TtError "csrc/common/error_utils.h:L348")
  is the error type used along the way.
- **The doc's example check.** `torch.ones(-1, device="tpu")` fails in
  [`ValidateTensorByteSize`](../catalog/csrc/common/dtype.cc.md#ValidateTensorByteSize), called from
  the factory kernel [`AtenEmptyMemoryFormat`](../catalog/csrc/ops/nullary_aten_kernels.cc.md#AtenEmptyMemoryFormat).
- **Async errors are sticky.** Errors detected asynchronously (e.g. device-side assertions) are
  latched by [`SetStickyError`](../catalog/csrc/common/error_utils.cc.md#SetStickyError "csrc/common/error_utils.cc:L935")
  and re-thrown at the next sync by
  [`SyncAndCheckStickyError`](../catalog/csrc/common/error_utils.cc.md#SyncAndCheckStickyError "csrc/common/error_utils.cc:L972")
  - which is why the reported Python line can be later than the culprit (see
  [tpu-debugging-ladder](tpu-debugging-ladder.md)).

## Why it matters / when it applies
- Bug reports to the TorchTPU team should include at least the Python traceback plus the C++ error
  trace (debugging levels 1 + 2).
- Read the C++ trace top-down: the first frame names the validation that failed; the rest is the
  propagation path.
- Perf lens: the stack-trace payload is only built when enabled, so leaving
  `TORCH_SHOW_CPP_STACKTRACES` unset in benchmark runs avoids per-error string work; it has no
  effect on the success path.

## Connections
- Code concepts: [error-handling](../concepts/error-handling.md),
  [op-names-and-python-context](../concepts/op-names-and-python-context.md),
  [eager-op-dispatch](../concepts/eager-op-dispatch.md)
- Module catalogs: [csrc/common/status_builder.cc](../catalog/csrc/common/status_builder.cc.md),
  [csrc/common/status_builder.h](../catalog/csrc/common/status_builder.h.md),
  [csrc/common/error_utils.cc](../catalog/csrc/common/error_utils.cc.md),
  [csrc/common/env_vars.h](../catalog/csrc/common/env_vars.h.md)
- Related doc-concepts: [tpu-debugging-ladder](tpu-debugging-ladder.md),
  [tpu-common-failure-patterns](tpu-common-failure-patterns.md),
  [environment-variables](environment-variables.md)

## Source
Extracted from `docs/markdown/error_glossary.md` and its byte-identical duplicate
`docs/markdown/4_debugging_and_performance_analysis_3_getting_better_error_information.md` (both kept in place).
