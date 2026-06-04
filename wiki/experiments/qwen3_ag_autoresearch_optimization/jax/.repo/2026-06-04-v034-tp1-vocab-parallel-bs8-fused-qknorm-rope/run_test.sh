#!/bin/bash
xpk workload create \
  --workload alekseyv-qwen3-v034-test6 \
  --command "cd /app && LIBTPU_INIT_ARGS='--xla_tpu_scoped_vmem_limit_kib=98304' JAX_PLATFORMS='tpu' python /app/test_custom_vjp.py" \
  --tpu-type=v6e-8 \
  --num-slices=1 \
  --cluster alekseyv-tpu-v6e8-spot-xpk \
  --zone us-central2-b \
  --project tpu-pytorch \
  --docker-image us-central1-docker.pkg.dev/tpu-pytorch/torchtitan-images/qwen3-test
