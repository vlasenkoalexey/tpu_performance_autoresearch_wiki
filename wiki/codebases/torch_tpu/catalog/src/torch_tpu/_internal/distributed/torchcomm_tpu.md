---
title: 'Module: src/torch_tpu/_internal/distributed/torchcomm_tpu.py'
type: catalog
provenance: extracted
module: src/torch_tpu/_internal/distributed/torchcomm_tpu.py
status: fresh
symbol_base: scip-python python torch_tpu 0.0.0 `src.torch_tpu._internal.distributed.torchcomm_tpu`/
symbols:
  TorchCommsTPU._pg: TorchCommsTPU#_pg.
  TorchCommsTPU._check_not_finalized: TorchCommsTPU#_check_not_finalized().
  TorchCommsTPU.split: TorchCommsTPU#split().
  TorchCommsTPU._device: TorchCommsTPU#_device.
  TorchCommsTPU._rank: TorchCommsTPU#_rank.
  TorchCommsTPU._name: TorchCommsTPU#_name.
  TorchCommsTPU._size: TorchCommsTPU#_size.
  TorchCommsTPU: TorchCommsTPU#
  TorchCommsTPU.reduce_scatter: TorchCommsTPU#reduce_scatter().
  TorchCommsTPU.reduce_scatter_single: TorchCommsTPU#reduce_scatter_single().
  TorchCommsTPU.all_reduce: TorchCommsTPU#all_reduce().
  TorchCommsTPU.finalize: TorchCommsTPU#finalize().
  TorchCommsTPU.all_gather: TorchCommsTPU#all_gather().
  TorchCommsTPU.all_gather_single: TorchCommsTPU#all_gather_single().
  TorchCommsTPU.all_to_all_single: TorchCommsTPU#all_to_all_single().
  _TorchCommBackendBase: _TorchCommBackendBase.
  TorchCommsTPU._finalized: TorchCommsTPU#_finalized.
  TorchCommsTPU.init: TorchCommsTPU#init().
  TorchCommsTPU.broadcast: TorchCommsTPU#broadcast().
  TorchCommsTPU.barrier: TorchCommsTPU#barrier().
  TorchCommsTPU.send: TorchCommsTPU#send().
  TorchCommsTPU.recv: TorchCommsTPU#recv().
  TorchCommsTPU.all_to_all: TorchCommsTPU#all_to_all().
  TorchCommsTPU.split_group: TorchCommsTPU#split_group().
  TorchCommsTPU._store: TorchCommsTPU#_store.
  create_torchcomms_tpu: create_torchcomms_tpu().
  TorchCommTPU: TorchCommTPU.
  _to_dist_reduce_op: _to_dist_reduce_op().
  TorchCommsTPU._backend_name: TorchCommsTPU#_backend_name.
  TorchCommsTPU._timeout: TorchCommsTPU#_timeout.
  TorchCommsTPU.__init__: TorchCommsTPU#__init__().
  TorchCommsTPU.get_comm_name: TorchCommsTPU#get_comm_name().
  TorchCommsTPU.set_timeout: TorchCommsTPU#set_timeout().
  TorchCommsTPU.rank: TorchCommsTPU#rank().
  TorchCommsTPU.size: TorchCommsTPU#size().
  TorchCommsTPU.device: TorchCommsTPU#device().
  TorchCommsTPU.name: TorchCommsTPU#name().
  TorchCommsTPU.backend_name: TorchCommsTPU#backend_name().
  TorchCommsTPU.device_type: TorchCommsTPU#device_type().
  TorchCommsTPU.hints: TorchCommsTPU#hints().
  TorchCommsTPU.store: TorchCommsTPU#store().
  TorchCommsTPU.timeout: TorchCommsTPU#timeout().
  TorchCommsTPU.get_rank: TorchCommsTPU#get_rank().
  TorchCommsTPU.get_size: TorchCommsTPU#get_size().
  TorchCommsTPU.get_device: TorchCommsTPU#get_device().
  TorchCommsTPU.get_name: TorchCommsTPU#get_name().
  TorchCommsTPU.get_backend_name: TorchCommsTPU#get_backend_name().
  TorchCommsTPU.get_backend: TorchCommsTPU#get_backend().
  TorchCommsTPU.unsafe_get_backend: TorchCommsTPU#unsafe_get_backend().
  TorchCommsTPU.is_finalized: TorchCommsTPU#is_finalized().
  TorchCommsTPU.__enter__: TorchCommsTPU#__enter__().
  TorchCommsTPU.__exit__: TorchCommsTPU#__exit__().
  TorchCommsTPU.all_gather_v: TorchCommsTPU#all_gather_v().
  TorchCommsTPU.all_gather_into_tensor: TorchCommsTPU#all_gather_into_tensor().
  TorchCommsTPU.reduce_scatter_v: TorchCommsTPU#reduce_scatter_v().
  TorchCommsTPU.reduce_scatter_tensor: TorchCommsTPU#reduce_scatter_tensor().
  TorchCommsTPU.all_to_all_v_single: TorchCommsTPU#all_to_all_v_single().
  TorchCommsTPU.create_pair_comm: TorchCommsTPU#create_pair_comm().
  TorchCommsTPU.reconfigure: TorchCommsTPU#reconfigure().
  TorchCommsTPU.create_window: TorchCommsTPU#create_window().
  TorchCommsTPU.map_remote_tensor: TorchCommsTPU#map_remote_tensor().
  TorchCommsTPU.create_batch: TorchCommsTPU#create_batch().
  TorchCommsTPU.all_reduce_coalesced: TorchCommsTPU#all_reduce_coalesced().
  TorchCommsTPU.all_gather_coalesced: TorchCommsTPU#all_gather_coalesced().
  TorchCommsTPU.reduce_scatter_coalesced: TorchCommsTPU#reduce_scatter_coalesced().
  TorchCommsTPU.all_to_all_coalesced: TorchCommsTPU#all_to_all_coalesced().
  TorchCommsTPU.reduce: TorchCommsTPU#reduce().
  TorchCommsTPU.gather: TorchCommsTPU#gather().
  TorchCommsTPU.scatter: TorchCommsTPU#scatter().
  TorchCommsTPU.monitored_barrier: TorchCommsTPU#monitored_barrier().
  TorchCommsTPU.register_flight_recorder_hook: TorchCommsTPU#register_flight_recorder_hook().
  TorchCommsTPU.get_flight_recorder_traces: TorchCommsTPU#get_flight_recorder_traces().
  TorchCommsTPU.broadcast_object_list: TorchCommsTPU#broadcast_object_list().
  TorchCommsTPU.all_gather_object: TorchCommsTPU#all_gather_object().
  TorchCommsTPU.gather_object: TorchCommsTPU#gather_object().
  TorchCommsTPU.scatter_object_list: TorchCommsTPU#scatter_object_list().
  create_torchcomm_tpu: create_torchcomm_tpu.
  register_torchcomms_tpu: register_torchcomms_tpu().
  _get_first_int_env_once: _get_first_int_env_once().
  TorchCommsTPU._hints: TorchCommsTPU#_hints.
  is_torchcomms_registered: is_torchcomms_registered().
---
# Module: [`src/torch_tpu/_internal/distributed/torchcomm_tpu.py`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/torchcomm_tpu.py)

## Classes
### <a id="TorchCommsTPU"></a>`TorchCommsTPU`
- def: [`src/torch_tpu/_internal/distributed/torchcomm_tpu.py:96`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/torchcomm_tpu.py#L96) — documented in [distributed-launchers-and-spmd](../../../../../concepts/distributed-launchers-and-spmd.md)
- doc: TorchComms communicator implementation for TPU devices.
- signature: `class TorchCommsTPU(_TorchCommBackendBase):`
- members:
  - <a id="TorchCommsTPU.all_gather"></a>`all_gather(self, tensor_list: list[torch.Tensor], tensor: torch.Tensor, async_op: bool = False)` — [`L373`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/torchcomm_tpu.py#L373) — documented in [distributed-launchers-and-spmd](../../../../../concepts/distributed-launchers-and-spmd.md)
  - <a id="TorchCommsTPU.all_gather_coalesced"></a>`all_gather_coalesced(self, output_lists: list[list[torch.Tensor]], input_list: list[torch.Tensor], async_op: bool = False)` — [`L667`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/torchcomm_tpu.py#L667) — Coalesced all-gather across lists of tensors.
  - <a id="TorchCommsTPU.all_gather_into_tensor"></a>`all_gather_into_tensor(self, output: torch.Tensor, input: torch.Tensor, async_op: bool = False)` — [`L412`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/torchcomm_tpu.py#L412) — Alias for all_gather_single.
  - <a id="TorchCommsTPU.all_gather_object"></a>`all_gather_object(self, object_list: list[Any], obj: Any)` — [`L780`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/torchcomm_tpu.py#L780) — All-gathers picklable Python objects across all ranks.
  - <a id="TorchCommsTPU.all_gather_single"></a>`all_gather_single(self, output: torch.Tensor, input: torch.Tensor, async_op: bool = False)` — [`L397`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/torchcomm_tpu.py#L397) — documented in [distributed-launchers-and-spmd](../../../../../concepts/distributed-launchers-and-spmd.md)
  - <a id="TorchCommsTPU.all_gather_v"></a>`all_gather_v(self, tensor_list: list[torch.Tensor], tensor: torch.Tensor, async_op: bool = False)` — [`L388`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/torchcomm_tpu.py#L388) — Vectorized all_gather for variable-size tensors.
  - <a id="TorchCommsTPU.all_reduce"></a>`all_reduce(self, tensor: torch.Tensor, op: Any = dist.ReduceOp.SUM, async_op: bool = False)` — [`L357`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/torchcomm_tpu.py#L357) — documented in [distributed-launchers-and-spmd](../../../../../concepts/distributed-launchers-and-spmd.md)
  - <a id="TorchCommsTPU.all_reduce_coalesced"></a>`all_reduce_coalesced(self, tensors: list[torch.Tensor], op: dist.ReduceOp = dist.ReduceOp.SUM, async_op: bool = False)` — [`L655`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/torchcomm_tpu.py#L655) — Coalesced all-reduce across a list of tensors.
  - <a id="TorchCommsTPU.all_to_all"></a>`all_to_all(self, output_list: list[torch.Tensor], input_list: list[torch.Tensor], async_op: bool = False)` — [`L538`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/torchcomm_tpu.py#L538)
  - <a id="TorchCommsTPU.all_to_all_coalesced"></a>`all_to_all_coalesced(self, output_lists: list[list[torch.Tensor]], input_lists: list[list[torch.Tensor]], async_op: bool = False)` — [`L692`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/torchcomm_tpu.py#L692) — Coalesced all-to-all across lists of tensors.
  - <a id="TorchCommsTPU.all_to_all_single"></a>`all_to_all_single(self, output: torch.Tensor, input: torch.Tensor, output_split_sizes: list[int] | None = None, input_split_sizes: list[int] | None = None, async_op: bool = False)` — [`L553`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/torchcomm_tpu.py#L553) — documented in [distributed-launchers-and-spmd](../../../../../concepts/distributed-launchers-and-spmd.md)
  - <a id="TorchCommsTPU.all_to_all_v_single"></a>`all_to_all_v_single(self, output: torch.Tensor, input: torch.Tensor, output_split_sizes: list[int] | None = None, input_split_sizes: list[int] | None = None, async_op: bool = False, output_splits: list[int] | None = None, input_splits: list[int] | None = None)` — [`L572`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/torchcomm_tpu.py#L572) — Vectorized all_to_all_single.
  - <a id="TorchCommsTPU.backend_name"></a>`backend_name(self)` — [`L239`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/torchcomm_tpu.py#L239) — The backend name string ('tpu').
  - <a id="TorchCommsTPU.barrier"></a>`barrier(self, async_op: bool = False)` — [`L492`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/torchcomm_tpu.py#L492)
  - <a id="TorchCommsTPU.broadcast"></a>`broadcast(self, tensor: torch.Tensor, root: int = 0, async_op: bool = False, src: int | None = None)` — [`L475`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/torchcomm_tpu.py#L475)
  - <a id="TorchCommsTPU.broadcast_object_list"></a>`broadcast_object_list(self, object_list: list[Any], src: int = 0, device: torch.device | None = None)` — [`L768`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/torchcomm_tpu.py#L768) — Broadcasts a list of picklable Python objects from src rank.
  - <a id="TorchCommsTPU.create_batch"></a>`create_batch(self)` — [`L648`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/torchcomm_tpu.py#L648) — Creates a batch handle to coalesce collective operations.
  - <a id="TorchCommsTPU.create_pair_comm"></a>`create_pair_comm(self, peer_rank: int, hints: dict[str, Any] | None = None)` — [`L595`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/torchcomm_tpu.py#L595) — Creates a dedicated 1-to-1 PairComm with a peer rank.
  - <a id="TorchCommsTPU.create_window"></a>`create_window(self, tensor: torch.Tensor, hints: dict[str, Any] | None = None)` — [`L628`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/torchcomm_tpu.py#L628) — Creates a one-sided RMA Window allocation over a tensor.
  - <a id="TorchCommsTPU.device"></a>`device(self)` — [`L229`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/torchcomm_tpu.py#L229) — The TPU device bound to this communicator.
  - <a id="TorchCommsTPU.device_type"></a>`device_type(self)` — [`L244`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/torchcomm_tpu.py#L244) — The device type string ('tpu').
  - <a id="TorchCommsTPU.finalize"></a>`finalize(self)` — [`L295`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/torchcomm_tpu.py#L295) — Release communicator resources and mark as finalized.
  - <a id="TorchCommsTPU.gather"></a>`gather(self, output_list: list[torch.Tensor] | None = None, input_tensor: torch.Tensor | None = None, dst: int = 0, async_op: bool = False)` — [`L717`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/torchcomm_tpu.py#L717) — Gathers tensors from all ranks into output_list on dst rank.
  - <a id="TorchCommsTPU.gather_object"></a>`gather_object(self, obj: Any, object_gather_list: list[Any] | None = None, dst: int = 0)` — [`L791`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/torchcomm_tpu.py#L791) — Gathers picklable Python objects to dst rank.
  - <a id="TorchCommsTPU.get_backend"></a>`get_backend(self)` — [`L283`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/torchcomm_tpu.py#L283) — Return the underlying backend object.
  - <a id="TorchCommsTPU.get_backend_name"></a>`get_backend_name(self)` — [`L279`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/torchcomm_tpu.py#L279) — Return the backend name string.
  - <a id="TorchCommsTPU.get_comm_name"></a>`get_comm_name(self)` — [`L210`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/torchcomm_tpu.py#L210) — Returns the communicator name.
  - <a id="TorchCommsTPU.get_device"></a>`get_device(self)` — [`L271`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/torchcomm_tpu.py#L271) — Return the bound device.
  - <a id="TorchCommsTPU.get_flight_recorder_traces"></a>`get_flight_recorder_traces(self)` — [`L760`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/torchcomm_tpu.py#L760) — Returns recent circular buffer collective traces.
  - <a id="TorchCommsTPU.get_name"></a>`get_name(self)` — [`L275`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/torchcomm_tpu.py#L275) — Return the communicator name.
  - <a id="TorchCommsTPU.get_rank"></a>`get_rank(self)` — [`L263`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/torchcomm_tpu.py#L263) — Return the communicator rank.
  - <a id="TorchCommsTPU.get_size"></a>`get_size(self)` — [`L267`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/torchcomm_tpu.py#L267) — Return the communicator world size.
  - <a id="TorchCommsTPU.hints"></a>`hints(self)` — [`L249`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/torchcomm_tpu.py#L249) — Communicator hints dictionary.
  - <a id="TorchCommsTPU.init"></a>`init(self, device: torch.device | str | None = None, name: str | None = None, options: Any = None)` — [`L182`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/torchcomm_tpu.py#L182) — Initializes the backend when instantiated via torchcomms.register_backend.
  - <a id="TorchCommsTPU.is_finalized"></a>`is_finalized(self)` — [`L291`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/torchcomm_tpu.py#L291) — Check if the communicator has been finalized/closed.
  - <a id="TorchCommsTPU.map_remote_tensor"></a>`map_remote_tensor(self, tensor: torch.Tensor, peer_rank: int)` — [`L638`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/torchcomm_tpu.py#L638) — Maps a remote rank's tensor memory into local address space.
  - <a id="TorchCommsTPU.monitored_barrier"></a>`monitored_barrier(self, timeout: Any = None, wait_all_ranks: bool = True)` — [`L743`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/torchcomm_tpu.py#L743) — Monitored health-check barrier across ranks.
  - <a id="TorchCommsTPU.name"></a>`name(self)` — [`L234`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/torchcomm_tpu.py#L234) — The unique name of the communicator.
  - <a id="TorchCommsTPU.rank"></a>`rank(self)` — [`L219`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/torchcomm_tpu.py#L219) — The rank of this process within the communicator.
  - <a id="TorchCommsTPU.reconfigure"></a>`reconfigure(self, ranks: list[int] | None = None, size: int | None = None, timeout: Any = None)` — [`L615`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/torchcomm_tpu.py#L615) — Dynamically reconfigures communicator topology or rank membership.
  - <a id="TorchCommsTPU.recv"></a>`recv(self, tensor: torch.Tensor, src: int, async_op: bool = False, tag: int = 0)` — [`L522`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/torchcomm_tpu.py#L522)
  - <a id="TorchCommsTPU.reduce"></a>`reduce(self, tensor: torch.Tensor, dst: int = 0, op: dist.ReduceOp = dist.ReduceOp.SUM, async_op: bool = False)` — [`L704`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/torchcomm_tpu.py#L704) — Reduces a tensor to a single destination root rank.
  - <a id="TorchCommsTPU.reduce_scatter"></a>`reduce_scatter(self, output: torch.Tensor, tensor_list: list[torch.Tensor], op: Any = dist.ReduceOp.SUM, async_op: bool = False)` — [`L421`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/torchcomm_tpu.py#L421) — documented in [distributed-launchers-and-spmd](../../../../../concepts/distributed-launchers-and-spmd.md)
  - <a id="TorchCommsTPU.reduce_scatter_coalesced"></a>`reduce_scatter_coalesced(self, output_list: list[torch.Tensor], input_lists: list[list[torch.Tensor]], op: dist.ReduceOp = dist.ReduceOp.SUM, async_op: bool = False)` — [`L679`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/torchcomm_tpu.py#L679) — Coalesced reduce-scatter across lists of tensors.
  - <a id="TorchCommsTPU.reduce_scatter_single"></a>`reduce_scatter_single(self, output: torch.Tensor, input: torch.Tensor, op: Any = dist.ReduceOp.SUM, async_op: bool = False)` — [`L448`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/torchcomm_tpu.py#L448) — documented in [distributed-launchers-and-spmd](../../../../../concepts/distributed-launchers-and-spmd.md)
  - <a id="TorchCommsTPU.reduce_scatter_tensor"></a>`reduce_scatter_tensor(self, output: torch.Tensor, input: torch.Tensor, op: Any = dist.ReduceOp.SUM, async_op: bool = False)` — [`L465`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/torchcomm_tpu.py#L465) — Alias for reduce_scatter_single.
  - <a id="TorchCommsTPU.reduce_scatter_v"></a>`reduce_scatter_v(self, output: torch.Tensor, input_list: list[torch.Tensor], op: Any = dist.ReduceOp.SUM, async_op: bool = False)` — [`L438`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/torchcomm_tpu.py#L438) — Vectorized reduce_scatter.
  - <a id="TorchCommsTPU.register_flight_recorder_hook"></a>`register_flight_recorder_hook(self, hook: Any)` — [`L752`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/torchcomm_tpu.py#L752) — Registers a FlightRecorder tracing hook.
  - <a id="TorchCommsTPU.scatter"></a>`scatter(self, output_tensor: torch.Tensor, scatter_list: list[torch.Tensor] | None = None, src: int = 0, async_op: bool = False)` — [`L730`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/torchcomm_tpu.py#L730) — Scatters a list of tensors from src rank to all ranks.
  - <a id="TorchCommsTPU.scatter_object_list"></a>`scatter_object_list(self, scatter_object_output_list: list[Any], scatter_object_input_list: list[Any] | None = None, src: int = 0)` — [`L803`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/torchcomm_tpu.py#L803) — Scatters a list of picklable Python objects from src rank.
  - <a id="TorchCommsTPU.send"></a>`send(self, tensor: torch.Tensor, dst: int, async_op: bool = False, tag: int = 0)` — [`L506`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/torchcomm_tpu.py#L506)
  - <a id="TorchCommsTPU.set_timeout"></a>`set_timeout(self, timeout: datetime.timedelta)` — [`L214`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/torchcomm_tpu.py#L214) — Sets the communicator timeout.
  - <a id="TorchCommsTPU.size"></a>`size(self)` — [`L224`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/torchcomm_tpu.py#L224) — The total number of processes in the communicator.
  - <a id="TorchCommsTPU.split"></a>`split(self, ranks_or_color: Any = None, name_or_key: Any = None, options: Any = None, *, color: int | None = None, key: int | None = None)` — [`L308`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/torchcomm_tpu.py#L308) — Creates a new subgroup communicator. — documented in [distributed-launchers-and-spmd](../../../../../concepts/distributed-launchers-and-spmd.md)
  - <a id="TorchCommsTPU.split_group"></a>`split_group(self, ranks: list[int], hints: dict[str, Any] | None = None)` — [`L605`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/torchcomm_tpu.py#L605) — Creates a subgroup communicator for an explicit list of ranks.
  - <a id="TorchCommsTPU.store"></a>`store(self)` — [`L254`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/torchcomm_tpu.py#L254) — The underlying rendezvous store if provided.
  - <a id="TorchCommsTPU.timeout"></a>`timeout(self)` — [`L259`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/torchcomm_tpu.py#L259) — Communicator timeout duration.
  - <a id="TorchCommsTPU.unsafe_get_backend"></a>`unsafe_get_backend(self)` — [`L287`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/torchcomm_tpu.py#L287) — Directly access the underlying backend object.
- protocol/private: <a id="TorchCommsTPU.__enter__"></a>`__enter__`[`L302`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/torchcomm_tpu.py#L302), <a id="TorchCommsTPU.__exit__"></a>`__exit__`[`L305`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/torchcomm_tpu.py#L305), <a id="TorchCommsTPU.__init__"></a>`__init__`[`L104`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/torchcomm_tpu.py#L104), <a id="TorchCommsTPU._backend_name"></a>`_backend_name`[`L118`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/torchcomm_tpu.py#L118), <a id="TorchCommsTPU._check_not_finalized"></a>`_check_not_finalized`[`L349`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/torchcomm_tpu.py#L349), <a id="TorchCommsTPU._device"></a>`_device`[`L123`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/torchcomm_tpu.py#L123), <a id="TorchCommsTPU._finalized"></a>`_finalized`[`L157`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/torchcomm_tpu.py#L157), <a id="TorchCommsTPU._hints"></a>`_hints`[`L155`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/torchcomm_tpu.py#L155), <a id="TorchCommsTPU._name"></a>`_name`[`L153`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/torchcomm_tpu.py#L153), <a id="TorchCommsTPU._pg"></a>`_pg`[`L161`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/torchcomm_tpu.py#L161), <a id="TorchCommsTPU._rank"></a>`_rank`[`L140`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/torchcomm_tpu.py#L140), <a id="TorchCommsTPU._size"></a>`_size`[`L147`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/torchcomm_tpu.py#L147), <a id="TorchCommsTPU._store"></a>`_store`[`L154`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/torchcomm_tpu.py#L154), <a id="TorchCommsTPU._timeout"></a>`_timeout`[`L156`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/torchcomm_tpu.py#L156)
- uses (calls/refs, reference-scoped): [`_TorchCommBackendBase`](torchcomm_tpu.md#_TorchCommBackendBase), [`TorchCommTPU`](torchcomm_tpu.md#TorchCommTPU), [`_to_dist_reduce_op`](torchcomm_tpu.md#_to_dist_reduce_op), [`_get_first_int_env_once`](torchcomm_tpu.md#_get_first_int_env_once)
- used by: [`TorchCommTPU`](torchcomm_tpu.md#TorchCommTPU), [`create_torchcomms_tpu`](torchcomm_tpu.md#create_torchcomms_tpu), [`register_torchcomms_tpu`](torchcomm_tpu.md#register_torchcomms_tpu)

## Functions
- <a id="_get_first_int_env_once"></a>`_get_first_int_env_once(names: tuple[str, ...], default_value: int)` — [`L41`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/torchcomm_tpu.py#L41) — Returns the value of the first of `names` that is set to an integer.
- <a id="_to_dist_reduce_op"></a>`_to_dist_reduce_op(op: Any)` — [`L59`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/torchcomm_tpu.py#L59) — Converts torchcomms.ReduceOp or dist.ReduceOp to dist.ReduceOp.
- <a id="create_torchcomms_tpu"></a>`create_torchcomms_tpu(backend_str: str, device: torch.device | str | None, name: str | None = None, store: dist.Store | None = None, hints: dict[str, Any] | None = None)` — [`L816`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/torchcomm_tpu.py#L816) — Factory function to instantiate a TorchCommsTPU communicator.
- <a id="is_torchcomms_registered"></a>`is_torchcomms_registered(backend_name: str = "tpu")` — [`L874`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/torchcomm_tpu.py#L874) — Check whether the given backend is registered in torchcomms.
- <a id="register_torchcomms_tpu"></a>`register_torchcomms_tpu()` — [`L838`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/torchcomm_tpu.py#L838) — Registers the TPU backend with torchcomms and torch.distributed.Backend.

## Module values
- <a id="TorchCommTPU"></a>`TorchCommTPU` — [`L834`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/torchcomm_tpu.py#L834)
- <a id="_TorchCommBackendBase"></a>`_TorchCommBackendBase` — [`L36`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/torchcomm_tpu.py#L36)
- <a id="create_torchcomm_tpu"></a>`create_torchcomm_tpu` — [`L835`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/torchcomm_tpu.py#L835)

