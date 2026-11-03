---
title: Derive, don't declare (and minimize knobs)
type: doc-concept
provenance: doc
source: docs/developers_guide/coding_guidance.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-11-03T02:35:38Z}
---
# Derive, don't declare (and minimize knobs)

## Definition
One of the two meta-principles of the vllm-torchtpu coding guidance: any value
recoverable from tensor shapes, dtypes, hardware APIs, sharding specs or cost models is
**derived at the point of use**, never duplicated into a config knob, env var, magic
number or redundant member variable. Its companion (section 6, "minimize surface
area") says every new argument, flag and env var must justify itself, and tuning values
are never knobs.

## The rules
| ID | Rule |
|---|---|
| R-4.1 | No string- or attribute-probing dispatch (no model-name matching, no `getattr` with default on config, no dtype-by-string); key behavior on capabilities (`model_config.uses_mrope`) |
| R-4.2 | Derive from argument shapes (`block_size = w.shape[-1] // scale.shape[-1]`), not caller-supplied duplicates |
| R-4.3 | No env reads inside jitted/compiled functions - read in a thin un-jitted wrapper and pass as a static argument; an env read at trace time is baked into the graph and later changes silently do nothing |
| R-4.4 | No hard-coded hardware constants - query `pltpu.get_tpu_info()`, `get_device_name()`, `get_dtype_packing()` |
| R-4.5 | No magic mesh-axis strings - shared constants such as `EP_AXIS_NAME` |
| R-4.6 | Config flows through vLLM's typed config, never `additional_config` dict digging; infer DP from the mesh |
| R-4.7 | Typed containers over dicts/bools/sentinels; one enum over N booleans |
| R-6.1 / R-6.2 | A new env var/flag only as (a) a migration-window backend selector with a deletion condition, (b) a debug escape hatch that does not change defaults, or (c) a documented quality/perf dial with the exact mode still available. **Never** block sizes, thresholds or buffer sizes |
| R-6.3 - R-6.6 | Collapse special cases (MLA as attention with `num_kv_heads=1`; decode and spec-decode must not behave differently); one sharding formulation for DP and non-DP; gate fixes on the mechanism variable, not the model where the bug surfaced; branch on declared checkpoint metadata |

## In vllm-torchtpu (grounded)
- R-4.5's in-repo good example: [`EP_AXIS_NAME`](../catalog/src/vllm_torchtpu/distributed/ep_mesh.md#EP_AXIS_NAME)
  with [`build_ep_mesh`](../catalog/src/vllm_torchtpu/distributed/ep_mesh.md#build_ep_mesh).
  The doc itself names the literal `P("model")` in `layers/core/` (e.g.
  `gdn_attention.py`, `attention_interface.py`) as the anti-pattern still present.
- R-4.3 / R-2.6 in practice: env vars are read only through the `envs` registry
  ([`environment_variables`](../catalog/src/vllm_torchtpu/envs.md#environment_variables.environment_variables)),
  and process-level startup mutation (`LIBTPU_INIT_ARGS`, caches) happens in one place,
  `env_override.py`, before libtpu loads
  ([`set_libtpu_flag_default`](../catalog/src/vllm_torchtpu/env_override.md#set_libtpu_flag_default)).
  See [env-var-registry-and-compile-key](env-var-registry-and-compile-key.md) for the
  mechanism, including how every registered env var enters the compile cache key.
- R-6.2's "tuning values are tables, not knobs" is implemented by the per-kernel
  [tuned-block-size-tables](tuned-block-size-tables.md).

## Why it matters / when it applies
The appendix's rationale is a perf argument as much as a correctness one: in an
inference stack a stale declared value rarely crashes - it yields silently wrong numerics
or a **perf cliff** (wrong tile, wrong mesh axis, wrong packing), the most expensive
class of bug to detect. Derived values survive vLLM upstream churn; declared copies go
stale with no error. For an optimization loop this means: prefer a derivation or a
tuned-table entry over a new env var, and expect reviewers to reject tuning knobs.

## Doc vs code at this commit
- Known exceptions to R-4.4 remain: `TpuPlatform.fp8_dtype` compares the device name to
  `"tpu v6e"`, and the quantized-matmul tuned table hard-codes per-generation VMEM
  limits (see [kernel-hardware-resource-rules](kernel-hardware-resource-rules.md)).
- Several perf-tuning env vars exist despite R-6.2 (for example
  [`MOE_FUSED_EP_V2_HEIGHT_RUNGS_OVERRIDE`](../catalog/src/vllm_torchtpu/envs.md#MOE_FUSED_EP_V2_HEIGHT_RUNGS_OVERRIDE),
  [`TPU_PP_CHUNK_SLACK`](../catalog/src/vllm_torchtpu/envs.md#TPU_PP_CHUNK_SLACK)); the
  `check-env-reads` pre-commit hook is a ratchet against `tools/env_reads_baseline.txt`,
  so pre-existing direct `os.environ` reads outside `envs.py` are tolerated until
  migrated.

## Connections
- Code concepts: [distributed-parallelism-and-meshes](../concepts/distributed-parallelism-and-meshes.md),
  [compilation-and-graph-capture](../concepts/compilation-and-graph-capture.md),
  [attention-and-layer-core](../concepts/attention-and-layer-core.md),
  [tpu-platform](../concepts/tpu-platform.md)
- Module catalogs: [envs](../catalog/src/vllm_torchtpu/envs.md),
  [env_override](../catalog/src/vllm_torchtpu/env_override.md),
  [distributed/ep_mesh](../catalog/src/vllm_torchtpu/distributed/ep_mesh.md)
- Related doc-concepts: [env-var-registry-and-compile-key](env-var-registry-and-compile-key.md),
  [tuned-block-size-tables](tuned-block-size-tables.md),
  [kernel-hardware-resource-rules](kernel-hardware-resource-rules.md),
  [plugin-architecture-and-kernel-bridge](plugin-architecture-and-kernel-bridge.md),
  [fail-fast-and-fallback-policy](fail-fast-and-fallback-policy.md)

## Source
Extracted from `docs/developers_guide/coding_guidance.md` sections 4 and 6 and the
appendix (kept in place).
