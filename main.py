import os
import torch
from torch import autocast
from diffusers import StableDiffusionPipeline

model_id = "CompVis/stable-diffusion-v1-4"
device = "cuda"

YOUR_TOKEN = os.environ["HUGGINGFACE_HUB_TOKEN"]

pipe = StableDiffusionPipeline.from_pretrained(model_id, use_auth_token=YOUR_TOKEN)
pipe = pipe.to(device)

prompt = "a photo of an astronaut riding a horse on mars"
with autocast("cuda"):
    image = pipe(prompt, guidance_scale=7.5)["sample"][0]

image.save("astronaut_rides_horse.png")
