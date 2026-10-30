---
title: 'Module: torchtitan/experiments/tpu/transformers_modeling_backend/config_registry.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/transformers_modeling_backend/config_registry.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.transformers_modeling_backend.config_registry`/
symbols:
  _tpu_hf_config: _tpu_hf_config().
  _TPU_FLAVORS: _TPU_FLAVORS.
  as_cpu_reference: as_cpu_reference().
  _c4_test_loader: _c4_test_loader().
  _model_registry: _model_registry().
  _fused_ce_loss: _fused_ce_loss().
  _training_config: _training_config().
  _DEFAULT_HF_MODEL: _DEFAULT_HF_MODEL.
  hf_debugmodel: hf_debugmodel().
  hf_debugmodel_max: hf_debugmodel_max().
  hf_debugmodel_kernels_sdpa: hf_debugmodel_kernels_sdpa().
  hf_debugmodel_kernels_splash: hf_debugmodel_kernels_splash().
  hf_full_max: hf_full_max().
  hf_full_max_plain_ce: hf_full_max_plain_ce().
  hf_moe_auto: hf_moe_auto().
  hf_moe_auto_eager: hf_moe_auto_eager().
  hf_moe_auto_compile: hf_moe_auto_compile().
  _set_attn_implementation: _set_attn_implementation().
  _set_attn_mask_type: _set_attn_mask_type().
  _is_hf_moe: _is_hf_moe().
---
# Module: [`torchtitan/experiments/tpu/transformers_modeling_backend/config_registry.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/config_registry.py)

## Functions
- <a id="_c4_test_loader"></a>`_c4_test_loader()` — [`L174`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/config_registry.py#L174) — This base replaced the HF text dataloader with Grain (upstream #4088).
- <a id="_fused_ce_loss"></a>`_fused_ce_loss()` — [`L86`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/config_registry.py#L86) — The fused-CE loss config with this lane's tuned Mosaic tiles.
- <a id="_is_hf_moe"></a>`_is_hf_moe(hf_model: str)` — [`L110`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/config_registry.py#L110) — True when the HF config declares routed experts.
- <a id="_model_registry"></a>`_model_registry(flavor: str, *, seq_len: int)` — [`L77`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/config_registry.py#L77) — The backend's model_registry, extended with this lane's own flavors.
- <a id="_set_attn_implementation"></a>`_set_attn_implementation(model_config, attn: str)` — [`L142`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/config_registry.py#L142) — Point HF at an attention implementation this lane can actually run.
- <a id="_set_attn_mask_type"></a>`_set_attn_mask_type(model_config, mask_type: str)` — [`L158`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/config_registry.py#L158) — Select causal vs document-causal masking for the packed token stream.
- <a id="_tpu_hf_config"></a>`_tpu_hf_config(flavor: str, hf_model: str, *, local_batch_size: int = 1, seq_len: int = 2048, steps: int = 10, compile: bool = False, attn: str = "sdpa", fused_loss: bool = False, attn_mask_type: str = "block_causal", save_attention: bool = False, use_pallas_grouped_mm: bool = False)` — [`L182`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/config_registry.py#L182) — Build a TPU job config around one of the backend's model flavors. — documented in [tpu-layer-loop-remat-and-layouts](../../../../../concepts/tpu-layer-loop-remat-and-layouts.md)
- <a id="_training_config"></a>`_training_config(*, local_batch_size: int, seq_len: int, steps: int)` — [`L134`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/config_registry.py#L134) — Express the (local_batch_size, seq_len) recipe in the token budget.
- <a id="as_cpu_reference"></a>`as_cpu_reference(config: TPUTransformersBackendConfig)` — [`L350`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/config_registry.py#L350) — The single-device CPU counterpart of a lane config, for parity tests.
- <a id="hf_debugmodel"></a>`hf_debugmodel()` — [`L273`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/config_registry.py#L273) — Two-layer, narrow model -- the smoke test for the TPU path.
- <a id="hf_debugmodel_kernels_sdpa"></a>`hf_debugmodel_kernels_sdpa()` — [`L289`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/config_registry.py#L289) — The kernel-shaped debug model on the portable path (sdpa, plain CE,
- <a id="hf_debugmodel_kernels_splash"></a>`hf_debugmodel_kernels_splash()` — [`L295`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/config_registry.py#L295) — The kernel-shaped debug model with splash attention and plain CE.
- <a id="hf_debugmodel_max"></a>`hf_debugmodel_max()` — [`L278`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/config_registry.py#L278) — ``hf_full_max``'s feature set on the two-layer kernel-shaped debug model.
- <a id="hf_full_max"></a>`hf_full_max()` — [`L301`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/config_registry.py#L301) — The lane's config: splash attention, fused CE, per-layer compile.
- <a id="hf_full_max_plain_ce"></a>`hf_full_max_plain_ce()` — [`L315`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/config_registry.py#L315) — ``hf_full_max`` with the model's own head and plain cross entropy.
- <a id="hf_moe_auto"></a>`hf_moe_auto()` — [`L321`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/config_registry.py#L321) — A MoE checkpoint, built at its own architecture, on TPU grouped experts.
- <a id="hf_moe_auto_compile"></a>`hf_moe_auto_compile()` — [`L344`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/config_registry.py#L344) — hf_moe_auto without use_pallas_grouped_mm (compile only; A/B reference).
- <a id="hf_moe_auto_eager"></a>`hf_moe_auto_eager()` — [`L339`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/config_registry.py#L339) — hf_moe_auto without compile or use_pallas_grouped_mm (debugging baseline).

## Module values
- <a id="_DEFAULT_HF_MODEL"></a>`_DEFAULT_HF_MODEL` — [`L107`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/config_registry.py#L107)
- <a id="_TPU_FLAVORS"></a>`_TPU_FLAVORS` — [`L62`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/config_registry.py#L62)

