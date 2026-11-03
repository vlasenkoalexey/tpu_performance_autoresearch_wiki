---
title: 'Module: src/vllm_torchtpu/kernels/mla/sparse/native_sc_gather.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/mla/sparse/native_sc_gather.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.mla.sparse.native_sc_gather`/
symbols:
  ROPE_PACKING: ROPE_PACKING.
  dsa_gather_native_sc: dsa_gather_native_sc().
  NUM_LANES: NUM_LANES.
  _kernel.serve_batch: _kernel().serve_batch().
  _kernel.serve_batch.body: _kernel().serve_batch().body().
  _kernel: _kernel().
  OCCURRENCES_PER_ATOM: OCCURRENCES_PER_ATOM.
  _kernel.serve_batch.run_inner: _kernel().serve_batch().run_inner().
  _kernel.serve_batch.destinations: _kernel().serve_batch().destinations().
  _delta_swap: _delta_swap().
  transpose_quad: transpose_quad().
  QUADS_PER_ATOM: QUADS_PER_ATOM.
  _kernel._serve_live: _kernel()._serve_live().
  _kernel.serve_batch.values: _kernel().serve_batch().values().
  NUM_CORES: NUM_CORES.
  NUM_SUBCORES: NUM_SUBCORES.
  ROPE_WORDS: ROPE_WORDS.
---
# Module: [`src/vllm_torchtpu/kernels/mla/sparse/native_sc_gather.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/native_sc_gather.py)

## Functions
- <a id="_delta_swap"></a>`_delta_swap(x, y, shift, mask)` — [`L45`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/native_sc_gather.py#L45)
- <a id="_kernel"></a>`_kernel(nope_hbm_ref: Any, rope_hbm_ref: Any, indices_hbm_ref: Any, nope_out_hbm_ref: Any, rope_out_hbm_ref: Any, sem_ref: Any, live_vmem_ref: Any = None, live_sem_ref: Any = None, *, core_axis_name: str, subcore_axis_name: str, num_owners: int, atoms_per_batch: int, batches_per_owner: int, wait_mode: str, serve_pipelined: bool, live_hbm_ref: Any = None, guard_tail: bool = False, rope_words: int = ROPE_WORDS)` — [`L72`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/native_sc_gather.py#L72)
- <a id="_kernel._serve_live"></a>`_serve_live()` — [`L233`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/native_sc_gather.py#L233)
- <a id="_kernel.serve_batch.body"></a>`body(*refs)` — [`L122`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/native_sc_gather.py#L122)
- <a id="_kernel.serve_batch.destinations"></a>`destinations(atom, stream)` — [`L116`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/native_sc_gather.py#L116)
- <a id="dsa_gather_native_sc"></a>`dsa_gather_native_sc(nope_cache: jax.Array, rope_cache: jax.Array, indices: jax.Array, *, out_size: int, atoms_per_batch: int = 16, wait_mode: str = "overlap_rope", serve_pipelined: bool = True, num_live_indices: jax.Array | None = None, live_multiple: int = 1)` — [`L251`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/native_sc_gather.py#L251) — Gather explicit native-SC ``uint32`` NOPE and ROPE cache rows. — documented in [mla-attention-kernels](../../../../../../concepts/mla-attention-kernels.md)
- <a id="_kernel.serve_batch.run_inner"></a>`run_inner()` — [`L191`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/native_sc_gather.py#L191)
- <a id="_kernel.serve_batch"></a>`serve_batch(indices_ref)` — [`L108`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/native_sc_gather.py#L108)
- <a id="transpose_quad"></a>`transpose_quad(data: list[Any])` — [`L53`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/native_sc_gather.py#L53) — Four tokens' banded words -> four bands of token-interleaved words.
- <a id="_kernel.serve_batch.values"></a>`values(atom, stream)` — [`L113`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/native_sc_gather.py#L113)

## Module values
- <a id="NUM_CORES"></a>`NUM_CORES` — [`L36`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/native_sc_gather.py#L36)
- <a id="NUM_LANES"></a>`NUM_LANES` — [`L38`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/native_sc_gather.py#L38) — documented in [mla-attention-kernels](../../../../../../concepts/mla-attention-kernels.md)
- <a id="NUM_SUBCORES"></a>`NUM_SUBCORES` — [`L37`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/native_sc_gather.py#L37)
- <a id="OCCURRENCES_PER_ATOM"></a>`OCCURRENCES_PER_ATOM` — [`L41`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/native_sc_gather.py#L41)
- <a id="QUADS_PER_ATOM"></a>`QUADS_PER_ATOM` — [`L40`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/native_sc_gather.py#L40)
- <a id="ROPE_PACKING"></a>`ROPE_PACKING` — [`L39`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/native_sc_gather.py#L39) — documented in [mla-attention-kernels](../../../../../../concepts/mla-attention-kernels.md)
- <a id="ROPE_WORDS"></a>`ROPE_WORDS` — [`L42`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/native_sc_gather.py#L42)

