---
title: 'Module: src/vllm_torchtpu/kernels/gdn/v3/config.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/gdn/v3/config.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.gdn.v3.config`/
symbols:
  GDNConfig.seq_tile_size: GDNConfig#seq_tile_size().
  GDNConfig.dtypes: GDNConfig#dtypes.
  GDNConfig.chunk_size: GDNConfig#chunk_size().
  Dtypes.compute: Dtypes#compute.
  GDNConfig.num_v_heads: GDNConfig#num_v_heads.
  GDNConfig: GDNConfig#
  GDNConfig.get_scratch_shape_dict: GDNConfig#get_scratch_shape_dict().
  GDNConfig.kq_head_dim: GDNConfig#kq_head_dim.
  GDNConfig.get_kernel_name: GDNConfig#get_kernel_name().
  GDNConfig.v_per_kq_head: GDNConfig#v_per_kq_head().
  GDNConfig.is_kda: GDNConfig#is_kda().
  GDNConfig.window_size: GDNConfig#window_size.
  GDNConfig.conv_hbm_offset: GDNConfig#conv_hbm_offset().
  GDNConfig.get_out_shape: GDNConfig#get_out_shape().
  GDNConfig.v_head_dim: GDNConfig#v_head_dim.
  GDNMode: GDNMode#
  GDNConfig.num_kq_heads: GDNConfig#num_kq_heads.
  GDNConfig.gate_dim: GDNConfig#gate_dim().
  GDNConfig.attention_mode: GDNConfig#attention_mode.
  GDNConfig.get_vmem_limit_bytes: GDNConfig#get_vmem_limit_bytes().
  GDNConfig.mode: GDNConfig#mode.
  GDNConfig.prev_kernel_size: GDNConfig#prev_kernel_size().
  AttentionMode: AttentionMode#
  GDNConfig.triangular_block_size: GDNConfig#triangular_block_size().
  GDNConfig.use_recurrent: GDNConfig#use_recurrent().
  GDNMode.PER_SEQ: GDNMode#PER_SEQ.
  GDNConfig.v_dim_size: GDNConfig#v_dim_size().
  Dtypes.recurrent_state: Dtypes#recurrent_state.
  GDNConfig.dim_size: GDNConfig#dim_size.
  GDNConfig.tile_size: GDNConfig#tile_size.
  GDNConfig.kq_dim_size: GDNConfig#kq_dim_size().
  GDNConfig.aligned_num_v_heads: GDNConfig#aligned_num_v_heads().
  GDNConfig.kernel_size: GDNConfig#kernel_size.
  GDNConfig.gate_lower_bound: GDNConfig#gate_lower_bound.
  GDNConfig.aligned_gate_dim: GDNConfig#aligned_gate_dim().
  AttentionMode.KDA: AttentionMode#KDA.
  Dtypes.conv_state: Dtypes#conv_state.
  GDNConfig.batch_size: GDNConfig#batch_size.
  GDNConfig.is_shared: GDNConfig#is_shared.
  AttentionMode.GDN: AttentionMode#GDN.
  Dtypes: Dtypes#
  Dtypes.act_out: Dtypes#act_out.
  GDNConfig.recurrent_hbm_offset: GDNConfig#recurrent_hbm_offset().
  GDNMode.BATCHED: GDNMode#BATCHED.
  Dtypes.act_in: Dtypes#act_in.
  GDNConfig.num_buffers: GDNConfig#num_buffers.
  GDNConfig.get_metadata: GDNConfig#get_metadata().
  GDNConfig.DEFAULT_VMEM_FRACTION: GDNConfig#DEFAULT_VMEM_FRACTION.
  GDNConfig.WINDOWED_VMEM_FRACTION: GDNConfig#WINDOWED_VMEM_FRACTION.
---
# Module: [`src/vllm_torchtpu/kernels/gdn/v3/config.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/config.py)

## Classes
### <a id="AttentionMode"></a>`AttentionMode`  ·  implements/extends StrEnum
- def: [`src/vllm_torchtpu/kernels/gdn/v3/config.py:25`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/config.py#L25)
- signature: `class AttentionMode(enum.StrEnum):`
- members:
  - <a id="AttentionMode.GDN"></a>`GDN` — [`L27`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/config.py#L27)
  - <a id="AttentionMode.KDA"></a>`KDA` — [`L30`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/config.py#L30)
- used by: [`fused_conv1d_gdn`](wrapper.md#fused_conv1d_gdn), [`is_kda`](config.md#GDNConfig.is_kda), [`run_kernel`](../../../layers/adapter/custom_ops/kda_attention_op.md#_build_fused_core.fused_core.run_kernel), [`attention_mode`](config.md#GDNConfig.attention_mode)

### <a id="Dtypes"></a>`Dtypes`
- def: [`src/vllm_torchtpu/kernels/gdn/v3/config.py:43`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/config.py#L43)
- signature: `class Dtypes:`
- members:
  - <a id="Dtypes.act_in"></a>`act_in` — [`L44`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/config.py#L44)
  - <a id="Dtypes.act_out"></a>`act_out` — [`L45`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/config.py#L45)
  - <a id="Dtypes.compute"></a>`compute` — [`L46`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/config.py#L46) — documented in [gated-deltanet-kernels](../../../../../../concepts/gated-deltanet-kernels.md)
  - <a id="Dtypes.conv_state"></a>`conv_state` — [`L48`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/config.py#L48)
  - <a id="Dtypes.recurrent_state"></a>`recurrent_state` — [`L47`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/config.py#L47)
- used by: [`call_kernel`](wrapper.md#fused_conv1d_gdn.call_kernel), [`inner_kernel`](wrapper.md#inner_kernel), [`create_allocs`](memory_ref.md#create_allocs), [`dtypes`](config.md#GDNConfig.dtypes), [`recurrent_gdn`](compute_gdn.md#recurrent_gdn), [`recurrent_kda`](compute_kda.md#recurrent_kda), [`chunked_gdn_per_seq`](compute_gdn.md#chunked_gdn_per_seq), [`chunked_kda`](compute_kda.md#chunked_kda), [`chunked_gdn`](compute_gdn.md#chunked_gdn), [`chunked_kda_per_seq`](compute_kda.md#chunked_kda_per_seq), [`load_and_select_states`](vmem_ldst.md#load_and_select_states), [`recurrent_kda_per_seq`](compute_kda.md#recurrent_kda_per_seq), [`recurrent_gdn_per_seq`](compute_gdn.md#recurrent_gdn_per_seq), [`conv_hbm_offset`](config.md#GDNConfig.conv_hbm_offset), [`get_out_shape`](config.md#GDNConfig.get_out_shape)

### <a id="GDNConfig"></a>`GDNConfig`
- def: [`src/vllm_torchtpu/kernels/gdn/v3/config.py:53`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/config.py#L53) — documented in [gated-deltanet-kernels](../../../../../../concepts/gated-deltanet-kernels.md)
- signature: `class GDNConfig:`
- members:
  - <a id="GDNConfig.aligned_gate_dim"></a>`aligned_gate_dim(self)` — [`L129`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/config.py#L129)
  - <a id="GDNConfig.aligned_num_v_heads"></a>`aligned_num_v_heads(self)` — [`L180`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/config.py#L180)
  - <a id="GDNConfig.chunk_size"></a>`chunk_size(self)` — [`L100`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/config.py#L100) — documented in [gated-deltanet-kernels](../../../../../../concepts/gated-deltanet-kernels.md)
  - <a id="GDNConfig.conv_hbm_offset"></a>`conv_hbm_offset(self)` — [`L83`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/config.py#L83)
  - <a id="GDNConfig.gate_dim"></a>`gate_dim(self)` — [`L122`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/config.py#L122) — Width of the gate activation `a`, in elements per token.
  - <a id="GDNConfig.get_kernel_name"></a>`get_kernel_name(self)` — [`L185`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/config.py#L185) — documented in [gated-deltanet-kernels](../../../../../../concepts/gated-deltanet-kernels.md)
  - <a id="GDNConfig.get_metadata"></a>`get_metadata(self)` — [`L196`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/config.py#L196)
  - <a id="GDNConfig.get_out_shape"></a>`get_out_shape(self)` — [`L206`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/config.py#L206) — documented in [gated-deltanet-kernels](../../../../../../concepts/gated-deltanet-kernels.md)
  - <a id="GDNConfig.get_scratch_shape_dict"></a>`get_scratch_shape_dict(self)` — [`L227`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/config.py#L227) — documented in [gated-deltanet-kernels](../../../../../../concepts/gated-deltanet-kernels.md)
  - <a id="GDNConfig.get_vmem_limit_bytes"></a>`get_vmem_limit_bytes(cls, window_size: int = 1)` — [`L220`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/config.py#L220) — Returns the VMEM limit for a kernel keeping window_size checkpoints. — documented in [gated-deltanet-kernels](../../../../../../concepts/gated-deltanet-kernels.md)
  - <a id="GDNConfig.is_kda"></a>`is_kda(self)` — [`L118`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/config.py#L118) — documented in [gated-deltanet-kernels](../../../../../../concepts/gated-deltanet-kernels.md)
  - <a id="GDNConfig.kq_dim_size"></a>`kq_dim_size(self)` — [`L172`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/config.py#L172)
  - <a id="GDNConfig.prev_kernel_size"></a>`prev_kernel_size(self)` — [`L114`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/config.py#L114)
  - <a id="GDNConfig.recurrent_hbm_offset"></a>`recurrent_hbm_offset(self)` — [`L96`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/config.py#L96)
  - <a id="GDNConfig.seq_tile_size"></a>`seq_tile_size(self)` — [`L108`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/config.py#L108) — documented in [gated-deltanet-kernels](../../../../../../concepts/gated-deltanet-kernels.md)
  - <a id="GDNConfig.triangular_block_size"></a>`triangular_block_size(self)` — [`L134`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/config.py#L134) — Sub-block size of the chunked KDA intra-chunk solve.
  - <a id="GDNConfig.use_recurrent"></a>`use_recurrent(self)` — [`L159`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/config.py#L159) — Whether GDN runs the token-recurrent scan instead of the chunked one.
  - <a id="GDNConfig.v_dim_size"></a>`v_dim_size(self)` — [`L168`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/config.py#L168)
  - <a id="GDNConfig.v_per_kq_head"></a>`v_per_kq_head(self)` — [`L176`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/config.py#L176)
  - <a id="GDNConfig.DEFAULT_VMEM_FRACTION"></a>`DEFAULT_VMEM_FRACTION` — [`L216`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/config.py#L216)
  - <a id="GDNConfig.WINDOWED_VMEM_FRACTION"></a>`WINDOWED_VMEM_FRACTION` — [`L217`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/config.py#L217)
  - <a id="GDNConfig.attention_mode"></a>`attention_mode` — [`L64`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/config.py#L64)
  - <a id="GDNConfig.batch_size"></a>`batch_size` — [`L56`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/config.py#L56)
  - <a id="GDNConfig.dim_size"></a>`dim_size` — [`L57`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/config.py#L57)
  - <a id="GDNConfig.dtypes"></a>`dtypes` — [`L55`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/config.py#L55) — documented in [gated-deltanet-kernels](../../../../../../concepts/gated-deltanet-kernels.md)
  - <a id="GDNConfig.gate_lower_bound"></a>`gate_lower_bound` — [`L67`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/config.py#L67)
  - <a id="GDNConfig.is_shared"></a>`is_shared` — [`L80`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/config.py#L80)
  - <a id="GDNConfig.kernel_size"></a>`kernel_size` — [`L58`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/config.py#L58)
  - <a id="GDNConfig.kq_head_dim"></a>`kq_head_dim` — [`L62`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/config.py#L62) — documented in [gated-deltanet-kernels](../../../../../../concepts/gated-deltanet-kernels.md)
  - <a id="GDNConfig.mode"></a>`mode` — [`L54`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/config.py#L54)
  - <a id="GDNConfig.num_buffers"></a>`num_buffers` — [`L68`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/config.py#L68)
  - <a id="GDNConfig.num_kq_heads"></a>`num_kq_heads` — [`L60`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/config.py#L60)
  - <a id="GDNConfig.num_v_heads"></a>`num_v_heads` — [`L61`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/config.py#L61) — documented in [gated-deltanet-kernels](../../../../../../concepts/gated-deltanet-kernels.md)
  - <a id="GDNConfig.tile_size"></a>`tile_size` — [`L59`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/config.py#L59)
  - <a id="GDNConfig.v_head_dim"></a>`v_head_dim` — [`L63`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/config.py#L63) — documented in [gated-deltanet-kernels](../../../../../../concepts/gated-deltanet-kernels.md)
  - <a id="GDNConfig.window_size"></a>`window_size` — [`L78`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/config.py#L78) — documented in [gated-deltanet-kernels](../../../../../../concepts/gated-deltanet-kernels.md)
- uses (calls/refs, reference-scoped): [`GDNMode`](config.md#GDNMode), [`AttentionMode`](config.md#AttentionMode), [`PER_SEQ`](config.md#GDNMode.PER_SEQ), [`recurrent_state`](config.md#Dtypes.recurrent_state), [`KDA`](config.md#AttentionMode.KDA), [`Dtypes`](config.md#Dtypes), [`GDN`](config.md#AttentionMode.GDN), [`act_out`](config.md#Dtypes.act_out)
- used by: [`call_kernel`](wrapper.md#fused_conv1d_gdn.call_kernel), [`inner_kernel`](wrapper.md#inner_kernel), [`fused_conv1d_gdn`](wrapper.md#fused_conv1d_gdn), [`create_allocs`](memory_ref.md#create_allocs), [`recurrent_gdn`](compute_gdn.md#recurrent_gdn), [`recurrent_kda`](compute_kda.md#recurrent_kda), [`chunked_gdn_per_seq`](compute_gdn.md#chunked_gdn_per_seq), [`chunked_kda`](compute_kda.md#chunked_kda), [`chunked_gdn`](compute_gdn.md#chunked_gdn), [`copy_in`](memory_ref.md#StateInBufferedRef.copy_in), [`copy_out`](memory_ref.md#StateOutBufferedRef.copy_out), [`chunked_kda_per_seq`](compute_kda.md#chunked_kda_per_seq), [`load_activation_as_large`](vmem_ldst.md#load_activation_as_large), [`load_and_select_states`](vmem_ldst.md#load_and_select_states), [`outer_kernel`](wrapper.md#outer_kernel), [`causal_conv1d`](compute_conv1d.md#causal_conv1d), [`load_activation_as_compact`](vmem_ldst.md#load_activation_as_compact), [`recurrent_kda_per_seq`](compute_kda.md#recurrent_kda_per_seq), [`compute_per_seq_metadata`](metadata.md#compute_per_seq_metadata), [`recurrent_gdn_per_seq`](compute_gdn.md#recurrent_gdn_per_seq), [`wait_in`](memory_ref.md#StateInBufferedRef.wait_in), [`wait_out`](memory_ref.md#StateOutBufferedRef.wait_out), [`cfg`](memory_ref.md#BaseBufferedRef.cfg), [`copy_in`](memory_ref.md#InBufferedRef.copy_in), [`copy_out`](memory_ref.md#OutBufferedRef.copy_out), [`compute_batched_seq_metadata`](metadata.md#compute_batched_seq_metadata), [`wait_in`](memory_ref.md#InBufferedRef.wait_in), [`wait_out`](memory_ref.md#OutBufferedRef.wait_out), [`create`](memory_ref.md#MetadataRef.create), [`activate_gate`](compute_kda.md#activate_gate), [`create`](memory_ref.md#BaseBufferedRef.create)

### <a id="GDNMode"></a>`GDNMode`  ·  implements/extends StrEnum
- def: [`src/vllm_torchtpu/kernels/gdn/v3/config.py:33`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/config.py#L33) — documented in [gated-deltanet-kernels](../../../../../../concepts/gated-deltanet-kernels.md)
- signature: `class GDNMode(enum.StrEnum):`
- members:
  - <a id="GDNMode.BATCHED"></a>`BATCHED` — [`L37`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/config.py#L37)
  - <a id="GDNMode.PER_SEQ"></a>`PER_SEQ` — [`L38`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/config.py#L38)
- used by: [`call_kernel`](wrapper.md#fused_conv1d_gdn.call_kernel), [`fused_conv1d_gdn`](wrapper.md#fused_conv1d_gdn), [`seq_tile_size`](config.md#GDNConfig.seq_tile_size), [`chunk_size`](config.md#GDNConfig.chunk_size), [`get_scratch_shape_dict`](config.md#GDNConfig.get_scratch_shape_dict), [`mode`](config.md#GDNConfig.mode)

