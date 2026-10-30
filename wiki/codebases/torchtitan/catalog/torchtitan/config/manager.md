---
title: 'Module: torchtitan/config/manager.py'
type: catalog
provenance: extracted
module: torchtitan/config/manager.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.config.manager`/
symbols:
  ConfigManager: ConfigManager#
  ConfigManager.parse_args: ConfigManager#parse_args().
  config: config.
  ConfigManager.config: ConfigManager#config.
  ConfigManager._merge_configs: ConfigManager#_merge_configs().
  ConfigManager.override_imports_rule: ConfigManager#override_imports_rule().
  _reconstruct_config: _reconstruct_config().
  ConfigManager._load_config: ConfigManager#_load_config().
  ConfigManager._validate_config: ConfigManager#_validate_config().
  custom_registry: custom_registry.
  config_manager: config_manager.
  ConfigManager.__init__: ConfigManager#__init__().
  ConfigManager.__reduce__: ConfigManager#__reduce__().
  ConfigManager.register_tyro_rules: ConfigManager#register_tyro_rules().
  ConfigManager.list_str_rule: ConfigManager#list_str_rule().
---
# Module: [`torchtitan/config/manager.py`](../../../../../../raw/code/torchtitan/torchtitan/config/manager.py)

## Classes
### <a id="ConfigManager"></a>`ConfigManager`
- def: [`torchtitan/config/manager.py:29`](../../../../../../raw/code/torchtitan/torchtitan/config/manager.py#L29) — documented in [job-config](../../../concepts/job-config.md)
- members:
  - <a id="ConfigManager._load_config"></a>`_load_config(self, args: list[str])` — [`L58`](../../../../../../raw/code/torchtitan/torchtitan/config/manager.py#L58) — Parse --module and --config from args, load config from config_registry.
  - <a id="ConfigManager._merge_configs"></a>`_merge_configs(base, custom)` — [`L172`](../../../../../../raw/code/torchtitan/torchtitan/config/manager.py#L172) — Merges a base config class with user-defined extensions.
  - <a id="ConfigManager.list_str_rule"></a>`list_str_rule(type_info: tyro.constructors.PrimitiveTypeInfo)` — [`L257`](../../../../../../raw/code/torchtitan/torchtitan/config/manager.py#L257) — Support for comma separated string parsing
  - <a id="ConfigManager.override_imports_rule"></a>`override_imports_rule(type_info: tyro.constructors.PrimitiveTypeInfo)` — [`L270`](../../../../../../raw/code/torchtitan/torchtitan/config/manager.py#L270) — Parse ``--override.imports`` targets, each with optional kwargs.
  - <a id="ConfigManager.parse_args"></a>`parse_args(self, args: list[str] | None = None)` — [`L44`](../../../../../../raw/code/torchtitan/torchtitan/config/manager.py#L44) — documented in [job-config](../../../concepts/job-config.md)
  - <a id="ConfigManager.register_tyro_rules"></a>`register_tyro_rules(registry: tyro.constructors.ConstructorRegistry)` — [`L255`](../../../../../../raw/code/torchtitan/torchtitan/config/manager.py#L255)
  - <a id="ConfigManager.config"></a>`config` — [`L50`](../../../../../../raw/code/torchtitan/torchtitan/config/manager.py#L50)
- protocol/private: <a id="ConfigManager.__init__"></a>`__init__`[`L41`](../../../../../../raw/code/torchtitan/torchtitan/config/manager.py#L41), <a id="ConfigManager.__reduce__"></a>`__reduce__`[`L217`](../../../../../../raw/code/torchtitan/torchtitan/config/manager.py#L217), <a id="ConfigManager._validate_config"></a>`_validate_config`[`L223`](../../../../../../raw/code/torchtitan/torchtitan/config/manager.py#L223)
- uses (calls/refs, reference-scoped): [`logger`](../tools/logging.md#logger), [`OverrideImport`](override.md#OverrideImport), [`_reconstruct_config`](manager.md#_reconstruct_config), [`custom_registry`](manager.md#custom_registry), [`format_cli_imports`](override.md#format_cli_imports), [`parse_cli_imports`](override.md#parse_cli_imports), [`_supported_experiments`](../experiments/__init__.md#_supported_experiments), [`_supported_models`](../models/__init__.md#_supported_models)
- used by: [`TORCH_DTYPE_MAP`](__init__.md#TORCH_DTYPE_MAP), [`main`](../experiments/rl/train.md#main), [`_run_cpu_verification`](../experiments/tpu/base_distributed_device_test.md#_run_cpu_verification), [`_test_train_distributed`](../experiments/tpu/base_distributed_device_test.md#BaseDistributedDeviceTest._test_train_distributed), [`main`](../train.md#main), [`main`](../experiments/tpu/rl_nc_ray/grpo.md#main), [`config`](manager.md#config), [`main`](../experiments/graph_trainer/precompile_main.md#main), [`main`](../experiments/tpu/gmain.md#main), [`config`](../models/flux/inference/infer.md#config), [`main`](../experiments/jax/train_minimal.md#main), [`_reconstruct_config`](manager.md#_reconstruct_config), [`config_manager`](manager.md#config_manager), [`config_manager`](../models/flux/inference/infer.md#config_manager)  (21 test-only)

## Functions
- <a id="_reconstruct_config"></a>`_reconstruct_config(base, custom, data)` — [`L19`](../../../../../../raw/code/torchtitan/torchtitan/config/manager.py#L19) — Reconstructs a merged config instance for pickling.

## Module values
- <a id="config"></a>`config` — [`L330`](../../../../../../raw/code/torchtitan/torchtitan/config/manager.py#L330)
- <a id="config_manager"></a>`config_manager` — [`L329`](../../../../../../raw/code/torchtitan/torchtitan/config/manager.py#L329)
- <a id="custom_registry"></a>`custom_registry` — [`L308`](../../../../../../raw/code/torchtitan/torchtitan/config/manager.py#L308)

