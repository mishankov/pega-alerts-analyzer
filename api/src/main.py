from typing import List
import datetime

from fastapi import FastAPI, File, UploadFile, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from pega.schemas.alert import Alert, AlertCreate
from database import crud, models
from database.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/ping")
def health_check():
    return {"status": "OK", "server_time": datetime.datetime.now()}


@app.get("/alerts", response_model=List[Alert])
def get_alerts(db: Session = Depends(get_db)):
    alerts = crud.get_alerts(db, 100)
    return alerts


@app.delete("/alerts")
def purge_alerts(db: Session = Depends(get_db)):
    crud.delete_all_alerts(db)
    return "OK"


@app.post("/alerts/uploadfile")
def upload_alerts_file(file: UploadFile = File(...), db: Session = Depends(get_db)):
    lines = file.file.readlines()
    alerts = []
    for line in lines:
        decoded_line = line.decode("UTF-8")
        alerts.append(AlertCreate.from_alert_line(decoded_line, file.filename))

    crud.create_alerts(db, alerts)

    return {"filename": file.filename, "count": len(lines)}
