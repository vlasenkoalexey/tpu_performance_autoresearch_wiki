---
title: 'Module: src/vllm_torchtpu/kernels/experimental/batched_rpa/bref_override.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/experimental/batched_rpa/bref_override.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.experimental.batched_rpa.bref_override`/
symbols:
  KVBufferedRefHeadAlongSublane.copy_in: KVBufferedRefHeadAlongSublane#copy_in().
  _BypassRef: _BypassRef#
  _BypassRef.create: _BypassRef#create().
  KVBufferedRefSeqAlongLane.copy_out: KVBufferedRefSeqAlongLane#copy_out().
  KVBufferedRefHeadAlongSublane.copy_out: KVBufferedRefHeadAlongSublane#copy_out().
  _step_guard: _step_guard().
  KVBufferedRefSeqAlongLane.copy_in: KVBufferedRefSeqAlongLane#copy_in().
  KVBufferedRefHeadAlongSublane.cfgs: KVBufferedRefHeadAlongSublane#cfgs.
  _BypassRef.copy_out: _BypassRef#copy_out().
  _BypassRef.wait_out: _BypassRef#wait_out().
  BatchingORef.copy_out: BatchingORef#copy_out().
  BatchingLSERef.copy_out: BatchingLSERef#copy_out().
  BatchingQRef.copy_in: BatchingQRef#copy_in().
  KVBufferedRefSeqAlongLane.cfgs: KVBufferedRefSeqAlongLane#cfgs.
  _BypassRef.dst_ref: _BypassRef#dst_ref.
  _BypassRef.copy_in: _BypassRef#copy_in().
  _BypassRef.wait_in: _BypassRef#wait_in().
  _BypassRef.src_ref: _BypassRef#src_ref.
  KVBufferedRefSeqAlongLane.create: KVBufferedRefSeqAlongLane#create().
  KVBufferedRefSeqAlongLane.wait_in: KVBufferedRefSeqAlongLane#wait_in().
  KVBufferedRefSeqAlongLane.wait_out: KVBufferedRefSeqAlongLane#wait_out().
  KVBufferedRefHeadAlongSublane.create: KVBufferedRefHeadAlongSublane#create().
  KVBufferedRefHeadAlongSublane.wait_in: KVBufferedRefHeadAlongSublane#wait_in().
  KVBufferedRefHeadAlongSublane.wait_out: KVBufferedRefHeadAlongSublane#wait_out().
  BatchingORef.create: BatchingORef#create().
  BatchingORef.wait_out: BatchingORef#wait_out().
  BatchingLSERef.create: BatchingLSERef#create().
  BatchingLSERef.wait_out: BatchingLSERef#wait_out().
  BatchingQRef.create: BatchingQRef#create().
  BatchingQRef.wait_in: BatchingQRef#wait_in().
  _BaseBufferedRef: _BaseBufferedRef#
  KVBufferedRefSeqAlongLane: KVBufferedRefSeqAlongLane#
  KVBufferedRefHeadAlongSublane: KVBufferedRefHeadAlongSublane#
  BatchingORef: BatchingORef#
  BatchingLSERef: BatchingLSERef#
  BatchingQRef: BatchingQRef#
  BatchingORef.cfgs: BatchingORef#cfgs.
  BatchingLSERef.cfgs: BatchingLSERef#cfgs.
  BatchingQRef.cfgs: BatchingQRef#cfgs.
  _BaseBufferedRef.__post_init__: _BaseBufferedRef#__post_init__().
  _BypassRef.bind: _BypassRef#bind().
---
# Module: [`src/vllm_torchtpu/kernels/experimental/batched_rpa/bref_override.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/bref_override.py)

## Classes
### <a id="BatchingLSERef"></a>`BatchingLSERef`  ·  implements/extends _BypassRef
- def: [`src/vllm_torchtpu/kernels/experimental/batched_rpa/bref_override.py:527`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/bref_override.py#L527)
- doc: Handles writing LSE values to HBM, overlapped with compute via
- signature: `class BatchingLSERef(_BypassRef):`
- members:
  - <a id="BatchingLSERef.copy_out"></a>`copy_out(self, step: int | jax.Array, slot: int | jax.Array, total_steps: int | jax.Array)` — [`L556`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/bref_override.py#L556)
  - <a id="BatchingLSERef.create"></a>`create(cls, spec: pl.BlockSpec, dtype_or_type: jax.Array, buffer_type: pltpu.BufferType, buffer_count: int, use_lookahead: bool = False, cfgs: configs.RpaConfigs | None = None, **kwargs)` — [`L534`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/bref_override.py#L534)
  - <a id="BatchingLSERef.wait_out"></a>`wait_out(self, step: int | jax.Array, slot: int | jax.Array, total_steps: int | jax.Array)` — [`L582`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/bref_override.py#L582)
  - <a id="BatchingLSERef.cfgs"></a>`cfgs` — [`L531`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/bref_override.py#L531)
- uses (calls/refs, reference-scoped): [`batch_size`](configs.md#RpaConfigs.batch_size), [`RpaConfigs`](configs.md#RpaConfigs), [`_BypassRef`](bref_override.md#_BypassRef), [`create`](bref_override.md#_BypassRef.create), [`_step_guard`](bref_override.md#_step_guard), [`dst_ref`](bref_override.md#_BypassRef.dst_ref)
- used by: [`create_allocs`](kernel.md#create_allocs), [`_BypassRef`](bref_override.md#_BypassRef), [`create`](bref_override.md#_BypassRef.create), [`copy_out`](bref_override.md#_BypassRef.copy_out), [`wait_out`](bref_override.md#_BypassRef.wait_out)

### <a id="BatchingORef"></a>`BatchingORef`  ·  implements/extends _BypassRef
- def: [`src/vllm_torchtpu/kernels/experimental/batched_rpa/bref_override.py:447`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/bref_override.py#L447)
- doc: Handles normalizing and storing the final attention output.
- signature: `class BatchingORef(_BypassRef):`
- members:
  - <a id="BatchingORef.copy_out"></a>`copy_out(self, step: int | jax.Array, slot: int | jax.Array, total_steps: int | jax.Array)` — [`L475`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/bref_override.py#L475)
  - <a id="BatchingORef.create"></a>`create(cls, spec: pl.BlockSpec, dtype_or_type: jax.Array, buffer_type: pltpu.BufferType, buffer_count: int, use_lookahead: bool = False, cfgs: configs.RpaConfigs | None = None, **kwargs)` — [`L453`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/bref_override.py#L453)
  - <a id="BatchingORef.wait_out"></a>`wait_out(self, step: int | jax.Array, slot: int | jax.Array, total_steps: int | jax.Array)` — [`L502`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/bref_override.py#L502)
  - <a id="BatchingORef.cfgs"></a>`cfgs` — [`L450`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/bref_override.py#L450)
- uses (calls/refs, reference-scoped): [`batch_size`](configs.md#RpaConfigs.batch_size), [`RpaConfigs`](configs.md#RpaConfigs), [`_BypassRef`](bref_override.md#_BypassRef), [`create`](bref_override.md#_BypassRef.create), [`_step_guard`](bref_override.md#_step_guard), [`dst_ref`](bref_override.md#_BypassRef.dst_ref)
- used by: [`create_allocs`](kernel.md#create_allocs), [`_BypassRef`](bref_override.md#_BypassRef), [`create`](bref_override.md#_BypassRef.create), [`copy_out`](bref_override.md#_BypassRef.copy_out), [`wait_out`](bref_override.md#_BypassRef.wait_out)

### <a id="BatchingQRef"></a>`BatchingQRef`  ·  implements/extends _BypassRef
- def: [`src/vllm_torchtpu/kernels/experimental/batched_rpa/bref_override.py:607`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/bref_override.py#L607)
- doc: Handles fetching Q blocks using precomputed metadata.
- signature: `class BatchingQRef(_BypassRef):`
- members:
  - <a id="BatchingQRef.copy_in"></a>`copy_in(self, step: int | jax.Array, slot: int | jax.Array, total_steps: int | jax.Array)` — [`L635`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/bref_override.py#L635)
  - <a id="BatchingQRef.create"></a>`create(cls, spec: pl.BlockSpec, dtype_or_type: jax.Array, buffer_type: pltpu.BufferType, buffer_count: int, use_lookahead: bool = False, cfgs: configs.RpaConfigs | None = None, **kwargs)` — [`L613`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/bref_override.py#L613)
  - <a id="BatchingQRef.wait_in"></a>`wait_in(self, step: int | jax.Array, slot: int | jax.Array, total_steps: int | jax.Array)` — [`L658`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/bref_override.py#L658)
  - <a id="BatchingQRef.cfgs"></a>`cfgs` — [`L610`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/bref_override.py#L610)
- uses (calls/refs, reference-scoped): [`batch_size`](configs.md#RpaConfigs.batch_size), [`RpaConfigs`](configs.md#RpaConfigs), [`_BypassRef`](bref_override.md#_BypassRef), [`create`](bref_override.md#_BypassRef.create), [`_step_guard`](bref_override.md#_step_guard), [`src_ref`](bref_override.md#_BypassRef.src_ref)
- used by: [`create_allocs`](kernel.md#create_allocs), [`_BypassRef`](bref_override.md#_BypassRef), [`create`](bref_override.md#_BypassRef.create), [`copy_in`](bref_override.md#_BypassRef.copy_in), [`wait_in`](bref_override.md#_BypassRef.wait_in)

### <a id="KVBufferedRefHeadAlongSublane"></a>`KVBufferedRefHeadAlongSublane`  ·  implements/extends _BypassRef
- def: [`src/vllm_torchtpu/kernels/experimental/batched_rpa/bref_override.py:291`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/bref_override.py#L291)
- doc: Handles fetching and updating KV cache using HEAD_ALONG_SUBLANE memory layout.
- signature: `class KVBufferedRefHeadAlongSublane(_BypassRef):`
- members:
  - <a id="KVBufferedRefHeadAlongSublane.copy_in"></a>`copy_in(self, step: int | jax.Array, slot: int | jax.Array, total_steps: int | jax.Array)` — [`L319`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/bref_override.py#L319)
  - <a id="KVBufferedRefHeadAlongSublane.copy_out"></a>`copy_out(self, step: int | jax.Array, slot: int | jax.Array, total_steps: int | jax.Array)` — [`L366`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/bref_override.py#L366)
  - <a id="KVBufferedRefHeadAlongSublane.create"></a>`create(cls, spec: pl.BlockSpec, dtype_or_type: jax.Array, buffer_type: pltpu.BufferType, buffer_count: int, use_lookahead: bool = False, cfgs: configs.RpaConfigs | None = None, **kwargs)` — [`L297`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/bref_override.py#L297)
  - <a id="KVBufferedRefHeadAlongSublane.wait_in"></a>`wait_in(self, step: int | jax.Array, slot: int | jax.Array, total_steps: int | jax.Array)` — [`L398`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/bref_override.py#L398)
  - <a id="KVBufferedRefHeadAlongSublane.wait_out"></a>`wait_out(self, step: int | jax.Array, slot: int | jax.Array, total_steps: int | jax.Array)` — [`L421`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/bref_override.py#L421)
  - <a id="KVBufferedRefHeadAlongSublane.cfgs"></a>`cfgs` — [`L294`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/bref_override.py#L294)
- uses (calls/refs, reference-scoped): [`serve`](configs.md#RpaConfigs.serve), [`bkv_p_new`](configs.md#RpaConfigs.bkv_p_new), [`batch_size`](configs.md#RpaConfigs.batch_size), [`RpaConfigs`](configs.md#RpaConfigs), [`page_size`](configs.md#ServingConfigs.page_size), [`kv_hbm_stride`](configs.md#RpaConfigs.kv_hbm_stride), [`_BypassRef`](bref_override.md#_BypassRef), [`create`](bref_override.md#_BypassRef.create), [`bkv_p_cache`](configs.md#RpaConfigs.bkv_p_cache), [`_step_guard`](bref_override.md#_step_guard), [`dst_ref`](bref_override.md#_BypassRef.dst_ref), [`src_ref`](bref_override.md#_BypassRef.src_ref)
- used by: [`create_allocs`](kernel.md#create_allocs), [`_BypassRef`](bref_override.md#_BypassRef), [`create`](bref_override.md#_BypassRef.create), [`copy_out`](bref_override.md#_BypassRef.copy_out), [`wait_out`](bref_override.md#_BypassRef.wait_out), [`copy_in`](bref_override.md#_BypassRef.copy_in), [`wait_in`](bref_override.md#_BypassRef.wait_in)

### <a id="KVBufferedRefSeqAlongLane"></a>`KVBufferedRefSeqAlongLane`  ·  implements/extends _BypassRef
- def: [`src/vllm_torchtpu/kernels/experimental/batched_rpa/bref_override.py:138`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/bref_override.py#L138)
- doc: Handles fetching/updating KV cache using SEQ_ALONG_LANE memory layout.
- signature: `class KVBufferedRefSeqAlongLane(_BypassRef):`
- members:
  - <a id="KVBufferedRefSeqAlongLane.copy_in"></a>`copy_in(self, step: int | jax.Array, slot: int | jax.Array, total_steps: int | jax.Array)` — [`L166`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/bref_override.py#L166)
  - <a id="KVBufferedRefSeqAlongLane.copy_out"></a>`copy_out(self, step: int | jax.Array, slot: int | jax.Array, total_steps: int | jax.Array)` — [`L210`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/bref_override.py#L210)
  - <a id="KVBufferedRefSeqAlongLane.create"></a>`create(cls, spec: pl.BlockSpec, dtype_or_type: jax.Array, buffer_type: pltpu.BufferType, buffer_count: int, use_lookahead: bool = False, cfgs: configs.RpaConfigs | None = None, **kwargs)` — [`L144`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/bref_override.py#L144)
  - <a id="KVBufferedRefSeqAlongLane.wait_in"></a>`wait_in(self, step: int | jax.Array, slot: int | jax.Array, total_steps: int | jax.Array)` — [`L241`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/bref_override.py#L241)
  - <a id="KVBufferedRefSeqAlongLane.wait_out"></a>`wait_out(self, step: int | jax.Array, slot: int | jax.Array, total_steps: int | jax.Array)` — [`L265`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/bref_override.py#L265)
  - <a id="KVBufferedRefSeqAlongLane.cfgs"></a>`cfgs` — [`L141`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/bref_override.py#L141)
- uses (calls/refs, reference-scoped): [`serve`](configs.md#RpaConfigs.serve), [`bkv_p_new`](configs.md#RpaConfigs.bkv_p_new), [`batch_size`](configs.md#RpaConfigs.batch_size), [`RpaConfigs`](configs.md#RpaConfigs), [`_BypassRef`](bref_override.md#_BypassRef), [`create`](bref_override.md#_BypassRef.create), [`bkv_p_cache`](configs.md#RpaConfigs.bkv_p_cache), [`_step_guard`](bref_override.md#_step_guard), [`page_size_log2`](configs.md#ServingConfigs.page_size_log2), [`dst_ref`](bref_override.md#_BypassRef.dst_ref), [`page_size_mask`](configs.md#ServingConfigs.page_size_mask), [`src_ref`](bref_override.md#_BypassRef.src_ref)
- used by: [`create_allocs`](kernel.md#create_allocs), [`_BypassRef`](bref_override.md#_BypassRef), [`create`](bref_override.md#_BypassRef.create), [`copy_out`](bref_override.md#_BypassRef.copy_out), [`wait_out`](bref_override.md#_BypassRef.wait_out), [`copy_in`](bref_override.md#_BypassRef.copy_in), [`wait_in`](bref_override.md#_BypassRef.wait_in)

### <a id="_BaseBufferedRef"></a>`_BaseBufferedRef`  ·  implements/extends BufferedRef
- def: [`src/vllm_torchtpu/kernels/experimental/batched_rpa/bref_override.py:26`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/bref_override.py#L26)
- signature: `class _BaseBufferedRef(pltpu.BufferedRef):`
- protocol/private: <a id="_BaseBufferedRef.__post_init__"></a>`__post_init__`[`L27`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/bref_override.py#L27)
- uses (calls/refs, reference-scoped): [`_BypassRef`](bref_override.md#_BypassRef)
- used by: [`_BypassRef`](bref_override.md#_BypassRef), [`create`](bref_override.md#_BypassRef.create)

### <a id="_BypassRef"></a>`_BypassRef`  ·  implements/extends _BaseBufferedRef
- def: [`src/vllm_torchtpu/kernels/experimental/batched_rpa/bref_override.py:35`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/bref_override.py#L35)
- doc: `pltpu.BufferedRef` bound to explicit `(step, slot, total_steps)` DMAs.
- signature: `class _BypassRef(_BaseBufferedRef):`
- members:
  - <a id="_BypassRef.bind"></a>`bind(self, src_ref=None, dst_ref=None)` — [`L41`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/bref_override.py#L41)
  - <a id="_BypassRef.copy_in"></a>`copy_in(self, step: int | jax.Array, slot: int | jax.Array, total_steps: int | jax.Array)` — [`L75`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/bref_override.py#L75)
  - <a id="_BypassRef.copy_out"></a>`copy_out(self, step: int | jax.Array, slot: int | jax.Array, total_steps: int | jax.Array)` — [`L95`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/bref_override.py#L95)
  - <a id="_BypassRef.create"></a>`create(cls, spec: pl.BlockSpec, dtype_or_type: jax.Array, buffer_type: pltpu.BufferType, buffer_count: int, use_lookahead: bool = False, **kwargs)` — [`L46`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/bref_override.py#L46)
  - <a id="_BypassRef.wait_in"></a>`wait_in(self, step: int | jax.Array, slot: int | jax.Array, total_steps: int | jax.Array)` — [`L85`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/bref_override.py#L85)
  - <a id="_BypassRef.wait_out"></a>`wait_out(self, step: int | jax.Array, slot: int | jax.Array, total_steps: int | jax.Array)` — [`L105`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/bref_override.py#L105)
  - <a id="_BypassRef.dst_ref"></a>`dst_ref` — [`L39`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/bref_override.py#L39)
  - <a id="_BypassRef.src_ref"></a>`src_ref` — [`L38`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/bref_override.py#L38)
- uses (calls/refs, reference-scoped): [`copy_in`](bref_override.md#KVBufferedRefHeadAlongSublane.copy_in), [`copy_out`](bref_override.md#KVBufferedRefSeqAlongLane.copy_out), [`copy_out`](bref_override.md#KVBufferedRefHeadAlongSublane.copy_out), [`copy_in`](bref_override.md#KVBufferedRefSeqAlongLane.copy_in), [`copy_in`](bref_override.md#BatchingQRef.copy_in), [`copy_out`](bref_override.md#BatchingLSERef.copy_out), [`copy_out`](bref_override.md#BatchingORef.copy_out), [`create`](bref_override.md#BatchingLSERef.create), [`create`](bref_override.md#BatchingORef.create), [`create`](bref_override.md#BatchingQRef.create), [`create`](bref_override.md#KVBufferedRefHeadAlongSublane.create), [`create`](bref_override.md#KVBufferedRefSeqAlongLane.create), [`wait_in`](bref_override.md#BatchingQRef.wait_in), [`wait_in`](bref_override.md#KVBufferedRefHeadAlongSublane.wait_in), [`wait_in`](bref_override.md#KVBufferedRefSeqAlongLane.wait_in), [`wait_out`](bref_override.md#BatchingLSERef.wait_out), [`wait_out`](bref_override.md#BatchingORef.wait_out), [`wait_out`](bref_override.md#KVBufferedRefHeadAlongSublane.wait_out), [`wait_out`](bref_override.md#KVBufferedRefSeqAlongLane.wait_out), [`BatchingLSERef`](bref_override.md#BatchingLSERef), [`BatchingORef`](bref_override.md#BatchingORef), [`BatchingQRef`](bref_override.md#BatchingQRef), [`KVBufferedRefHeadAlongSublane`](bref_override.md#KVBufferedRefHeadAlongSublane), [`KVBufferedRefSeqAlongLane`](bref_override.md#KVBufferedRefSeqAlongLane), [`_BaseBufferedRef`](bref_override.md#_BaseBufferedRef)
- used by: [`copy_in`](bref_override.md#KVBufferedRefHeadAlongSublane.copy_in), [`copy_out`](bref_override.md#KVBufferedRefSeqAlongLane.copy_out), [`copy_out`](bref_override.md#KVBufferedRefHeadAlongSublane.copy_out), [`copy_in`](bref_override.md#KVBufferedRefSeqAlongLane.copy_in), [`copy_in`](bref_override.md#BatchingQRef.copy_in), [`copy_out`](bref_override.md#BatchingLSERef.copy_out), [`copy_out`](bref_override.md#BatchingORef.copy_out), [`create`](bref_override.md#BatchingLSERef.create), [`create`](bref_override.md#BatchingORef.create), [`create`](bref_override.md#BatchingQRef.create), [`create`](bref_override.md#KVBufferedRefHeadAlongSublane.create), [`create`](bref_override.md#KVBufferedRefSeqAlongLane.create), [`wait_in`](bref_override.md#BatchingQRef.wait_in), [`wait_in`](bref_override.md#KVBufferedRefHeadAlongSublane.wait_in), [`wait_in`](bref_override.md#KVBufferedRefSeqAlongLane.wait_in), [`wait_out`](bref_override.md#BatchingLSERef.wait_out), [`wait_out`](bref_override.md#BatchingORef.wait_out), [`wait_out`](bref_override.md#KVBufferedRefHeadAlongSublane.wait_out), [`wait_out`](bref_override.md#KVBufferedRefSeqAlongLane.wait_out), [`BatchingLSERef`](bref_override.md#BatchingLSERef), [`BatchingORef`](bref_override.md#BatchingORef), [`BatchingQRef`](bref_override.md#BatchingQRef), [`KVBufferedRefHeadAlongSublane`](bref_override.md#KVBufferedRefHeadAlongSublane), [`KVBufferedRefSeqAlongLane`](bref_override.md#KVBufferedRefSeqAlongLane), [`_BaseBufferedRef`](bref_override.md#_BaseBufferedRef)

## Functions
- <a id="_step_guard"></a>`_step_guard(step: int | jax.Array, total_steps: int | jax.Array)` — [`L114`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/bref_override.py#L114) — Returns `(is_no_op, block_idx)` for a possibly out-of-range pipeline step.

