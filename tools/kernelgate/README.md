# KernelGate

Verification gates for TPU kernel benchmarking (CLI: `kgate`). KernelGate productionizes a
benchmarking/verification methodology for candidate kernels (hand-written or
LLM-generated) against a reference workload: co-measured interleaved timing,
floor-normalized oracle parity (fp32, fp64 escalation), sensitivity coverage
batteries (family specs or declarative axes), parity-gated sweeps, a 4-leg
flag-fairness harness, a compile-only config-fit sweep, speed-of-light
roofline gates, tamper-evident run receipts, and a static prefilter for known
reward-hacking patterns.

Design rationale and the survey of published harnesses (KernelBench,
robust-kbench, Kevin, GPU MODE KernelBot, BackendBench, the FlashAttention
test suite) live in
`wiki/analyses/2026-07-15-kernel-benchmark-methodology-survey.md`.
The v0.2 gates distill the 2026-07-16/17 campaign incidents: the 21k
HIGHEST-baseline false-FAIL, the 37k both-flagged false-1.00x, the 4p v042
head-skip, and the 2p/4p VMEM OOM-grind.

## The problem-module protocol

Every benchmark case is a plain Python module:

```python
CONFIG = {...}                      # operating-point parameters
def create_inputs(...): ...         # -> tuple of input arrays (canonical seed 42)
def workload(*inputs): ...          # the computation under test
```

KernelGate consumes any module exposing this protocol, for both the baseline and
the candidate. Notes:

- **Entry resolution.** The baseline entry defaults to `workload`
  (`--baseline-entry` overrides). The candidate entry is auto-resolved:
  first the well-known names (`workload_cand`, `custom_workload`,
  `workload_pallas`, ..., `workload`), then an arity scan (exactly one public
  function whose required positional count matches the input count). Pass
  `--entry` when in doubt.
- **Seeds.** If `create_inputs` takes a `seed` parameter it is passed through;
  otherwise the seed is injected by temporarily monkey-patching
  `jax.random.key`/`PRNGKey` around the call (most campaign baselines hardcode
  seed 42).
- **Sibling imports.** A candidate may `import baseline` for CONFIG /
  create_inputs; the loader puts each module's directory on `sys.path`.

## Install / run

No packaging ceremony required — either:

```bash
pip install -e tools/kernelgate     # console script `kgate`
# or
PYTHONPATH=tools/kernelgate python -m kernelgate <cmd> ...
```

Dependencies: `numpy` plus whatever `jax` the execution environment provides
(deliberately unpinned; validated against JAX 0.9.0 on the benchmark pod's
`/opt/venv` and 0.10.x CPU).

Exit codes everywhere: `0` PASS, `1` advisory lint findings, `2` gate
FAIL / anomaly / INVALID.
Every command prints a human table, then the full machine-readable JSON after
a `--- KGATE-JSON ---` marker; `-o out.json` also writes it to a file.

## Commands

### `kgate measure` — co-measured interleaved timing

```bash
kgate measure --baseline baseline.py --candidate cand.py \
    [--seed 42] [--warmup 10] [--n-min 30] [--n-max 120] [--se-target 0.001] \
    [--chip-env TPU_VISIBLE_DEVICES=2 --chip-env LIBTPU_INIT_ARGS=...] [-o out.json]
```

Discipline enforced per run:

- baseline and candidate timed **interleaved** in the same process on the same
  buffers, `block_until_ready` fencing every call;
- **both orderings**: ordering A times the candidate *first* inside each
  iteration (candidate-before-reference), ordering B the baseline first;
  ordering-dependent speedups (>15% relative) are an anomaly;
- **adaptive trial count** per ordering: start n=30/leg, stop when both legs
  reach SE/mean < 0.001, hard cap n=120;
- the **candidate executes first in the process**, after the allocator is
  poisoned with NaN output-shaped buffers (via `jax.eval_shape`, no
  execution) — defeats result inheritance from reused allocator memory;
- **input byte-identity** (md5 of every input array before/after) — any
  mutation is an anomaly;
- candidate output must be finite and shape-match the baseline;
- p50 below a 1 ms dispatch window emits a sizing warning;
- full **environment capture** into the JSON: `LIBTPU_INIT_ARGS`, `XLA_FLAGS`,
  all `TPU_*`/`JAX_*` vars, jax/jaxlib/libtpu versions, device kind/count.

Reported per leg per ordering: p50/mean/std/min/n; plus pooled p50 ratio.
Any anomaly → nonzero exit. `--chip-env KEY=VAL` re-execs the command in a
child process with those vars set before `jax` is imported.

### `kgate parity` — floor-normalized oracle gate (fp32, fp64 escalation)

```bash
kgate parity --baseline baseline.py --candidate cand.py --seeds 42,43 \
    [--multiplier 2.0] [--oracle auto|fp32|fp64] [--floor-eps 1e-9] \
    [--scale-probes 10,50] [--scale-input 1] [--spec spec.py] \
    [--chunk "0:0,1:0,2:0"] [-o out.json]
```

- **Oracle**: the same canonical bf16 inputs are cast to float32 (float leaves
  only; integer index/length inputs pass through) and run through the
  *baseline* workload. x64 stays disabled. The oracle is a float32 recompute
  of the exact baseline semantics on the exact input values — not an fp32
  re-generation, which would draw different random values.
- **fp64 escalation (v0.2, the 21k fix)**: when the baseline computes in
  exact fp32 — `Precision.HIGHEST` matmuls, or fp32 inputs — the fp32
  recompute IS the baseline, the floor collapses to zero, and the gate
  degenerates to a ~1e-6 *absolute* tolerance that false-FAILs correct
  kernel-scale candidates. `--oracle auto` (default) escalates to a float64
  recompute (scoped x64, executed on the host CPU backend — TPUs have no
  f64) when the fp32 floor max_abs falls below `--floor-eps` or the baseline
  source mentions `Precision.HIGHEST`. The report and human output record
  which oracle graded each point (`oracle_used`).
- **Floor** = baseline(bf16) vs oracle error. **Gate**: candidate ≤
  `multiplier` × floor on **both** max_abs and mean_abs, and 100% finite.
- Guarded relative error is reported, **never gates**.
- `--scale-probes 10,50` re-runs the gate with one designated input rescaled
  (default index 1 = K in the attention families, or the spec's
  `SCALE_INPUT`) to sharpen softmax conditioning.
- `--chunk "0:0,1:0,2:0"` runs the oracle in size-1 slices of the listed
  inputs along the given axes (outputs concatenated along
  `--chunk-out-axis`) when the full-shape fp32 intermediate exceeds HBM —
  only valid for batch-like axes; you assert that by passing the flag.
- Any exception = FAIL with the traceback in the JSON. Nothing is swallowed.

### `kgate coverage` — sensitivity battery

```bash
kgate coverage --baseline baseline.py --candidate cand.py \
    --spec tools/kernelgate/kernelgate/specs/paged_attention.py [-o out.json]
```

A family spec module defines `perturb_regions(baseline_module, inputs)`
returning probes: perturbed inputs + a boolean **affected mask** over the
output. For each probe KernelGate asserts the candidate matches the baseline's
sensitivity structure exactly:

- unaffected set: **bit-identical** between clean and perturbed candidate
  runs (any change = leak / aliasing / causal violation);
- affected set: candidate must respond above the power threshold
  (silence = skipped work);
- spec sanity is checked first (baseline must itself be silent on the
  unaffected set and loud on the affected set, else `SPEC_ERROR` — the probe
  is not charged to the candidate).

Shipped specs (in `kernelgate/specs/`), derived from the campaign verifier
batteries:

| spec | family layouts | probes |
|---|---|---|
| `causal_blocks.py` | causal MHA/GQA, q/k/v = first 3 inputs, `(B,H,S,D)` or `(H,S,D)` | per-k-block V spikes (8 blocks) + boundary column spikes |
| `gqa_isolation.py` | `(Hq,S,D)` q with `(Hkv,S,D)` k/v | K- and V-side per-KV-head group isolation |
| `paged_attention.py` | paged decode `(queries, k_pages, v_pages, kv_lens, page_indices, cu_q_lens)` | GQA group isolation, per-sequence isolation, invalid-token no-leak |

**Declarative specs (v0.2, the v042 fix).** Instead of a `perturb_regions`
module, `--spec` also accepts a `.json` / `.yaml` file (or a `.py` defining
`SPEC` / `AXES`) that just names the problem's semantic axes:

```yaml
axes:
  - {name: head, input: 0, size: 8, input_slice: "[i]", output_slice: "[i]"}
scale: 2.0      # perturbation: slice * scale (+ optional `add` for zero-heavy slices)
```

kgate generates one probe per (axis, slot) — perturb the input slice, assert
the mapped output region moves and everything else is bit-identical — and
additionally screens the clean candidate output for dead slots (all-NaN /
all-zero). A v042-class kernel (computes only head 0 of the group) FAILs
with the skipped heads named in the per-axis table + `violations` list.
Index expressions are evaluated as `np.s_<expr>` with `i` = slot
(`"[:, i]"`, `"[i // 4]"`, ...); Python-module specs may pass callables.

### `kgate sweep` — parity-gated grid sweep

```bash
kgate sweep --baseline baseline.py --candidate cand.py \
    --params "bq=512,1024,2048;bk=128,256,512" [--n-min 10] [-o out.json]
```

Full grid over the candidate entry's static kwargs. Each config is
quick-parity-gated (1 seed, oracle computed once and reused) and only then
timed (adaptive, n ≥ 10). Configs failing parity are reported as
`PARITY_FAIL` and are **never timed and never eligible for argmin**; configs
that crash are `ERROR` rows and the sweep continues.

### `kgate flags` — 4-leg flag-fairness harness (v0.2, the 37k fix)

```bash
kgate flags --baseline baseline.py --candidate cand.py \
    --flag "LIBTPU_INIT_ARGS=--xla_tpu_scoped_vmem_limit_kib=131072" \
    [--seed 42] [--warmup 5] [-n 20] [-o out.json]
```

A TPU flag is process-global — exporting it once in the shell applies it to
BOTH legs of a "baseline vs candidate" comparison and reports 1.00x for a
real flag win (the 37k incident). `kgate flags` runs FOUR legs, each in its
own fresh process with a fresh `JAX_COMPILATION_CACHE_DIR` per flag value:
naive-default, naive-flagged, cand-default, cand-flagged (the candidate may
be the same file as the baseline = a flag-only cell). It reports all four
p50s and BOTH framing ratios explicitly labeled:

- `flag_only_ratio`   = naive_default / naive_flagged — the deployable flag win;
- `kernel_cell_ratio` = naive_flagged / cand_flagged — the kernel win at fixed flag;
- `end_to_end_ratio`  = naive_default / cand_flagged.

When baseline and candidate resolve to the same module + entry, the harness
emits the **same-graph trap warning** (kernel_cell_ratio is 1.00x by
construction) and points at flag_only_ratio; a flag already exported in the
parent environment at the flagged value is an ANOMALY (the "-default" legs
would not be default). The parent process never imports jax, so the command
is safe to drive from a supervisor that must not grab a chip.

### `kgate fit` — compile-only config-fit sweep (v0.2, the 2p/4p OOM-grind fix)

```bash
kgate fit --candidate cand.py --configs '[{"bq":512,"bk":256}, {"bq":1024,"bk":512}]' \
    [--baseline baseline.py] [--run-once] [-o out.json]
```

Answers "which configs fit the chip's VMEM/HBM envelope" without timing
anything. For each config (static kwargs on the candidate entry; `--configs`
is inline JSON or a file path) it jit-lowers + compiles (`--run-once` also
executes once, catching allocation-time failures), catches
RESOURCE_EXHAUSTED / Mosaic VMEM errors, and parses the requested-vs-limit
numbers out of the error text — Mosaic `44.05M > 32M` / `Used 44.05M of
32.00M`, XLA HBM `Used 34.00G of 30.75G` / `temporaries (64.00G) exceeds
available HBM (31.25G)`, and byte-count `size N ... limit of M` forms; the
raw error line is kept in the row. Output is a TSV table:
`config | fits | requested | limit | error_class`. An OOM never crashes the
sweep.

### `kgate verify-receipt` — audit a run receipt (v0.2)

```bash
kgate verify-receipt receipt.json [--skip-inputs]
```

Every `measure` / `parity` / `flags` run also writes `receipt.json`
(`--receipt PATH` / `--no-receipt`): {kgate_version, git_sha, timestamp,
oracle_type, input_shapes, inputs_sha256, outputs_sha256, floor, thresholds,
verdict, argv} plus a sha256 self-hash over the canonical JSON.
`verify-receipt` recomputes the self-hash (any edit — verdict, floor, p50 —
is detected), cross-checks the verdict against the recorded gate/ratio
arithmetic (a re-hashed forgery must also keep the numbers consistent), and
regenerates the inputs from the recorded module + seed to compare hashes
(`--skip-inputs` on a machine without the module). Exit 0 only on `OK`.
The self-hash is integrity, not authentication — it detects editing, not a
determined forger; pair with trusted storage for that.

### `kgate roofline` — speed-of-light hard gate

```bash
kgate roofline --candidate-json measure.json --flops 2.2e12 --bytes 4.3e8 \
    [--peak-tflops 918 --peak-gbps 1640]
```

Measured p50 *faster* than `max(flops/peak_compute, bytes/peak_bw)` is
physically impossible ⇒ exit `INVALID`. Otherwise reports achieved TFLOP/s,
GB/s, and % of light. Peaks default from the device kind recorded in the
measure JSON (v4/v5e/v5p/v6e table in `roofline.py`); override for other
hardware.

FLOP accounting for the attention families (JAXBench-harness formulas, as
used in the campaign baselines — full S×S, no causal halving):

| family | FLOPs |
|---|---|
| causal MHA (1p) | `4·B·H·S²·D` |
| GQA/sparse (4p) | `4·Hq·S²·D` |
| flex + bias (5p) | `4·B·H·S²·D + B·H·S²` |
| paged decode (6p) | `num_seqs·Hq·4·S·D` |

### `kgate lint` — static prefilter (advisory)

```bash
kgate lint --candidate cand.py
```

AST checks: try/except around the compute path (silent fallback), calling the
baseline workload from the compute path (result relabeling), trivial input
passthrough, no compute primitives in the module. Exit `1` on findings —
advisory by design: cheap, evadable, still worth running first. A clean lint
proves nothing.

## Recommended gate order

```
lint  →  fit (config envelope, when sweeping block sizes)
      →  parity (2 seeds, + scale probes)  →  coverage (family or declarative spec)
      →  measure  →  roofline
      →  flags (when the claim involves a flag — both framings, always)
      →  verify-receipt (supervisor side, on the worker's receipt.json)
```

A candidate is only reportable when parity + coverage PASS, measure is
anomaly-free, and roofline is not INVALID; a flag-assisted claim is only
reportable in the `kgate flags` framing that matches the cell (flag-only vs
kernel-under-flag). (The mechanism-level profiler audit — "the custom call
actually ran" — stays with the kernel-verifier agent flow; KernelGate's
scope is the numerical + timing gates.)

## Regression fixtures

`tests/fixtures/` pins known-good and known-bad kernels from campaign history
(verbatim copies, attribution headers in each file). The known-bad ones are
the gates' regression suite — each MUST keep failing:

| fixture | class | must fail |
|---|---|---|
| `sparse_4p/bad_v002_coverage.py` | output written before accumulation completes (block-unit confusion) | parity, coverage |
| `sparse_4p/bad_v013_double_scale.py` | double softmax scale (family pre-scales q in create_inputs) | parity |
| `flex_5p/bad_v005_noncompiling.py` | Mosaic lowering failure | parity must FAIL-with-traceback, not crash |
| `paged_6p/bad_v003_gqa_aliasing.py` | GQA group/head einsum aliasing | coverage (group isolation) |

The v0.2 incident classes are pinned as inline-source regression tests
rather than fixture files: the 21k HIGHEST false-FAIL
(`tests/test_parity_fp64.py` — the correct candidate must PASS under the
escalated oracle and reproducibly false-FAIL under `--oracle fp32`), the 37k
both-flagged false-1.00x (`tests/test_flags.py` — the same-graph invocation
must emit the trap warning), and the v042 head-skip
(`tests/test_coverage_declarative.py` — heads 1..N must be named).

Known-good: `flash_1p/good_ag_final.py` (~2.8–3.1x), `flex_5p/good_ag_final.py`,
`paged_6p/good_ag_final.py` — must PASS parity (+ coverage where a spec applies).

## Tests

```bash
python -m pytest tests/ -q                 # CPU-portable subset (logic, lint,
                                           # protocol, tiny end-to-end gates)
KGATE_TPU=1 python -m pytest tests/ -q     # + real-kernel regression gates
                                           # (requires a TPU chip)
```

## Known limitations (v0.2)

- Forward-pass only; no VJP/backward parity yet (survey item 8).
- Single-chip; no multi-chip/collective kernels.
- Timing is host-wall interleaved p50 only; the multi-estimator agreement
  check (xprof device-time vs host wall) is not wired in (survey item 4).
- Output-buffer *donation* is not used (inputs are reused across interleaved
  iterations by design); allocator poisoning + candidate-runs-first cover the
  memory-reuse exploit class instead.
- Coverage probes hold their perturbed input copies on device for the run's
  duration — large-footprint families (paged KV caches) need headroom.
- Cache-state policy (survey item 6): inputs stay HBM-resident across trials;
  this is recorded implicitly by the methodology, not configurable yet.
