from typing import List

from test_framework import generic_test



def intersect_two_sorted_arrays(A: List[int], B: List[int]) -> List[int]:
    intersection = []
    i = j = 0
    while i < len(A) and j < len(B):
        if A[i] == B[j]:
            if (not intersection) or intersection[-1] != A[i]:
                intersection.append(A[i])
            i, j = i+1, j+1 
        elif A[i] < B[j]:
            i += 1
        else: # A[i] > B[j]
            j += 1
    return intersection

A = [1,2,2,5]
B = [2,2,3,4]
expected = [2]
assert intersect_two_sorted_arrays(A, B) == expected


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('intersect_sorted_arrays.py',
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
