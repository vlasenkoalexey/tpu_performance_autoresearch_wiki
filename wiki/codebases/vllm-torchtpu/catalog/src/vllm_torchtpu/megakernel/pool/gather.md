---
title: 'Module: src/vllm_torchtpu/megakernel/pool/gather.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/megakernel/pool/gather.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.megakernel.pool.gather`/
symbols:
  gather_gdn_states: gather_gdn_states().
  gather_gdn_states._kernel.finish_page_read: gather_gdn_states()._kernel().finish_page_read().
  gather_gdn_states._kernel.start_page_read: gather_gdn_states()._kernel().start_page_read().
  gather_gdn_states._kernel: gather_gdn_states()._kernel().
  gather_gdn_states._kernel.page_base_for: gather_gdn_states()._kernel().page_base_for().
  gather_gdn_states._kernel.gather_pair_even: gather_gdn_states()._kernel().gather_pair_even().
  gather_gdn_states._kernel.gather_pair_odd: gather_gdn_states()._kernel().gather_pair_odd().
  gather_gdn_states._kernel.has_input_state: gather_gdn_states()._kernel().has_input_state().
  _PALLAS_NAME: _PALLAS_NAME.
  gather_gdn_states._kernel.is_active: gather_gdn_states()._kernel().is_active().
---
# Module: [`src/vllm_torchtpu/megakernel/pool/gather.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/gather.py)

## Functions
- <a id="gather_gdn_states._kernel"></a>`_kernel(*refs)` — [`L143`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/gather.py#L143) — documented in [megakernel-pool](../../../../../concepts/megakernel-pool.md)
- <a id="gather_gdn_states._kernel.finish_page_read"></a>`finish_page_read(raw_ref, sub, s, p_slot, g_slot, r_slot, r_sub)` — [`L201`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/gather.py#L201) — documented in [megakernel-pool](../../../../../concepts/megakernel-pool.md)
- <a id="gather_gdn_states"></a>`gather_gdn_states(layout: PoolLayout, ex: ExecSpec, raw_pools: tuple[jax.Array, ...] | list[jax.Array], ckpt_indices: jax.Array, read_offsets: jax.Array, active_seqs: jax.Array | str | None = None, *, interpret: bool | None = None)` — [`L39`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/gather.py#L39) — Gather per-rank GDN `conv` and `rec` states from per-attention `raw_pools`. — documented in [megakernel-pool](../../../../../concepts/megakernel-pool.md)
- <a id="gather_gdn_states._kernel.gather_pair_even"></a>`gather_pair_even(pair, _, raw_ref=raw_ref, sub=sub, g_slot=g_slot, r_slot=r_slot, r_sub=r_sub, has_next_o=has_next_o, next_raw_ref=next_raw_ref, next_sub=next_sub)` — [`L310`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/gather.py#L310)
- <a id="gather_gdn_states._kernel.gather_pair_odd"></a>`gather_pair_odd(pair, _, raw_ref=raw_ref, sub=sub, g_slot=g_slot, r_slot=r_slot, r_sub=r_sub, p0=p0, p1=p1)` — [`L351`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/gather.py#L351)
- <a id="gather_gdn_states._kernel.has_input_state"></a>`has_input_state(sub, s)` — [`L172`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/gather.py#L172)
- <a id="gather_gdn_states._kernel.is_active"></a>`is_active(s)` — [`L165`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/gather.py#L165)
- <a id="gather_gdn_states._kernel.page_base_for"></a>`page_base_for(sub, s)` — [`L176`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/gather.py#L176)
- <a id="gather_gdn_states._kernel.start_page_read"></a>`start_page_read(raw_ref, sub, s, p_slot)` — [`L193`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/gather.py#L193)

## Module values
- <a id="_PALLAS_NAME"></a>`_PALLAS_NAME` — [`L33`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/gather.py#L33)

