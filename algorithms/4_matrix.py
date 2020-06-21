# Поумножаем матрицы. На вход приходят 2 матрицы в виде двумерных массивов размерностью l x m первый и m x n второй.
# Нужно перемножить эти матрицы и вернуть двумерный массив размером l x n.

from typing import List

from tests.algorithm_tests import matrix_multiplication_test


@matrix_multiplication_test(15)
def matrix_multiplication(matrix_a: List[List[float]], matrix_b: List[List[float]]) -> List[List[float]]:
    pass


if __name__ == '__main__':
    matrix_multiplication()
