from variables.variables import * 

class FinGPT():
    def __init__(self):
        print("[INFO] {:.2f}...initializing fingpt module".format(
            time.time()-start_time
        ))
        
        base_model = "NousResearch/Llama-2-13b-hf"
        peft_model = "FinGPT/fingpt-sentiment_llama2-13b_lora"
        
        self.tokenizer = LlamaTokenizerFast.from_pretrained(
            base_model#, trust_remote_code=True
        )  
        
        self.tokenizer.pad_token = self.tokenizer.eos_token 
        
        model = LlamaForCausalLM.from_pretrained(
            base_model, device_map="cuda:0",
            load_in_8bit=True, #trust_remote_code=True
        )
        
        model = PeftModel.from_pretrained(model, peft_model)
        self.model = model.eval()

        self.prompt = None 
        self.reponse_tag = None 
        
    def generate_prompt_result(self):
        tokens = self.tokenizer(
            self.prompt, return_tensors="pt", padding=True,
            max_length=512
        )
        
        del tokens["token_type_ids"] #BECAUSE OF MODEL
        
        res = self.model.generate(**tokens)#, max_length=512)#had **tokens
        
        res_sentences = [
            self.tokenizer.decode(i) for i in res
        ]
        
        self.prompt_result = [
            o.split(self.response_tag)[1] for o in res_sentences
        ]