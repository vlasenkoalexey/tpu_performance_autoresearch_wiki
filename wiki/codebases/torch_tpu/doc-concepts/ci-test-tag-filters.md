---
title: CI job membership via Bazel test-tag filters
type: doc-concept
provenance: doc
source: docs/developers/list_ci_tests_guide.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T02:38:46Z}
---
# CI job membership via Bazel test-tag filters

## Definition
Which tests a TorchTPU CI job runs is not written down anywhere directly. It is the result of three inputs: each CI job is a Bazel config in `.bazelrc` with a `--test_tag_filters` list, each test target in a `BUILD` file carries `tags`, and `.github/workflows/` binds each job to a machine type (CPU, TPU v5e, v6e, v7x). `ci/tools/list_ci_tests.py` evaluates Bazel's tag-filter algebra over all targets so you can ask "which jobs run this test?" or "which tests does this job run?".

## In torch_tpu (grounded)
The tool and the test BUILD graph sit outside the indexed source (`ci/` and `tests/` are not catalogued), so this page is prose-only. The selection rule it reproduces:
- A filter starting with `-` is negative, any other is positive. A target with **any** negatively-filtered tag is excluded, and exclusion always wins.
- If the job has any positive filters, the target must carry at least one of them. With no positive filters, everything not excluded runs.
- Example: `ci_tpu_v5_presubmit` = `-notest,-nobuild,-nopresubmit,-fails-on-tpu-v5,presubmit-v5`, so a test runs there only if tagged `presubmit-v5` and none of the negatives.

The doc's snapshot of job sizes: CPU jobs ~840 targets, TPU postsubmit/nightly ~140-150 per generation (v5e, v6e, v7x), TPU presubmits much smaller (v5e 97, v7x 33). Hardware tags such as `requires-tpu` / `requires-tpu-v5lite` keep TPU tests off CPU runners. The doc's worked example is `//csrc/ops/macros:kernel_test`, whose `presubmit-v7` tag is what pulls it into `ci_tpu_v7_presubmit`. Its presubmit list also includes a perf-relevant microbenchmark target (`//src/torch_tpu/_internal/performance/micro:qwen3_explore`) and `//tests/compile:*` torch.compile tests.

Useful invocations: `--list_jobs` (reads `.bazelrc` only, instant), `--test=<label>` (tags, BUILD file and every job that runs it; exit 1 if missing), `--jobs=` / `--tests='<glob>'` (composable filters), `--format=count`.

## Why it matters / when it applies
- **Per-generation coverage is uneven.** A kernel or lowering change can pass the v5e presubmit and still only be exercised on v7x in postsubmit or nightly. Before trusting "CI is green" for a TPU-generation-specific perf change (block sizes, Mosaic kernels), check which generations actually ran the relevant test.
- `fails-on-tpu-vN` tags are a quick inventory of known per-generation gaps.
- Before tagging a new op or kernel test, confirm with `--test` that the tags place it in the intended presubmit job. Watch for `Unknown` machine type or a 0 count, which means no runner or no matching tag.

## Connections
- Code concepts: [aten-kernel-authoring](../concepts/aten-kernel-authoring.md), [torch-compile-backend](../concepts/torch-compile-backend.md), [hardware-introspection](../concepts/hardware-introspection.md)
- Module catalogs: none - `ci/tools/list_ci_tests.py` is not in the indexed shards.
- Related doc-concepts: [python-version-support-policy](python-version-support-policy.md), [api-lifecycle-stages](api-lifecycle-stages.md)

## Source
Extracted from `docs/developers/list_ci_tests_guide.md`, listed under Tooling in `docs/developers/README.md` (both kept in place).
