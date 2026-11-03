---
title: Decode-side capacity preemption abort (P/D error contract)
type: doc-concept
provenance: doc
source: docs/user_guide/disaggregated_serving.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-11-03T02:35:38Z}
---
# Decode-side capacity preemption abort (P/D error contract)

## Definition
In a disaggregated deployment, a decode engine that runs out of KV-cache blocks would,
in stock vLLM, preempt `RUNNING` requests back to `waiting` and later **recompute their
prompts locally** - defeating the point of offloading prefill. The disaggregation guide
documents vllm-torchtpu's alternative: on a `kv_consumer` with
`kv_load_failure_policy="fail"` (upstream default), capacity-evicted requests are
**aborted** and returned to the router with a structured error so the router can
re-prefill elsewhere. Administrative `reset_prefix_cache` still requeues without
aborting.

## In vllm-torchtpu (grounded)
- [`patch_scheduler_init`](../catalog/src/vllm_torchtpu/core/abort_on_preemption.md#patch_scheduler_init)
  wraps vLLM's `Scheduler.__init__`; when
  [`_should_enable_abort_on_preemption`](../catalog/src/vllm_torchtpu/core/abort_on_preemption.md#_should_enable_abort_on_preemption)
  is true it installs [`_CapacityPreemption`](../catalog/src/vllm_torchtpu/core/abort_on_preemption.md#_CapacityPreemption),
  replacing `_preempt_request`, `reset_prefix_cache` and `update_from_output`.
- Enablement rule (code): `additional_config.abort_on_preemption` (must be a bool) wins
  when present; otherwise abort is on iff the engine is a `kv_consumer` with
  `kv_load_failure_policy == "fail"`. **Not in the doc:** setting
  `abort_on_preemption: true` on an engine that is not a `kv_consumer` raises
  `ValueError`.
- Error contract (doc): a single terminal output per victim with
  `finish_reason="error"`, `stop_reason="kv_cache_preempted"`, and
  `kv_transfer_params.kv_transfer_error` = `{status_code: 500, status_name:
  "model.KVCachePreempt", ...}`, emitted once the preemption step's `finished_req_ids`
  drain; preemption metrics (`vllm:num_preemptions`, `vllm:request_num_preemptions`,
  `PREEMPTED` events) are still recorded alongside `vllm:request_success{finished_reason="error"}`.
- A related decode-side guard: [`_validate_token_budget_fits_compile_sizes`](../catalog/src/vllm_torchtpu/platforms/tpu_platform.md#_validate_token_budget_fits_compile_sizes)
  rejects decode servers whose compile sizes cannot hold a locally recomputed prompt
  (its docstring cites exactly the "decode server resumes a preempted request" crash),
  which matters if you switch abort off.

## Why it matters / when it applies
- Local recompute on decode puts a prefill-sized step into a decode engine: a TPOT spike
  for every co-scheduled request, and possibly a bucket that was never compiled.
- Turn abort off (`{"abort_on_preemption": false}`) only if the decode pool's compile
  sizes and HBM budget can absorb recompute; turn it on with
  `kv_load_failure_policy="recompute"` to keep KV-load failures recoverable while still
  aborting capacity victims.
- Routers must treat `model.KVCachePreempt` as retryable.

## Connections
- Code concepts: [tpu-schedulers](../concepts/tpu-schedulers.md), [kv-transfer-and-disaggregated-serving](../concepts/kv-transfer-and-disaggregated-serving.md), [kv-cache-layout-and-hbm-budget](../concepts/kv-cache-layout-and-hbm-budget.md)
- Module catalogs: [abort_on_preemption](../catalog/src/vllm_torchtpu/core/abort_on_preemption.md), [tpu_platform](../catalog/src/vllm_torchtpu/platforms/tpu_platform.md)
- Related doc-concepts: [raiden-pd-disaggregation](raiden-pd-disaggregation.md), [token-padding-buckets](token-padding-buckets.md), [tpu-patch-registry](tpu-patch-registry.md)

## Source
Extracted from `docs/user_guide/disaggregated_serving.md` (section 4, kept in place).
