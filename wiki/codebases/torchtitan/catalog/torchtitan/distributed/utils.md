---
title: 'Module: torchtitan/distributed/utils.py'
type: catalog
provenance: extracted
module: torchtitan/distributed/utils.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.distributed.utils`/
symbols:
  get_spmd_backend: get_spmd_backend().
  set_determinism: set_determinism().
  init_distributed: init_distributed().
  is_in_batch_invariant_mode: is_in_batch_invariant_mode().
  get_spmd_context.context: get_spmd_context().context().
  get_spmd_context: get_spmd_context().
  set_batch_invariance: set_batch_invariance().
  set_spmd_backend: set_spmd_backend().
  dist_sum: dist_sum().
  set_pg_timeouts: set_pg_timeouts().
  dist_sum_tensor: dist_sum_tensor().
  check_dtensor_placements_match: check_dtensor_placements_match().
  clip_grad_norm_: clip_grad_norm_().
  enable_fp32_matmul_emulation_with_bf16x9: enable_fp32_matmul_emulation_with_bf16x9().
  dist_max: dist_max().
  init_distributed._warn_overwrite_env: init_distributed()._warn_overwrite_env().
  _dist_reduce: _dist_reduce().
  _batch_invariant_enabled._batch_invariant_enabled: _batch_invariant_enabled._batch_invariant_enabled.
  init_distributed._get_distributed_backend: init_distributed()._get_distributed_backend().
  _spmd_backend: _spmd_backend.
  SpmdContext: SpmdContext#
  dist_mean: dist_mean().
  check_dtensor_placements_match.normalize_dim: check_dtensor_placements_match().normalize_dim().
  _dist_reduce_tensor: _dist_reduce_tensor().
  init_fake_mode: init_fake_mode().
  _clip_grad_norm_with_ep: _clip_grad_norm_with_ep().
  SpmdContext.__call__: SpmdContext#__call__().
---
# Module: [`torchtitan/distributed/utils.py`](../../../../../../raw/code/torchtitan/torchtitan/distributed/utils.py)

## Classes
### <a id="SpmdContext"></a>`SpmdContext`  ·  implements/extends Protocol
- def: [`torchtitan/distributed/utils.py:413`](../../../../../../raw/code/torchtitan/torchtitan/distributed/utils.py#L413)
- signature: `class SpmdContext(Protocol):`
- protocol/private: <a id="SpmdContext.__call__"></a>`__call__`[`L415`](../../../../../../raw/code/torchtitan/torchtitan/distributed/utils.py#L415)
- used by: [`get_spmd_context`](utils.md#get_spmd_context), [`train_context`](../trainer.md#Trainer.train_context)  (1 test-only)

## Functions
- <a id="_clip_grad_norm_with_ep"></a>`_clip_grad_norm_with_ep(parameters: torch.Tensor | Iterable[torch.Tensor], max_norm: float, norm_type: float, error_if_nonfinite: bool, foreach: bool | None, pp_mesh: DeviceMesh | None)` — [`L678`](../../../../../../raw/code/torchtitan/torchtitan/distributed/utils.py#L678)
- <a id="_dist_reduce"></a>`_dist_reduce(x: torch.Tensor, reduceOp: str, mesh: DeviceMesh | None, extra_pg: dist.ProcessGroup | None)` — [`L78`](../../../../../../raw/code/torchtitan/torchtitan/distributed/utils.py#L78) — Perform distributed reduction on a tensor.
- <a id="_dist_reduce_tensor"></a>`_dist_reduce_tensor(x: torch.Tensor, reduceOp: str, mesh: DeviceMesh | None, extra_pg: dist.ProcessGroup | None)` — [`L98`](../../../../../../raw/code/torchtitan/torchtitan/distributed/utils.py#L98) — Perform a distributed reduction without moving the result to the CPU.
- <a id="init_distributed._get_distributed_backend"></a>`_get_distributed_backend(enable_cpu_backend)` — [`L522`](../../../../../../raw/code/torchtitan/torchtitan/distributed/utils.py#L522)
- <a id="init_distributed._warn_overwrite_env"></a>`_warn_overwrite_env(env, val)` — [`L515`](../../../../../../raw/code/torchtitan/torchtitan/distributed/utils.py#L515)
- <a id="check_dtensor_placements_match"></a>`check_dtensor_placements_match(actual: tuple[Placement, ...], expected: tuple[Placement, ...], tensor_ndim: int)` — [`L50`](../../../../../../raw/code/torchtitan/torchtitan/distributed/utils.py#L50) — Compare DTensor placements, normalizing negative Shard dims to tensor rank.
- <a id="clip_grad_norm_"></a>`clip_grad_norm_(parameters: torch.Tensor | Iterable[torch.Tensor], max_norm: float, norm_type: float = 2, error_if_nonfinite: bool = False, foreach: bool | None = None, pp_mesh: DeviceMesh | None = None, ep_enabled: bool = False)` — [`L597`](../../../../../../raw/code/torchtitan/torchtitan/distributed/utils.py#L597) — Clip the gradient norm of an iterable of parameters.
- <a id="get_spmd_context.context"></a>`context()` — [`L425`](../../../../../../raw/code/torchtitan/torchtitan/distributed/utils.py#L425)
- <a id="dist_max"></a>`dist_max(x: torch.Tensor, mesh: DeviceMesh | None = None, extra_pg: dist.ProcessGroup | None = None)` — [`L131`](../../../../../../raw/code/torchtitan/torchtitan/distributed/utils.py#L131)
- <a id="dist_mean"></a>`dist_mean(x: torch.Tensor, mesh: DeviceMesh | None = None, extra_pg: dist.ProcessGroup | None = None)` — [`L162`](../../../../../../raw/code/torchtitan/torchtitan/distributed/utils.py#L162)
- <a id="dist_sum"></a>`dist_sum(x: torch.Tensor, mesh: DeviceMesh | None = None, extra_pg: dist.ProcessGroup | None = None)` — [`L141`](../../../../../../raw/code/torchtitan/torchtitan/distributed/utils.py#L141)
- <a id="dist_sum_tensor"></a>`dist_sum_tensor(x: torch.Tensor, mesh: DeviceMesh | None = None, extra_pg: dist.ProcessGroup | None = None)` — [`L151`](../../../../../../raw/code/torchtitan/torchtitan/distributed/utils.py#L151) — Sum a tensor across process groups and keep the result on its device.
- <a id="enable_fp32_matmul_emulation_with_bf16x9"></a>`enable_fp32_matmul_emulation_with_bf16x9()` — [`L318`](../../../../../../raw/code/torchtitan/torchtitan/distributed/utils.py#L318) — Enable BF16x9 emulation for FP32 CUDA matmuls where supported.
- <a id="get_spmd_backend"></a>`get_spmd_backend()` — [`L45`](../../../../../../raw/code/torchtitan/torchtitan/distributed/utils.py#L45) — Return the active SPMD backend. — documented in [config-overrides](../../../concepts/config-overrides.md)
- <a id="get_spmd_context"></a>`get_spmd_context(*, parallel_dims: ParallelDims | None = None, spmd_typechecking: bool = False)` — [`L419`](../../../../../../raw/code/torchtitan/torchtitan/distributed/utils.py#L419) — documented in [parallel-dims-and-parallelization](../../../concepts/parallel-dims-and-parallelization.md)
- <a id="init_distributed"></a>`init_distributed(comm_config: CommConfig, enable_cpu_backend: bool = False, base_folder: str = "", ranks: list[int] | None = None)` — [`L468`](../../../../../../raw/code/torchtitan/torchtitan/distributed/utils.py#L468)
- <a id="init_fake_mode"></a>`init_fake_mode(world_size: int, *, rank: int = 0)` — [`L450`](../../../../../../raw/code/torchtitan/torchtitan/distributed/utils.py#L450) — Initialize fake backend
- <a id="is_in_batch_invariant_mode"></a>`is_in_batch_invariant_mode()` — [`L313`](../../../../../../raw/code/torchtitan/torchtitan/distributed/utils.py#L313) — Return whether batch-invariant mode is active.
- <a id="check_dtensor_placements_match.normalize_dim"></a>`normalize_dim(dim: int, ndim: int)` — [`L59`](../../../../../../raw/code/torchtitan/torchtitan/distributed/utils.py#L59)
- <a id="set_batch_invariance"></a>`set_batch_invariance(enable: bool)` — [`L340`](../../../../../../raw/code/torchtitan/torchtitan/distributed/utils.py#L340) — Enable batch-invariant mode for reproducible RL training.
- <a id="set_determinism"></a>`set_determinism(parallel_dims: ParallelDims, device: torch.device, debug_config: DebugConfig, distinct_seed_mesh_dims: list[str])` — [`L172`](../../../../../../raw/code/torchtitan/torchtitan/distributed/utils.py#L172) — Set the same DTensor manual seed for all dimensions in world mesh, but only different seeds — documented in [parallel-dims-and-parallelization](../../../concepts/parallel-dims-and-parallelization.md)
- <a id="set_pg_timeouts"></a>`set_pg_timeouts(timeout: timedelta, parallel_dims: ParallelDims)` — [`L565`](../../../../../../raw/code/torchtitan/torchtitan/distributed/utils.py#L565) — Sets the timeout for all PGs in the provided mesh, and the default (world) group.
- <a id="set_spmd_backend"></a>`set_spmd_backend(spmd_backend: str)` — [`L39`](../../../../../../raw/code/torchtitan/torchtitan/distributed/utils.py#L39) — Set the active SPMD backend for distributed runtime helpers.

## Module values
- <a id="_batch_invariant_enabled._batch_invariant_enabled"></a>`_batch_invariant_enabled` — [`L310`](../../../../../../raw/code/torchtitan/torchtitan/distributed/utils.py#L310)
- <a id="_spmd_backend"></a>`_spmd_backend` — [`L36`](../../../../../../raw/code/torchtitan/torchtitan/distributed/utils.py#L36)

