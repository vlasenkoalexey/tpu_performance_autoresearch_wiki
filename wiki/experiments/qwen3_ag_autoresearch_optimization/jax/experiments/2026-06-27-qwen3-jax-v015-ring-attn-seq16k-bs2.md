---
variant: 8B/v6e-8
hypothesis: Ring attention seqlen=16384 scaling (batch_size=2)
status: invalid
created: 2026-06-27
---

# Experiment v015: Ring attention seqlen=16384 scaling (batch_size=2)

## Hypothesis under test

**Hypothesis**: Decreasing the per-chip batch size to 2 while keeping sequence length at 16384 will avoid the compile-time OOM from the ~40GB logits tensor, allowing us to successfully amortize the sequence-parallel cross-chip communication overhead introduced by Ring Attention.

**Mechanism**: We run the `v012` Ring Attention codebase but with `--seqlen 16384` and `--batch_size 2`. This reduces the float32 logits tensor to `[2, 16384, 151936]`, which occupies ~19.9GB (comfortably fitting in the 33.8GB HBM capacity of the v6e chip), while still providing enough attention compute per head to overlap communication of KV blocks over the ring.

**Predicted signal**: We expect the step MFU to rise significantly from 22.8% (at 8K context) toward the 32.5% single-chip baseline. `all-gather` and `reduce-scatter` communication time fraction should drop in the profile.

**Falsification criterion**: Step MFU does not exceed 25% or the run crashes with an OOM.

## Setup

```bash
# Actual command from gke-cluster-runner report
LIBTPU_INIT_ARGS="--xla_tpu_scoped_vmem_limit_kib=81920" XLA_FLAGS="--xla_dump_to=gs://tpu-pytorch-alekseyv-us-central2/autoresearch/qwen3_ag/2026-06-27-qwen3-jax-v015-ring-attn-seq16k-bs2/hlo --xla_dump_hlo_as_text --xla_dump_hlo_as_proto --xla_dump_hlo_pass_re=.*" JAX_PERSISTENT_CACHE_MIN_COMPILE_TIME_SECS=1 JAX_PERSISTENT_CACHE_MIN_ENTRY_SIZE_BYTES=0 JAX_COMPILATION_CACHE_DIR=gs://tpu-pytorch-alekseyv-us-central2/jax-compile-cache JAX_REMAT=1 JAX_ATTENTION_IMPL=splash python -m train --train_steps 20 --batch_size 2 --seqlen 16384 --profile_dir gs://tpu-pytorch-alekseyv-us-central2/autoresearch/qwen3_ag/2026-06-27-qwen3-jax-v015-ring-attn-seq16k-bs2/plugins/profile --profile_start_step 10 --profile_steps 3
```
- Image: `us-central1-docker.pkg.dev/tpu-pytorch/torchtitan-images/qwen3-8b-jax:v012-ring-attention`
- Cluster: `alekseyv-tpu-v6e8-spot-xpk`

## Results

**Status**: Crashed
**Exit Code**: 1
**Phase at End**: crash

```
jax.errors.JaxRuntimeError: RESOURCE_EXHAUSTED: XLA:TPU compile permanent error. Ran out of memory in memory space hbm. Used 46.60G of 31.25G hbm. Exceeded hbm capacity by 15.35G.

Total hbm usage >= 46.85G:
    reserved        260.00M 
    program          46.60G 
    arguments            0B 

Output size 0B; shares 0B with arguments.

Program hbm requirement 46.60G:
    global           336.5K
    HLO temp         46.60G (100.0% utilization: Unpadded (37.34G) Padded (37.34G), 19.9% fragmentation (9.26G))
```

## Profile

Missing due to compile-time OOM.

## HLO Dump

Available at: `gs://tpu-pytorch-alekseyv-us-central2/autoresearch/qwen3_ag/2026-06-27-qwen3-jax-v015-ring-attn-seq16k-bs2/hlo/`

## Verdict

**invalid** - The experiment crashed with an OOM at compile time due to excessive HLO temp memory requirement (46.60G). Even with `batch_size=2`, the combination of `seqlen=16384` and `sp=2` causes intermediate buffers in the XLA graph to blow past the 31.25G HBM capacity limit. Scaling Ring Attention on this topology size (v6e-8) to amortize communication overhead seems blocked by memory constraints for now.



## Next hypotheses

None — TODO: backfill reason


## See also

<!-- TODO: add links -->


## Sources

<!-- TODO: add sources -->
