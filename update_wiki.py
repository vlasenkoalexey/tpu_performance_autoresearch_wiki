import re

with open('/mnt/disks/persist/torch-tpu/tpu_performance_autoresearch_wiki_ag_demo/wiki/index.md', 'r') as f:
    content = f.read()

# Update page count
content = re.sub(r'4 analyses', '5 analyses', content)
content = re.sub(r'193 pages', '194 pages', content)
content = re.sub(r'## Analyses \(5 \+\)', '## Analyses (6 +)', content)

# Add new analysis link
new_analysis = "- [2026-07-03 qwen3_ag-jax retrospective](analyses/2026-07-03-qwen3_ag-jax-retrospective.md) — FULL lane retrospective: 70+ experiments evaluated. Frontier shifted to Splash Attention + nnx.scan/remat (v020 at 32.3% MFU), stepping away from custom Pallas kernels due to instability.\n"

content = content.replace("## Analyses (6 +)\n", "## Analyses (6 +)\n" + new_analysis)

with open('/mnt/disks/persist/torch-tpu/tpu_performance_autoresearch_wiki_ag_demo/wiki/index.md', 'w') as f:
    f.write(content)

with open('/mnt/disks/persist/torch-tpu/tpu_performance_autoresearch_wiki_ag_demo/wiki/log.md', 'r') as f:
    log_content = f.read()

new_log = """
## [2026-07-03] analyze | qwen3_ag-jax retrospective

**Op**: analyze
**Pages created**: wiki/analyses/2026-07-03-qwen3_ag-jax-retrospective.md
**Key result**: Consolidating 70+ experiments for qwen3_ag/jax. `v020-splash-attn-only` executed recently yielding 32.3% MFU via nnx.scan+remat, disabling custom Pallas kernels.
**Notes**: Recommended focusing on Splash Attention and scanning layers.
"""

log_content = log_content.replace("# Log\n", "# Log\n" + new_log)

with open('/mnt/disks/persist/torch-tpu/tpu_performance_autoresearch_wiki_ag_demo/wiki/log.md', 'w') as f:
    f.write(log_content)
