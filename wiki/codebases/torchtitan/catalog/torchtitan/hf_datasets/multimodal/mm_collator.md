---
title: 'Module: torchtitan/hf_datasets/multimodal/mm_collator.py'
type: catalog
provenance: extracted
module: torchtitan/hf_datasets/multimodal/mm_collator.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.hf_datasets.multimodal.mm_collator`/MultiModalCollator#
symbols:
  MultiModalCollator.__call__: __call__().
  MultiModalCollator: ''
  MultiModalCollator.Config: Config#
  MultiModalCollator.collate_images: collate_images().
  MultiModalCollator.collate_text: collate_text().
  MultiModalCollator.tokenizer: tokenizer.
  MultiModalCollator.Config.build_mrope_positions: Config#build_mrope_positions.
  MultiModalCollator._build_mrope_positions: _build_mrope_positions().
  MultiModalCollator.temporal_patch_size: temporal_patch_size.
  MultiModalCollator.patch_order: patch_order.
  MultiModalCollator.__init__: __init__().
  MultiModalCollator.max_images_per_batch: max_images_per_batch.
  MultiModalCollator.spatial_merge_size: spatial_merge_size.
  MultiModalCollator.Config.patch_size: Config#patch_size.
  MultiModalCollator.Config.temporal_patch_size: Config#temporal_patch_size.
  MultiModalCollator.Config.spatial_merge_size: Config#spatial_merge_size.
  MultiModalCollator.Config.patch_order: Config#patch_order.
  MultiModalCollator._num_tokens_per_batch: _num_tokens_per_batch.
  MultiModalCollator._max_context_length: _max_context_length.
  MultiModalCollator.patch_size: patch_size.
  MultiModalCollator.build_mrope_positions: build_mrope_positions.
  MultiModalCollator.Config.max_images_per_batch: Config#max_images_per_batch.
---
# Module: [`torchtitan/hf_datasets/multimodal/mm_collator.py`](../../../../../../../raw/code/torchtitan/torchtitan/hf_datasets/multimodal/mm_collator.py)

## Classes
### <a id="MultiModalCollator"></a>`MultiModalCollator`  ·  implements/extends Collator
- def: [`torchtitan/hf_datasets/multimodal/mm_collator.py:22`](../../../../../../../raw/code/torchtitan/torchtitan/hf_datasets/multimodal/mm_collator.py#L22) — documented in [hf-datasets](../../../../concepts/hf-datasets.md)
- doc: Multimodal collator for VLM training.
- signature: `class MultiModalCollator(Collator):`
- members:
  - <a id="MultiModalCollator.__call__"></a>`__call__(self, batch: Sequence[dict[str, Any]])` — [`L290`](../../../../../../../raw/code/torchtitan/torchtitan/hf_datasets/multimodal/mm_collator.py#L290) — Collate batch with patch-based approach. — documented in [hf-datasets](../../../../concepts/hf-datasets.md)
  - <a id="MultiModalCollator._build_mrope_positions"></a>`_build_mrope_positions(self, tokens: torch.Tensor, grid_thw: torch.Tensor | None, grid_thw_videos: torch.Tensor | None, positions: torch.Tensor | None, *, image_token_id: int, video_token_id: int)` — [`L120`](../../../../../../../raw/code/torchtitan/torchtitan/hf_datasets/multimodal/mm_collator.py#L120) — Build 3D (temporal, height, width) MRoPE position IDs per token. — documented in [hf-datasets](../../../../concepts/hf-datasets.md)
  - <a id="MultiModalCollator.collate_images"></a>`collate_images(self, all_images: list[torch.Tensor])` — [`L49`](../../../../../../../raw/code/torchtitan/torchtitan/hf_datasets/multimodal/mm_collator.py#L49) — Process image/video tensors into packed patches and grid dimensions. — documented in [hf-datasets](../../../../concepts/hf-datasets.md)
  - <a id="MultiModalCollator.collate_text"></a>`collate_text(self, batch: list[dict[str, Any]])` — [`L81`](../../../../../../../raw/code/torchtitan/torchtitan/hf_datasets/multimodal/mm_collator.py#L81) — Concatenate whole samples and pad only the token-batch tail. — documented in [hf-datasets](../../../../concepts/hf-datasets.md)
  - <a id="MultiModalCollator.build_mrope_positions"></a>`build_mrope_positions` — [`L46`](../../../../../../../raw/code/torchtitan/torchtitan/hf_datasets/multimodal/mm_collator.py#L46)
  - <a id="MultiModalCollator.max_images_per_batch"></a>`max_images_per_batch` — [`L41`](../../../../../../../raw/code/torchtitan/torchtitan/hf_datasets/multimodal/mm_collator.py#L41) — documented in [hf-datasets](../../../../concepts/hf-datasets.md)
  - <a id="MultiModalCollator.patch_order"></a>`patch_order` — [`L47`](../../../../../../../raw/code/torchtitan/torchtitan/hf_datasets/multimodal/mm_collator.py#L47) — documented in [hf-datasets](../../../../concepts/hf-datasets.md)
  - <a id="MultiModalCollator.patch_size"></a>`patch_size` — [`L42`](../../../../../../../raw/code/torchtitan/torchtitan/hf_datasets/multimodal/mm_collator.py#L42)
  - <a id="MultiModalCollator.spatial_merge_size"></a>`spatial_merge_size` — [`L44`](../../../../../../../raw/code/torchtitan/torchtitan/hf_datasets/multimodal/mm_collator.py#L44) — documented in [hf-datasets](../../../../concepts/hf-datasets.md)
  - <a id="MultiModalCollator.temporal_patch_size"></a>`temporal_patch_size` — [`L43`](../../../../../../../raw/code/torchtitan/torchtitan/hf_datasets/multimodal/mm_collator.py#L43) — documented in [hf-datasets](../../../../concepts/hf-datasets.md)
  - <a id="MultiModalCollator.tokenizer"></a>`tokenizer` — [`L45`](../../../../../../../raw/code/torchtitan/torchtitan/hf_datasets/multimodal/mm_collator.py#L45) — documented in [hf-datasets](../../../../concepts/hf-datasets.md)
- protocol/private: <a id="MultiModalCollator.__init__"></a>`__init__`[`L38`](../../../../../../../raw/code/torchtitan/torchtitan/hf_datasets/multimodal/mm_collator.py#L38), <a id="MultiModalCollator._max_context_length"></a>`_max_context_length`[`L40`](../../../../../../../raw/code/torchtitan/torchtitan/hf_datasets/multimodal/mm_collator.py#L40), <a id="MultiModalCollator._num_tokens_per_batch"></a>`_num_tokens_per_batch`[`L39`](../../../../../../../raw/code/torchtitan/torchtitan/hf_datasets/multimodal/mm_collator.py#L39)
- uses (calls/refs, reference-scoped): [`IGNORE_INDEX`](../../components/loss.md#IGNORE_INDEX), [`MultiModalTokenizer`](../../components/tokenizer.md#MultiModalTokenizer), [`DatasetBuildContext`](../../components/data/types.md#DatasetBuildContext), [`Collator`](../../components/data/collators.md#Collator), [`TrainerBatch`](../../components/data/collators.md#TrainerBatch.TrainerBatch), [`num_tokens_per_batch`](../../components/data/types.md#DatasetBuildContext.num_tokens_per_batch), [`Config`](mm_collator.md#MultiModalCollator.Config), [`max_context_length`](../../components/data/types.md#DatasetBuildContext.max_context_length), [`tokenizer`](../../components/data/types.md#DatasetBuildContext.tokenizer), [`build_mrope_positions`](mm_collator.md#MultiModalCollator.Config.build_mrope_positions), [`patch_order`](mm_collator.md#MultiModalCollator.Config.patch_order), [`patch_size`](mm_collator.md#MultiModalCollator.Config.patch_size), [`spatial_merge_size`](mm_collator.md#MultiModalCollator.Config.spatial_merge_size), [`temporal_patch_size`](mm_collator.md#MultiModalCollator.Config.temporal_patch_size), [`max_images_per_batch`](mm_collator.md#MultiModalCollator.Config.max_images_per_batch), [`TOKEN_FIELDS`](../../components/tokenizer.md#MultiModalTokenizer.TOKEN_FIELDS), [`vision_to_patches`](utils/image.md#vision_to_patches)
- used by: [`_kimi_multimodal_dataloader`](../../models/kimi_k2_7/config_registry.md#_kimi_multimodal_dataloader), [`_muse_glimmer_mm_dataloader`](../../models/muse_glimmer/config_registry.md#_muse_glimmer_mm_dataloader), [`_kimi_k3_multimodal_dataloader`](../../models/kimi_k3/config_registry.md#_kimi_k3_multimodal_dataloader), [`_multimodal_collator_config`](../../models/qwen3_5/config_registry.md#_multimodal_collator_config), [`_multimodal_collator_config`](../../models/qwen3_6/config_registry.md#_multimodal_collator_config), [`_multimodal_collator_config`](../../models/qwen3_8/config_registry.md#_multimodal_collator_config), [`Collator`](../../components/data/collators.md#Collator)

### <a id="MultiModalCollator.Config"></a>`MultiModalCollator.Config`  ·  implements/extends Config
- def: [`torchtitan/hf_datasets/multimodal/mm_collator.py:30`](../../../../../../../raw/code/torchtitan/torchtitan/hf_datasets/multimodal/mm_collator.py#L30) — documented in [hf-datasets](../../../../concepts/hf-datasets.md)
- signature: `class Config(Collator.Config):`
- members:
  - <a id="MultiModalCollator.Config.build_mrope_positions"></a>`build_mrope_positions` — [`L35`](../../../../../../../raw/code/torchtitan/torchtitan/hf_datasets/multimodal/mm_collator.py#L35) — documented in [hf-datasets](../../../../concepts/hf-datasets.md)
  - <a id="MultiModalCollator.Config.max_images_per_batch"></a>`max_images_per_batch` — [`L31`](../../../../../../../raw/code/torchtitan/torchtitan/hf_datasets/multimodal/mm_collator.py#L31)
  - <a id="MultiModalCollator.Config.patch_order"></a>`patch_order` — [`L36`](../../../../../../../raw/code/torchtitan/torchtitan/hf_datasets/multimodal/mm_collator.py#L36)
  - <a id="MultiModalCollator.Config.patch_size"></a>`patch_size` — [`L32`](../../../../../../../raw/code/torchtitan/torchtitan/hf_datasets/multimodal/mm_collator.py#L32)
  - <a id="MultiModalCollator.Config.spatial_merge_size"></a>`spatial_merge_size` — [`L34`](../../../../../../../raw/code/torchtitan/torchtitan/hf_datasets/multimodal/mm_collator.py#L34)
  - <a id="MultiModalCollator.Config.temporal_patch_size"></a>`temporal_patch_size` — [`L33`](../../../../../../../raw/code/torchtitan/torchtitan/hf_datasets/multimodal/mm_collator.py#L33)
- uses (calls/refs, reference-scoped): [`Collator`](../../components/data/collators.md#Collator), [`Config`](../../components/data/collators.md#Collator.Config)
- used by: [`_kimi_multimodal_dataloader`](../../models/kimi_k2_7/config_registry.md#_kimi_multimodal_dataloader), [`_muse_glimmer_mm_dataloader`](../../models/muse_glimmer/config_registry.md#_muse_glimmer_mm_dataloader), [`_kimi_k3_multimodal_dataloader`](../../models/kimi_k3/config_registry.md#_kimi_k3_multimodal_dataloader), [`_multimodal_collator_config`](../../models/qwen3_5/config_registry.md#_multimodal_collator_config), [`_multimodal_collator_config`](../../models/qwen3_6/config_registry.md#_multimodal_collator_config), [`_multimodal_collator_config`](../../models/qwen3_8/config_registry.md#_multimodal_collator_config), [`patch_order`](mm_collator.md#MultiModalCollator.patch_order), [`temporal_patch_size`](mm_collator.md#MultiModalCollator.temporal_patch_size), [`__init__`](mm_collator.md#MultiModalCollator.__init__), [`max_images_per_batch`](mm_collator.md#MultiModalCollator.max_images_per_batch), [`spatial_merge_size`](mm_collator.md#MultiModalCollator.spatial_merge_size), [`build_mrope_positions`](mm_collator.md#MultiModalCollator.build_mrope_positions), [`patch_size`](mm_collator.md#MultiModalCollator.patch_size)

