#!/usr/bin/env bash
# GKE TPU cluster inventory probe. For each cluster in each specified project:
# status, XPK presence, TPU Ready/total node count, our recent jane-* workload
# count, XPK type per slice, raw topology, machine type.
#
# Refactored from .env/probe-cluster-inventory.sh — adds CLI flags for filtering
# to specific projects. The per-cluster scanning logic is unchanged from the
# battle-tested version (timeouts on every gcloud + kubectl call, error states
# classified as cred-fail / timeout / -, etc.).
#
# Usage:
#   scan-gke-clusters.sh --project <p> [--project <p> ...]
#   scan-gke-clusters.sh --help
#
# At least one --project is required (explicit > implicit). The skill
# /scan-gke-clusters orchestrates per-project invocations + merging.
#
# Timeouts (CRITICAL: dead clusters' kube-apiservers hang forever otherwise):
#   - gcloud get-credentials wrapped in `timeout 15s`
#   - every kubectl call uses `--request-timeout=5s`
#   - whole-cluster probe wrapped in `timeout 30s` as backstop
#   - node-pools list wrapped in `timeout 10s`
#   - cluster list wrapped in `timeout 30s`
#
# Output TSV (13 columns):
#   project  cluster  location  status  xpk  tpu_ready  tpu_total  our_uses  xpk_type  topology  machine_type  gcsfuse  spot
#
#   xpk          : Y = jobset CRD + Kueue clusterqueue both present
#                  js-only = jobset CRD only (XPK won't work without setup)
#                  N = neither
#                  cred-fail / timeout / -   = error states
#   tpu_ready    : count of nodes with cloud.google.com/gke-tpu-accelerator label AND Ready=True
#   tpu_total   : count of nodes with that label
#   our_uses     : count of JobSets whose name contains "jane-" (diagnostic only)
#   xpk_type     : ";"-joined XPK accelerator types per pool, e.g. "v5p-512;v5p-256".
#                  Derivation: v5p chip count = product(placement axes), XPK-N where N = 2× chips
#                  (v5p has 2 TCs/chip). v6e/v5e/v4/v7x chip count = product(axes), XPK-N = chips
#                  (1 TC/chip). "?" if topology or machine type unknown.
#   topology     : ";"-joined "<placement>:<node_count>" pairs across all TPU pools
#                  (e.g. "4x4x16:64;4x4x8:32"). "-" if no TPU pool.
#   machine_type : ";"-joined unique machineType values across TPU pools, e.g. "ct5p-hightpu-4t".
#                  Used to derive the TPU type family (ct5p/ct6e/ct5e/ct4p/ct7x → v5p/v6e/v5e/v4/v7x).
#   gcsfuse      : Y = GCS Fuse CSI driver addon enabled on the cluster
#                  N = disabled / absent. (cluster-level addon; +1 `gcloud clusters describe`.
#                  NOTE: "addon enabled" != "gcsfuse usable for a given workload" — true usability
#                  also depends on the workload volume spec + node SA bucket perms, not probed here.)
#                  "-" for non-RUNNING / unprobeable clusters.
#   spot         : Y = at least one TPU node pool is a Spot pool (config.spot=True)
#                  N = no TPU pool is Spot. "-" for non-RUNNING / unprobeable clusters.
#                  Free: folded into the node-pools list already queried for topology.
set -uo pipefail

# CLI parsing
PROJECTS=()
while [ $# -gt 0 ]; do
  case "$1" in
    --project)
      [ -z "${2-}" ] && { echo "ERROR: --project requires a value" >&2; exit 2; }
      PROJECTS+=("$2")
      shift 2
      ;;
    --help|-h)
      sed -n '2,/^set/p' "$0" | grep -E '^#( |$)' | sed 's/^# \?//'
      exit 0
      ;;
    *)
      echo "ERROR: unknown flag: $1" >&2
      echo "Run with --help for usage." >&2
      exit 2
      ;;
  esac
done

if [ ${#PROJECTS[@]} -eq 0 ]; then
  echo "ERROR: at least one --project is required" >&2
  echo "Run with --help for usage." >&2
  exit 2
fi

KT="kubectl --request-timeout=5s"
echo -e "project\tcluster\tlocation\tstatus\txpk\ttpu_ready\ttpu_total\tour_uses\txpk_type\ttopology\tmachine_type\tgcsfuse\tspot"

for proj in "${PROJECTS[@]}"; do
  while IFS=$'\t' read -r name loc status; do
    [ -z "$name" ] && continue
    if [ "$status" != "RUNNING" ]; then
      echo -e "$proj\t$name\t$loc\t$status\t-\t-\t-\t-\t-\t-\t-\t-\t-"
      continue
    fi
    line=$(timeout 30s bash -c '
      proj="$1"; name="$2"; loc="$3"; status="$4"
      timeout 15s gcloud container clusters get-credentials "$name" --location="$loc" --project="$proj" >/dev/null 2>&1 || {
        printf "%s\t%s\t%s\t%s\tcred-fail\t-\t-\t-\t-\t-\t-\t-\t-\n" "$proj" "$name" "$loc" "$status"; exit 0; }
      ctx="gke_${proj}_${loc}_${name}"
      KT="kubectl --request-timeout=5s --context=$ctx"
      has_cq=$($KT get clusterqueue --no-headers 2>/dev/null | wc -l)
      has_js=$($KT get crd jobsets.jobset.x-k8s.io --no-headers 2>/dev/null | wc -l)
      if [ "$has_cq" -gt 0 ] && [ "$has_js" -gt 0 ]; then xpk="Y"
      elif [ "$has_js" -gt 0 ]; then xpk="js-only"
      else xpk="N"; fi
      tpu_ready=$($KT get nodes -l cloud.google.com/gke-tpu-accelerator -o jsonpath='"'"'{range .items[*]}{.status.conditions[?(@.type=="Ready")].status}{"\n"}{end}'"'"' 2>/dev/null | grep -c "^True$" || true)
      tpu_total=$($KT get nodes -l cloud.google.com/gke-tpu-accelerator --no-headers 2>/dev/null | wc -l)
      our_uses=$($KT get jobsets -A --no-headers 2>/dev/null | awk "/jane-/" | wc -l)
      # Capture all node pools (including 1-host pools with empty topology), then keep only TPU ones
      # by filtering on machineType prefix (ct5p / ct6e / ct5lp / ct4p / tpu7x).
      pools=$(timeout 10s gcloud container node-pools list --cluster="$name" --location="$loc" --project="$proj" --format="value(placementPolicy.tpuTopology,initialNodeCount,config.machineType,config.spot)" 2>/dev/null | awk -F"\t" '"'"'$3 ~ /^(ct5p|ct6e|ct5e|ct5lp|ct4p|tpu7x)-/ {print}'"'"')
      topology=$(echo "$pools" | awk -F"\t" '"'"'NF>=2 {t=($1==""?"1-host":$1); print t":"$2}'"'"' | paste -sd";" -)
      machine_type=$(echo "$pools" | awk -F"\t" '"'"'{print $3}'"'"' | sort -u | grep -v "^$" | paste -sd";" -)
      xpk_type=$(echo "$pools" | awk -F"\t" '"'"'
        function product(s,    n, a, p, i) {
          if (s == "") return 1   # 1-host pool = 1 chip on accel ct5p; chips/host fixed per family below
          n = split(s, a, "x"); p = 1; for (i=1; i<=n; i++) p *= a[i]; return p
        }
        NF>=3 {
          chips = product($1); mt = $3
          # chips/host: 4 for ct5p-hightpu-4t / ct6e-standard-4t / ct4p-hightpu-4t / tpu7x-standard-4t
          # 1 for ct5lp-hightpu-1t. 1-host pools: chips = initialNodeCount × chips_per_host
          # TC ratios (sourced from wiki/concepts/tpu-hardware-generations.md):
          #   v4, v5p: 2 TCs/chip   v5e, v6e: 1 TC/chip   v7x: 2 TCs/chip (2 chiplets × 1 TC each)
          if (mt ~ /^ct5p-hightpu-4t/) { fam = "v5p"; tc = 2; cph = 4 }
          else if (mt ~ /^ct6e-standard-4t/) { fam = "v6e"; tc = 1; cph = 4 }
          else if (mt ~ /^ct6e-standard-1t/) { fam = "v6e"; tc = 1; cph = 1 }
          else if (mt ~ /^ct6e-standard-8t/) { fam = "v6e"; tc = 1; cph = 8 }
          else if (mt ~ /^ct5lp-hightpu-1t/) { fam = "v5e"; tc = 1; cph = 1 }
          else if (mt ~ /^ct5lp-hightpu-4t/) { fam = "v5e"; tc = 1; cph = 4 }
          else if (mt ~ /^ct5lp-hightpu-8t/) { fam = "v5e"; tc = 1; cph = 8 }
          else if (mt ~ /^ct5(e|lp)-/) { fam = "v5e"; tc = 1; cph = 4 }
          else if (mt ~ /^ct4p-hightpu-4t/) { fam = "v4"; tc = 2; cph = 4 }
          else if (mt ~ /^tpu7x-standard-4t/) { fam = "v7x"; tc = 2; cph = 4 }
          else { print "?"; next }
          if ($1 == "") chips = $2 * cph   # 1-host pool: chips = nodes × chips/host
          print fam "-" (chips * tc)
        }'"'"' | paste -sd";" -)
      [ -z "$topology" ] && topology="-"
      [ -z "$machine_type" ] && machine_type="-"
      [ -z "$xpk_type" ] && xpk_type="-"
      # spot: Y if any TPU pool is a Spot pool (config.spot column 4 == "True"). "-" if no TPU pool.
      if [ -n "$pools" ]; then
        spot=$(echo "$pools" | awk -F"\t" '"'"'$4=="True"{f=1} END{print (f?"Y":"N")}'"'"')
      else
        spot="-"
      fi
      # gcsfuse: cluster-level GCS Fuse CSI driver addon (one extra describe call).
      gcsfuse_raw=$(timeout 10s gcloud container clusters describe "$name" --location="$loc" --project="$proj" --format="value(addonsConfig.gcsFuseCsiDriverConfig.enabled)" 2>/dev/null)
      [ "$gcsfuse_raw" = "True" ] && gcsfuse="Y" || gcsfuse="N"
      printf "%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n" "$proj" "$name" "$loc" "$status" "$xpk" "$tpu_ready" "$tpu_total" "$our_uses" "$xpk_type" "$topology" "$machine_type" "$gcsfuse" "$spot"
    ' _ "$proj" "$name" "$loc" "$status" 2>/dev/null)
    if [ -z "$line" ]; then
      echo -e "$proj\t$name\t$loc\t$status\ttimeout\t-\t-\t-\t-\t-\t-\t-\t-"
    else
      echo "$line"
    fi
  done < <(timeout 30s gcloud container clusters list --project="$proj" --format='value(name,location,status)' 2>/dev/null)
done
