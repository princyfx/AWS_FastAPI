from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import gunicorn 
import uvicorn
from qna import nlp_qna 
from typing import Dict, Any

from pydantic import BaseModel

app = FastAPI()

from fastapi import FastAPI
from pydantic import BaseModel

# Assuming you have already defined the nlp_qna function and nlp model

class QARequest(BaseModel):
    context: str
    question: str

class QAResponse(BaseModel):
    response: str

# Endpoint to handle POST requests to /qna
@app.post("/qna/")
async def qna(qa_request: Dict[Any,Any]):
    print(qa_request)
    """context = qa_request.context
    question = qa_request.question"""
    # Call the nlp_qna function with both context and question arguments
    result = nlp_qna(qa_request["context"], qa_request["question"])
    return result 