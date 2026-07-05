#!/bin/bash

workload_name="alekseyv-qwen3-jax-v016-glubw-v9"
cluster_name="alekseyv-tpu-v6e8-spot-xpk"
cluster_context="gke_tpu-pytorch_us-central2_alekseyv-tpu-v6e8-spot-xpk"
cluster_project="tpu-pytorch"
cluster_zone="us-central2"
gcs_root="gs://tpu-pytorch-alekseyv-us-central2/autoresearch/qwen3_ag/2026-06-27-qwen3-jax-v016-fused-glu-bwd"

start_time=$(date +%s)
last_log_lines=""
last_log_time=$(date +%s)
last_hlo_count=0
state="running"
hang_evidence=""
steps_seen=0
last_step_logged="null"

while true; do
  loop_start=$(date +%s)
  
  POD=$(kubectl --context="${cluster_context}" get pods --no-headers 2>/dev/null | awk -v wn="${workload_name}-slice-job-0-0-0" '$1 ~ "^"wn {print $1; exit}')
  
  if [ -n "$POD" ]; then
    PHASE=$(kubectl --context="${cluster_context}" get pod "${POD}" -o jsonpath='{.status.phase}' 2>/dev/null)
    
    if [ "$PHASE" == "Succeeded" ] || [ "$PHASE" == "Failed" ]; then
      break
    fi
    
    logs=$(kubectl --context="${cluster_context}" logs "${POD}" --tail=200 2>/dev/null)
    if [ "$logs" != "$last_log_lines" ] && [ -n "$logs" ]; then
      last_log_time=$(date +%s)
      last_log_lines="$logs"
      
      latest_step=$(echo "$logs" | grep -iE 'step [0-9]+' | tail -1 | grep -oE '[0-9]+' | head -1)
      if [ -n "$latest_step" ]; then
        last_step_logged=$latest_step
        steps_seen=$(echo "$logs" | grep -icE 'step [0-9]+')
      fi
    fi
    
    now=$(date +%s)
    idle_time=$((now - last_log_time))
    
    if [ $idle_time -ge 300 ]; then
      CPU=$(kubectl --context="${cluster_context}" top pod "${POD}" --no-headers 2>/dev/null | awk '{print $2}' | sed 's/m//')
      HLO_COUNT=$(gsutil ls -l "${gcs_root}/hlo/" 2>/dev/null | wc -l)
      
      if [ -n "$CPU" ] && [ "$CPU" -lt 100 ]; then
        if [ "$HLO_COUNT" -eq "$last_hlo_count" ]; then
          state="hung"
          hang_evidence="5min idle, CPU ${CPU}m, HLO module count unchanged at $HLO_COUNT for 5min"
          yes | xpk workload delete --workload="${workload_name}" --cluster="${cluster_name}" \
            --project="${cluster_project}" --zone="${cluster_zone}"
          break
        fi
      fi
      last_hlo_count=$HLO_COUNT
    fi
  fi
  
  run_time=$(( $(date +%s) - start_time ))
  if [ $run_time -ge 3600 ]; then
    state="hung"
    hang_evidence="60min hard ceiling reached"
    yes | xpk workload delete --workload="${workload_name}" --cluster="${cluster_name}" \
      --project="${cluster_project}" --zone="${cluster_zone}"
    break
  fi
  
  loop_end=$(date +%s)
  loop_duration=$((loop_end - loop_start))
  sleep_time=$((30 - loop_duration))
  if [ $sleep_time -gt 0 ]; then
    sleep $sleep_time
  fi
done

if [ "$state" == "hung" ]; then
  final_state="hung"
  exit_code="null"
  headline="Hung: $hang_evidence"
else
  exit_code=$(kubectl --context="${cluster_context}" get pod "${POD}" -o jsonpath='{.status.containerStatuses[0].state.terminated.exitCode}' 2>/dev/null)
  
  if [ "$exit_code" == "0" ]; then
    gsutil ls "${gcs_root}/plugins/profile/" >/dev/null 2>&1
    prof_ok=$?
    gsutil ls "${gcs_root}/hlo/" >/dev/null 2>&1
    hlo_ok=$?
    
    if [ $prof_ok -ne 0 ] || [ $hlo_ok -ne 0 ]; then
       final_state="crashed"
       headline="Exit 0 but missing profile or HLO artifacts"
    else
       final_state="completed"
       headline="Clean exit 0"
    fi
  else
    final_state="crashed"
    headline="Non-zero exit code $exit_code"
  fi
fi

wall_time=$(( $(date +%s) - start_time ))

cat <<EOF
state: $final_state
exit_code: $exit_code
phase_at_end: ${PHASE:-unknown}
wall_time_s: $wall_time
steps_seen: $steps_seen
last_step_logged: $last_step_logged
EOF

if [ -n "$hang_evidence" ]; then
  echo "hang_evidence: $hang_evidence"
fi

cat <<EOF
profile_gcs: ${gcs_root}/plugins/profile/
hlo_gcs: ${gcs_root}/hlo/
headline: $headline
last_log_lines: |
$(echo "$last_log_lines" | tail -n 10 | sed 's/^/  /')
EOF
