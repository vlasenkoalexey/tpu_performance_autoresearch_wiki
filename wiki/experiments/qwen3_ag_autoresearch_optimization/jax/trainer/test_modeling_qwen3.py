import sys
sys.path.insert(0, '/mnt/disks/persist/torch-tpu/tpu_performance_autoresearch_wiki_ag_demo/wiki/experiments/qwen3_ag_autoresearch_optimization/jax/.repo/2026-06-27-v016-fused-glu-bwd/trainer')
from model.modeling_qwen3 import set_splash_mesh, Qwen3MLP
from transformers import Qwen3Config
config = Qwen3Config()
print("Success!")
