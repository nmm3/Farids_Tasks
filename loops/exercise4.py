# Пользователь вводит число. Проверить, является ли оно простым (делится только на 1 и на себя).
# Вывести "{введенное число} является простым числом". Иначе "{введенное число} не является простым числом"
#
# Пример входных данных 1:
# 1
# Пример выходных данных 1:
# 1 является простым числом
#
# Пример входных данных 2:
# 8
# Пример выходных данных 2:
# 8 не является простым числом
#
# Пример входных данных 3:
# 69
# Пример выходных данных 3:
# 69 не является простым числом
#
# Пример входных данных 4:
# 228
# Пример выходных данных 4:
# 228 не является простым числом
#
# Пример входных данных 5:
# 997
# Пример выходных данных 5:
# 997 является простым числом

def solve():

    x = int(input('Загадай число: '))
    boop = False

    for i in range(2, x):
        if bool(x % i) != True:
            boop = True

    if boop == True:
        print('Непростое.')
    else:
        print('Простое.')



if __name__ == '__main__':
    solve()