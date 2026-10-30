---
title: 'Module: torchtitan/components/metrics.py'
type: catalog
provenance: extracted
module: torchtitan/components/metrics.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.components.metrics`/
symbols:
  MetricsProcessor: MetricsProcessor#
  MetricsProcessor.Config: MetricsProcessor#Config#
  MetricsProcessor.log: MetricsProcessor#log().
  MetricsProcessor.Config.log_freq: MetricsProcessor#Config#log_freq.
  MetricsProcessor.__init__: MetricsProcessor#__init__().
  MetricsProcessor.log_validation: MetricsProcessor#log_validation().
  MetricsProcessor._build_metric_logger: MetricsProcessor#_build_metric_logger().
  BaseLogger: BaseLogger#
  ensure_pp_loss_visible: ensure_pp_loss_visible().
  DeviceMemoryMonitor.get_peak_stats: DeviceMemoryMonitor#get_peak_stats().
  BaseLogger.log: BaseLogger#log().
  BaseLogger.close: BaseLogger#close().
  build_device_memory_monitor: build_device_memory_monitor().
  MetricsProcessor.should_log: MetricsProcessor#should_log().
  _get_metrics_rank: _get_metrics_rank().
  MetricsProcessor.device_memory_monitor: MetricsProcessor#device_memory_monitor.
  MetricsProcessor.ntokens_since_last_log: MetricsProcessor#ntokens_since_last_log.
  DeviceMemoryMonitor.device_capacity_gib: DeviceMemoryMonitor#device_capacity_gib.
  MetricsProcessor.Config.enable_tensorboard: MetricsProcessor#Config#enable_tensorboard.
  MetricsProcessor.color: MetricsProcessor#color.
  TensorBoardLogger: TensorBoardLogger#
  WandBLogger: WandBLogger#
  DeviceMemoryMonitor.device_name: DeviceMemoryMonitor#device_name.
  DeviceMemoryMonitor.device_capacity: DeviceMemoryMonitor#device_capacity.
  WandBLogger.tag: WandBLogger#tag.
  LoggerContainer.add_logger: LoggerContainer#add_logger().
  MetricsProcessor.data_loading_times: MetricsProcessor#data_loading_times.
  MetricsProcessor.step_last_log: MetricsProcessor#step_last_log.
  MetricsProcessor.logger: MetricsProcessor#logger.
  MetricsProcessor.close: MetricsProcessor#close().
  DeviceMemoryMonitor.reset_peak_stats: DeviceMemoryMonitor#reset_peak_stats().
  TensorBoardLogger.writer: TensorBoardLogger#writer.
  MetricsProcessor.parallel_dims: MetricsProcessor#parallel_dims.
  TensorBoardLogger.log: TensorBoardLogger#log().
  WandBLogger.log: WandBLogger#log().
  LoggerContainer.log: LoggerContainer#log().
  LoggerContainer.close: LoggerContainer#close().
  MetricsProcessor.Config.enable_moe_routing: MetricsProcessor#Config#enable_moe_routing.
  MetricsProcessor.time_last_log: MetricsProcessor#time_last_log.
  DeviceMemoryMonitor._to_pct: DeviceMemoryMonitor#_to_pct().
  MetricsProcessor.config: MetricsProcessor#config.
  WandBLogger.wandb: WandBLogger#wandb.
  LoggerContainer._loggers: LoggerContainer#_loggers.
  MetricsProcessor.Config.enable_wandb: MetricsProcessor#Config#enable_wandb.
  MetricsProcessor.num_flops_per_token: MetricsProcessor#num_flops_per_token.
  LoggerContainer: LoggerContainer#
  LoggerContainer.number_of_loggers: LoggerContainer#number_of_loggers().
  MetricsProcessor.optimizers: MetricsProcessor#optimizers.
  DeviceMemoryMonitor.device: DeviceMemoryMonitor#device.
  DeviceMemoryMonitor._to_gib: DeviceMemoryMonitor#_to_gib().
  DeviceMemoryMonitor.__init__: DeviceMemoryMonitor#__init__().
  DeviceMemoryMonitor.device_index: DeviceMemoryMonitor#device_index.
  TensorBoardLogger.close: TensorBoardLogger#close().
  WandBLogger.close: WandBLogger#close().
  LoggerContainer.__init__: LoggerContainer#__init__().
  MetricsProcessor.Config.__post_init__: MetricsProcessor#Config#__post_init__().
  DeviceMemoryMonitor: DeviceMemoryMonitor#
  TensorBoardLogger.tag: TensorBoardLogger#tag.
  MetricsProcessor.Config.save_tb_folder: MetricsProcessor#Config#save_tb_folder.
  MetricsProcessor.Config.save_for_all_ranks: MetricsProcessor#Config#save_for_all_ranks.
  MetricsProcessor.gpu_peak_flops: MetricsProcessor#gpu_peak_flops.
  MetricsProcessor.has_quantization: MetricsProcessor#has_quantization.
  DeviceMemStats: DeviceMemStats.
  MetricsProcessor.Config.disable_color_printing: MetricsProcessor#Config#disable_color_printing.
  MetricsProcessor.model_parts: MetricsProcessor#model_parts.
  TensorBoardLogger.__init__: TensorBoardLogger#__init__().
  WandBLogger.__init__: WandBLogger#__init__().
---
# Module: [`torchtitan/components/metrics.py`](../../../../../../raw/code/torchtitan/torchtitan/components/metrics.py)

## Classes
### <a id="BaseLogger"></a>`BaseLogger`
- def: [`torchtitan/components/metrics.py:106`](../../../../../../raw/code/torchtitan/torchtitan/components/metrics.py#L106)
- doc: Logger that does nothing, used when logging is disabled.
- signature: `class BaseLogger:`
- members:
  - <a id="BaseLogger.close"></a>`close(self)` — [`L112`](../../../../../../raw/code/torchtitan/torchtitan/components/metrics.py#L112)
  - <a id="BaseLogger.log"></a>`log(self, metrics: dict[str, Any], step: int)` — [`L109`](../../../../../../raw/code/torchtitan/torchtitan/components/metrics.py#L109)
- uses (calls/refs, reference-scoped): [`TensorBoardLogger`](metrics.md#TensorBoardLogger), [`WandBLogger`](metrics.md#WandBLogger), [`close`](metrics.md#LoggerContainer.close), [`log`](metrics.md#LoggerContainer.log), [`log`](metrics.md#TensorBoardLogger.log), [`log`](metrics.md#WandBLogger.log), [`LoggerContainer`](metrics.md#LoggerContainer), [`close`](metrics.md#TensorBoardLogger.close), [`close`](metrics.md#WandBLogger.close)  (6 test-only)
- used by: [`log`](metrics.md#MetricsProcessor.log), [`log_validation`](metrics.md#MetricsProcessor.log_validation), [`_build_metric_logger`](metrics.md#MetricsProcessor._build_metric_logger), [`log`](../experiments/rl/observability/metrics/processor.md#MetricsProcessor.log), [`_backends`](../experiments/rl/observability/metrics/processor.md#MetricsProcessor._backends), [`close`](../experiments/rl/observability/metrics/processor.md#MetricsProcessor.close), [`TensorBoardLogger`](metrics.md#TensorBoardLogger), [`WandBLogger`](metrics.md#WandBLogger), [`add_logger`](metrics.md#LoggerContainer.add_logger), [`logger`](metrics.md#MetricsProcessor.logger), [`close`](metrics.md#MetricsProcessor.close), [`close`](metrics.md#LoggerContainer.close), [`log`](metrics.md#LoggerContainer.log), [`LoggerContainer`](metrics.md#LoggerContainer), [`__init__`](metrics.md#LoggerContainer.__init__)  (1 test-only)

### <a id="DeviceMemoryMonitor"></a>`DeviceMemoryMonitor`
- def: [`torchtitan/components/metrics.py:38`](../../../../../../raw/code/torchtitan/torchtitan/components/metrics.py#L38)
- signature: `class DeviceMemoryMonitor:`
- members:
  - <a id="DeviceMemoryMonitor.get_peak_stats"></a>`get_peak_stats(self)` — [`L63`](../../../../../../raw/code/torchtitan/torchtitan/components/metrics.py#L63)
  - <a id="DeviceMemoryMonitor.reset_peak_stats"></a>`reset_peak_stats(self)` — [`L93`](../../../../../../raw/code/torchtitan/torchtitan/components/metrics.py#L93)
  - <a id="DeviceMemoryMonitor.device"></a>`device` — [`L43`](../../../../../../raw/code/torchtitan/torchtitan/components/metrics.py#L43)
  - <a id="DeviceMemoryMonitor.device_capacity"></a>`device_capacity` — [`L46`](../../../../../../raw/code/torchtitan/torchtitan/components/metrics.py#L46)
  - <a id="DeviceMemoryMonitor.device_capacity_gib"></a>`device_capacity_gib` — [`L49`](../../../../../../raw/code/torchtitan/torchtitan/components/metrics.py#L49)
  - <a id="DeviceMemoryMonitor.device_index"></a>`device_index` — [`L45`](../../../../../../raw/code/torchtitan/torchtitan/components/metrics.py#L45)
  - <a id="DeviceMemoryMonitor.device_name"></a>`device_name` — [`L44`](../../../../../../raw/code/torchtitan/torchtitan/components/metrics.py#L44)
- protocol/private: <a id="DeviceMemoryMonitor.__init__"></a>`__init__`[`L39`](../../../../../../raw/code/torchtitan/torchtitan/components/metrics.py#L39), <a id="DeviceMemoryMonitor._to_gib"></a>`_to_gib`[`L54`](../../../../../../raw/code/torchtitan/torchtitan/components/metrics.py#L54), <a id="DeviceMemoryMonitor._to_pct"></a>`_to_pct`[`L60`](../../../../../../raw/code/torchtitan/torchtitan/components/metrics.py#L60)
- uses (calls/refs, reference-scoped): [`logger`](../tools/logging.md#logger), [`device_type`](../tools/utils.md#device_type), [`device_module`](../tools/utils.md#device_module), [`DeviceMemStats`](metrics.md#DeviceMemStats)
- used by: [`log`](metrics.md#MetricsProcessor.log), [`__init__`](metrics.md#MetricsProcessor.__init__), [`log_validation`](metrics.md#MetricsProcessor.log_validation), [`build_device_memory_monitor`](metrics.md#build_device_memory_monitor), [`device_memory_monitor`](metrics.md#MetricsProcessor.device_memory_monitor)

### <a id="LoggerContainer"></a>`LoggerContainer`  ·  implements/extends BaseLogger
- def: [`torchtitan/components/metrics.py:182`](../../../../../../raw/code/torchtitan/torchtitan/components/metrics.py#L182)
- doc: Container to call all loggers enabled in the job config.
- signature: `class LoggerContainer(BaseLogger):`
- members:
  - <a id="LoggerContainer.add_logger"></a>`add_logger(self, logger_instance: BaseLogger)` — [`L188`](../../../../../../raw/code/torchtitan/torchtitan/components/metrics.py#L188)
  - <a id="LoggerContainer.close"></a>`close(self)` — [`L199`](../../../../../../raw/code/torchtitan/torchtitan/components/metrics.py#L199)
  - <a id="LoggerContainer.log"></a>`log(self, metrics: dict[str, Any], step: int)` — [`L191`](../../../../../../raw/code/torchtitan/torchtitan/components/metrics.py#L191)
  - <a id="LoggerContainer.number_of_loggers"></a>`number_of_loggers(self)` — [`L196`](../../../../../../raw/code/torchtitan/torchtitan/components/metrics.py#L196)
- protocol/private: <a id="LoggerContainer.__init__"></a>`__init__`[`L185`](../../../../../../raw/code/torchtitan/torchtitan/components/metrics.py#L185), <a id="LoggerContainer._loggers"></a>`_loggers`[`L186`](../../../../../../raw/code/torchtitan/torchtitan/components/metrics.py#L186)
- uses (calls/refs, reference-scoped): [`BaseLogger`](metrics.md#BaseLogger), [`log`](metrics.md#BaseLogger.log), [`close`](metrics.md#BaseLogger.close)
- used by: [`_build_metric_logger`](metrics.md#MetricsProcessor._build_metric_logger), [`BaseLogger`](metrics.md#BaseLogger), [`log`](metrics.md#BaseLogger.log), [`close`](metrics.md#BaseLogger.close)

### <a id="MetricsProcessor"></a>`MetricsProcessor`  ·  implements/extends Configurable
- def: [`torchtitan/components/metrics.py:265`](../../../../../../raw/code/torchtitan/torchtitan/components/metrics.py#L265) — documented in [training-components](../../../concepts/training-components.md)
- doc: Metrics processor to processes the metrics and log metrics.
- signature: `class MetricsProcessor(Configurable):`
- members:
  - <a id="MetricsProcessor._build_metric_logger"></a>`_build_metric_logger(self, *, config: Config, parallel_dims: ParallelDims, dump_folder: str, pp_schedule: str, ft_enable: bool = False, ft_replica_id: int = 0, config_dict: dict[str, Any] | None = None, tag: str | None = None)` — [`L381`](../../../../../../raw/code/torchtitan/torchtitan/components/metrics.py#L381) — Build an appropriate metric logger based on configuration.
  - <a id="MetricsProcessor.close"></a>`close(self)` — [`L598`](../../../../../../raw/code/torchtitan/torchtitan/components/metrics.py#L598)
  - <a id="MetricsProcessor.log"></a>`log(self, step: int, global_avg_loss: float, global_max_loss: float, grad_norm: float, extra_metrics: dict[str, Any] | None = None)` — [`L467`](../../../../../../raw/code/torchtitan/torchtitan/components/metrics.py#L467) — Log training metrics including loss, throughput, and memory statistics. — documented in [training-components](../../../concepts/training-components.md)
  - <a id="MetricsProcessor.log_validation"></a>`log_validation(self, loss: float, step: int, extra_metrics: dict[str, Any] | None = None)` — [`L558`](../../../../../../raw/code/torchtitan/torchtitan/components/metrics.py#L558)
  - <a id="MetricsProcessor.should_log"></a>`should_log(self, step: int)` — [`L376`](../../../../../../raw/code/torchtitan/torchtitan/components/metrics.py#L376)
  - <a id="MetricsProcessor.color"></a>`color` — [`L318`](../../../../../../raw/code/torchtitan/torchtitan/components/metrics.py#L318)
  - <a id="MetricsProcessor.config"></a>`config` — [`L314`](../../../../../../raw/code/torchtitan/torchtitan/components/metrics.py#L314)
  - <a id="MetricsProcessor.data_loading_times"></a>`data_loading_times` — [`L322`](../../../../../../raw/code/torchtitan/torchtitan/components/metrics.py#L322)
  - <a id="MetricsProcessor.device_memory_monitor"></a>`device_memory_monitor` — [`L317`](../../../../../../raw/code/torchtitan/torchtitan/components/metrics.py#L317)
  - <a id="MetricsProcessor.gpu_peak_flops"></a>`gpu_peak_flops` — [`L320`](../../../../../../raw/code/torchtitan/torchtitan/components/metrics.py#L320)
  - <a id="MetricsProcessor.has_quantization"></a>`has_quantization` — [`L327`](../../../../../../raw/code/torchtitan/torchtitan/components/metrics.py#L327)
  - <a id="MetricsProcessor.logger"></a>`logger` — [`L315`](../../../../../../raw/code/torchtitan/torchtitan/components/metrics.py#L315)
  - <a id="MetricsProcessor.model_parts"></a>`model_parts` — [`L329`](../../../../../../raw/code/torchtitan/torchtitan/components/metrics.py#L329)
  - <a id="MetricsProcessor.ntokens_since_last_log"></a>`ntokens_since_last_log` — [`L321`](../../../../../../raw/code/torchtitan/torchtitan/components/metrics.py#L321)
  - <a id="MetricsProcessor.num_flops_per_token"></a>`num_flops_per_token` — [`L326`](../../../../../../raw/code/torchtitan/torchtitan/components/metrics.py#L326)
  - <a id="MetricsProcessor.optimizers"></a>`optimizers` — [`L328`](../../../../../../raw/code/torchtitan/torchtitan/components/metrics.py#L328)
  - <a id="MetricsProcessor.parallel_dims"></a>`parallel_dims` — [`L316`](../../../../../../raw/code/torchtitan/torchtitan/components/metrics.py#L316)
  - <a id="MetricsProcessor.step_last_log"></a>`step_last_log` — [`L324`](../../../../../../raw/code/torchtitan/torchtitan/components/metrics.py#L324)
  - <a id="MetricsProcessor.time_last_log"></a>`time_last_log` — [`L323`](../../../../../../raw/code/torchtitan/torchtitan/components/metrics.py#L323)
- protocol/private: <a id="MetricsProcessor.__init__"></a>`__init__`[`L331`](../../../../../../raw/code/torchtitan/torchtitan/components/metrics.py#L331)
- uses (calls/refs, reference-scoped): [`logger`](../tools/logging.md#logger), [`Configurable`](../config/configurable.md#Configurable), [`ParallelDims`](../distributed/parallel_dims.md#ParallelDims), [`Config`](metrics.md#MetricsProcessor.Config), [`log_freq`](metrics.md#MetricsProcessor.Config.log_freq), [`OptimizersContainer`](optimizer/optimizer.md#OptimizersContainer), [`BaseLogger`](metrics.md#BaseLogger), [`get_peak_stats`](metrics.md#DeviceMemoryMonitor.get_peak_stats), [`log`](metrics.md#BaseLogger.log), [`close`](metrics.md#BaseLogger.close), [`build_device_memory_monitor`](metrics.md#build_device_memory_monitor), [`_get_metrics_rank`](metrics.md#_get_metrics_rank), [`non_data_parallel_size`](../distributed/parallel_dims.md#ParallelDims.non_data_parallel_size), [`Color`](../tools/utils.md#Color), [`get_peak_flops`](../tools/utils.md#get_peak_flops), [`NoColor`](../tools/utils.md#NoColor), [`enable_tensorboard`](metrics.md#MetricsProcessor.Config.enable_tensorboard), [`TensorBoardLogger`](metrics.md#TensorBoardLogger), [`WandBLogger`](metrics.md#WandBLogger), [`add_logger`](metrics.md#LoggerContainer.add_logger), [`device_name`](metrics.md#DeviceMemoryMonitor.device_name), [`turquoise`](../tools/utils.md#NoColor.turquoise), [`reset_peak_stats`](metrics.md#DeviceMemoryMonitor.reset_peak_stats), [`enable_wandb`](metrics.md#MetricsProcessor.Config.enable_wandb), [`LoggerContainer`](metrics.md#LoggerContainer), [`number_of_loggers`](metrics.md#LoggerContainer.number_of_loggers), [`blue`](../tools/utils.md#NoColor.blue), [`green`](../tools/utils.md#NoColor.green), [`reset`](../tools/utils.md#NoColor.reset), [`DeviceMemoryMonitor`](metrics.md#DeviceMemoryMonitor), [`cyan`](../tools/utils.md#NoColor.cyan), [`magenta`](../tools/utils.md#NoColor.magenta), [`orange`](../tools/utils.md#NoColor.orange), [`red`](../tools/utils.md#NoColor.red), [`save_for_all_ranks`](metrics.md#MetricsProcessor.Config.save_for_all_ranks), [`save_tb_folder`](metrics.md#MetricsProcessor.Config.save_tb_folder), [`yellow`](../tools/utils.md#NoColor.yellow), [`disable_color_printing`](metrics.md#MetricsProcessor.Config.disable_color_printing)
- used by: [`Configurable`](../config/configurable.md#Configurable), [`sft_llama3_8b_metamath`](../experiments/tpu/llama3/config_registry.md#sft_llama3_8b_metamath), [`qwen3_8b`](../experiments/tpu/qwen3/config_registry.md#qwen3_8b), [`flux_debugmodel`](../models/flux/config_registry.md#flux_debugmodel), [`reg_trainer_qwen3_8b`](../experiments/tpu/qwen3/config_registry.md#reg_trainer_qwen3_8b), [`qwen3_1_7b`](../experiments/tpu/qwen3/config_registry.md#qwen3_1_7b), [`llama3_70b`](../experiments/tpu/llama3/config_registry.md#llama3_70b), [`llama3_405b`](../experiments/tpu/llama3/config_registry.md#llama3_405b), [`llama3_8b`](../experiments/tpu/llama3/config_registry.md#llama3_8b), [`llama3_debugmodel`](../models/llama3/config_registry.md#llama3_debugmodel), [`llama3_torchft_debugmodel`](../experiments/torchft/llama3/config_registry.md#llama3_torchft_debugmodel), [`_muse_glimmer_30b_base`](../experiments/tpu/muse_glimmer/config_registry.md#_muse_glimmer_30b_base), [`flux_dev`](../models/flux/config_registry.md#flux_dev), [`flux_schnell`](../models/flux/config_registry.md#flux_schnell), [`llama3_405b`](../models/llama3/config_registry.md#llama3_405b), [`_tpu_hf_config`](../experiments/tpu/transformers_modeling_backend/config_registry.md#_tpu_hf_config), [`transformers_modeling_backend_sft_full`](../experiments/transformers_modeling_backend/config_registry.md#transformers_modeling_backend_sft_full), [`sft_debugmodel`](../models/llama3/config_registry.md#sft_debugmodel), [`sft_qwen3_8b_math`](../models/qwen3/config_registry.md#sft_qwen3_8b_math), [`transformers_modeling_backend_sft_debugmodel`](../experiments/transformers_modeling_backend/config_registry.md#transformers_modeling_backend_sft_debugmodel), [`qwen35_debugmodel_moe`](../models/qwen3_5/config_registry.md#qwen35_debugmodel_moe), [`deepseek_v4_debugmodel`](../models/deepseek_v4/config_registry.md#deepseek_v4_debugmodel), [`qwen35_moe_35b`](../experiments/tpu/qwen3_5/config_registry.md#qwen35_moe_35b), [`qwen38_debugmodel_moe`](../models/qwen3_8/config_registry.md#qwen38_debugmodel_moe), [`deepseek_v3_debugmodel`](../models/deepseek_v3/config_registry.md#deepseek_v3_debugmodel), [`deepseek_v4_flash`](../models/deepseek_v4/config_registry.md#deepseek_v4_flash), [`deepseek_v4_pro`](../models/deepseek_v4/config_registry.md#deepseek_v4_pro), [`qwen36_debugmodel_moe`](../models/qwen3_6/config_registry.md#qwen36_debugmodel_moe), [`_gpt_oss_debugmodel`](../models/gpt_oss/config_registry.md#_gpt_oss_debugmodel), [`deepseek_v4_mtp_debugmodel`](../models/deepseek_v4/config_registry.md#deepseek_v4_mtp_debugmodel), [`kimi_k2_5_debugmodel`](../models/kimi_k2_7/config_registry.md#kimi_k2_5_debugmodel), [`muse_glimmer_debugmodel`](../models/muse_glimmer/config_registry.md#muse_glimmer_debugmodel), [`transformers_modeling_backend_debugmodel`](../experiments/transformers_modeling_backend/config_registry.md#transformers_modeling_backend_debugmodel), [`qwen3_debugmodel`](../experiments/tpu/qwen3/config_registry.md#qwen3_debugmodel), [`transformers_modeling_backend_debugmodel_moe`](../experiments/transformers_modeling_backend/config_registry.md#transformers_modeling_backend_debugmodel_moe), [`qwen35_debugmodel`](../models/qwen3_5/config_registry.md#qwen35_debugmodel), [`qwen38_debugmodel`](../models/qwen3_8/config_registry.md#qwen38_debugmodel), [`llama3_70b`](../models/llama3/config_registry.md#llama3_70b), [`muse_glimmer_debugmodel_mm`](../models/muse_glimmer/config_registry.md#muse_glimmer_debugmodel_mm), [`qwen36_debugmodel`](../models/qwen3_6/config_registry.md#qwen36_debugmodel)  (+28 more; 11 test-only)

### <a id="MetricsProcessor.Config"></a>`MetricsProcessor.Config`  ·  implements/extends Config
- def: [`torchtitan/components/metrics.py:283`](../../../../../../raw/code/torchtitan/torchtitan/components/metrics.py#L283)
- signature: `class Config(Configurable.Config):`
- members:
  - <a id="MetricsProcessor.Config.disable_color_printing"></a>`disable_color_printing` — [`L293`](../../../../../../raw/code/torchtitan/torchtitan/components/metrics.py#L293) — ---
  - <a id="MetricsProcessor.Config.enable_moe_routing"></a>`enable_moe_routing` — [`L287`](../../../../../../raw/code/torchtitan/torchtitan/components/metrics.py#L287) — ---
  - <a id="MetricsProcessor.Config.enable_tensorboard"></a>`enable_tensorboard` — [`L290`](../../../../../../raw/code/torchtitan/torchtitan/components/metrics.py#L290) — ---
  - <a id="MetricsProcessor.Config.enable_wandb"></a>`enable_wandb` — [`L307`](../../../../../../raw/code/torchtitan/torchtitan/components/metrics.py#L307) — ---
  - <a id="MetricsProcessor.Config.log_freq"></a>`log_freq` — [`L284`](../../../../../../raw/code/torchtitan/torchtitan/components/metrics.py#L284) — --- — documented in [training-components](../../../concepts/training-components.md)
  - <a id="MetricsProcessor.Config.save_for_all_ranks"></a>`save_for_all_ranks` — [`L299`](../../../../../../raw/code/torchtitan/torchtitan/components/metrics.py#L299) — ---
  - <a id="MetricsProcessor.Config.save_tb_folder"></a>`save_tb_folder` — [`L296`](../../../../../../raw/code/torchtitan/torchtitan/components/metrics.py#L296) — ---
- protocol/private: <a id="MetricsProcessor.Config.__post_init__"></a>`__post_init__`[`L310`](../../../../../../raw/code/torchtitan/torchtitan/components/metrics.py#L310)
- uses (calls/refs, reference-scoped): [`Configurable`](../config/configurable.md#Configurable), [`Config`](../config/configurable.md#Configurable.Config)
- used by: [`sft_llama3_8b_metamath`](../experiments/tpu/llama3/config_registry.md#sft_llama3_8b_metamath), [`qwen3_8b`](../experiments/tpu/qwen3/config_registry.md#qwen3_8b), [`flux_debugmodel`](../models/flux/config_registry.md#flux_debugmodel), [`reg_trainer_qwen3_8b`](../experiments/tpu/qwen3/config_registry.md#reg_trainer_qwen3_8b), [`start_trainer`](../experiments/tpu/conformer/train_minimal.md#start_trainer), [`qwen3_1_7b`](../experiments/tpu/qwen3/config_registry.md#qwen3_1_7b), [`llama3_70b`](../experiments/tpu/llama3/config_registry.md#llama3_70b), [`llama3_405b`](../experiments/tpu/llama3/config_registry.md#llama3_405b), [`llama3_8b`](../experiments/tpu/llama3/config_registry.md#llama3_8b), [`llama3_debugmodel`](../models/llama3/config_registry.md#llama3_debugmodel), [`_qwen3_moe_30b_fsdp_only_full_ac`](../experiments/tpu/qwen3/config_registry.md#_qwen3_moe_30b_fsdp_only_full_ac), [`llama3_torchft_debugmodel`](../experiments/torchft/llama3/config_registry.md#llama3_torchft_debugmodel), [`_muse_glimmer_30b_base`](../experiments/tpu/muse_glimmer/config_registry.md#_muse_glimmer_30b_base), [`flux_dev`](../models/flux/config_registry.md#flux_dev), [`flux_schnell`](../models/flux/config_registry.md#flux_schnell), [`llama3_405b`](../models/llama3/config_registry.md#llama3_405b), [`_tpu_hf_config`](../experiments/tpu/transformers_modeling_backend/config_registry.md#_tpu_hf_config), [`_collect_moe_routing_metrics`](../trainer.md#Trainer._collect_moe_routing_metrics), [`transformers_modeling_backend_sft_full`](../experiments/transformers_modeling_backend/config_registry.md#transformers_modeling_backend_sft_full), [`sft_debugmodel`](../models/llama3/config_registry.md#sft_debugmodel), [`sft_qwen3_8b_math`](../models/qwen3/config_registry.md#sft_qwen3_8b_math), [`transformers_modeling_backend_sft_debugmodel`](../experiments/transformers_modeling_backend/config_registry.md#transformers_modeling_backend_sft_debugmodel), [`qwen35_debugmodel_moe`](../models/qwen3_5/config_registry.md#qwen35_debugmodel_moe), [`deepseek_v4_debugmodel`](../models/deepseek_v4/config_registry.md#deepseek_v4_debugmodel), [`qwen35_moe_35b`](../experiments/tpu/qwen3_5/config_registry.md#qwen35_moe_35b), [`qwen38_debugmodel_moe`](../models/qwen3_8/config_registry.md#qwen38_debugmodel_moe), [`deepseek_v3_debugmodel`](../models/deepseek_v3/config_registry.md#deepseek_v3_debugmodel), [`deepseek_v4_flash`](../models/deepseek_v4/config_registry.md#deepseek_v4_flash), [`deepseek_v4_pro`](../models/deepseek_v4/config_registry.md#deepseek_v4_pro), [`qwen36_debugmodel_moe`](../models/qwen3_6/config_registry.md#qwen36_debugmodel_moe), [`_gpt_oss_debugmodel`](../models/gpt_oss/config_registry.md#_gpt_oss_debugmodel), [`deepseek_v4_mtp_debugmodel`](../models/deepseek_v4/config_registry.md#deepseek_v4_mtp_debugmodel), [`kimi_k2_5_debugmodel`](../models/kimi_k2_7/config_registry.md#kimi_k2_5_debugmodel), [`muse_glimmer_debugmodel`](../models/muse_glimmer/config_registry.md#muse_glimmer_debugmodel), [`transformers_modeling_backend_debugmodel`](../experiments/transformers_modeling_backend/config_registry.md#transformers_modeling_backend_debugmodel), [`qwen3_debugmodel`](../experiments/tpu/qwen3/config_registry.md#qwen3_debugmodel), [`transformers_modeling_backend_debugmodel_moe`](../experiments/transformers_modeling_backend/config_registry.md#transformers_modeling_backend_debugmodel_moe), [`qwen35_debugmodel`](../models/qwen3_5/config_registry.md#qwen35_debugmodel), [`qwen38_debugmodel`](../models/qwen3_8/config_registry.md#qwen38_debugmodel), [`llama3_70b`](../models/llama3/config_registry.md#llama3_70b)  (+25 more; 13 test-only)

### <a id="TensorBoardLogger"></a>`TensorBoardLogger`  ·  implements/extends BaseLogger
- def: [`torchtitan/components/metrics.py:116`](../../../../../../raw/code/torchtitan/torchtitan/components/metrics.py#L116)
- doc: Logger implementation for TensorBoard.
- signature: `class TensorBoardLogger(BaseLogger):`
- members:
  - <a id="TensorBoardLogger.close"></a>`close(self)` — [`L132`](../../../../../../raw/code/torchtitan/torchtitan/components/metrics.py#L132)
  - <a id="TensorBoardLogger.log"></a>`log(self, metrics: dict[str, Any], step: int)` — [`L124`](../../../../../../raw/code/torchtitan/torchtitan/components/metrics.py#L124)
  - <a id="TensorBoardLogger.tag"></a>`tag` — [`L120`](../../../../../../raw/code/torchtitan/torchtitan/components/metrics.py#L120)
  - <a id="TensorBoardLogger.writer"></a>`writer` — [`L121`](../../../../../../raw/code/torchtitan/torchtitan/components/metrics.py#L121)
- protocol/private: <a id="TensorBoardLogger.__init__"></a>`__init__`[`L119`](../../../../../../raw/code/torchtitan/torchtitan/components/metrics.py#L119)
- uses (calls/refs, reference-scoped): [`logger`](../tools/logging.md#logger), [`BaseLogger`](metrics.md#BaseLogger)
- used by: [`_build_metric_logger`](metrics.md#MetricsProcessor._build_metric_logger), [`BaseLogger`](metrics.md#BaseLogger), [`_backends`](../experiments/rl/observability/metrics/processor.md#MetricsProcessor._backends), [`log`](metrics.md#BaseLogger.log), [`close`](metrics.md#BaseLogger.close)  (1 test-only)

### <a id="WandBLogger"></a>`WandBLogger`  ·  implements/extends BaseLogger
- def: [`torchtitan/components/metrics.py:136`](../../../../../../raw/code/torchtitan/torchtitan/components/metrics.py#L136)
- doc: Logger implementation for Weights & Biases.
- signature: `class WandBLogger(BaseLogger):`
- members:
  - <a id="WandBLogger.close"></a>`close(self)` — [`L177`](../../../../../../raw/code/torchtitan/torchtitan/components/metrics.py#L177)
  - <a id="WandBLogger.log"></a>`log(self, metrics: dict[str, Any], step: int)` — [`L170`](../../../../../../raw/code/torchtitan/torchtitan/components/metrics.py#L170)
  - <a id="WandBLogger.tag"></a>`tag` — [`L149`](../../../../../../raw/code/torchtitan/torchtitan/components/metrics.py#L149)
  - <a id="WandBLogger.wandb"></a>`wandb` — [`L148`](../../../../../../raw/code/torchtitan/torchtitan/components/metrics.py#L148)
- protocol/private: <a id="WandBLogger.__init__"></a>`__init__`[`L139`](../../../../../../raw/code/torchtitan/torchtitan/components/metrics.py#L139)
- uses (calls/refs, reference-scoped): [`logger`](../tools/logging.md#logger), [`BaseLogger`](metrics.md#BaseLogger)
- used by: [`_build_metric_logger`](metrics.md#MetricsProcessor._build_metric_logger), [`BaseLogger`](metrics.md#BaseLogger), [`_backends`](../experiments/rl/observability/metrics/processor.md#MetricsProcessor._backends), [`log`](metrics.md#BaseLogger.log), [`close`](metrics.md#BaseLogger.close)  (1 test-only)

## Functions
- <a id="_get_metrics_rank"></a>`_get_metrics_rank(*, parallel_dims: ParallelDims, pp_schedule: str)` — [`L237`](../../../../../../raw/code/torchtitan/torchtitan/components/metrics.py#L237) — Determines which rank should log metrics.
- <a id="build_device_memory_monitor"></a>`build_device_memory_monitor()` — [`L97`](../../../../../../raw/code/torchtitan/torchtitan/components/metrics.py#L97)
- <a id="ensure_pp_loss_visible"></a>`ensure_pp_loss_visible(*, parallel_dims: ParallelDims, pp_schedule: str, color: Color | NoColor)` — [`L204`](../../../../../../raw/code/torchtitan/torchtitan/components/metrics.py#L204) — Ensures that the loss is visible on the console for pipeline-parallel training.

## Module values
- <a id="DeviceMemStats"></a>`DeviceMemStats` — [`L25`](../../../../../../raw/code/torchtitan/torchtitan/components/metrics.py#L25)

