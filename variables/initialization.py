import time 
start_time = time.time()

print("[INFO] {:.2f}...loading libraries".format(
    time.time()-start_time
))

import finnhub 

import os 
os.environ["TRANSFORMERS_CACHE"] = "sn850:/huggingface/cache/"
os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"] = "2"
os.environ["PYTORCH_CUDA_ALLOC_CONF"]   = "max_split_size_mb:200"

from transformers import LlamaTokenizerFast, LlamaForCausalLM
from peft import PeftModel 
import accelerate, bitsandbytes

import json 
import pandas as pd