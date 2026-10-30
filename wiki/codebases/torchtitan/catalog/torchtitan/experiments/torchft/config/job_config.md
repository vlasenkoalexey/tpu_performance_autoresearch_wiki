---
title: 'Module: torchtitan/experiments/torchft/config/job_config.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/torchft/config/job_config.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.torchft.config.job_config`/
symbols:
  FaultTolerance: FaultTolerance#
  FaultTolerantModelSpec: FaultTolerantModelSpec#
  FaultTolerance.num_fragments: FaultTolerance#num_fragments.
  JobConfig: JobConfig#
  FaultTolerance.sync_steps: FaultTolerance#sync_steps.
  FaultTolerance.should_quantize: FaultTolerance#should_quantize.
  FaultTolerance.fragment_sync_delay: FaultTolerance#fragment_sync_delay.
  FaultTolerance.fragment_update_alpha: FaultTolerance#fragment_update_alpha.
  FaultTolerance.module_fqns_per_model_fragment: FaultTolerance#module_fqns_per_model_fragment.
  FaultTolerantModelSpec.fragment_fn: FaultTolerantModelSpec#fragment_fn.
  JobConfig.fault_tolerance: JobConfig#fault_tolerance.
---
# Module: [`torchtitan/experiments/torchft/config/job_config.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/config/job_config.py)

## Classes
### <a id="FaultTolerance"></a>`FaultTolerance`  ·  implements/extends Config
- def: [`torchtitan/experiments/torchft/config/job_config.py:15`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/config/job_config.py#L15)
- doc: Extends TorchFTManager.Config to also support Streaming DiLoCo
- signature: `class FaultTolerance(TorchFTManager.Config):`
- members:
  - <a id="FaultTolerance.fragment_sync_delay"></a>`fragment_sync_delay` — [`L38`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/config/job_config.py#L38) — ---
  - <a id="FaultTolerance.fragment_update_alpha"></a>`fragment_update_alpha` — [`L52`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/config/job_config.py#L52) — ---
  - <a id="FaultTolerance.module_fqns_per_model_fragment"></a>`module_fqns_per_model_fragment` — [`L63`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/config/job_config.py#L63) — ---
  - <a id="FaultTolerance.num_fragments"></a>`num_fragments` — [`L72`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/config/job_config.py#L72) — ---
  - <a id="FaultTolerance.should_quantize"></a>`should_quantize` — [`L26`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/config/job_config.py#L26) — ---
  - <a id="FaultTolerance.sync_steps"></a>`sync_steps` — [`L20`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/config/job_config.py#L20) — ---
- uses (calls/refs, reference-scoped): [`TorchFTManager`](../manager.md#TorchFTManager), [`Config`](../manager.md#TorchFTManager.Config)
- used by: [`llama3_torchft_debugmodel`](../llama3/config_registry.md#llama3_torchft_debugmodel), [`maybe_semi_sync_training`](../manager.md#maybe_semi_sync_training), [`fragment_llm`](../diloco/utils.md#fragment_llm), [`fault_tolerance`](../trainer.md#FaultTolerantTrainer.Config.fault_tolerance), [`JobConfig`](job_config.md#JobConfig)

### <a id="FaultTolerantModelSpec"></a>`FaultTolerantModelSpec`  ·  implements/extends ModelSpec
- def: [`torchtitan/experiments/torchft/config/job_config.py:81`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/config/job_config.py#L81)
- signature: `class FaultTolerantModelSpec(ModelSpec):`
- members:
  - <a id="FaultTolerantModelSpec.fragment_fn"></a>`fragment_fn` — [`L82`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/config/job_config.py#L82)
- uses (calls/refs, reference-scoped): [`ModelSpec`](../../../protocols/model_spec.md#ModelSpec)
- used by: [`ModelSpec`](../../../protocols/model_spec.md#ModelSpec), [`model_registry`](../llama3/__init__.md#model_registry)

### <a id="JobConfig"></a>`JobConfig`
- def: [`torchtitan/experiments/torchft/config/job_config.py:86`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/config/job_config.py#L86)
- signature: `class JobConfig:`
- members:
  - <a id="JobConfig.fault_tolerance"></a>`fault_tolerance` — [`L87`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/config/job_config.py#L87)
- uses (calls/refs, reference-scoped): [`FaultTolerance`](job_config.md#FaultTolerance)

