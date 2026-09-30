porog = float(input("Введите порог температуры: "))
n = int(input("Введите количество измерений: "))

error_count = 0

for i in range(n):
    x = input("Введите значение температуры: ")

    if x == "error":
        error_count += 1

print(f"Количество измерений: {n}")
print(f"Количество ошибок: {error_count}")