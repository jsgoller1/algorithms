from typing import List

from test_framework import generic_test, test_utils

"""
Our string will be 2n long for n pairs. 
At each index, we can either close an existing pair, or open a new one. 

"""

def generate_balanced_parentheses(num_pairs: int) -> List[str]:
    solutions = []
    def recurse(current, num_open, num_closed):
        if num_closed == num_pairs:
            solutions.append(''.join(current))
            return 
        if num_open < num_pairs:
            current.append('(')
            recurse(current, num_open+1, num_closed)
            current.pop()
        if num_open > num_closed:
            current.append(')')
            recurse(current, num_open, num_closed+1)
            current.pop()
    recurse([],0,0)
    return solutions


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('enumerate_balanced_parentheses.py',
                                       'enumerate_balanced_parentheses.tsv',
                                       generate_balanced_parentheses,
                                       test_utils.unordered_compare))
