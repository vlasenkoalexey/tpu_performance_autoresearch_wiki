import os
import glob
import re
import yaml
import json

exp_dir = '/mnt/disks/persist/torch-tpu/tpu_performance_autoresearch_wiki_ag_demo/wiki/experiments/qwen3_ag_autoresearch_optimization/jax/experiments'
files = glob.glob(os.path.join(exp_dir, '*.md'))

results = []
for f in files:
    with open(f, 'r') as f_obj:
        content = f_obj.read()
    
    # parse frontmatter
    fm_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    fm = {}
    if fm_match:
        try:
            fm = yaml.safe_load(fm_match.group(1)) or {}
        except Exception:
            pass
            
    v_id_match = re.search(r'-(v\d+[a-z]*|v6e8-baseline|v000-repro)-', os.path.basename(f))
    v_id = v_id_match.group(1) if v_id_match else os.path.basename(f)
    
    # Try to extract metric
    metric_match = re.search(r'## Results.*?([0-9.]+% MFU)', content, re.DOTALL)
    mfu = metric_match.group(1) if metric_match else ""
    
    results.append({
        'v-ID': v_id,
        'date': fm.get('updated', fm.get('created', '')),
        'variant': fm.get('variant', '8B/v6e-8'),
        'tags': fm.get('tags', []),
        'verdict': fm.get('verdict', 'in_progress'),
        'mfu': mfu,
        'slug': os.path.basename(f)
    })

print(json.dumps(results, default=str))
