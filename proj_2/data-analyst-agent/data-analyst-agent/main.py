from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import base64
import io
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/")
async def analyze(file: UploadFile = File(...)):
    # Read the uploaded file
    question = (await file.read()).decode("utf-8").strip()

    if "highest grossing films" in question.lower():
        from agents.film_agent import process_film_question
        return JSONResponse(content=process_film_question(question))
    
    elif "indian high court" in question.lower():
        from agents.judgment_agent import process_judgment_question
        return JSONResponse(content=process_judgment_question(question))
    
    else:
        return JSONResponse(content=["Unsupported question type."]*4)
