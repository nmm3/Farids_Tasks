# Пользователь вводит число a от 0 до 100. Выводить "Не угадал, попробуй снова" до тех пор, 
# пока пользователь не введет a. Как пользователь введет а - вывести "Поздравляю!"
#
# Пример входных данных 1:
# 3, 1, 2, 3
# Пример выходных данных 1:
# Не угадал, попробуй снова
# Не угадал, попробуй снова
# Поздравляю!
#
# Пример входных данных 2:
# 24, 1, 6, 16, 96, 24
# Пример выходных данных 2:
# Не угадал, попробуй снова
# Не угадал, попробуй снова
# Не угадал, попробуй снова
# Не угадал, попробуй снова
# Поздравляю!

def solve():
    x = int(input('Загадай число: '))
    print('А теперь угадай, какое число ты загадал!')
    a = int(input('Ну же... '))
    while a != x:
        print('Все хуйня, давай по новой!')
        a = int(input('Ну же... '))
    print('Наконец!')




if __name__ == '__main__':
    solve()