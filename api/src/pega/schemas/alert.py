from typing import Optional

from pydantic import BaseModel, Field

from .common import YN


class AlertBase(BaseModel):
    # https://community.pega.com/knowledgebase/articles/application-development/84/alert-format
    timestamp: Optional[str]
    version: Optional[str]
    messageId: Optional[str]
    KPIValue: Optional[int]
    KPIThreshold: Optional[int]
    serverId: Optional[str]
    requestorId: Optional[str]
    userId: Optional[str]
    workPool: Optional[str]
    ruleApplicationNameVersion: Optional[str]
    encodedRuleset: Optional[str]
    checkoutEnabled: Optional[YN]
    interactionNumber: Optional[str]
    correlationId: Optional[str]
    sequence: Optional[int]
    thread: Optional[str]
    pegaThreadName: Optional[str]
    logger: Optional[str]
    stack: Optional[str]
    lastInput: Optional[str]
    firstActivity: Optional[str]
    lastStep: Optional[str]
    traceList: Optional[str]
    PALData: Optional[str]
    primaryPageClass: Optional[str]
    primaryPageName: Optional[str]
    stepPageClass: Optional[str]
    stepPageName: Optional[str]
    pegaStack: Optional[str]
    parameterPage: Optional[str]
    line: Optional[str]

    fileName: Optional[str]


class AlertCreate(AlertBase):
    pass


class Alert(AlertBase):
    id: Optional[int]

    class Config:
        orm_mode = True
