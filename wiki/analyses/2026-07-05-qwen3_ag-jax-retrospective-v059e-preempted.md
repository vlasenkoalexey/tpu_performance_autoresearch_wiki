# Retrospective: v059e

## Context
After successfully fixing the `_attn_splash` transpose bug in `v059d`, we launched `v059e` to run the workload with the correct `--tp_parallelism 2` configuration on the `alekseyv-tpu-v6e8-spot-xpk` cluster.

## Analysis
The `v059e` experiment failed after hitting the 60-minute ceiling without the worker pod ever appearing on the cluster. The subagent log reports:
`hang_evidence: "hard 60m ceiling reached; worker pod never appeared (likely stuck in Kueue admission or unschedulable)"`

Given that the cluster has 16 nodes and no active workloads or pending jobs (confirmed by `kubectl get jobset` and `kubectl get clusterqueues`), this strongly indicates that the spot instances underlying the node pool have been preempted by GCP or the cluster is temporarily unable to provision the required resources due to spot unavailability. The `alekseyv-tpu-v6e8-spot-xpk` cluster is evidently fully saturated/preempted despite appearing active in GKE.

## Resolution
We scanned available clusters via `gcloud container clusters list` and identified `jialeic-tpu-v6e8-spot-xpk` as an alternative cluster that is online, has no Kueue backlog, and has `tpu-v6e-slice` nodes available in a `2x4` (v6e-8) topology.
I will launch a new experimental variant (`v059f`) that is structurally identical to `v059e`, but targetting this new cluster.
