---
title: 'Module: src/vllm_torchtpu/omni/platform.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/omni/platform.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.omni.platform`/
symbols:
  OmniTpuPlatform.set_device: OmniTpuPlatform#set_device().
  OmniTpuPlatform.dist_backend: OmniTpuPlatform#dist_backend().
  OmniTpuPlatform.get_diffusion_attn_backend_cls: OmniTpuPlatform#get_diffusion_attn_backend_cls().
  OmniTpuPlatform._offload_dense_all_to_all: OmniTpuPlatform#_offload_dense_all_to_all().
  OmniTpuPlatform: OmniTpuPlatform#
  OmniTpuPlatform.__init__: OmniTpuPlatform#__init__().
  OmniTpuPlatform.get_device_count: OmniTpuPlatform#get_device_count().
  logger: logger.
  OmniTpuPlatform._worker_world_size: OmniTpuPlatform#_worker_world_size.
  OmniTpuPlatform._set_shared_slicebuilder_addresses: OmniTpuPlatform#_set_shared_slicebuilder_addresses().
  OmniTpuPlatform._omni_enum: OmniTpuPlatform#_omni_enum.
  OmniTpuPlatform.supports_torch_inductor: OmniTpuPlatform#supports_torch_inductor().
  OmniTpuPlatform.supports_diffusion_dense_flash_attention: OmniTpuPlatform#supports_diffusion_dense_flash_attention().
  OmniTpuPlatform.get_profiler_cls: OmniTpuPlatform#get_profiler_cls().
  OmniTpuPlatform.supports_float64: OmniTpuPlatform#supports_float64().
  OmniTpuPlatform.supports_cpu_offload: OmniTpuPlatform#supports_cpu_offload().
  OmniTpuPlatform.get_torch_device: OmniTpuPlatform#get_torch_device().
  OmniTpuPlatform.get_device_version: OmniTpuPlatform#get_device_version().
  OmniTpuPlatform.synchronize: OmniTpuPlatform#synchronize().
  OmniTpuPlatform.empty_cache: OmniTpuPlatform#empty_cache().
  OmniTpuPlatform.get_device_total_memory: OmniTpuPlatform#get_device_total_memory().
  OmniTpuPlatform.get_free_memory: OmniTpuPlatform#get_free_memory().
  OmniTpuPlatform.get_device_memory: OmniTpuPlatform#get_device_memory().
  OmniTpuPlatform.max_memory_reserved: OmniTpuPlatform#max_memory_reserved().
  OmniTpuPlatform.max_memory_allocated: OmniTpuPlatform#max_memory_allocated().
  OmniTpuPlatform.reset_peak_memory_stats: OmniTpuPlatform#reset_peak_memory_stats().
  OmniTpuPlatform.get_omni_ar_worker_cls: OmniTpuPlatform#get_omni_ar_worker_cls().
  OmniTpuPlatform.get_omni_generation_worker_cls: OmniTpuPlatform#get_omni_generation_worker_cls().
  OmniTpuPlatform.get_default_stage_config_path: OmniTpuPlatform#get_default_stage_config_path().
---
# Module: [`src/vllm_torchtpu/omni/platform.py`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/platform.py)

## Classes
### <a id="OmniTpuPlatform"></a>`OmniTpuPlatform`  ·  implements/extends TpuPlatform
- def: [`src/vllm_torchtpu/omni/platform.py:30`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/platform.py#L30) — documented in [omni-diffusion-support](../../../../concepts/omni-diffusion-support.md)
- doc: TPU implementation of OmniPlatform.
- signature: `class OmniTpuPlatform(OmniPlatform, TpuPlatform):`
- members:
  - <a id="OmniTpuPlatform._offload_dense_all_to_all"></a>`_offload_dense_all_to_all()` — [`L121`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/platform.py#L121) — Run dense all-to-alls on SparseCore in multi-rank diffusion workers. — documented in [omni-diffusion-support](../../../../concepts/omni-diffusion-support.md)
  - <a id="OmniTpuPlatform._set_shared_slicebuilder_addresses"></a>`_set_shared_slicebuilder_addresses(world_size: int)` — [`L138`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/platform.py#L138) — Give every diffusion worker the same PjRt slicebuilder addresses.
  - <a id="OmniTpuPlatform.dist_backend"></a>`dist_backend(self)` — [`L43`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/platform.py#L43) — documented in [omni-diffusion-support](../../../../concepts/omni-diffusion-support.md)
  - <a id="OmniTpuPlatform.empty_cache"></a>`empty_cache(cls)` — [`L178`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/platform.py#L178)
  - <a id="OmniTpuPlatform.get_default_stage_config_path"></a>`get_default_stage_config_path(cls)` — [`L224`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/platform.py#L224)
  - <a id="OmniTpuPlatform.get_device_count"></a>`get_device_count(cls)` — [`L166`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/platform.py#L166)
  - <a id="OmniTpuPlatform.get_device_memory"></a>`get_device_memory(cls, device: torch.device | None = None)` — [`L197`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/platform.py#L197)
  - <a id="OmniTpuPlatform.get_device_total_memory"></a>`get_device_total_memory(cls, device_id: int = 0)` — [`L182`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/platform.py#L182)
  - <a id="OmniTpuPlatform.get_device_version"></a>`get_device_version(cls)` — [`L170`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/platform.py#L170)
  - <a id="OmniTpuPlatform.get_diffusion_attn_backend_cls"></a>`get_diffusion_attn_backend_cls(cls, selected_backend: str | None, head_size: int, allow_trtllm_default: bool = False)` — [`L53`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/platform.py#L53) — documented in [omni-diffusion-support](../../../../concepts/omni-diffusion-support.md)
  - <a id="OmniTpuPlatform.get_free_memory"></a>`get_free_memory(cls, device: torch.device | None = None)` — [`L192`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/platform.py#L192)
  - <a id="OmniTpuPlatform.get_omni_ar_worker_cls"></a>`get_omni_ar_worker_cls(cls)` — [`L216`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/platform.py#L216)
  - <a id="OmniTpuPlatform.get_omni_generation_worker_cls"></a>`get_omni_generation_worker_cls(cls)` — [`L220`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/platform.py#L220)
  - <a id="OmniTpuPlatform.get_profiler_cls"></a>`get_profiler_cls(cls)` — [`L86`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/platform.py#L86)
  - <a id="OmniTpuPlatform.get_torch_device"></a>`get_torch_device(cls, _local_rank: int | None = None)` — [`L162`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/platform.py#L162)
  - <a id="OmniTpuPlatform.max_memory_allocated"></a>`max_memory_allocated(cls, device: torch.device | None = None)` — [`L208`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/platform.py#L208)
  - <a id="OmniTpuPlatform.max_memory_reserved"></a>`max_memory_reserved(cls, device: torch.device | None = None)` — [`L204`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/platform.py#L204)
  - <a id="OmniTpuPlatform.reset_peak_memory_stats"></a>`reset_peak_memory_stats(cls, device: torch.device | None = None)` — [`L212`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/platform.py#L212)
  - <a id="OmniTpuPlatform.set_device"></a>`set_device(cls, device: torch.device | int)` — [`L98`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/platform.py#L98) — documented in [omni-diffusion-support](../../../../concepts/omni-diffusion-support.md)
  - <a id="OmniTpuPlatform.supports_cpu_offload"></a>`supports_cpu_offload(cls)` — [`L94`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/platform.py#L94)
  - <a id="OmniTpuPlatform.supports_diffusion_dense_flash_attention"></a>`supports_diffusion_dense_flash_attention(cls)` — [`L82`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/platform.py#L82)
  - <a id="OmniTpuPlatform.supports_float64"></a>`supports_float64(cls)` — [`L90`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/platform.py#L90)
  - <a id="OmniTpuPlatform.supports_torch_inductor"></a>`supports_torch_inductor(cls)` — [`L78`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/platform.py#L78)
  - <a id="OmniTpuPlatform.synchronize"></a>`synchronize(cls, device: torch.device | int | None = None)` — [`L174`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/platform.py#L174)
- protocol/private: <a id="OmniTpuPlatform.__init__"></a>`__init__`[`L48`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/platform.py#L48), <a id="OmniTpuPlatform._omni_enum"></a>`_omni_enum`[`L37`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/platform.py#L37), <a id="OmniTpuPlatform._worker_world_size"></a>`_worker_world_size`[`L40`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/platform.py#L40)
- uses (calls/refs, reference-scoped): [`apply_omni_model_specific_patches`](patches.md#apply_omni_model_specific_patches), [`TpuPlatform`](../platforms/tpu_platform.md#TpuPlatform), [`set_libtpu_flag_default`](../env_override.md#set_libtpu_flag_default), [`_prepare_singlehost_tpu_env`](../platforms/tpu_platform.md#TpuPlatform._prepare_singlehost_tpu_env), [`get_worker_distributed_backend`](../platforms/tpu_platform.md#TpuPlatform.get_worker_distributed_backend), [`apply_omni_tpu_patches`](patches.md#apply_omni_tpu_patches), [`device_count`](../platforms/tpu_platform.md#TpuPlatform.device_count), [`logger`](platform.md#logger)
- used by: [`TpuPlatform`](../platforms/tpu_platform.md#TpuPlatform)

## Module values
- <a id="logger"></a>`logger` — [`L27`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/platform.py#L27)

