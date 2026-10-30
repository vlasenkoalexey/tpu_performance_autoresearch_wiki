---
title: 'Module: torchtitan/experiments/jax/jax_job_config.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/jax/jax_job_config.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.jax.jax_job_config`/
symbols:
  JaxJobConfig: JaxJobConfig#
  JaxConfig: JaxConfig#
  JaxConfig.use_scan: JaxConfig#use_scan.
  JaxJobConfig.jax_config: JaxJobConfig#jax_config.
  JaxConfig.tpu_megacore: JaxConfig#tpu_megacore.
  JaxConfig.tpu_num_slices: JaxConfig#tpu_num_slices.
  JaxConfig.model_layer_override: JaxConfig#model_layer_override.
  JaxConfig.adamw_bf16_state: JaxConfig#adamw_bf16_state.
---
# Module: [`torchtitan/experiments/jax/jax_job_config.py`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/jax_job_config.py)

## Classes
### <a id="JaxConfig"></a>`JaxConfig`
- def: [`torchtitan/experiments/jax/jax_job_config.py:9`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/jax_job_config.py#L9) — documented in [jax-lane](../../../../concepts/jax-lane.md)
- doc: Runtime knobs specific to the pure-JAX / Flax NNX trainer.
- signature: `class JaxConfig:`
- members:
  - <a id="JaxConfig.adamw_bf16_state"></a>`adamw_bf16_state` — [`L23`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/jax_job_config.py#L23)
  - <a id="JaxConfig.model_layer_override"></a>`model_layer_override` — [`L16`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/jax_job_config.py#L16)
  - <a id="JaxConfig.tpu_megacore"></a>`tpu_megacore` — [`L14`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/jax_job_config.py#L14)
  - <a id="JaxConfig.tpu_num_slices"></a>`tpu_num_slices` — [`L15`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/jax_job_config.py#L15)
  - <a id="JaxConfig.use_scan"></a>`use_scan` — [`L13`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/jax_job_config.py#L13)
- used by: [`llama3_debugmodel`](llama3/config_registry.md#llama3_debugmodel), [`JaxJobConfig`](jax_job_config.md#JaxJobConfig)

### <a id="JaxJobConfig"></a>`JaxJobConfig`  ·  implements/extends BaseTPUTrainerConfig
- def: [`torchtitan/experiments/jax/jax_job_config.py:27`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/jax_job_config.py#L27) — documented in [jax-lane](../../../../concepts/jax-lane.md)
- signature: `class JaxJobConfig(BaseTPUTrainerConfig):`
- members:
  - <a id="JaxJobConfig.jax_config"></a>`jax_config` — [`L28`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/jax_job_config.py#L28)
- uses (calls/refs, reference-scoped): [`BaseTPUTrainerConfig`](../tpu/tpu_job_config.md#BaseTPUTrainerConfig), [`JaxConfig`](jax_job_config.md#JaxConfig)
- used by: [`llama3_debugmodel`](llama3/config_registry.md#llama3_debugmodel), [`BaseTPUTrainerConfig`](../tpu/tpu_job_config.md#BaseTPUTrainerConfig), [`main`](train_minimal.md#main)  (1 test-only)

