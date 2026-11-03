---
title: 'Module: src/vllm_torchtpu/omni/patches.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/omni/patches.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.omni.patches`/
symbols:
  apply_omni_model_specific_patches: apply_omni_model_specific_patches().
  _patch_ltx2_split_rope: _patch_ltx2_split_rope().
  logger: logger.
  _patch_wan_fused_qk_norm_rope: _patch_wan_fused_qk_norm_rope().
  _patch_sdpa_fallback_dispatch: _patch_sdpa_fallback_dispatch().
  _patch_ltx2_vocoder_cpu_init: _patch_ltx2_vocoder_cpu_init().
  _patch_diffusion_worker_d2h_stream: _patch_diffusion_worker_d2h_stream().
  _wrap_ltx2_bwe_filter_restore: _wrap_ltx2_bwe_filter_restore().
  _patch_ltx2_split_rope._cached_rope_forward: _patch_ltx2_split_rope()._cached_rope_forward().
  _patch_diffusion_ipc_cpu_pack: _patch_diffusion_ipc_cpu_pack().
  _patch_qwen_image_rope_txt_freqs_clone: _patch_qwen_image_rope_txt_freqs_clone().
  _patch_wan_pair_swap_rope: _patch_wan_pair_swap_rope().
  _patch_wan_ffn_gelu_fence: _patch_wan_ffn_gelu_fence().
  _patch_diffusion_startup_warmup_sync: _patch_diffusion_startup_warmup_sync().
  _patch_wan_fused_qk_norm_rope._fused_self_attention_forward: _patch_wan_fused_qk_norm_rope()._fused_self_attention_forward().
  _patch_wan_fresh_timestep: _patch_wan_fresh_timestep().
  _wrap_fresh_timestep: _wrap_fresh_timestep().
  apply_omni_tpu_patches: apply_omni_tpu_patches().
  _patch_diffusion_worker_d2h_stream._tpu_async_output_loop: _patch_diffusion_worker_d2h_stream()._tpu_async_output_loop().
  _wrap_fresh_timestep._fresh_timestep_forward: _wrap_fresh_timestep()._fresh_timestep_forward().
  _optimization_barrier_op: _optimization_barrier_op().
  _clone_txt_freqs: _clone_txt_freqs().
  _patch_wan_ffn_gelu_fence._fenced_gelu_forward: _patch_wan_ffn_gelu_fence()._fenced_gelu_forward().
  _patch_ltx2_split_rope._apply_split_rotary_emb: _patch_ltx2_split_rope()._apply_split_rotary_emb().
  _D2H_STREAM_PATCHED: _D2H_STREAM_PATCHED.
  _FRESH_TIMESTEP_PATCHED: _FRESH_TIMESTEP_PATCHED.
  _SDPA_FALLBACK_PATCHED: _SDPA_FALLBACK_PATCHED.
  _VOCODER_CPU_INIT_PATCHED: _VOCODER_CPU_INIT_PATCHED.
  _patch_ltx2_vocoder_cpu_init._cpu_vocoder_load_component: _patch_ltx2_vocoder_cpu_init()._cpu_vocoder_load_component().
  _BWE_FILTER_CPU_RESTORE_PATCHED: _BWE_FILTER_CPU_RESTORE_PATCHED.
  _wrap_ltx2_bwe_filter_restore._cpu_restore_ltx_bwe_resampler_filter: _wrap_ltx2_bwe_filter_restore()._cpu_restore_ltx_bwe_resampler_filter().
  _SPLIT_ROPE_PATCHED: _SPLIT_ROPE_PATCHED.
  _patch_diffusion_ipc_cpu_pack._safe_pack_tensor_if_large: _patch_diffusion_ipc_cpu_pack()._safe_pack_tensor_if_large().
  _clone_txt_freqs._forward: _clone_txt_freqs()._forward().
  _patch_diffusion_startup_warmup_sync._synced_run_startup_warmup: _patch_diffusion_startup_warmup_sync()._synced_run_startup_warmup().
  _CurrentDeviceWorkerProxy: _CurrentDeviceWorkerProxy#
  _CurrentDeviceWorkerProxy.__init__: _CurrentDeviceWorkerProxy#__init__().
  _CurrentDeviceWorkerProxy.__getattr__: _CurrentDeviceWorkerProxy#__getattr__().
  _CurrentDeviceWorkerProxy.__setattr__: _CurrentDeviceWorkerProxy#__setattr__().
---
# Module: [`src/vllm_torchtpu/omni/patches.py`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/patches.py)

## Classes
### <a id="_CurrentDeviceWorkerProxy"></a>`_CurrentDeviceWorkerProxy`
- def: [`src/vllm_torchtpu/omni/patches.py:246`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/patches.py#L246)
- protocol/private: <a id="_CurrentDeviceWorkerProxy.__getattr__"></a>`__getattr__`[`L253`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/patches.py#L253), <a id="_CurrentDeviceWorkerProxy.__init__"></a>`__init__`[`L250`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/patches.py#L250), <a id="_CurrentDeviceWorkerProxy.__setattr__"></a>`__setattr__`[`L258`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/patches.py#L258)
- used by: [`_tpu_async_output_loop`](patches.md#_patch_diffusion_worker_d2h_stream._tpu_async_output_loop)

## Functions
- <a id="_patch_ltx2_split_rope._apply_split_rotary_emb"></a>`_apply_split_rotary_emb(x: torch.Tensor, freqs: tuple[torch.Tensor, torch.Tensor], *, head_dim: int)` — [`L621`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/patches.py#L621) — documented in [omni-diffusion-support](../../../../concepts/omni-diffusion-support.md)
- <a id="_patch_ltx2_split_rope._cached_rope_forward"></a>`_cached_rope_forward(self: Any, coords: torch.Tensor, device: str | torch.device | None = None, out_dtype: torch.dtype | None = None)` — [`L585`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/patches.py#L585) — documented in [omni-diffusion-support](../../../../concepts/omni-diffusion-support.md)
- <a id="_clone_txt_freqs"></a>`_clone_txt_freqs(forward: Any)` — [`L141`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/patches.py#L141)
- <a id="_wrap_ltx2_bwe_filter_restore._cpu_restore_ltx_bwe_resampler_filter"></a>`_cpu_restore_ltx_bwe_resampler_filter(vocoder: Any)` — [`L498`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/patches.py#L498)
- <a id="_patch_ltx2_vocoder_cpu_init._cpu_vocoder_load_component"></a>`_cpu_vocoder_load_component(component_cls: Any, model: str, subfolder: str, *args: Any, **kwargs: Any)` — [`L469`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/patches.py#L469)
- <a id="_patch_wan_ffn_gelu_fence._fenced_gelu_forward"></a>`_fenced_gelu_forward(self: Any, x: torch.Tensor)` — [`L202`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/patches.py#L202) — documented in [omni-diffusion-support](../../../../concepts/omni-diffusion-support.md)
- <a id="_clone_txt_freqs._forward"></a>`_forward(self: Any, *args: Any, **kwargs: Any)` — [`L142`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/patches.py#L142)
- <a id="_wrap_fresh_timestep._fresh_timestep_forward"></a>`_fresh_timestep_forward(self: Any, hidden_states: Any, timestep: Any, *args: Any, **kwargs: Any)` — [`L388`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/patches.py#L388) — documented in [omni-diffusion-support](../../../../concepts/omni-diffusion-support.md)
- <a id="_patch_wan_fused_qk_norm_rope._fused_self_attention_forward"></a>`_fused_self_attention_forward(self: Any, hidden_states: torch.Tensor, rotary_emb: Any = None, attn_metadata: Any = None)` — [`L324`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/patches.py#L324) — documented in [omni-diffusion-support](../../../../concepts/omni-diffusion-support.md)
- <a id="_optimization_barrier_op"></a>`_optimization_barrier_op()` — [`L36`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/patches.py#L36)
- <a id="_patch_diffusion_ipc_cpu_pack"></a>`_patch_diffusion_ipc_cpu_pack()` — [`L89`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/patches.py#L89) — documented in [omni-diffusion-support](../../../../concepts/omni-diffusion-support.md)
- <a id="_patch_diffusion_startup_warmup_sync"></a>`_patch_diffusion_startup_warmup_sync()` — [`L265`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/patches.py#L265) — Synchronize the device after vLLM-Omni's diffusion startup warmup. — documented in [omni-diffusion-support](../../../../concepts/omni-diffusion-support.md)
- <a id="_patch_diffusion_worker_d2h_stream"></a>`_patch_diffusion_worker_d2h_stream()` — [`L212`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/patches.py#L212) — documented in [omni-diffusion-support](../../../../concepts/omni-diffusion-support.md)
- <a id="_patch_ltx2_split_rope"></a>`_patch_ltx2_split_rope()` — [`L533`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/patches.py#L533) — documented in [omni-diffusion-support](../../../../concepts/omni-diffusion-support.md)
- <a id="_patch_ltx2_vocoder_cpu_init"></a>`_patch_ltx2_vocoder_cpu_init()` — [`L438`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/patches.py#L438) — documented in [omni-diffusion-support](../../../../concepts/omni-diffusion-support.md)
- <a id="_patch_qwen_image_rope_txt_freqs_clone"></a>`_patch_qwen_image_rope_txt_freqs_clone()` — [`L118`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/patches.py#L118) — documented in [omni-diffusion-support](../../../../concepts/omni-diffusion-support.md)
- <a id="_patch_sdpa_fallback_dispatch"></a>`_patch_sdpa_fallback_dispatch()` — [`L405`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/patches.py#L405) — documented in [omni-diffusion-support](../../../../concepts/omni-diffusion-support.md)
- <a id="_patch_wan_ffn_gelu_fence"></a>`_patch_wan_ffn_gelu_fence()` — [`L177`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/patches.py#L177) — documented in [omni-diffusion-support](../../../../concepts/omni-diffusion-support.md)
- <a id="_patch_wan_fresh_timestep"></a>`_patch_wan_fresh_timestep()` — [`L340`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/patches.py#L340) — documented in [omni-diffusion-support](../../../../concepts/omni-diffusion-support.md)
- <a id="_patch_wan_fused_qk_norm_rope"></a>`_patch_wan_fused_qk_norm_rope()` — [`L297`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/patches.py#L297) — documented in [omni-diffusion-support](../../../../concepts/omni-diffusion-support.md)
- <a id="_patch_wan_pair_swap_rope"></a>`_patch_wan_pair_swap_rope()` — [`L149`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/patches.py#L149) — documented in [omni-diffusion-support](../../../../concepts/omni-diffusion-support.md)
- <a id="_patch_diffusion_ipc_cpu_pack._safe_pack_tensor_if_large"></a>`_safe_pack_tensor_if_large(val: torch.Tensor, *args: Any, **kwargs: Any)` — [`L111`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/patches.py#L111)
- <a id="_patch_diffusion_startup_warmup_sync._synced_run_startup_warmup"></a>`_synced_run_startup_warmup(self: Any)` — [`L286`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/patches.py#L286)
- <a id="_patch_diffusion_worker_d2h_stream._tpu_async_output_loop"></a>`_tpu_async_output_loop(self: Any)` — [`L238`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/patches.py#L238) — documented in [omni-diffusion-support](../../../../concepts/omni-diffusion-support.md)
- <a id="_wrap_fresh_timestep"></a>`_wrap_fresh_timestep(cls: type)` — [`L380`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/patches.py#L380) — documented in [omni-diffusion-support](../../../../concepts/omni-diffusion-support.md)
- <a id="_wrap_ltx2_bwe_filter_restore"></a>`_wrap_ltx2_bwe_filter_restore(ltx2_runtime: Any)` — [`L491`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/patches.py#L491) — documented in [omni-diffusion-support](../../../../concepts/omni-diffusion-support.md)
- <a id="apply_omni_model_specific_patches"></a>`apply_omni_model_specific_patches()` — [`L74`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/patches.py#L74) — Apply model-specific runtime patches. — documented in [omni-diffusion-support](../../../../concepts/omni-diffusion-support.md)
- <a id="apply_omni_tpu_patches"></a>`apply_omni_tpu_patches()` — [`L45`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/patches.py#L45) — Extend the async output timeout for TPU compilation and execution.

## Module values
- <a id="_BWE_FILTER_CPU_RESTORE_PATCHED"></a>`_BWE_FILTER_CPU_RESTORE_PATCHED` — [`L488`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/patches.py#L488)
- <a id="_D2H_STREAM_PATCHED"></a>`_D2H_STREAM_PATCHED` — [`L209`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/patches.py#L209)
- <a id="_FRESH_TIMESTEP_PATCHED"></a>`_FRESH_TIMESTEP_PATCHED` — [`L377`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/patches.py#L377)
- <a id="_SDPA_FALLBACK_PATCHED"></a>`_SDPA_FALLBACK_PATCHED` — [`L402`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/patches.py#L402)
- <a id="_SPLIT_ROPE_PATCHED"></a>`_SPLIT_ROPE_PATCHED` — [`L530`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/patches.py#L530)
- <a id="_VOCODER_CPU_INIT_PATCHED"></a>`_VOCODER_CPU_INIT_PATCHED` — [`L435`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/patches.py#L435)
- <a id="logger"></a>`logger` — [`L32`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/patches.py#L32)

