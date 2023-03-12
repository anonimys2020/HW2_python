# В данной задаче можно попробовать найти сумму меньшего из двух соседних чисел,
# считанных из входных данных, и вернуть эту сумму в результате.

# ввод n
n = int(input())

result = 0
previous = 0

# цикл for от i до n
for i in range(n):
    # ввод current
    current = int(input())
    # находим минимум среди двух соседних чисел далее складываем и сохраняем в переменную result
    if previous < current:
        result += previous
    else:
        result += current
    previous = current

# вывод result
print(result)