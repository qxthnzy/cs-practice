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

def column_means(
    matrix: list[list[float]]
) -> list[float]:
    if not matrix:
        return []

    array = np.asarray(matrix, dtype=float)
    return np.round(array.mean(axis=0), 6).tolist()


def column_range(
    matrix: list[list[float]], column: int
) -> float:
    if not matrix:
        return 0.0

    array = np.asarray(matrix, dtype=float)
    values = array[:, column]

    return round(float(values.max() - values.min()), 6)