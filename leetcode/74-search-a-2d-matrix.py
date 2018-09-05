"""
https://leetcode.com/problems/search-a-2d-matrix/description/
---
Understand

Program takes a value and a list of lists, should efficiently find whether
the value is in any sublist. Returns bool, not index.

This is a D&C problem - the lists are sorted, and later lists bound earlier lists. We do not
need to examine every item, so we can likely binsearch.
----
Plan

Naive: for sublist in list, if val in list return true, otherwise return false. O(m*n).

Better (this will be implemented on first try): Binary search based on first and last value in lists,
then binary search the list. log(m) + log(n).

Alternative - write one binsearch, use list comprehension to create list of first elements, then
binsearch the list whose index is returned (or none)

We will start by using two different implementations of binary
search, and then seeing if we can refactor them into one.

Possible to use binsearch function in standard lib? Python bisect docs say to use .index(), but source
shows this is O(N) (https://github.com/python/cpython/blob/master/Objects/listobject.c#L2491)

Actually - what if we follow the search based on first values of the list, find the closest value,
and then search the sublist?

Is there a way to easily do interval matching?

Wait - what if we squash the list, binsearch, and return true? We're not trying to find the index, just if it's
in the list.

----
Execute: See below - I copied / pasted my own binary search code from a private repo.
----
Review - Dang. I feel pretty silly about this one. All you have to do is flatten the list and do a
simple binsearch, but I immediately jumped into trying to test individual intervals, which was completely
unnecessary since we are just returning a bool. Even if we were returning an int, this approach would still
work - we could (probably) just divide the index in the flattened list by the row size.
"""


def binary_search(val, arr):
    """
    Executes a binary search. Assumes arr is sorted and contains
    no non-ints.

    Returns index of val in arr, or -1 if val isn't in arr.
    """
    if arr == []:
        return -1

    if (val < arr[0]) or (val > arr[len(arr) - 1]):
        return -1

    # Perform traditional halving, but until L and R are adjacent
    right = len(arr) - 1
    left = 0
    while (right - left != 1):
        mid = (left + right)//2
        if val == arr[mid]:
            return mid
        elif val > arr[mid]:
            left = mid
        else:  # val < arr[mid]
            right = mid

    # Explicitly test both
    if val == arr[right]:
        return right
    elif val == arr[left]:
        return left
    else:
        return -1


class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        flat_matrix = []
        for row in matrix:
            flat_matrix += row

        index = binary_search(target, flat_matrix)

        return index >= 0


if __name__ == '__main__':
    s = Solution()
    assert s.searchMatrix([
        [1,   3,  5,  7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ], 3) == True
