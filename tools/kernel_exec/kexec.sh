#!/usr/bin/env bash
# kexec — the kernel lane's single execution indirection.
#
# Every device-touching command in the kernel loop (kgate measure / verify / fit / flags)
# goes through `kexec run`. It executes either:
#   local   — flock'd, chip-pinned, on this workstation                      (default)
#
# CHIP PINNING SETS BOTH TPU_VISIBLE_CHIPS AND TPU_VISIBLE_DEVICES. TPU_VISIBLE_CHIPS is the
# real control (torch_tpu copies it verbatim; libtpu turns it into --deepsea_hal_included_devs).
# TPU_VISIBLE_DEVICES ALONE DOES NOT ISOLATE on >1-core-per-chip parts: measured on v7x
# (2 cores/chip), TPU_VISIBLE_DEVICES=0 still exposed all 8 devices, while TPU_VISIBLE_CHIPS=0
# correctly yielded 2. On v6e (1 core/chip) the two coincide, which is why this hid for so long.
# torch_tpu additionally requires both to AGREE under the RANK/WORLD_SIZE bootstrap
# (vllm_torchtpu/worker/tpu_worker.py), so we set both.
#   cluster — kubectl exec into a persistent GKE pod holding real chips
#
# Callers are identical in both modes, so kgate, /author-kernel and kernel-verifier need
# no changes. This is the file `wiki/kernel_experiments/program.md` refers to as the
# "local exec path" (it previously pointed at tools/agy_loop/exec_chip.sh, which never existed).
#
# ARTIFACTS ARE ALWAYS gs:// IN CLUSTER MODE — enforced, not advisory. All four artifact
# classes write straight to GCS (validated 2026-08-19, see
# wiki/observations/tpu-dump-flags-write-directly-to-gcs.md), so the pod is stateless:
# no scratch volume, no kubectl cp, and no ephemeral-storage eviction (the failure that
# destroyed two full-model captures).
#
# Usage:
#   kexec.sh discover                            # what TPU capacity does this cluster have?
#   kexec.sh up      --family <slug> --accelerator <A> --topology <T> [--chips N] [--hours H] [--service-account KSA] --image <IMG>
#   kexec.sh run     --family <slug> [--chip N] -- <command...>
#   kexec.sh sync    --family <slug>            # push .repo worktree into the pod
#   kexec.sh status  --family <slug>
#   kexec.sh down    --family <slug>
set -euo pipefail

# repo root = tools/kernel_exec/../..  (this file lives at <root>/tools/kernel_exec/kexec.sh)
WIKI_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
NS="${KEXEC_NAMESPACE:-default}"
DEFAULT_IMAGE="${KEXEC_IMAGE:-}"

die() { echo "kexec: $*" >&2; exit 1; }
# NOTHING about a TPU generation is hardcoded. Accelerator + topology are discovered from
# the cluster (`kexec discover`) and passed explicitly; the GKE label VALUE differs per
# generation (tpu7x, tpu-v6e-slice, tpu-v5p-slice, tpu-v5-lite-podslice, ...), so guessing
# a default silently pins one generation. Chips-per-node likewise varies by machine type.
FAMILY=""; CHIPS=""; HOURS=8; CHIP=0; IMAGE="$DEFAULT_IMAGE"; ACCEL=""; TOPO=""
# Workload-Identity KSA for the pod. Node oauth scopes can cap the node SA below gs://
# write (torchtpu-v7x-80 nodes are devstorage.read_only), which breaks the gs://-artifact
# contract enforced below. A WI-annotated KSA bypasses node scopes; these pods never set
# hostNetwork, so WI resolves. Empty => cluster default SA.
SA="${KEXEC_SERVICE_ACCOUNT:-}"
# Extra pod labels, "k=v,k2=v2". Needed where TPU pods are Kueue-managed: the admission
# webhook stamps every TPU pod with a scheduling gate and routes it by
# kueue.x-k8s.io/queue-name. Landing in the wrong (contended) queue leaves the pod
# SchedulingGated forever with no Workload object to explain why.
POD_LABELS="${KEXEC_POD_LABELS:-}"
CMD="${1:-}"; shift || true
ARGS=()
while [[ $# -gt 0 ]]; do
  case "$1" in
    --family)      FAMILY="$2"; shift 2;;
    --chips)       CHIPS="$2";  shift 2;;
    --hours)       HOURS="$2";  shift 2;;
    --chip)        CHIP="$2";   shift 2;;
    --image)       IMAGE="$2";  shift 2;;
    --accelerator) ACCEL="$2";  shift 2;;
    --topology)    TOPO="$2";   shift 2;;
    --service-account) SA="$2"; shift 2;;
    --pod-labels)  POD_LABELS="$2"; shift 2;;
    --) shift; ARGS=("$@"); break;;
    *) die "unknown arg: $1";;
  esac
done
[[ "$CMD" == "discover" || -n "$FAMILY" ]] || die "--family <slug> is required"

# ---------------------------------------------------------------- discover
# Enumerate the TPU capacity actually present on the current cluster, any generation.
# This is what the process shows the user when asking local-vs-cluster.
if [[ "$CMD" == "discover" ]]; then
  CTX="$(kubectl config current-context)"
  echo "cluster: $CTX"
  printf '%-26s %-22s %-10s %-22s %-7s %s\n' NODEPOOL ACCELERATOR TOPOLOGY MACHINE-TYPE CHIPS STATUS
  kubectl get nodes -l cloud.google.com/gke-tpu-accelerator \
    -o jsonpath='{range .items[*]}{.metadata.labels.cloud\.google\.com/gke-nodepool}{"\t"}{.metadata.labels.cloud\.google\.com/gke-tpu-accelerator}{"\t"}{.metadata.labels.cloud\.google\.com/gke-tpu-topology}{"\t"}{.metadata.labels.node\.kubernetes\.io/instance-type}{"\t"}{.status.allocatable.google\.com/tpu}{"\t"}{.status.conditions[-1].type}{"\n"}{end}' 2>/dev/null \
    | sort -u | awk -F'\t' '{printf "%-26s %-22s %-10s %-22s %-7s %s\n",$1,$2,$3,$4,$5,$6}'
  echo
  echo "then: kexec.sh up --family <slug> --accelerator <ACCELERATOR> --topology <TOPOLOGY> [--chips N] --image <IMG>"
  exit 0
fi

FAMDIR="$WIKI_ROOT/wiki/kernel_experiments/$FAMILY/pallas"
[[ -d "$FAMDIR" ]] || die "no such family dir: $FAMDIR"
STATE="$FAMDIR/.exec-target"           # gitignored; the durable record of WHERE this family runs
POD="kexec-${FAMILY}"
POD="${POD:0:60}"

# ---------------------------------------------------------------- helpers
target()      { [[ -f "$STATE" ]] && grep -m1 '^target=' "$STATE" | cut -d= -f2 || echo local; }
state_get()   { [[ -f "$STATE" ]] && (grep -m1 "^$1=" "$STATE" | cut -d= -f2- || true); }
kctx()        { local c; c="$(state_get context)"; [[ -n "$c" ]] && echo "--context=$c" || echo ""; }

# Enforcement: in cluster mode every artifact destination must be a gs:// URI.
# A local path in the pod is invisible to the wiki and risks eviction; refuse early
# and loudly rather than losing the capture after a long run.
assert_gcs_artifacts() {
  local bad=()
  for var in XLA_FLAGS LIBTPU_INIT_ARGS; do
    local v="${!var:-}"
    [[ -z "$v" ]] && continue
    while read -r hit; do
      [[ -z "$hit" ]] && continue
      [[ "$hit" == gs://* ]] || bad+=("$var: $hit")
    done < <(grep -oE '\-\-xla_(dump_to|jf_dump_to|mosaic_dump_to)=[^ ]+' <<<"$v" | cut -d= -f2-)
  done
  # Flag-with-value forms (--flag=value)
  for a in "${ARGS[@]:-}"; do
    case "$a" in
      --trace-dir=*|--artifact-dir=*|--capture-dir=*)
        [[ "${a#*=}" == gs://* ]] || bad+=("$a");;
    esac
  done
  # Separated forms (--flag value) for the CAPTURE/DUMP flags only.
  #
  # DELIBERATELY NOT ENFORCED HERE: kgate's own `-o` / `--receipt`.
  # Enforcing gs:// on those was tried (2026-08-19) and was strictly WORSE than the problem it
  # was meant to fix. kgate writes JSON with a plain `open(path,"w")` (kernelgate/receipt.py:178,
  # report.py:14) and has NO gs:// support at all, so a gs:// receipt target does not error --
  # it silently produces NO FILE ANYWHERE while kgate still prints STATUS: PASS. Measured: a
  # v002 cand2 run reported 2.205x with its receipt written to neither the bucket nor the pod.
  # Before the enforcement, receipts at least existed on pod disk and could be pulled back.
  # The real gap is in kgate (needs gs:// write support) and is reported on the experiment page
  # rather than patched here -- tools/kernelgate is shared tooling this lane may not edit.
  # Until then the contract is: kgate receipts go to a POD-LOCAL path and the runner MUST pull
  # them back before teardown.
  local i n=${#ARGS[@]}
  for ((i=0; i<n; i++)); do
    case "${ARGS[i]}" in
      --trace-dir|--artifact-dir|--capture-dir)
        local v="${ARGS[i+1]:-}"
        [[ -n "$v" && "$v" != gs://* ]] && bad+=("${ARGS[i]} $v");;
    esac
  done
  if ((${#bad[@]})); then
    printf 'kexec: cluster mode requires gs:// artifact targets; got:\n' >&2
    printf '  %s\n' "${bad[@]}" >&2
    die "refusing to run (a pod-local dump is unrecoverable and can evict the pod)"
  fi
}

# ---------------------------------------------------------------- up
if [[ "$CMD" == "up" ]]; then
  [[ -n "$IMAGE" ]] || die "--image required (needs jax[tpu] + libtpu + kgate installed).
    Set KEXEC_IMAGE to avoid repeating it."
  [[ -n "$ACCEL" && -n "$TOPO" ]] || die "--accelerator and --topology are required.
    Run 'kexec.sh discover' to list what this cluster has; the label value is
    generation-specific (tpu7x / tpu-v6e-slice / tpu-v5p-slice / tpu-v5-lite-podslice / ...)."
  CTX="$(kubectl config current-context)"
  # Default chips to the node's actual allocatable count for the chosen pool, so we neither
  # under-request (stranding chips) nor over-request (unschedulable) on an unfamiliar generation.
  if [[ -z "$CHIPS" ]]; then
    CHIPS="$(kubectl get nodes -l "cloud.google.com/gke-tpu-accelerator=$ACCEL,cloud.google.com/gke-tpu-topology=$TOPO" \
      -o jsonpath='{.items[0].status.allocatable.google\.com/tpu}' 2>/dev/null)"
    [[ -n "$CHIPS" ]] || die "could not infer chips for $ACCEL/$TOPO — pass --chips N explicitly"
    echo "kexec: --chips not given; using the node's allocatable count for $ACCEL/$TOPO = $CHIPS"
  fi
  DEADLINE=$(( HOURS * 3600 ))
  echo "kexec: provisioning $POD ($CHIPS chips, $ACCEL/$TOPO, TTL ${HOURS}h) on $CTX"
  EXTRA_LABELS=""
  if [[ -n "$POD_LABELS" ]]; then
    IFS=',' read -ra _kv <<< "$POD_LABELS"
    for kv in "${_kv[@]}"; do
      EXTRA_LABELS+=$'\n'"    \"${kv%%=*}\": \"${kv#*=}\""
    done
  fi

  # activeDeadlineSeconds is the load-bearing safety property: `sleep infinity` never exits
  # on its own, so a leaked pod would hold scarce chips forever. The cluster kills it even
  # if every software teardown path fails.
  kubectl $([[ -n "$CTX" ]] && echo "--context=$CTX") -n "$NS" apply -f - <<YAML
apiVersion: v1
kind: Pod
metadata:
  name: $POD
  labels:
    app: kexec
    kexec-family: "$FAMILY"$EXTRA_LABELS
spec:
  restartPolicy: Never
${SA:+  serviceAccountName: $SA}
  activeDeadlineSeconds: $DEADLINE
  nodeSelector:
    cloud.google.com/gke-tpu-accelerator: $ACCEL
    cloud.google.com/gke-tpu-topology: $TOPO
  containers:
  - name: dev
    image: $IMAGE
    command: ["/bin/bash","-c","sleep infinity"]
    securityContext: { privileged: true }
    resources:
      limits: { google.com/tpu: "$CHIPS" }
    env:
    - { name: KEXEC_POD, value: "1" }
YAML

  cat > "$STATE" <<EOF
target=cluster
pod=$POD
namespace=$NS
context=$CTX
chips=$CHIPS
accelerator=$ACCEL
topology=$TOPO
image=$IMAGE
service_account=$SA
pod_labels=$POD_LABELS
deadline_hours=$HOURS
created=$(date -u +%Y-%m-%dT%H:%M:%SZ)
EOF
  echo "kexec: waiting for $POD to be Ready (TPU nodes can take a few minutes)..."
  kubectl --context="$CTX" -n "$NS" wait --for=condition=Ready "pod/$POD" --timeout=900s
  echo "kexec: UP. Teardown is MANDATORY at family close: kexec.sh down --family $FAMILY"
  echo "kexec: hard TTL ${HOURS}h — the cluster reaps it even if teardown is missed."
  exit 0
fi

# ---------------------------------------------------------------- status / down
if [[ "$CMD" == "status" ]]; then
  echo "family : $FAMILY"; echo "target : $(target)"
  [[ -f "$STATE" ]] && sed 's/^/  /' "$STATE"
  if [[ "$(target)" == cluster ]]; then
    kubectl $(kctx) -n "$NS" get pod "$POD" 2>/dev/null || echo "  POD MISSING (state file is stale — run 'up' or 'down')"
  fi
  exit 0
fi

if [[ "$CMD" == "down" ]]; then
  if [[ "$(target)" == cluster ]]; then
    echo "kexec: deleting $POD"
    # Wait for actual deletion: a --wait=false delete leaves the pod present long enough
    # that an immediate `up` hits "pod updates may not change fields other than image"
    # and silently keeps the OLD spec (observed 2026-08-19: a serviceAccountName change
    # was rejected this way and the run continued on the wrong identity).
    kubectl $(kctx) -n "$NS" delete pod "$POD" --ignore-not-found --wait=true --timeout=180s
  fi
  rm -f "$STATE"
  echo "kexec: DOWN (family $FAMILY reverts to local)"
  exit 0
fi

# ---------------------------------------------------------------- sync
# Kernels are single small files; the family's archive_remote may be `none` (no push path),
# so the worktree is copied in directly rather than cloned.
if [[ "$CMD" == "sync" ]]; then
  [[ "$(target)" == cluster ]] || { echo "kexec: local target — nothing to sync"; exit 0; }
  [[ -d "$FAMDIR/.repo" ]] || die "no worktree at $FAMDIR/.repo (K4 creates it)"
  echo "kexec: syncing .repo -> $POD:/work"
  kubectl $(kctx) -n "$NS" exec "$POD" -- mkdir -p /work
  tar -C "$FAMDIR/.repo" --exclude='.git' -cf - . \
    | kubectl $(kctx) -n "$NS" exec -i "$POD" -- tar -C /work -xf -
  echo "kexec: synced"
  exit 0
fi

# ---------------------------------------------------------------- run
if [[ "$CMD" == "run" ]]; then
  ((${#ARGS[@]})) || die "run needs a command after --"
  if [[ "$(target)" == cluster ]]; then
    assert_gcs_artifacts
    kubectl $(kctx) -n "$NS" get pod "$POD" >/dev/null 2>&1 \
      || die "pod $POD is gone (TTL expired or deleted). Run: kexec.sh up --family $FAMILY"
    # No flock: the pod's chips are exclusively ours by k8s admission — that guarantee is
    # exactly why a pod beats SSH into a shared TPU-VM.
    exec kubectl $(kctx) -n "$NS" exec -i "$POD" -- env \
      TPU_VISIBLE_CHIPS="$CHIP" TPU_VISIBLE_DEVICES="$CHIP" \
      XLA_FLAGS="${XLA_FLAGS:-}" \
      LIBTPU_INIT_ARGS="${LIBTPU_INIT_ARGS:-}" \
      bash -lc 'cd /work 2>/dev/null || true; "$@"' _ "${ARGS[@]}"
  else
    # Local: serial per chip via the per-chip flock; cross-chip overlap is allowed for
    # compile/parity but a TIMING window owns the whole host (program.md Discipline table).
    exec flock "/tmp/tpu-chip-${CHIP}.lock" env \
      TPU_VISIBLE_CHIPS="$CHIP" TPU_VISIBLE_DEVICES="$CHIP" "${ARGS[@]}"
  fi
fi

die "unknown command '${CMD:-}' (want: discover | up | run | sync | status | down)"
