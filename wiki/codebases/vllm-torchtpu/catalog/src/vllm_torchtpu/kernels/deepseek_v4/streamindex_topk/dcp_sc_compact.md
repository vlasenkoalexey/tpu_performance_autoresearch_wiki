---
title: 'Module: src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/dcp_sc_compact.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/dcp_sc_compact.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.deepseek_v4.streamindex_topk.dcp_sc_compact`/
symbols:
  _pack_body.pipeline_step: _pack_body().pipeline_step().
  _gather_and_pack_body.pipeline_step: _gather_and_pack_body().pipeline_step().
  pack_owned_winners: pack_owned_winners().
  _pack_body: _pack_body().
  _gather_and_pack_body: _gather_and_pack_body().
  SCAN_UNROLL: SCAN_UNROLL.
  _pack_body.pipeline_step.fill: _pack_body().pipeline_step().fill().
  _pack_body.pipeline_step.emit: _pack_body().pipeline_step().emit().
  _pack_body.pipeline_step.copy_out: _pack_body().pipeline_step().copy_out().
  _gather_and_pack_body.pipeline_step.fill: _gather_and_pack_body().pipeline_step().fill().
  _gather_and_pack_body.pipeline_step.emit: _gather_and_pack_body().pipeline_step().emit().
  _gather_and_pack_body.pipeline_step.copy_out: _gather_and_pack_body().pipeline_step().copy_out().
---
# Module: [`src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/dcp_sc_compact.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/dcp_sc_compact.py)

## Functions
- <a id="_gather_and_pack_body"></a>`_gather_and_pack_body(slots_hbm, idxs_hbm, rank_hbm, out_hbm, rowbuf_vmem, *, b: int, width: int, num_waves: int, lanes: int, num_cores: int, num_subcores: int)` — [`L92`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/dcp_sc_compact.py#L92)
- <a id="_pack_body"></a>`_pack_body(merged_hbm, out_hbm, rowbuf_vmem, *, b: int, width: int, num_waves: int, lanes: int, num_cores: int, num_subcores: int)` — [`L28`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/dcp_sc_compact.py#L28)
- <a id="_pack_body.pipeline_step.copy_out"></a>`copy_out(i)` — [`L68`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/dcp_sc_compact.py#L68)
- <a id="_gather_and_pack_body.pipeline_step.copy_out"></a>`copy_out(i)` — [`L139`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/dcp_sc_compact.py#L139)
- <a id="_pack_body.pipeline_step.emit"></a>`emit(i, woff)` — [`L52`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/dcp_sc_compact.py#L52)
- <a id="_gather_and_pack_body.pipeline_step.emit"></a>`emit(i, woff)` — [`L121`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/dcp_sc_compact.py#L121)
- <a id="_pack_body.pipeline_step.fill"></a>`fill(i)` — [`L46`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/dcp_sc_compact.py#L46)
- <a id="_gather_and_pack_body.pipeline_step.fill"></a>`fill(i)` — [`L115`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/dcp_sc_compact.py#L115)
- <a id="pack_owned_winners"></a>`pack_owned_winners(slots: jax.Array, idxs: jax.Array | None = None, dcp_rank: int | jax.Array | None = None)` — [`L173`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/dcp_sc_compact.py#L173) — Compacts non-negative rank-local winners into a `-1`-padded prefix.
- <a id="_pack_body.pipeline_step"></a>`pipeline_step(merged_vmem, out_vmem)` — [`L43`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/dcp_sc_compact.py#L43)
- <a id="_gather_and_pack_body.pipeline_step"></a>`pipeline_step(slots_vmem, idxs_vmem, rank_vmem, out_vmem)` — [`L109`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/dcp_sc_compact.py#L109)

## Module values
- <a id="SCAN_UNROLL"></a>`SCAN_UNROLL` — [`L25`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/dcp_sc_compact.py#L25)

