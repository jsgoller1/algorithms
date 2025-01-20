from typing import List

from test_framework import generic_test, test_utils

"""
"""

def combinations(n: int, k: int) -> List[List[int]]:
    solutions = []
    def recurse(current_solution, i):
        if len(current_solution) == k:
            solutions.append(current_solution[:])
        for j in range(i+1, n+1):
            current_solution.append(j)
            recurse(current_solution, j)
            current_solution.pop()
    recurse([], 0)
    return solutions


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'combinations.py',
            'combinations.tsv',
            combinations,
            comparator=test_utils.unordered_compare))
