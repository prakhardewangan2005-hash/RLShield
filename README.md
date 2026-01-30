# 🛡️ RLShield Lite

A lightweight **FastAPI-based reinforcement learning shield and monitoring service**, designed to simulate **production-grade ML inference, ranking, and observability systems**.  
Built as a **resume-grade ML systems project** aligned with **Microsoft ML / MLE Intern** expectations.

---

## 🚀 Live Deployment

- **Base URL:** https://rlshield-production.up.railway.app  
- **Swagger / OpenAPI Docs:** https://rlshield-production.up.railway.app/docs  

Health check:


GET /
→ { "status": "RLShield running" }

---

## 📌 Overview

RLShield Lite demonstrates how **machine learning models are served, ranked, monitored, and evaluated in production**.

Instead of focusing on training models, this project emphasizes:
- ML inference pipelines
- Latency-aware ranking
- Metrics aggregation
- API-first system design

This mirrors **real-world ML platforms** used in large-scale tech companies.

---

## ✨ Features

- **Inference Simulation**  
  Generates scores, labels (Low / Medium / High), confidence values, and latency to mimic real ML inference.

- **Ranking Logic**  
  Implements a custom weighted ranking function:

- **Persistent Storage**
  Uses SQLite to store all decisions

---

## 🚀 Deployment

- **Deployed using Railway with:**
  Python 3.11

  ASGI (Uvicorn)

  Auto CI/CD via GitHub
