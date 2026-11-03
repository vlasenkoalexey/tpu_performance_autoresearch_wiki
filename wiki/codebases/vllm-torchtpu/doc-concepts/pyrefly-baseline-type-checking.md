---
title: Pyrefly type checking with counted baselines (pre-commit and full environment)
type: doc-concept
provenance: doc
source: docs/developers_guide/type_checking.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-11-03T02:35:38Z}
---
# Pyrefly type checking with counted baselines (pre-commit and full environment)

## Definition
Every PR is gated by two pyrefly runs. The pre-commit hook checks without third-party
packages (torch, jax and vllm resolve to `Any`) against `.pyrefly-baseline.json`;
Buildkite's "Type Check - Full Environment" runs `tools/typecheck_full.sh` inside the CI
image, where calls into torch, jax and vllm are checked against their real signatures,
against `.pyrefly-baseline-full.json`. Both go through `tools/check_pyrefly_baseline.py`,
which **counts** errors: each error needs its own baseline entry and each entry its own
error, matched on file, kind and message.

## In vllm-torchtpu (grounded)
Tooling only (`tools/`, `.pre-commit-config.yaml`); no runtime symbols. Mechanics from
the doc, checked against the hook config:
- The counting wrapper exists because pyrefly's own baseline lets one entry cover every
  repeat of a message in a file, so a fixed error coming back would go unnoticed.
- `tools/typecheck_full.sh` re-runs itself inside the nightly
  `vllm/vllm-torchtpu:nightly` image (built from the `dev` target with test deps; not
  `:latest`, which is the `prod` target) when started outside a container - Docker, no
  TPU. `TYPECHECK_IMAGE=<tag>` points it at a locally built `dev` image or a specific
  `nightly-<YYYYMMDD>-<commit>-<vllm-ref>` tag when the PR changes dependencies or the
  nightly lags `main`.
- Run ruff and pyrefly through pre-commit (`pyrefly==1.3.0` pinned), not from `PATH`.

## Fixing and baselines
- Fix the code; never add new baseline entries; keep runtime behavior unchanged (no
  `try/except` or fallback values to silence an error). Typical fixes: `assert x is not
  None` right before use, narrow into a local before storing on `self`, `typing.cast`
  where vLLM declares a looser type, initialize before conditionals.
- `# pyrefly: ignore[<code>]` on its own line only for false positives, always naming
  the code.
- Regenerate (`uvx pyrefly@1.3.0 check --update-baseline`, `bash tools/typecheck_full.sh
  --update-baseline`) only to delete entries for fixed errors; the diff must only delete
  (moved/renamed files excepted). A stale entry fails the check because it would hide the
  next error with the same message.

## Why it matters / when it applies
Not a performance mechanism, but a gate any perf PR touching `src/` must pass. The
full-environment check is the one that catches misuse of real torch / JAX / vLLM
signatures (for example after a pin bump that the
[plugin architecture](plugin-architecture-and-kernel-bridge.md) treats as load-bearing),
and the "no runtime change to satisfy the checker" rule is the type-checking face of
[fail-fast-and-fallback-policy](fail-fast-and-fallback-policy.md).

## Connections
- Related doc-concepts: [ci-test-markers-and-pipelines](ci-test-markers-and-pipelines.md),
  [fail-fast-and-fallback-policy](fail-fast-and-fallback-policy.md),
  [plugin-architecture-and-kernel-bridge](plugin-architecture-and-kernel-bridge.md)

## Source
Extracted from `docs/developers_guide/type_checking.md` (kept in place).
