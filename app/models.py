from sqlalchemy import Column, Integer, Float, String, DateTime
from datetime import datetime
from .database import Base

class Decision(Base):
    __tablename__ = "decisions"

    id = Column(Integer, primary_key=True, index=True)
    score = Column(Float)
    label = Column(String)
    confidence = Column(Float)
    latency_ms = Column(Float)
    weighted_score = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)
