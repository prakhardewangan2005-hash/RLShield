from pydantic import BaseModel, Field
from typing import List

class PredictRequest(BaseModel):
    input_data: str = Field(..., example="sample telemetry data")

class PredictResponse(BaseModel):
    score: float
    label: str
    confidence: float
    latency_ms: float
    weighted_score: float

class MetricResponse(BaseModel):
    p95_latency_ms: float
    accuracy_percentage: float
    total_samples: int

class DecisionResponse(BaseModel):
    id: int
    score: float
    label: str
    confidence: float
    latency_ms: float
    weighted_score: float
    timestamp: str

    class Config:
        from_attributes = True
