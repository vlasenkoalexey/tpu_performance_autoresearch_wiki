---
title: 'Module: torchtitan/experiments/jax/trainer.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/jax/trainer.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.jax.trainer`/
symbols:
  JaxTrainer.train: JaxTrainer#train().
  JaxTrainer.setup_model: JaxTrainer#setup_model().
  logger: logger.
  _scale_by_adam_bf16_state.update_fn: _scale_by_adam_bf16_state().update_fn().
  JaxTrainer.setup_dataloader: JaxTrainer#setup_dataloader().
  _scale_by_adam_bf16_state: _scale_by_adam_bf16_state().
  JaxTrainer.setup_optimizer: JaxTrainer#setup_optimizer().
  JaxTrainer.mesh: JaxTrainer#mesh.
  JaxTrainer.train_step: JaxTrainer#train_step().
  JaxTrainer.num_global_devices: JaxTrainer#num_global_devices.
  JaxTrainer.num_local_devices: JaxTrainer#num_local_devices.
  _scale_by_adam_bf16_state.init_fn: _scale_by_adam_bf16_state().init_fn().
  _scale_by_adam_bf16_state.update_fn._mu: _scale_by_adam_bf16_state().update_fn()._mu().
  _scale_by_adam_bf16_state.update_fn._nu: _scale_by_adam_bf16_state().update_fn()._nu().
  _scale_by_adam_bf16_state.update_fn._upd: _scale_by_adam_bf16_state().update_fn()._upd().
  JaxTrainer: JaxTrainer#
  JaxTrainer.job_config: JaxTrainer#job_config.
  JaxTrainer.accelerator: JaxTrainer#accelerator.
  JaxTrainer.loss_fn: JaxTrainer#loss_fn().
  P: P.
  JaxTrainer.__init__: JaxTrainer#__init__().
  JaxTrainer.model_args: JaxTrainer#model_args.
---
# Module: [`torchtitan/experiments/jax/trainer.py`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/trainer.py)

## Classes
### <a id="JaxTrainer"></a>`JaxTrainer`
- def: [`torchtitan/experiments/jax/trainer.py:91`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/trainer.py#L91) — documented in [jax-lane](../../../../concepts/jax-lane.md)
- signature: `class JaxTrainer:`
- members:
  - <a id="JaxTrainer.loss_fn"></a>`loss_fn(model)` — [`L348`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/trainer.py#L348)
  - <a id="JaxTrainer.setup_dataloader"></a>`setup_dataloader(self, job_config)` — [`L111`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/trainer.py#L111) — Build a dataloader that returns (inputs, labels) numpy arrays.
  - <a id="JaxTrainer.setup_model"></a>`setup_model(self, job_config)` — [`L165`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/trainer.py#L165) — Instantiate and shard the Flax NNX model. — documented in [jax-lane](../../../../concepts/jax-lane.md)
  - <a id="JaxTrainer.setup_optimizer"></a>`setup_optimizer(self, job_config, model)` — [`L268`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/trainer.py#L268)
  - <a id="JaxTrainer.train"></a>`train(self)` — [`L321`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/trainer.py#L321) — documented in [jax-lane](../../../../concepts/jax-lane.md)
  - <a id="JaxTrainer.train_step"></a>`train_step(model, optimizer: nnx.Optimizer, inputs, labels)` — [`L347`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/trainer.py#L347) — documented in [trainer-and-train-loop](../../../../concepts/trainer-and-train-loop.md)
  - <a id="JaxTrainer.accelerator"></a>`accelerator` — [`L103`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/trainer.py#L103)
  - <a id="JaxTrainer.job_config"></a>`job_config` — [`L102`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/trainer.py#L102)
  - <a id="JaxTrainer.mesh"></a>`mesh` — [`L101`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/trainer.py#L101)
  - <a id="JaxTrainer.model_args"></a>`model_args` — [`L261`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/trainer.py#L261)
  - <a id="JaxTrainer.num_global_devices"></a>`num_global_devices` — [`L104`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/trainer.py#L104)
  - <a id="JaxTrainer.num_local_devices"></a>`num_local_devices` — [`L105`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/trainer.py#L105)
- protocol/private: <a id="JaxTrainer.__init__"></a>`__init__`[`L93`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/trainer.py#L93)
- uses (calls/refs, reference-scoped): [`SelectiveAC`](../../distributed/activation_checkpoint.md#SelectiveAC), [`Config`](../../distributed/activation_checkpoint.md#SelectiveAC.Config), [`FullAC`](../../distributed/activation_checkpoint.md#FullAC), [`Config`](../../distributed/activation_checkpoint.md#FullAC.Config), [`maybe_enable_profiling`](jax_profiling.md#maybe_enable_profiling), [`logger`](trainer.md#logger), [`args`](llama3/__init__.md#args), [`make_splash_attention_fn`](splash_attn.md#make_splash_attention_fn), [`step`](jax_profiling.md#maybe_enable_profiling.JaxProfiler.step), [`shard_input`](distributed.md#shard_input), [`sharding_map_original`](llama3/sharding.md#sharding_map_original), [`_scale_by_adam_bf16_state`](trainer.md#_scale_by_adam_bf16_state), [`sharding_map_scan`](llama3/sharding.md#sharding_map_scan), [`num_flops_per_token`](metrics.md#JaxMetricsProcessor.num_flops_per_token), [`apply_sharding_to_state`](distributed.md#apply_sharding_to_state), [`log`](metrics.md#JaxMetricsProcessor.log), [`should_log`](metrics.md#JaxMetricsProcessor.should_log), [`data_loading_times`](metrics.md#JaxMetricsProcessor.data_loading_times), [`ntokens_since_last_log`](metrics.md#JaxMetricsProcessor.ntokens_since_last_log), [`Transformer`](llama3/model.md#Transformer), [`max_seq_len`](llama3/model.md#ModelArgs.max_seq_len), [`JaxMetricsProcessor`](metrics.md#JaxMetricsProcessor), [`fake_dataloader`](data_utils.md#fake_dataloader), [`torch_loader_to_jax`](data_utils.md#torch_loader_to_jax)
- used by: [`main_train_loop`](train_minimal.md#main_train_loop)

## Functions
- <a id="_scale_by_adam_bf16_state.update_fn._mu"></a>`_mu(g, m)` — [`L60`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/trainer.py#L60)
- <a id="_scale_by_adam_bf16_state.update_fn._nu"></a>`_nu(g, n)` — [`L66`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/trainer.py#L66)
- <a id="_scale_by_adam_bf16_state"></a>`_scale_by_adam_bf16_state(b1, b2, eps)` — [`L37`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/trainer.py#L37) — Adam with mu and nu stored in bf16; math runs in fp32 per-leaf.
- <a id="_scale_by_adam_bf16_state.update_fn._upd"></a>`_upd(g, m, n)` — [`L73`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/trainer.py#L73)
- <a id="_scale_by_adam_bf16_state.init_fn"></a>`init_fn(params)` — [`L49`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/trainer.py#L49)
- <a id="_scale_by_adam_bf16_state.update_fn"></a>`update_fn(updates, state, params=None)` — [`L54`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/trainer.py#L54)

## Module values
- <a id="P"></a>`P` — [`L34`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/trainer.py#L34)
- <a id="logger"></a>`logger` — [`L32`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/trainer.py#L32)

