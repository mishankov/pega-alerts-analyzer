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

    @classmethod
    def from_alert_line(cls, alert_line: str, file_name: str = "PegaRULES-ALERTS.log"):
        alert_line_splited = alert_line.split("*")
        return cls(
            fileName=file_name,
            timestamp=alert_line_splited[0],
            version=alert_line_splited[1],
            messageId=alert_line_splited[2],
            KPIValue=alert_line_splited[3],
            KPIThreshold=alert_line_splited[4],
            serverId=alert_line_splited[5],
            # =alert_line_splited[6],
            # =alert_line_splited[7],
            requestorId=alert_line_splited[8],
            userId=alert_line_splited[9],
            workPool=alert_line_splited[10],
            ruleApplicationNameVersion=alert_line_splited[11],
            encodedRuleset=alert_line_splited[12],
            checkoutEnabled=alert_line_splited[13],
            interactionNumber=alert_line_splited[14],
            correlationId=alert_line_splited[15],
            sequence=alert_line_splited[16],
            thread=alert_line_splited[17],
            pegaThreadName=alert_line_splited[18],
            logger=alert_line_splited[19],
            stack=alert_line_splited[20],
            lastInput=alert_line_splited[21],
            firstActivity=alert_line_splited[22],
            lastStep=alert_line_splited[23],
            # =alert_line_splited[24],
            # =alert_line_splited[25],
            # =alert_line_splited[26],
            # =alert_line_splited[27],
            traceList=alert_line_splited[28],
            PALData=alert_line_splited[29],
            primaryPageClass=alert_line_splited[30],
            primaryPageName=alert_line_splited[31],
            stepPageClass=alert_line_splited[32],
            stepPageName=alert_line_splited[33],
            pegaStack=alert_line_splited[34],
            parameterPage=alert_line_splited[35],
            line=alert_line_splited[36],
        )


class AlertCreate(AlertBase):
    pass


class Alert(AlertBase):
    id: Optional[int]

    class Config:
        orm_mode = True
