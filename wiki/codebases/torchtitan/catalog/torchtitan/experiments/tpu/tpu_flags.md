---
title: 'Module: torchtitan/experiments/tpu/tpu_flags.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/tpu_flags.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.tpu_flags`/
symbols:
  FlagMap: FlagMap#
  merge_flags: merge_flags().
  _apply_flags: _apply_flags().
  parse_flags: parse_flags().
  apply_init_flags: apply_init_flags().
  HIERARCHICAL_REDUCE_SCATTER.HIERARCHICAL_REDUCE_SCATTER: HIERARCHICAL_REDUCE_SCATTER.HIERARCHICAL_REDUCE_SCATTER.
  SPARSECORE_LATENCY_HIDING_SCHEDULER.SPARSECORE_LATENCY_HIDING_SCHEDULER: SPARSECORE_LATENCY_HIDING_SCHEDULER.SPARSECORE_LATENCY_HIDING_SCHEDULER.
  _flag_map_rule: _flag_map_rule().
  ICI_AG_PIPELINING.ICI_AG_PIPELINING: ICI_AG_PIPELINING.ICI_AG_PIPELINING.
  SPARSECORE_ASYNC_ALL_GATHER.SPARSECORE_ASYNC_ALL_GATHER: SPARSECORE_ASYNC_ALL_GATHER.SPARSECORE_ASYNC_ALL_GATHER.
  TPU7X_THROUGHPUT_P_STATE.TPU7X_THROUGHPUT_P_STATE: TPU7X_THROUGHPUT_P_STATE.TPU7X_THROUGHPUT_P_STATE.
  format_flags: format_flags().
  SELECTIVE_ICI_RS_PIPELINING.SELECTIVE_ICI_RS_PIPELINING: SELECTIVE_ICI_RS_PIPELINING.SELECTIVE_ICI_RS_PIPELINING.
  resolve_flags: resolve_flags().
  CONVOLUTION_UNFUSING.CONVOLUTION_UNFUSING: CONVOLUTION_UNFUSING.CONVOLUTION_UNFUSING.
  REMOVE: REMOVE.
  _removed_names: _removed_names().
  _flag_value_str: _flag_value_str().
  DUAL_SPARSECORE_REDUCE_SCATTER.DUAL_SPARSECORE_REDUCE_SCATTER: DUAL_SPARSECORE_REDUCE_SCATTER.DUAL_SPARSECORE_REDUCE_SCATTER.
  FlagValue: FlagValue.
  SPARSECORE_COLLECTIVE_OFFLOAD.SPARSECORE_COLLECTIVE_OFFLOAD: SPARSECORE_COLLECTIVE_OFFLOAD.SPARSECORE_COLLECTIVE_OFFLOAD.
  DISABLE_ENHANCED_LAUNCH_BARRIER.DISABLE_ENHANCED_LAUNCH_BARRIER: DISABLE_ENHANCED_LAUNCH_BARRIER.DISABLE_ENHANCED_LAUNCH_BARRIER.
  _conflicting_names: _conflicting_names().
  _format_flag: _format_flag().
---
# Module: [`torchtitan/experiments/tpu/tpu_flags.py`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_flags.py)

## Classes
### <a id="FlagMap"></a>`FlagMap`  ·  implements/extends dict
- def: [`torchtitan/experiments/tpu/tpu_flags.py:45`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_flags.py#L45) — documented in [jax-lane](../../../../concepts/jax-lane.md)
- doc: A map of bare flag name -&gt; value, parsed from one command-line string.
- signature: `class FlagMap(dict[str, str]):`
- used by: [`merge_flags`](tpu_flags.md#merge_flags), [`libtpu_init_flags`](tpu_job_config.md#BaseTPUTrainerConfig.libtpu_init_flags), [`parse_flags`](tpu_flags.md#parse_flags), [`HIERARCHICAL_REDUCE_SCATTER`](tpu_flags.md#HIERARCHICAL_REDUCE_SCATTER.HIERARCHICAL_REDUCE_SCATTER), [`SPARSECORE_LATENCY_HIDING_SCHEDULER`](tpu_flags.md#SPARSECORE_LATENCY_HIDING_SCHEDULER.SPARSECORE_LATENCY_HIDING_SCHEDULER), [`_flag_map_rule`](tpu_flags.md#_flag_map_rule), [`ICI_AG_PIPELINING`](tpu_flags.md#ICI_AG_PIPELINING.ICI_AG_PIPELINING), [`SPARSECORE_ASYNC_ALL_GATHER`](tpu_flags.md#SPARSECORE_ASYNC_ALL_GATHER.SPARSECORE_ASYNC_ALL_GATHER), [`TPU7X_THROUGHPUT_P_STATE`](tpu_flags.md#TPU7X_THROUGHPUT_P_STATE.TPU7X_THROUGHPUT_P_STATE), [`xla_flags`](tpu_job_config.md#BaseTPUTrainerConfig.xla_flags), [`SELECTIVE_ICI_RS_PIPELINING`](tpu_flags.md#SELECTIVE_ICI_RS_PIPELINING.SELECTIVE_ICI_RS_PIPELINING), [`resolve_flags`](tpu_flags.md#resolve_flags), [`CONVOLUTION_UNFUSING`](tpu_flags.md#CONVOLUTION_UNFUSING.CONVOLUTION_UNFUSING), [`DUAL_SPARSECORE_REDUCE_SCATTER`](tpu_flags.md#DUAL_SPARSECORE_REDUCE_SCATTER.DUAL_SPARSECORE_REDUCE_SCATTER), [`DISABLE_ENHANCED_LAUNCH_BARRIER`](tpu_flags.md#DISABLE_ENHANCED_LAUNCH_BARRIER.DISABLE_ENHANCED_LAUNCH_BARRIER), [`SPARSECORE_COLLECTIVE_OFFLOAD`](tpu_flags.md#SPARSECORE_COLLECTIVE_OFFLOAD.SPARSECORE_COLLECTIVE_OFFLOAD), [`extra_libtpu_init_flags`](tpu_job_config.md#BaseTPUTrainerConfig.extra_libtpu_init_flags), [`extra_xla_flags`](tpu_job_config.md#BaseTPUTrainerConfig.extra_xla_flags)  (2 test-only)

## Functions
- <a id="_apply_flags"></a>`_apply_flags(env_var: str, config_flags: Mapping[str, str], extra_flags: Mapping[str, str], environ: MutableMapping[str, str])` — [`L231`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_flags.py#L231) — Merges the config and ``extra_`` layers under the existing env var. — documented in [jax-lane](../../../../concepts/jax-lane.md)
- <a id="_conflicting_names"></a>`_conflicting_names(config_flags: Mapping[str, str], env_flags: Mapping[str, str])` — [`L284`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_flags.py#L284) — Returns the flags both maps set, to a different value.
- <a id="_flag_map_rule"></a>`_flag_map_rule(type_info: tyro.constructors.PrimitiveTypeInfo)` — [`L57`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_flags.py#L57) — Parses a ``FlagMap`` field from one ``flag=value ...`` string.
- <a id="_flag_value_str"></a>`_flag_value_str(value: FlagValue)` — [`L295`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_flags.py#L295) — Renders a flag value the way libtpu and XLA parse it.
- <a id="_format_flag"></a>`_format_flag(name: str, value: str)` — [`L304`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_flags.py#L304) — Renders one flag, valueless when the value is empty.
- <a id="_removed_names"></a>`_removed_names(config_flags: Mapping[str, str], extra_flags: Mapping[str, str])` — [`L273`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_flags.py#L273) — Returns the config's flags that ``extra_flags`` asks to remove.
- <a id="apply_init_flags"></a>`apply_init_flags(config, *, environ: MutableMapping[str, str] | None = None)` — [`L109`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_flags.py#L109) — Applies a config's flags, before any TPU device is used. — documented in [jax-lane](../../../../concepts/jax-lane.md)
- <a id="format_flags"></a>`format_flags(flags: Mapping[str, str])` — [`L82`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_flags.py#L82) — Renders a flag map as a command-line string for libtpu or XLA.
- <a id="merge_flags"></a>`merge_flags(*bundles: Mapping[str, FlagValue], **overrides: FlagValue)` — [`L72`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_flags.py#L72) — Merges bundles then keyword overrides, later arguments winning. — documented in [tpu-trainer-and-job-config](../../../../concepts/tpu-trainer-and-job-config.md)
- <a id="parse_flags"></a>`parse_flags(flag_string: str)` — [`L87`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_flags.py#L87) — Parses whitespace-separated ``name=value`` entries; ``!name`` removes. — documented in [tpu-trainer-and-job-config](../../../../concepts/tpu-trainer-and-job-config.md)
- <a id="resolve_flags"></a>`resolve_flags(*layers: Mapping[str, str])` — [`L99`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_flags.py#L99) — Merges flag layers in increasing precedence, dropping removed flags. — documented in [tpu-trainer-and-job-config](../../../../concepts/tpu-trainer-and-job-config.md)

## Module values
- <a id="CONVOLUTION_UNFUSING.CONVOLUTION_UNFUSING"></a>`CONVOLUTION_UNFUSING` — [`L200`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_flags.py#L200)
- <a id="DISABLE_ENHANCED_LAUNCH_BARRIER.DISABLE_ENHANCED_LAUNCH_BARRIER"></a>`DISABLE_ENHANCED_LAUNCH_BARRIER` — [`L226`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_flags.py#L226)
- <a id="DUAL_SPARSECORE_REDUCE_SCATTER.DUAL_SPARSECORE_REDUCE_SCATTER"></a>`DUAL_SPARSECORE_REDUCE_SCATTER` — [`L160`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_flags.py#L160)
- <a id="FlagValue"></a>`FlagValue` — [`L35`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_flags.py#L35)
- <a id="HIERARCHICAL_REDUCE_SCATTER.HIERARCHICAL_REDUCE_SCATTER"></a>`HIERARCHICAL_REDUCE_SCATTER` — [`L169`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_flags.py#L169)
- <a id="ICI_AG_PIPELINING.ICI_AG_PIPELINING"></a>`ICI_AG_PIPELINING` — [`L186`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_flags.py#L186)
- <a id="REMOVE"></a>`REMOVE` — [`L42`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_flags.py#L42)
- <a id="SELECTIVE_ICI_RS_PIPELINING.SELECTIVE_ICI_RS_PIPELINING"></a>`SELECTIVE_ICI_RS_PIPELINING` — [`L178`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_flags.py#L178)
- <a id="SPARSECORE_ASYNC_ALL_GATHER.SPARSECORE_ASYNC_ALL_GATHER"></a>`SPARSECORE_ASYNC_ALL_GATHER` — [`L192`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_flags.py#L192)
- <a id="SPARSECORE_COLLECTIVE_OFFLOAD.SPARSECORE_COLLECTIVE_OFFLOAD"></a>`SPARSECORE_COLLECTIVE_OFFLOAD` — [`L208`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_flags.py#L208)
- <a id="SPARSECORE_LATENCY_HIDING_SCHEDULER.SPARSECORE_LATENCY_HIDING_SCHEDULER"></a>`SPARSECORE_LATENCY_HIDING_SCHEDULER` — [`L150`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_flags.py#L150)
- <a id="TPU7X_THROUGHPUT_P_STATE.TPU7X_THROUGHPUT_P_STATE"></a>`TPU7X_THROUGHPUT_P_STATE` — [`L219`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_flags.py#L219)

