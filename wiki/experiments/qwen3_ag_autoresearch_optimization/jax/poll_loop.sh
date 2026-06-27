#!/bin/bash
while true; do
  kubectl logs -l job-name=alekseyv-qwen3-jax-v005-batch-slice-job-0 --tail=200 > current_logs.txt
  if grep -q "EXIT_CODE=1" current_logs.txt || grep -q "XPK End" current_logs.txt || grep -q "Traceback" current_logs.txt || grep -q "jax.errors" current_logs.txt; then
    echo "Job completed or failed."
    cat current_logs.txt
    break
  fi
  sleep 30
done
