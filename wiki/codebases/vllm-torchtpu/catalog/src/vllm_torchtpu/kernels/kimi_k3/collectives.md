---
title: 'Module: src/vllm_torchtpu/kernels/kimi_k3/collectives.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/kimi_k3/collectives.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.kimi_k3.collectives`/
symbols:
  ring_collective: ring_collective().
  project_reduce_scatter: project_reduce_scatter().
  mla_preprocess: mla_preprocess().
  gather_moe_inputs: gather_moe_inputs().
  _all_gather_kernel: _all_gather_kernel().
  ring_collective.local: ring_collective().local().
  _all_gather_kernel.peer: _all_gather_kernel().peer().
  _all_gather_kernel.store: _all_gather_kernel().store().
  _all_gather_kernel.receive: _all_gather_kernel().receive().
  _gather_project_kernel.receive: _gather_project_kernel().receive().
  pack_mla_gate: pack_mla_gate().
  ring_tables: ring_tables().
  _gather_project_kernel.remote: _gather_project_kernel().remote().
  gather_project: gather_project().
  mla_chip_layout: mla_chip_layout().
  _reduce_scatter_kernel.ring_coords: _reduce_scatter_kernel().ring_coords().
  _gather_project_kernel.finish.copy: _gather_project_kernel().finish().copy().
  mla_preprocess.local: mla_preprocess().local().
  _reduce_scatter_kernel: _reduce_scatter_kernel().
  _project_ring_kernel: _project_ring_kernel().
  project_reduce_scatter.local: project_reduce_scatter().local().
  _gather_project_kernel: _gather_project_kernel().
  _gather_project: _gather_project().
  gather_project.local: gather_project().local().
  _project_ring_kernel.ring_coords: _project_ring_kernel().ring_coords().
  _gather_project_kernel.peer: _gather_project_kernel().peer().
  _reduce_scatter_kernel.enter: _reduce_scatter_kernel().enter().
  _reduce_scatter_kernel.wait: _reduce_scatter_kernel().wait().
  _reduce_scatter_kernel.forward: _reduce_scatter_kernel().forward().
  _all_gather_kernel.enter: _all_gather_kernel().enter().
  _all_gather_kernel.forward: _all_gather_kernel().forward().
  _all_gather_kernel.finish: _all_gather_kernel().finish().
  _project_ring_kernel.enter: _project_ring_kernel().enter().
  _project_ring_kernel.wait_before: _project_ring_kernel().wait_before().
  _project_ring_kernel.forward: _project_ring_kernel().forward().
  _gather_project_kernel.enter: _gather_project_kernel().enter().
  _gather_project_kernel.forward: _gather_project_kernel().forward().
  _gather_project_kernel.finish: _gather_project_kernel().finish().
  mla_preprocess.local.norm: mla_preprocess().local().norm().
  _regions: _regions().
  _reduce_scatter_kernel.remote: _reduce_scatter_kernel().remote().
  _all_gather_kernel.owner: _all_gather_kernel().owner().
  _all_gather_kernel.remote: _all_gather_kernel().remote().
  _project_ring_kernel.remote: _project_ring_kernel().remote().
  CYCLES: CYCLES.
  pack_mla_gate.local: pack_mla_gate().local().
  gather_moe_inputs.pack: gather_moe_inputs().pack().
  ring_collective.general: ring_collective().general().
  _gather_project_kernel.owner: _gather_project_kernel().owner().
  _reduce_scatter_kernel.enter.initialized: _reduce_scatter_kernel().enter().initialized().
  _reduce_scatter_kernel.seed: _reduce_scatter_kernel().seed().
  _reduce_scatter_kernel.add: _reduce_scatter_kernel().add().
  _reduce_scatter_kernel.forward.acquire: _reduce_scatter_kernel().forward().acquire().
  _reduce_scatter_kernel.finish: _reduce_scatter_kernel().finish().
  _all_gather_kernel.enter.initialized: _all_gather_kernel().enter().initialized().
  _all_gather_kernel.seed: _all_gather_kernel().seed().
  _all_gather_kernel.forward.acquire: _all_gather_kernel().forward().acquire().
  _project_ring_kernel.enter.initialized: _project_ring_kernel().enter().initialized().
  _project_ring_kernel.load_weight: _project_ring_kernel().load_weight().
  _project_ring_kernel.seed: _project_ring_kernel().seed().
  _project_ring_kernel.add: _project_ring_kernel().add().
  _project_ring_kernel.forward.acquire: _project_ring_kernel().forward().acquire().
  _project_ring_kernel.finish: _project_ring_kernel().finish().
  _gather_project_kernel.enter.initialized: _gather_project_kernel().enter().initialized().
  _gather_project_kernel.enter.load_weight: _gather_project_kernel().enter().load_weight().
  _gather_project_kernel.seed: _gather_project_kernel().seed().
  _gather_project_kernel.forward.acquire: _gather_project_kernel().forward().acquire().
  _gather_project_kernel.weights_ready: _gather_project_kernel().weights_ready().
---
# Module: [`src/vllm_torchtpu/kernels/kimi_k3/collectives.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/collectives.py)

## Functions
- <a id="_all_gather_kernel"></a>`_all_gather_kernel(tables, x, out, load_sems, send_sems, recv_sems, credits, store_sems, payload, received, *, regions, buffers)` — [`L334`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/collectives.py#L334) — documented in [kimi-k3-kernels](../../../../../concepts/kimi-k3-kernels.md)
- <a id="_gather_project"></a>`_gather_project(x, w, tables, collective_id)` — [`L915`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/collectives.py#L915) — documented in [kimi-k3-kernels](../../../../../concepts/kimi-k3-kernels.md)
- <a id="_gather_project_kernel"></a>`_gather_project_kernel(tables, x, w, out, load_sems, send_sems, recv_sems, credits, payload, received, weights, acc, output_buffers, wsem, output_sems, *, regions)` — [`L759`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/collectives.py#L759) — documented in [kimi-k3-kernels](../../../../../concepts/kimi-k3-kernels.md)
- <a id="_project_ring_kernel"></a>`_project_ring_kernel(tables_ref, x_ref, w_ref, o_ref, local_sems, send_sems, recv_sems, credits, store_sem, local_buf, payload, received, weights, inputs, weight_sem, *, streams, buffers)` — [`L545`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/collectives.py#L545) — documented in [kimi-k3-kernels](../../../../../concepts/kimi-k3-kernels.md)
- <a id="_reduce_scatter_kernel"></a>`_reduce_scatter_kernel(tables_ref, x_ref, o_ref, local_sems, send_sems, recv_sems, credits, store_sem, local_buf, payload, received, *, streams, buffers)` — [`L199`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/collectives.py#L199) — documented in [kimi-k3-kernels](../../../../../concepts/kimi-k3-kernels.md)
- <a id="_regions"></a>`_regions(rows, width)` — [`L185`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/collectives.py#L185) — documented in [kimi-k3-kernels](../../../../../concepts/kimi-k3-kernels.md)
- <a id="_reduce_scatter_kernel.forward.acquire"></a>`acquire()` — [`L314`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/collectives.py#L314)
- <a id="_all_gather_kernel.forward.acquire"></a>`acquire()` — [`L443`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/collectives.py#L443)
- <a id="_project_ring_kernel.forward.acquire"></a>`acquire()` — [`L669`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/collectives.py#L669)
- <a id="_gather_project_kernel.forward.acquire"></a>`acquire()` — [`L861`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/collectives.py#L861)
- <a id="_reduce_scatter_kernel.add"></a>`add()` — [`L299`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/collectives.py#L299)
- <a id="_project_ring_kernel.add"></a>`add()` — [`L654`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/collectives.py#L654)
- <a id="_gather_project_kernel.finish.copy"></a>`copy(owner_id)` — [`L897`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/collectives.py#L897) — documented in [kimi-k3-kernels](../../../../../concepts/kimi-k3-kernels.md)
- <a id="_reduce_scatter_kernel.enter"></a>`enter()` — [`L227`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/collectives.py#L227)
- <a id="_all_gather_kernel.enter"></a>`enter()` — [`L362`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/collectives.py#L362)
- <a id="_project_ring_kernel.enter"></a>`enter()` — [`L578`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/collectives.py#L578)
- <a id="_gather_project_kernel.enter"></a>`enter()` — [`L790`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/collectives.py#L790)
- <a id="_reduce_scatter_kernel.finish"></a>`finish()` — [`L320`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/collectives.py#L320)
- <a id="_all_gather_kernel.finish"></a>`finish()` — [`L449`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/collectives.py#L449)
- <a id="_project_ring_kernel.finish"></a>`finish()` — [`L675`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/collectives.py#L675)
- <a id="_gather_project_kernel.finish"></a>`finish()` — [`L893`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/collectives.py#L893)
- <a id="_reduce_scatter_kernel.forward"></a>`forward()` — [`L312`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/collectives.py#L312)
- <a id="_all_gather_kernel.forward"></a>`forward()` — [`L441`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/collectives.py#L441)
- <a id="_project_ring_kernel.forward"></a>`forward()` — [`L667`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/collectives.py#L667)
- <a id="_gather_project_kernel.forward"></a>`forward()` — [`L859`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/collectives.py#L859)
- <a id="gather_moe_inputs"></a>`gather_moe_inputs(x, weights, ids, mesh, tables, *, collective_id)` — [`L126`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/collectives.py#L126) — Gather latent tokens, BF16 weights and signed 16-bit IDs together. — documented in [kimi-k3-kernels](../../../../../concepts/kimi-k3-kernels.md)
- <a id="gather_project"></a>`gather_project(x, w, mesh, tables, *, collective_id)` — [`L957`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/collectives.py#L957) — Gather SP32 hidden states while projecting into packed KDA inputs. — documented in [kimi-k3-kernels](../../../../../concepts/kimi-k3-kernels.md)
- <a id="ring_collective.general"></a>`general(part)` — [`L471`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/collectives.py#L471) — documented in [kimi-k3-kernels](../../../../../concepts/kimi-k3-kernels.md)
- <a id="_reduce_scatter_kernel.enter.initialized"></a>`initialized(ready)` — [`L241`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/collectives.py#L241)
- <a id="_all_gather_kernel.enter.initialized"></a>`initialized(ready)` — [`L374`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/collectives.py#L374)
- <a id="_project_ring_kernel.enter.initialized"></a>`initialized(ready)` — [`L592`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/collectives.py#L592)
- <a id="_gather_project_kernel.enter.initialized"></a>`initialized(ready)` — [`L802`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/collectives.py#L802)
- <a id="_project_ring_kernel.load_weight"></a>`load_weight()` — [`L600`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/collectives.py#L600)
- <a id="_gather_project_kernel.enter.load_weight"></a>`load_weight()` — [`L810`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/collectives.py#L810)
- <a id="pack_mla_gate.local"></a>`local(weight)` — [`L58`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/collectives.py#L58)
- <a id="mla_preprocess.local"></a>`local(x, weight, packed_gate, qnorm, kvnorm)` — [`L79`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/collectives.py#L79) — documented in [kimi-k3-kernels](../../../../../concepts/kimi-k3-kernels.md)
- <a id="ring_collective.local"></a>`local(part)` — [`L491`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/collectives.py#L491) — documented in [kimi-k3-kernels](../../../../../concepts/kimi-k3-kernels.md)
- <a id="project_reduce_scatter.local"></a>`local(x, w)` — [`L717`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/collectives.py#L717) — documented in [kimi-k3-kernels](../../../../../concepts/kimi-k3-kernels.md)
- <a id="gather_project.local"></a>`local(x, w)` — [`L960`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/collectives.py#L960) — documented in [kimi-k3-kernels](../../../../../concepts/kimi-k3-kernels.md)
- <a id="mla_chip_layout"></a>`mla_chip_layout(devices, owners)` — [`L38`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/collectives.py#L38) — Physical pairs and same-core groups, ordered by Torch token ownership. — documented in [kimi-k3-kernels](../../../../../concepts/kimi-k3-kernels.md)
- <a id="mla_preprocess"></a>`mla_preprocess(x, weight, packed_gate, qnorm, kvnorm, mesh, owners, *, sequence_parallel, eps)` — [`L72`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/collectives.py#L72) — Source MLA layout with a common parameter interface for all buckets. — documented in [kimi-k3-kernels](../../../../../concepts/kimi-k3-kernels.md)
- <a id="mla_preprocess.local.norm"></a>`norm(value, scale)` — [`L80`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/collectives.py#L80) — documented in [kimi-k3-kernels](../../../../../concepts/kimi-k3-kernels.md)
- <a id="_all_gather_kernel.owner"></a>`owner(pos, family)` — [`L354`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/collectives.py#L354)
- <a id="_gather_project_kernel.owner"></a>`owner(pos, f)` — [`L783`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/collectives.py#L783)
- <a id="gather_moe_inputs.pack"></a>`pack(x, weights, ids)` — [`L133`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/collectives.py#L133) — documented in [kimi-k3-kernels](../../../../../concepts/kimi-k3-kernels.md)
- <a id="pack_mla_gate"></a>`pack_mla_gate(weight, mesh, pairs)` — [`L54`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/collectives.py#L54) — Replicate complementary TP2 gate shards from the original TP32 weights. — documented in [kimi-k3-kernels](../../../../../concepts/kimi-k3-kernels.md)
- <a id="_all_gather_kernel.peer"></a>`peer(pos, family)` — [`L357`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/collectives.py#L357) — documented in [kimi-k3-kernels](../../../../../concepts/kimi-k3-kernels.md)
- <a id="_gather_project_kernel.peer"></a>`peer(pos, f)` — [`L786`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/collectives.py#L786)
- <a id="project_reduce_scatter"></a>`project_reduce_scatter(x, w, mesh, tables, *, collective_id)` — [`L689`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/collectives.py#L689) — Fuse a three-head BF16 attention projection with SP32 RS. — documented in [kimi-k3-kernels](../../../../../concepts/kimi-k3-kernels.md)
- <a id="_all_gather_kernel.receive"></a>`receive()` — [`L428`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/collectives.py#L428) — documented in [kimi-k3-kernels](../../../../../concepts/kimi-k3-kernels.md)
- <a id="_gather_project_kernel.receive"></a>`receive()` — [`L846`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/collectives.py#L846) — documented in [kimi-k3-kernels](../../../../../concepts/kimi-k3-kernels.md)
- <a id="_reduce_scatter_kernel.remote"></a>`remote(index)` — [`L276`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/collectives.py#L276)
- <a id="_all_gather_kernel.remote"></a>`remote(index)` — [`L397`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/collectives.py#L397)
- <a id="_project_ring_kernel.remote"></a>`remote(index)` — [`L628`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/collectives.py#L628)
- <a id="_gather_project_kernel.remote"></a>`remote(s, index)` — [`L821`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/collectives.py#L821) — documented in [kimi-k3-kernels](../../../../../concepts/kimi-k3-kernels.md)
- <a id="ring_collective"></a>`ring_collective(x, mesh, tables, *, gather, collective_id)` — [`L454`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/collectives.py#L454) — AG takes global [T,D]; RS takes global [32,T,D] partials. — documented in [kimi-k3-kernels](../../../../../concepts/kimi-k3-kernels.md)
- <a id="_reduce_scatter_kernel.ring_coords"></a>`ring_coords(pos, family)` — [`L222`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/collectives.py#L222) — documented in [kimi-k3-kernels](../../../../../concepts/kimi-k3-kernels.md)
- <a id="_project_ring_kernel.ring_coords"></a>`ring_coords(pos, family)` — [`L573`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/collectives.py#L573)
- <a id="ring_tables"></a>`ring_tables(devices, token_ranks)` — [`L157`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/collectives.py#L157) — Build [family,position/peer/token-owner,mesh-index] lookup tables. — documented in [kimi-k3-kernels](../../../../../concepts/kimi-k3-kernels.md)
- <a id="_reduce_scatter_kernel.seed"></a>`seed()` — [`L293`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/collectives.py#L293)
- <a id="_all_gather_kernel.seed"></a>`seed()` — [`L420`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/collectives.py#L420)
- <a id="_project_ring_kernel.seed"></a>`seed()` — [`L648`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/collectives.py#L648)
- <a id="_gather_project_kernel.seed"></a>`seed()` — [`L838`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/collectives.py#L838)
- <a id="_all_gather_kernel.store"></a>`store(index)` — [`L407`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/collectives.py#L407) — documented in [kimi-k3-kernels](../../../../../concepts/kimi-k3-kernels.md)
- <a id="_reduce_scatter_kernel.wait"></a>`wait()` — [`L287`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/collectives.py#L287)
- <a id="_project_ring_kernel.wait_before"></a>`wait_before()` — [`L639`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/collectives.py#L639)
- <a id="_gather_project_kernel.weights_ready"></a>`weights_ready()` — [`L867`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/collectives.py#L867)

## Module values
- <a id="CYCLES"></a>`CYCLES` — [`L31`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/collectives.py#L31)

