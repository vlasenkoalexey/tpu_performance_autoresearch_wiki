#!/bin/bash
CLUSTER_CONTEXT="gke_tpu-pytorch_us-central2_alekseyv-tpu-v6e8-spot-xpk"
WORKLOAD_NAME="alekseyv-qwen3-jax-v059c-tp2-bs4"
GCS_ROOT="gs://tpu-pytorch-alekseyv-us-central2/autoresearch/qwen3_ag/2026-07-04-qwen3-jax-v059c-tp2-bs4"
CLUSTER_NAME="alekseyv-tpu-v6e8-spot-xpk"
CLUSTER_PROJECT="tpu-pytorch"
CLUSTER_ZONE="us-central2"

# Ensure we loop forever until an exit condition is met
while true; do
  start_time=$(date +%s)
  
  POD=$(kubectl --context="${CLUSTER_CONTEXT}" get pods --no-headers 2>/dev/null | awk -v wn="${WORKLOAD_NAME}-slice-job-0-0-0" '$1 ~ "^"wn {print $1; exit}')
  
  if [ -z "$POD" ]; then
    echo "Waiting for pod to appear..."
  else
    # Check pod state
    STATE=$(kubectl --context="${CLUSTER_CONTEXT}" get pod "${POD}" -o jsonpath='{.status.phase}' 2>/dev/null)
    
    if [ "$STATE" == "Succeeded" ] || [ "$STATE" == "Failed" ]; then
      EXIT=$(kubectl --context="${CLUSTER_CONTEXT}" get pod "${POD}" -o jsonpath='{.status.containerStatuses[0].state.terminated.exitCode}' 2>/dev/null)
      echo "Pod terminated with exit code: $EXIT"
      
      echo "Fetching logs..."
      kubectl --context="${CLUSTER_CONTEXT}" logs "${POD}" --tail=50
      
      echo "Checking artifacts..."
      gsutil ls "${GCS_ROOT}/plugins/profile/" 2>&1 | head -3
      gsutil ls "${GCS_ROOT}/hlo/" 2>&1 | head -3
      
      exit 0
    elif [ "$STATE" == "Running" ]; then
      echo "Pod is Running. Fetching logs..."
      kubectl --context="${CLUSTER_CONTEXT}" logs "${POD}" --tail=50
    else
      echo "Pod state: $STATE"
    fi
  fi
  
  end_time=$(date +%s)
  elapsed=$((end_time - start_time))
  
  if [ $elapsed -lt 30 ]; then
    sleep $((30 - elapsed))
  fi
done
