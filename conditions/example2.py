# Попрсить пользователя ввести число от 0 до 100. Если пользователь вводит число меньше нуля или больше 100, вывести: "Читай внимательнее!"
# иначе вывести "Спасибо!" 
# 
# Пример входных данных 1:
# 5
# Пример выходных данных 1:
# Спасибо!
#
# Пример входных данных 2:
# 1488
# Пример выходных данных 2:
# Читай внимательнее!


def solve():
    x = int(input('Введите число от 0 до 100: '))
    if x < 0 or x > 100:
        print('Читай внимательнее!')
    else:
        print('Спасибо!')

        

if __name__ == '__main__':
    solve()