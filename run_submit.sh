#!/bin/bash
yes | xpk workload create --workload="alekseyv-qwen3-jax-v059e-tp2-bs4" \
  --cluster="alekseyv-tpu-v6e8-spot-xpk" \
  --project="tpu-pytorch" \
  --zone="us-central2" \
  --tpu-type="v6e-8" \
  --docker-image="us-central1-docker.pkg.dev/tpu-pytorch/torchtitan-images/qwen3-8b-jax:v059d-tp2-bs4" \
  --command='LIBTPU_INIT_ARGS="--xla_tpu_scoped_vmem_limit_kib=81920" XLA_FLAGS="--xla_dump_to=gs://tpu-pytorch-alekseyv-us-central2/autoresearch/qwen3_ag/2026-07-05-qwen3-jax-v059e-tp2-bs4/hlo --xla_dump_hlo_as_text --xla_dump_hlo_as_proto --xla_dump_hlo_pass_re=.*" JAX_PERSISTENT_CACHE_MIN_COMPILE_TIME_SECS=1 JAX_PERSISTENT_CACHE_MIN_ENTRY_SIZE_BYTES=0 JAX_COMPILATION_CACHE_DIR=gs://tpu-pytorch-alekseyv-us-central2/jax-compile-cache JAX_REMAT=1 JAX_ATTENTION_IMPL=splash python -m train --train_steps 20 --batch_size 4 --seqlen 8192 --tp_parallelism 2 --profile_dir gs://tpu-pytorch-alekseyv-us-central2/autoresearch/qwen3_ag/2026-07-05-qwen3-jax-v059e-tp2-bs4/plugins/profile --profile_start_step 10 --profile_steps 3'
