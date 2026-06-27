---
hypothesis: qwen3-jax-splash-attention
model: qwen3-ag-jax
variant: "8B/v6e-8"
commit: 319cc42d62c2ffc71056c42ab30d4d0fdbcae8cf
verdict: refuted
---

## Hypothesis under test
[qwen3-jax-splash-attention](../../../../hypotheses/qwen3-jax-splash-attention.md) — GQA-native kernel; avoids `[B,H,S,S]`; prerequisite for seq 8192.

## Setup
Cluster: `alekseyv-tpu-v6e8-spot-xpk` (TPU v6e-8)
Docker image: `us-central1-docker.pkg.dev/tpu-pytorch/torchtitan-images/qwen3-8b-jax:v001-splash-2`
Command:
```bash
LIBTPU_INIT_ARGS="--xla_tpu_scoped_vmem_limit_kib=81920" XLA_FLAGS="--xla_dump_to=... --xla_dump_hlo_as_text --xla_dump_hlo_as_proto --xla_dump_hlo_pass_re=.*" JAX_PERSISTENT_CACHE_MIN_COMPILE_TIME_SECS=1 JAX_PERSISTENT_CACHE_MIN_ENTRY_SIZE_BYTES=0 JAX_COMPILATION_CACHE_DIR=... JAX_ATTENTION_IMPL=splash python -m train --steps 20 --batch_size 1 --seqlen 8192 --profile_dir ... --profile_step 10
```

## Baseline comparison
Baseline: seq2048 bs8 at 512 ms / 31,955 TPS / 20.5% MFU. Target is 8192 context length.

## Results
| Metric | Baseline | This run | Delta | Noise |
|---|---|---|---|---|
| Step time | N/A | N/A | N/A | N/A |
| MFU | N/A | N/A | N/A | N/A |

## Observations
- Crashed during compilation: `RESOURCE_EXHAUSTED: XLA:TPU compile permanent error. Ran out of memory in memory space hbm. Used 44.80G of 31.25G hbm. Exceeded hbm capacity by 13.55G.`

## Verdict
**refuted**. The splash attention kernel alone is insufficient to fit an 8192 sequence length within the 31.25G HBM capacity of a v6e TPU. Additional memory optimization techniques are required to reduce the activation footprint.

## Next hypotheses
- [qwen3-jax-tokamax-ce](../../../../hypotheses/qwen3-jax-tokamax-ce.md) — streamed cross-entropy to drop the logits tensor from HBM.
- [qwen3-jax-gradient-checkpointing](../../../../hypotheses/qwen3-jax-gradient-checkpointing.md) — rematerialize forward activations during the backward pass to drastically cut the HBM footprint.
