from typing import List

from sqlalchemy.orm import Session
from sqlalchemy import func

from . import models
from pega import schemas


def get_alerts(db: Session, limit: int):
    return db.query(models.PegaAlert).limit(limit).all()


def delete_all_alerts(db: Session):
    db.query(models.PegaAlert).delete()
    db.commit()


def create_alert(db: Session, alert: schemas.alert.AlertCreate):
    db_alert = models.PegaAlert(**alert.dict())
    db.add(db_alert)
    db.commit()
    db.refresh(db_alert)
    return db_alert


def create_alerts(db: Session, alerts: List[schemas.alert.AlertCreate]):
    for alert in alerts:
        db_alert = models.PegaAlert(**alert.dict())
        db.add(db_alert)
    db.commit()


def get_alerts_files(db: Session):
    return (
        db.query(models.PegaAlert.fileName, func.count(1))
        .group_by(models.PegaAlert.fileName)
        .all()
    )
