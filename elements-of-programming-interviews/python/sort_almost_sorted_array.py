from typing import Iterator, List

from test_framework import generic_test

"""
ex: k=17, [1, -11, 2, -2, -19, 4, -9, 1, 10, -12, 6, -19, 9, -5, 0, 5, -4, 13, 19, 19, 11]
return [-19, -19, -12, -11, -9, -5, -4, -2, 0, 1, 1, 2, 4, 5, 6, 9, 10, 11, 13, 19, 19]

- brute force is just sorting the array
- if k is 0, array is already sorted
- if k is 1, then between arr[i-1], arr[i], and arr[i+1] there is a minimal element. 
- the smallest element of the array is within k of 0. 
- the second smallest element is within k of 1. 
- if k is greater than or equal to array len, no better than brute force 

"""
from heapq import heappush, heappop


def sort_approximately_sorted_array(sequence: Iterator[int],
                                    k: int) -> List[int]:
    heap = []
    ans = []
    i = 0
    while i <= k:
        try:
            heappush(heap, next(sequence))
        except StopIteration:
            pass
        i += 1
    while heap:
        ans.append(heappop(heap))
        try:
            heappush(heap, next(sequence))
        except StopIteration:
            continue
    return ans


def sort_approximately_sorted_array_wrapper(sequence, k):
    return sort_approximately_sorted_array(iter(sequence), k)


if __name__ == '__main__':
    cases = [
        ([1, -11, 2, -2, -19, 4, -9, 1, 10, -12, 6, -19, 9, -5, 0, 5, -4, 13, 19, 19, 11], 17),
        ([1, 2, 3, 4, 5, 6, 7], 0),
        ([2, 1, 4, 3, 7, 6, 9, 8], 1),
    ]
    for case, k in cases:
        expected = sorted(case)
        actual = sort_approximately_sorted_array_wrapper(case, k)
        assert actual == expected, f"\n{k}:{case}\n{actual} != {expected}"
    exit(
        generic_test.generic_test_main(
            'sort_almost_sorted_array.py', 'sort_almost_sorted_array.tsv',
            sort_approximately_sorted_array_wrapper))
