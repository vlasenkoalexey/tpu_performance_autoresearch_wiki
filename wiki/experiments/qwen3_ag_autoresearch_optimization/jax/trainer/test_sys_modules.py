import sys
sys.path.insert(0, '/mnt/disks/persist/torch-tpu/tpu_performance_autoresearch_wiki_ag_demo/wiki/experiments/qwen3_ag_autoresearch_optimization/jax/.repo/2026-06-27-v016-fused-glu-bwd/trainer')

from model import modeling_qwen3 as mq
print("Imported:", mq.__file__)
print("Name:", mq.__name__)
print("Dir:", dir(mq))
