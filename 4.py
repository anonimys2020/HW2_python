# ввод первого элемента
prev = int(input())
length = 1
max_length = 1 #

while True:
    n = int(input()) # ввод n
    if n == 0: # остановка цикла в случае ввода 0
        break
    if n > prev or n < prev: # проверка если n > prev или n < prev то увеличить length на единицу
        length += 1
    else:
        if length > max_length: #
            max_length = length
        length = 2
    prev = n

# вывод max_length
print(max_length)