---
title: Python and PyTorch version support policy
type: doc-concept
provenance: doc
source: docs/developers/python_support_policy.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T02:38:46Z}
---
# Python and PyTorch version support policy

## Definition
TorchTPU does not define its own Python support window. It follows upstream PyTorch's Release Compatibility Matrix for the **minimum PyTorch release TorchTPU supports**, and adds and sunsets CPython minor versions per PyTorch's policy (RFC-0038, tied to CPython EOL). At v0.2.0 that means Python **3.11, 3.12, 3.13 and 3.14, including free-threaded 3.14t**. The doc keeps the list in sync with `oss/pyproject.toml` (`requires-python = ">=3.11"`), `oss/bazel/supported_python_versions.bzl` and the OSS README through a `LINT.IfChange` block.

## In torch_tpu (grounded)
The Python policy is configuration, not code, but its PyTorch-side counterpart is implemented at import time. The C++ extension is shipped as per-PyTorch-ABI glue `.so` files named `<module>_<major>_<minor>_<patch>.so`. [`install_hook`](../catalog/src/torch_tpu/_versioned_so_loader.md#install_hook) (called from the package `__init__`) installs a [`VersionDispatchFinder`](../catalog/src/torch_tpu/_versioned_so_loader.md#VersionDispatchFinder) that redirects `torch_tpu._internal.<module>` imports to the glue matching the installed torch. [`resolve_suffix`](../catalog/src/torch_tpu/_versioned_so_loader.md#resolve_suffix) picks the newest glue whose version is <= the installed PyTorch (dev builds compare by their release triple), and the glue is linked `-z now`, so an ABI mismatch fails loudly at import rather than crashing mid-run.

## Why it matters / when it applies
- **Environment reproducibility for experiments:** the getting-started docs pin Python 3.12 and say not to install PyTorch separately (the wheel pulls a matching CPU PyTorch). A hand-installed torch that is newer than every bundled glue silently uses the newest glue, and one older than every glue is an import error. Record the torch, torch_tpu and Python versions on experiment pages.
- Free-threaded 3.14t is in the supported set, but TorchTPU's eager runtime still relies on thread-local context states, so treat no-GIL perf claims as unverified until measured.
- New Python versions arrive only when the minimum supported PyTorch supports them, so bumping Python in an experiment image can force a PyTorch bump too.

## Connections
- Code concepts: [hardware-introspection](../concepts/hardware-introspection.md), [pjrt-client](../concepts/pjrt-client.md)
- Module catalogs: [src/torch_tpu/_versioned_so_loader](../catalog/src/torch_tpu/_versioned_so_loader.md), `src/torch_tpu/__init__.py` (no catalog page: it defines no documentable symbols)
- Related doc-concepts: [tpu-device-backend-initialization](tpu-device-backend-initialization.md), [ci-test-tag-filters](ci-test-tag-filters.md)

## Source
Extracted from `docs/developers/python_support_policy.md` (kept in place).
