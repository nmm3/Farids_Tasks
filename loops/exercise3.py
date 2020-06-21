# Пользователь вводит число n. Вывести Ряд Фибоначчи до n члена. 
# k член ряда Фибоначчи расчитывается по формуле ak = ak-1 + ak-2
# Например, рядом фибоначчи до 7-го члена будет 1 1 2 3 5 8 13
#
# Пример входных данных 1:
# 1
# Пример выходных данных 1:
# 1
#
# Пример входных данных 2:
# 7
# Пример выходных данных 2:
# 1 1 2 3 5 8 13
#
# Пример входных данных 3:
# 9
# Пример выходных данных 3:
# 1 1 2 3 5 8 13 21 34

def solve():
    fibonacci_numbers = '1'
    number_of_numbers = int(input('Введите нужное число: '))

    if number_of_numbers == 1:
        print('1')
    else:
        pre_pre_fibonacci_value = 0
        pre_fibonacci_value = 1
        for i in range(0, number_of_numbers-1):
            fibonacci_value = pre_fibonacci_value + pre_pre_fibonacci_value
            fibonacci_numbers += ' ' + str(fibonacci_value)
            pre_fibonacci_value, pre_pre_fibonacci_value = pre_pre_fibonacci_value, pre_fibonacci_value
            pre_fibonacci_value += pre_pre_fibonacci_value
        print(fibonacci_numbers)


if __name__ == '__main__':
    solve()