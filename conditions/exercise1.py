# Пользователь вводит 2 числа. Если второе число является делителем первого числа, то вывести "Первое число делится без остатка на второе"
# Иначе вывести "Первое число делится с остатком на второе. Остаток: {полученный остаток от деления}"
#
# Пример входных данных 1:
# 5, 2
# Пример выходных данных 1:
# Первое число делится с остатком на второе. Остаток: 1
#
# Пример входных данных 2:
# 6, 3
# Пример выходных данных 2:
# Первое число делится без остатка на второе

def solve():
    a1 = int(input("Введите делимое: "))
    a2 = int(input("Введите делитель: "))
    if a1%a2 == 0:
        print('Правильный выбор!')
    else:
        print('Попробуй еще раз. Остаток: ' + str(a1%a2))

        


if __name__ == '__main__':
    solve()