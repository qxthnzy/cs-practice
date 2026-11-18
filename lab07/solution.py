import numpy as np

def reshape_rows(
    values: list[float], width: int
) -> list[list[float]]:
    if width <= 0 or len(values) % width != 0:
        return []

    matrix = np.asarray(values, dtype=float)
    return matrix.reshape(-1, width).tolist()

def block(
    matrix: list[list[float]],
    rows: list[int],
    columns: list[int]
) -> list[list[float]]:
    if not matrix or not rows:
        return []

    if not columns:
        return [[] for _ in rows]

    array = np.asarray(matrix, dtype=float)
    return array[np.ix_(rows, columns)].tolist()