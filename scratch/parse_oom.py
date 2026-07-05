import re
from collections import defaultdict

with open('oom.txt', 'r') as f:
    text = f.read()

# Find all shapes like bf16[36,1024,6144] or f32[...
shapes = re.findall(r'(?:f32|bf16|f16|s32)\[([^\]]+)\]', text)

counts = defaultdict(int)
for s in shapes:
    counts[s] += 1

# Extract sizes and sort
def get_size(s):
    try:
        parts = s.split(',')
        elems = 1
        for p in parts:
            if p:
                elems *= int(p)
        return elems * 2 # Just assume 2 bytes
    except:
        return 0

sizes = []
for s, count in counts.items():
    sizes.append((s, count, get_size(s)))

sizes.sort(key=lambda x: x[2], reverse=True)

print("Top 20 largest tensor shapes:")
for s, count, size in sizes[:20]:
    print(f"Size: {size / (1024**3):.2f} GB | Count: {count} | Shape: {s}")
