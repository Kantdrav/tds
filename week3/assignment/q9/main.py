from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
import json
import os

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Simulated TypeScript book content (you can replace this with a vector store or real data)
DOCUMENTS = [
    {
        "text": "The => syntax in TypeScript is affectionately called the fat arrow.",
        "source": "typescript-book/arrow-functions.md"
    },
    {
        "text": "The !! operator converts any value into an explicit boolean.",
        "source": "typescript-book/truthy-falsy.md"
    }
]

@app.get("/search")
async def search(q: Optional[str] = None):
    if not q:
        raise HTTPException(status_code=400, detail="Query parameter 'q' is required")

    q_lower = q.lower()
    for doc in DOCUMENTS:
        if all(keyword in doc["text"].lower() for keyword in q_lower.split()):
            return {
                "answer": doc["text"],
                "sources": doc["source"]
            }

    return {
        "answer": "No relevant information found.",
        "sources": ""
    }
