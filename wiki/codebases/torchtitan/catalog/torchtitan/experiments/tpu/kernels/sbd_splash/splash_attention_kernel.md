---
title: 'Module: torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.kernels.sbd_splash.splash_attention_kernel`/
symbols:
  _splash_attention_forward: _splash_attention_forward().
  _splash_attention_bwd_dkv: _splash_attention_bwd_dkv().
  _flash_attention_dkv_kernel.body: _flash_attention_dkv_kernel().body().
  flash_attention_kernel.body: flash_attention_kernel().body().
  SplashConfig.__post_init__: SplashConfig#__post_init__().
  _make_splash_attention: _make_splash_attention().
  _make_dynamic_splash_attention: _make_dynamic_splash_attention().
  flash_attention_kernel: flash_attention_kernel().
  _flash_attention_dkv_kernel: _flash_attention_dkv_kernel().
  NUM_LANES: NUM_LANES.
  _splash_attention_bwd: _splash_attention_bwd().
  SplashAttentionKernel.manual_sharding_spec: SplashAttentionKernel#manual_sharding_spec().
  SplashConfig.get_default: SplashConfig#get_default().
  _splash_attention_custom: _splash_attention_custom().
  SplashConfig.use_base2_exp: SplashConfig#use_base2_exp.
  _flash_attention_dq_kernel.body: _flash_attention_dq_kernel().body().
  _splash_attention_fwd: _splash_attention_fwd().
  SplashConfig.dropout_rate: SplashConfig#dropout_rate.
  _flash_attention_dq_kernel: _flash_attention_dq_kernel().
  SplashConfig.bias_per_key_rows: SplashConfig#bias_per_key_rows.
  MaskInfo: MaskInfo.
  _splash_attention: _splash_attention().
  NUM_SUBLANES: NUM_SUBLANES.
  LOG2E: LOG2E.
  _mix_dropout_seed: _mix_dropout_seed().
  SplashConfig.dropout_mask_version: SplashConfig#dropout_mask_version.
  QKVLayout: QKVLayout#
  SplashConfig.k_layout: SplashConfig#k_layout.
  _make_dynamic_splash_attention.process_mask_shard: _make_dynamic_splash_attention().process_mask_shard().
  _hash_keep_bool: _hash_keep_bool().
  _splash_attention_bwd_dkv.unravel: _splash_attention_bwd_dkv().unravel().
  SplashAttentionKernel.fwd_mask_info: SplashAttentionKernel#fwd_mask_info.
  from_head_minor: from_head_minor().
  SplashConfig: SplashConfig#
  SplashConfig.q_layout: SplashConfig#q_layout.
  partial: partial.
  QKVLayout.HEAD_DIM_MINOR: QKVLayout#HEAD_DIM_MINOR.
  SplashConfig.v_layout: SplashConfig#v_layout.
  SplashConfig.has_backward_blocks: SplashConfig#has_backward_blocks().
  _splash_attention_forward.unravel: _splash_attention_forward().unravel().
  SplashAttentionKernel.__call__: SplashAttentionKernel#__call__().
  SplashConfig.block_q_dkv: SplashConfig#block_q_dkv.
  flash_attention_kernel._gen_dropout_keep: flash_attention_kernel()._gen_dropout_keep().
  _apply_mask_and_soft_cap: _apply_mask_and_soft_cap().
  DROPOUT_QUANTUM: DROPOUT_QUANTUM.
  SplashConfig.block_q: SplashConfig#block_q.
  SplashConfig.block_kv_dkv: SplashConfig#block_kv_dkv.
  flash_attention_kernel.end: flash_attention_kernel().end().
  MaskFunctionType: MaskFunctionType.
  SplashConfig.block_kv: SplashConfig#block_kv.
  SplashConfig.block_kv_dkv_compute: SplashConfig#block_kv_dkv_compute.
  NN_DIM_NUMBERS: NN_DIM_NUMBERS.
  NT_DIM_NUMBERS: NT_DIM_NUMBERS.
  SplashConfig.block_kv_compute: SplashConfig#block_kv_compute.
  SplashAttentionKernel.tree_flatten: SplashAttentionKernel#tree_flatten().
  SplashConfig.dropout_fold_rescale: SplashConfig#dropout_fold_rescale.
  to_i32: to_i32.
  SplashAttentionKernel.dkv_mask_info: SplashAttentionKernel#dkv_mask_info.
  make_splash_mha: make_splash_mha.
  SplashConfig.dq_reduction_steps: SplashConfig#dq_reduction_steps.
  SplashConfig.qk_diag_grid: SplashConfig#qk_diag_grid.
  _splash_attention_forward.create_kv_index_map.index_map: _splash_attention_forward().create_kv_index_map().index_map().
  _splash_attention_bwd_dkv.create_kv_index_map.index_map: _splash_attention_bwd_dkv().create_kv_index_map().index_map().
  _splash_attention_bwd_dkv._bwd_cost_estimate: _splash_attention_bwd_dkv()._bwd_cost_estimate().
  SplashAttentionKernel: SplashAttentionKernel#
  _make_dynamic_splash_attention.process_all_shards: _make_dynamic_splash_attention().process_all_shards().
  make_splash_mqa: make_splash_mqa.
  SplashConfig.attn_logits_soft_cap: SplashConfig#attn_logits_soft_cap.
  flash_attention_kernel.init: flash_attention_kernel().init().
  SplashAttentionKernel.tree_unflatten: SplashAttentionKernel#tree_unflatten().
  make_splash_mha_single_device: make_splash_mha_single_device.
  make_splash_mqa_single_device: make_splash_mqa_single_device.
  make_dynamic_splash_mqa: make_dynamic_splash_mqa.
  make_dynamic_splash_mha: make_dynamic_splash_mha.
  _splash_attention_forward.create_kv_index_map: _splash_attention_forward().create_kv_index_map().
  _splash_attention_bwd_dkv.mask_index_map: _splash_attention_bwd_dkv().mask_index_map().
  _splash_attention_bwd_dkv.create_kv_index_map: _splash_attention_bwd_dkv().create_kv_index_map().
  _not: _not().
  SplashConfig.qk_diag_skip: SplashConfig#qk_diag_skip.
  SplashConfig.dropout_mask_as_multiplier: SplashConfig#dropout_mask_as_multiplier.
  SplashConfig.bias_per_key_dbias: SplashConfig#bias_per_key_dbias.
  SplashConfig.dropout_bwd_fused_compare: SplashConfig#dropout_bwd_fused_compare.
  _bytes: _bytes().
  _splash_attention_forward.unravel.index_map: _splash_attention_forward().unravel().index_map().
  _splash_attention_forward.mask_index_map: _splash_attention_forward().mask_index_map().
  _splash_attention_forward._fwd_cost_estimate: _splash_attention_forward()._fwd_cost_estimate().
  _splash_attention_bwd_dkv.unravel.index_map: _splash_attention_bwd_dkv().unravel().index_map().
  _splash_attention_bwd_dkv.create_dkv_index_map: _splash_attention_bwd_dkv().create_dkv_index_map().
  SplashConfig.residual_checkpoint_name: SplashConfig#residual_checkpoint_name.
  SplashConfig.max_logit_const: SplashConfig#max_logit_const.
  SplashConfig.use_experimental_scheduler: SplashConfig#use_experimental_scheduler.
  SplashConfig.bias_per_key_dbias_scratch: SplashConfig#bias_per_key_dbias_scratch.
  SplashConfig.dropout_single_bwd_apply: SplashConfig#dropout_single_bwd_apply.
  SplashConfig.dropout_bwd_fused_compare_bf16: SplashConfig#dropout_bwd_fused_compare_bf16.
  SplashConfig.dropout_bwd_bf16_mask: SplashConfig#dropout_bwd_bf16_mask.
  _div: _div().
  _splash_attention_forward.init_if_empty: _splash_attention_forward().init_if_empty().
  SplashAttentionKernel.kwargs: SplashAttentionKernel#kwargs.
  LOG2E_INV: LOG2E_INV.
  _flash_attention_dkv_kernel.init_dbias: _flash_attention_dkv_kernel().init_dbias().
  SplashAttentionKernel.__init__: SplashAttentionKernel#__init__().
  _and: _and().
  get_kernel_name: get_kernel_name().
  SplashConfig.fuse_reciprocal: SplashConfig#fuse_reciprocal.
  SplashConfig.interpret: SplashConfig#interpret.
  SplashConfig.bias_per_key_dbias_mxu_reduce: SplashConfig#bias_per_key_dbias_mxu_reduce.
  SplashConfig.dropout_cheap_construction: SplashConfig#dropout_cheap_construction.
  SplashConfig.dropout_int_construction: SplashConfig#dropout_int_construction.
  SplashConfig.dropout_probe_single_draw: SplashConfig#dropout_probe_single_draw.
  SplashConfig.dropout_probe_half_area: SplashConfig#dropout_probe_half_area.
  _apply_mask_and_soft_cap.cap_logits: _apply_mask_and_soft_cap().cap_logits().
  _flash_attention_dkv_kernel.body._load_kv: _flash_attention_dkv_kernel().body()._load_kv().
  _H_C1: _H_C1.
  _H_C2: _H_C2.
  _H_C3: _H_C3.
  _H_C4: _H_C4.
  _H_C5: _H_C5.
  SegmentIds: SegmentIds#
  SegmentIds.q: SegmentIds#q.
  SegmentIds.kv: SegmentIds#kv.
  SplashConfig.block_q_dq: SplashConfig#block_q_dq.
  SplashConfig.block_kv_dq: SplashConfig#block_kv_dq.
  SplashConfig.use_fused_bwd_kernel: SplashConfig#use_fused_bwd_kernel.
  SplashConfig.num_stacked_q_heads: SplashConfig#num_stacked_q_heads.
  SplashConfig.fwd_cost_estimate: SplashConfig#fwd_cost_estimate.
  SplashConfig.bwd_cost_estimate: SplashConfig#bwd_cost_estimate.
  SplashConfig.dropout_hoist_gen: SplashConfig#dropout_hoist_gen.
  SplashConfig.dropout_dkv_no_unroll: SplashConfig#dropout_dkv_no_unroll.
  P: P.
  QKVLayout.SEQ_MINOR: QKVLayout#SEQ_MINOR.
  _flash_attention_dq_kernel.init: _flash_attention_dq_kernel().init().
  _flash_attention_dq_kernel.end: _flash_attention_dq_kernel().end().
  _flash_attention_dkv_kernel.init: _flash_attention_dkv_kernel().init().
  _flash_attention_dkv_kernel.init_dbias_pk_scratch: _flash_attention_dkv_kernel().init_dbias_pk_scratch().
  _flash_attention_dkv_kernel.write_dbias_pk: _flash_attention_dkv_kernel().write_dbias_pk().
  _flash_attention_dkv_kernel.init_dbias_pk: _flash_attention_dkv_kernel().init_dbias_pk().
---
# Module: [`torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py)

## Classes
### <a id="QKVLayout"></a>`QKVLayout`  ·  implements/extends IntEnum
- def: [`torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py:155`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L155)
- signature: `class QKVLayout(enum.IntEnum):`
- members:
  - <a id="QKVLayout.HEAD_DIM_MINOR"></a>`HEAD_DIM_MINOR` — [`L156`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L156)
  - <a id="QKVLayout.SEQ_MINOR"></a>`SEQ_MINOR` — [`L157`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L157)
- used by: [`_splash_attention_forward`](splash_attention_kernel.md#_splash_attention_forward), [`_splash_attention_bwd_dkv`](splash_attention_kernel.md#_splash_attention_bwd_dkv), [`_flash_attention_dkv_kernel`](splash_attention_kernel.md#_flash_attention_dkv_kernel), [`flash_attention_kernel`](splash_attention_kernel.md#flash_attention_kernel), [`_flash_attention_dq_kernel`](splash_attention_kernel.md#_flash_attention_dq_kernel), [`k_layout`](splash_attention_kernel.md#SplashConfig.k_layout), [`from_head_minor`](splash_attention_kernel.md#from_head_minor), [`q_layout`](splash_attention_kernel.md#SplashConfig.q_layout), [`v_layout`](splash_attention_kernel.md#SplashConfig.v_layout)

### <a id="SegmentIds"></a>`SegmentIds`  ·  implements/extends NamedTuple
- def: [`torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py:112`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L112)
- doc: SegmentIds for Q and KV sequences.
- signature: `class SegmentIds(NamedTuple):`
- members:
  - <a id="SegmentIds.kv"></a>`kv` — [`L133`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L133)
  - <a id="SegmentIds.q"></a>`q` — [`L132`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L132)
- used by: [`_segment_ids`](../splash_bias_dropout.md#_segment_ids)

### <a id="SplashAttentionKernel"></a>`SplashAttentionKernel`
- def: [`torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py:3281`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L3281) — documented in [tpu-pallas-kernels](../../../../../../concepts/tpu-pallas-kernels.md)
- signature: `class SplashAttentionKernel:`
- members:
  - <a id="SplashAttentionKernel.manual_sharding_spec"></a>`manual_sharding_spec(self, sharding: jax.sharding.NamedSharding)` — [`L3301`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L3301) — Returns a value that can be used as a shard_map partition spec for the kernel. — documented in [tpu-pallas-kernels](../../../../../../concepts/tpu-pallas-kernels.md)
  - <a id="SplashAttentionKernel.tree_flatten"></a>`tree_flatten(self)` — [`L3333`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L3333)
  - <a id="SplashAttentionKernel.tree_unflatten"></a>`tree_unflatten(cls, kwargs, values)` — [`L3337`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L3337)
  - <a id="SplashAttentionKernel.dkv_mask_info"></a>`dkv_mask_info` — [`L3291`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L3291)
  - <a id="SplashAttentionKernel.fwd_mask_info"></a>`fwd_mask_info` — [`L3290`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L3290)
  - <a id="SplashAttentionKernel.kwargs"></a>`kwargs` — [`L3289`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L3289)
- protocol/private: <a id="SplashAttentionKernel.__call__"></a>`__call__`[`L3293`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L3293), <a id="SplashAttentionKernel.__init__"></a>`__init__`[`L3283`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L3283)
- uses (calls/refs, reference-scoped): [`MaskInfo`](splash_attention_kernel.md#MaskInfo), [`_splash_attention`](splash_attention_kernel.md#_splash_attention), [`block_mask`](splash_attention_mask_info.md#MaskInfo.block_mask), [`partial_mask_blocks`](splash_attention_mask_info.md#MaskInfo.partial_mask_blocks), [`active_rows`](splash_attention_mask_info.md#MaskInfo.active_rows), [`q_sequence`](splash_attention_mask_info.md#MaskInfo.q_sequence), [`num_active_blocks`](splash_attention_mask_info.md#MaskInfo.num_active_blocks), [`active_cols`](splash_attention_mask_info.md#MaskInfo.active_cols), [`mask_next`](splash_attention_mask_info.md#MaskInfo.mask_next)
- used by: [`_make_splash_attention`](splash_attention_kernel.md#_make_splash_attention), [`_make_dynamic_splash_attention`](splash_attention_kernel.md#_make_dynamic_splash_attention)  (2 test-only)

### <a id="SplashConfig"></a>`SplashConfig`
- def: [`torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py:167`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L167) — documented in [tpu-pallas-kernels](../../../../../../concepts/tpu-pallas-kernels.md)
- doc: Tile sizes parameterizing SplashAttention kernels.
- signature: `class SplashConfig:`
- members:
  - <a id="SplashConfig.get_default"></a>`get_default(cls)` — [`L445`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L445) — documented in [tpu-pallas-kernels](../../../../../../concepts/tpu-pallas-kernels.md)
  - <a id="SplashConfig.has_backward_blocks"></a>`has_backward_blocks(self)` — [`L436`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L436)
  - <a id="SplashConfig.attn_logits_soft_cap"></a>`attn_logits_soft_cap` — [`L199`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L199)
  - <a id="SplashConfig.bias_per_key_dbias"></a>`bias_per_key_dbias` — [`L270`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L270)
  - <a id="SplashConfig.bias_per_key_dbias_mxu_reduce"></a>`bias_per_key_dbias_mxu_reduce` — [`L274`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L274)
  - <a id="SplashConfig.bias_per_key_dbias_scratch"></a>`bias_per_key_dbias_scratch` — [`L278`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L278)
  - <a id="SplashConfig.bias_per_key_rows"></a>`bias_per_key_rows` — [`L262`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L262)
  - <a id="SplashConfig.block_kv"></a>`block_kv` — [`L179`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L179)
  - <a id="SplashConfig.block_kv_compute"></a>`block_kv_compute` — [`L180`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L180)
  - <a id="SplashConfig.block_kv_dkv"></a>`block_kv_dkv` — [`L183`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L183)
  - <a id="SplashConfig.block_kv_dkv_compute"></a>`block_kv_dkv_compute` — [`L184`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L184)
  - <a id="SplashConfig.block_kv_dq"></a>`block_kv_dq` — [`L188`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L188)
  - <a id="SplashConfig.block_q"></a>`block_q` — [`L178`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L178)
  - <a id="SplashConfig.block_q_dkv"></a>`block_q_dkv` — [`L182`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L182)
  - <a id="SplashConfig.block_q_dq"></a>`block_q_dq` — [`L187`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L187)
  - <a id="SplashConfig.bwd_cost_estimate"></a>`bwd_cost_estimate` — [`L196`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L196)
  - <a id="SplashConfig.dq_reduction_steps"></a>`dq_reduction_steps` — [`L208`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L208)
  - <a id="SplashConfig.dropout_bwd_bf16_mask"></a>`dropout_bwd_bf16_mask` — [`L301`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L301)
  - <a id="SplashConfig.dropout_bwd_fused_compare"></a>`dropout_bwd_fused_compare` — [`L289`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L289)
  - <a id="SplashConfig.dropout_bwd_fused_compare_bf16"></a>`dropout_bwd_fused_compare_bf16` — [`L294`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L294)
  - <a id="SplashConfig.dropout_cheap_construction"></a>`dropout_cheap_construction` — [`L311`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L311)
  - <a id="SplashConfig.dropout_dkv_no_unroll"></a>`dropout_dkv_no_unroll` — [`L305`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L305)
  - <a id="SplashConfig.dropout_fold_rescale"></a>`dropout_fold_rescale` — [`L252`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L252)
  - <a id="SplashConfig.dropout_hoist_gen"></a>`dropout_hoist_gen` — [`L244`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L244)
  - <a id="SplashConfig.dropout_int_construction"></a>`dropout_int_construction` — [`L318`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L318)
  - <a id="SplashConfig.dropout_mask_as_multiplier"></a>`dropout_mask_as_multiplier` — [`L255`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L255)
  - <a id="SplashConfig.dropout_mask_version"></a>`dropout_mask_version` — [`L239`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L239)
  - <a id="SplashConfig.dropout_probe_half_area"></a>`dropout_probe_half_area` — [`L329`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L329)
  - <a id="SplashConfig.dropout_probe_single_draw"></a>`dropout_probe_single_draw` — [`L324`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L324)
  - <a id="SplashConfig.dropout_rate"></a>`dropout_rate` — [`L234`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L234) — documented in [tpu-pallas-kernels](../../../../../../concepts/tpu-pallas-kernels.md)
  - <a id="SplashConfig.dropout_single_bwd_apply"></a>`dropout_single_bwd_apply` — [`L283`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L283)
  - <a id="SplashConfig.fuse_reciprocal"></a>`fuse_reciprocal` — [`L200`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L200)
  - <a id="SplashConfig.fwd_cost_estimate"></a>`fwd_cost_estimate` — [`L195`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L195)
  - <a id="SplashConfig.interpret"></a>`interpret` — [`L203`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L203)
  - <a id="SplashConfig.k_layout"></a>`k_layout` — [`L192`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L192)
  - <a id="SplashConfig.max_logit_const"></a>`max_logit_const` — [`L202`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L202)
  - <a id="SplashConfig.num_stacked_q_heads"></a>`num_stacked_q_heads` — [`L190`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L190)
  - <a id="SplashConfig.q_layout"></a>`q_layout` — [`L191`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L191)
  - <a id="SplashConfig.qk_diag_grid"></a>`qk_diag_grid` — [`L226`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L226)
  - <a id="SplashConfig.qk_diag_skip"></a>`qk_diag_skip` — [`L221`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L221)
  - <a id="SplashConfig.residual_checkpoint_name"></a>`residual_checkpoint_name` — [`L198`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L198)
  - <a id="SplashConfig.use_base2_exp"></a>`use_base2_exp` — [`L201`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L201) — documented in [tpu-pallas-kernels](../../../../../../concepts/tpu-pallas-kernels.md)
  - <a id="SplashConfig.use_experimental_scheduler"></a>`use_experimental_scheduler` — [`L210`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L210)
  - <a id="SplashConfig.use_fused_bwd_kernel"></a>`use_fused_bwd_kernel` — [`L189`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L189)
  - <a id="SplashConfig.v_layout"></a>`v_layout` — [`L193`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L193)
- protocol/private: <a id="SplashConfig.__post_init__"></a>`__post_init__`[`L339`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L339)
- uses (calls/refs, reference-scoped): [`QKVLayout`](splash_attention_kernel.md#QKVLayout), [`HEAD_DIM_MINOR`](splash_attention_kernel.md#QKVLayout.HEAD_DIM_MINOR)
- used by: [`_splash_attention_forward`](splash_attention_kernel.md#_splash_attention_forward), [`_splash_attention_bwd_dkv`](splash_attention_kernel.md#_splash_attention_bwd_dkv), [`body`](splash_attention_kernel.md#_flash_attention_dkv_kernel.body), [`body`](splash_attention_kernel.md#flash_attention_kernel.body), [`_build_kernel`](../splash_bias_dropout.md#_build_kernel), [`_make_splash_attention`](splash_attention_kernel.md#_make_splash_attention), [`_make_dynamic_splash_attention`](splash_attention_kernel.md#_make_dynamic_splash_attention), [`_flash_attention_dkv_kernel`](splash_attention_kernel.md#_flash_attention_dkv_kernel), [`flash_attention_kernel`](splash_attention_kernel.md#flash_attention_kernel), [`_splash_attention_bwd`](splash_attention_kernel.md#_splash_attention_bwd), [`_splash_attention_custom`](splash_attention_kernel.md#_splash_attention_custom), [`body`](splash_attention_kernel.md#_flash_attention_dq_kernel.body), [`_splash_attention_fwd`](splash_attention_kernel.md#_splash_attention_fwd), [`_flash_attention_dq_kernel`](splash_attention_kernel.md#_flash_attention_dq_kernel), [`_splash_attention`](splash_attention_kernel.md#_splash_attention), [`process_mask_shard`](splash_attention_kernel.md#_make_dynamic_splash_attention.process_mask_shard), [`_bwd_b`](../splash_bias_dropout.md#sbd_attention_bwd._bwd_b), [`_fwd_b`](../splash_bias_dropout.md#sbd_attention_fwd._fwd_b), [`_gen_dropout_keep`](splash_attention_kernel.md#flash_attention_kernel._gen_dropout_keep), [`end`](splash_attention_kernel.md#flash_attention_kernel.end), [`_bwd_cost_estimate`](splash_attention_kernel.md#_splash_attention_bwd_dkv._bwd_cost_estimate), [`init`](splash_attention_kernel.md#flash_attention_kernel.init)

## Functions
- <a id="_and"></a>`_and(x: jax.Array | bool, y: jax.Array | bool)` — [`L104`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L104)
- <a id="_apply_mask_and_soft_cap"></a>`_apply_mask_and_soft_cap(qk: jax.Array, mask_value: float, mask_ref, q_sequence_ref, q_segment_ids_ref, kv_segment_ids_ref, *, attn_logits_soft_cap: float | None, k_slice: pl.Slice, k_offset: int | jax.Array, bq: int, k_in_lanes=True, mask_function=None, has_partial_mask: bool = False)` — [`L463`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L463)
- <a id="_splash_attention_bwd_dkv._bwd_cost_estimate"></a>`_bwd_cost_estimate(q: jax.Array, k: jax.Array, v: jax.Array, q_segment_ids: jax.Array | None, kv_segment_ids: jax.Array | None, logsumexp: jax.Array, do: jax.Array, di: jax.Array, partial_mask_blocks: jax.Array | None, q_sequence: jax.Array | None, out_shapes: list[jax.ShapeDtypeStruct], mask_sparsity_factor: float)` — [`L3008`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L3008)
- <a id="_bytes"></a>`_bytes(x: jax.Array | jax.ShapeDtypeStruct | None)` — [`L1100`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L1100)
- <a id="_div"></a>`_div(dividend: int, divisor: int)` — [`L1093`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L1093)
- <a id="_flash_attention_dkv_kernel"></a>`_flash_attention_dkv_kernel(active_rows_ref, active_cols_ref, mask_next_ref, bounds_start_ref, bounds_end_ref, block_mask_ref, q_ref, k_ref, v_ref, bias_ref, dropout_mask_ref, dropout_seed_ref, q_segment_ids_ref, kv_segment_ids_ref, logsumexp_ref, do_ref, di_ref, mask_ref, q_sequence_ref, dq_alias, dk_alias, dv_alias, dbias_alias, dq_ref, dk_ref, dv_ref, dbias_ref, dq_scratch_ref, dk_scratch_ref, dv_scratch_ref, dbias_scratch_ref=None, *, mask_value: float, q_steps: int, bq: int, bkv_compute: int, bkv: int, mask_function: MaskFunctionType | None, bias_function=None, q_heads_per_kv_head: int, config: SplashConfig)` — [`L1933`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L1933) — documented in [tpu-pallas-kernels](../../../../../../concepts/tpu-pallas-kernels.md)
- <a id="_flash_attention_dq_kernel"></a>`_flash_attention_dq_kernel(active_rows_ref, active_cols_ref, mask_next_ref, bounds_start_ref, bounds_end_ref, block_mask_ref, q_ref, k_ref, v_ref, q_segment_ids_ref, kv_segment_ids_ref, logsumexp_ref, do_ref, di_ref, mask_ref, q_sequence_ref, dq_scratch_ref, dq_ref, *, mask_value: float, kv_steps: int, bq: int, bkv: int, mask_function: MaskFunctionType | None, config: SplashConfig)` — [`L1808`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L1808) — documented in [tpu-pallas-kernels](../../../../../../concepts/tpu-pallas-kernels.md)
- <a id="_splash_attention_forward._fwd_cost_estimate"></a>`_fwd_cost_estimate(q: jax.Array, k: jax.Array, v: jax.Array, bias: jax.Array | None, dropout_mask: jax.Array | None, q_segment_ids: jax.Array | None, kv_segment_ids: jax.Array | None, partial_mask_blocks: jax.Array | None, out_shapes: list[jax.ShapeDtypeStruct], mask_sparsity: float)` — [`L1488`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L1488)
- <a id="flash_attention_kernel._gen_dropout_keep"></a>`_gen_dropout_keep(kv_compute_index, slice_k)` — [`L676`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L676)
- <a id="_hash_keep_bool"></a>`_hash_keep_bool(w0, w1, h, q_abs, kv_abs, rate)` — [`L81`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L81) — Vector i32 mix -> bool keep tile in the CALLER's layout.
- <a id="_flash_attention_dkv_kernel.body._load_kv"></a>`_load_kv(ref, layout)` — [`L2081`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L2081)
- <a id="_make_dynamic_splash_attention"></a>`_make_dynamic_splash_attention(mask: jax.Array, *, mesh: jax.sharding.Mesh | None = None, mask_spec: jax.sharding.PartitionSpec | None = None, config: SplashConfig | None = None, is_mqa: bool, save_residuals: bool = False, mask_value: float = base.DEFAULT_MASK_VALUE, downcast_smem_data: bool = True, partial_mask_blocks_dtype: jax.typing.DTypeLike = np.int8)` — [`L3425`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L3425) — documented in [tpu-pallas-kernels](../../../../../../concepts/tpu-pallas-kernels.md)
- <a id="_make_splash_attention"></a>`_make_splash_attention(mask: np.ndarray | mask_lib.Mask, *, config: SplashConfig | None = None, is_mqa: bool, save_residuals: bool = False, mask_value: float = base.DEFAULT_MASK_VALUE, downcast_smem_data: bool = True, partial_mask_blocks_dtype: jax.typing.DTypeLike = np.int8, q_seq_shards: int, bias_function=None)` — [`L3348`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L3348) — documented in [tpu-pallas-kernels](../../../../../../concepts/tpu-pallas-kernels.md)
- <a id="_mix_dropout_seed"></a>`_mix_dropout_seed(seed0, seed1, h, q_quant, kv_quant)` — [`L42`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L42) — Mixes (head, q_quantum, kv_quantum) into the two seed words.
- <a id="_not"></a>`_not(x: jax.Array | bool)` — [`L98`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L98)
- <a id="_splash_attention"></a>`_splash_attention(fwd_mask_info: MaskInfo, dkv_mask_info: MaskInfo | None, q: jax.Array, k: jax.Array, v: jax.Array, bias: jax.Array | None = None, dropout_mask: jax.Array | None = None, dropout_seed: jax.Array | None = None, segment_ids: base.SegmentIds | None = None, sinks: jax.Array | None = None, *, is_mqa: bool, config: SplashConfig | None, save_residuals: bool, mask_value: float, max_logit_value: jax.Array | None = None, mask_function: MaskFunctionType | None, bias_function=None, fwd_mask_sparsity: float, dkv_mask_sparsity: float)` — [`L3235`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L3235) — documented in [tpu-pallas-kernels](../../../../../../concepts/tpu-pallas-kernels.md)
- <a id="_splash_attention_bwd"></a>`_splash_attention_bwd(save_residuals: bool, mask_value: float, is_mqa: bool, config: SplashConfig, mask_function: MaskFunctionType | None, bias_function, fwd_mask_sparsity: float, dkv_mask_sparsity: float, res: base.SplashResidualsType, grads: jax.Array | tuple[jax.Array, dict[str, jax.Array]])` — [`L3127`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L3127) — documented in [tpu-pallas-kernels](../../../../../../concepts/tpu-pallas-kernels.md)
- <a id="_splash_attention_bwd_dkv"></a>`_splash_attention_bwd_dkv(q, k, v, bias, dropout_mask, dropout_seed, segment_ids, logsumexp, do, di, *, bq: int, bkv: int, bkv_compute: int, is_mqa: bool, mask_info: MaskInfo, mask_value: float, mask_function: MaskFunctionType | None, bias_function=None, config: SplashConfig, dkv_mask_sparsity: float)` — [`L2572`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L2572) — documented in [tpu-pallas-kernels](../../../../../../concepts/tpu-pallas-kernels.md)
- <a id="_splash_attention_custom"></a>`_splash_attention_custom(fwd_mask_info: MaskInfo, dkv_mask_info: MaskInfo | None, q: jax.Array, k: jax.Array, v: jax.Array, bias: jax.Array | None, dropout_mask: jax.Array | None, dropout_seed: jax.Array | None, segment_ids: base.SegmentIds | None, sinks: jax.Array | None, save_residuals: bool, mask_value: float, is_mqa: bool, config: SplashConfig, mask_function: MaskFunctionType | None, bias_function=None, fwd_mask_sparsity: float = 1, dkv_mask_sparsity: float = 1, max_logit_value: jax.Array | None = None)` — [`L1678`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L1678) — documented in [tpu-pallas-kernels](../../../../../../concepts/tpu-pallas-kernels.md)
- <a id="_splash_attention_forward"></a>`_splash_attention_forward(mask_info: MaskInfo, q: jax.Array, k: jax.Array, v: jax.Array, bias: jax.Array | None, dropout_mask: jax.Array | None, dropout_seed: jax.Array | None, segment_ids: base.SegmentIds | None, sinks: jax.Array | None, mask_value: float, is_mqa: bool, config: SplashConfig, save_residuals: bool, mask_function: MaskFunctionType | None, bias_function=None, fwd_mask_sparsity: float = 1, max_logit_value: jax.Array | None = None, save_max_logits: bool = True)` — [`L1113`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L1113) — documented in [tpu-pallas-kernels](../../../../../../concepts/tpu-pallas-kernels.md)
- <a id="_splash_attention_fwd"></a>`_splash_attention_fwd(fwd_mask_info: MaskInfo, dkv_mask_info: MaskInfo | None, q: jax.Array, k: jax.Array, v: jax.Array, bias: jax.Array | None, dropout_mask: jax.Array | None, dropout_seed: jax.Array | None, segment_ids: base.SegmentIds | None, sinks: jax.Array | None, save_residuals: bool, mask_value: float, is_mqa: bool, config: SplashConfig, mask_function: MaskFunctionType | None, bias_function=None, fwd_mask_sparsity: float = 1, dkv_mask_sparsity: float = 1, max_logit_value: jax.Array | None = None)` — [`L1740`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L1740) — documented in [tpu-pallas-kernels](../../../../../../concepts/tpu-pallas-kernels.md)
- <a id="flash_attention_kernel.body"></a>`body(kv_compute_index, _, has_partial_mask=False)` — [`L728`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L728) — documented in [tpu-pallas-kernels](../../../../../../concepts/tpu-pallas-kernels.md)
- <a id="_flash_attention_dq_kernel.body"></a>`body(has_partial_mask: bool = False)` — [`L1863`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L1863)
- <a id="_flash_attention_dkv_kernel.body"></a>`body(i, _, has_partial_mask=False)` — [`L2072`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L2072)
- <a id="_apply_mask_and_soft_cap.cap_logits"></a>`cap_logits(logits)` — [`L541`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L541)
- <a id="_splash_attention_bwd_dkv.create_dkv_index_map"></a>`create_dkv_index_map(h, i, j, *_)` — [`L2755`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L2755)
- <a id="_splash_attention_forward.create_kv_index_map"></a>`create_kv_index_map(layout)` — [`L1278`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L1278)
- <a id="_splash_attention_bwd_dkv.create_kv_index_map"></a>`create_kv_index_map(layout)` — [`L2659`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L2659)
- <a id="flash_attention_kernel.end"></a>`end()` — [`L1061`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L1061)
- <a id="_flash_attention_dq_kernel.end"></a>`end()` — [`L1929`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L1929)
- <a id="flash_attention_kernel"></a>`flash_attention_kernel(active_rows_ref, active_cols_ref, mask_next_ref, bounds_start_ref, bounds_end_ref, block_mask_ref, q_ref, k_ref, v_ref, bias_ref, dropout_mask_ref, dropout_seed_ref, q_segment_ids_ref, kv_segment_ids_ref, sinks_ref, mask_ref, q_sequence_ref, max_logit_value_ref, o_ref, logsumexp_ref, l_linear_ref, max_logits_ref, m_scratch_ref, l_scratch_ref, o_scratch_ref, *, mask_value: float, kv_steps: int, bq: int, bkv: int, bkv_compute: int, head_dim_v: int, num_stacked_q_heads: int, mask_function: MaskFunctionType | None, bias_function=None, fuse_reciprocal: bool, config: SplashConfig)` — [`L560`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L560) — documented in [tpu-pallas-kernels](../../../../../../concepts/tpu-pallas-kernels.md)
- <a id="from_head_minor"></a>`from_head_minor(vals: tuple[Any, ...], layout: QKVLayout)` — [`L160`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L160)
- <a id="get_kernel_name"></a>`get_kernel_name(is_mqa: bool, save_residuals: bool, is_segmented: bool, phase: str)` — [`L138`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L138) — Returns a unique name for all SplashAttention kernel variants.
- <a id="_splash_attention_forward.unravel.index_map"></a>`index_map(h_block, grid_idx, rows_ref, cols_ref, *_)` — [`L1267`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L1267)
- <a id="_splash_attention_forward.create_kv_index_map.index_map"></a>`index_map(h_block, i, j)` — [`L1279`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L1279)
- <a id="_splash_attention_bwd_dkv.unravel.index_map"></a>`index_map(h, grid_idx, rows_ref, cols_ref, *_)` — [`L2629`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L2629)
- <a id="_splash_attention_bwd_dkv.create_kv_index_map.index_map"></a>`index_map(h, i, j, *_)` — [`L2660`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L2660)
- <a id="flash_attention_kernel.init"></a>`init()` — [`L651`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L651)
- <a id="_flash_attention_dq_kernel.init"></a>`init()` — [`L1860`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L1860)
- <a id="_flash_attention_dkv_kernel.init"></a>`init()` — [`L2048`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L2048)
- <a id="_flash_attention_dkv_kernel.init_dbias"></a>`init_dbias()` — [`L2521`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L2521)
- <a id="_flash_attention_dkv_kernel.init_dbias_pk"></a>`init_dbias_pk()` — [`L2069`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L2069)
- <a id="_flash_attention_dkv_kernel.init_dbias_pk_scratch"></a>`init_dbias_pk_scratch()` — [`L2058`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L2058)
- <a id="_splash_attention_forward.init_if_empty"></a>`init_if_empty(x: jax.Array, value: float)` — [`L1623`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L1623)
- <a id="_splash_attention_forward.mask_index_map"></a>`mask_index_map(h_block, grid_idx, rows_ref, cols_ref, mask_next_ref=None, *_)` — [`L1294`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L1294)
- <a id="_splash_attention_bwd_dkv.mask_index_map"></a>`mask_index_map(h, grid_idx, rows_ref, cols_ref, mask_next_ref=None, *_)` — [`L2639`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L2639)
- <a id="_make_dynamic_splash_attention.process_all_shards"></a>`process_all_shards(mask)` — [`L3510`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L3510)
- <a id="_make_dynamic_splash_attention.process_mask_shard"></a>`process_mask_shard(mask)` — [`L3454`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L3454)
- <a id="_splash_attention_forward.unravel"></a>`unravel(f)` — [`L1266`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L1266)
- <a id="_splash_attention_bwd_dkv.unravel"></a>`unravel(f)` — [`L2628`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L2628)
- <a id="_flash_attention_dkv_kernel.write_dbias_pk"></a>`write_dbias_pk()` — [`L2065`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L2065)

## Module values
- <a id="DROPOUT_QUANTUM"></a>`DROPOUT_QUANTUM` — [`L39`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L39)
- <a id="LOG2E"></a>`LOG2E` — [`L35`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L35) — documented in [tpu-pallas-kernels](../../../../../../concepts/tpu-pallas-kernels.md)
- <a id="LOG2E_INV"></a>`LOG2E_INV` — [`L36`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L36)
- <a id="MaskFunctionType"></a>`MaskFunctionType` — [`L135`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L135)
- <a id="MaskInfo"></a>`MaskInfo` — [`L27`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L27) — documented in [tpu-pallas-kernels](../../../../../../concepts/tpu-pallas-kernels.md)
- <a id="NN_DIM_NUMBERS"></a>`NN_DIM_NUMBERS` — [`L32`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L32)
- <a id="NT_DIM_NUMBERS"></a>`NT_DIM_NUMBERS` — [`L33`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L33)
- <a id="NUM_LANES"></a>`NUM_LANES` — [`L29`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L29) — documented in [tpu-pallas-kernels](../../../../../../concepts/tpu-pallas-kernels.md)
- <a id="NUM_SUBLANES"></a>`NUM_SUBLANES` — [`L30`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L30)
- <a id="P"></a>`P` — [`L26`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L26)
- <a id="_H_C1"></a>`_H_C1` — [`L74`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L74)
- <a id="_H_C2"></a>`_H_C2` — [`L75`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L75)
- <a id="_H_C3"></a>`_H_C3` — [`L76`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L76)
- <a id="_H_C4"></a>`_H_C4` — [`L77`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L77)
- <a id="_H_C5"></a>`_H_C5` — [`L78`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L78)
- <a id="make_dynamic_splash_mha"></a>`make_dynamic_splash_mha` — [`L3528`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L3528)
- <a id="make_dynamic_splash_mqa"></a>`make_dynamic_splash_mqa` — [`L3527`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L3527)
- <a id="make_splash_mha"></a>`make_splash_mha` — [`L3520`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L3520)
- <a id="make_splash_mha_single_device"></a>`make_splash_mha_single_device` — [`L3523`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L3523)
- <a id="make_splash_mqa"></a>`make_splash_mqa` — [`L3521`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L3521)
- <a id="make_splash_mqa_single_device"></a>`make_splash_mqa_single_device` — [`L3525`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L3525)
- <a id="partial"></a>`partial` — [`L28`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L28)
- <a id="to_i32"></a>`to_i32` — [`L460`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py#L460)

