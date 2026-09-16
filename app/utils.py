def clamp_score(
    score: float,
) -> float:
    if score > 100:
        return 100
    return score
