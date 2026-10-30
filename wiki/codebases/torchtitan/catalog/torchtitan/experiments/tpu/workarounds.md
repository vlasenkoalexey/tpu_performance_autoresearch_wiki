---
title: 'Module: torchtitan/experiments/tpu/workarounds.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/workarounds.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.workarounds`/
symbols:
  use_tokamax_splash_attention_patch: use_tokamax_splash_attention_patch().
  apply_patches: apply_patches().
  use_splash_attention_patch: use_splash_attention_patch().
  use_cpu_safe_histc_patch: use_cpu_safe_histc_patch().
  use_output_projection_patch: use_output_projection_patch().
  use_tokamax_splash_attention_patch._splash_forward: use_tokamax_splash_attention_patch()._splash_forward().
  use_tokamax_splash_attention_patch._sa: use_tokamax_splash_attention_patch()._sa().
  use_gmm_kernel_patch: use_gmm_kernel_patch().
  PallasLossLinear: PallasLossLinear#
  disable_pinned_host_memory: disable_pinned_host_memory().
  PallasLossLinear.__init__: PallasLossLinear#__init__().
  extract_splash_kwargs: extract_splash_kwargs().
  use_tokamax_splash_attention_patch._splash_sdpa_native: use_tokamax_splash_attention_patch()._splash_sdpa_native().
  _check_fused_loss_logit_transform: _check_fused_loss_logit_transform().
  use_splash_attention_patch._splash_sdpa_native: use_splash_attention_patch()._splash_sdpa_native().
  PallasLossLinear._restore_infix: PallasLossLinear#_restore_infix().
  PallasLossLinear.weight: PallasLossLinear#weight().
  use_gmm_kernel_patch._custom_run_experts_grouped_mm: use_gmm_kernel_patch()._custom_run_experts_grouped_mm().
  use_gmm_kernel_patch.bypassed_padding_wrapper: use_gmm_kernel_patch().bypassed_padding_wrapper().
  use_splash_attention_patch._splash_forward: use_splash_attention_patch()._splash_forward().
  PallasLossLinear.forward: PallasLossLinear#forward().
  SPLASH_KEYS: SPLASH_KEYS.
  use_tokamax_splash_attention_patch._filter_splash_kwargs: use_tokamax_splash_attention_patch()._filter_splash_kwargs().
  PallasLossLinear._INFIX: PallasLossLinear#_INFIX.
  raise_dynamo_recompile_limits: raise_dynamo_recompile_limits().
  PallasLossLinear.original_linear: PallasLossLinear#original_linear.
  PallasLossLinear._strip_infix: PallasLossLinear#_strip_infix().
  _check_lm_head_is_plain_projection: _check_lm_head_is_plain_projection().
  use_fill_indices_patch: use_fill_indices_patch().
  use_cpu_safe_histc_patch._cpu_safe_histc: use_cpu_safe_histc_patch()._cpu_safe_histc().
  use_tokamax_splash_attention_patch._get_kwargs: use_tokamax_splash_attention_patch()._get_kwargs().
---
# Module: [`torchtitan/experiments/tpu/workarounds.py`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/workarounds.py)

## Classes
### <a id="PallasLossLinear"></a>`PallasLossLinear`
- def: [`torchtitan/experiments/tpu/workarounds.py:460`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/workarounds.py#L460) — documented in [tpu-trainer-and-job-config](../../../../concepts/tpu-trainer-and-job-config.md)
- doc: Wrapper for model.output to return (x, weight) for Pallas loss.
- signature: `class PallasLossLinear(nn.Module):`
- members:
  - <a id="PallasLossLinear._restore_infix"></a>`_restore_infix(self, state_dict, prefix, *args, **kwargs)` — [`L486`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/workarounds.py#L486) — Rename ``<prefix>X`` -> ``<prefix>original_linear.X`` on the way in.
  - <a id="PallasLossLinear._strip_infix"></a>`_strip_infix(module, state_dict, prefix, local_metadata)` — [`L480`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/workarounds.py#L480) — Rename ``<prefix>original_linear.X`` -> ``<prefix>X`` on the way out.
  - <a id="PallasLossLinear.forward"></a>`forward(self, x: torch.Tensor)` — [`L501`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/workarounds.py#L501)
  - <a id="PallasLossLinear.weight"></a>`weight(self)` — [`L496`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/workarounds.py#L496)
  - <a id="PallasLossLinear.original_linear"></a>`original_linear` — [`L475`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/workarounds.py#L475)
- protocol/private: <a id="PallasLossLinear._INFIX"></a>`_INFIX`[`L471`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/workarounds.py#L471), <a id="PallasLossLinear.__init__"></a>`__init__`[`L473`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/workarounds.py#L473)
- used by: [`use_output_projection_patch`](workarounds.md#use_output_projection_patch)  (4 test-only)

## Functions
- <a id="_check_fused_loss_logit_transform"></a>`_check_fused_loss_logit_transform(model: nn.Module, job_config: Any)` — [`L637`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/workarounds.py#L637) — Raises if the fused loss would apply a different logit transform.
- <a id="_check_lm_head_is_plain_projection"></a>`_check_lm_head_is_plain_projection(lm_head: nn.Linear)` — [`L505`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/workarounds.py#L505) — Raises if the fused loss would skip work done in ``lm_head.forward``.
- <a id="use_cpu_safe_histc_patch._cpu_safe_histc"></a>`_cpu_safe_histc(input, bins=100, min=0, max=0, *, out=None)` — [`L628`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/workarounds.py#L628)
- <a id="use_gmm_kernel_patch._custom_run_experts_grouped_mm"></a>`_custom_run_experts_grouped_mm(w1: torch.Tensor, w2: torch.Tensor, w3: torch.Tensor, x: torch.Tensor, num_tokens_per_expert: torch.Tensor)` — [`L572`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/workarounds.py#L572)
- <a id="use_tokamax_splash_attention_patch._filter_splash_kwargs"></a>`_filter_splash_kwargs(kwargs_dict)` — [`L303`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/workarounds.py#L303)
- <a id="use_tokamax_splash_attention_patch._get_kwargs"></a>`_get_kwargs(**kwargs)` — [`L291`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/workarounds.py#L291)
- <a id="use_tokamax_splash_attention_patch._sa"></a>`_sa(name)` — [`L248`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/workarounds.py#L248)
- <a id="use_splash_attention_patch._splash_forward"></a>`_splash_forward(self, q, k, v, *, scale=None, enable_gqa=False, is_causal=True, **extra_args)` — [`L41`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/workarounds.py#L41) — Replace ScaledDotProductAttention.forward with splash_sdpa.
- <a id="use_tokamax_splash_attention_patch._splash_forward"></a>`_splash_forward(self, q, k, v, *, scale=None, enable_gqa=False, is_causal=True, **extra_args)` — [`L319`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/workarounds.py#L319)
- <a id="use_splash_attention_patch._splash_sdpa_native"></a>`_splash_sdpa_native(self, *, query, key, value, scale=None, **kwargs)` — [`L89`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/workarounds.py#L89) — Replaces a module's ``_sdpa_native_torch`` method with splash_sdpa.
- <a id="use_tokamax_splash_attention_patch._splash_sdpa_native"></a>`_splash_sdpa_native(self, *, query, key, value, scale=None, **kwargs)` — [`L384`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/workarounds.py#L384)
- <a id="apply_patches"></a>`apply_patches(model: nn.Module, job_config: Any)` — [`L714`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/workarounds.py#L714) — Applies all TPU-specific patches and workarounds to the model. — documented in [tpu-trainer-and-job-config](../../../../concepts/tpu-trainer-and-job-config.md)
- <a id="use_gmm_kernel_patch.bypassed_padding_wrapper"></a>`bypassed_padding_wrapper(fn)` — [`L595`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/workarounds.py#L595)
- <a id="disable_pinned_host_memory"></a>`disable_pinned_host_memory()` — [`L685`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/workarounds.py#L685) — Makes the data pipeline allocate pageable batches instead of pinned ones.
- <a id="extract_splash_kwargs"></a>`extract_splash_kwargs(sa_config: Any)` — [`L21`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/workarounds.py#L21) — Safe prefix-mapping helper to map sa_config attributes to standard names.
- <a id="raise_dynamo_recompile_limits"></a>`raise_dynamo_recompile_limits(model_config)` — [`L760`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/workarounds.py#L760) — Size Dynamo's recompile limits for per-layer compile under SimpleFSDP.
- <a id="use_cpu_safe_histc_patch"></a>`use_cpu_safe_histc_patch()` — [`L624`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/workarounds.py#L624) — Monkey patches torch.histc to support int dtypes on CPU.
- <a id="use_fill_indices_patch"></a>`use_fill_indices_patch(model: nn.Module)` — [`L605`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/workarounds.py#L605) — Enables the fill indices kernel for MoE modules in the model.
- <a id="use_gmm_kernel_patch"></a>`use_gmm_kernel_patch(model: nn.Module)` — [`L554`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/workarounds.py#L554) — Enables the GMM kernel for GroupedExperts modules in the model. — documented in [tpu-trainer-and-job-config](../../../../concepts/tpu-trainer-and-job-config.md)
- <a id="use_output_projection_patch"></a>`use_output_projection_patch(model: nn.Module)` — [`L532`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/workarounds.py#L532) — Replaces model.output with an identity-like module that returns (x, weight).
- <a id="use_splash_attention_patch"></a>`use_splash_attention_patch(model: nn.Module, sa_config: Any = None)` — [`L33`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/workarounds.py#L33) — Patches splash attention into the model. — documented in [tpu-pallas-kernels](../../../../concepts/tpu-pallas-kernels.md)
- <a id="use_tokamax_splash_attention_patch"></a>`use_tokamax_splash_attention_patch(model: nn.Module, sa_config: Any)` — [`L234`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/workarounds.py#L234) — Patches zero-overhead Tokamax layout-fused splash attention into the model. — documented in [tpu-pallas-kernels](../../../../concepts/tpu-pallas-kernels.md)

## Module values
- <a id="SPLASH_KEYS"></a>`SPLASH_KEYS` — [`L12`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/workarounds.py#L12)

