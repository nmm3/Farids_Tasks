# Пользователь вводит 2 числа: координаты x и y точки. 
# Нужно проверить, лежит ли точка внутри области, ограниченной четырьмя прямыми.
# 1. x = 1 - левая граница 
# 2. x = 5 - правая граница
# 3. у = x - нижняя граница
# 4. y = 2x + 5 - верхняя граница
# Если точка лежит внутри этой области, вывести "Точка находится внутри области", иначе вывести "Точка находится вне области"
#
# Пример входных данных 1:
# 1 1
# Пример выходных данных 1:
# Точка находится вне области
#
# Пример входных данных 2:
# 2 3
# Пример выходных данных 2:
# Точка находится внутри области
#
# Пример входных данных 3:
# 3 12
# Пример выходных данных 3:
# Точка находится вне области
#
# Пример входных данных 4:
# 3 10
# Пример выходных данных 4:
# Точка находится внутри области

def solve():
    print('Варнинг: наши действия не несут никакого практического смысла, джаст фо фан, как грится.')
    x = int(input('Введите X: '))
    y = int(input('Введите Y: '))
    if (5 > x > 1) and (y > x) and (y < ((2 * x) + 5)):
        print('Точка находится внутри области.')
    else:
        print('Точка в своем сознании настолько преисполнилась...')

if __name__ == '__main__':
    solve()