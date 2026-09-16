from fastapi import FastAPI
from pydantic import BaseModel

from app.predictor import predict_score

app = FastAPI()

class PredictionRequest(BaseModel):
    study_hours: float
    sleep_hours: float
    exercise_hours: float
class PredictionRespone(BaseModel):
    score: float
    
@app.get("/")
def root() -> dict[str, str]:
    return {
        "message": "Hello, AI Backend"
    }

@app.get("/health")
def health() -> dict[str, str]:
    return {
        "status": "ok"
    }
@app.post("/predict")
def predict(request: PredictionRequest) -> PredictionRespone:
    score = predict_score(
        study_hours=request.study_hours,
        sleep_hours=request.sleep_hours,
        exercise_hours=request.exercise_hours,
    )
    
    return PredictionRespone(score=score)

@app.get("/info")
def info() -> dict[str, str]:
    return {
        "name": "Student Score Predictor",
        "version": "1.0.0"
    }