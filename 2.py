# ввод n
n = int(input())

found_zero = False # флаг, указывающий на то, что был найден ноль

for i in range(n):
    x = int(input()) # считываем очередное число
    if x == 0:
        found_zero = True

# вывод результата
if found_zero:
    print("YES")
else:
    print("NO")