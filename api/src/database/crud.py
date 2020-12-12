from sqlalchemy.orm import Session

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
