def predict_score(
    study_hours: float,
    sleep_hours: float,
) -> float:
    if study_hours < 0:
        raise ValueError("study_hours cannot be negative")
    if sleep_hours < 0:
        raise ValueError("sleepy_hours cannot be negative")
    
    score = study_hours * 8 + sleep_hours * 2
    return min(score, 100.0)