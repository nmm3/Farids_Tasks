# Решить уравнение вида ax + b = c. Пользователь вводит a, b c. Нужно найти x
# Пример входных данных:
# 1, 2, 3
# Пример выходных данных:
# 1

    # Арифметические операции:
    # + - сложение
    # - - вычитание
    # * - умножение
    # / - деление
    # % - деление с остатком (Результат - остаток от деления. Пример 1: 7 % 3 == 1; Пример 2: 6 % 3 == 0)
    # () - скобки для приоритета операций
    # ** - возведение в степень (Пример: 3 ** 3 == 27)
    #
    # Переменные:
    # Пример 1: `a = 1` - Создаем переменную a со значением 1 
    # Пример 2: `a = 'abcde'` - Создаем переменную a со значением 'abcde'
    #
    # Стандартные функции:
    # str(a) - перевод числа в строку (a - число; возвращает строку);
    # print(a) - напечатать строку в консоль (a - строка; ничего не возвращает);
    # input(a) - попросить пользователя ввести данные (a - строка, отображаемая в консоли перед вводом; 
    # возвращает строку);
    # int(a) - перевод строки в число (a - строка; возвращает число);
    #
    # Литералы:
    # строковый литерал: начинается с ' или " заканчивается ' или "
    # 0123456789 - десятичный численный литерал
    # True, False - булевый литерал

def solve():
    a = int(input('Введите делитель: '))
    b = int(input('Введите остаток: '))
    с = int(input('Введите делимое: '))
    x = (с-b)/a
    print('Ваше неполное частное: ', str(x))

if __name__ == '__main__':
    solve()