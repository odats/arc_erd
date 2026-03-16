# arc_erd
Code accompanying the paper “On the Geometry of Analogical Reasoning in Latent Space” (ICLR 2026 GRaM Workshop).

run
pip install matplotlib numpy pandas wandb x-transformers nbconvert ipykernel datasets tqdm

jupyter nbconvert --to script arc_erd.ipynb 
torchrun --standalone --nproc_per_node=gpu arc_erd.py

wandb
training: https://wandb.ai/oleg-dats/erd_iclr_train
ttt: https://wandb.ai/oleg-dats/erd_iclr_ttt/
