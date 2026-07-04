---
title: 'Module: easydel/modules/_base/image_classification_module.py'
type: catalog
provenance: extracted
module: easydel/modules/_base/image_classification_module.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules._base.image_classification_module`/BaseImageClassificationModule#
symbols:
  BaseImageClassificationModule.__init__: __init__().
  BaseImageClassificationModule: ''
  BaseImageClassificationModule.classifier: classifier.
  BaseImageClassificationModule.__call__: __call__().
  BaseImageClassificationModule.get_task_head: get_task_head().
  BaseImageClassificationModule.get_encoder: get_encoder().
  BaseImageClassificationModule.get_lm_head: get_lm_head().
  BaseImageClassificationModule.get_decoder: get_decoder().
---
# Module: [`easydel/modules/_base/image_classification_module.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/image_classification_module.py)

## Classes
### `BaseImageClassificationModule`  ·  implements/extends BaseTaskModule
- def: [`easydel/modules/_base/image_classification_module.py:74`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/image_classification_module.py#L74)
- doc: Generic base class for Image Classification.
- signature: `class BaseImageClassificationModule(BaseTaskModule[ModelT, ConfigT]):`
- members:
  - `__call__(self, pixel_values: Float[Array, "batch channels height width"], output_attentions: bool | None = None, output_hidden_states: bool | None = None)` — [`L232`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/image_classification_module.py#L232) — Forward pass for image classification.
  - `__init__(self, config: ConfigT, base_model: ModelT | None = None, base_model_class: type[ModelT] | None = None, base_model_name: str = "vision_model", dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs, pooling_strategy: str = "first", classifier_bias: bool = True, classifier_kernel_init: Callable | None = None)` — [`L122`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/image_classification_module.py#L122) — Initialize the Image Classification module.
  - `get_decoder(self)` — [`L328`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/image_classification_module.py#L328) — Raise NotImplementedError for image classification models.
  - `get_encoder(self)` — [`L317`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/image_classification_module.py#L317) — Return the vision encoder.
  - `get_lm_head(self)` — [`L306`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/image_classification_module.py#L306) — Raise NotImplementedError for image classification models.
  - `get_task_head(self)` — [`L297`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/image_classification_module.py#L297) — Return the classification head.
  - `classifier` — [`L219`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/image_classification_module.py#L219)
- uses (calls/refs, reference-scoped): [`ColumnParallelLinear`](../../layers/linears/_linear.md#ColumnParallelLinear), [`auto_remat`](../../infra/utils.md#auto_remat), [`base_model`](_base_task_module.md#BaseTaskModule.base_model), [`BaseTaskModule`](_base_task_module.md#BaseTaskModule), [`ModelT`](_base_task_module.md#ModelT), [`ConfigT`](_base_task_module.md#ConfigT), [`CLIPForImageClassification`](../clip/modeling_clip.md#CLIPForImageClassification), [`SiglipForImageClassification`](../siglip/modeling_siglip.md#SiglipForImageClassification), [`__init__`](_base_task_module.md#BaseTaskModule.__init__), [`ImageClassifierOutput`](../../infra/modeling_outputs.md#ImageClassifierOutput), [`_gradient_checkpointing_feature`](_base_task_module.md#BaseTaskModule._gradient_checkpointing_feature), [`get_config`](_features.md#GradientCheckpointingFeature.get_config), [`should_checkpoint`](_features.md#GradientCheckpointingFeature.should_checkpoint), [`pool_sequence`](_base_task_module.md#BaseTaskModule.pool_sequence), [`_head_bias`](_base_task_module.md#BaseTaskModule._head_bias), [`_head_kernel_init`](_base_task_module.md#BaseTaskModule._head_kernel_init), [`get_task_head`](../clip/modeling_clip.md#CLIPForImageClassification.get_task_head), [`get_task_head`](../siglip/modeling_siglip.md#SiglipForImageClassification.get_task_head), [`get_decoder`](../clip/modeling_clip.md#CLIPForImageClassification.get_decoder), [`get_decoder`](../siglip/modeling_siglip.md#SiglipForImageClassification.get_decoder), [`get_encoder`](../clip/modeling_clip.md#CLIPForImageClassification.get_encoder), [`get_encoder`](../siglip/modeling_siglip.md#SiglipForImageClassification.get_encoder), [`get_lm_head`](../clip/modeling_clip.md#CLIPForImageClassification.get_lm_head), [`get_lm_head`](../siglip/modeling_siglip.md#SiglipForImageClassification.get_lm_head)
- used by: [`get_lm_head`](../../infra/base_module.md#EasyDeLBaseModule.get_lm_head), [`get_decoder`](_base_task_module.md#BaseTaskModule.get_decoder), [`get_encoder`](_base_task_module.md#BaseTaskModule.get_encoder), [`BaseTaskModule`](_base_task_module.md#BaseTaskModule), [`get_task_head`](_base_task_module.md#BaseTaskModule.get_task_head), [`CLIPForImageClassification`](../clip/modeling_clip.md#CLIPForImageClassification), [`SiglipForImageClassification`](../siglip/modeling_siglip.md#SiglipForImageClassification), [`create_image_classification_class`](_auto_mapper.md#create_image_classification_class), [`__call__`](../clip/modeling_clip.md#CLIPForImageClassification.__call__), [`__call__`](../siglip/modeling_siglip.md#SiglipForImageClassification.__call__), [`__init__`](../siglip/modeling_siglip.md#SiglipForImageClassification.__init__), [`__init__`](../clip/modeling_clip.md#CLIPForImageClassification.__init__), [`get_task_head`](../clip/modeling_clip.md#CLIPForImageClassification.get_task_head), [`get_task_head`](../siglip/modeling_siglip.md#SiglipForImageClassification.get_task_head), [`use_classif`](../siglip/modeling_siglip.md#SiglipForImageClassification.use_classif)

