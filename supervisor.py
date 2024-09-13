class ConversationSupervisor:
    def __init__(self):
        self.history=[]
    def add_interaction(self,user_query:str,llm_response:str):
        self.history.append({
            "user_query":user_query,
            "llm_response":llm_response
        })
    def get_context(self):
        return self.history
    