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
        - require sorting entire subarray from first unsorted element to last unsorted; smallest cover covering all unsorted elements
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
This problem was _HARD_ - I spent maybe 2.5 hours on it with multiple approaches. I didn't fully understand 
the statement, but still struggled. In the end, some key insights were:
- We are looking for the "minimum cover" of the set that covers the unsorted portion
- if we only rearrange the elements there, it comes out completed sorted. 
- This means that if the first element of the array is greater than the last, the entire array must be sorted. 

Solution:
- Do one pass from left to right. Any element that is less than the current known maximum element is "out of order".
- Do a pass from right to left. Any element greater than the current minimum is out of order. 
- The cover will be from the lowest out-of-order element to the greatest out of order element. 

"""
from typing import List


class Solution:
    def findUnsortedSubarray(self, arr: List[int]) -> int:
        curr_min = min_wrong_i = float('inf')
        curr_max = max_wrong_i = -float('inf')
        # Do left to right pass; any where val is lt max is out of order
        for i, val in enumerate(arr):
            if val < curr_max:
                min_wrong_i = min(i, min_wrong_i)
                max_wrong_i = max(i, max_wrong_i)
            else:
                curr_max = val
        for i, val in list(enumerate(arr))[::-1]:
            if val > curr_min:
                min_wrong_i = min(i, min_wrong_i)
                max_wrong_i = max(i, max_wrong_i)
            else:
                curr_min = val
        cover_size = max_wrong_i - min_wrong_i + 1
        return 0 if abs(cover_size) == float('inf') else cover_size


if __name__ == '__main__':
    s = Solution()
    cases = [
        ([1], 0),  # single element array, already sorted
        ([1, 2, 3, 4], 0),  # already sorted
        ([5, 6, 1, 2, 3], 5),  # two sorted subarrays in unsorted order; pick smaller cover
        ([5, 6, 7, 1, 2, 3], 6),  # two equal-sized sorted subarrays in unsorted order; pick smaller cover
        ([20, 4, 5, 6, 3], 5),  # whole array
        ([20, 4, 5, 6, 3, 4, 5], 7),  # whole array
        ([19, 20, 4, 5, 6, 3, 4, 5], 8)  # whole array
    ]
    for input_args, expected in cases:
        actual = s.findUnsortedSubarray(input_args)
        assert expected == actual, f"{input_args}, {expected} != {actual}"
