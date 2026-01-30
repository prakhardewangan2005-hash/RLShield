# RLShield Lite

A lightweight FastAPI-based reinforcement learning shield and monitoring service for Microsoft ML Intern project.

## Features
- **Inference Simulation**: Generates scores, labels, and confidence intervals.
- **Ranking Logic**: Implements custom weighted scoring: `score*0.7 + confidence*30 - latency_ms*0.01`.
- **Persistence**: SQLite storage for all decisions.
- **Metrics**: Real-time p95 latency and accuracy tracking.

## Setup Instructions

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
