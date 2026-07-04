---
title: 'Module: easydel/modules/_base/_features.py'
type: catalog
provenance: extracted
module: easydel/modules/_base/_features.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules._base._features`/
symbols:
  GradientCheckpointingFeature.get_config: GradientCheckpointingFeature#get_config().
  GradientCheckpointingFeature.should_checkpoint: GradientCheckpointingFeature#should_checkpoint().
  SequenceLengthPoolingFeature.strategy: SequenceLengthPoolingFeature#strategy.
  SequenceLengthPoolingFeature.pool: SequenceLengthPoolingFeature#pool().
  SequenceLengthPoolingFeature.__repr__: SequenceLengthPoolingFeature#__repr__().
  TieEmbeddingsFeature.setup: TieEmbeddingsFeature#setup().
  GradientCheckpointingFeature.policy: GradientCheckpointingFeature#policy.
  LogitCapFeature.apply: LogitCapFeature#apply().
  RouterAuxLossFeature.compute_loss: RouterAuxLossFeature#compute_loss().
  LogitCapFeature: LogitCapFeature#
  LogitCapFeature.cap_value: LogitCapFeature#cap_value.
  TieEmbeddingsFeature: TieEmbeddingsFeature#
  RouterAuxLossFeature: RouterAuxLossFeature#
  GradientCheckpointingFeature: GradientCheckpointingFeature#
  SequenceLengthPoolingFeature: SequenceLengthPoolingFeature#
  LogitCapFeature.__repr__: LogitCapFeature#__repr__().
  TieEmbeddingsFeature.__repr__: TieEmbeddingsFeature#__repr__().
  RouterAuxLossFeature.__repr__: RouterAuxLossFeature#__repr__().
  GradientCheckpointingFeature.__repr__: GradientCheckpointingFeature#__repr__().
  TieEmbeddingsFeature.tie: TieEmbeddingsFeature#tie.
  RouterAuxLossFeature.coef: RouterAuxLossFeature#coef.
  SequenceLengthPoolingFeature.pad_token_id: SequenceLengthPoolingFeature#pad_token_id.
  GradientCheckpointingFeature.save_names: GradientCheckpointingFeature#save_names.
  GradientCheckpointingFeature.exclude_names: GradientCheckpointingFeature#exclude_names.
  LogitCapFeature.__init__: LogitCapFeature#__init__().
  TieEmbeddingsFeature.__init__: TieEmbeddingsFeature#__init__().
  RouterAuxLossFeature.__init__: RouterAuxLossFeature#__init__().
  GradientCheckpointingFeature.__init__: GradientCheckpointingFeature#__init__().
  SequenceLengthPoolingFeature.__init__: SequenceLengthPoolingFeature#__init__().
---
# Module: [`easydel/modules/_base/_features.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_features.py)

## Classes
### `GradientCheckpointingFeature`
- def: [`easydel/modules/_base/_features.py:354`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_features.py#L354)
- doc: Configure gradient checkpointing for model components.
- signature: `class GradientCheckpointingFeature:`
- members:
  - `__init__(self, policy: str | None = None, save_names: list[str] | None = None, exclude_names: list[str] | None = None)` — [`L391`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_features.py#L391) — Initialize gradient checkpointing feature.
  - `__repr__(self)` — [`L482`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_features.py#L482) — Return string representation of the feature.
  - `get_config(self)` — [`L448`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_features.py#L448) — Get checkpointing configuration as a dictionary.
  - `should_checkpoint(self)` — [`L429`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_features.py#L429) — Check if gradient checkpointing should be applied.
  - `exclude_names` — [`L427`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_features.py#L427)
  - `policy` — [`L425`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_features.py#L425)
  - `save_names` — [`L426`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_features.py#L426)
- used by: [`_lm_head_name`](conditional_generation_module.md#BaseConditionalGenerationModule._lm_head_name), [`_lm_head_name`](causal_lm_module.md#BaseCausalLMModule._lm_head_name), [`__init__`](image_classification_module.md#BaseImageClassificationModule.__init__), [`__init__`](question_answering_module.md#BaseQuestionAnsweringModule.__init__), [`_score_head_name`](sequence_classification_module.md#BaseSequenceClassificationModule._score_head_name), [`dropout`](token_classification_module.md#BaseTokenClassificationModule.dropout), [`_gradient_checkpointing_feature`](_base_task_module.md#BaseTaskModule._gradient_checkpointing_feature)

### `LogitCapFeature`
- def: [`easydel/modules/_base/_features.py:61`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_features.py#L61)
- doc: Apply logit capping to prevent extreme values.
- signature: `class LogitCapFeature:`
- members:
  - `__init__(self, cap_value: float)` — [`L94`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_features.py#L94) — Initialize logit capping feature.
  - `__repr__(self)` — [`L143`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_features.py#L143) — Return string representation of the feature.
  - `apply(self, logits: Float[Array, "batch seq_len vocab"])` — [`L117`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_features.py#L117) — Apply logit capping to the given logits.
  - `cap_value` — [`L115`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_features.py#L115)
- used by: [`apply_logit_cap`](_base_task_module.md#BaseTaskModule.apply_logit_cap), [`_logit_cap_feature`](_base_task_module.md#BaseTaskModule._logit_cap_feature)

### `RouterAuxLossFeature`
- def: [`easydel/modules/_base/_features.py:249`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_features.py#L249)
- doc: Compute auxiliary loss for MoE router load balancing.
- signature: `class RouterAuxLossFeature:`
- members:
  - `__init__(self, coef: float)` — [`L283`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_features.py#L283) — Initialize router auxiliary loss feature.
  - `__repr__(self)` — [`L345`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_features.py#L345) — Return string representation of the feature.
  - `compute_loss(self, router_losses: list[Array] | tuple[Array, ...] | None)` — [`L309`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_features.py#L309) — Compute the weighted auxiliary loss from router losses.
  - `coef` — [`L307`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_features.py#L307)
- used by: [`compute_router_aux_loss`](_base_task_module.md#BaseTaskModule.compute_router_aux_loss), [`_router_aux_loss_feature`](_base_task_module.md#BaseTaskModule._router_aux_loss_feature)

### `SequenceLengthPoolingFeature`
- def: [`easydel/modules/_base/_features.py:491`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_features.py#L491)
- doc: Pool sequence representations for classification tasks.
- signature: `class SequenceLengthPoolingFeature:`
- members:
  - `__init__(self, strategy: str = "last", pad_token_id: int | None = None)` — [`L527`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_features.py#L527) — Initialize sequence pooling feature.
  - `__repr__(self)` — [`L662`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_features.py#L662) — Return string representation of the feature.
  - `pool(self, hidden_states: Float[Array, "batch seq_len hidden"], input_ids: Array | None = None, attention_mask: Array | None = None)` — [`L574`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_features.py#L574) — Pool hidden states to get sequence-level representation.
  - `pad_token_id` — [`L572`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_features.py#L572)
  - `strategy` — [`L571`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_features.py#L571)
- used by: [`pool_sequence`](_base_task_module.md#BaseTaskModule.pool_sequence), [`_pooling_feature`](_base_task_module.md#BaseTaskModule._pooling_feature)

### `TieEmbeddingsFeature`
- def: [`easydel/modules/_base/_features.py:152`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_features.py#L152)
- doc: Tie input embeddings with output head weights.
- signature: `class TieEmbeddingsFeature:`
- members:
  - `__init__(self, tie: bool = True)` — [`L184`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_features.py#L184) — Initialize embedding tying feature.
  - `__repr__(self)` — [`L240`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_features.py#L240) — Return string representation of the feature.
  - `setup(self, embedding_module: nn.Module, lm_head_module: nn.Module)` — [`L203`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_features.py#L203) — Set up weight tying between embedding and LM head.
  - `tie` — [`L201`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_features.py#L201)
- used by: [`_lm_head_name`](conditional_generation_module.md#BaseConditionalGenerationModule._lm_head_name), [`_lm_head_name`](causal_lm_module.md#BaseCausalLMModule._lm_head_name), [`_tie_embeddings_feature`](_base_task_module.md#BaseTaskModule._tie_embeddings_feature)

