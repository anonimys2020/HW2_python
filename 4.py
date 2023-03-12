best = 0
current = 0

previous = None
incr = None

# ввод: n
n = int(input())

# цикл while пока значение переменной n не равно 0
while n != 0:
    # Флаг any_fits указывает, может ли текущий элемент быть добавлен в текущую последовательность
    any_fits = previous is None or incr is None
    # если n не равен previous и если флаг равен True или n больше previous, то увеличить current на 1 и если previous не равен None и n больше previous, то incr = True
    # иначе incr = None. Если current больше best, то присваиваем best = current. Далее обнуляем current
    if n != previous:
        if any_fits:
            if previous is not None:
                if n > previous:
                    incr = True
            current += 1
        elif n > previous:
            if previous is not None:
                if n > previous:
                    incr = True
            current += 1
    else:
        incr = None
        if current > best:
            best = current
        current = 1
    # присвоить previous = n
    previous = n
    # ввод: новое число n
    n = int(input())

# если current больше best, то присвоить переменной best значение переменной current
if current > best:
    best = current

# вывод best
print(best)