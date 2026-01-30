import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.database import Base, get_db

# Setup test database
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

@pytest.fixture(scope="module", autouse=True)
def setup_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

client = TestClient(app)

def test_predict_endpoint():
    response = client.post("/api/predict", json={"input_data": "test signal"})
    assert response.status_code == 200
    data = response.json()
    assert "score" in data
    assert "label" in data
    assert "weighted_score" in data
    assert data["label"] in ["Low", "Medium", "High"]

def test_metrics_endpoint():
    # Ensure there's at least one record
    client.post("/api/predict", json={"input_data": "metric test"})
    response = client.get("/api/metrics")
    assert response.status_code == 200
    data = response.json()
    assert "p95_latency_ms" in data
    assert data["total_samples"] >= 1

def test_decisions_endpoint():
    response = client.get("/api/decisions")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) <= 50
