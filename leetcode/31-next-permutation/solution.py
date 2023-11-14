from typing import List
"""
All possible perms: (O(n!))
generate any one perm: O(n) (pull random elements from list of indices)
First, last: O(nlogn) (sort, then reverse)

- moving forward in the list of sorted permutations involves moving n left of m, where n > m. First perm is sorted
  ascending, last sorted descending. 

wraparound edge case is easy to detect, O(n) scan for descending order. If so, just reverse in O(n) time and return. 

- Can we easily get a permutation that is "mid" for a high and low? (binary search)
    - no: binary search requires mid+1, which is "next" (the problem we are solving)

- [1,2,3,4,5]
- [1,2,3,5,4]
- [1,2,4,3,5]
...
- [1,5,2,3,4]
- [1,5,2,4,3]
- [1,5,3,2,4]
- [1,5,3,4,2]
- [1,5,4,2,3]
- [1,5,4,3,2]
- [2,1,3,4,5]

- It seems like we need to take the rightmost possible element and swap it left with the closest where L < R,
then sort everything to the right of it. O(n) + O(n*log(n))
    - How will we tell [1,5,3,4,2] apart from [1,5,4,3,2] without O(n^2) checks? 
        - In both, 2 is the rightmost element
        - [1,5,3,4,2] has a shorter distance swap (3 and 4)

- If we go pair by pair from the right to left looking for arr[l] < arr[r], stop at the first one we find. arr[l] is our "pivot",
but we may not actually want to swap it with arr[r]. (O(n))
- the proper swap partner for the pivot is the smallest element to its right that is still larger than it. O(n)
- we then do the swap. O(c).
- Then we reverse everything the right of the index where the pivot was before the swap. O(n).


"""


def find_pivot(arr):
    i = len(arr)-2
    while i >= 0:
        if arr[i] < arr[i+1]:
            return i
        i -= 1
    return -1


assert find_pivot([0, 1, 2, 3, 4, 5]) == 4
assert find_pivot([5, 4, 3, 2, 1]) == -1
assert find_pivot([2, 5, 4, 3, 2, 1]) == 0


def is_descending(nums):
    i = 0
    while i < len(nums)-1:
        if nums[i] < nums[i+1]:
            return False
        i += 1
    return True


assert not is_descending([1, 2, 3, 4, 5])
assert is_descending([5, 4, 3, 2, 1])
assert is_descending([5, 5, 3, 2, 1])
assert is_descending([])


def find_partner(arr, i):
    min_j = -1
    for j, val in enumerate(arr[i+1:], i+1):
        if val > arr[i]:
            min_j = j
    return min_j


assert find_partner([1, 5, 4, 3, 2], 0) == 4
assert find_partner([5, 4, 3, 2], 0) == -1


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if is_descending(nums):
            nums.sort()
            return
        i = find_pivot(nums)
        j = find_partner(nums, i)
        nums[i], nums[j] = nums[j], nums[i]
        for i, val in enumerate(nums[:i+1] + nums[i+1:][::-1]):
            nums[i] = val


s = Solution()
cases = [
    ([1, 2, 3], [1, 3, 2]),
    ([3, 2, 1], [1, 2, 3]),
    ([1, 1, 5], [1, 5, 1]),
    ([1, 5, 4, 3, 2], [2, 1, 3, 4, 5]),
    ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5])
]
for arr, expected in cases:
    actual = arr.copy()
    s.nextPermutation(actual)
    assert actual == expected, f"{arr}: {actual} != {expected}"
