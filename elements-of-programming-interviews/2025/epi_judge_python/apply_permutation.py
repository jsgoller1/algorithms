from typing import List

from test_framework import generic_test

"""
Trivial with linear extra storage; just permute then write back. 
Otherwise, this can be graph problem: start with 0th element, bump element
we move to to temporary storage, the move that element to the right place. 

A =    [0,100,-2,33]
perm = [2,0,1,3]
result = [100,-2,0,33]

"""
def apply_shift(perm, A, start_idx):
    temp = A[start_idx]
    next_idx = perm[start_idx]
    perm[start_idx] = None
    while next_idx != start_idx: 
        A[next_idx], temp = temp, A[next_idx]
        curr_idx = next_idx
        next_idx = perm[next_idx]
        perm[curr_idx] = None 
    A[start_idx] = temp 

def apply_permutation(perm: List[int], A: List[int]) -> None:
    for idx in perm: 
        if idx != None: 
            apply_shift(perm, A, idx)
    return


def apply_permutation_wrapper(perm, A):
    apply_permutation(perm, A)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('apply_permutation.py',
                                       'apply_permutation.tsv',
                                       apply_permutation_wrapper))
