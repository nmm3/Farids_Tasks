# Пользователь вводит 3 числа. Каждое число - это длина стороны треугольника. Нужно вывести, является ли треугольник равносторонним, равнобедренным или общего вида
#
# Пример входных данных 1:
# 3, 3, 3
# Пример выходных данных 1:
# Равносторонний треугольник
#
# Пример входных данных 2:
# 2, 3, 3
# Пример выходных данных 2:
# Равнобедренный треугольник
#
# Пример входных данных 3:
# 2, 3, 4
# Пример выходных данных 3:
# Треугольник общего вида

def solve():
    a1 = int(input('Введите первую сторону: '))
    a2 = int(input('Введите вторую сторону: '))
    a3 = int(input('Введите третью сторону: '))
    if a1 == a2 == a3:
        print('Равносторонний треугольник.')
    elif a1 != a2 != a3:
        print('Треугольник общего вида. ')
     else:
        print('Если я что-то понимаю в геометрии, это равнобедренный треугольник.')


if __name__ == '__main__':
    solve()