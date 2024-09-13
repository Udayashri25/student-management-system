from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from backend.agent import agent
from backend.recommender import RecommendationSystem
from backend.logging import Logger
from backend.supervisor import ConversationSupervisor

app=FastAPI()

@app.get("/")
async def read_root():
    return{"message":"Hello"}

agent=agent(model_name="mistralai/Mistral-7B-v0.1")
recommender=RecommendationSystem()
logger=Logger()
supervisor=ConversationSupervisor()

class QueryModel(BaseModel):
    query:str

@app.post("/ask")
async def ask_agent(query:QueryModel):
    try:
        context="you are a student assistant that provides information about books and answers related queries"
        response=agent.ask_question(query.query,context)
        supervisor.add_interaction(query.query,response)
        logger.log_interaction(query.query,response)
        return{"response":response}
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))
@app.post("/recommend")
async def recommend_books(query:QueryModel):
    try:
        recommendation=recommender.recommend(query.query)
        return{"recommendation":recommendation}
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))
@app.post("/followup")
async def followup_agent(query:QueryModel):
    try:
        history=supervisor.get_context()
        response=agent.follow_up_questions(query.query,history)
        supervisor.add_interaction(query.query,response)
        logger.log_interaction(query.query,response)
        return {"response":response}
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))
    

        