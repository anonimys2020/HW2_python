max_num = 0
count_max = 0

# ввод: первое число
num = int(input())

# цикл while, пока число не равно 0
while num != 0:
    if num > max_num: # если число больше текущего максимума то...
        max_num = num # обновляем максимум
        count_max = 1 # сбрасываем счетчик
    elif num == max_num: # если число равно текущему максимуму то...
        count_max += 1 # увеличиваем счетчик на 1

    # ввод: следующее число
    num = int(input())

# вывод: результат
print(count_max)