---
title: 'Module: torchtitan/components/loss.py'
type: catalog
provenance: extracted
module: torchtitan/components/loss.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.components.loss`/
symbols:
  CrossEntropyLoss: CrossEntropyLoss#
  ChunkedLossWrapper: ChunkedLossWrapper#
  CrossEntropyLoss.Config: CrossEntropyLoss#Config#
  ChunkedLossWrapper.Config: ChunkedLossWrapper#Config#
  ChunkedLossWrapper.Config.loss_fn: ChunkedLossWrapper#Config#loss_fn.
  CrossEntropyLoss.Config.global_vocab_size: CrossEntropyLoss#Config#global_vocab_size.
  BaseLoss: BaseLoss#
  IGNORE_INDEX: IGNORE_INDEX.
  ChunkedLossWrapper.Config.num_chunks: ChunkedLossWrapper#Config#num_chunks.
  ChunkedLossWrapper.__call__: ChunkedLossWrapper#__call__().
  cross_entropy_loss: cross_entropy_loss().
  BaseLoss._maybe_compile: BaseLoss#_maybe_compile().
  BaseLoss.Config: BaseLoss#Config#
  compute_logprobs: compute_logprobs().
  LossFunction.LossFunction: LossFunction.LossFunction.
  GradAccumulator.add: GradAccumulator#add().
  ChunkedLossWrapper.set_lm_head: ChunkedLossWrapper#set_lm_head().
  MSELoss.__init__: MSELoss#__init__().
  CrossEntropyLoss.__call__: CrossEntropyLoss#__call__().
  GradAccumulator._placements: GradAccumulator#_placements.
  BaseLoss.fn: BaseLoss#fn.
  MSELoss.Config: MSELoss#Config#
  CrossEntropyLoss.fn: CrossEntropyLoss#fn.
  GradAccumulator.result: GradAccumulator#result().
  ChunkedLossWrapper.loss_fn: ChunkedLossWrapper#loss_fn.
  BaseLoss.__call__: BaseLoss#__call__().
  MSELoss: MSELoss#
  CrossEntropyLoss.__init__: CrossEntropyLoss#__init__().
  GradAccumulator._buffer: GradAccumulator#_buffer.
  ChunkedLossWrapper._gradient_backprop: ChunkedLossWrapper#_gradient_backprop().
  ChunkedLossWrapper._chunk: ChunkedLossWrapper#_chunk().
  BaseLoss.__init__: BaseLoss#__init__().
  ChunkedLossWrapper.__init__: ChunkedLossWrapper#__init__().
  ChunkedLossWrapper.lm_head: ChunkedLossWrapper#lm_head.
  CrossEntropyLoss.global_vocab_size: CrossEntropyLoss#global_vocab_size.
  ChunkedLossWrapper.num_chunks: ChunkedLossWrapper#num_chunks.
  GradAccumulator._next_idx: GradAccumulator#_next_idx.
  GradAccumulator._device_mesh: GradAccumulator#_device_mesh.
  _LossParallelCrossEntropy.forward: _LossParallelCrossEntropy#forward().
  _LossParallelCrossEntropy.backward: _LossParallelCrossEntropy#backward().
  GradAccumulator.num_chunks: GradAccumulator#num_chunks.
  GradAccumulator.seq_dim: GradAccumulator#seq_dim.
  ChunkedLossWrapper._chunk_local: ChunkedLossWrapper#_chunk_local().
  _LossParallelCrossEntropy: _LossParallelCrossEntropy#
  mse_loss: mse_loss().
  GradAccumulator: GradAccumulator#
  ChunkedLossWrapper._combine_chunk_metrics: ChunkedLossWrapper#_combine_chunk_metrics().
  _DecoderOutputGradientBackProp: _DecoderOutputGradientBackProp#
  _LossParallelCrossEntropy.spmd_typecheck: _LossParallelCrossEntropy#spmd_typecheck().
  MSELoss.fn: MSELoss#fn.
  GradAccumulator.__init__: GradAccumulator#__init__().
  _DecoderOutputGradientBackProp.forward: _DecoderOutputGradientBackProp#forward().
  _DecoderOutputGradientBackProp.backward: _DecoderOutputGradientBackProp#backward().
---
# Module: [`torchtitan/components/loss.py`](../../../../../../raw/code/torchtitan/torchtitan/components/loss.py)

## Classes
### <a id="BaseLoss"></a>`BaseLoss`  ·  implements/extends ABC, Configurable
- def: [`torchtitan/components/loss.py:236`](../../../../../../raw/code/torchtitan/torchtitan/components/loss.py#L236) — documented in [training-components](../../../concepts/training-components.md)
- doc: Abstract base class for all loss functions.
- signature: `class BaseLoss(ABC, Configurable):`
- members:
  - <a id="BaseLoss.__call__"></a>`__call__(self, pred: torch.Tensor, labels: torch.Tensor, global_valid_tokens: torch.Tensor | None = None, **kwargs: Any)` — [`L264`](../../../../../../raw/code/torchtitan/torchtitan/components/loss.py#L264) — Return the scaled loss and any metrics computed by the loss.
  - <a id="BaseLoss.fn"></a>`fn` — [`L245`](../../../../../../raw/code/torchtitan/torchtitan/components/loss.py#L245)
- protocol/private: <a id="BaseLoss.__init__"></a>`__init__`[`L252`](../../../../../../raw/code/torchtitan/torchtitan/components/loss.py#L252), <a id="BaseLoss._maybe_compile"></a>`_maybe_compile`[`L255`](../../../../../../raw/code/torchtitan/torchtitan/components/loss.py#L255)
- uses (calls/refs, reference-scoped): [`logger`](../tools/logging.md#logger), [`Configurable`](../config/configurable.md#Configurable), [`enable`](../config/configs.md#CompileConfig.enable), [`CompileConfig`](../config/configs.md#CompileConfig), [`CrossEntropyLoss`](loss.md#CrossEntropyLoss), [`ChunkedLossWrapper`](loss.md#ChunkedLossWrapper), [`get_spmd_backend`](../distributed/utils.md#get_spmd_backend), [`components`](../config/configs.md#CompileConfig.components), [`backend`](../config/configs.md#CompileConfig.backend), [`PallasCrossEntropyLoss`](../experiments/tpu/loss.md#PallasCrossEntropyLoss), [`current_spmd_mesh`](../distributed/spmd_types.md#current_spmd_mesh), [`Config`](loss.md#BaseLoss.Config), [`DAPOLoss`](../experiments/rl/losses/dapo.md#DAPOLoss), [`LossFunction`](loss.md#LossFunction.LossFunction), [`MSELoss`](loss.md#MSELoss)  (1 test-only)
- used by: [`Configurable`](../config/configurable.md#Configurable), [`CrossEntropyLoss`](loss.md#CrossEntropyLoss), [`ChunkedLossWrapper`](loss.md#ChunkedLossWrapper), [`loss`](../trainer.md#Trainer.Config.loss), [`Config`](loss.md#CrossEntropyLoss.Config), [`Config`](loss.md#ChunkedLossWrapper.Config), [`loss_fn`](loss.md#ChunkedLossWrapper.Config.loss_fn), [`loss`](../experiments/rl/actors/trainer.md#PolicyTrainer.Config.loss), [`PallasCrossEntropyLoss`](../experiments/tpu/loss.md#PallasCrossEntropyLoss), [`__init__`](../experiments/tpu/loss.md#PallasCrossEntropyLoss.__init__), [`loss_fn`](../trainer.md#Trainer.loss_fn), [`Config`](../experiments/tpu/loss.md#PallasCrossEntropyLoss.Config), [`Config`](../experiments/rl/losses/grpo.md#GRPOLoss.Config), [`DAPOLoss`](../experiments/rl/losses/dapo.md#DAPOLoss), [`__init__`](loss.md#MSELoss.__init__), [`Config`](../experiments/rl/losses/dapo.md#DAPOLoss.Config), [`Config`](loss.md#MSELoss.Config), [`fn`](loss.md#CrossEntropyLoss.fn), [`loss_fn`](loss.md#ChunkedLossWrapper.loss_fn), [`MSELoss`](loss.md#MSELoss), [`output_multiplier`](../experiments/tpu/loss.md#PallasCrossEntropyLoss.output_multiplier)  (4 test-only)

### <a id="BaseLoss.Config"></a>`BaseLoss.Config`  ·  implements/extends Config
- def: [`torchtitan/components/loss.py:248`](../../../../../../raw/code/torchtitan/torchtitan/components/loss.py#L248)
- signature: `class Config(Configurable.Config):`
- uses (calls/refs, reference-scoped): [`Configurable`](../config/configurable.md#Configurable), [`Config`](../config/configurable.md#Configurable.Config)
- used by: [`loss`](../trainer.md#Trainer.Config.loss), [`Config`](loss.md#CrossEntropyLoss.Config), [`Config`](loss.md#ChunkedLossWrapper.Config), [`loss_fn`](loss.md#ChunkedLossWrapper.Config.loss_fn), [`loss`](../experiments/rl/actors/trainer.md#PolicyTrainer.Config.loss), [`Config`](../experiments/tpu/loss.md#PallasCrossEntropyLoss.Config), [`Config`](../experiments/rl/losses/grpo.md#GRPOLoss.Config), [`Config`](../experiments/rl/losses/dapo.md#DAPOLoss.Config), [`Config`](loss.md#MSELoss.Config), [`__init__`](loss.md#BaseLoss.__init__)  (1 test-only)

### <a id="ChunkedLossWrapper"></a>`ChunkedLossWrapper`  ·  implements/extends BaseLoss
- def: [`torchtitan/components/loss.py:515`](../../../../../../raw/code/torchtitan/torchtitan/components/loss.py#L515) — documented in [graph-trainer](../../../concepts/graph-trainer.md)
- doc: Chunked loss wrapper that splits the sequence dimension to reduce peak memory.
- signature: `class ChunkedLossWrapper(BaseLoss):`
- members:
  - <a id="ChunkedLossWrapper.__call__"></a>`__call__(self, pred: torch.Tensor | tuple[torch.Tensor, ...], labels: torch.Tensor | tuple[torch.Tensor, ...], global_valid_tokens: torch.Tensor | None = None, **loss_inputs: Any)` — [`L581`](../../../../../../raw/code/torchtitan/torchtitan/components/loss.py#L581) — Compute chunked loss.
  - <a id="ChunkedLossWrapper._combine_chunk_metrics"></a>`_combine_chunk_metrics(current: dict[str, torch.Tensor], values: dict[str, torch.Tensor])` — [`L778`](../../../../../../raw/code/torchtitan/torchtitan/components/loss.py#L778) — Combine metrics from one sequence chunk into the local accumulator.
  - <a id="ChunkedLossWrapper._gradient_backprop"></a>`_gradient_backprop(self, hidden_states: tuple[torch.Tensor, ...], accumulated_grads: tuple[torch.Tensor, ...], total_loss: torch.Tensor)` — [`L806`](../../../../../../raw/code/torchtitan/torchtitan/components/loss.py#L806) — Return a differentiable loss via _DecoderOutputGradientBackProp.
  - <a id="ChunkedLossWrapper.set_lm_head"></a>`set_lm_head(self, lm_head: nn.Module)` — [`L577`](../../../../../../raw/code/torchtitan/torchtitan/components/loss.py#L577) — Set the lm_head module. Must be called before the first __call__.
  - <a id="ChunkedLossWrapper.lm_head"></a>`lm_head` — [`L575`](../../../../../../raw/code/torchtitan/torchtitan/components/loss.py#L575)
  - <a id="ChunkedLossWrapper.loss_fn"></a>`loss_fn` — [`L574`](../../../../../../raw/code/torchtitan/torchtitan/components/loss.py#L574)
  - <a id="ChunkedLossWrapper.num_chunks"></a>`num_chunks` — [`L573`](../../../../../../raw/code/torchtitan/torchtitan/components/loss.py#L573)
- protocol/private: <a id="ChunkedLossWrapper.__init__"></a>`__init__`[`L567`](../../../../../../raw/code/torchtitan/torchtitan/components/loss.py#L567), <a id="ChunkedLossWrapper._chunk"></a>`_chunk`[`L649`](../../../../../../raw/code/torchtitan/torchtitan/components/loss.py#L649), <a id="ChunkedLossWrapper._chunk_local"></a>`_chunk_local`[`L638`](../../../../../../raw/code/torchtitan/torchtitan/components/loss.py#L638)
- uses (calls/refs, reference-scoped): [`build`](../config/configurable.md#Configurable.Config.build), [`CompileConfig`](../config/configs.md#CompileConfig), [`Config`](loss.md#ChunkedLossWrapper.Config), [`loss_fn`](loss.md#ChunkedLossWrapper.Config.loss_fn), [`get_spmd_backend`](../distributed/utils.md#get_spmd_backend), [`BaseLoss`](loss.md#BaseLoss), [`num_chunks`](loss.md#ChunkedLossWrapper.Config.num_chunks), [`ChunkedLossWrapperWithParamGrads`](../experiments/graph_trainer/chunked_loss.md#ChunkedLossWrapperWithParamGrads), [`add`](loss.md#GradAccumulator.add), [`result`](loss.md#GradAccumulator.result), [`_gradient_backprop`](../experiments/graph_trainer/chunked_loss.md#ChunkedLossWrapperWithParamGrads._gradient_backprop), [`GradAccumulator`](loss.md#GradAccumulator), [`_DecoderOutputGradientBackProp`](loss.md#_DecoderOutputGradientBackProp)
- used by: [`llama3_debugmodel`](../models/llama3/config_registry.md#llama3_debugmodel), [`llama3_405b`](../models/llama3/config_registry.md#llama3_405b), [`_collect_moe_routing_metrics`](../trainer.md#Trainer._collect_moe_routing_metrics), [`sft_debugmodel`](../models/llama3/config_registry.md#sft_debugmodel), [`sft_qwen3_8b_math`](../models/qwen3/config_registry.md#sft_qwen3_8b_math), [`qwen35_debugmodel_moe`](../models/qwen3_5/config_registry.md#qwen35_debugmodel_moe), [`deepseek_v4_debugmodel`](../models/deepseek_v4/config_registry.md#deepseek_v4_debugmodel), [`qwen38_debugmodel_moe`](../models/qwen3_8/config_registry.md#qwen38_debugmodel_moe), [`deepseek_v3_debugmodel`](../models/deepseek_v3/config_registry.md#deepseek_v3_debugmodel), [`deepseek_v4_flash`](../models/deepseek_v4/config_registry.md#deepseek_v4_flash), [`deepseek_v4_pro`](../models/deepseek_v4/config_registry.md#deepseek_v4_pro), [`qwen36_debugmodel_moe`](../models/qwen3_6/config_registry.md#qwen36_debugmodel_moe), [`_gpt_oss_debugmodel`](../models/gpt_oss/config_registry.md#_gpt_oss_debugmodel), [`kimi_k2_5_debugmodel`](../models/kimi_k2_7/config_registry.md#kimi_k2_5_debugmodel), [`muse_glimmer_debugmodel`](../models/muse_glimmer/config_registry.md#muse_glimmer_debugmodel), [`qwen35_debugmodel`](../models/qwen3_5/config_registry.md#qwen35_debugmodel), [`qwen38_debugmodel`](../models/qwen3_8/config_registry.md#qwen38_debugmodel), [`kimi_k2_5`](../models/kimi_k2_7/config_registry.md#kimi_k2_5), [`llama3_70b`](../models/llama3/config_registry.md#llama3_70b), [`muse_glimmer_debugmodel_mm`](../models/muse_glimmer/config_registry.md#muse_glimmer_debugmodel_mm), [`qwen36_debugmodel`](../models/qwen3_6/config_registry.md#qwen36_debugmodel), [`deepseek_v3_671b`](../models/deepseek_v3/config_registry.md#deepseek_v3_671b), [`qwen3_debugmodel`](../models/qwen3/config_registry.md#qwen3_debugmodel), [`deepseek_v3_16b`](../models/deepseek_v3/config_registry.md#deepseek_v3_16b), [`qwen3_moe_debug`](../models/qwen3/config_registry.md#qwen3_moe_debug), [`llama3_8b`](../models/llama3/config_registry.md#llama3_8b), [`qwen35_122b_a10b`](../models/qwen3_5/config_registry.md#qwen35_122b_a10b), [`qwen35_35b_a3b`](../models/qwen3_5/config_registry.md#qwen35_35b_a3b), [`qwen35_397b_a17b`](../models/qwen3_5/config_registry.md#qwen35_397b_a17b), [`qwen36_35b_a3b`](../models/qwen3_6/config_registry.md#qwen36_35b_a3b), [`kimi_k3_debugmodel`](../models/kimi_k3/config_registry.md#kimi_k3_debugmodel), [`qwen3_moe_deepep`](../models/qwen3/config_registry.md#qwen3_moe_deepep), [`qwen35_27b`](../models/qwen3_5/config_registry.md#qwen35_27b), [`qwen35_9b`](../models/qwen3_5/config_registry.md#qwen35_9b), [`qwen36_27b`](../models/qwen3_6/config_registry.md#qwen36_27b), [`qwen38_27b`](../models/qwen3_8/config_registry.md#qwen38_27b), [`qwen3_debugmodel_flex_flash`](../models/qwen3/config_registry.md#qwen3_debugmodel_flex_flash), [`kimi_vl_a3b`](../models/kimi_k2_7/config_registry.md#kimi_vl_a3b), [`moonlight_16b_a3b`](../models/kimi_k2_7/config_registry.md#moonlight_16b_a3b), [`qwen35_0_8b`](../models/qwen3_5/config_registry.md#qwen35_0_8b)  (+24 more; 25 test-only)

### <a id="ChunkedLossWrapper.Config"></a>`ChunkedLossWrapper.Config`  ·  implements/extends Config
- def: [`torchtitan/components/loss.py:560`](../../../../../../raw/code/torchtitan/torchtitan/components/loss.py#L560) — documented in [training-components](../../../concepts/training-components.md)
- signature: `class Config(BaseLoss.Config):`
- members:
  - <a id="ChunkedLossWrapper.Config.loss_fn"></a>`loss_fn` — [`L564`](../../../../../../raw/code/torchtitan/torchtitan/components/loss.py#L564) — --- — documented in [training-components](../../../concepts/training-components.md)
  - <a id="ChunkedLossWrapper.Config.num_chunks"></a>`num_chunks` — [`L561`](../../../../../../raw/code/torchtitan/torchtitan/components/loss.py#L561) — ---
- uses (calls/refs, reference-scoped): [`CrossEntropyLoss`](loss.md#CrossEntropyLoss), [`Config`](loss.md#CrossEntropyLoss.Config), [`BaseLoss`](loss.md#BaseLoss), [`Config`](loss.md#BaseLoss.Config)
- used by: [`llama3_debugmodel`](../models/llama3/config_registry.md#llama3_debugmodel), [`llama3_405b`](../models/llama3/config_registry.md#llama3_405b), [`sft_debugmodel`](../models/llama3/config_registry.md#sft_debugmodel), [`sft_qwen3_8b_math`](../models/qwen3/config_registry.md#sft_qwen3_8b_math), [`qwen35_debugmodel_moe`](../models/qwen3_5/config_registry.md#qwen35_debugmodel_moe), [`deepseek_v4_debugmodel`](../models/deepseek_v4/config_registry.md#deepseek_v4_debugmodel), [`qwen38_debugmodel_moe`](../models/qwen3_8/config_registry.md#qwen38_debugmodel_moe), [`deepseek_v3_debugmodel`](../models/deepseek_v3/config_registry.md#deepseek_v3_debugmodel), [`deepseek_v4_flash`](../models/deepseek_v4/config_registry.md#deepseek_v4_flash), [`deepseek_v4_pro`](../models/deepseek_v4/config_registry.md#deepseek_v4_pro), [`qwen36_debugmodel_moe`](../models/qwen3_6/config_registry.md#qwen36_debugmodel_moe), [`_gpt_oss_debugmodel`](../models/gpt_oss/config_registry.md#_gpt_oss_debugmodel), [`kimi_k2_5_debugmodel`](../models/kimi_k2_7/config_registry.md#kimi_k2_5_debugmodel), [`muse_glimmer_debugmodel`](../models/muse_glimmer/config_registry.md#muse_glimmer_debugmodel), [`qwen35_debugmodel`](../models/qwen3_5/config_registry.md#qwen35_debugmodel), [`qwen38_debugmodel`](../models/qwen3_8/config_registry.md#qwen38_debugmodel), [`kimi_k2_5`](../models/kimi_k2_7/config_registry.md#kimi_k2_5), [`llama3_70b`](../models/llama3/config_registry.md#llama3_70b), [`muse_glimmer_debugmodel_mm`](../models/muse_glimmer/config_registry.md#muse_glimmer_debugmodel_mm), [`qwen36_debugmodel`](../models/qwen3_6/config_registry.md#qwen36_debugmodel), [`deepseek_v3_671b`](../models/deepseek_v3/config_registry.md#deepseek_v3_671b), [`qwen3_debugmodel`](../models/qwen3/config_registry.md#qwen3_debugmodel), [`deepseek_v3_16b`](../models/deepseek_v3/config_registry.md#deepseek_v3_16b), [`qwen3_moe_debug`](../models/qwen3/config_registry.md#qwen3_moe_debug), [`llama3_8b`](../models/llama3/config_registry.md#llama3_8b), [`qwen35_122b_a10b`](../models/qwen3_5/config_registry.md#qwen35_122b_a10b), [`qwen35_35b_a3b`](../models/qwen3_5/config_registry.md#qwen35_35b_a3b), [`qwen35_397b_a17b`](../models/qwen3_5/config_registry.md#qwen35_397b_a17b), [`qwen36_35b_a3b`](../models/qwen3_6/config_registry.md#qwen36_35b_a3b), [`kimi_k3_debugmodel`](../models/kimi_k3/config_registry.md#kimi_k3_debugmodel), [`qwen3_moe_deepep`](../models/qwen3/config_registry.md#qwen3_moe_deepep), [`qwen35_27b`](../models/qwen3_5/config_registry.md#qwen35_27b), [`qwen35_9b`](../models/qwen3_5/config_registry.md#qwen35_9b), [`qwen36_27b`](../models/qwen3_6/config_registry.md#qwen36_27b), [`qwen38_27b`](../models/qwen3_8/config_registry.md#qwen38_27b), [`qwen3_debugmodel_flex_flash`](../models/qwen3/config_registry.md#qwen3_debugmodel_flex_flash), [`kimi_vl_a3b`](../models/kimi_k2_7/config_registry.md#kimi_vl_a3b), [`moonlight_16b_a3b`](../models/kimi_k2_7/config_registry.md#moonlight_16b_a3b), [`qwen35_0_8b`](../models/qwen3_5/config_registry.md#qwen35_0_8b), [`qwen35_2b`](../models/qwen3_5/config_registry.md#qwen35_2b)  (+19 more; 25 test-only)

### <a id="CrossEntropyLoss"></a>`CrossEntropyLoss`  ·  implements/extends BaseLoss
- def: [`torchtitan/components/loss.py:287`](../../../../../../raw/code/torchtitan/torchtitan/components/loss.py#L287) — documented in [training-components](../../../concepts/training-components.md)
- doc: Cross-entropy loss with sum reduction for token-based normalization.
- signature: `class CrossEntropyLoss(BaseLoss):`
- members:
  - <a id="CrossEntropyLoss.fn"></a>`fn` — [`L296`](../../../../../../raw/code/torchtitan/torchtitan/components/loss.py#L296) — ---
  - <a id="CrossEntropyLoss.global_vocab_size"></a>`global_vocab_size` — [`L298`](../../../../../../raw/code/torchtitan/torchtitan/components/loss.py#L298)
- protocol/private: <a id="CrossEntropyLoss.__call__"></a>`__call__`[`L300`](../../../../../../raw/code/torchtitan/torchtitan/components/loss.py#L300), <a id="CrossEntropyLoss.__init__"></a>`__init__`[`L295`](../../../../../../raw/code/torchtitan/torchtitan/components/loss.py#L295)
- uses (calls/refs, reference-scoped): [`CompileConfig`](../config/configs.md#CompileConfig), [`Config`](loss.md#CrossEntropyLoss.Config), [`get_spmd_backend`](../distributed/utils.md#get_spmd_backend), [`global_vocab_size`](loss.md#CrossEntropyLoss.Config.global_vocab_size), [`BaseLoss`](loss.md#BaseLoss), [`cross_entropy_loss`](loss.md#cross_entropy_loss), [`current_spmd_mesh`](../distributed/spmd_types.md#current_spmd_mesh), [`_maybe_compile`](loss.md#BaseLoss._maybe_compile), [`LossFunction`](loss.md#LossFunction.LossFunction), [`MTPLoss`](../models/deepseek_v3/mtp.md#MTPLoss)
- used by: [`sft_llama3_8b_metamath`](../experiments/tpu/llama3/config_registry.md#sft_llama3_8b_metamath), [`reg_trainer_qwen3_8b`](../experiments/tpu/qwen3/config_registry.md#reg_trainer_qwen3_8b), [`qwen3_1_7b`](../experiments/tpu/qwen3/config_registry.md#qwen3_1_7b), [`llama3_70b`](../experiments/tpu/llama3/config_registry.md#llama3_70b), [`llama3_405b`](../experiments/tpu/llama3/config_registry.md#llama3_405b), [`llama3_8b`](../experiments/tpu/llama3/config_registry.md#llama3_8b), [`llama3_debugmodel`](../models/llama3/config_registry.md#llama3_debugmodel), [`llama3_torchft_debugmodel`](../experiments/torchft/llama3/config_registry.md#llama3_torchft_debugmodel), [`_muse_glimmer_30b_base`](../experiments/tpu/muse_glimmer/config_registry.md#_muse_glimmer_30b_base), [`llama3_405b`](../models/llama3/config_registry.md#llama3_405b), [`qwen3_moe_30b`](../experiments/tpu/qwen3/config_registry.md#qwen3_moe_30b), [`_tpu_hf_config`](../experiments/tpu/transformers_modeling_backend/config_registry.md#_tpu_hf_config), [`transformers_modeling_backend_sft_full`](../experiments/transformers_modeling_backend/config_registry.md#transformers_modeling_backend_sft_full), [`sft_debugmodel`](../models/llama3/config_registry.md#sft_debugmodel), [`sft_qwen3_8b_math`](../models/qwen3/config_registry.md#sft_qwen3_8b_math), [`transformers_modeling_backend_sft_debugmodel`](../experiments/transformers_modeling_backend/config_registry.md#transformers_modeling_backend_sft_debugmodel), [`qwen35_debugmodel_moe`](../models/qwen3_5/config_registry.md#qwen35_debugmodel_moe), [`deepseek_v4_debugmodel`](../models/deepseek_v4/config_registry.md#deepseek_v4_debugmodel), [`qwen35_moe_35b`](../experiments/tpu/qwen3_5/config_registry.md#qwen35_moe_35b), [`qwen38_debugmodel_moe`](../models/qwen3_8/config_registry.md#qwen38_debugmodel_moe), [`deepseek_v3_debugmodel`](../models/deepseek_v3/config_registry.md#deepseek_v3_debugmodel), [`deepseek_v4_flash`](../models/deepseek_v4/config_registry.md#deepseek_v4_flash), [`deepseek_v4_pro`](../models/deepseek_v4/config_registry.md#deepseek_v4_pro), [`qwen36_debugmodel_moe`](../models/qwen3_6/config_registry.md#qwen36_debugmodel_moe), [`_gpt_oss_debugmodel`](../models/gpt_oss/config_registry.md#_gpt_oss_debugmodel), [`kimi_k2_5_debugmodel`](../models/kimi_k2_7/config_registry.md#kimi_k2_5_debugmodel), [`muse_glimmer_debugmodel`](../models/muse_glimmer/config_registry.md#muse_glimmer_debugmodel), [`transformers_modeling_backend_debugmodel`](../experiments/transformers_modeling_backend/config_registry.md#transformers_modeling_backend_debugmodel), [`qwen3_debugmodel`](../experiments/tpu/qwen3/config_registry.md#qwen3_debugmodel), [`transformers_modeling_backend_debugmodel_moe`](../experiments/transformers_modeling_backend/config_registry.md#transformers_modeling_backend_debugmodel_moe), [`qwen35_debugmodel`](../models/qwen3_5/config_registry.md#qwen35_debugmodel), [`qwen38_debugmodel`](../models/qwen3_8/config_registry.md#qwen38_debugmodel), [`kimi_k2_5`](../models/kimi_k2_7/config_registry.md#kimi_k2_5), [`llama3_70b`](../models/llama3/config_registry.md#llama3_70b), [`muse_glimmer_debugmodel_mm`](../models/muse_glimmer/config_registry.md#muse_glimmer_debugmodel_mm), [`qwen36_debugmodel`](../models/qwen3_6/config_registry.md#qwen36_debugmodel), [`deepseek_v3_671b`](../models/deepseek_v3/config_registry.md#deepseek_v3_671b), [`qwen3_debugmodel`](../models/qwen3/config_registry.md#qwen3_debugmodel), [`deepseek_v3_16b`](../models/deepseek_v3/config_registry.md#deepseek_v3_16b), [`conformer_test`](../experiments/tpu/conformer/config_registry.md#conformer_test)  (+44 more; 16 test-only)

### <a id="CrossEntropyLoss.Config"></a>`CrossEntropyLoss.Config`  ·  implements/extends Config
- def: [`torchtitan/components/loss.py:291`](../../../../../../raw/code/torchtitan/torchtitan/components/loss.py#L291) — documented in [training-components](../../../concepts/training-components.md)
- signature: `class Config(BaseLoss.Config):`
- members:
  - <a id="CrossEntropyLoss.Config.global_vocab_size"></a>`global_vocab_size` — [`L292`](../../../../../../raw/code/torchtitan/torchtitan/components/loss.py#L292) — --- — documented in [training-components](../../../concepts/training-components.md)
- uses (calls/refs, reference-scoped): [`BaseLoss`](loss.md#BaseLoss), [`Config`](loss.md#BaseLoss.Config)
- used by: [`sft_llama3_8b_metamath`](../experiments/tpu/llama3/config_registry.md#sft_llama3_8b_metamath), [`reg_trainer_qwen3_8b`](../experiments/tpu/qwen3/config_registry.md#reg_trainer_qwen3_8b), [`qwen3_1_7b`](../experiments/tpu/qwen3/config_registry.md#qwen3_1_7b), [`llama3_70b`](../experiments/tpu/llama3/config_registry.md#llama3_70b), [`llama3_405b`](../experiments/tpu/llama3/config_registry.md#llama3_405b), [`llama3_8b`](../experiments/tpu/llama3/config_registry.md#llama3_8b), [`llama3_debugmodel`](../models/llama3/config_registry.md#llama3_debugmodel), [`llama3_torchft_debugmodel`](../experiments/torchft/llama3/config_registry.md#llama3_torchft_debugmodel), [`_muse_glimmer_30b_base`](../experiments/tpu/muse_glimmer/config_registry.md#_muse_glimmer_30b_base), [`llama3_405b`](../models/llama3/config_registry.md#llama3_405b), [`qwen3_moe_30b`](../experiments/tpu/qwen3/config_registry.md#qwen3_moe_30b), [`_tpu_hf_config`](../experiments/tpu/transformers_modeling_backend/config_registry.md#_tpu_hf_config), [`transformers_modeling_backend_sft_full`](../experiments/transformers_modeling_backend/config_registry.md#transformers_modeling_backend_sft_full), [`sft_debugmodel`](../models/llama3/config_registry.md#sft_debugmodel), [`sft_qwen3_8b_math`](../models/qwen3/config_registry.md#sft_qwen3_8b_math), [`transformers_modeling_backend_sft_debugmodel`](../experiments/transformers_modeling_backend/config_registry.md#transformers_modeling_backend_sft_debugmodel), [`qwen35_debugmodel_moe`](../models/qwen3_5/config_registry.md#qwen35_debugmodel_moe), [`deepseek_v4_debugmodel`](../models/deepseek_v4/config_registry.md#deepseek_v4_debugmodel), [`qwen35_moe_35b`](../experiments/tpu/qwen3_5/config_registry.md#qwen35_moe_35b), [`qwen38_debugmodel_moe`](../models/qwen3_8/config_registry.md#qwen38_debugmodel_moe), [`deepseek_v3_debugmodel`](../models/deepseek_v3/config_registry.md#deepseek_v3_debugmodel), [`deepseek_v4_flash`](../models/deepseek_v4/config_registry.md#deepseek_v4_flash), [`deepseek_v4_pro`](../models/deepseek_v4/config_registry.md#deepseek_v4_pro), [`qwen36_debugmodel_moe`](../models/qwen3_6/config_registry.md#qwen36_debugmodel_moe), [`_gpt_oss_debugmodel`](../models/gpt_oss/config_registry.md#_gpt_oss_debugmodel), [`deepseek_v4_mtp_debugmodel`](../models/deepseek_v4/config_registry.md#deepseek_v4_mtp_debugmodel), [`kimi_k2_5_debugmodel`](../models/kimi_k2_7/config_registry.md#kimi_k2_5_debugmodel), [`muse_glimmer_debugmodel`](../models/muse_glimmer/config_registry.md#muse_glimmer_debugmodel), [`transformers_modeling_backend_debugmodel`](../experiments/transformers_modeling_backend/config_registry.md#transformers_modeling_backend_debugmodel), [`qwen3_debugmodel`](../experiments/tpu/qwen3/config_registry.md#qwen3_debugmodel), [`transformers_modeling_backend_debugmodel_moe`](../experiments/transformers_modeling_backend/config_registry.md#transformers_modeling_backend_debugmodel_moe), [`qwen35_debugmodel`](../models/qwen3_5/config_registry.md#qwen35_debugmodel), [`qwen38_debugmodel`](../models/qwen3_8/config_registry.md#qwen38_debugmodel), [`kimi_k2_5`](../models/kimi_k2_7/config_registry.md#kimi_k2_5), [`llama3_70b`](../models/llama3/config_registry.md#llama3_70b), [`muse_glimmer_debugmodel_mm`](../models/muse_glimmer/config_registry.md#muse_glimmer_debugmodel_mm), [`qwen36_debugmodel`](../models/qwen3_6/config_registry.md#qwen36_debugmodel), [`deepseek_v3_671b`](../models/deepseek_v3/config_registry.md#deepseek_v3_671b), [`qwen3_debugmodel`](../models/qwen3/config_registry.md#qwen3_debugmodel), [`deepseek_v3_16b`](../models/deepseek_v3/config_registry.md#deepseek_v3_16b)  (+44 more; 16 test-only)

### <a id="GradAccumulator"></a>`GradAccumulator`
- def: [`torchtitan/components/loss.py:397`](../../../../../../raw/code/torchtitan/torchtitan/components/loss.py#L397)
- doc: Accumulates chunk gradients into a pre-allocated buffer.
- signature: `class GradAccumulator:`
- members:
  - <a id="GradAccumulator.add"></a>`add(self, chunk_grad: torch.Tensor)` — [`L448`](../../../../../../raw/code/torchtitan/torchtitan/components/loss.py#L448) — Add the next chunk gradient sequentially.
  - <a id="GradAccumulator.result"></a>`result(self)` — [`L491`](../../../../../../raw/code/torchtitan/torchtitan/components/loss.py#L491) — Return the accumulated gradient tensor, wrapped as DTensor if needed.
  - <a id="GradAccumulator.num_chunks"></a>`num_chunks` — [`L433`](../../../../../../raw/code/torchtitan/torchtitan/components/loss.py#L433)
  - <a id="GradAccumulator.seq_dim"></a>`seq_dim` — [`L434`](../../../../../../raw/code/torchtitan/torchtitan/components/loss.py#L434)
- protocol/private: <a id="GradAccumulator.__init__"></a>`__init__`[`L422`](../../../../../../raw/code/torchtitan/torchtitan/components/loss.py#L422), <a id="GradAccumulator._buffer"></a>`_buffer`[`L446`](../../../../../../raw/code/torchtitan/torchtitan/components/loss.py#L446), <a id="GradAccumulator._device_mesh"></a>`_device_mesh`[`L436`](../../../../../../raw/code/torchtitan/torchtitan/components/loss.py#L436), <a id="GradAccumulator._next_idx"></a>`_next_idx`[`L435`](../../../../../../raw/code/torchtitan/torchtitan/components/loss.py#L435), <a id="GradAccumulator._placements"></a>`_placements`[`L438`](../../../../../../raw/code/torchtitan/torchtitan/components/loss.py#L438)
- used by: [`__call__`](loss.md#ChunkedLossWrapper.__call__)

### <a id="MSELoss"></a>`MSELoss`  ·  implements/extends BaseLoss
- def: [`torchtitan/components/loss.py:322`](../../../../../../raw/code/torchtitan/torchtitan/components/loss.py#L322)
- doc: MSE loss with sum reduction for Transformer models training (e.g. Flux).
- signature: `class MSELoss(BaseLoss):`
- members:
  - <a id="MSELoss.fn"></a>`fn` — [`L330`](../../../../../../raw/code/torchtitan/torchtitan/components/loss.py#L330) — ---
- protocol/private: <a id="MSELoss.__init__"></a>`__init__`[`L329`](../../../../../../raw/code/torchtitan/torchtitan/components/loss.py#L329)
- uses (calls/refs, reference-scoped): [`CompileConfig`](../config/configs.md#CompileConfig), [`BaseLoss`](loss.md#BaseLoss), [`_maybe_compile`](loss.md#BaseLoss._maybe_compile), [`LossFunction`](loss.md#LossFunction.LossFunction), [`Config`](loss.md#MSELoss.Config), [`mse_loss`](loss.md#mse_loss)
- used by: [`flux_debugmodel`](../models/flux/config_registry.md#flux_debugmodel), [`flux_dev`](../models/flux/config_registry.md#flux_dev), [`flux_schnell`](../models/flux/config_registry.md#flux_schnell), [`BaseLoss`](loss.md#BaseLoss)

### <a id="MSELoss.Config"></a>`MSELoss.Config`  ·  implements/extends Config
- def: [`torchtitan/components/loss.py:326`](../../../../../../raw/code/torchtitan/torchtitan/components/loss.py#L326)
- signature: `class Config(BaseLoss.Config):`
- uses (calls/refs, reference-scoped): [`BaseLoss`](loss.md#BaseLoss), [`Config`](loss.md#BaseLoss.Config)
- used by: [`flux_debugmodel`](../models/flux/config_registry.md#flux_debugmodel), [`flux_dev`](../models/flux/config_registry.md#flux_dev), [`flux_schnell`](../models/flux/config_registry.md#flux_schnell), [`__init__`](loss.md#MSELoss.__init__)

### <a id="_DecoderOutputGradientBackProp"></a>`_DecoderOutputGradientBackProp`
- def: [`torchtitan/components/loss.py:827`](../../../../../../raw/code/torchtitan/torchtitan/components/loss.py#L827)
- members:
  - <a id="_DecoderOutputGradientBackProp.backward"></a>`backward(ctx, grad_output: torch.Tensor)` — [`L855`](../../../../../../raw/code/torchtitan/torchtitan/components/loss.py#L855)
  - <a id="_DecoderOutputGradientBackProp.forward"></a>`forward(ctx, num_predictions: int, *args: torch.Tensor)` — [`L841`](../../../../../../raw/code/torchtitan/torchtitan/components/loss.py#L841)
- used by: [`_gradient_backprop`](loss.md#ChunkedLossWrapper._gradient_backprop)

### <a id="_LossParallelCrossEntropy"></a>`_LossParallelCrossEntropy`
- def: [`torchtitan/components/loss.py:74`](../../../../../../raw/code/torchtitan/torchtitan/components/loss.py#L74)
- members:
  - <a id="_LossParallelCrossEntropy.backward"></a>`backward(ctx, grad_output: torch.Tensor)` — [`L199`](../../../../../../raw/code/torchtitan/torchtitan/components/loss.py#L199)
  - <a id="_LossParallelCrossEntropy.forward"></a>`forward(ctx, logits: torch.Tensor, labels: torch.Tensor, tp_group: dist.ProcessGroup, global_vocab_size: int, reduction: str = "sum")` — [`L112`](../../../../../../raw/code/torchtitan/torchtitan/components/loss.py#L112) — Compute exact CE from local vocab shards via TP all-reduces.
  - <a id="_LossParallelCrossEntropy.spmd_typecheck"></a>`spmd_typecheck(result: torch.Tensor, *, logits: torch.Tensor, labels: torch.Tensor, tp_group: dist.ProcessGroup)` — [`L91`](../../../../../../raw/code/torchtitan/torchtitan/components/loss.py#L91) — SPMD type: logits S(-1)@TP, labels I@TP -> loss I@TP.
- uses (calls/refs, reference-scoped): [`IGNORE_INDEX`](loss.md#IGNORE_INDEX)
- used by: [`cross_entropy_loss`](loss.md#cross_entropy_loss)

## Functions
- <a id="compute_logprobs"></a>`compute_logprobs(logits: torch.Tensor, labels: torch.Tensor, *, return_entropy: bool = False)` — [`L334`](../../../../../../raw/code/torchtitan/torchtitan/components/loss.py#L334) — Per-token logprobs from ``logits[T, V]`` and ``labels[T]``.
- <a id="cross_entropy_loss"></a>`cross_entropy_loss(pred: torch.Tensor, labels: torch.Tensor, *, global_vocab_size: int | None = None)` — [`L37`](../../../../../../raw/code/torchtitan/torchtitan/components/loss.py#L37) — Cross-entropy over ``pred[T, V]`` and ``labels[T]`` with sum reduction.
- <a id="mse_loss"></a>`mse_loss(pred: torch.Tensor, labels: torch.Tensor)` — [`L229`](../../../../../../raw/code/torchtitan/torchtitan/components/loss.py#L229) — MSE loss with sum reduction for Transformer models training.

## Module values
- <a id="IGNORE_INDEX"></a>`IGNORE_INDEX` — [`L32`](../../../../../../raw/code/torchtitan/torchtitan/components/loss.py#L32)
- <a id="LossFunction.LossFunction"></a>`LossFunction` — [`L34`](../../../../../../raw/code/torchtitan/torchtitan/components/loss.py#L34)

