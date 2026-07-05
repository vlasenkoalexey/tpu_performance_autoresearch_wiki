import subprocess
import time
import sys
import re

cluster_context = "gke_tpu-pytorch_us-central2_alekseyv-tpu-v6e8-spot-xpk"
workload_name = "alekseyv-qwen3-jax-v059e-tp2-bs4"
gcs_root = "gs://tpu-pytorch-alekseyv-us-central2/autoresearch/qwen3_ag/2026-07-05-qwen3-jax-v059e-tp2-bs4"
cluster_name = "alekseyv-tpu-v6e8-spot-xpk"
cluster_project = "tpu-pytorch"
cluster_zone = "us-central2"

def run_cmd(cmd):
    try:
        return subprocess.check_output(cmd, shell=True, text=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        return e.output

def get_pod():
    out = run_cmd(f"kubectl --context={cluster_context} get pods --no-headers")
    prefix = f"{workload_name}-slice-job-0-0-0"
    for line in out.splitlines():
        if line.startswith(prefix):
            return line.split()[0]
    return None

last_log_line_count = 0
last_log_update_time = time.time()
start_time = time.time()
last_hlo_count = 0

def check_hlo_count():
    out = run_cmd(f"gsutil ls -l {gcs_root}/hlo/ | wc -l")
    try:
        return int(out.strip())
    except:
        return 0

def check_cpu(pod):
    out = run_cmd(f"kubectl --context={cluster_context} top pod {pod} --no-headers")
    try:
        for line in out.splitlines():
            if pod in line:
                cpu_str = line.split()[1]
                return int(cpu_str.replace('m', ''))
    except:
        pass
    return 0

while True:
    time.sleep(30)
    
    elapsed = time.time() - start_time
    if elapsed > 3600:
        print("state: hung\nheadline: hard 60m ceiling reached")
        run_cmd(f"yes | xpk workload delete --workload={workload_name} --cluster={cluster_name} --project={cluster_project} --zone={cluster_zone}")
        break

    pod = get_pod()
    if not pod:
        print("Waiting for pod to appear...")
        continue
        
    exit_code_str = run_cmd(f"kubectl --context={cluster_context} get pod {pod} -o jsonpath='{{.status.containerStatuses[0].state.terminated.exitCode}}'")
    if exit_code_str.strip() and exit_code_str.strip().isdigit():
        exit_code = int(exit_code_str.strip())
        print(f"Container exited with {exit_code}")
        break

    logs = run_cmd(f"kubectl --context={cluster_context} logs {pod} --tail=200")
    log_lines = len(logs.splitlines())
    
    # Very rudimentary check for new log lines. Realistically we should hash the last few lines.
    if logs.strip() != "":
        current_hash = hash(logs.strip())
    else:
        current_hash = 0
        
    if not hasattr(check_hlo_count, 'last_hash'):
        check_hlo_count.last_hash = current_hash
        check_hlo_count.last_update = time.time()
        
    if current_hash != check_hlo_count.last_hash:
        check_hlo_count.last_hash = current_hash
        check_hlo_count.last_update = time.time()
        
    idle_time = time.time() - check_hlo_count.last_update
    
    if idle_time > 300: # 5 mins
        cpu = check_cpu(pod)
        current_hlo = check_hlo_count()
        if cpu < 1000 and current_hlo == last_hlo_count: # cpu is in millicores, 1000m = 1 core
            print(f"state: hung\nheadline: 5min idle, CPU {cpu}m, HLO module count unchanged at {current_hlo}")
            run_cmd(f"yes | xpk workload delete --workload={workload_name} --cluster={cluster_name} --project={cluster_project} --zone={cluster_zone}")
            break
        last_hlo_count = current_hlo

print("Loop finished, fetching final status")
