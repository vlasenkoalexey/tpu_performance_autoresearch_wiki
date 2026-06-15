import re

path = 'tokamax/_src/autotuning/cache.py'
with open(path, 'r') as f:
    text = f.read()

# Make _load_cache return {}
text = re.sub(r'def _load_cache.*?return out', r'def _load_cache(self, device_kind, cache_path=None):\n    return {}', text, flags=re.DOTALL)

with open(path, 'w') as f:
    f.write(text)

path_api = 'tokamax/_src/autotuning/api.py'
with open(path_api, 'r') as f:
    text_api = f.read()

# Make autotune pass through the original function!
new_api = """
import functools
import jax

def autotune(*args, **kwargs):
  def wrapper(f):
    return f
  return wrapper

"""
with open(path_api, 'w') as f:
    f.write(new_api)

print('Patched')
