---
title: 'Module: torchtitan_recipes/tests/features.py'
type: catalog
provenance: extracted
module: torchtitan_recipes/tests/features.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan_recipes.tests.features`/
symbols:
  deepseek_v3_debugmodel_sdc_replay_mismatch: deepseek_v3_debugmodel_sdc_replay_mismatch().
  llama3_debugmodel_validation_tp2_cp2_pp2: llama3_debugmodel_validation_tp2_cp2_pp2().
  llama3_debugmodel_pp2_custom_csv: llama3_debugmodel_pp2_custom_csv().
  llama3_debugmodel_fsdp2_tp2_pp2_save: llama3_debugmodel_fsdp2_tp2_pp2_save().
  llama3_debugmodel_fsdp2_tp2_pp2_compile: llama3_debugmodel_fsdp2_tp2_pp2_compile().
  llama3_debugmodel_pp2_zbv: llama3_debugmodel_pp2_zbv().
  llama3_debugmodel_sdc_replay_cudagraph: llama3_debugmodel_sdc_replay_cudagraph().
  llama3_debugmodel_tp2_pp2_gpipe: llama3_debugmodel_tp2_pp2_gpipe().
  llama3_debugmodel_ddp2_cp2: llama3_debugmodel_ddp2_cp2().
  llama3_debugmodel_hsdp2x2_cp2: llama3_debugmodel_hsdp2x2_cp2().
  llama3_debugmodel_fsdp2_pp2_1f1b: llama3_debugmodel_fsdp2_pp2_1f1b().
  llama3_debugmodel_fsdp2_cp2: llama3_debugmodel_fsdp2_cp2().
  llama3_debugmodel_pp2_1f1b: llama3_debugmodel_pp2_1f1b().
  llama3_debugmodel_ulysses_cp2: llama3_debugmodel_ulysses_cp2().
  deepseek_v3_debugmodel_fused_grouped_experts_tp2_ep4: deepseek_v3_debugmodel_fused_grouped_experts_tp2_ep4().
  llama3_debugmodel_float8_emulate_lora_tp2_pp2: llama3_debugmodel_float8_emulate_lora_tp2_pp2().
  llama3_debugmodel_pp4_interleaved_1f1b: llama3_debugmodel_pp4_interleaved_1f1b().
  SDCReplayMismatchTrainer.train_step: SDCReplayMismatchTrainer#train_step().
  llama3_debugmodel_cp4: llama3_debugmodel_cp4().
  llama3_debugmodel_optional_checkpoint_load_tp2: llama3_debugmodel_optional_checkpoint_load_tp2().
  llama3_debugmodel_pp4_zero_bubble: llama3_debugmodel_pp4_zero_bubble().
  llama3_debugmodel_varlen_attn_fsdp4_sac: llama3_debugmodel_varlen_attn_fsdp4_sac().
  llama3_debugmodel_seed_checkpoint: llama3_debugmodel_seed_checkpoint().
  llama3_debugmodel_default: llama3_debugmodel_default().
  llama3_debugmodel_hf_checkpoint_save: llama3_debugmodel_hf_checkpoint_save().
  llama3_debugmodel_hf_checkpoint_load: llama3_debugmodel_hf_checkpoint_load().
  llama3_debugmodel_fused_swiglu_tp2: llama3_debugmodel_fused_swiglu_tp2().
  llama3_debugmodel_hsdp2x2: llama3_debugmodel_hsdp2x2().
  llama3_debugmodel_full_checkpoint_save: llama3_debugmodel_full_checkpoint_save().
  llama3_debugmodel_compile_sac_op: llama3_debugmodel_compile_sac_op().
  llama3_debugmodel_last_save_model_only_bf16: llama3_debugmodel_last_save_model_only_bf16().
  llama3_debugmodel_ddp4: llama3_debugmodel_ddp4().
  llama3_debugmodel_gradient_accumulation: llama3_debugmodel_gradient_accumulation().
  llama3_debugmodel_compile: llama3_debugmodel_compile().
  llama3_debugmodel_tp2: llama3_debugmodel_tp2().
  llama3_debugmodel_tp2_compile: llama3_debugmodel_tp2_compile().
  llama3_debugmodel_optional_checkpoint_save: llama3_debugmodel_optional_checkpoint_save().
  llama3_debugmodel_ce_loss_tp2: llama3_debugmodel_ce_loss_tp2().
  llama3_debugmodel_tp2_no_sp: llama3_debugmodel_tp2_no_sp().
  llama3_debugmodel_tp2_asynctp_compile_spmd_types: llama3_debugmodel_tp2_asynctp_compile_spmd_types().
  llama3_debugmodel_full_checkpoint_load: llama3_debugmodel_full_checkpoint_load().
  llama3_debugmodel_fsdp2_pp2_1f1b_layers_per_stage: llama3_debugmodel_fsdp2_pp2_1f1b_layers_per_stage().
  llama3_debugmodel_fsdp2_tp2_pp2_load: llama3_debugmodel_fsdp2_tp2_pp2_load().
  llama3_debugmodel_pp4_interleaved_1f1b_layers_per_stage: llama3_debugmodel_pp4_interleaved_1f1b_layers_per_stage().
  llama3_debugmodel_optimizer_bf16_states: llama3_debugmodel_optimizer_bf16_states().
  llama3_debugmodel_hsdp2x2_tp2: llama3_debugmodel_hsdp2x2_tp2().
  llama3_debugmodel_fsdp2_tp2_cp2: llama3_debugmodel_fsdp2_tp2_cp2().
  llama3_debugmodel_fsdp_reshard_always: llama3_debugmodel_fsdp_reshard_always().
  llama3_debugmodel_sft: llama3_debugmodel_sft().
  SDCReplayMismatchTrainer.forward_backward_step: SDCReplayMismatchTrainer#forward_backward_step().
  SDCReplayMismatchTrainer.Config: SDCReplayMismatchTrainer#Config#
  SDCReplayMismatchTrainer.__init__: SDCReplayMismatchTrainer#__init__().
  SDCReplayMismatchTrainer: SDCReplayMismatchTrainer#
  SDCReplayMismatchTrainer._num_forward_backward_calls: SDCReplayMismatchTrainer#_num_forward_backward_calls.
---
# Module: [`torchtitan_recipes/tests/features.py`](../../../../../../raw/code/torchtitan/torchtitan_recipes/tests/features.py)

## Classes
### <a id="SDCReplayMismatchTrainer"></a>`SDCReplayMismatchTrainer`  ·  implements/extends Trainer
- def: [`torchtitan_recipes/tests/features.py:40`](../../../../../../raw/code/torchtitan/torchtitan_recipes/tests/features.py#L40)
- doc: Inject a replay-only gradient mismatch and verify it is fatal.
- signature: `class SDCReplayMismatchTrainer(Trainer):`
- members:
  - <a id="SDCReplayMismatchTrainer.forward_backward_step"></a>`forward_backward_step(self, *, input_dict: dict[str, Any] | list[dict[str, Any]], global_valid_tokens: torch.Tensor)` — [`L51`](../../../../../../raw/code/torchtitan/torchtitan_recipes/tests/features.py#L51) — documented in [trainer-and-train-loop](../../../concepts/trainer-and-train-loop.md)
  - <a id="SDCReplayMismatchTrainer.train_step"></a>`train_step(self, data_iterator: Iterator[dict[str, Any]])` — [`L79`](../../../../../../raw/code/torchtitan/torchtitan_recipes/tests/features.py#L79) — documented in [trainer-and-train-loop](../../../concepts/trainer-and-train-loop.md)
- protocol/private: <a id="SDCReplayMismatchTrainer.__init__"></a>`__init__`[`L47`](../../../../../../raw/code/torchtitan/torchtitan_recipes/tests/features.py#L47), <a id="SDCReplayMismatchTrainer._num_forward_backward_calls"></a>`_num_forward_backward_calls`[`L49`](../../../../../../raw/code/torchtitan/torchtitan_recipes/tests/features.py#L49)
- uses (calls/refs, reference-scoped): [`logger`](../../torchtitan/tools/logging.md#logger), [`Trainer`](../../torchtitan/trainer.md#Trainer), [`train_step`](../../torchtitan/trainer.md#Trainer.train_step), [`model_parts`](../../torchtitan/trainer.md#Trainer.model_parts), [`forward_backward_step`](../../torchtitan/trainer.md#Trainer.forward_backward_step), [`__init__`](../../torchtitan/trainer.md#Trainer.__init__), [`sdc_replayer`](../../torchtitan/trainer.md#Trainer.sdc_replayer), [`steps_since_reset`](../../torchtitan/observability/sdc_replayer.md#SDCReplayer.steps_since_reset), [`SDCReplayMismatch`](../../torchtitan/observability/sdc_replayer.md#SDCReplayMismatch), [`signature_mismatch`](../../torchtitan/observability/sdc_replayer.md#SDCReplayMismatch.signature_mismatch), [`local_step`](../../torchtitan/observability/sdc_replayer.md#SDCReplayMismatch.local_step), [`rank`](../../torchtitan/observability/sdc_replayer.md#SDCReplayMismatch.rank), [`replay`](../../torchtitan/observability/sdc_replayer.md#SDCReplayMismatch.replay), [`step`](../../torchtitan/observability/sdc_replayer.md#SDCReplayMismatch.step)  (1 test-only)
- used by: [`Trainer`](../../torchtitan/trainer.md#Trainer), [`train_step`](../../torchtitan/trainer.md#Trainer.train_step), [`forward_backward_step`](../../torchtitan/trainer.md#Trainer.forward_backward_step)  (1 test-only)

### <a id="SDCReplayMismatchTrainer.Config"></a>`SDCReplayMismatchTrainer.Config`  ·  implements/extends Config
- def: [`torchtitan_recipes/tests/features.py:44`](../../../../../../raw/code/torchtitan/torchtitan_recipes/tests/features.py#L44)
- signature: `class Config(Trainer.Config):`
- uses (calls/refs, reference-scoped): [`Trainer`](../../torchtitan/trainer.md#Trainer), [`Config`](../../torchtitan/trainer.md#Trainer.Config)
- used by: (2 test-only callers)

## Functions
- <a id="deepseek_v3_debugmodel_fused_grouped_experts_tp2_ep4"></a>`deepseek_v3_debugmodel_fused_grouped_experts_tp2_ep4()` — [`L507`](../../../../../../raw/code/torchtitan/torchtitan_recipes/tests/features.py#L507)
- <a id="deepseek_v3_debugmodel_sdc_replay_mismatch"></a>`deepseek_v3_debugmodel_sdc_replay_mismatch()` — [`L99`](../../../../../../raw/code/torchtitan/torchtitan_recipes/tests/features.py#L99)
- <a id="llama3_debugmodel_ce_loss_tp2"></a>`llama3_debugmodel_ce_loss_tp2()` — [`L155`](../../../../../../raw/code/torchtitan/torchtitan_recipes/tests/features.py#L155)
- <a id="llama3_debugmodel_compile"></a>`llama3_debugmodel_compile()` — [`L135`](../../../../../../raw/code/torchtitan/torchtitan_recipes/tests/features.py#L135)
- <a id="llama3_debugmodel_compile_sac_op"></a>`llama3_debugmodel_compile_sac_op()` — [`L142`](../../../../../../raw/code/torchtitan/torchtitan_recipes/tests/features.py#L142)
- <a id="llama3_debugmodel_cp4"></a>`llama3_debugmodel_cp4()` — [`L379`](../../../../../../raw/code/torchtitan/torchtitan_recipes/tests/features.py#L379)
- <a id="llama3_debugmodel_ddp2_cp2"></a>`llama3_debugmodel_ddp2_cp2()` — [`L419`](../../../../../../raw/code/torchtitan/torchtitan_recipes/tests/features.py#L419)
- <a id="llama3_debugmodel_ddp4"></a>`llama3_debugmodel_ddp4()` — [`L363`](../../../../../../raw/code/torchtitan/torchtitan_recipes/tests/features.py#L363)
- <a id="llama3_debugmodel_default"></a>`llama3_debugmodel_default()` — [`L127`](../../../../../../raw/code/torchtitan/torchtitan_recipes/tests/features.py#L127)
- <a id="llama3_debugmodel_float8_emulate_lora_tp2_pp2"></a>`llama3_debugmodel_float8_emulate_lora_tp2_pp2()` — [`L528`](../../../../../../raw/code/torchtitan/torchtitan_recipes/tests/features.py#L528)
- <a id="llama3_debugmodel_fsdp2_cp2"></a>`llama3_debugmodel_fsdp2_cp2()` — [`L408`](../../../../../../raw/code/torchtitan/torchtitan_recipes/tests/features.py#L408)
- <a id="llama3_debugmodel_fsdp2_pp2_1f1b"></a>`llama3_debugmodel_fsdp2_pp2_1f1b()` — [`L247`](../../../../../../raw/code/torchtitan/torchtitan_recipes/tests/features.py#L247)
- <a id="llama3_debugmodel_fsdp2_pp2_1f1b_layers_per_stage"></a>`llama3_debugmodel_fsdp2_pp2_1f1b_layers_per_stage()` — [`L258`](../../../../../../raw/code/torchtitan/torchtitan_recipes/tests/features.py#L258)
- <a id="llama3_debugmodel_fsdp2_tp2_cp2"></a>`llama3_debugmodel_fsdp2_tp2_cp2()` — [`L441`](../../../../../../raw/code/torchtitan/torchtitan_recipes/tests/features.py#L441)
- <a id="llama3_debugmodel_fsdp2_tp2_pp2_compile"></a>`llama3_debugmodel_fsdp2_tp2_pp2_compile()` — [`L295`](../../../../../../raw/code/torchtitan/torchtitan_recipes/tests/features.py#L295)
- <a id="llama3_debugmodel_fsdp2_tp2_pp2_load"></a>`llama3_debugmodel_fsdp2_tp2_pp2_load()` — [`L289`](../../../../../../raw/code/torchtitan/torchtitan_recipes/tests/features.py#L289)
- <a id="llama3_debugmodel_fsdp2_tp2_pp2_save"></a>`llama3_debugmodel_fsdp2_tp2_pp2_save()` — [`L276`](../../../../../../raw/code/torchtitan/torchtitan_recipes/tests/features.py#L276)
- <a id="llama3_debugmodel_fsdp_reshard_always"></a>`llama3_debugmodel_fsdp_reshard_always()` — [`L447`](../../../../../../raw/code/torchtitan/torchtitan_recipes/tests/features.py#L447)
- <a id="llama3_debugmodel_full_checkpoint_load"></a>`llama3_debugmodel_full_checkpoint_load()` — [`L188`](../../../../../../raw/code/torchtitan/torchtitan_recipes/tests/features.py#L188)
- <a id="llama3_debugmodel_full_checkpoint_save"></a>`llama3_debugmodel_full_checkpoint_save()` — [`L181`](../../../../../../raw/code/torchtitan/torchtitan_recipes/tests/features.py#L181)
- <a id="llama3_debugmodel_fused_swiglu_tp2"></a>`llama3_debugmodel_fused_swiglu_tp2()` — [`L499`](../../../../../../raw/code/torchtitan/torchtitan_recipes/tests/features.py#L499)
- <a id="llama3_debugmodel_gradient_accumulation"></a>`llama3_debugmodel_gradient_accumulation()` — [`L474`](../../../../../../raw/code/torchtitan/torchtitan_recipes/tests/features.py#L474) — Two gradient accumulation steps on 2 GPUs.
- <a id="llama3_debugmodel_hf_checkpoint_load"></a>`llama3_debugmodel_hf_checkpoint_load()` — [`L202`](../../../../../../raw/code/torchtitan/torchtitan_recipes/tests/features.py#L202) — Loads what ``llama3_debugmodel_hf_checkpoint_save`` wrote.
- <a id="llama3_debugmodel_hf_checkpoint_save"></a>`llama3_debugmodel_hf_checkpoint_save()` — [`L194`](../../../../../../raw/code/torchtitan/torchtitan_recipes/tests/features.py#L194)
- <a id="llama3_debugmodel_hsdp2x2"></a>`llama3_debugmodel_hsdp2x2()` — [`L371`](../../../../../../raw/code/torchtitan/torchtitan_recipes/tests/features.py#L371)
- <a id="llama3_debugmodel_hsdp2x2_cp2"></a>`llama3_debugmodel_hsdp2x2_cp2()` — [`L431`](../../../../../../raw/code/torchtitan/torchtitan_recipes/tests/features.py#L431)
- <a id="llama3_debugmodel_hsdp2x2_tp2"></a>`llama3_debugmodel_hsdp2x2_tp2()` — [`L402`](../../../../../../raw/code/torchtitan/torchtitan_recipes/tests/features.py#L402)
- <a id="llama3_debugmodel_last_save_model_only_bf16"></a>`llama3_debugmodel_last_save_model_only_bf16()` — [`L224`](../../../../../../raw/code/torchtitan/torchtitan_recipes/tests/features.py#L224)
- <a id="llama3_debugmodel_optimizer_bf16_states"></a>`llama3_debugmodel_optimizer_bf16_states()` — [`L356`](../../../../../../raw/code/torchtitan/torchtitan_recipes/tests/features.py#L356)
- <a id="llama3_debugmodel_optional_checkpoint_load_tp2"></a>`llama3_debugmodel_optional_checkpoint_load_tp2()` — [`L461`](../../../../../../raw/code/torchtitan/torchtitan_recipes/tests/features.py#L461) — Loads a ``[dp:4]`` checkpoint at ``[dp:2, tp:2]``.
- <a id="llama3_debugmodel_optional_checkpoint_save"></a>`llama3_debugmodel_optional_checkpoint_save()` — [`L454`](../../../../../../raw/code/torchtitan/torchtitan_recipes/tests/features.py#L454)
- <a id="llama3_debugmodel_pp2_1f1b"></a>`llama3_debugmodel_pp2_1f1b()` — [`L231`](../../../../../../raw/code/torchtitan/torchtitan_recipes/tests/features.py#L231) — PP-only, so it leaves SPMD type checking off.
- <a id="llama3_debugmodel_pp2_custom_csv"></a>`llama3_debugmodel_pp2_custom_csv()` — [`L342`](../../../../../../raw/code/torchtitan/torchtitan_recipes/tests/features.py#L342)
- <a id="llama3_debugmodel_pp2_zbv"></a>`llama3_debugmodel_pp2_zbv()` — [`L331`](../../../../../../raw/code/torchtitan/torchtitan_recipes/tests/features.py#L331)
- <a id="llama3_debugmodel_pp4_interleaved_1f1b"></a>`llama3_debugmodel_pp4_interleaved_1f1b()` — [`L308`](../../../../../../raw/code/torchtitan/torchtitan_recipes/tests/features.py#L308) — PP-only; see ``llama3_debugmodel_pp2_1f1b`` for why type checking is off.
- <a id="llama3_debugmodel_pp4_interleaved_1f1b_layers_per_stage"></a>`llama3_debugmodel_pp4_interleaved_1f1b_layers_per_stage()` — [`L318`](../../../../../../raw/code/torchtitan/torchtitan_recipes/tests/features.py#L318)
- <a id="llama3_debugmodel_pp4_zero_bubble"></a>`llama3_debugmodel_pp4_zero_bubble()` — [`L324`](../../../../../../raw/code/torchtitan/torchtitan_recipes/tests/features.py#L324)
- <a id="llama3_debugmodel_sdc_replay_cudagraph"></a>`llama3_debugmodel_sdc_replay_cudagraph()` — [`L118`](../../../../../../raw/code/torchtitan/torchtitan_recipes/tests/features.py#L118)
- <a id="llama3_debugmodel_seed_checkpoint"></a>`llama3_debugmodel_seed_checkpoint()` — [`L545`](../../../../../../raw/code/torchtitan/torchtitan_recipes/tests/features.py#L545)
- <a id="llama3_debugmodel_sft"></a>`llama3_debugmodel_sft()` — [`L539`](../../../../../../raw/code/torchtitan/torchtitan_recipes/tests/features.py#L539)
- <a id="llama3_debugmodel_tp2"></a>`llama3_debugmodel_tp2()` — [`L148`](../../../../../../raw/code/torchtitan/torchtitan_recipes/tests/features.py#L148)
- <a id="llama3_debugmodel_tp2_asynctp_compile_spmd_types"></a>`llama3_debugmodel_tp2_asynctp_compile_spmd_types()` — [`L175`](../../../../../../raw/code/torchtitan/torchtitan_recipes/tests/features.py#L175)
- <a id="llama3_debugmodel_tp2_compile"></a>`llama3_debugmodel_tp2_compile()` — [`L169`](../../../../../../raw/code/torchtitan/torchtitan_recipes/tests/features.py#L169)
- <a id="llama3_debugmodel_tp2_no_sp"></a>`llama3_debugmodel_tp2_no_sp()` — [`L163`](../../../../../../raw/code/torchtitan/torchtitan_recipes/tests/features.py#L163)
- <a id="llama3_debugmodel_tp2_pp2_gpipe"></a>`llama3_debugmodel_tp2_pp2_gpipe()` — [`L264`](../../../../../../raw/code/torchtitan/torchtitan_recipes/tests/features.py#L264)
- <a id="llama3_debugmodel_ulysses_cp2"></a>`llama3_debugmodel_ulysses_cp2()` — [`L389`](../../../../../../raw/code/torchtitan/torchtitan_recipes/tests/features.py#L389) — Attention reshards the CP axis onto the head dimension.
- <a id="llama3_debugmodel_validation_tp2_cp2_pp2"></a>`llama3_debugmodel_validation_tp2_cp2_pp2()` — [`L483`](../../../../../../raw/code/torchtitan/torchtitan_recipes/tests/features.py#L483)
- <a id="llama3_debugmodel_varlen_attn_fsdp4_sac"></a>`llama3_debugmodel_varlen_attn_fsdp4_sac()` — [`L520`](../../../../../../raw/code/torchtitan/torchtitan_recipes/tests/features.py#L520)

