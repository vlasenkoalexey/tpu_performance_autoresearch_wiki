---
title: 'Module: src/vllm_torchtpu/megakernel/pool/scatter_kv.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/megakernel/pool/scatter_kv.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.megakernel.pool.scatter_kv`/
symbols:
  scatter_single_token_across_att: scatter_single_token_across_att().
  scatter_kv: scatter_kv().
  kv_cols: kv_cols().
  scatter_kv.scatter_kv_seq: scatter_kv().scatter_kv_seq().
  scatter_kv.scatter_kv_row: scatter_kv().scatter_kv_row().
---
# Module: [`src/vllm_torchtpu/megakernel/pool/scatter_kv.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter_kv.py)

## Functions
- <a id="kv_cols"></a>`kv_cols(kc: ScatterKernel)` — [`L31`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter_kv.py#L31) — Pre-transpose every pool's new K / V rows into lane columns (`NS > 1`). — documented in [megakernel-pool](../../../../../concepts/megakernel-pool.md)
- <a id="scatter_kv"></a>`scatter_kv(kc: ScatterKernel)` — [`L118`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter_kv.py#L118) — Scatter every active row (`T == 1`) or sequence (`T > 1`) into its pages. — documented in [megakernel-pool](../../../../../concepts/megakernel-pool.md)
- <a id="scatter_kv.scatter_kv_row"></a>`scatter_kv_row(b, _)` — [`L128`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter_kv.py#L128)
- <a id="scatter_kv.scatter_kv_seq"></a>`scatter_kv_seq(s, _)` — [`L141`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter_kv.py#L141)
- <a id="scatter_single_token_across_att"></a>`scatter_single_token_across_att(kc: ScatterKernel, s_idx: Any, b_idx: Any, t_idx: Any)` — [`L42`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter_kv.py#L42) — Write row `b_idx`'s K / V into its page of every attention pool. — documented in [megakernel-pool](../../../../../concepts/megakernel-pool.md)

