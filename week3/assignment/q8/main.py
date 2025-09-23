from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import numpy as np
import openai
import os

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["POST", "OPTIONS"],
    allow_headers=["*"],
)

class SimilarityRequest(BaseModel):
    docs: List[str]
    query: str

class SimilarityResponse(BaseModel):
    matches: List[str]

def get_embeddings(texts: List[str]) -> List[List[float]]:
    try:
        client = openai.OpenAI()  # uses OPENAI_API_KEY from env
        response = client.embeddings.create(
            input=texts,
            model="text-embedding-3-small"
        )
        return [item.embedding for item in response.data]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Embedding error: {str(e)}")

def cosine_similarity(a: np.ndarray, b: np.ndarray) -> float:
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

@app.post("/similarity", response_model=SimilarityResponse)
async def get_similar_docs(request: SimilarityRequest):
    if not request.docs or not request.query:
        raise HTTPException(status_code=400, detail="Both 'docs' and 'query' are required.")
    
    all_texts = request.docs + [request.query]
    embeddings = get_embeddings(all_texts)
    doc_embeddings = np.array(embeddings[:-1])
    query_embedding = np.array(embeddings[-1])

    similarities = [cosine_similarity(doc_emb, query_embedding) for doc_emb in doc_embeddings]
    ranked_indices = np.argsort(similarities)[::-1][:3]
    top_matches = [request.docs[i] for i in ranked_indices]

    return SimilarityResponse(matches=top_matches)
