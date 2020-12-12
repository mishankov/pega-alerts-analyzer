from typing import List
import datetime

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


@app.get("/ping")
def health_check():
    return {"status": "OK", "server_time": datetime.datetime.now()}


@app.get("/alerts", response_model=List[Alert])
def get_alerts():
    return [
        Alert(
            checkoutEnabled="Y",
            correlationId="aksjdklajfkl",
            KPIThreshold=300,
            KPIValue=301,
        ),
        Alert(
            checkoutEnabled="N", correlationId="ewer", KPIThreshold=500, KPIValue=1000
        ),
    ]


@app.post("/alerts/uploadfile")
def upload_alerts_file():
    return "OK"
