import time
import random
import numpy as np

def perform_inference(input_data: str):
    """
    Simulates an ML model inference.
    In a real scenario, this would call a loaded .onnx or .pt model.
    """
    start_time = time.time()
    
    # Simulate processing time 10ms - 100ms
    time.sleep(random.uniform(0.01, 0.1))
    
    # Deterministic pseudo-randomness based on input length for consistency
    score = float(min(100, max(0, (len(input_data) * 7) % 101)))
    confidence = round(random.uniform(0.7, 0.99), 2)
    
    if score < 33:
        label = "Low"
    elif score < 66:
        label = "Medium"
    else:
        label = "High"
        
    latency_ms = (time.time() - start_time) * 1000
    
    # Requirement: weighted_score = score*0.7 + confidence*30 - latency_ms*0.01
    weighted_score = (score * 0.7) + (confidence * 30) - (latency_ms * 0.01)
    
    return score, label, confidence, latency_ms, weighted_score

def calculate_metrics(decisions):
    if not decisions:
        return 0.0, 0.0, 0
    
    latencies = [d.latency_ms for d in decisions]
    p95_latency = float(np.percentile(latencies, 95))
    
    # For accuracy, we simulate a 'ground truth' check. 
    # In this logic, we assume 'High' labels with confidence > 0.8 are correct.
    correct = 0
    for d in decisions:
        if d.label == "High" and d.confidence > 0.8:
            correct += 1
        elif d.label != "High":
            correct += 1
            
    accuracy = (correct / len(decisions)) * 100
    return round(p95_latency, 2), round(accuracy, 2), len(decisions)
