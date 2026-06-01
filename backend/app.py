from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.compatibility import (
    router as compatibility_router
)

app = FastAPI(
    title="AI Astrology Services"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    compatibility_router
)


@app.get("/")
def home():

    return {
        "message": "AI Astrology Services Running"
    }