from typing import List

from test_framework import generic_test, test_utils


"""
List can contain duplicates
"""

def permutations(A: List[int]) -> List[List[int]]:
    solutions = set()
    curr_solution = []
    def recurse():
        if len(curr_solution) == len(A):
            solutions.add(tuple(curr_solution))
        for i, val in enumerate(A):
            if val != None:
                curr_solution.append(val)
                A[i] = None 
                recurse()
                A[i] = val 
                curr_solution.pop()
    recurse()
    return [list(solution) for solution in solutions]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('permutations.py', 'permutations.tsv',
                                       permutations,
                                       test_utils.unordered_compare))
