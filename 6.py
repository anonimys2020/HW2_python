# ввод n
n = int(input())
factorial = 1
sum = 1

# цикл for от 1 до n включительно
for i in range(1, n+1):
    factorial *= i
    sum += 1/factorial

# вывод округленного результата до 5 знаков после запятой.
print(round(sum, 5))