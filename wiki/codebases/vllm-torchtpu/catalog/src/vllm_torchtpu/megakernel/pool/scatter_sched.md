---
title: 'Module: src/vllm_torchtpu/megakernel/pool/scatter_sched.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/megakernel/pool/scatter_sched.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.megakernel.pool.scatter_sched`/
symbols:
  ckpt_prologue: ckpt_prologue().
  start_seq_in: start_seq_in().
  wait_seq_in: wait_seq_in().
  scatter_ckpt_states: scatter_ckpt_states().
  scatter_ckpt_states.scatter_pair: scatter_ckpt_states().scatter_pair().
---
# Module: [`src/vllm_torchtpu/megakernel/pool/scatter_sched.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter_sched.py)

## Functions
- <a id="ckpt_prologue"></a>`ckpt_prologue(kc: ScatterKernel)` — [`L101`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter_sched.py#L101) — Start the first state reads; zero the slot pages' unused tails. — documented in [megakernel-pool](../../../../../concepts/megakernel-pool.md)
- <a id="scatter_ckpt_states"></a>`scatter_ckpt_states(kc: ScatterKernel)` — [`L134`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter_sched.py#L134) — Read, pack and write every GDN layer's states (`NS`-specialized order). — documented in [megakernel-pool](../../../../../concepts/megakernel-pool.md)
- <a id="scatter_ckpt_states.scatter_pair"></a>`scatter_pair(pair, _, raw_out_ref=raw_out_ref, sub=sub, o=o)` — [`L258`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter_sched.py#L258)
- <a id="start_seq_in"></a>`start_seq_in(kc: ScatterKernel, o: Any, s: Any, in_slot: Any)` — [`L31`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter_sched.py#L31) — Start reading GDN layer `o`'s conv / rec state of sequence `s`. — documented in [megakernel-pool](../../../../../concepts/megakernel-pool.md)
- <a id="wait_seq_in"></a>`wait_seq_in(kc: ScatterKernel, o: Any, s: Any, in_slot: Any)` — [`L66`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter_sched.py#L66) — Wait for `start_seq_in(o, s, in_slot)`. — documented in [megakernel-pool](../../../../../concepts/megakernel-pool.md)

