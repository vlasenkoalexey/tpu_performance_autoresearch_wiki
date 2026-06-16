/create-experiment for qwen3 model, name folder qwen3_cc_autoresearch_optimization. Bootstrap torchax and jax lanes. Start with torchax lane and add a simple trainer similar to what llama3 is using 

Add abiltiy to collect profiles using jax profiler and dump them to GCS so they can be accessed and analyzed by xprof-mcp, profiler dir should be specified by command line flag.

You can save profiles to gcs://tpu-pytorch-alekseyv-us-central2/autoresearch/qwen3_cc bucket.

Use py312 conda env, assume that you are running on v6e4, test that you can train this model for few steps and collect profile.

Confirm that xprof-mcp is running and you can load and analyze this profile.

check if JAX_COMPILATION_CACHE_DIR should be on gcs

list available v6e8 clusters, check how many v6e8 clusters are there, and what clusters are free 

copy dockerfile from llama3 torchax experiment, adapt what's needed 

run single experiment on v6e8 to establish baseline collect profiles, hlo and measure mfu > 19.2% 

check gke-cluster-runner agent for running on gke

submit and push changes

write eqvivalence test for torchax model compared to HF model when running on CPU for forward and backward pass if possible

commit and push changes

now convert model to jax/flax in jax experiment lane -> done in one shot

can you run model on gke to establish mfu baseline and collect profiles, you can reuse same image as for torchax most likely > 20.5% MFU

 /start-experiment for Qwen3-8B, native-JAX/Flax NNX, on v6e-8, you can use up to 4 clusters in parallel, enable stop hook to prevent experiment from auto-stopping