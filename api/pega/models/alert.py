from typing import Optional

from pydantic import BaseModel


class Alert(BaseModel):
    # https://community.pega.com/knowledgebase/articles/application-development/84/alert-format
    timestamp: Optional[str]
    version: Optional[str]
    KPIValue: Optional[int]
    KPIThreshold: Optional[int]
    serverId: Optional[str]
    requestorId: Optional[str]
    userId: Optional[str]
    workPool: Optional[str]
    ruleApplicationNameVersion: Optional[str]
    encodedRuleset: Optional[str]
    checkoutEnabled: Optional[str]  # Y/N
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
