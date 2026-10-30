---
title: Building the torch_tpu wheel - -c opt and --config=wheel_common
type: doc-concept
provenance: doc
source: README.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T02:38:46Z}
---
# Building the torch_tpu wheel - -c opt and --config=wheel_common

## Definition
The README's build-from-source section has two rules that matter for performance and correctness:
- **Optimized mode is the default and the expectation.** All OSS Bazel builds default to `-c opt` via `.bazelrc`; unoptimized builds (`-c fastbuild`, `-c dbg`) "can degrade performance" and are not used for wheels. An unoptimized wheel is only produced if you opt in with `--//:allow_unoptimized_wheel=True`.
- **`--config=wheel_common` is mandatory.** It sets `--//:wheel_build=True`, which routes the shared XLA/MLIR backend through a `torch_version`-reset transition so that it is factored into a single `libxla_base.so`. Without it each per-torch-version component ships its own copy of the backend and the wheel aborts on `import torch` with duplicate static registrations. The config also enables RBE remote cache/execution; without credentials append `--config=no_rbe` *after* `wheel_common` (the later config wins).

Canonical command: `bazel build --config=wheel_common //ci/wheel:torch_tpu_wheel` (plus `--config=no_rbe` when needed). The nightly pip index is the alternative to building.

## In torch_tpu (grounded)
These are build-system facts with no C++/Python symbol in the catalog. Where they live in the repo (prose only, not catalog links):
- `.bazelrc` sets `build --compilation_mode=opt` ("Default to optimized (-c opt) builds in OSS").
- `BUILD.bazel` defines the `allow_unoptimized_wheel` and `wheel_build` bool flags.
- `ci/wheel/pywrap_mapper.bzl` holds the guard that fails the wheel action with "The torch_tpu wheel must be built with compilation mode -c opt" unless the override flag is set, and a second guard that refuses wheel builds without `wheel_build` because the result would be "a silently broken wheel".
- Related runtime caveat: the tier-2/3 compilation caches are namespaced by [`GetTorchTpuBinaryFingerprint`](../catalog/csrc/common/compilation_cache_utils.cc.md#GetTorchTpuBinaryFingerprint), which combines a hand-bumped `kTorchTpuBinaryVersion` constant with the PjRt/libtpu version string - not a hash of the build. Two locally built wheels (e.g. `-c dbg` and `-c opt` of the same source) therefore share cache entries; that is harmless for the XLA executables themselves, which do not depend on how torch_tpu's host code was compiled ([multi-tier-compilation-cache.md](multi-tier-compilation-cache.md)).

## Why it matters / when it applies
- Every eager op runs through C++ dispatch, cache-key fingerprinting and StableHLO building on the host; in a `-c dbg`/`fastbuild` wheel that host path is much slower, which inflates dispatch-bound eager step times and makes perf measurements meaningless. Any benchmark or autoresearch experiment must state that it ran on an `-c opt` wheel.
- The guard means a slow wheel cannot happen by accident - only with the explicit `allow_unoptimized_wheel` flag - so when a custom-built wheel is suspiciously slow, check the build command for that flag first.
- The README also warns that installing the wheel with the default index pulls the CUDA `torch` build; use the nightly index URL (CPU torch) to avoid the extra dependency weight.

## Connections
- Code concepts: [compilation-cache](../concepts/compilation-cache.md), [eager-op-dispatch](../concepts/eager-op-dispatch.md), [pjrt-client](../concepts/pjrt-client.md)
- Module catalogs: [csrc/common/compilation_cache_utils.cc](../catalog/csrc/common/compilation_cache_utils.cc.md)
- Related doc-concepts: [torch-tpu-architecture-and-lowering-stack.md](torch-tpu-architecture-and-lowering-stack.md), [python-version-support-policy.md](python-version-support-policy.md), [multi-tier-compilation-cache.md](multi-tier-compilation-cache.md), [tpu-device-backend-initialization.md](tpu-device-backend-initialization.md)

## Source
Extracted from `README.md` ("Build from source") (kept in place).
