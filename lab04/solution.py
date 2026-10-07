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

def ranking(names: list[str], scores: list[float]) -> list[str]:
    result = []
    for i in range(len(scores)):
        result.append((scores[i], i))
    answer = []
    while result:
        best = 0
        for i in range(len(result)):
            if result[i][0] > result[best][0]:
                best = i
        answer.append(names[result[best][1]])
        result.pop(best)
    return answer