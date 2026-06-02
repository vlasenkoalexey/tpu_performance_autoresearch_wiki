## [2026-06-02] start | maxtext reference lane — first run dispatching

**Op**: start (reference-ceiling lane for qwen3_cc).
**Trigger**: confirmed MaxText ships `configs/models/qwen3-8b.yml` matching our architecture exactly (obs `qwen3-maxtext-config-exists.md`).
**Setup**: worktree `/mnt/disks/persist/maxtext-tpu-recipes-v0.1.4` (`tpu-recipes-v0.1.4` / `9f1820b47`), venv `/mnt/disks/persist/venv-maxtext-v0.1.4`, base image `maxtext_base_image:latest` (rebuilt 2026-06-02). Added benchmark configs `qwen3_8b_8192_ref` (seq8192 bs3) + `qwen3_8b_2048_ref` (seq2048 bs4) mirroring the llama3 `no-collective-matmul` recipe tuning.
**Cluster**: alekseyv-tpu-v6e8-spot-xpk (v6e-8, fsdp=8). **First dispatch**: `qwen3_8b_8192_ref` (program-target seq, directly comparable to the llama3 MaxText 44.6% reference).
**Notes**: run via `benchmark_runner xpk` (builds runner image on the base, pushes to gcr.io/tpu-pytorch, submits xpk workload). No model code in this lane — MaxText verbatim.
**Workload**: `ale-qwen3-8b-8-1-060213-9sh` (seq8192, bs3). Entrypoint `python3 -m MaxText.train ... model_name=qwen3-8b`; full MaxText recipe XLA stack incl. SparseCore-offload + HOST_OFFLOAD + jf_spmd (note: jf_spmd crashed our jax build v019 but MaxText's jax0.6.1 image accepts it).
