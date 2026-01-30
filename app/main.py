from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from . import models, schemas, utils
from .database import engine, get_db

# Initialize Database
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="RLShield Lite API")

@app.post("/api/predict", response_model=schemas.PredictResponse)
def predict(request: schemas.PredictRequest, db: Session = Depends(get_db)):
    score, label, confidence, latency_ms, weighted_score = utils.perform_inference(request.input_data)
    
    db_decision = models.Decision(
        score=score,
        label=label,
        confidence=confidence,
        latency_ms=latency_ms,
        weighted_score=weighted_score
    )
    db.add(db_decision)
    db.commit()
    db.refresh(db_decision)
    
    return {
        "score": score,
        "label": label,
        "confidence": confidence,
        "latency_ms": latency_ms,
        "weighted_score": weighted_score
    }

@app.get("/api/metrics", response_model=schemas.MetricResponse)
def get_metrics(db: Session = Depends(get_db)):
    decisions = db.query(models.Decision).all()
    p95, accuracy, total = utils.calculate_metrics(decisions)
    return {
        "p95_latency_ms": p95,
        "accuracy_percentage": accuracy,
        "total_samples": total
    }

@app.get("/api/decisions", response_model=List[schemas.DecisionResponse])
def get_decisions(db: Session = Depends(get_db)):
    # Return last 50 decisions
    decisions = db.query(models.Decision).order_by(models.Decision.id.desc()).limit(50).all()
    
    results = []
    for d in decisions:
        results.append({
            "id": d.id,
            "score": d.score,
            "label": d.label,
            "confidence": d.confidence,
            "latency_ms": d.latency_ms,
            "weighted_score": d.weighted_score,
            "timestamp": d.timestamp.isoformat()
        })
    return results
