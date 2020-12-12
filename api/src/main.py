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
    print(lines[22].decode("UTF-8").split("*"))
    for line in lines:
        prepared_line = line.decode("UTF-8").split("*")
        crud.create_alert(
            db,
            AlertCreate(
                fileName=file.filename,
                timestamp=prepared_line[0],
                version=prepared_line[1],
                messageId=prepared_line[2],
                KPIValue=prepared_line[3],
                KPIThreshold=prepared_line[4],
                serverId=prepared_line[5],
                # =prepared_line[6],
                # =prepared_line[7],
                requestorId=prepared_line[8],
                userId=prepared_line[9],
                workPool=prepared_line[10],
                ruleApplicationNameVersion=prepared_line[11],
                encodedRuleset=prepared_line[12],
                checkoutEnabled=prepared_line[13],
                interactionNumber=prepared_line[14],
                correlationId=prepared_line[15],
                sequence=prepared_line[16],
                thread=prepared_line[17],
                pegaThreadName=prepared_line[18],
                logger=prepared_line[19],
                stack=prepared_line[20],
                lastInput=prepared_line[21],
                firstActivity=prepared_line[22],
                lastStep=prepared_line[23],
                # =prepared_line[24],
                # =prepared_line[25],
                # =prepared_line[26],
                # =prepared_line[27],
                traceList=prepared_line[28],
                PALData=prepared_line[29],
                primaryPageClass=prepared_line[30],
                primaryPageName=prepared_line[31],
                stepPageClass=prepared_line[32],
                stepPageName=prepared_line[33],
                pegaStack=prepared_line[34],
                parameterPage=prepared_line[35],
                line=prepared_line[36],
            ),
        )

    return {"filename": file.filename, "count": len(lines)}
