# Пользователь вводит число. Если это число равно 42, то вывести "Это ответ". Если не равно, вывести, "Это вопрос"
#
# Пример входных данных 1:
# 5
# Пример выходных данных 1:
# Это вопрос
#
# Пример входных данных 2:
# 42
# Пример выходных данных 2:
# Это ответ



def solve():
    # if ... else- оператор условия. Если условие выполнилось, то выполняется код в этом блоке.
    # Если условие не выполнилось, то выполняется блок кода, прописанный в else.
    # Пример:
    # if 1 == 2:
    #     print('1 == 2')
    # else:
    #     print('1 != 2')
    #
    #
    # Операторы сравнения:
    # == - равно
    # != - не равно
    # > - больше
    # < - меньше
    # >= - больше или равно
    # <= - меньше или равно
    #
    # Булева алгебра: 
    # and - логическое умножение:
    # 1 and 1 == 1
    # 1 and 0 == 0
    # 0 and 1 == 0
    # 0 and 0 == 0 
    # 
    # or - логическое сложение:
    # 1 or 1 == 1
    # 1 or 0 == 1
    # 0 or 1 == 1
    # 0 or 0 == 0
    # 
    # not - логическое отрицание
    # not 1 == 0 
    # not 0 == 1

    a = int(input('Введите число a: '))
    if a == 42:
        print('Это ответ')
        
    else:
        print('Это вопрос')

        
    
    
    
    

if __name__ == '__main__':
    solve()