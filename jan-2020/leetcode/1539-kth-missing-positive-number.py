"""
See binary search template for explanation.
"""


def binary_search(arr, val, cmp, ret):
    if not arr:
        return -1

    lo, hi = 0, len(arr)-1
    while lo < hi-1:
        lo, hi = cmp(arr, lo, val, hi)

    return ret(arr, lo, val, hi)


def kth_missing_cmp(arr, lo, k, hi):
    mid = (hi+lo)//2
    mid_missing_before = arr[mid] - mid - 1
    return (mid, hi) if mid_missing_before < k else (lo, mid)


def kth_missing_ret(arr, lo, k, hi):
    return hi if arr[lo] - lo - 1 < k else lo


class Solution:
    def findKthPositive(self, arr, k):
        # k-th missing is greater than largest
        if arr[-1] - len(arr) < k:
            return arr[-1] + k - (arr[-1] - len(arr))

        nearest_i = binary_search(arr, k, kth_missing_cmp, kth_missing_ret)
        left_missing = arr[nearest_i] - nearest_i - 1
        return arr[nearest_i] - (left_missing - k) - 1
