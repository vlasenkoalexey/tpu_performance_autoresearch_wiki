---
title: CI hardware routing - pytest markers, Buildkite lanes and the perf lane
type: doc-concept
provenance: doc
source: docs/developers_guide/testing_and_ci.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-11-03T02:35:38Z}
---
# CI hardware routing - pytest markers, Buildkite lanes and the perf lane

## Definition
vllm-torchtpu's CI runs on Buildkite with every step in a Kubernetes pod. Pytest markers
decide which hardware a test lands on: unmarked tests run on CPU pods with the JAX CPU
backend, `tpu_test` on a single-host TPU v7x slice, `multichip` on a larger v7x slice.
`nightly` decides only *when* a test runs, never on what hardware. Pipelines are split
into lanes (`tests`, `integration`, `perf`, `verify`); the perf/eval lane that runs the
[benchmark harness](benchmark-harness-and-regression-gates.md) is gated by PR labels and
nightly schedules.

## In vllm-torchtpu (grounded)
The routing is defined in `pyproject.toml` (`[tool.pytest.ini_options]` markers),
`tests/conftest.py` and `.buildkite/pipeline_*.yml`; none of it is in the indexed
package, so this page has no catalog symbols.

| Marker | CI hardware | Notes |
|---|---|---|
| (unmarked) | CPU pod, `JAX_PLATFORMS=cpu` | Mocked TPU devices; module imports must work on CPU because collection precedes marker filtering |
| `tpu_test` | TPU v7x 1x1x1 | Required for anything using `torch.device("tpu")`, including tests taking the `device` fixture (`--use-tpu` defaults on) |
| `multichip` | TPU v7x 2x2x1 | TP/EP/DP collectives and multi-chip kernel tests |
| `spawns_tpu_workers` | Multi-chip slice | Spawns a `torch.distributed.run` group; ordered to run before in-process TPU tests in the same session |
| `nightly` | Nightly workflow (`NIGHTLY=1`) | Must still carry `tpu_test` / `multichip` if it needs a TPU |
| `omni` | v7x 1x1x1, `-omni` image | `tests_omni/` (vllm-omni multimodal / diffusion) |

Local equivalents (matching the pipeline marker expressions):
`JAX_PLATFORMS=cpu pytest tests/ -m "not tpu_test and not multichip and not nightly"`;
on a TPU VM `-m "tpu_test and not nightly and not multichip"`; on an 8-device host
`-m "not nightly and multichip"`. Speculative-decoding e2e tests
(`tests/entrypoints/llm/test_speculative_decoding.py`) run in their own 2-chip and
8-chip steps with longer timeouts (1800 s / 3600 s).

## Lanes and gating
- `pipeline_perf.yml` (perf + eval) does not run on post-merge builds; on PRs only with
  the `run-perf-eval` label, or `run-full-ci` (sets `NIGHTLY=1`, runs every lane). The
  02:00 PT nightly runs all of it; scheduled builds with `CI_LANES=perf` run the perf lane
  alone in between. The integration pipeline also runs the lane because its LKG
  promotion waits on two perf steps.
- TPU CI needs the `ready` label (a maintainer reviews fork PRs first; on fork PRs every
  push removes the label). `skip-tpu-ci` runs only the type check and CPU unit tests.
  `oncall-fix` jumps the TPU queue for build-breakage fixes.
- Nightly images (`ci`, `dev`, `prod`) are published from `main`; the `dev` image on
  Docker Hub (`vllm/vllm-torchtpu:nightly`) is what local full type checking uses
  ([pyrefly-baseline-type-checking](pyrefly-baseline-type-checking.md)).
- Pre-commit gates include `ruff`, `pyrefly`, `pymarkdown`, `check-env-reads` (env reads
  must go through `envs.py`) and `check-b023-baseline` (no new loop-variable closures in
  Pallas kernel files under `kernels/`, where `pl.when` / `pl.loop` bodies make B023 a
  real hazard).

## Why it matters / when it applies
- The coding guidance requires tests on the smallest hardware that exercises the behavior
  (R-8.5) and correct markers (R-8.4: green CI does not mean the code ran - check the
  pipeline ignore lists and markers). Perf measurement never goes in `tests/` (R-8.9).
- `main` follows a revert-on-breakage policy: a PR that regresses nightly benchmarks or
  integration suites is reverted, not fixed forward (CONTRIBUTING; PR-2). PRs over ~500
  lines of core logic need an RFC issue first.
- v7x is the generation CI validates continuously (see
  [tpu-generations-and-logical-devices](tpu-generations-and-logical-devices.md)), so v7x
  slice shapes are where per-PR correctness evidence comes from.

## Doc vs code at this commit
- Chip vs device wording is inconsistent: the doc's marker table says `tpu_test` = "1 chip"
  and `multichip` = "4 chips" (2x2x1), while its section headings say "2-Chip Queue" and
  "8-Chip Queue" and `pyproject.toml` describes `multichip` as running "on an 8-chip
  agent". The headings and pyproject count devices (a v7x chip exposes two), the table
  counts chips.
- The doc describes `check-env-reads` as verifying that **all** env reads go through
  `envs.py`; the hook is a ratchet against `tools/env_reads_baseline.txt`, so existing
  direct reads are tolerated and only new ones fail. `check-b023-baseline` is likewise a
  baseline ratchet.

## Connections
- Code concepts: [speculative-decoding](../concepts/speculative-decoding.md),
  [omni-diffusion-support](../concepts/omni-diffusion-support.md),
  [distributed-parallelism-and-meshes](../concepts/distributed-parallelism-and-meshes.md)
- Related doc-concepts: [benchmark-harness-and-regression-gates](benchmark-harness-and-regression-gates.md),
  [pyrefly-baseline-type-checking](pyrefly-baseline-type-checking.md),
  [perf-evidence-standard](perf-evidence-standard.md),
  [tpu-generations-and-logical-devices](tpu-generations-and-logical-devices.md),
  [env-var-registry-and-compile-key](env-var-registry-and-compile-key.md)

## Source
Extracted from `docs/developers_guide/testing_and_ci.md` (which includes
`.buildkite/README.md`) and `docs/developers_guide/contributing.md` (which includes
`CONTRIBUTING.md`) (kept in place).
