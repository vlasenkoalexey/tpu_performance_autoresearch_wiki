---
title: 'Module: src/vllm_torchtpu/platforms/pcp_validation.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/platforms/pcp_validation.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.platforms.pcp_validation`/
symbols:
  PcpStaticSupportValidator.validate_platform_config: PcpStaticSupportValidator#validate_platform_config().
  PcpStaticSupportValidator.from_vllm_config: PcpStaticSupportValidator#from_vllm_config().
  PcpStaticConfig.enabled: PcpStaticConfig#enabled().
  PcpStaticSupportValidator: PcpStaticSupportValidator#
  PcpStaticConfig.pcp_size: PcpStaticConfig#pcp_size.
  PcpStaticConfig.interleave_size: PcpStaticConfig#interleave_size.
  PcpStaticConfig: PcpStaticConfig#
  PcpStaticConfig.speculative_method: PcpStaticConfig#speculative_method.
  PcpStaticConfig.dcp_size: PcpStaticConfig#dcp_size.
  PcpStaticConfig.speculative_enabled: PcpStaticConfig#speculative_enabled.
  PcpStaticConfig.num_speculative_tokens: PcpStaticConfig#num_speculative_tokens.
  PcpStaticConfig.is_moe: PcpStaticConfig#is_moe.
  PcpStaticConfig.expert_parallel: PcpStaticConfig#expert_parallel.
  PcpStaticConfig.pipeline_parallel_size: PcpStaticConfig#pipeline_parallel_size.
  PcpStaticConfig.async_scheduling: PcpStaticConfig#async_scheduling.
---
# Module: [`src/vllm_torchtpu/platforms/pcp_validation.py`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/pcp_validation.py)

## Classes
### <a id="PcpStaticConfig"></a>`PcpStaticConfig`
- def: [`src/vllm_torchtpu/platforms/pcp_validation.py:20`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/pcp_validation.py#L20) — documented in [tpu-platform](../../../../concepts/tpu-platform.md)
- signature: `class PcpStaticConfig:`
- members:
  - <a id="PcpStaticConfig.enabled"></a>`enabled(self)` — [`L33`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/pcp_validation.py#L33) — documented in [tpu-platform](../../../../concepts/tpu-platform.md)
  - <a id="PcpStaticConfig.async_scheduling"></a>`async_scheduling` — [`L25`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/pcp_validation.py#L25) — documented in [tpu-platform](../../../../concepts/tpu-platform.md)
  - <a id="PcpStaticConfig.dcp_size"></a>`dcp_size` — [`L23`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/pcp_validation.py#L23) — documented in [tpu-platform](../../../../concepts/tpu-platform.md)
  - <a id="PcpStaticConfig.expert_parallel"></a>`expert_parallel` — [`L30`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/pcp_validation.py#L30) — documented in [tpu-platform](../../../../concepts/tpu-platform.md)
  - <a id="PcpStaticConfig.interleave_size"></a>`interleave_size` — [`L22`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/pcp_validation.py#L22) — documented in [tpu-platform](../../../../concepts/tpu-platform.md)
  - <a id="PcpStaticConfig.is_moe"></a>`is_moe` — [`L29`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/pcp_validation.py#L29) — documented in [tpu-platform](../../../../concepts/tpu-platform.md)
  - <a id="PcpStaticConfig.num_speculative_tokens"></a>`num_speculative_tokens` — [`L28`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/pcp_validation.py#L28) — documented in [tpu-platform](../../../../concepts/tpu-platform.md)
  - <a id="PcpStaticConfig.pcp_size"></a>`pcp_size` — [`L21`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/pcp_validation.py#L21) — documented in [tpu-platform](../../../../concepts/tpu-platform.md)
  - <a id="PcpStaticConfig.pipeline_parallel_size"></a>`pipeline_parallel_size` — [`L24`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/pcp_validation.py#L24) — documented in [tpu-platform](../../../../concepts/tpu-platform.md)
  - <a id="PcpStaticConfig.speculative_enabled"></a>`speculative_enabled` — [`L26`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/pcp_validation.py#L26) — documented in [tpu-platform](../../../../concepts/tpu-platform.md)
  - <a id="PcpStaticConfig.speculative_method"></a>`speculative_method` — [`L27`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/pcp_validation.py#L27) — documented in [tpu-platform](../../../../concepts/tpu-platform.md)
- used by: [`check_and_update_config`](tpu_platform.md#TpuPlatform.check_and_update_config), [`validate_platform_config`](pcp_validation.md#PcpStaticSupportValidator.validate_platform_config), [`from_vllm_config`](pcp_validation.md#PcpStaticSupportValidator.from_vllm_config), [`_validate_kv_sharing_supported`](../spec_decode/eagle3.md#Eagle3Proposer._validate_kv_sharing_supported), [`_pcp_enabled`](../runner/tpu_runner.md#TPUModelRunner._pcp_enabled), [`_mtp_enabled`](../runner/tpu_runner.md#TPUModelRunner._mtp_enabled)

### <a id="PcpStaticSupportValidator"></a>`PcpStaticSupportValidator`
- def: [`src/vllm_torchtpu/platforms/pcp_validation.py:37`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/pcp_validation.py#L37) — documented in [tpu-platform](../../../../concepts/tpu-platform.md)
- signature: `class PcpStaticSupportValidator:`
- members:
  - <a id="PcpStaticSupportValidator.from_vllm_config"></a>`from_vllm_config(vllm_config: Any)` — [`L39`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/pcp_validation.py#L39) — documented in [tpu-platform](../../../../concepts/tpu-platform.md)
  - <a id="PcpStaticSupportValidator.validate_platform_config"></a>`validate_platform_config(vllm_config: Any, *, kv_cache_layout: str)` — [`L78`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/pcp_validation.py#L78) — documented in [tpu-platform](../../../../concepts/tpu-platform.md)
- uses (calls/refs, reference-scoped): [`enabled`](pcp_validation.md#PcpStaticConfig.enabled), [`interleave_size`](pcp_validation.md#PcpStaticConfig.interleave_size), [`pcp_size`](pcp_validation.md#PcpStaticConfig.pcp_size), [`PcpStaticConfig`](pcp_validation.md#PcpStaticConfig), [`speculative_method`](pcp_validation.md#PcpStaticConfig.speculative_method), [`dcp_size`](pcp_validation.md#PcpStaticConfig.dcp_size), [`expert_parallel`](pcp_validation.md#PcpStaticConfig.expert_parallel), [`is_moe`](pcp_validation.md#PcpStaticConfig.is_moe), [`num_speculative_tokens`](pcp_validation.md#PcpStaticConfig.num_speculative_tokens), [`speculative_enabled`](pcp_validation.md#PcpStaticConfig.speculative_enabled), [`async_scheduling`](pcp_validation.md#PcpStaticConfig.async_scheduling), [`pipeline_parallel_size`](pcp_validation.md#PcpStaticConfig.pipeline_parallel_size)
- used by: [`check_and_update_config`](tpu_platform.md#TpuPlatform.check_and_update_config), [`_validate_kv_sharing_supported`](../spec_decode/eagle3.md#Eagle3Proposer._validate_kv_sharing_supported), [`_profiler_world_size`](../runner/tpu_runner.md#TPUModelRunner._profiler_world_size)

