"""
Given an array of integers that are out of order, determine the 
bounds of the smallest window that must be sorted in order for
the entire array to be sorted. 

Ex: [3,7,5,6,9] -> (1,3)

Leetcode #581; question in the book calls for indexes, Leetcode calls for length

LC constraints:
    - between 1 and 10,000 numbers
    - Individual numbers between -100,000 and 100,000
    
- Cases:
    - 2+ unsorted subarrays: 
        - require sorting entire subarray from first unsorted element to last unsorted; in the above case, whole array
        - Don't have a choice about this; picking smaller of the two leaves the array unsorted
        - Even if a third is found, we still have to sort from the first
        - [3,2,1,4,5,6,7,8,9,12,11,10] 
              ^                ^
    - 2 unsorted arrays; i.e. two sorted subarrays in wrong order
        - Pick shorter of two
        - [5,6,1,2,3]
              ^
    - 1 unsorted array: [4,3,2,1]
        - Return entire array
    - Completely sorted: [1,2,3,4]
        - Return 0
    - Singleton: [1]
        - Return 0
-----------------------------------

    
Problem feels like it has some kind of optimal substructure:
    - [2,3,4,5,1] depends on [2,3,4,5] depends on [2,3,4]
    - [3,2,1,4,5,6,7,8,9,12,11] = whole array = [3,1,2,3,4,5,6,7,8,9,12,11]; answer is same if going from left to right vs right to left

- One edge case: [5,6,7,1,2,3,4] vs [4,5,6,7,1,2,3] - same values, two adjacent sorted arrays that are not in the correct order themselves. 
    - [5,6,7,1,2,3,4] -> optimal is 5,6,7,1, not 7,1,2,3,4
    - [4,5,6,7,1,2,3] -> optimal is 7,1,2,3, not 4,5,6,7,1

- Should we look for sorted or unsorted?
    - if there's multiple unsorted ranges, the entire range in between needs to be sorted:
        - [2,1,3,4,5,6,8,7] -> whole array 
-------------------------
Going from left to right
    i = 0, j = 1
    unsorted_subarrays = 0
    cover_start = None
    cover_end = None
    while j < len(arr):
        if arr[j] > arr[i]:
            cover_start = i if cover_start == None else cover_start
            if cover_end != j-1:
                unsorted_subarrays += 1
            cover_end = j
    
    cover_size = cover_end - cover_start + 1
    remainder_size = len(arr) - cover_size
    if unsorted_subarrays == 0:
        return 0
    elif unsorted_subarrays == 1:
        return min(cover_size, remainder_size)
    else:
        return cover_size
"""
from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        return 0


if __name__ == '__main__':
    s = Solution()
    cases = [
        # ([2, 6, 4, 8, 10, 9, 15], 5),  # Need to sort [6, 4, 8, 10, 9] in ascending order
        # ([1, 2, 3, 4], 0),  # already sorted
        ([1], 0),  # single element array, already sorted
    ]
    for input_args, expected in cases:
        actual = s.findUnsortedSubarray(input_args)
        assert expected == actual, f"{input_args}, {expected} != {actual}"
