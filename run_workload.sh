#!/bin/bash
cluster_context="gke_tpu-pytorch_us-central2_alekseyv-xpk-v6e-cluster"
user_prefix="alekseyv"
model_name="qwen3"
lane="jax"
workload_name="alekseyv-qwen3-jax-v016-fused-glu-v13"
cluster_name="alekseyv-xpk-v6e-cluster"
image="us-central1-docker.pkg.dev/tpu-pytorch/torchtitan-images/qwen3-8b-jax:v016-fused-glu-bwd-v13"
launch_cmd="XLA_FLAGS=\"--xla_dump_to=gs://tpu-pytorch-alekseyv-us-central2/autoresearch/qwen3_ag/2026-06-27-qwen3-jax-v016-fused-glu-v13/hlo --xla_dump_hlo_as_text --xla_dump_hlo_as_proto --xla_dump_hlo_pass_re=.*\" JAX_PERSISTENT_CACHE_MIN_COMPILE_TIME_SECS=1 JAX_PERSISTENT_CACHE_MIN_ENTRY_SIZE_BYTES=0 JAX_COMPILATION_CACHE_DIR=gs://tpu-pytorch-alekseyv-us-central2/jax-compile-cache python train.py --config=configs/qwen3_8b.yml --model.fused_glu=true"

IFS='_' read -r _ cluster_project cluster_zone _ <<< "${cluster_context}"

yes | xpk workload create --workload="${workload_name}" --cluster="${cluster_name}" \
  --project="${cluster_project}" --zone="${cluster_zone}" \
  --docker-image="${image}" --command="${launch_cmd}" --tpu-type=v6e-32

echo "Waiting 30s for Kueue admission..."
sleep 30
if ! kubectl --context="${cluster_context}" get jobset "${workload_name}" -n default 2>&1; then
  echo "Submission failed."
  exit 1
fi
echo "Jobset created."
