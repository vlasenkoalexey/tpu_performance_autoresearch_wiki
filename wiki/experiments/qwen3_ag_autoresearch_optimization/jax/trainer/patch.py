with open("model/modeling_qwen3.py", "r") as f:
    text = f.read()

new_text = text.replace("""            from . import modeling_qwen3 as mq
            mesh = mq._SPLASH_MESH
            if mesh is None:
                raise RuntimeError("fused_glu needs a registered mesh. Call `set_splash_mesh(mesh)`.")
            
            mapped_glu = shard_map(
                fused_glu,
                mesh=mesh,""", """            mesh = _SPLASH_MESH
            if mesh is None:
                raise RuntimeError("fused_glu needs a registered mesh. Call `set_splash_mesh(mesh)`.")
            
            mapped_glu = shard_map(
                fused_glu,
                mesh=mesh,""")

with open("model/modeling_qwen3.py", "w") as f:
    f.write(new_text)
