from typing import List

from test_framework import generic_test


def multiply(num1: List[int], num2: List[int]) -> List[int]:
    neg = -1 if (num1[0] < 0) ^ (num2[0] < 0) else 1
    num1[0] = abs(num1[0])
    num2[0] = abs(num2[0])

    total = 0
    place = 1
    for digit1 in num1[::-1]:
        curr_place = place
        curr_total = 0
        for digit2 in num2[::-1]:
            curr_total += digit1 * digit2 * curr_place
            curr_place *= 10
        total += curr_total
        place *= 10

    solution = [] if total else [0]
    while total:
        solution.append(total % 10)
        total = total // 10
    solution[-1] *= neg

    return solution[::-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_multiply.py',
                                       'int_as_array_multiply.tsv', multiply))
