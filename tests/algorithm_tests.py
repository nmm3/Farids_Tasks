import datetime
import os
import random
import typing
from typing import List

import numpy as np


def _print_test_stats(test_number: int, start_time, finish_time):
    print("Тест {} прошел. Затраченное время: {:.3f} миллисекунд"
          .format(test_number, (finish_time.timestamp() - start_time.timestamp()) * 1000))


def _generate_random_array(size: int) -> List[int]:
    result = []
    for i in range(0, size):
        result.append(random.randint(-100000, 100000))
    return result


def _assert_sorted(array: List[int]):
    previous_value = array[0]
    for i in range(1, len(array)):
        assert previous_value <= array[i], "Сортируй нормально да! Тут какое-то месиво, а не отсортированный список!"
        previous_value = array[i]


def sort_test(number_of_tests: int):
    def func_wrapper(sort_func):
        def args_wrapper(*args, **kwargs):
            for i in range(1, number_of_tests):
                start_time = datetime.datetime.now()
                input_array = _generate_random_array(2 ** i)
                result = sort_func(input_array)
                finish_time = datetime.datetime.now()

                _assert_sorted(result)
                assert len(input_array) == len(result), "Размеры входного и выходного массива не совпадают"

                _print_test_stats(i, start_time, finish_time)
        return args_wrapper
    return func_wrapper


def primes_test(number_of_tests: int):
    def func_wrapper(primes_func):
        def args_wrapper(*args, **kwargs):
            print(os.getcwd())
            primes = list(map(lambda x: int(x.replace('\n', '')), open('../tests/primes.txt').readlines()))
            for i in range(1, number_of_tests):
                start_time = datetime.datetime.now()
                terminal_number = 2 ** i
                result = primes_func(terminal_number)
                finish_time = datetime.datetime.now()

                j = 0
                assert result[-1] <= terminal_number, "Куда прешь, слишком дохуя чисел, не хочешь ли ты меня наебать!?"
                while j < len(result):
                    assert primes[j] == result[j], "Тут где-то либо не простое число, либо не все найдены!"
                    j += 1
                assert primes[j] > terminal_number, "Слишком рано остановилась, нужно больше простых чисел!"

                _print_test_stats(i, start_time, finish_time)
        return args_wrapper
    return func_wrapper


def _generate_matrix(m: int, n: int) -> List[List[float]]:
    matrix = []
    for i in range(0, m):
        row = []
        matrix.append(row)
        for j in range(0, n):
            row.append(random.uniform(-100, 100))
    return matrix


def _check_matrix_equality(matrix_a: List[List[float]], matrix_b: List[List[float]]):
    assert len(matrix_a) == len(matrix_b), "Размер матрицы поехал!"
    for i in range(len(matrix_a)):
        assert len(matrix_a[i]) == len(matrix_b[i]), "Размер матрицы поехал!"

    for i in range(0, len(matrix_a)):
        for j in range(0, len(matrix_a[i])):
            assert 0.95 < abs(matrix_a[i][j] / matrix_b[i][j]) < 1.05, "Значения в матрице поехали! " \
                                                                       "Мб я накосячил, а мб и нет. Пиши если че"


def matrix_multiplication_test(number_of_tests: int):
    def func_wrapper(matrix_mult_func):
        def args_wrapper(*args, **kwargs):
            for i in range(1, number_of_tests):
                l_dim = i ** 2
                m_dim = (i ** 2) * 2
                n_dim = (i ** 2) * 4
                matrix_a = _generate_matrix(l_dim, m_dim)
                matrix_b = _generate_matrix(m_dim, n_dim)

                start_time = datetime.datetime.now()
                result = matrix_mult_func(matrix_a, matrix_b)
                finish_time = datetime.datetime.now()

                np_result = np.matmul(np.array(matrix_a), np.array(matrix_b))
                _check_matrix_equality(result, typing.cast(List[List[float]], np_result))

                _print_test_stats(i, start_time, finish_time)
        return args_wrapper
    return func_wrapper
