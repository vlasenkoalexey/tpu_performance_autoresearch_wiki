---
title: 'Module: torchtitan/experiments/tpu/grouped_experts.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/grouped_experts.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.grouped_experts`/
symbols:
  TpuGroupedExperts.forward: TpuGroupedExperts#forward().
  TpuGroupedExperts: TpuGroupedExperts#
  TpuGroupedExpertsConverter: TpuGroupedExpertsConverter#
  TpuGroupedExpertsConverter.convert: TpuGroupedExpertsConverter#convert().
  TpuGroupedExperts._native_experts_forward: TpuGroupedExperts#_native_experts_forward().
  TpuGroupedExperts.Config: TpuGroupedExperts#Config#
  TpuGroupedExperts._native_sharding_applied: TpuGroupedExperts#_native_sharding_applied.
  TpuGroupedExpertsConverter.Config: TpuGroupedExpertsConverter#Config#
  TpuGroupedExperts.__init__: TpuGroupedExperts#__init__().
  TpuGroupedExperts._distribute_states: TpuGroupedExperts#_distribute_states().
  _native_weight_sharding: _native_weight_sharding().
  TpuGroupedExperts.w3_EDF: TpuGroupedExperts#w3_EDF.
  TpuGroupedExperts._init_param: TpuGroupedExperts#_init_param().
  TpuGroupedExperts.w1_EDF: TpuGroupedExperts#w1_EDF.
  TpuGroupedExperts.w2_EFD: TpuGroupedExperts#w2_EFD.
  TpuGroupedExperts.use_kernel_native_weight_layout: TpuGroupedExperts#use_kernel_native_weight_layout.
  TpuGroupedExperts.parallelize: TpuGroupedExperts#parallelize().
  TpuGroupedExperts.Config.activation: TpuGroupedExperts#Config#activation.
  TpuGroupedExperts.num_experts: TpuGroupedExperts#num_experts.
  TpuGroupedExperts.Config.use_pallas_grouped_mm: TpuGroupedExperts#Config#use_pallas_grouped_mm.
  TpuGroupedExperts.local_tensor: TpuGroupedExperts#local_tensor().
  TpuGroupedExperts.use_pallas_paired_grouped_mm: TpuGroupedExperts#use_pallas_paired_grouped_mm.
  TpuGroupedExperts.activation: TpuGroupedExperts#activation.
  TpuGroupedExperts.use_pallas_grouped_mm: TpuGroupedExperts#use_pallas_grouped_mm.
  TpuGroupedExperts.pallas_grouped_mm_tgmm_tiling: TpuGroupedExperts#pallas_grouped_mm_tgmm_tiling.
  TpuGroupedExperts._activation_fn: TpuGroupedExperts#_activation_fn().
  _CANONICAL_TO_NATIVE_WEIGHT: _CANONICAL_TO_NATIVE_WEIGHT.
  TpuGroupedExperts._use_transposed_w2_rhs: TpuGroupedExperts#_use_transposed_w2_rhs.
  TpuGroupedExperts.pallas_grouped_mm_tile_m: TpuGroupedExperts#pallas_grouped_mm_tile_m.
  TpuGroupedExperts.pallas_grouped_mm_tile_k: TpuGroupedExperts#pallas_grouped_mm_tile_k.
  TpuGroupedExperts.pallas_grouped_mm_tile_n: TpuGroupedExperts#pallas_grouped_mm_tile_n.
  TpuGroupedExperts.pallas_grouped_mm_w2_tgmm_tiling: TpuGroupedExperts#pallas_grouped_mm_w2_tgmm_tiling.
  TpuGroupedExperts.pallas_grouped_mm_w2_transposed_tgmm_tiling: TpuGroupedExperts#pallas_grouped_mm_w2_transposed_tgmm_tiling.
  TpuGroupedExperts._canonical_weights_on_save: TpuGroupedExperts#_canonical_weights_on_save().
  TpuGroupedExperts._native_weights_on_load: TpuGroupedExperts#_native_weights_on_load().
  TpuGroupedExperts.Config.use_kernel_native_weight_layout: TpuGroupedExperts#Config#use_kernel_native_weight_layout.
  TpuGroupedExpertsConverter.__init__: TpuGroupedExpertsConverter#__init__().
  _transpose_last_two_dims: _transpose_last_two_dims().
  TpuGroupedExperts.Config.use_pallas_paired_grouped_mm: TpuGroupedExperts#Config#use_pallas_paired_grouped_mm.
  TpuGroupedExperts.Config.pallas_grouped_mm_tile_m: TpuGroupedExperts#Config#pallas_grouped_mm_tile_m.
  TpuGroupedExperts.Config.pallas_grouped_mm_tile_k: TpuGroupedExperts#Config#pallas_grouped_mm_tile_k.
  TpuGroupedExperts.Config.pallas_grouped_mm_tile_n: TpuGroupedExperts#Config#pallas_grouped_mm_tile_n.
  TpuGroupedExperts.Config.pallas_grouped_mm_tgmm_tiling: TpuGroupedExperts#Config#pallas_grouped_mm_tgmm_tiling.
  TpuGroupedExperts.Config.pallas_grouped_mm_w2_tgmm_tiling: TpuGroupedExperts#Config#pallas_grouped_mm_w2_tgmm_tiling.
  TpuGroupedExperts.Config.pallas_grouped_mm_w2_transposed_tgmm_tiling: TpuGroupedExperts#Config#pallas_grouped_mm_w2_transposed_tgmm_tiling.
  __all__: __all__.
---
# Module: [`torchtitan/experiments/tpu/grouped_experts.py`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/grouped_experts.py)

## Classes
### <a id="TpuGroupedExperts"></a>`TpuGroupedExperts`  ·  implements/extends GroupedExperts
- def: [`torchtitan/experiments/tpu/grouped_experts.py:90`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/grouped_experts.py#L90) — documented in [tpu-moe-dispatch-and-grouped-experts](../../../../concepts/tpu-moe-dispatch-and-grouped-experts.md)
- doc: TPU expert kernels with opt-in Pallas grouped paths.
- signature: `class TpuGroupedExperts(GroupedExperts):`
- members:
  - <a id="TpuGroupedExperts._canonical_weights_on_save"></a>`_canonical_weights_on_save(module, state_dict, prefix, local_metadata)` — [`L228`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/grouped_experts.py#L228) — Expose kernel-native parameters in canonical checkpoint layout.
  - <a id="TpuGroupedExperts._init_param"></a>`_init_param(self, name: str, param: torch.nn.Parameter)` — [`L189`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/grouped_experts.py#L189) — Initialize native storage through a canonical contiguous tensor.
  - <a id="TpuGroupedExperts._native_experts_forward"></a>`_native_experts_forward(self, x_RD: torch.Tensor, num_tokens_per_expert_E: torch.Tensor)` — [`L248`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/grouped_experts.py#L248) — ``GroupedExperts.forward`` with a configurable activation.
  - <a id="TpuGroupedExperts._native_weights_on_load"></a>`_native_weights_on_load(module, state_dict, prefix, *args)` — [`L238`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/grouped_experts.py#L238) — Load canonical checkpoint tensors into kernel-native storage.
  - <a id="TpuGroupedExperts.forward"></a>`forward(self, x_RD: torch.Tensor, num_tokens_per_expert_E: torch.Tensor, row_scale_R: torch.Tensor | None = None)` — [`L288`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/grouped_experts.py#L288) — Run the experts on expert-sorted rows.
  - <a id="TpuGroupedExperts.local_tensor"></a>`local_tensor(tensor: torch.Tensor)` — [`L308`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/grouped_experts.py#L308)
  - <a id="TpuGroupedExperts.parallelize"></a>`parallelize(self, parallel_dims)` — [`L215`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/grouped_experts.py#L215)
  - <a id="TpuGroupedExperts.activation"></a>`activation` — [`L161`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/grouped_experts.py#L161)
  - <a id="TpuGroupedExperts.num_experts"></a>`num_experts` — [`L146`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/grouped_experts.py#L146)
  - <a id="TpuGroupedExperts.pallas_grouped_mm_tgmm_tiling"></a>`pallas_grouped_mm_tgmm_tiling` — [`L167`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/grouped_experts.py#L167)
  - <a id="TpuGroupedExperts.pallas_grouped_mm_tile_k"></a>`pallas_grouped_mm_tile_k` — [`L165`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/grouped_experts.py#L165)
  - <a id="TpuGroupedExperts.pallas_grouped_mm_tile_m"></a>`pallas_grouped_mm_tile_m` — [`L164`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/grouped_experts.py#L164)
  - <a id="TpuGroupedExperts.pallas_grouped_mm_tile_n"></a>`pallas_grouped_mm_tile_n` — [`L166`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/grouped_experts.py#L166)
  - <a id="TpuGroupedExperts.pallas_grouped_mm_w2_tgmm_tiling"></a>`pallas_grouped_mm_w2_tgmm_tiling` — [`L168`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/grouped_experts.py#L168)
  - <a id="TpuGroupedExperts.pallas_grouped_mm_w2_transposed_tgmm_tiling"></a>`pallas_grouped_mm_w2_transposed_tgmm_tiling` — [`L169`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/grouped_experts.py#L169)
  - <a id="TpuGroupedExperts.use_kernel_native_weight_layout"></a>`use_kernel_native_weight_layout` — [`L172`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/grouped_experts.py#L172)
  - <a id="TpuGroupedExperts.use_pallas_grouped_mm"></a>`use_pallas_grouped_mm` — [`L162`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/grouped_experts.py#L162)
  - <a id="TpuGroupedExperts.use_pallas_paired_grouped_mm"></a>`use_pallas_paired_grouped_mm` — [`L163`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/grouped_experts.py#L163)
  - <a id="TpuGroupedExperts.w1_EDF"></a>`w1_EDF` — [`L147`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/grouped_experts.py#L147)
  - <a id="TpuGroupedExperts.w2_EFD"></a>`w2_EFD` — [`L150`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/grouped_experts.py#L150)
  - <a id="TpuGroupedExperts.w3_EDF"></a>`w3_EDF` — [`L153`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/grouped_experts.py#L153)
- protocol/private: <a id="TpuGroupedExperts.__init__"></a>`__init__`[`L135`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/grouped_experts.py#L135), <a id="TpuGroupedExperts._activation_fn"></a>`_activation_fn`[`L283`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/grouped_experts.py#L283), <a id="TpuGroupedExperts._distribute_states"></a>`_distribute_states`[`L205`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/grouped_experts.py#L205), <a id="TpuGroupedExperts._native_sharding_applied"></a>`_native_sharding_applied`[`L174`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/grouped_experts.py#L174), <a id="TpuGroupedExperts._use_transposed_w2_rhs"></a>`_use_transposed_w2_rhs`[`L173`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/grouped_experts.py#L173)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`get_spmd_backend`](../../distributed/utils.md#get_spmd_backend), [`get_optional_mesh`](../../distributed/parallel_dims.md#ParallelDims.get_optional_mesh), [`parallelize`](../../protocols/module.md#Module.parallelize), [`GroupedExperts`](../../models/common/moe.md#GroupedExperts), [`_distribute_states`](../../protocols/module.md#Module._distribute_states), [`forward`](../../models/common/moe.md#GroupedExperts.forward), [`hidden_dim`](../../models/common/moe.md#GroupedExperts.Config.hidden_dim), [`num_experts`](../../models/common/moe.md#GroupedExperts.Config.num_experts), [`dim`](../../models/common/moe.md#GroupedExperts.Config.dim), [`w2_EDF`](../../models/common/moe.md#GroupedExperts.w2_EDF), [`w1_EFD`](../../models/common/moe.md#GroupedExperts.w1_EFD), [`Config`](grouped_experts.md#TpuGroupedExperts.Config), [`spmd_mesh_size`](../../distributed/spmd_types.md#spmd_mesh_size), [`w3_EFD`](../../models/common/moe.md#GroupedExperts.w3_EFD), [`segment_matmul_pallas_2d`](kernels/expert_segment_matmul.md#segment_matmul_pallas_2d), [`_grouped_mm`](../../models/common/moe.md#GroupedExperts._grouped_mm), [`_sharding_config`](../../protocols/module.md#Module._sharding_config), [`_native_weight_sharding`](grouped_experts.md#_native_weight_sharding), [`paired_segment_matmul_pallas_2d`](kernels/paired_segment_matmul.md#paired_segment_matmul_pallas_2d), [`_init_param`](../../protocols/module.md#Module._init_param), [`activation`](grouped_experts.md#TpuGroupedExperts.Config.activation), [`use_pallas_grouped_mm`](grouped_experts.md#TpuGroupedExperts.Config.use_pallas_grouped_mm), [`__init__`](../../models/common/moe.md#GroupedExperts.__init__), [`_CANONICAL_TO_NATIVE_WEIGHT`](grouped_experts.md#_CANONICAL_TO_NATIVE_WEIGHT), [`use_kernel_native_weight_layout`](grouped_experts.md#TpuGroupedExperts.Config.use_kernel_native_weight_layout), [`pallas_grouped_mm_tgmm_tiling`](grouped_experts.md#TpuGroupedExperts.Config.pallas_grouped_mm_tgmm_tiling), [`pallas_grouped_mm_tile_k`](grouped_experts.md#TpuGroupedExperts.Config.pallas_grouped_mm_tile_k), [`pallas_grouped_mm_tile_m`](grouped_experts.md#TpuGroupedExperts.Config.pallas_grouped_mm_tile_m), [`pallas_grouped_mm_tile_n`](grouped_experts.md#TpuGroupedExperts.Config.pallas_grouped_mm_tile_n), [`pallas_grouped_mm_w2_tgmm_tiling`](grouped_experts.md#TpuGroupedExperts.Config.pallas_grouped_mm_w2_tgmm_tiling), [`pallas_grouped_mm_w2_transposed_tgmm_tiling`](grouped_experts.md#TpuGroupedExperts.Config.pallas_grouped_mm_w2_transposed_tgmm_tiling), [`use_pallas_paired_grouped_mm`](grouped_experts.md#TpuGroupedExperts.Config.use_pallas_paired_grouped_mm)
- used by: [`_qwen3_moe_30b_fsdp_only_full_ac`](qwen3/config_registry.md#_qwen3_moe_30b_fsdp_only_full_ac), [`qwen3_moe_235b_scan`](qwen3/config_registry.md#qwen3_moe_235b_scan), [`_qwen3_moe_235b_fsdp_only`](qwen3/config_registry.md#_qwen3_moe_235b_fsdp_only), [`parallelize`](../../protocols/module.md#Module.parallelize), [`GroupedExperts`](../../models/common/moe.md#GroupedExperts), [`configure_qwen_simple_fsdp_shard_dims`](qwen3_sharding.md#configure_qwen_simple_fsdp_shard_dims), [`_distribute_states`](../../protocols/module.md#Module._distribute_states), [`forward`](../../models/common/moe.md#GroupedExperts.forward), [`convert`](grouped_experts.md#TpuGroupedExpertsConverter.convert), [`_init_param`](../../protocols/module.md#Module._init_param), [`_use_pallas_grouped_mm`](transformers_modeling_backend/model.md#_use_pallas_grouped_mm)  (8 test-only)

### <a id="TpuGroupedExperts.Config"></a>`TpuGroupedExperts.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/tpu/grouped_experts.py:112`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/grouped_experts.py#L112)
- signature: `class Config(GroupedExperts.Config):`
- members:
  - <a id="TpuGroupedExperts.Config.activation"></a>`activation` — [`L113`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/grouped_experts.py#L113)
  - <a id="TpuGroupedExperts.Config.pallas_grouped_mm_tgmm_tiling"></a>`pallas_grouped_mm_tgmm_tiling` — [`L120`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/grouped_experts.py#L120)
  - <a id="TpuGroupedExperts.Config.pallas_grouped_mm_tile_k"></a>`pallas_grouped_mm_tile_k` — [`L118`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/grouped_experts.py#L118)
  - <a id="TpuGroupedExperts.Config.pallas_grouped_mm_tile_m"></a>`pallas_grouped_mm_tile_m` — [`L117`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/grouped_experts.py#L117)
  - <a id="TpuGroupedExperts.Config.pallas_grouped_mm_tile_n"></a>`pallas_grouped_mm_tile_n` — [`L119`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/grouped_experts.py#L119)
  - <a id="TpuGroupedExperts.Config.pallas_grouped_mm_w2_tgmm_tiling"></a>`pallas_grouped_mm_w2_tgmm_tiling` — [`L124`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/grouped_experts.py#L124)
  - <a id="TpuGroupedExperts.Config.pallas_grouped_mm_w2_transposed_tgmm_tiling"></a>`pallas_grouped_mm_w2_transposed_tgmm_tiling` — [`L130`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/grouped_experts.py#L130)
  - <a id="TpuGroupedExperts.Config.use_kernel_native_weight_layout"></a>`use_kernel_native_weight_layout` — [`L133`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/grouped_experts.py#L133)
  - <a id="TpuGroupedExperts.Config.use_pallas_grouped_mm"></a>`use_pallas_grouped_mm` — [`L114`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/grouped_experts.py#L114)
  - <a id="TpuGroupedExperts.Config.use_pallas_paired_grouped_mm"></a>`use_pallas_paired_grouped_mm` — [`L116`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/grouped_experts.py#L116)
- uses (calls/refs, reference-scoped): [`GroupedExperts`](../../models/common/moe.md#GroupedExperts), [`Config`](../../models/common/moe.md#GroupedExperts.Config)
- used by: [`_qwen3_moe_30b_fsdp_only_full_ac`](qwen3/config_registry.md#_qwen3_moe_30b_fsdp_only_full_ac), [`qwen3_moe_235b_scan`](qwen3/config_registry.md#qwen3_moe_235b_scan), [`_qwen3_moe_235b_fsdp_only`](qwen3/config_registry.md#_qwen3_moe_235b_fsdp_only), [`convert`](grouped_experts.md#TpuGroupedExpertsConverter.convert), [`__init__`](grouped_experts.md#TpuGroupedExperts.__init__), [`use_kernel_native_weight_layout`](grouped_experts.md#TpuGroupedExperts.use_kernel_native_weight_layout), [`_use_pallas_grouped_mm`](transformers_modeling_backend/model.md#_use_pallas_grouped_mm), [`use_pallas_paired_grouped_mm`](grouped_experts.md#TpuGroupedExperts.use_pallas_paired_grouped_mm), [`activation`](grouped_experts.md#TpuGroupedExperts.activation), [`pallas_grouped_mm_tgmm_tiling`](grouped_experts.md#TpuGroupedExperts.pallas_grouped_mm_tgmm_tiling), [`use_pallas_grouped_mm`](grouped_experts.md#TpuGroupedExperts.use_pallas_grouped_mm), [`pallas_grouped_mm_tile_k`](grouped_experts.md#TpuGroupedExperts.pallas_grouped_mm_tile_k), [`pallas_grouped_mm_tile_m`](grouped_experts.md#TpuGroupedExperts.pallas_grouped_mm_tile_m), [`pallas_grouped_mm_tile_n`](grouped_experts.md#TpuGroupedExperts.pallas_grouped_mm_tile_n), [`pallas_grouped_mm_w2_tgmm_tiling`](grouped_experts.md#TpuGroupedExperts.pallas_grouped_mm_w2_tgmm_tiling), [`pallas_grouped_mm_w2_transposed_tgmm_tiling`](grouped_experts.md#TpuGroupedExperts.pallas_grouped_mm_w2_transposed_tgmm_tiling)  (6 test-only)

### <a id="TpuGroupedExpertsConverter"></a>`TpuGroupedExpertsConverter`  ·  implements/extends ModelConfigConverter
- def: [`torchtitan/experiments/tpu/grouped_experts.py:396`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/grouped_experts.py#L396) — documented in [tpu-moe-dispatch-and-grouped-experts](../../../../concepts/tpu-moe-dispatch-and-grouped-experts.md)
- doc: Select the TPU grouped-expert implementation before construction.
- signature: `class TpuGroupedExpertsConverter(ModelConfigConverter):`
- members:
  - <a id="TpuGroupedExpertsConverter.convert"></a>`convert(self, model_config)` — [`L406`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/grouped_experts.py#L406)
- protocol/private: <a id="TpuGroupedExpertsConverter.__init__"></a>`__init__`[`L403`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/grouped_experts.py#L403)
- uses (calls/refs, reference-scoped): [`logger`](../../tools/logging.md#logger), [`ModelConfigConverter`](../../protocols/model.md#ModelConfigConverter), [`GroupedExperts`](../../models/common/moe.md#GroupedExperts), [`derive`](../../config/override.md#derive), [`traverse`](../../config/configurable.md#Configurable.Config.traverse), [`TpuGroupedExperts`](grouped_experts.md#TpuGroupedExperts), [`Config`](../../models/common/moe.md#GroupedExperts.Config), [`Config`](grouped_experts.md#TpuGroupedExperts.Config), [`Config`](grouped_experts.md#TpuGroupedExpertsConverter.Config)
- used by: [`qwen3_moe_30b`](qwen3/config_registry.md#qwen3_moe_30b), [`qwen3_moe_235b_scan`](qwen3/config_registry.md#qwen3_moe_235b_scan), [`_qwen3_moe_235b_fsdp_only`](qwen3/config_registry.md#_qwen3_moe_235b_fsdp_only), [`ModelConfigConverter`](../../protocols/model.md#ModelConfigConverter), [`convert`](../../protocols/model.md#ModelConfigConverter.convert), [`substitute_tpu_experts`](transformers_modeling_backend/model.md#substitute_tpu_experts), [`_TPU_MOE_CONVERTERS`](qwen3_5/config_registry.md#_TPU_MOE_CONVERTERS)  (5 test-only)

### <a id="TpuGroupedExpertsConverter.Config"></a>`TpuGroupedExpertsConverter.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/tpu/grouped_experts.py:400`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/grouped_experts.py#L400)
- signature: `class Config(ModelConfigConverter.Config):`
- uses (calls/refs, reference-scoped): [`ModelConfigConverter`](../../protocols/model.md#ModelConfigConverter), [`Config`](../../protocols/model.md#ModelConfigConverter.Config)
- used by: [`qwen3_moe_30b`](qwen3/config_registry.md#qwen3_moe_30b), [`qwen3_moe_235b_scan`](qwen3/config_registry.md#qwen3_moe_235b_scan), [`_qwen3_moe_235b_fsdp_only`](qwen3/config_registry.md#_qwen3_moe_235b_fsdp_only), [`substitute_tpu_experts`](transformers_modeling_backend/model.md#substitute_tpu_experts), [`_TPU_MOE_CONVERTERS`](qwen3_5/config_registry.md#_TPU_MOE_CONVERTERS), [`__init__`](grouped_experts.md#TpuGroupedExpertsConverter.__init__)  (5 test-only)

## Functions
- <a id="_native_weight_sharding"></a>`_native_weight_sharding(config: ShardingConfig)` — [`L79`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/grouped_experts.py#L79) — Map canonical expert state names/layouts to kernel-native storage.
- <a id="_transpose_last_two_dims"></a>`_transpose_last_two_dims(layout: spmd.SpmdType, *, ndim: int = 3)` — [`L31`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/grouped_experts.py#L31) — Transpose tensor-dimension references in an SPMD layout.

## Module values
- <a id="_CANONICAL_TO_NATIVE_WEIGHT"></a>`_CANONICAL_TO_NATIVE_WEIGHT` — [`L24`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/grouped_experts.py#L24)
- <a id="__all__"></a>`__all__` — [`L422`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/grouped_experts.py#L422)

