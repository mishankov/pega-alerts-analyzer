from typing import List

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from pega.models.alert import Alert


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def health_check():
    return {"status": "OK"}


@app.get("/alerts", response_model=List[Alert])
def get_alerts():
    return []
