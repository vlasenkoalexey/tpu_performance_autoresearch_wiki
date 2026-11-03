---
title: 'Module: src/vllm_torchtpu/distributed/kv_transfer/host_kv_shm.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/distributed/kv_transfer/host_kv_shm.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.distributed.kv_transfer.host_kv_shm`/
symbols:
  HostKVShmPool._mlock_blocking: HostKVShmPool#_mlock_blocking().
  HostKVShmPool.layer_view: HostKVShmPool#layer_view().
  HostKVShmPool.create: HostKVShmPool#create().
  HostKVShmPool.rank_layer_views: HostKVShmPool#rank_layer_views().
  HostKVShmPool.unpack_rank_layers: HostKVShmPool#unpack_rank_layers().
  HostKVShmPool.pack_rank: HostKVShmPool#pack_rank().
  HostKVShmPool.unpack_rank: HostKVShmPool#unpack_rank().
  HostKVShmPool._used_per_layer: HostKVShmPool#_used_per_layer().
  PoolSpec.per_layer_bytes: PoolSpec#per_layer_bytes().
  PoolSpec.per_rank_bytes: PoolSpec#per_rank_bytes().
  PoolSpec.per_slot_bytes: PoolSpec#per_slot_bytes().
  HostKVShmPool.release_slot: HostKVShmPool#release_slot().
  _libc_for_mlock: _libc_for_mlock.
  HostKVShmPool._shm: HostKVShmPool#_shm.
  HostKVShmPool.attach: HostKVShmPool#attach().
  HostKVShmPool.close: HostKVShmPool#close().
  logger: logger.
  HostKVShmPool._lock: HostKVShmPool#_lock.
  PoolSpec.num_layers: PoolSpec#num_layers.
  PoolSpec.total_bytes: PoolSpec#total_bytes().
  HostKVShmPool.spec: HostKVShmPool#spec.
  _memmove: _memmove.
  HostKVShmPool.mlock_async: HostKVShmPool#mlock_async().
  HostKVShmPool._free: HostKVShmPool#_free.
  HostKVShmPool.acquire_slot: HostKVShmPool#acquire_slot().
  PoolSpec.num_slots: PoolSpec#num_slots.
  HostKVShmPool: HostKVShmPool#
  HostKVShmPool._munlock_pool: HostKVShmPool#_munlock_pool().
  HostKVShmPool._copy_into_shm: HostKVShmPool#_copy_into_shm().
  PoolSpec: PoolSpec#
  PoolSpec.layer_shard_shape: PoolSpec#layer_shard_shape.
  HostKVShmPool._mlocked_regions: HostKVShmPool#_mlocked_regions.
  HostKVShmPool._mlock_done: HostKVShmPool#_mlock_done.
  PoolSpec.dtype: PoolSpec#dtype.
  HostKVShmPool._mlock_thread: HostKVShmPool#_mlock_thread.
  PoolSpec.tp_size: PoolSpec#tp_size.
  HostKVShmPool._owner: HostKVShmPool#_owner.
  HostKVShmPool.__init__: HostKVShmPool#__init__().
  HostKVShmPool.wait_mlock: HostKVShmPool#wait_mlock().
  _dtype_bytes: _dtype_bytes().
  _shm_base_addr: _shm_base_addr().
  PoolSpec.max_blocks: PoolSpec#max_blocks.
---
# Module: [`src/vllm_torchtpu/distributed/kv_transfer/host_kv_shm.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/host_kv_shm.py)

## Classes
### <a id="HostKVShmPool"></a>`HostKVShmPool`
- def: [`src/vllm_torchtpu/distributed/kv_transfer/host_kv_shm.py:121`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/host_kv_shm.py#L121)
- doc: Per-host shared-memory pool. Rank 0 `create()`s, others `attach()`.
- signature: `class HostKVShmPool:`
- members:
  - <a id="HostKVShmPool._copy_into_shm"></a>`_copy_into_shm(self, offset: int, src: memoryview, nbytes: int)` — [`L389`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/host_kv_shm.py#L389) — Copy a contiguous source buffer into shm.
  - <a id="HostKVShmPool._used_per_layer"></a>`_used_per_layer(self, num_blocks: int)` — [`L319`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/host_kv_shm.py#L319) — Bytes used by one layer's shard at the actual block count.
  - <a id="HostKVShmPool.acquire_slot"></a>`acquire_slot(self, timeout: float | None = None)` — [`L277`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/host_kv_shm.py#L277)
  - <a id="HostKVShmPool.attach"></a>`attach(cls, spec: PoolSpec, name: str)` — [`L261`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/host_kv_shm.py#L261)
  - <a id="HostKVShmPool.close"></a>`close(self)` — [`L429`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/host_kv_shm.py#L429)
  - <a id="HostKVShmPool.create"></a>`create(cls, spec: PoolSpec, name: str)` — [`L236`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/host_kv_shm.py#L236)
  - <a id="HostKVShmPool.layer_view"></a>`layer_view(self, slot_idx: int, rank: int, layer_idx: int, num_blocks: int)` — [`L294`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/host_kv_shm.py#L294) — Return a CPU tensor view over the (slot, rank, layer) region.
  - <a id="HostKVShmPool.mlock_async"></a>`mlock_async(self, my_rank: int | None = None)` — [`L144`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/host_kv_shm.py#L144) — Run mlock(2) on a daemon thread so init isn't blocked.
  - <a id="HostKVShmPool.pack_rank"></a>`pack_rank(self, slot_idx: int, rank: int, num_blocks: int)` — [`L326`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/host_kv_shm.py#L326) — Copy the `num_blocks`-sized shard of each layer into a single
  - <a id="HostKVShmPool.rank_layer_views"></a>`rank_layer_views(self, slot_idx: int, rank: int, num_blocks: int)` — [`L343`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/host_kv_shm.py#L343) — Return one memoryview per layer over the (slot, rank, layer)
  - <a id="HostKVShmPool.release_slot"></a>`release_slot(self, slot_idx: int)` — [`L282`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/host_kv_shm.py#L282)
  - <a id="HostKVShmPool.unpack_rank"></a>`unpack_rank(self, slot_idx: int, rank: int, num_blocks: int, payload)` — [`L409`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/host_kv_shm.py#L409) — Inverse of pack_rank: scatter a received contiguous payload into
  - <a id="HostKVShmPool.unpack_rank_layers"></a>`unpack_rank_layers(self, slot_idx: int, rank: int, num_blocks: int, layer_buffers: list)` — [`L364`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/host_kv_shm.py#L364) — Inverse of rank_layer_views. `layer_buffers` is a list of
  - <a id="HostKVShmPool.wait_mlock"></a>`wait_mlock(self, timeout: float | None = None)` — [`L167`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/host_kv_shm.py#L167) — Block until the async mlock completes (or until timeout). Mainly
  - <a id="HostKVShmPool.spec"></a>`spec` — [`L125`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/host_kv_shm.py#L125)
- protocol/private: <a id="HostKVShmPool.__init__"></a>`__init__`[`L124`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/host_kv_shm.py#L124), <a id="HostKVShmPool._free"></a>`_free`[`L135`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/host_kv_shm.py#L135), <a id="HostKVShmPool._lock"></a>`_lock`[`L136`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/host_kv_shm.py#L136), <a id="HostKVShmPool._mlock_blocking"></a>`_mlock_blocking`[`L173`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/host_kv_shm.py#L173), <a id="HostKVShmPool._mlock_done"></a>`_mlock_done`[`L133`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/host_kv_shm.py#L133), <a id="HostKVShmPool._mlock_thread"></a>`_mlock_thread`[`L132`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/host_kv_shm.py#L132), <a id="HostKVShmPool._mlocked_regions"></a>`_mlocked_regions`[`L131`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/host_kv_shm.py#L131), <a id="HostKVShmPool._munlock_pool"></a>`_munlock_pool`[`L228`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/host_kv_shm.py#L228), <a id="HostKVShmPool._owner"></a>`_owner`[`L127`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/host_kv_shm.py#L127), <a id="HostKVShmPool._shm"></a>`_shm`[`L126`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/host_kv_shm.py#L126)
- uses (calls/refs, reference-scoped): [`per_layer_bytes`](host_kv_shm.md#PoolSpec.per_layer_bytes), [`per_rank_bytes`](host_kv_shm.md#PoolSpec.per_rank_bytes), [`per_slot_bytes`](host_kv_shm.md#PoolSpec.per_slot_bytes), [`_libc_for_mlock`](host_kv_shm.md#_libc_for_mlock), [`logger`](host_kv_shm.md#logger), [`num_layers`](host_kv_shm.md#PoolSpec.num_layers), [`total_bytes`](host_kv_shm.md#PoolSpec.total_bytes), [`_memmove`](host_kv_shm.md#_memmove), [`num_slots`](host_kv_shm.md#PoolSpec.num_slots), [`PoolSpec`](host_kv_shm.md#PoolSpec), [`layer_shard_shape`](host_kv_shm.md#PoolSpec.layer_shard_shape), [`dtype`](host_kv_shm.md#PoolSpec.dtype), [`tp_size`](host_kv_shm.md#PoolSpec.tp_size), [`_dtype_bytes`](host_kv_shm.md#_dtype_bytes), [`_shm_base_addr`](host_kv_shm.md#_shm_base_addr)
- used by: [`_coord_rank0_ipc_loop`](zmq_shm_base.md#ZmqShmKvConnectorBase._coord_rank0_ipc_loop), [`_coord_rank0_handle_new_load`](zmq_shm_base.md#ZmqShmKvConnectorBase._coord_rank0_handle_new_load), [`_coord_rank0_pull`](zmq_shm_base.md#ZmqShmKvConnectorBase._coord_rank0_pull), [`_coord_rank0_handle_new_send`](zmq_shm_base.md#ZmqShmKvConnectorBase._coord_rank0_handle_new_send), [`_coord_rank0_register_copy`](zmq_shm_base.md#ZmqShmKvConnectorBase._coord_rank0_register_copy), [`_coord_scatter_shard`](zmq_shm_base.md#ZmqShmKvConnectorBase._coord_scatter_shard), [`_coord_rank0_build_pull_response`](zmq_shm_base.md#ZmqShmKvConnectorBase._coord_rank0_build_pull_response), [`_coord_get_finished`](zmq_shm_base.md#ZmqShmKvConnectorBase._coord_get_finished), [`_warmup_coord_once`](zmq_shm_base.md#ZmqShmKvConnectorBase._warmup_coord_once), [`_coord_pool`](zmq_shm_base.md#ZmqShmKvConnectorBase._coord_pool), [`_coord_rank0_expire_loop`](zmq_shm_base.md#ZmqShmKvConnectorBase._coord_rank0_expire_loop), [`_pull_channel`](zmq_shm_base.md#ZmqShmKvConnectorBase._pull_channel), [`_coord_teardown`](zmq_shm_base.md#ZmqShmKvConnectorBase._coord_teardown), [`_build_d2h_views`](tpu_connector.md#TPUConnectorWorker._build_d2h_views), [`_pool_attach`](zmq_shm_base.md#ZmqShmKvConnectorBase._pool_attach), [`_pool_create`](zmq_shm_base.md#ZmqShmKvConnectorBase._pool_create)

### <a id="PoolSpec"></a>`PoolSpec`
- def: [`src/vllm_torchtpu/distributed/kv_transfer/host_kv_shm.py:89`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/host_kv_shm.py#L89)
- doc: Describes the per-host pool. Must match byte-for-byte across ranks.
- signature: `class PoolSpec:`
- members:
  - <a id="PoolSpec.per_layer_bytes"></a>`per_layer_bytes(self)` — [`L102`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/host_kv_shm.py#L102)
  - <a id="PoolSpec.per_rank_bytes"></a>`per_rank_bytes(self)` — [`L109`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/host_kv_shm.py#L109)
  - <a id="PoolSpec.per_slot_bytes"></a>`per_slot_bytes(self)` — [`L113`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/host_kv_shm.py#L113)
  - <a id="PoolSpec.total_bytes"></a>`total_bytes(self)` — [`L117`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/host_kv_shm.py#L117)
  - <a id="PoolSpec.dtype"></a>`dtype` — [`L99`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/host_kv_shm.py#L99)
  - <a id="PoolSpec.layer_shard_shape"></a>`layer_shard_shape` — [`L98`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/host_kv_shm.py#L98)
  - <a id="PoolSpec.max_blocks"></a>`max_blocks` — [`L95`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/host_kv_shm.py#L95)
  - <a id="PoolSpec.num_layers"></a>`num_layers` — [`L94`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/host_kv_shm.py#L94)
  - <a id="PoolSpec.num_slots"></a>`num_slots` — [`L92`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/host_kv_shm.py#L92)
  - <a id="PoolSpec.tp_size"></a>`tp_size` — [`L93`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/host_kv_shm.py#L93)
- uses (calls/refs, reference-scoped): [`_dtype_bytes`](host_kv_shm.md#_dtype_bytes)
- used by: [`_build_pool_spec`](zmq_shm_base.md#ZmqShmKvConnectorBase._build_pool_spec), [`_mlock_blocking`](host_kv_shm.md#HostKVShmPool._mlock_blocking), [`layer_view`](host_kv_shm.md#HostKVShmPool.layer_view), [`create`](host_kv_shm.md#HostKVShmPool.create), [`rank_layer_views`](host_kv_shm.md#HostKVShmPool.rank_layer_views), [`unpack_rank_layers`](host_kv_shm.md#HostKVShmPool.unpack_rank_layers), [`pack_rank`](host_kv_shm.md#HostKVShmPool.pack_rank), [`unpack_rank`](host_kv_shm.md#HostKVShmPool.unpack_rank), [`_used_per_layer`](host_kv_shm.md#HostKVShmPool._used_per_layer), [`attach`](host_kv_shm.md#HostKVShmPool.attach), [`_lock`](host_kv_shm.md#HostKVShmPool._lock), [`__init__`](host_kv_shm.md#HostKVShmPool.__init__)

## Functions
- <a id="_dtype_bytes"></a>`_dtype_bytes(dtype: torch.dtype)` — [`L84`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/host_kv_shm.py#L84)
- <a id="_shm_base_addr"></a>`_shm_base_addr(shm: shared_memory.SharedMemory)` — [`L73`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/host_kv_shm.py#L73) — Return the raw mmap base address of a SharedMemory block.

## Module values
- <a id="_libc_for_mlock"></a>`_libc_for_mlock` — [`L64`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/host_kv_shm.py#L64)
- <a id="_memmove"></a>`_memmove` — [`L52`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/host_kv_shm.py#L52)
- <a id="logger"></a>`logger` — [`L49`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/host_kv_shm.py#L49)

