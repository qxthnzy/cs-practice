import numpy as np

def reshape_rows(
    values: list[float], width: int
) -> list[list[float]]:
    if width <= 0 or len(values) % width != 0:
        return []

    matrix = np.asarray(values, dtype=float)
    return matrix.reshape(-1, width).tolist()