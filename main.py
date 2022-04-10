from typing import Dict
from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware

from routes.router import router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root() -> Dict:
    return {
        "message": "Simple Manga API. Check /docs for API endpoints."
    }

app.include_router(router)