from typing import List

from test_framework import generic_test

from collections import Counter

def longest_subarray_with_distinct_entries(A: List[int]) -> int:
    present = Counter()
    longest = l = 0
    for r in range(len(A)):
        present[A[r]] += 1
        while present[A[r]] > 1:
            present[A[l]] -= 1
            l += 1
        longest = max(longest, r - l + 1)
    return longest

def longest_subarray_with_distinct_entries_first_attempt(A: List[int]) -> int:
    distinct = Counter(set(A))
    present = Counter()
    longest = l = r = 0 
    while r < len(A):
        present[A[r]] += 1
        while present - distinct: 
            present[A[l]] -= 1
            l += 1 
        longest = max(r-l+1, longest)
        r += 1 
    return longest


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'longest_subarray_with_distinct_values.py',
            'longest_subarray_with_distinct_values.tsv',
            longest_subarray_with_distinct_entries))
