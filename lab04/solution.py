def winner(names: list[str], scores: list[float]) -> str:
    best = 0
    for i in range(len(scores)):
        if scores[i] > scores[best]:
            best = i
    return names[best]

def average(scores: list[float]) -> float:
    if len(scores) == 0:
        return 0.0
    return round(sum(scores) / len(scores), 2)