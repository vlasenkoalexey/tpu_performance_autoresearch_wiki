import os

with open("model/modeling_qwen3.py", "r") as f:
    content = f.read()

# Restore remat logic using jax.checkpoint
new_content = content.replace('''    def __call__(self, hidden_states, position_embeddings, attention_mask=None):
        @nnx.scan(in_axes=(nnx.Carry, 0, None, None), out_axes=nnx.Carry)
        def forward(hs, layer, pos_emb, mask):
            return layer(hs, pos_emb, mask)
            
        return forward(hidden_states, self.layers, position_embeddings, attention_mask)''', '''    def __call__(self, hidden_states, position_embeddings, attention_mask=None):
        import os
        import jax
        use_remat = os.environ.get("JAX_REMAT", "0") == "1"
        
        def layer_fn(hs, layer, pos_emb, mask):
            return layer(hs, pos_emb, mask)
            
        if use_remat:
            layer_fn = jax.checkpoint(layer_fn, prevent_cse=False)
            
        @nnx.scan(in_axes=(nnx.Carry, 0, None, None), out_axes=nnx.Carry)
        def forward(hs, layer, pos_emb, mask):
            return layer_fn(hs, layer, pos_emb, mask)
            
        return forward(hidden_states, self.layers, position_embeddings, attention_mask)''')

with open("model/modeling_qwen3.py", "w") as f:
    f.write(new_content)

