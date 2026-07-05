import json
import re

with open('parsed_experiments.json', 'r') as f:
    experiments = json.load(f)

# Add v020-splash-attn-only
experiments.append({
    'v-ID': 'v020',
    'date': '2026-07-03',
    'variant': '8B/v6e-8',
    'tags': ['splash-attention', 'torch.compile', 'scan', 'activation-checkpointing'],
    'verdict': 'supported',
    'mfu': '32.3% MFU',
    'slug': '2026-07-03-qwen3-jax-v020-splash-attn-only.md'
})

topics = {
    'pallas-kernels': re.compile(r'pallas|kernel|tokamax|mosaic|tpu-recipes|fused-rope|fused-rmsnorm|fused-qkv|splash-kernel|custom-call|hand-rolled|fused-glu'),
    'splash-attention': re.compile(r'splash|sa-block|sa_use|bkv|bq|sliding-window|nsa'),
    'op-fusion': re.compile(r'fusion|fuse-|coalesc|kernel-merge|epilogue|prologue|loop-fusion|input-fusion|output-fusion|convolution-fusion|elementwise-fusion|fused-qknorm'),
    'data-transformation': re.compile(r'moveaxis|transpose|layout|reshape|spmd-copy|data-format|data_formatting|bitcast|copy-elimination|layout-canonicaliz|permute|view'),
    'sharding-strategy': re.compile(r'shard|sharding|gspmd|shardy|partir|mesh|named-sharding|partial-replication|p-spec'),
    'fsdp-collective': re.compile(r'fsdp|all-gather|reduce-scatter|all-reduce|overlap|bucketing|async-collective|collective-matmul|host-offload|sparsecore-offload|sc-offload|collective|sc-bs'),
    'tensor-parallelism': re.compile(r'tp|tensor-parallel|tensor-paralle|sequence-parallel|vocab-parallel'),
    'moe': re.compile(r'moe|expert|dispatch|combine|gate|router|top-k|ragged-dot|segment-matmul'),
    'gate-up-fusion': re.compile(r'gate-up|gate_up|up-gate|fused-gate|weight-fused|fused-weight'),
    'compile-scan': re.compile(r'scan|compile|torch-compile|torch\.compile|graph-trainer|aot|graph-break|dynamo|fullgraph|chunked-xla|xla-sdpa|xla-bs'),
    'activation-checkpointing': re.compile(r'ac|checkpoint|remat|rematerialization|selective|ptd-checkpoint|memory-budget|ckpt|block-remat'),
    'vmem-scratch': re.compile(r'vmem|scoped-vmem|scratch|smem|tile-size|block-size|vmem-budget'),
    'dim-alignment-dtype': re.compile(r'bf16|fp8|fp16|dtype|precision|mxu-align|mixed-precision|reduce-dtype|param-dtype'),
    'batch-seq-amortization': re.compile(r'lbs|batch|seq-len|seq_len|seq8k|seq4k|amortization|gradient-accumulation|microbatch|lbs8|lbs16|bs2|bs4|bs8|bs16|bs24|bs32|bs64|seq1024|seq2048|seq16k'),
    'hbm-io': re.compile(r'hbm|oom|memory-pressure|defrag|peak-memory|cpu-offload|host-offload|spill|persistent-cache'),
    'libtpu-xla-flags': re.compile(r'libtpu|xla-flag|libtpu_init|enhanced-launch|barrier|collective-matmul|spmd-threshold|vmem-limit|tpu_use_|tpu_enable_'),
    'topology-hw': re.compile(r'topology|v5p|v6e|v7x|multi-slice|single-slice|num-slices|cross-gen|cross-arch|chip-count'),
    'profile-attribution': re.compile(r'xprof|profile-drilldown|op-profile|bucket-attribution|roofline|measurement'),
    'checkpointing': re.compile(r'orbax|checkpoint-save|checkpoint-load|async-save|persistence'),
    'ring-attention': re.compile(r'ring-attn|ring-attention'),
    'baseline': re.compile(r'baseline')
}

categorized = {}
for t in topics:
    categorized[t] = []
categorized['uncategorized'] = []

for exp in experiments:
    matched = False
    
    # Check tags first
    for tag in exp['tags']:
        for topic_name, pattern in topics.items():
            if tag == topic_name or pattern.search(tag):
                categorized[topic_name].append(exp)
                matched = True
                break
        if matched: break
    
    if matched: continue
    
    # Check slug
    for topic_name, pattern in topics.items():
        if pattern.search(exp['slug']):
            categorized[topic_name].append(exp)
            matched = True
            break
            
    if not matched:
        categorized['uncategorized'].append(exp)

print("Topic breakdown:")
for k, v in categorized.items():
    if len(v) > 0:
        print(f"{k}: {len(v)} experiments")
        for e in v:
            print(f"  {e['v-ID']} {e['verdict']} {e['mfu']} {e['slug']}")

