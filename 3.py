sum = 0 # сумма элементов
count = 0 # количество элементов

while True:
    x = int(input()) # ввод x
    if x == 0: # остановка цикла в случае ввода 0
        break
    sum += x
    count += 1

if count > 0: # проверка если count больше нуля то ...
    average = sum / count
    print(average) # вывод результата
else: # иначе вывод ошибки
    print("Нет элементов для расчета среднего арифметического")