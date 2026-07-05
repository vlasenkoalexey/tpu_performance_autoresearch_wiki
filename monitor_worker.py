import subprocess
import time
import re
import yaml

CLUSTER_CONTEXT = "gke_tpu-pytorch_us-central2_alekseyv-tpu-v6e8-spot-xpk"
WORKLOAD_NAME = "alekseyv-qwen3-jax-v031-maxce-sp1"
CLUSTER_NAME = "alekseyv-tpu-v6e8-spot-xpk"
CLUSTER_PROJECT = "tpu-pytorch"
CLUSTER_ZONE = "us-central2"
GCS_ROOT = "gs://tpu-pytorch-alekseyv-us-central2/autoresearch/qwen3_ag/2026-07-03-qwen3-jax-v031-maxtext-ce-bs4"

def run(cmd):
    return subprocess.run(cmd, shell=True, capture_output=True, text=True)

def get_pod():
    res = run(f"kubectl --context={CLUSTER_CONTEXT} get pods --no-headers")
    for line in res.stdout.split('\n'):
        if line.startswith(f"{WORKLOAD_NAME}-slice-job-0-0"):
            return line.split()[0]
    return None

def main():
    start_time = time.time()
    last_log_content = ""
    last_log_change_time = time.time()
    last_hlo_count = 0
    last_step = None
    steps_seen = 0
    
    pod = None
    while not pod:
        pod = get_pod()
        if not pod:
            time.sleep(10)
            
    print(f"Monitoring pod: {pod}", flush=True)
    
    while True:
        res = run(f"kubectl --context={CLUSTER_CONTEXT} get pod {pod} -o jsonpath='{{.status.phase}}'")
        phase = res.stdout.strip()
        if phase in ['Succeeded', 'Failed']:
            break
            
        wall_time = time.time() - start_time
        if wall_time > 3600:
            print("Hard ceiling 60m reached. Killing.", flush=True)
            run(f"yes | xpk workload delete --workload={WORKLOAD_NAME} --cluster={CLUSTER_NAME} --project={CLUSTER_PROJECT} --zone={CLUSTER_ZONE}")
            break
            
        log_res = run(f"kubectl --context={CLUSTER_CONTEXT} logs {pod} --tail=200")
        current_logs = log_res.stdout
        
        if current_logs != last_log_content:
            last_log_content = current_logs
            last_log_change_time = time.time()
            for line in current_logs.split('\n'):
                m = re.search(r'step[\s=:]*(\d+)', line, re.IGNORECASE)
                if m:
                    last_step = int(m.group(1))
                    steps_seen = max(steps_seen, last_step)
        
        time_since_log = time.time() - last_log_change_time
        
        if time_since_log > 300: # 5 mins
            print("5 mins no logs. Checking Tier 1", flush=True)
            top_res = run(f"kubectl --context={CLUSTER_CONTEXT} top pod {pod} --no-headers")
            cpu_val = 0
            if top_res.stdout:
                m = re.search(r'(\d+)m', top_res.stdout)
                if m:
                    cpu_val = int(m.group(1))
            
            hlo_res = run(f"gsutil ls -l {GCS_ROOT}/hlo/ 2>/dev/null | wc -l")
            try:
                hlo_count = int(hlo_res.stdout.strip())
            except:
                hlo_count = 0
                
            print(f"CPU m: {cpu_val}, HLO count: {hlo_count}", flush=True)
            
            if cpu_val < 500 and hlo_count == last_hlo_count:
                print("Tier 2 Hang detected. Killing.", flush=True)
                run(f"yes | xpk workload delete --workload={WORKLOAD_NAME} --cluster={CLUSTER_NAME} --project={CLUSTER_PROJECT} --zone={CLUSTER_ZONE}")
                
                report = {
                    "state": "hung",
                    "exit_code": None,
                    "phase_at_end": f"step_{last_step}" if last_step is not None else "compiling",
                    "wall_time_s": int(wall_time),
                    "steps_seen": steps_seen,
                    "last_step_logged": last_step,
                    "hang_evidence": f"5min idle, CPU {cpu_val}m, HLO module count unchanged at {hlo_count} for 5min",
                    "profile_gcs": "missing",
                    "hlo_gcs": "missing",
                    "last_log_lines": "\n".join(current_logs.split('\n')[-10:]),
                    "headline": f"Hung at step {last_step}" if last_step is not None else "Hung during compile"
                }
                with open("final_report.yaml", "w") as f:
                    yaml.dump(report, f)
                return
            
            last_hlo_count = hlo_count
        
        time.sleep(30)
        
    wall_time = time.time() - start_time
    exit_res = run(f"kubectl --context={CLUSTER_CONTEXT} get pod {pod} -o jsonpath='{{.status.containerStatuses[0].state.terminated.exitCode}}'")
    try:
        exit_code = int(exit_res.stdout.strip())
    except:
        exit_code = 1
        
    prof_res = run(f"gsutil ls {GCS_ROOT}/plugins/profile/ 2>&1 | head -3")
    hlo_res = run(f"gsutil ls {GCS_ROOT}/hlo/ 2>&1 | head -3")
    
    prof_ok = "Exception" not in prof_res.stdout and len(prof_res.stdout.strip()) > 0
    hlo_ok = "Exception" not in hlo_res.stdout and len(hlo_res.stdout.strip()) > 0
    
    state = "completed" if exit_code == 0 and prof_ok and hlo_ok else "crashed"
    
    last_log_lines = "\n".join(last_log_content.split('\n')[-10:])
    
    report = {
        "state": state,
        "exit_code": exit_code,
        "phase_at_end": f"step_{last_step}" if last_step is not None else "crash",
        "wall_time_s": int(wall_time),
        "steps_seen": steps_seen,
        "last_step_logged": last_step,
        "profile_gcs": f"{GCS_ROOT}/plugins/profile/" if prof_ok else "missing",
        "hlo_gcs": f"{GCS_ROOT}/hlo/" if hlo_ok else "missing",
        "last_log_lines": last_log_lines,
        "headline": f"Ran {steps_seen} steps clean" if state == 'completed' else f"Crashed with exit code {exit_code}"
    }
    with open("final_report.yaml", "w") as f:
        yaml.dump(report, f)

if __name__ == '__main__':
    main()
