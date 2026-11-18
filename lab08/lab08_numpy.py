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

# Задание 3. Строки и столбцы таблицы

temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18]
])

print("Форма:", temperatures.shape)
print("Размерность:", temperatures.ndim)
print("Количество элементов:", temperatures.size)

print("Элемент:", temperatures[1, 2])
print("Первая строка:", temperatures[0])
print("Последний столбец:", temperatures[:, -1])
print("Первые две строки без первого столбца:",
      temperatures[:2, 1:])

center = temperatures[:2, 1:3]
print("Центральный фрагмент:\n", center)
print("Форма фрагмента:", center.shape)


# Задание 4. Прямоугольные срезы

matrix = np.arange(1, 26).reshape(5, 5)

first_rows = matrix[:3, :]
last_rows = matrix[-2:, :]
first_columns = matrix[:, :2]
fragment = matrix[1:4, 2:5]
corner = matrix[-2:, -2:]

print("Первые три строки:\n", first_rows)
print("Форма:", first_rows.shape)

print("Последние две строки:\n", last_rows)
print("Форма:", last_rows.shape)

print("Первые два столбца:\n", first_columns)
print("Форма:", first_columns.shape)

print("Прямоугольный фрагмент:\n", fragment)
print("Форма:", fragment.shape)

print("Правый нижний угол:\n", corner)
print("Форма:", corner.shape)