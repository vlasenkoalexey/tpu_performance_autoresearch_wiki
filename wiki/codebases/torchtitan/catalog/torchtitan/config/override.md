---
title: 'Module: torchtitan/config/override.py'
type: catalog
provenance: extracted
module: torchtitan/config/override.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.config.override`/
symbols:
  apply_overrides: apply_overrides().
  OverrideConfig.imports: OverrideConfig#imports.
  derive: derive().
  _collect_claims: _collect_claims().
  override: override().
  OverrideConfig: OverrideConfig#
  override.decorator: override().decorator().
  _check_node_conflicts: _check_node_conflicts().
  Override.name: Override#name().
  _Claim.ov: _Claim#ov.
  Override.target_cls: Override#target_cls.
  Override.factory: Override#factory.
  _Claim.fqn: _Claim#fqn.
  _Claim.cfg: _Claim#cfg.
  Override: Override#
  _REGISTRY._REGISTRY: _REGISTRY._REGISTRY.
  OverrideImport: OverrideImport.
  _resolve_active: _resolve_active().
  _Claim.attr: _Claim#attr.
  _Claim.parent: _Claim#parent.
  parse_cli_imports: parse_cli_imports().
  format_cli_imports: format_cli_imports().
  _Claim: _Claim#
  _Claim.kwargs: _Claim#kwargs.
  Override.matches: Override#matches().
  clear_overrides: clear_overrides().
  _ConfigT: _ConfigT.
  Override.fqns: Override#fqns.
  Override.origin_module: Override#origin_module.
  Override.exact: Override#exact.
  Override.description: Override#description.
  _resolve_target: _resolve_target().
---
# Module: [`torchtitan/config/override.py`](../../../../../../raw/code/torchtitan/torchtitan/config/override.py)

## Classes
### <a id="Override"></a>`Override`
- def: [`torchtitan/config/override.py:137`](../../../../../../raw/code/torchtitan/torchtitan/config/override.py#L137)
- doc: A single registered override.
- signature: `class Override:`
- members:
  - <a id="Override.matches"></a>`matches(self, fqn: str)` — [`L160`](../../../../../../raw/code/torchtitan/torchtitan/config/override.py#L160) — Whether this override claims the node at ``fqn``.
  - <a id="Override.name"></a>`name(self)` — [`L156`](../../../../../../raw/code/torchtitan/torchtitan/config/override.py#L156) — Unique identifier: the factory's import path (``module.function``).
  - <a id="Override.description"></a>`description` — [`L151`](../../../../../../raw/code/torchtitan/torchtitan/config/override.py#L151)
  - <a id="Override.exact"></a>`exact` — [`L153`](../../../../../../raw/code/torchtitan/torchtitan/config/override.py#L153)
  - <a id="Override.factory"></a>`factory` — [`L149`](../../../../../../raw/code/torchtitan/torchtitan/config/override.py#L149)
  - <a id="Override.fqns"></a>`fqns` — [`L150`](../../../../../../raw/code/torchtitan/torchtitan/config/override.py#L150)
  - <a id="Override.origin_module"></a>`origin_module` — [`L152`](../../../../../../raw/code/torchtitan/torchtitan/config/override.py#L152)
  - <a id="Override.target_cls"></a>`target_cls` — [`L148`](../../../../../../raw/code/torchtitan/torchtitan/config/override.py#L148) — ---
- uses (calls/refs, reference-scoped): [`Configurable`](configurable.md#Configurable), [`Config`](configurable.md#Configurable.Config)
- used by: [`TORCH_DTYPE_MAP`](__init__.md#TORCH_DTYPE_MAP), [`apply_overrides`](override.md#apply_overrides), [`_collect_claims`](override.md#_collect_claims), [`decorator`](override.md#override.decorator), [`_check_node_conflicts`](override.md#_check_node_conflicts), [`ov`](override.md#_Claim.ov), [`_REGISTRY`](override.md#_REGISTRY._REGISTRY), [`_resolve_active`](override.md#_resolve_active)

### <a id="OverrideConfig"></a>`OverrideConfig`
- def: [`torchtitan/config/override.py:61`](../../../../../../raw/code/torchtitan/torchtitan/config/override.py#L61) — documented in [job-config](../../../concepts/job-config.md)
- signature: `class OverrideConfig:`
- members:
  - <a id="OverrideConfig.imports"></a>`imports` — [`L62`](../../../../../../raw/code/torchtitan/torchtitan/config/override.py#L62) — --- — documented in [job-config](../../../concepts/job-config.md)
- uses (calls/refs, reference-scoped): [`OverrideImport`](override.md#OverrideImport)
- used by: [`sft_llama3_8b_metamath`](../experiments/tpu/llama3/config_registry.md#sft_llama3_8b_metamath), [`llama3_70b`](../experiments/tpu/llama3/config_registry.md#llama3_70b), [`llama3_405b`](../experiments/tpu/llama3/config_registry.md#llama3_405b), [`llama3_8b`](../experiments/tpu/llama3/config_registry.md#llama3_8b), [`__init__`](../experiments/torchft/trainer.md#FaultTolerantTrainer.__init__), [`transfer_stream`](../trainer.md#Trainer.transfer_stream), [`TORCH_DTYPE_MAP`](__init__.md#TORCH_DTYPE_MAP), [`qwen3_moe_235b_scan`](../experiments/tpu/qwen3/config_registry.md#qwen3_moe_235b_scan), [`llama3_debugmodel`](../experiments/tpu/llama3/config_registry.md#llama3_debugmodel), [`llama3_1b`](../experiments/tpu/llama3/config_registry.md#llama3_1b), [`apply_overrides`](override.md#apply_overrides), [`_build_model`](../experiments/rl/actors/trainer.md#PolicyTrainer._build_model), [`_build_model`](../experiments/tpu/rl_nc_ray/trainer.md#RayTPUPolicyTrainer._build_model), [`override`](../trainer.md#Trainer.Config.override), [`register_to_vllm`](../experiments/rl/models/vllm_registry.md#register_to_vllm), [`_enable_pallas_cross_entropy`](../experiments/tpu/muse_glimmer/config_registry.md#_enable_pallas_cross_entropy), [`qwen3_moe_235b_fsdp_activation_offload_maxtext`](../experiments/tpu/qwen3/config_registry.md#qwen3_moe_235b_fsdp_activation_offload_maxtext), [`qwen3_moe_235b_scan_maxtext`](../experiments/tpu/qwen3/config_registry.md#qwen3_moe_235b_scan_maxtext), [`qwen3_32b_maxtext_parity`](../experiments/tpu/qwen3/config_registry.md#qwen3_32b_maxtext_parity), [`qwen3_8b_maxtext_parity`](../experiments/tpu/qwen3/config_registry.md#qwen3_8b_maxtext_parity), [`training`](../experiments/rl/models/vllm_wrapper.md#VLLMModelWrapper.__init__._InferenceConfig.training), [`_enable_pallas_cross_entropy`](../experiments/tpu/llama3/config_registry.md#_enable_pallas_cross_entropy), [`_enable_pallas_cross_entropy`](../experiments/tpu/qwen3/config_registry.md#_enable_pallas_cross_entropy), [`qwen3_moe_30b_fsdp_only_attention_parity_benchmark`](../experiments/tpu/qwen3/config_registry.md#qwen3_moe_30b_fsdp_only_attention_parity_benchmark), [`__init__`](../experiments/rl/models/vllm_wrapper.md#VLLMModelWrapper.__init__), [`enable_fused_swiglu`](../models/deepseek_v3/config_registry.md#enable_fused_swiglu), [`override`](../experiments/rl/actors/generator.md#VLLMGenerator.Config.override), [`override`](../experiments/rl/actors/trainer.md#PolicyTrainer.Config.override)  (18 test-only)

### <a id="_Claim"></a>`_Claim`
- def: [`torchtitan/config/override.py:371`](../../../../../../raw/code/torchtitan/torchtitan/config/override.py#L371)
- doc: One (override, matched node) pair, collected before any mutation.
- signature: `class _Claim:`
- members:
  - <a id="_Claim.attr"></a>`attr` — [`L382`](../../../../../../raw/code/torchtitan/torchtitan/config/override.py#L382)
  - <a id="_Claim.cfg"></a>`cfg` — [`L380`](../../../../../../raw/code/torchtitan/torchtitan/config/override.py#L380)
  - <a id="_Claim.fqn"></a>`fqn` — [`L379`](../../../../../../raw/code/torchtitan/torchtitan/config/override.py#L379)
  - <a id="_Claim.kwargs"></a>`kwargs` — [`L383`](../../../../../../raw/code/torchtitan/torchtitan/config/override.py#L383)
  - <a id="_Claim.ov"></a>`ov` — [`L378`](../../../../../../raw/code/torchtitan/torchtitan/config/override.py#L378)
  - <a id="_Claim.parent"></a>`parent` — [`L381`](../../../../../../raw/code/torchtitan/torchtitan/config/override.py#L381)
- uses (calls/refs, reference-scoped): [`Configurable`](configurable.md#Configurable), [`Config`](configurable.md#Configurable.Config), [`Override`](override.md#Override)
- used by: [`apply_overrides`](override.md#apply_overrides), [`_collect_claims`](override.md#_collect_claims), [`_check_node_conflicts`](override.md#_check_node_conflicts)

## Functions
- <a id="_check_node_conflicts"></a>`_check_node_conflicts(claims: list[_Claim])` — [`L414`](../../../../../../raw/code/torchtitan/torchtitan/config/override.py#L414) — Raise if two *different* overrides claim the same node or nested nodes.
- <a id="_collect_claims"></a>`_collect_claims(resolved: list[tuple[Override, dict[str, Any]]], config_root: Configurable.Config)` — [`L386`](../../../../../../raw/code/torchtitan/torchtitan/config/override.py#L386) — Traverse the original tree and gather every node each override claims. — documented in [job-config](../../../concepts/job-config.md)
- <a id="_resolve_active"></a>`_resolve_active(targets: list[tuple[str, str, dict[str, Any]]])` — [`L339`](../../../../../../raw/code/torchtitan/torchtitan/config/override.py#L339) — Pair each activated override with the kwargs of the target that named it.
- <a id="_resolve_target"></a>`_resolve_target(target: str)` — [`L313`](../../../../../../raw/code/torchtitan/torchtitan/config/override.py#L313) — Split a ``module.function`` override target and import its module.
- <a id="apply_overrides"></a>`apply_overrides(override_config: OverrideConfig, config_root: Configurable.Config)` — [`L448`](../../../../../../raw/code/torchtitan/torchtitan/config/override.py#L448) — Import override modules and apply active overrides to the config tree. — documented in [job-config](../../../concepts/job-config.md)
- <a id="clear_overrides"></a>`clear_overrides()` — [`L518`](../../../../../../raw/code/torchtitan/torchtitan/config/override.py#L518) — Remove all registered overrides. Intended for testing.
- <a id="override.decorator"></a>`decorator(fn: Callable)` — [`L227`](../../../../../../raw/code/torchtitan/torchtitan/config/override.py#L227)
- <a id="derive"></a>`derive(source: Configurable.Config, target_cls: type[_ConfigT], **deltas: object)` — [`L249`](../../../../../../raw/code/torchtitan/torchtitan/config/override.py#L249) — Build ``target_cls`` by copying fields shared with ``source``, then deltas. — documented in [job-config](../../../concepts/job-config.md)
- <a id="format_cli_imports"></a>`format_cli_imports(entries: list[OverrideImport])` — [`L128`](../../../../../../raw/code/torchtitan/torchtitan/config/override.py#L128) — Serialize ``imports`` entries back to CLI tokens (inverse of the parse).
- <a id="override"></a>`override(*, target: type[Configurable.Config], fqns: list[str] | None = None, description: str = "", exact: bool = False)` — [`L175`](../../../../../../raw/code/torchtitan/torchtitan/config/override.py#L175) — Decorator to register an override factory. — documented in [job-config](../../../concepts/job-config.md)
- <a id="parse_cli_imports"></a>`parse_cli_imports(tokens: list[str])` — [`L94`](../../../../../../raw/code/torchtitan/torchtitan/config/override.py#L94) — Parse ``--override.imports`` CLI tokens into ``imports`` entries.

## Module values
- <a id="OverrideImport"></a>`OverrideImport` — [`L57`](../../../../../../raw/code/torchtitan/torchtitan/config/override.py#L57)
- <a id="_ConfigT"></a>`_ConfigT` — [`L49`](../../../../../../raw/code/torchtitan/torchtitan/config/override.py#L49)
- <a id="_REGISTRY._REGISTRY"></a>`_REGISTRY` — [`L172`](../../../../../../raw/code/torchtitan/torchtitan/config/override.py#L172)

