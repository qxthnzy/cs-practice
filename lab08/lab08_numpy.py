import numpy as np


# Задание 1. Создание векторов и матриц

hours = np.arange(0, 22, 3)
line = np.linspace(0, 1, 5)
zeros = np.zeros(6, dtype=int)
unknown_table = np.full((2, 3), -1)
identity = np.eye(3)

print("Часы:", hours)
print("Линия:", line)
print("Нули:", zeros)
print("Матрица -1:\n", unknown_table)
print("Единичная матрица:\n", identity)

print("Форма:", hours.shape)
print("Размерность:", hours.ndim)
print("Количество элементов:", hours.size)
print("Тип данных:", hours.dtype)


# Задание 2. Индексы и срезы в векторе

print("Третий элемент:", hours[2])
print("Последний элемент:", hours[-1])
print("Индексы 2-5:", hours[2:6])
print("Каждый второй:", hours[::2])
print("Обратный порядок:", hours[::-1])