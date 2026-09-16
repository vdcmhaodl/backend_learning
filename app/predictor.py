from app.utils import clamp_score
def predict_score(
    study_hours: float,
    sleep_hours: float,
    exercise_hours: float,
) -> float:
    if study_hours < 0:
        raise ValueError("study_hours cannot be negative")
    if sleep_hours < 0:
        raise ValueError("sleepy_hours cannot be negative")
    if exercise_hours < 0:
        raise ValueError("exercise_hours cannot be negarive")
    
    score = study_hours * 8 + sleep_hours * 2 + exercise_hours * 3
    return clamp_score(score)