---
title: 'Module: torchtitan/experiments/tpu/graph_trainer/tpu_host_offload.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/graph_trainer/tpu_host_offload.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.graph_trainer.tpu_host_offload`/
symbols:
  offload_scan_activations: offload_scan_activations().
  _select_stacked_activation: _select_stacked_activation().
  _find_stack_consumer.walk: _find_stack_consumer().walk().
  _full_and_scan_offload_memory_policy_pass: _full_and_scan_offload_memory_policy_pass().
  _find_stack_producer: _find_stack_producer().
  _find_stack_consumer: _find_stack_consumer().
  _only_read_by: _only_read_by().
  _reads_one_slice: _reads_one_slice().
  _reload_body_slice: _reload_body_slice().
  _SCAN_HOP: _SCAN_HOP.
  _POLICY: _POLICY.
  _scan_body: _scan_body().
  _body_placeholder: _body_placeholder().
  _offload_body_output: _offload_body_output().
---
# Module: [`torchtitan/experiments/tpu/graph_trainer/tpu_host_offload.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tpu_host_offload.py)

## Functions
- <a id="_body_placeholder"></a>`_body_placeholder(body: torch.fx.GraphModule, index: int)` — [`L254`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tpu_host_offload.py#L254)
- <a id="_find_stack_consumer"></a>`_find_stack_consumer(node: Node)` — [`L157`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tpu_host_offload.py#L157) — The backward scan that reads ``node``, and its body placeholder index.
- <a id="_find_stack_producer"></a>`_find_stack_producer(node: Node)` — [`L136`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tpu_host_offload.py#L136) — The forward scan that produced ``node``, and which output it was.
- <a id="_full_and_scan_offload_memory_policy_pass"></a>`_full_and_scan_offload_memory_policy_pass(gm: torch.fx.GraphModule, *, config: GraphTrainer.Config)` — [`L365`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tpu_host_offload.py#L365) — FullAC, then keep the largest saved activation on the host.
- <a id="_offload_body_output"></a>`_offload_body_output(body: torch.fx.GraphModule, index: int)` — [`L228`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tpu_host_offload.py#L228) — Emit body output ``index`` on host instead of on device.
- <a id="_only_read_by"></a>`_only_read_by(node: Node, scan: Node)` — [`L113`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tpu_host_offload.py#L113) — Whether ``scan`` is the only thing that reads ``node`` or a view of it.
- <a id="_reads_one_slice"></a>`_reads_one_slice(body: torch.fx.GraphModule, index: int)` — [`L258`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tpu_host_offload.py#L258) — Whether body placeholder ``index`` is read a slice at a time.
- <a id="_reload_body_slice"></a>`_reload_body_slice(body: torch.fx.GraphModule, index: int)` — [`L277`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tpu_host_offload.py#L277) — Reload the per-iteration slice of body placeholder ``index``.
- <a id="_scan_body"></a>`_scan_body(gm: torch.fx.GraphModule, scan_node: Node)` — [`L103`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tpu_host_offload.py#L103) — The loop body of ``scan_node``.
- <a id="_select_stacked_activation"></a>`_select_stacked_activation(gm: torch.fx.GraphModule)` — [`L191`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tpu_host_offload.py#L191) — The largest value the forward loop saved and the backward loop reads.
- <a id="offload_scan_activations"></a>`offload_scan_activations(gm: torch.fx.GraphModule)` — [`L309`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tpu_host_offload.py#L309) — Keep the scan's stacked layer input on host between the two loops. — documented in [tpu-graph-trainer](../../../../../concepts/tpu-graph-trainer.md)
- <a id="_find_stack_consumer.walk"></a>`walk(n: Node)` — [`L168`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tpu_host_offload.py#L168)

## Module values
- <a id="_POLICY"></a>`_POLICY` — [`L100`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tpu_host_offload.py#L100)
- <a id="_SCAN_HOP"></a>`_SCAN_HOP` — [`L99`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tpu_host_offload.py#L99)

