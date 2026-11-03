---
title: 'Module: src/vllm_torchtpu/megakernel/pool/scatter_ckpt.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/megakernel/pool/scatter_ckpt.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.megakernel.pool.scatter_ckpt`/
symbols:
  start_scatter_seq: start_scatter_seq().
  wait_scatter_seq: wait_scatter_seq().
  pb_for: pb_for().
  slot_copy: slot_copy().
  prepare_ckpt: prepare_ckpt().
  is_contig_ckpt: is_contig_ckpt().
---
# Module: [`src/vllm_torchtpu/megakernel/pool/scatter_ckpt.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter_ckpt.py)

## Functions
- <a id="is_contig_ckpt"></a>`is_contig_ckpt(kc: ScatterKernel, sub: Any, s: Any)` — [`L154`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter_ckpt.py#L154) — Whether sequence `s`'s `T` checkpoint slots are consecutive.
- <a id="pb_for"></a>`pb_for(kc: ScatterKernel, sub: Any, s: Any, t: Any, span: int)` — [`L137`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter_ckpt.py#L137) — First page of sequence `s`'s checkpoint slot `t` in recurrent slot `sub`. — documented in [megakernel-pool](../../../../../concepts/megakernel-pool.md)
- <a id="prepare_ckpt"></a>`prepare_ckpt(layout: PoolLayout, ex: Any, conv: Any, rec: Any, ckpt_indices: Any, *, has_gdn: bool, interpret: bool)` — [`L32`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter_ckpt.py#L32) — Kernel conv input, its VMEM buffer shape / dtype and the GDN geometry. — documented in [megakernel-pool](../../../../../concepts/megakernel-pool.md)
- <a id="slot_copy"></a>`slot_copy(kc: ScatterKernel, raw_out_ref: Any, slot: Any, t: Any, pb_t: Any)` — [`L167`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter_ckpt.py#L167) — Copy of slot `t`'s live rows only (recurrent pages + conv rows). — documented in [megakernel-pool](../../../../../concepts/megakernel-pool.md)
- <a id="start_scatter_seq"></a>`start_scatter_seq(kc: ScatterKernel, raw_out_ref: Any, sub: Any, s: Any, slot: Any)` — [`L181`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter_ckpt.py#L181) — Pack sequence `s`'s states into slot pages; start their pool writes. — documented in [megakernel-pool](../../../../../concepts/megakernel-pool.md)
- <a id="wait_scatter_seq"></a>`wait_scatter_seq(kc: ScatterKernel, raw_out_ref: Any, sub: Any, s: Any, slot: Any)` — [`L305`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter_ckpt.py#L305) — Wait for `start_scatter_seq(raw_out_ref, sub, s, slot)`. — documented in [megakernel-pool](../../../../../concepts/megakernel-pool.md)

