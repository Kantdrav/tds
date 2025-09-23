from typing import Optional
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, PlainTextResponse, JSONResponse

import bs4 as bs
import requests
from bs4 import BeautifulSoup

import uvicorn

app = FastAPI()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for simplicity
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

@app.get("/", response_class=PlainTextResponse)
async def get_headings(country: Optional[str] = None):
    if not country:
        return {"error": "Please provide a country name in the query parameter 'country'."}
    
    url = f"https://en.wikipedia.org/wiki/{country.capitalize()}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    headings = []
    for tag in soup.find_all([f'h{i}' for i in range(1, 7)]):
        tag_name = getattr(tag, 'name', None)
        if tag_name and tag_name.startswith('h') and tag_name[1:].isdigit():
            level = int(tag_name[1:])
            prefix = '#' * level
            headings.append(f"{prefix} {tag.get_text(strip=True)}")
    return "\n".join(headings)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
