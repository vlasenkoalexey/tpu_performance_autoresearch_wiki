## [2026-06-02] loop-iteration | v006-splash-bs4 on 8B/v6e-8: invalid (splash-backward scoped-VMEM OOM, +2.15M over — tunable)

splash+remat+bs=4: both gates ON, compiled through forward INTO backward — **cleared the v002 HBM wall** (91.7G no longer the blocker). Crashed in the splash backward Pallas kernel `splash_mha_dkv_no_residuals`: scoped vmem 34.15M vs 32M limit, over by just 2.15M (block_q_dkv/block_kv_dkv=2048). NOT HBM-OOM, NOT a kernel NaN — a tunable VMEM-stack overrun. Fix: `--xla_tpu_scoped_vmem_limit_kib=98304` (flag-only). Re-dispatched as v008. No steps/profile; HLO dumped.

## [2026-06-02] loop-iteration | v005-remat-bs3 on 8B/v6e-8: **SUPPORTED — NEW FRONTIER 25.1% MFU** (+3.1pp vs v004)

remat+bs=3 (global 24) fits and beats v004 bs=2: 25.1% MFU, 4,874 tok/s/chip (vs 4,280), MXU 32.7%, loss 12.07 stable, exit 0. bs=2 was NOT the remat ceiling — batch keeps paying. Cumulative climb 20.5%→22.0%→**25.1%** (+22% tok/s/chip over baseline). Frontier config = `--use_remat --batch_size=3` on qwen3-8b-jax:v004-remat. Model page updated. Profile + 51 HLO files in GCS.

## [2026-06-02] loop-iteration | v004-remat-bs2 on 8B/v6e-8: **SUPPORTED — NEW FRONTIER 22.0% MFU** (+1.5pp / +7.3% vs baseline)

Gradient remat (`--use_remat`, per-layer jax.checkpoint) UNLOCKS bs=2 (which OOM'd without it at 43.12G) and lifts effective MFU 20.5% → **22.0%** (4,280 tok/s/chip vs 3,994). xprof: MXU 19.9%→27.8%, matmul share 37.6%→49.7%, collective 21.7%→14.2%. Remat's ~1.3× recompute is outweighed by the bs=2 occupancy gain. **grad-remat hypothesis SUPPORTED.** Committed remat code to TRAINER_DIR; stable lane image = qwen3-8b-jax:v004-remat; remat now default for subsequent experiments. Splash wired into the model (compile-checked, ready for v006). Model page Current best updated. Profile + 28 HLO files in GCS.

## [2026-06-02] loop-iteration | v003-sc-offload on 8B/v6e-8: refuted (−4.0 pp MFU, 16.5% vs 20.5%)

SparseCore collective-offload flags accepted by libtpu (no crash) and functionally offloaded the collectives (profile shows new `async-done` op = 32.2%), but net REGRESSION at the small bs=1 shape — async-offload overhead > TC relief. Unlike llama3 (where SC-offload was +3.4% at bs=4/seq8192+splash). Don't use at this shape; revisit post-splash at a larger shape. Profile + 1602 HLO files in GCS.

## [2026-06-02] loop-iteration | v001-batch-bs2 on 8B/v6e-8: invalid (compile OOM) → batch-scaling REFUTED

bs=2 (global 16) OOMs at compile: 43.12G vs 31.25G HBM, 100% HLO-temp, dominated by `bf16[2,32,2048,2048]` score copies. With v002 (bs=4 → 91.72G) this REFUTES qwen3-jax-batch-scaling: batch can't rise on the dense+no-remat path. Frontier stays at baseline bs=1/20.5% MFU. Filed grad-remat hypothesis; pivoting to memory wins (remat + splash) before batch. No profile (pre-step-0); partial HLO in GCS.

## [2026-06-02] loop-iteration | v002-batch-bs4 on 8B/v6e-8: invalid (compile OOM, HBM-ceiling marker)

bs=4 (global 32) OOMs at compile: 91.72G vs 31.25G HBM (2.9× over), from materialized `bf16[4,32,2048,2048]` attention-score tensors. Marks the dense-attention batch ceiling at bs≤3/seq2048. No profile (pre-step-0); 47 HLO files + memory report in GCS. Lever to pass it: splash (v004).

## [2026-06-02] start | /start-experiment session begin

**Op**: start
**Cluster pool**: alekseyv-tpu-v6e8-spot-xpk (single v6e-8 cluster, 5 free slices → up to 4 concurrent tracks)
**Parallelism**: 4 (4 concurrent workloads on the one cluster's slices)
**First-pick hypothesis**: qwen3-jax-batch-scaling (raise per-chip batch to fill ~20% MXU; flag-only, reuses qwen3-8b-jax image)
**Notes**: session opened via /start-experiment. Adapted flow: in-repo variant (no separate model trunk); flag-only experiments reuse the jax image, code-change experiments build a tagged variant image. Never-stop hook ON.
