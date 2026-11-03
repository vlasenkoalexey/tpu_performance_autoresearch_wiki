---
title: 'Module: src/vllm_torchtpu/megakernel/pool/scatter_ctx.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/megakernel/pool/scatter_ctx.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.megakernel.pool.scatter_ctx`/
symbols:
  ScatterKernel.build: ScatterKernel#build().
  batch_to_i32_cols: batch_to_i32_cols().
  is_active: is_active().
  ScatterKernel: ScatterKernel#
  ScatterKernel.sg: ScatterKernel#sg.
  ScatterGeom.T: ScatterGeom#T.
  ScatterGeom.NS: ScatterGeom#NS.
  ScatterGeom.interpret: ScatterGeom#interpret.
  ScatterGeom.NATT: ScatterGeom#NATT.
  ScatterGeom.page_size: ScatterGeom#page_size.
  ScatterGeom.ex: ScatterGeom#ex.
  ScatterGeom.pps: ScatterGeom#pps.
  ScatterGeom.layout: ScatterGeom#layout.
  ScatterGeom: ScatterGeom#
  ScatterGeom.G_PER_ATT: ScatterGeom#G_PER_ATT.
  ScatterGeom.h4: ScatterGeom#h4.
  ScatterGeom.rec_pages: ScatterGeom#rec_pages.
  ScatterGeom.use_conv_partial: ScatterGeom#use_conv_partial.
  ScatterGeom.conv_rows_pad: ScatterGeom#conv_rows_pad.
  ScatterGeom.direct_conv: ScatterGeom#direct_conv.
  ScatterKernel.knew_buf: ScatterKernel#knew_buf.
  ScatterKernel.vnew_buf: ScatterKernel#vnew_buf.
  ScatterKernel.page_buf: ScatterKernel#page_buf.
  ScatterGeom.rec_u32_cap: ScatterGeom#rec_u32_cap.
  ScatterGeom.conv_page: ScatterGeom#conv_page.
  ScatterGeom.conv_page_rows: ScatterGeom#conv_page_rows.
  ScatterGeom.page_rows: ScatterGeom#page_rows.
  ScatterGeom.act_mode: ScatterGeom#act_mode.
  ScatterGeom.pt_cols: ScatterGeom#pt_cols.
  ScatterGeom.vh: ScatterGeom#vh.
  ScatterGeom.ckpt_is_3d: ScatterGeom#ckpt_is_3d.
  ScatterKernel.ckpt_ref: ScatterKernel#ckpt_ref.
  ScatterKernel.raw_out_refs: ScatterKernel#raw_out_refs.
  ScatterKernel.rec_buf: ScatterKernel#rec_buf.
  ScatterKernel.conv_buf: ScatterKernel#conv_buf.
  ScatterKernel.sem_p: ScatterKernel#sem_p.
  ScatterKernel.k_cols_buf: ScatterKernel#k_cols_buf.
  ScatterKernel.v_cols_buf: ScatterKernel#v_cols_buf.
  ScatterGeom.B: ScatterGeom#B.
  ScatterGeom.MR: ScatterGeom#MR.
  ScatterGeom.page_shape: ScatterGeom#page_shape.
  ScatterGeom.has_gdn: ScatterGeom#has_gdn.
  ScatterGeom.n_smem: ScatterGeom#n_smem.
  ScatterGeom.n_hbm: ScatterGeom#n_hbm.
  ScatterGeom.s_names: ScatterGeom#s_names.
  ScatterGeom.n_pairs: ScatterGeom#n_pairs.
  ScatterGeom.taps: ScatterGeom#taps.
  ScatterGeom.ssm_u32_rows: ScatterGeom#ssm_u32_rows.
  ScatterGeom.ckpt_t_off: ScatterGeom#ckpt_t_off.
  ScatterKernel.pos_ref: ScatterKernel#pos_ref.
  ScatterKernel.kv_pages_ref: ScatterKernel#kv_pages_ref.
  ScatterKernel.conv_ref: ScatterKernel#conv_ref.
  ScatterKernel.rec_ref: ScatterKernel#rec_ref.
  ScatterKernel.kv_page: ScatterKernel#kv_page.
  ScatterKernel.sem_kv_rd: ScatterKernel#sem_kv_rd.
  ScatterKernel.sem_kv_wr: ScatterKernel#sem_kv_wr.
  ScatterKernel.sem_kv_in: ScatterKernel#sem_kv_in.
  ScatterKernel.sem_in: ScatterKernel#sem_in.
  ScatterKernel.lane_iota: ScatterKernel#lane_iota.
  ScatterKernel.total_gdn: ScatterKernel#total_gdn.
  ScatterGeom.HD: ScatterGeom#HD.
  ScatterGeom.KD: ScatterGeom#KD.
  ScatterGeom.VD: ScatterGeom#VD.
  ScatterGeom.QKV: ScatterGeom#QKV.
  ScatterGeom.conv_rows: ScatterGeom#conv_rows.
  ScatterGeom.conv_tail_row: ScatterGeom#conv_tail_row.
  ScatterGeom.ckpt_ndim: ScatterGeom#ckpt_ndim.
  ScatterKernel.act_ref: ScatterKernel#act_ref.
  ScatterKernel.knew_ref: ScatterKernel#knew_ref.
  ScatterKernel.vnew_ref: ScatterKernel#vnew_ref.
  ScatterKernel.w4_row_iota: ScatterKernel#w4_row_iota.
  ScatterKernel.SLOT_ROWS: ScatterKernel#SLOT_ROWS.
  ScatterGeom.qkv_128: ScatterGeom#qkv_128.
  ScatterKernel.CP_ROWS: ScatterKernel#CP_ROWS.
---
# Module: [`src/vllm_torchtpu/megakernel/pool/scatter_ctx.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter_ctx.py)

## Classes
### <a id="ScatterGeom"></a>`ScatterGeom`
- def: [`src/vllm_torchtpu/megakernel/pool/scatter_ctx.py:30`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter_ctx.py#L30)
- doc: Static (trace-time) geometry of one `scatter_pool_states` call.
- signature: `class ScatterGeom:`
- members:
  - <a id="ScatterGeom.B"></a>`B` — [`L43`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter_ctx.py#L43)
  - <a id="ScatterGeom.G_PER_ATT"></a>`G_PER_ATT` — [`L46`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter_ctx.py#L46)
  - <a id="ScatterGeom.HD"></a>`HD` — [`L48`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter_ctx.py#L48)
  - <a id="ScatterGeom.KD"></a>`KD` — [`L66`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter_ctx.py#L66)
  - <a id="ScatterGeom.MR"></a>`MR` — [`L45`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter_ctx.py#L45)
  - <a id="ScatterGeom.NATT"></a>`NATT` — [`L41`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter_ctx.py#L41)
  - <a id="ScatterGeom.NS"></a>`NS` — [`L42`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter_ctx.py#L42)
  - <a id="ScatterGeom.QKV"></a>`QKV` — [`L68`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter_ctx.py#L68)
  - <a id="ScatterGeom.T"></a>`T` — [`L44`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter_ctx.py#L44)
  - <a id="ScatterGeom.VD"></a>`VD` — [`L67`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter_ctx.py#L67)
  - <a id="ScatterGeom.act_mode"></a>`act_mode` — [`L59`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter_ctx.py#L59)
  - <a id="ScatterGeom.ckpt_is_3d"></a>`ckpt_is_3d` — [`L78`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter_ctx.py#L78)
  - <a id="ScatterGeom.ckpt_ndim"></a>`ckpt_ndim` — [`L80`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter_ctx.py#L80)
  - <a id="ScatterGeom.ckpt_t_off"></a>`ckpt_t_off` — [`L79`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter_ctx.py#L79)
  - <a id="ScatterGeom.conv_page"></a>`conv_page` — [`L54`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter_ctx.py#L54)
  - <a id="ScatterGeom.conv_page_rows"></a>`conv_page_rows` — [`L55`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter_ctx.py#L55)
  - <a id="ScatterGeom.conv_rows"></a>`conv_rows` — [`L71`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter_ctx.py#L71)
  - <a id="ScatterGeom.conv_rows_pad"></a>`conv_rows_pad` — [`L72`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter_ctx.py#L72)
  - <a id="ScatterGeom.conv_tail_row"></a>`conv_tail_row` — [`L77`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter_ctx.py#L77)
  - <a id="ScatterGeom.direct_conv"></a>`direct_conv` — [`L74`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter_ctx.py#L74)
  - <a id="ScatterGeom.ex"></a>`ex` — [`L39`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter_ctx.py#L39)
  - <a id="ScatterGeom.h4"></a>`h4` — [`L49`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter_ctx.py#L49)
  - <a id="ScatterGeom.has_gdn"></a>`has_gdn` — [`L57`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter_ctx.py#L57)
  - <a id="ScatterGeom.interpret"></a>`interpret` — [`L40`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter_ctx.py#L40)
  - <a id="ScatterGeom.layout"></a>`layout` — [`L38`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter_ctx.py#L38)
  - <a id="ScatterGeom.n_hbm"></a>`n_hbm` — [`L61`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter_ctx.py#L61)
  - <a id="ScatterGeom.n_pairs"></a>`n_pairs` — [`L63`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter_ctx.py#L63)
  - <a id="ScatterGeom.n_smem"></a>`n_smem` — [`L60`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter_ctx.py#L60)
  - <a id="ScatterGeom.page_rows"></a>`page_rows` — [`L56`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter_ctx.py#L56)
  - <a id="ScatterGeom.page_shape"></a>`page_shape` — [`L50`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter_ctx.py#L50)
  - <a id="ScatterGeom.page_size"></a>`page_size` — [`L47`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter_ctx.py#L47)
  - <a id="ScatterGeom.pps"></a>`pps` — [`L51`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter_ctx.py#L51)
  - <a id="ScatterGeom.pt_cols"></a>`pt_cols` — [`L64`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter_ctx.py#L64)
  - <a id="ScatterGeom.qkv_128"></a>`qkv_128` — [`L73`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter_ctx.py#L73)
  - <a id="ScatterGeom.rec_pages"></a>`rec_pages` — [`L52`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter_ctx.py#L52)
  - <a id="ScatterGeom.rec_u32_cap"></a>`rec_u32_cap` — [`L53`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter_ctx.py#L53)
  - <a id="ScatterGeom.s_names"></a>`s_names` — [`L62`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter_ctx.py#L62)
  - <a id="ScatterGeom.ssm_u32_rows"></a>`ssm_u32_rows` — [`L70`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter_ctx.py#L70)
  - <a id="ScatterGeom.taps"></a>`taps` — [`L69`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter_ctx.py#L69)
  - <a id="ScatterGeom.use_conv_partial"></a>`use_conv_partial` — [`L58`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter_ctx.py#L58)
  - <a id="ScatterGeom.vh"></a>`vh` — [`L65`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter_ctx.py#L65)
- uses (calls/refs, reference-scoped): [`PoolLayout`](layout.md#PoolLayout)
- used by: [`scatter_pool_states`](scatter.md#scatter_pool_states), [`start_scatter_seq`](scatter_ckpt.md#start_scatter_seq), [`scatter_single_token_across_att`](scatter_kv.md#scatter_single_token_across_att), [`scatter_kv`](scatter_kv.md#scatter_kv), [`ckpt_prologue`](scatter_sched.md#ckpt_prologue), [`build`](scatter_ctx.md#ScatterKernel.build), [`wait_scatter_seq`](scatter_ckpt.md#wait_scatter_seq), [`start_seq_in`](scatter_sched.md#start_seq_in), [`pb_for`](scatter_ckpt.md#pb_for), [`wait_seq_in`](scatter_sched.md#wait_seq_in), [`scatter_ckpt_states`](scatter_sched.md#scatter_ckpt_states), [`slot_copy`](scatter_ckpt.md#slot_copy), [`batch_to_i32_cols`](scatter_ctx.md#batch_to_i32_cols), [`kv_cols`](scatter_kv.md#kv_cols), [`scatter_kv_seq`](scatter_kv.md#scatter_kv.scatter_kv_seq), [`is_active`](scatter_ctx.md#is_active), [`is_contig_ckpt`](scatter_ckpt.md#is_contig_ckpt), [`sg`](scatter_ctx.md#ScatterKernel.sg)

### <a id="ScatterKernel"></a>`ScatterKernel`
- def: [`src/vllm_torchtpu/megakernel/pool/scatter_ctx.py:84`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter_ctx.py#L84) — documented in [megakernel-pool](../../../../../concepts/megakernel-pool.md)
- doc: The scatter kernel's refs (inputs, outputs, scratch) and lane iotas.
- signature: `class ScatterKernel:`
- members:
  - <a id="ScatterKernel.build"></a>`build(cls, sg: ScatterGeom, refs: Any)` — [`L119`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter_ctx.py#L119) — Split the kernel's `refs`; trace the lane iotas (in kernel order). — documented in [megakernel-pool](../../../../../concepts/megakernel-pool.md)
  - <a id="ScatterKernel.CP_ROWS"></a>`CP_ROWS` — [`L115`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter_ctx.py#L115)
  - <a id="ScatterKernel.SLOT_ROWS"></a>`SLOT_ROWS` — [`L116`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter_ctx.py#L116)
  - <a id="ScatterKernel.act_ref"></a>`act_ref` — [`L91`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter_ctx.py#L91)
  - <a id="ScatterKernel.ckpt_ref"></a>`ckpt_ref` — [`L90`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter_ctx.py#L90)
  - <a id="ScatterKernel.conv_buf"></a>`conv_buf` — [`L102`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter_ctx.py#L102)
  - <a id="ScatterKernel.conv_ref"></a>`conv_ref` — [`L94`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter_ctx.py#L94)
  - <a id="ScatterKernel.k_cols_buf"></a>`k_cols_buf` — [`L108`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter_ctx.py#L108)
  - <a id="ScatterKernel.knew_buf"></a>`knew_buf` — [`L98`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter_ctx.py#L98)
  - <a id="ScatterKernel.knew_ref"></a>`knew_ref` — [`L92`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter_ctx.py#L92)
  - <a id="ScatterKernel.kv_page"></a>`kv_page` — [`L97`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter_ctx.py#L97)
  - <a id="ScatterKernel.kv_pages_ref"></a>`kv_pages_ref` — [`L89`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter_ctx.py#L89)
  - <a id="ScatterKernel.lane_iota"></a>`lane_iota` — [`L110`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter_ctx.py#L110)
  - <a id="ScatterKernel.page_buf"></a>`page_buf` — [`L100`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter_ctx.py#L100)
  - <a id="ScatterKernel.pos_ref"></a>`pos_ref` — [`L88`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter_ctx.py#L88)
  - <a id="ScatterKernel.raw_out_refs"></a>`raw_out_refs` — [`L96`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter_ctx.py#L96)
  - <a id="ScatterKernel.rec_buf"></a>`rec_buf` — [`L101`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter_ctx.py#L101)
  - <a id="ScatterKernel.rec_ref"></a>`rec_ref` — [`L95`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter_ctx.py#L95)
  - <a id="ScatterKernel.sem_in"></a>`sem_in` — [`L106`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter_ctx.py#L106)
  - <a id="ScatterKernel.sem_kv_in"></a>`sem_kv_in` — [`L105`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter_ctx.py#L105)
  - <a id="ScatterKernel.sem_kv_rd"></a>`sem_kv_rd` — [`L103`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter_ctx.py#L103)
  - <a id="ScatterKernel.sem_kv_wr"></a>`sem_kv_wr` — [`L104`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter_ctx.py#L104)
  - <a id="ScatterKernel.sem_p"></a>`sem_p` — [`L107`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter_ctx.py#L107)
  - <a id="ScatterKernel.sg"></a>`sg` — [`L87`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter_ctx.py#L87)
  - <a id="ScatterKernel.total_gdn"></a>`total_gdn` — [`L112`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter_ctx.py#L112)
  - <a id="ScatterKernel.v_cols_buf"></a>`v_cols_buf` — [`L109`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter_ctx.py#L109)
  - <a id="ScatterKernel.vnew_buf"></a>`vnew_buf` — [`L99`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter_ctx.py#L99)
  - <a id="ScatterKernel.vnew_ref"></a>`vnew_ref` — [`L93`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter_ctx.py#L93)
  - <a id="ScatterKernel.w4_row_iota"></a>`w4_row_iota` — [`L111`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter_ctx.py#L111)
- uses (calls/refs, reference-scoped): [`I32`](../ops.md#I32), [`NS`](scatter_ctx.md#ScatterGeom.NS), [`NATT`](scatter_ctx.md#ScatterGeom.NATT), [`page_size`](scatter_ctx.md#ScatterGeom.page_size), [`ScatterGeom`](scatter_ctx.md#ScatterGeom), [`G_PER_ATT`](scatter_ctx.md#ScatterGeom.G_PER_ATT), [`conv_rows_pad`](scatter_ctx.md#ScatterGeom.conv_rows_pad), [`direct_conv`](scatter_ctx.md#ScatterGeom.direct_conv), [`h4`](scatter_ctx.md#ScatterGeom.h4), [`rec_pages`](scatter_ctx.md#ScatterGeom.rec_pages), [`act_mode`](scatter_ctx.md#ScatterGeom.act_mode), [`page_rows`](scatter_ctx.md#ScatterGeom.page_rows), [`has_gdn`](scatter_ctx.md#ScatterGeom.has_gdn), [`n_hbm`](scatter_ctx.md#ScatterGeom.n_hbm), [`n_smem`](scatter_ctx.md#ScatterGeom.n_smem), [`s_names`](scatter_ctx.md#ScatterGeom.s_names), [`taps`](scatter_ctx.md#ScatterGeom.taps), [`QKV`](scatter_ctx.md#ScatterGeom.QKV)
- used by: [`start_scatter_seq`](scatter_ckpt.md#start_scatter_seq), [`scatter_single_token_across_att`](scatter_kv.md#scatter_single_token_across_att), [`scatter_kv`](scatter_kv.md#scatter_kv), [`ckpt_prologue`](scatter_sched.md#ckpt_prologue), [`wait_scatter_seq`](scatter_ckpt.md#wait_scatter_seq), [`start_seq_in`](scatter_sched.md#start_seq_in), [`pb_for`](scatter_ckpt.md#pb_for), [`wait_seq_in`](scatter_sched.md#wait_seq_in), [`scatter_ckpt_states`](scatter_sched.md#scatter_ckpt_states), [`slot_copy`](scatter_ckpt.md#slot_copy), [`_kernel`](scatter.md#scatter_pool_states._kernel), [`batch_to_i32_cols`](scatter_ctx.md#batch_to_i32_cols), [`kv_cols`](scatter_kv.md#kv_cols), [`is_active`](scatter_ctx.md#is_active), [`is_contig_ckpt`](scatter_ckpt.md#is_contig_ckpt)

## Functions
- <a id="batch_to_i32_cols"></a>`batch_to_i32_cols(kc: ScatterKernel, tok_mr_hd: Any)` — [`L197`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter_ctx.py#L197) — `[MR, HD]` new K or V rows as `[HD // 4, page_size]` i32 fp8 columns.
- <a id="is_active"></a>`is_active(kc: ScatterKernel, s: Any)` — [`L186`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter_ctx.py#L186) — Whether sequence `s` is active (all / from checkpoints / mask ref).

