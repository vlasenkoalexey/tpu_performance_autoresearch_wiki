---
title: 'Module: torchtitan/experiments/tpu/loss.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/loss.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.loss`/
symbols:
  build_cross_entropy_loss: build_cross_entropy_loss().
  _legacy_pallas_loss_config: _legacy_pallas_loss_config().
  PallasCrossEntropyLoss: PallasCrossEntropyLoss#
  PallasCrossEntropyLoss.__init__: PallasCrossEntropyLoss#__init__().
  PallasCrossEntropyLoss.Config: PallasCrossEntropyLoss#Config#
  pallas_cross_entropy_loss: pallas_cross_entropy_loss().
  PallasCrossEntropyLoss.Config.soft_cap: PallasCrossEntropyLoss#Config#soft_cap.
  PallasCrossEntropyLoss.Config.output_multiplier: PallasCrossEntropyLoss#Config#output_multiplier.
  PallasCrossEntropyLoss.output_multiplier: PallasCrossEntropyLoss#output_multiplier.
  PallasCrossEntropyLoss.Config.b_block_size: PallasCrossEntropyLoss#Config#b_block_size.
  PallasCrossEntropyLoss.Config.h_block_size: PallasCrossEntropyLoss#Config#h_block_size.
  PallasCrossEntropyLoss.Config.v_block_size: PallasCrossEntropyLoss#Config#v_block_size.
  PallasCrossEntropyLoss.Config.implementation: PallasCrossEntropyLoss#Config#implementation.
  PallasCrossEntropyLoss.implementation: PallasCrossEntropyLoss#implementation.
  PallasCrossEntropyLoss.b_block_size: PallasCrossEntropyLoss#b_block_size.
  PallasCrossEntropyLoss.h_block_size: PallasCrossEntropyLoss#h_block_size.
  PallasCrossEntropyLoss.v_block_size: PallasCrossEntropyLoss#v_block_size.
  PallasCrossEntropyLoss.soft_cap: PallasCrossEntropyLoss#soft_cap.
---
# Module: [`torchtitan/experiments/tpu/loss.py`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/loss.py)

## Classes
### <a id="PallasCrossEntropyLoss"></a>`PallasCrossEntropyLoss`  ·  implements/extends BaseLoss
- def: [`torchtitan/experiments/tpu/loss.py:106`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/loss.py#L106)
- doc: Expose fused linear cross entropy through TorchTitan's loss protocol.
- signature: `class PallasCrossEntropyLoss(components_loss.BaseLoss):`
- members:
  - <a id="PallasCrossEntropyLoss.b_block_size"></a>`b_block_size` — [`L156`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/loss.py#L156)
  - <a id="PallasCrossEntropyLoss.h_block_size"></a>`h_block_size` — [`L157`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/loss.py#L157)
  - <a id="PallasCrossEntropyLoss.implementation"></a>`implementation` — [`L155`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/loss.py#L155)
  - <a id="PallasCrossEntropyLoss.output_multiplier"></a>`output_multiplier` — [`L160`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/loss.py#L160)
  - <a id="PallasCrossEntropyLoss.soft_cap"></a>`soft_cap` — [`L159`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/loss.py#L159)
  - <a id="PallasCrossEntropyLoss.v_block_size"></a>`v_block_size` — [`L158`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/loss.py#L158)
- protocol/private: <a id="PallasCrossEntropyLoss.__init__"></a>`__init__`[`L139`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/loss.py#L139)
- uses (calls/refs, reference-scoped): [`CompileConfig`](../../config/configs.md#CompileConfig), [`BaseLoss`](../../components/loss.md#BaseLoss), [`Config`](loss.md#PallasCrossEntropyLoss.Config), [`_maybe_compile`](../../components/loss.md#BaseLoss._maybe_compile), [`pallas_cross_entropy_loss`](loss.md#pallas_cross_entropy_loss), [`fn`](../../components/loss.md#BaseLoss.fn), [`soft_cap`](loss.md#PallasCrossEntropyLoss.Config.soft_cap), [`output_multiplier`](loss.md#PallasCrossEntropyLoss.Config.output_multiplier), [`b_block_size`](loss.md#PallasCrossEntropyLoss.Config.b_block_size), [`h_block_size`](loss.md#PallasCrossEntropyLoss.Config.h_block_size), [`v_block_size`](loss.md#PallasCrossEntropyLoss.Config.v_block_size), [`implementation`](loss.md#PallasCrossEntropyLoss.Config.implementation)
- used by: [`BaseLoss`](../../components/loss.md#BaseLoss), [`build_cross_entropy_loss`](loss.md#build_cross_entropy_loss), [`_legacy_pallas_loss_config`](loss.md#_legacy_pallas_loss_config), [`_enable_pallas_cross_entropy`](muse_glimmer/config_registry.md#_enable_pallas_cross_entropy), [`_enable_pallas_cross_entropy`](llama3/config_registry.md#_enable_pallas_cross_entropy), [`_enable_pallas_cross_entropy`](qwen3/config_registry.md#_enable_pallas_cross_entropy), [`_fused_ce_loss`](transformers_modeling_backend/config_registry.md#_fused_ce_loss), [`_mirror_logit_transform_into_fused_loss`](transformers_modeling_backend/model.md#TPUHFTransformerModel.Config._mirror_logit_transform_into_fused_loss)  (7 test-only)

### <a id="PallasCrossEntropyLoss.Config"></a>`PallasCrossEntropyLoss.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/tpu/loss.py:123`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/loss.py#L123)
- signature: `class Config(components_loss.BaseLoss.Config):`
- members:
  - <a id="PallasCrossEntropyLoss.Config.b_block_size"></a>`b_block_size` — [`L125`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/loss.py#L125)
  - <a id="PallasCrossEntropyLoss.Config.h_block_size"></a>`h_block_size` — [`L126`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/loss.py#L126)
  - <a id="PallasCrossEntropyLoss.Config.implementation"></a>`implementation` — [`L124`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/loss.py#L124)
  - <a id="PallasCrossEntropyLoss.Config.output_multiplier"></a>`output_multiplier` — [`L133`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/loss.py#L133) — ---
  - <a id="PallasCrossEntropyLoss.Config.soft_cap"></a>`soft_cap` — [`L128`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/loss.py#L128) — ---
  - <a id="PallasCrossEntropyLoss.Config.v_block_size"></a>`v_block_size` — [`L127`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/loss.py#L127)
- uses (calls/refs, reference-scoped): [`BaseLoss`](../../components/loss.md#BaseLoss), [`Config`](../../components/loss.md#BaseLoss.Config)
- used by: [`build_cross_entropy_loss`](loss.md#build_cross_entropy_loss), [`_legacy_pallas_loss_config`](loss.md#_legacy_pallas_loss_config), [`_enable_pallas_cross_entropy`](muse_glimmer/config_registry.md#_enable_pallas_cross_entropy), [`__init__`](loss.md#PallasCrossEntropyLoss.__init__), [`_enable_pallas_cross_entropy`](llama3/config_registry.md#_enable_pallas_cross_entropy), [`_enable_pallas_cross_entropy`](qwen3/config_registry.md#_enable_pallas_cross_entropy), [`_fused_ce_loss`](transformers_modeling_backend/config_registry.md#_fused_ce_loss), [`_mirror_logit_transform_into_fused_loss`](transformers_modeling_backend/model.md#TPUHFTransformerModel.Config._mirror_logit_transform_into_fused_loss), [`output_multiplier`](loss.md#PallasCrossEntropyLoss.output_multiplier), [`b_block_size`](loss.md#PallasCrossEntropyLoss.b_block_size), [`h_block_size`](loss.md#PallasCrossEntropyLoss.h_block_size), [`implementation`](loss.md#PallasCrossEntropyLoss.implementation), [`soft_cap`](loss.md#PallasCrossEntropyLoss.soft_cap), [`v_block_size`](loss.md#PallasCrossEntropyLoss.v_block_size)  (6 test-only)

## Functions
- <a id="_legacy_pallas_loss_config"></a>`_legacy_pallas_loss_config(job_config: tpu_job_config_module.TPUTrainerConfig)` — [`L164`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/loss.py#L164)
- <a id="build_cross_entropy_loss"></a>`build_cross_entropy_loss(job_config: (torchtitan.trainer.Trainer.Config | tpu_job_config_module.TPUTrainerConfig), **kwargs)` — [`L178`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/loss.py#L178) — Build explicit loss config, with legacy TPU recipe compatibility.
- <a id="pallas_cross_entropy_loss"></a>`pallas_cross_entropy_loss(pred: tuple[torch.Tensor, torch.Tensor], labels: torch.Tensor, *, implementation: Literal["mosaic_tpu", "xla"] = "mosaic_tpu", b_block_size: int = 1024, h_block_size: int = 512, v_block_size: int = 2048, soft_cap: float | None = None, output_multiplier: float = 1)` — [`L21`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/loss.py#L21) — Compute sum-reduced linear cross entropy without materializing logits.

