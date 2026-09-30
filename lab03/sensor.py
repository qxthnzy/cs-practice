porog = float(input("Введите порог температуры: "))
n = int(input("Введите количество измерений: "))

error_count = 0
prev_count = 0
max_temp = None

for i in range(n):
    x = input("Введите значение температуры: ")

    if x == "error":
        error_count += 1
    else:
        temp = float(x)

        if temp > porog:
            prev_count += 1

        if max_temp is None or temp > max_temp:
            max_temp = temp

print(f"Количество измерений: {n}")
print(f"Количество ошибок: {error_count}")
print(f"Количество значений выше порога: {prev_count}")
print(f"Максимальная температура: {max_temp:.1f}")