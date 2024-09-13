import datetime
import os
class Logger:
    def __init__(self,log_file="data/logs/user_logs.txt"):
     self.log_file=log_file
     os.makedirs(os.path.dirname(self.log_file),exist_ok=True)
    def log_interaction(self,user_query:str,llm_response:str):
        with open(self.log_file,'a') as log_f:
            log_f.write(f"{datetime.datetime.now()} - User: {user_query},Response:{llm_response}\n")
            