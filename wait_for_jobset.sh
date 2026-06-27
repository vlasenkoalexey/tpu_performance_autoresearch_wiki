#!/bin/bash
CONTEXT="gke_tpu-pytorch_us-central2_alekseyv-tpu-v6e8-spot-xpk"
JOBSET="alekseyv-qwen3-jax-v002-tokamax-ce-d"

while true; do
  STATUS=$(kubectl --context $CONTEXT get jobset $JOBSET -o jsonpath='{.status.conditions[?(@.type=="Completed")].status}' 2>/dev/null)
  FAILED=$(kubectl --context $CONTEXT get jobset $JOBSET -o jsonpath='{.status.conditions[?(@.type=="Failed")].status}' 2>/dev/null)
  
  if [ "$STATUS" == "True" ]; then
    echo "Jobset completed successfully."
    exit 0
  fi
  
  if [ "$FAILED" == "True" ]; then
    echo "Jobset failed."
    exit 1
  fi
  
  # Also check if it's no longer found (deleted)
  kubectl --context $CONTEXT get jobset $JOBSET >/dev/null 2>&1
  if [ $? -ne 0 ]; then
    echo "Jobset not found."
    exit 1
  fi

  sleep 30
done
