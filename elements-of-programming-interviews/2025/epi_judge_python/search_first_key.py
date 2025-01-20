from typing import List

from test_framework import generic_test


def binsearch(A, k):
    l, r = 0, len(A)-1
    while l <= r:
        m = (l + r) // 2 # Python; won't overflow INT_MAX
        if k < A[m]:
            r = m - 1
        elif k == A[m]:
            return m
        else:
            l = m + 1 
    return -1

def binsearch_k_exists(A, k):
    l, r = 0, len(A)-1
    while l <= r:
        m = (l + r) // 2 # Python; won't overflow INT_MAX
        if k <= A[m]:
            r = m - 1
        else:
            l = m + 1 
    return l

from random import randint
for i in range(1000):
    arr = list(set([randint(-100, 100) for i in range(10)]))
    arr.sort()
    i = randint(0, len(arr)-1)
    k = arr[i]
    idx = binsearch(arr, k)
    idx2 = binsearch_k_exists(arr, k)

    assert arr[idx] == k == arr[idx2], f"i: {i}; idx: {idx}; idx2: {idx2}"
    bad_idx = binsearch(arr, arr[-1]+1000)
    assert bad_idx == -1, f"{bad_idx}"



def search_first_of_k(arr: List[int], target: int) -> int:
    l, r = 0, len(arr) - 1
    while l <= r:  # Use <= for inclusive search space
        m = (l + r) // 2
        if arr[m] < target:
            l = m + 1
        else:  # arr[m] >= target
            r = m - 1  # Exclude current midpoint
    return l if l < len(arr) and arr[l] == target else -1

x = [0,1,2,2,2,5,6,7,8,9]
idx = search_first_of_k(x, 2)
assert idx == 2, f"idx: {idx}"


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_first_key.py',
                                       'search_first_key.tsv',
                                       search_first_of_k))
