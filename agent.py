from transformers import pipeline,AutoModelForCausalLM,AutoTokenizer
class agent:
    def __init__(self,model_name="mistralai/Mistral-7B-v0.1",device="cpu"):
     self.model_name=model_name
     self.device=device

     self.tokenizer=AutoTokenizer.from_pretrained(model_name)
     self.model=AutoModelForCausalLM.from_pretrained(model_name)
     self.pipeline=pipeline("text-generation",model=self.model,tokenizer=self.tokenizer,device=0 if device=="cuda" else -1)
    
    def ask_question(self,query:str,context:str="")->str:
        full_query=f"{context}\n{query}"
        response=self.pipeline(full_query,max_length=200,num_return_sequences=1)
        return response[0]['generated_text']
    def follow_up_questions(self,query:str,previous_responses:list)->str:
        conversation_history="".join([f"user:{resp['user_query']}\nAgent:{resp['llm_response']}\n" for resp in previous_responses])
        full_query=f"{conversation_history}User:{query}\nAgent:"
        response=self.pipeline(full_query,max_length=200,num_return_sequences=1)
        return response[0]['generated_text']
    