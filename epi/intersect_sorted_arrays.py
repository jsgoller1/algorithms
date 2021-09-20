from typing import List

from test_framework import generic_test

"""
Given two lists of ints, return a list containing the intersection of both
- Inputs may be empty or very large
- Inputs and outputs should contain only ints
- Inputs may have duplicates
- Output should not have duplicates, and should be sorted
####
- This is just a setwise intersection:
    - Create an empty set (dict mapping element to true)
    - For each element in A, then each element in B:
        - if the element is not in the set, add it. Otherwise skip it.
    - Return the set as a list
- Constructing set is O(len(A) + len(B)), then sorting is linearithmic in set's size; if both A and B are identical
then if len(A) = len(B) = N, O(N * log(N); sorting will dominate set construction in this case
- Can we do better than linearithmic since inputs are sorted? 
    - We do need to look at every input (linear)
#### 
Linear time two pointer approach
- Lists already sorted
- No lesser elements found to the right of any element
Pseudo:
- Initialize empty list sol
- Start with A pointer at A[0] and B pointer at B[0]; both at lowest input of each set
- If A[0] == B[0] and sol empty or sol[-1] != either, append to sol; advance both
- Otherwise whichever is lower: move it up until it's not lower
- Return sol
"""
def intersect_two_sorted_arrays(A: List[int], B: List[int]) -> List[int]:
    solution = []
    a_i = b_i = 0
    while a_i < len(A) and b_i < len(B):
        curr_a, curr_b = A[a_i], B[b_i]
        if curr_a == curr_b:
            if not solution or curr_a != solution[-1]:
                solution.append(curr_a)
            a_i += 1
            b_i += 1
        elif curr_a < curr_b:
            a_i += 1
        else:
            b_i += 1 
    return solution


def intersect_two_sorted_arrays_nlogn(A: List[int], B: List[int]) -> List[int]:
    "nlogn approach"
    return sorted(list(set(A).intersection(set(B))))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('intersect_sorted_arrays.py',
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
