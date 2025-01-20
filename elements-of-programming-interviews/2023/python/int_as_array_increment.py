from typing import List

from test_framework import generic_test


def plus_one(A: List[int]) -> List[int]:
    # haha list comprehension go brrr
    # (see my c++ solution for a more traditional answer)
    val = int("".join([str(val) for val in A])) + 1
    return [int(char) for char in list(str(val))]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))
