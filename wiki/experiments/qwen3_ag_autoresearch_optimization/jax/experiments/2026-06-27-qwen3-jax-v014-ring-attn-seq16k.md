---
variant: 8B/v6e-8
hypothesis: Ring attention seqlen=16384 scaling
status: invalid
created: 2026-06-27
---

# Experiment v014: Ring attention seqlen=16384 scaling

## Hypothesis under test

**Hypothesis**: Increasing the sequence length to 16384 will amortize the sequence-parallel cross-chip communication overhead introduced by Ring Attention, improving the MFU above the 22.8% observed at 8K context.

**Mechanism**: We will run the exact same `v012` Ring Attention codebase but with `--seqlen 16384` and `--batch_size 4` (to keep total tokens per step constant at 65536). The communication of KV blocks over the ring is overlapped with block compute; doubling the sequence length quadruples the attention compute per head while only doubling the communication, which should shift the roofline from memory/network-bound back towards compute-bound.

**Predicted signal**: We expect step MFU to rise significantly from 22.8% toward the 32.5% single-chip baseline. `all-gather` and `reduce-scatter` communication time fraction should drop in the profile.

**Falsification criterion**: Step MFU does not exceed 25%.

## Setup

```bash
# Actual command from gke-cluster-runner report
LIBTPU_INIT_ARGS="--xla_tpu_scoped_vmem_limit_kib=81920" XLA_FLAGS="--xla_dump_to=gs://tpu-pytorch-alekseyv-us-central2/autoresearch/qwen3_ag/2026-06-27-qwen3-jax-v014-ring-attn-seq16k/hlo --xla_dump_hlo_as_text --xla_dump_hlo_as_proto --xla_dump_hlo_pass_re=.*" JAX_PERSISTENT_CACHE_MIN_COMPILE_TIME_SECS=1 JAX_PERSISTENT_CACHE_MIN_ENTRY_SIZE_BYTES=0 JAX_COMPILATION_CACHE_DIR=gs://tpu-pytorch-alekseyv-us-central2/jax-compile-cache JAX_REMAT=1 JAX_ATTENTION_IMPL=splash python -m train --train_steps 20 --batch_size 4 --seqlen 16384 --profile_dir gs://tpu-pytorch-alekseyv-us-central2/autoresearch/qwen3_ag/2026-06-27-qwen3-jax-v014-ring-attn-seq16k/plugins/profile --profile_start_step 10 --profile_steps 3
```
- Image: `us-central1-docker.pkg.dev/tpu-pytorch/torchtitan-images/qwen3-8b-jax:v012-ring-attention`
- Cluster: `alekseyv-tpu-v6e8-spot-xpk`

## Results

**Status**: Crashed
**Exit Code**: 1
**Phase at End**: compiling

```
[train] starting train_steps=20 per_chip_batch=4 global_batch=32
[splash] bq=1024 bkv=1024 bq_dkv=1024 bkv_dkv=1024 fused_bwd=True bq_dq=None bkv_dq=None
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "/app/trainer/train.py", line 239, in <module>
    fire.Fire(main)
  File "/opt/venv/lib/python3.12/site-packages/fire/core.py", line 135, in Fire
    component_trace = _Fire(component, args, parsed_flag_args, context, name)
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/venv/lib/python3.12/site-packages/fire/core.py", line 468, in _Fire
    component, remaining_args = _CallAndUpdateTrace(
                                ^^^^^^^^^^^^^^^^^^^^
  File "/opt/venv/lib/python3.12/site-packages/fire/core.py", line 684, in _CallAndUpdateTrace
    component = fn(*varargs, **kwargs)
                ^^^^^^^^^^^^^^^^^^^^^^
  File "/app/trainer/train.py", line 189, in main
    loss, params, opt_state = jitted_step(params, opt_state, input_ids, labels)
                              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
jax.errors.JaxRuntimeError: RESOURCE_EXHAUSTED: Allocation (size=39829110784) would exceed memory (size=33822867456) :: #allocation710 [shape = 'f32[4,16384,151936]{2,1,0:T(8,128)}', space=hbm, size = 0xffffffffffffffff, tag = 'output of fusion.527@{1}'] :: <no-hlo-instruction>
```

## Profile

Missing due to compile-time crash.

## HLO Dump

Available at: `gs://tpu-pytorch-alekseyv-us-central2/autoresearch/qwen3_ag/2026-06-27-qwen3-jax-v014-ring-attn-seq16k/hlo/`

## Verdict

**invalid** - The experiment crashed with an OOM at compile time. The per-chip batch size of 4 with a 16384 sequence length causes the fusion output `[4, 16384, 151936]` (the logits tensor before the CE loss) to require ~39.8GB in float32, which exceeds the ~33.8GB HBM capacity of the v6e chip.



## Next hypotheses

None — TODO: backfill reason


## See also

<!-- TODO: add links -->


## Sources

<!-- TODO: add sources -->
