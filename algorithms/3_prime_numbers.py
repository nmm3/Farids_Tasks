# Написать алгоритм, который выводит все простые числа до определенного числа.
# На вход функции передается число, до которого нужно вывести простые числа.
# На выходе должен быть список простых чисел. (см. Решето Эратосфена)
# Пример: find_all_primes(6) выдаст список [2, 3, 5]

from typing import List

from tests.algorithm_tests import primes_test


@primes_test(25)
def find_all_primes(max_number: int) -> List[int]:
    pass


if __name__ == '__main__':
    find_all_primes()
