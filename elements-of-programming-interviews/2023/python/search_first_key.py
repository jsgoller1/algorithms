from typing import List

from test_framework import generic_test


"""
Approaches
- Linear search
- Binary search to first element, linear search
  left from there.
- Modified binary search?
"""

import random


def linear_search(A: List[int], k: int) -> int:
    i = 0
    while i < len(A):
        if A[i] == k:
            return i
        i += 1
    return -1


def bin_then_linear_search(A: List[int], k: int) -> int:
    l, r = 0, len(A)-1
    while l <= r:
        m = (l+r) // 2
        if A[m] > k:
            r = m-1
        elif A[m] < k:
            l = m+1
        elif A[m] == k:
            while m > 0 and A[m-1] == k:
                m -= 1
            return m
    return -1


def search_first_of_k(A: List[int], k: int) -> int:
    if not A:
        return -1
    l, r = 0, len(A)-1
    m = -1
    while l < r:
        m = (l+r) // 2
        if A[m] > k:
            r = m-1
        elif A[m] == k:
            r = m
        else:  # A[m] < k:
            l = m+1
    return -1 if A[l] != k else l


def binary_search(A: List[int], k: int) -> int:
    l, r = 0, len(A)-1
    while l <= r:
        # l + r can overflow, but not in Python
        m = l + ((r-l) // 2)
        if A[m] > k:
            r = m-1
        elif A[m] == k:
            return m
        else:  # A[m] < k:
            l = m+1
    return -1


if __name__ == '__main__':
    """
    arr = sorted([random.randint(-100, 100) for _ in range(random.randint(0, 100))])
    k = arr[random.randint(0, len(arr)-1)]
    expected = linear_search(arr, k)
    actual = search_first_of_k(arr, k)
    assert expected == actual, f"{actual} != {expected}\nk = {k}\n{arr}"
    """
    exit(
        generic_test.generic_test_main('search_first_key.py',
                                       'search_first_key.tsv',
                                       search_first_of_k))
