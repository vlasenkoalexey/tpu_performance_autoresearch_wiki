#!/bin/bash
CLUSTER_CONTEXT="gke_tpu-pytorch_us-central2_alekseyv-tpu-v6e8-spot-xpk"
WORKLOAD_NAME="alekseyv-qwen3-jax-v034-tokxla-bs4"
CLUSTER_NAME="alekseyv-tpu-v6e8-spot-xpk"
CLUSTER_PROJECT="tpu-pytorch"
CLUSTER_ZONE="us-central2"
GCS_ROOT="gs://tpu-pytorch-alekseyv-us-central2/autoresearch/qwen3_ag/2026-07-03-qwen3-jax-v034-tokamax-xla-bs4"

# Use -slice-job-0-0 as prefix since the pod is named alekseyv-qwen3-jax-v034-tokxla-bs4-slice-job-0-0-hm85s
POD=$(kubectl --context="${CLUSTER_CONTEXT}" get pods --no-headers 2>/dev/null | awk -v wn="${WORKLOAD_NAME}-slice-job-0-0-" '$1 ~ "^"wn {print $1; exit}')
echo "Monitoring $POD"

last_log_count=0
idle_count=0
start_time=$(date +%s)
last_hlo_count=0
last_logs=""

while true; do
  sleep 30
  
  EXIT=$(kubectl --context="${CLUSTER_CONTEXT}" get pod "${POD}" -o jsonpath='{.status.containerStatuses[0].state.terminated.exitCode}' 2>/dev/null)
  
  if [ -n "$EXIT" ]; then
    echo "Terminated with exit code $EXIT"
    break
  fi

  logs=$(kubectl --context="${CLUSTER_CONTEXT}" logs "${POD}" --tail=200 2>/dev/null)
  
  if [ "$logs" = "$last_logs" ]; then
    idle_count=$((idle_count+1))
  else
    idle_count=0
    last_logs="$logs"
    echo "$logs" | tail -n 1
  fi
  
  if [ $idle_count -ge 10 ]; then
    # 5 minutes idle
    cpu=$(kubectl --context="${CLUSTER_CONTEXT}" top pod "${POD}" --no-headers 2>/dev/null | awk '{print $2}' | sed 's/m//')
    hlo_count=$(gsutil ls -l "${GCS_ROOT}/hlo/" 2>/dev/null | wc -l)
    echo "Idle for 5 mins. CPU=${cpu:-0}m, HLO_COUNT=${hlo_count}"
    
    # top pod gives CPU in millicores (e.g. 500m is 50%, 1000m is 100%).
    # "idle/<10%" -> <100m
    if [ "${cpu:-0}" -lt 100 ] && [ "$hlo_count" -eq "$last_hlo_count" ]; then
      echo "HUNG"
      yes | xpk workload delete --workload="${WORKLOAD_NAME}" --cluster="${CLUSTER_NAME}" --project="${CLUSTER_PROJECT}" --zone="${CLUSTER_ZONE}"
      EXIT="hung"
      break
    fi
    last_hlo_count=$hlo_count
  fi
  
  wall_time=$(($(date +%s) - start_time))
  if [ $wall_time -ge 3600 ]; then
    echo "TIMEOUT"
    yes | xpk workload delete --workload="${WORKLOAD_NAME}" --cluster="${CLUSTER_NAME}" --project="${CLUSTER_PROJECT}" --zone="${CLUSTER_ZONE}"
    EXIT="timeout"
    break
  fi
done

echo "EXIT=$EXIT" > monitor_result.txt
kubectl --context="${CLUSTER_CONTEXT}" logs "${POD}" --tail=20 > monitor_logs.txt
echo "DONE"
