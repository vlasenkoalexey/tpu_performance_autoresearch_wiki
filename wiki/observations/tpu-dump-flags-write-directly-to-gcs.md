---
title: "All four TPU artifact classes (HLO, LLO, Mosaic, xprof trace) write directly to gs://"
type: observation
tags: [profiling, gcs, llo, mosaic, hlo, xprof, kernel-lane, tpu, v6e]
created: 2026-08-19
updated: 2026-08-19
---

Every artifact class the kernel loop produces can be written **straight to a `gs://` URI** — no
local disk, no copy-back step. Validated end-to-end on v6e (`TPU v6 lite`) 2026-08-19. This makes
a remote executor (a GKE pod) **stateless for artifacts**, which removes the failure mode that
destroyed two full-model profile captures.

## What was observed

Four probes, each a minimal JAX program on one chip, dumping to `gs://torchtitan-assets/_probe/<tag>`
and then listing the prefix:

| Artifact | Flag / API | Objects written | Verdict |
|---|---|---|---|
| HLO | `XLA_FLAGS=--xla_dump_to=gs://…` | 65 | **works** |
| **LLO** | `LIBTPU_INIT_ARGS=--xla_jf_dump_to=gs://… --xla_jf_dump_llo_text=true` | **823** | **works** |
| Mosaic MLIR | `LIBTPU_INIT_ARGS=--xla_mosaic_dump_to=gs://…` | 21 | **works** |
| xprof trace | `jax.profiler.trace("gs://…")` | `xplane.pb` + `trace.json.gz` | **works** |

Only the HLO row was previously documented ([xla-compiler-flags](../concepts/xla-compiler-flags.md):
*"Supports `gs://...` via TF GCS plugin"*). The mechanism is the same for the other three: libtpu
ships `GcsFileSystem` (315 symbol hits — see
[vllm-torchtpu-profiler-bypasses-gcs-handler](vllm-torchtpu-profiler-bypasses-gcs-handler.md)), and
all three writers reach it. Prior kernel-lane recipes
([llo-dumps-and-kernel-profiling-tracks-verified-on-v6e](llo-dumps-and-kernel-profiling-tracks-verified-on-v6e.md),
[`kernel-verifier`](../../.claude/agents/kernel-verifier.md) Step 3, BRIEFS §1) show these flags
**only with local paths** (`/tmp/jf_dump`), so the GCS capability was available but unused.

> [!warning] The Mosaic result required a control — the obvious test is confounded
> A first probe dumped Mosaic from a plain `jnp` matmul and found **0 objects**, which reads as
> "gs:// unsupported". It is not: a matmul compiles **no Pallas kernel**, so there was nothing to
> dump to any destination. Re-run with a real `pl.pallas_call`, local and GCS legs produced
> **21 objects each** — identical. Any future probe of a dump flag must run a program that
> actually exercises the dumper, and should carry a local-dir control leg.

## How to see it

```bash
# LLO straight to GCS (the kernel loop's main profiling input)
LIBTPU_INIT_ARGS="--xla_jf_dump_to=gs://<bucket>/<exp>/jf --xla_jf_dump_llo_text=true" \
TPU_VISIBLE_DEVICES=0 python workload.py
gsutil ls -r gs://<bucket>/<exp>/jf | head
```

`xprof-cli` reads a `gs://` `--logdir` identically to a local dir (serverless `XPROF_MODE=local`),
so `get_llo_fit_summary` and the rest of the analysis chain need no change.

**kgate needs no modification either**: it captures via `jax.profiler.trace(args.trace_dir)`
([`flags.py:249`](../../tools/kernelgate/kernelgate/flags.py)), so `--trace-dir gs://…` already
works. The `--chip-env KEY=VAL` re-exec is likewise the supported way to inject
`LIBTPU_INIT_ARGS` / `XLA_FLAGS` before JAX initializes.

## Implications

- **A remote kernel executor can be stateless.** With every dump target a `gs://` URI, a GKE pod
  needs no sized scratch volume, no `kubectl cp` artifact-return path, and cannot be evicted for
  `ephemeral-storage`. Enforcing `gs://` in cluster mode is strictly simpler than supporting local
  paths plus retrieval.
- **It removes a known capture-killer.** A full 1T-class serving model (TP=32 / 4 hosts) put 31 GB of compile cache +
  15 GB of HLO on the node, hit `DiskPressure`, and all four pods were **Evicted** (rank 0 exit
  137) — the traces were lost. Multi-GB K1 `jf_dump`s carry the same risk locally (three
  concurrent runs reached 94 % disk, 2026-07-21).
- **Local runs benefit too** — a `gs://` target sidesteps the "prune the dump as soon as its digest
  is transcribed" disk-pressure rule in
  [`kernel_experiments/program.md`](../kernel_experiments/program.md) Profiling tier 1.
- **Caveat — `--xla_jf_dump_to` is not universally available.** BRIEFS §135 records it SIGABRTing
  (missing `vmem_report_header.tmpl`) across six consecutive sessions on some boxes, with
  `--xla_mosaic_dump_to` as the working substitute for structural firing audits. This probe did
  not hit it on this v6e box. A GCS destination does not change that failure mode either way.
- Validated on **v6e** and (HLO / Mosaic / LLO) on **v7x** — see the credentials section below.

## Credentials: a read-only node scope does NOT mean "this cluster cannot dump to GCS"

The writers above need a *credential*, and on GKE the obvious one is the node service account —
whose token is capped by the node pool's **oauth scopes**. A pool created with
`devstorage.read_only` therefore fails every `gs://` dump, and the natural (wrong) conclusion is
that the cluster is unusable for artifact capture and the run must move elsewhere.

**Try Workload Identity before relocating.** A pod that runs as a KSA annotated with
`iam.gke.io/gcp-service-account: <GSA>` gets its token from the GKE metadata server as that GSA,
and **node oauth scopes do not apply to it** — so a read-only node pool still dumps to GCS.
No service-account key file is involved, and none should be: mounting a key is the failure-prone
path this replaces.

```yaml
spec:
  serviceAccountName: <ksa-bound-to-a-gsa-with-storage-write>   # NOT hostNetwork: true
```

Checks, in order — each one distinguishes a different failure:

```bash
# 1. which identity does the pod actually have? (node SA => WI is not in effect)
curl -sH 'Metadata-Flavor: Google'   http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/email
# 2. can that identity write THIS bucket? (403 here is IAM, not scopes)
#    plain upload with the metadata token, then confirm the object from outside the pod
# 3. only then: do the dump FLAGS write? (they use libtpu's own GcsFileSystem, not gcloud)
```

**Two traps this sequence catches**, both observed 2026-08-19 on a `tpu7x` pool whose nodes were
`devstorage.read_only`:

- **Identity resolving is not permission.** The metadata email returned the WI GSA while writes to
  one bucket returned **403** and another succeeded — bucket IAM is a separate axis from both node
  scopes and WI. Grade on an object that lands, verified from *outside* the pod; an HTTP 200 or an
  accepted flag is not evidence a file exists.
- **`hostNetwork: true` defeats WI**, because the pod then reaches the node's metadata server
  directly. Manifests that need host networking cannot use this route; a plain exec/dev pod can.

With WI in place on that read-only pool, the dump flags wrote straight to `gs://`:
**HLO 64 objects, Mosaic MLIR 22, LLO 1,399** — counts confirmed by listing the prefix from a
workstation, not from the pod that wrote them.

> [!warning] `jax.profiler.trace` is the one class that did NOT work on that v7x image
> It **SIGSEGV**s (signal 11) — and the control run proves this is not a GCS issue: tracing to a
> **local** directory crashes identically. So the trace row of the table above is v6e-verified but
> **generation- and image-sensitive**, while the three compiler-side dumps (HLO / Mosaic / LLO)
> worked on both. Anything depending on `jax.profiler.trace` — `kgate verify --capture`
> ([`flags.py:249`](../../tools/kernelgate/kernelgate/flags.py)) — must be probed on the target
> image before a capture is planned around it.

## Seen in

- Probes run 2026-08-19 on the local v6e-4 workstation, chip 0 (`flock`-serialized), JAX + current
  libtpu. Probe scripts were scratch; the table above is the durable record.
- Workload-Identity leg: 2026-08-19, a single-host `tpu7x` GKE pod on a `devstorage.read_only`
  node pool, JAX 0.10.2. Object counts listed from outside the pod.
- Motivating context: designing a `kubectl exec` remote executor for the kernel lane
  ([layer-epilogue-fusion binding](../kernel_experiments/layer-epilogue-fusion/pallas/program.md)).

## See also

- [vllm-torchtpu bypasses TorchTPU's GCS-capable xprof trace handler](vllm-torchtpu-profiler-bypasses-gcs-handler.md) — why *vLLM* traces could not reach GCS (a PyTorch handler substituted for the GCS-capable one); the kernel lane does not use that path
- [LLO dumps + kernel-profiling tracks verified on v6e](llo-dumps-and-kernel-profiling-tracks-verified-on-v6e.md) — the flag set, local-path form
- [xla-compiler-flags](../concepts/xla-compiler-flags.md) · [xla-dump-flags](../concepts/xla-dump-flags.md)
- [profile-analyzer-index](../profile-analyzer-index.md) — the analysis-side catalog

## Sources

- Direct measurement, 2026-08-19 (this wiki's local v6e box).
- `tools/kernelgate/kernelgate/flags.py:249` — `jax.profiler.trace(args.trace_dir)`.
