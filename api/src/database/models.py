from sqlalchemy import Column, Integer, String

from .database import Base


class PegaAlert(Base):
    __tablename__ = "pega_alerts"

    id = Column(Integer, primary_key=True, index=True)
    fileName = Column(String)

    timestamp = Column(String)
    version = Column(String)
    messageId = Column(String)
    KPIValue = Column(Integer)
    KPIThreshold = Column(Integer)
    serverId = Column(String)
    requestorId = Column(String)
    userId = Column(String)
    workPool = Column(String)
    ruleApplicationNameVersion = Column(String)
    encodedRuleset = Column(String)
    checkoutEnabled = Column(String)
    interactionNumber = Column(String)
    correlationId = Column(String)
    sequence = Column(Integer)
    thread = Column(String)
    pegaThreadName = Column(String)
    logger = Column(String)
    stack = Column(String)
    lastInput = Column(String)
    firstActivity = Column(String)
    lastStep = Column(String)
    traceList = Column(String)
    PALData = Column(String)
    primaryPageClass = Column(String)
    primaryPageName = Column(String)
    stepPageClass = Column(String)
    stepPageName = Column(String)
    pegaStack = Column(String)
    parameterPage = Column(String)
    line = Column(String)
