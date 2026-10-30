---
title: 'Module: torchtitan/experiments/tpu/gdist.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/gdist.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.gdist`/
symbols:
  Environment.launch_config: Environment#launch_config().
  torchrun._run_deferred: torchrun()._run_deferred().
  torchrun: torchrun().
  Environment.default_nnodes: Environment#default_nnodes().
  Environment.default_run_id: Environment#default_run_id().
  Environment.rdzv_endpoint: Environment#rdzv_endpoint().
  Environment.local_addr: Environment#local_addr().
  Environment.name: Environment#name().
  LocalEnvironment: LocalEnvironment#
  Environment.run: Environment#run().
  LocalEnvironment.rdzv_endpoint: LocalEnvironment#rdzv_endpoint().
  Environment.default_nproc_per_node: Environment#default_nproc_per_node().
  LocalEnvironment.run: LocalEnvironment#run().
  LocalEnvironment.local_addr: LocalEnvironment#local_addr().
  LocalEnvironment.default_nnodes: LocalEnvironment#default_nnodes().
  Environment: Environment#
  LocalEnvironment.default_run_id: LocalEnvironment#default_run_id().
  LocalEnvironment.name: LocalEnvironment#name().
---
# Module: [`torchtitan/experiments/tpu/gdist.py`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/gdist.py)

## Classes
### <a id="Environment"></a>`Environment`
- def: [`torchtitan/experiments/tpu/gdist.py:85`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/gdist.py#L85)
- members:
  - <a id="Environment.default_nnodes"></a>`default_nnodes(self)` — [`L173`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/gdist.py#L173) — Default number of machines in this job.
  - <a id="Environment.default_nproc_per_node"></a>`default_nproc_per_node(self)` — [`L195`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/gdist.py#L195) — The default number of local ranks to run.
  - <a id="Environment.default_run_id"></a>`default_run_id(self)` — [`L132`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/gdist.py#L132) — The run_id to use for `torchrun`.
  - <a id="Environment.launch_config"></a>`launch_config(self, **kwargs)` — [`L208`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/gdist.py#L208) — `LaunchConfig`s for this environment.
  - <a id="Environment.local_addr"></a>`local_addr(self)` — [`L161`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/gdist.py#L161) — The address of the local node in rendezvous.
  - <a id="Environment.name"></a>`name(self)` — [`L188`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/gdist.py#L188) — The human-readable name of this environment.
  - <a id="Environment.rdzv_endpoint"></a>`rdzv_endpoint(self)` — [`L144`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/gdist.py#L144) — The rdzv_endpoint to use for `torchrun`.
  - <a id="Environment.run"></a>`run(self, fn)` — [`L100`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/gdist.py#L100) — Wraps `fn` w.r.t the environment.
- uses (calls/refs, reference-scoped): [`rdzv_endpoint`](gdist.md#LocalEnvironment.rdzv_endpoint), [`default_nnodes`](gdist.md#LocalEnvironment.default_nnodes), [`local_addr`](gdist.md#LocalEnvironment.local_addr), [`run`](gdist.md#LocalEnvironment.run), [`default_run_id`](gdist.md#LocalEnvironment.default_run_id), [`name`](gdist.md#LocalEnvironment.name)
- used by: [`_run_deferred`](gdist.md#torchrun._run_deferred), [`LocalEnvironment`](gdist.md#LocalEnvironment)

### <a id="LocalEnvironment"></a>`LocalEnvironment`
- def: [`torchtitan/experiments/tpu/gdist.py:252`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/gdist.py#L252)
- members:
  - <a id="LocalEnvironment.default_nnodes"></a>`default_nnodes(self)` — [`L302`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/gdist.py#L302)
  - <a id="LocalEnvironment.default_run_id"></a>`default_run_id(self)` — [`L272`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/gdist.py#L272)
  - <a id="LocalEnvironment.local_addr"></a>`local_addr(self)` — [`L298`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/gdist.py#L298)
  - <a id="LocalEnvironment.name"></a>`name(self)` — [`L306`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/gdist.py#L306)
  - <a id="LocalEnvironment.rdzv_endpoint"></a>`rdzv_endpoint(self)` — [`L294`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/gdist.py#L294)
  - <a id="LocalEnvironment.run"></a>`run(self, fn)` — [`L268`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/gdist.py#L268)
- uses (calls/refs, reference-scoped): [`Environment`](gdist.md#Environment)
- used by: [`_run_deferred`](gdist.md#torchrun._run_deferred), [`default_nnodes`](gdist.md#Environment.default_nnodes), [`default_run_id`](gdist.md#Environment.default_run_id), [`local_addr`](gdist.md#Environment.local_addr), [`name`](gdist.md#Environment.name), [`rdzv_endpoint`](gdist.md#Environment.rdzv_endpoint), [`run`](gdist.md#Environment.run)

## Functions
- <a id="torchrun._run_deferred"></a>`_run_deferred(*args)` — [`L50`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/gdist.py#L50)
- <a id="torchrun"></a>`torchrun(fn, *, nnodes=None, nproc_per_node=None)` — [`L21`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/gdist.py#L21) — A programmatic API to `torchrun`, used to spawn `n` copies of `fn`.

