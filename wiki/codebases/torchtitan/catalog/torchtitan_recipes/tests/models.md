---
title: 'Module: torchtitan_recipes/tests/models.py'
type: catalog
provenance: extracted
module: torchtitan_recipes/tests/models.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan_recipes.tests.models`/
symbols:
  gpt_oss_debugmodel_flex_fsdp2_cp2_pp2_ep4_sac: gpt_oss_debugmodel_flex_fsdp2_cp2_pp2_ep4_sac().
  deepseek_v3_debugmodel_fsdp2_cp2_pp2_ep4: deepseek_v3_debugmodel_fsdp2_cp2_pp2_ep4().
  qwen3_debugmodel_moe_param_groups_fsdp2_tp2_cp2_ep8: qwen3_debugmodel_moe_param_groups_fsdp2_tp2_cp2_ep8().
  muse_glimmer_debugmodel_mm_tp2_cp2_pp2: muse_glimmer_debugmodel_mm_tp2_cp2_pp2().
  deepseek_v3_debugmodel_fsdp2_tp2_cp2_ep8: deepseek_v3_debugmodel_fsdp2_tp2_cp2_ep8().
  llama3_debugmodel_fsdp2_tp2_cp2: llama3_debugmodel_fsdp2_tp2_cp2().
  gpt_oss_debugmodel_fsdp4_tp2_ep4: gpt_oss_debugmodel_fsdp4_tp2_ep4().
  gpt_oss_debugmodel_fsdp4_pp2_ep4_sac: gpt_oss_debugmodel_fsdp4_pp2_ep4_sac().
  muse_glimmer_debugmodel_fsdp2_tp2_cp2: muse_glimmer_debugmodel_fsdp2_tp2_cp2().
  qwen3_debugmodel_fsdp2_tp2_cp2_compile_helion_rope: qwen3_debugmodel_fsdp2_tp2_cp2_compile_helion_rope().
  _configure_fsdp_numerics: _configure_fsdp_numerics().
  llama3_debugmodel_fsdp2_tp2_pp2: llama3_debugmodel_fsdp2_tp2_pp2().
  deepseek_v3_debugmodel_mtp_cp2: deepseek_v3_debugmodel_mtp_cp2().
  deepseek_v4_debugmodel_fsdp2_tp2_ep2: deepseek_v4_debugmodel_fsdp2_tp2_ep2().
  qwen35_debugmodel_moe_fsdp4_tp2_ep4: qwen35_debugmodel_moe_fsdp4_tp2_ep4().
  deepseek_v3_debugmodel_mtp_fsdp4_ep2_compile: deepseek_v3_debugmodel_mtp_fsdp4_ep2_compile().
  kimi_k2_5_debugmodel_muon_fsdp2_pp2_ep2: kimi_k2_5_debugmodel_muon_fsdp2_pp2_ep2().
  qwen3_debugmodel_fsdp2_tp2_cp2: qwen3_debugmodel_fsdp2_tp2_cp2().
  qwen3_debugmodel_non_fused_qkv_fsdp2_tp2_cp2: qwen3_debugmodel_non_fused_qkv_fsdp2_tp2_cp2().
  qwen35_debugmodel_moe_fsdp2_tp2_pp2_ep4: qwen35_debugmodel_moe_fsdp2_tp2_pp2_ep4().
  qwen35_debugmodel_varlen_attn_fsdp2_tp2_sac: qwen35_debugmodel_varlen_attn_fsdp2_tp2_sac().
  gpt_oss_debugmodel_fsdp4_tp2_ep4_compile: gpt_oss_debugmodel_fsdp4_tp2_ep4_compile().
  deepseek_v3_debugmodel_fused_mla_swiglu_fsdp4_ep2: deepseek_v3_debugmodel_fused_mla_swiglu_fsdp4_ep2().
  kimi_k2_5_debugmodel_muon_fsdp8_ep8: kimi_k2_5_debugmodel_muon_fsdp8_ep8().
  deepseek_v3_debugmodel_hsdp2x2_ep2: deepseek_v3_debugmodel_hsdp2x2_ep2().
  qwen3_debugmodel_moe_param_groups_fsdp2_tp2_ep4: qwen3_debugmodel_moe_param_groups_fsdp2_tp2_ep4().
  muse_glimmer_debugmodel_mm_fsdp2_tp2: muse_glimmer_debugmodel_mm_fsdp2_tp2().
  llama3_debugmodel_region_ac_fsdp2_tp2_cp2: llama3_debugmodel_region_ac_fsdp2_tp2_cp2().
  deepseek_v3_debugmodel_mtp_tp2_cp2: deepseek_v3_debugmodel_mtp_tp2_cp2().
  kimi_k2_5_debugmodel_seed_checkpoint: kimi_k2_5_debugmodel_seed_checkpoint().
  qwen3_debugmodel_fsdp2_tp2_cp2_no_sp: qwen3_debugmodel_fsdp2_tp2_cp2_no_sp().
  deepseek_v3_debugmodel_fsdp8_ep8: deepseek_v3_debugmodel_fsdp8_ep8().
  muse_glimmer_debugmodel_fsdp8: muse_glimmer_debugmodel_fsdp8().
---
# Module: [`torchtitan_recipes/tests/models.py`](../../../../../../raw/code/torchtitan/torchtitan_recipes/tests/models.py)

## Functions
- <a id="_configure_fsdp_numerics"></a>`_configure_fsdp_numerics(config: Trainer.Config, *, expert_parallel_degree: int = 1)` — [`L34`](../../../../../../raw/code/torchtitan/torchtitan_recipes/tests/models.py#L34) — Use a logical-world-eight FSDP topology for numerical comparison.
- <a id="deepseek_v3_debugmodel_fsdp2_cp2_pp2_ep4"></a>`deepseek_v3_debugmodel_fsdp2_cp2_pp2_ep4()` — [`L149`](../../../../../../raw/code/torchtitan/torchtitan_recipes/tests/models.py#L149)
- <a id="deepseek_v3_debugmodel_fsdp2_tp2_cp2_ep8"></a>`deepseek_v3_debugmodel_fsdp2_tp2_cp2_ep8()` — [`L133`](../../../../../../raw/code/torchtitan/torchtitan_recipes/tests/models.py#L133)
- <a id="deepseek_v3_debugmodel_fsdp8_ep8"></a>`deepseek_v3_debugmodel_fsdp8_ep8()` — [`L127`](../../../../../../raw/code/torchtitan/torchtitan_recipes/tests/models.py#L127)
- <a id="deepseek_v3_debugmodel_fused_mla_swiglu_fsdp4_ep2"></a>`deepseek_v3_debugmodel_fused_mla_swiglu_fsdp4_ep2()` — [`L193`](../../../../../../raw/code/torchtitan/torchtitan_recipes/tests/models.py#L193)
- <a id="deepseek_v3_debugmodel_hsdp2x2_ep2"></a>`deepseek_v3_debugmodel_hsdp2x2_ep2()` — [`L166`](../../../../../../raw/code/torchtitan/torchtitan_recipes/tests/models.py#L166)
- <a id="deepseek_v3_debugmodel_mtp_cp2"></a>`deepseek_v3_debugmodel_mtp_cp2()` — [`L106`](../../../../../../raw/code/torchtitan/torchtitan_recipes/tests/models.py#L106)
- <a id="deepseek_v3_debugmodel_mtp_fsdp4_ep2_compile"></a>`deepseek_v3_debugmodel_mtp_fsdp4_ep2_compile()` — [`L92`](../../../../../../raw/code/torchtitan/torchtitan_recipes/tests/models.py#L92)
- <a id="deepseek_v3_debugmodel_mtp_tp2_cp2"></a>`deepseek_v3_debugmodel_mtp_tp2_cp2()` — [`L120`](../../../../../../raw/code/torchtitan/torchtitan_recipes/tests/models.py#L120)
- <a id="deepseek_v4_debugmodel_fsdp2_tp2_ep2"></a>`deepseek_v4_debugmodel_fsdp2_tp2_ep2()` — [`L176`](../../../../../../raw/code/torchtitan/torchtitan_recipes/tests/models.py#L176)
- <a id="gpt_oss_debugmodel_flex_fsdp2_cp2_pp2_ep4_sac"></a>`gpt_oss_debugmodel_flex_fsdp2_cp2_pp2_ep4_sac()` — [`L343`](../../../../../../raw/code/torchtitan/torchtitan_recipes/tests/models.py#L343)
- <a id="gpt_oss_debugmodel_fsdp4_pp2_ep4_sac"></a>`gpt_oss_debugmodel_fsdp4_pp2_ep4_sac()` — [`L365`](../../../../../../raw/code/torchtitan/torchtitan_recipes/tests/models.py#L365)
- <a id="gpt_oss_debugmodel_fsdp4_tp2_ep4"></a>`gpt_oss_debugmodel_fsdp4_tp2_ep4()` — [`L329`](../../../../../../raw/code/torchtitan/torchtitan_recipes/tests/models.py#L329)
- <a id="gpt_oss_debugmodel_fsdp4_tp2_ep4_compile"></a>`gpt_oss_debugmodel_fsdp4_tp2_ep4_compile()` — [`L318`](../../../../../../raw/code/torchtitan/torchtitan_recipes/tests/models.py#L318)
- <a id="kimi_k2_5_debugmodel_muon_fsdp2_pp2_ep2"></a>`kimi_k2_5_debugmodel_muon_fsdp2_pp2_ep2()` — [`L380`](../../../../../../raw/code/torchtitan/torchtitan_recipes/tests/models.py#L380) — One four-GPU smoke path covering PP=2, FSDP=2, and EP=2.
- <a id="kimi_k2_5_debugmodel_muon_fsdp8_ep8"></a>`kimi_k2_5_debugmodel_muon_fsdp8_ep8()` — [`L402`](../../../../../../raw/code/torchtitan/torchtitan_recipes/tests/models.py#L402)
- <a id="kimi_k2_5_debugmodel_seed_checkpoint"></a>`kimi_k2_5_debugmodel_seed_checkpoint()` — [`L413`](../../../../../../raw/code/torchtitan/torchtitan_recipes/tests/models.py#L413) — Use the same Kimi model with an optimizer safe for unsharded setup.
- <a id="llama3_debugmodel_fsdp2_tp2_cp2"></a>`llama3_debugmodel_fsdp2_tp2_cp2()` — [`L51`](../../../../../../raw/code/torchtitan/torchtitan_recipes/tests/models.py#L51)
- <a id="llama3_debugmodel_fsdp2_tp2_pp2"></a>`llama3_debugmodel_fsdp2_tp2_pp2()` — [`L78`](../../../../../../raw/code/torchtitan/torchtitan_recipes/tests/models.py#L78)
- <a id="llama3_debugmodel_region_ac_fsdp2_tp2_cp2"></a>`llama3_debugmodel_region_ac_fsdp2_tp2_cp2()` — [`L66`](../../../../../../raw/code/torchtitan/torchtitan_recipes/tests/models.py#L66)
- <a id="muse_glimmer_debugmodel_fsdp2_tp2_cp2"></a>`muse_glimmer_debugmodel_fsdp2_tp2_cp2()` — [`L427`](../../../../../../raw/code/torchtitan/torchtitan_recipes/tests/models.py#L427)
- <a id="muse_glimmer_debugmodel_fsdp8"></a>`muse_glimmer_debugmodel_fsdp8()` — [`L421`](../../../../../../raw/code/torchtitan/torchtitan_recipes/tests/models.py#L421)
- <a id="muse_glimmer_debugmodel_mm_fsdp2_tp2"></a>`muse_glimmer_debugmodel_mm_fsdp2_tp2()` — [`L445`](../../../../../../raw/code/torchtitan/torchtitan_recipes/tests/models.py#L445)
- <a id="muse_glimmer_debugmodel_mm_tp2_cp2_pp2"></a>`muse_glimmer_debugmodel_mm_tp2_cp2_pp2()` — [`L458`](../../../../../../raw/code/torchtitan/torchtitan_recipes/tests/models.py#L458)
- <a id="qwen35_debugmodel_moe_fsdp2_tp2_pp2_ep4"></a>`qwen35_debugmodel_moe_fsdp2_tp2_pp2_ep4()` — [`L276`](../../../../../../raw/code/torchtitan/torchtitan_recipes/tests/models.py#L276)
- <a id="qwen35_debugmodel_moe_fsdp4_tp2_ep4"></a>`qwen35_debugmodel_moe_fsdp4_tp2_ep4()` — [`L290`](../../../../../../raw/code/torchtitan/torchtitan_recipes/tests/models.py#L290)
- <a id="qwen35_debugmodel_varlen_attn_fsdp2_tp2_sac"></a>`qwen35_debugmodel_varlen_attn_fsdp2_tp2_sac()` — [`L306`](../../../../../../raw/code/torchtitan/torchtitan_recipes/tests/models.py#L306)
- <a id="qwen3_debugmodel_fsdp2_tp2_cp2"></a>`qwen3_debugmodel_fsdp2_tp2_cp2()` — [`L232`](../../../../../../raw/code/torchtitan/torchtitan_recipes/tests/models.py#L232)
- <a id="qwen3_debugmodel_fsdp2_tp2_cp2_compile_helion_rope"></a>`qwen3_debugmodel_fsdp2_tp2_cp2_compile_helion_rope()` — [`L250`](../../../../../../raw/code/torchtitan/torchtitan_recipes/tests/models.py#L250)
- <a id="qwen3_debugmodel_fsdp2_tp2_cp2_no_sp"></a>`qwen3_debugmodel_fsdp2_tp2_cp2_no_sp()` — [`L244`](../../../../../../raw/code/torchtitan/torchtitan_recipes/tests/models.py#L244)
- <a id="qwen3_debugmodel_moe_param_groups_fsdp2_tp2_cp2_ep8"></a>`qwen3_debugmodel_moe_param_groups_fsdp2_tp2_cp2_ep8()` — [`L216`](../../../../../../raw/code/torchtitan/torchtitan_recipes/tests/models.py#L216)
- <a id="qwen3_debugmodel_moe_param_groups_fsdp2_tp2_ep4"></a>`qwen3_debugmodel_moe_param_groups_fsdp2_tp2_ep4()` — [`L206`](../../../../../../raw/code/torchtitan/torchtitan_recipes/tests/models.py#L206)
- <a id="qwen3_debugmodel_non_fused_qkv_fsdp2_tp2_cp2"></a>`qwen3_debugmodel_non_fused_qkv_fsdp2_tp2_cp2()` — [`L264`](../../../../../../raw/code/torchtitan/torchtitan_recipes/tests/models.py#L264)

