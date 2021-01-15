"""
Given a sorted integer array arr, two integers k and x, return the k closest
integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:
    |a - x| < |b - x|, or
    |a - x| == |b - x| and a < b
 

Example 1:
Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]

Example 2:
Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]

Constraints:
    - 1 <= k <= arr.length (we will never be asked to return more elements than there are)
    - 1 <= arr.length <= 104 (array length is 104 or less)
    - Absolute value of elements in the array and x will not exceed 104 (between -104,104)

Cases:
    - Singleton array
    - X not in array
    - X in array 
----------------------
I've solved this for an unsorted array with a maxheap, which would work here too. However,
I think a better solution is possible since the array is sorted. 

- Find nearest element to x in array (can do in log time with bisect)
    - arr[0]: return arr[0] and k-1 elements to the right
    - arr[-1]: return arr[-1] and k-1 elements to the left
    - Somewhere in middle:
        - get element at insertion point, then k-1 elements between i-k+1, i+k-1; can do this in k steps with two pointers
--------
solution(arr,x,k):
    if len(arr) == k:
        return arr
    
    i = nearest_element_to_x_using_bisect()
    if i == 0:
        return arr[:k]
    elif i == len(arr)-1:
        return arr[-k:]
    else:
        ans = deque([])
        l, r = i, i+1 # only reach this point if both i and i+1 are valid. 
        while len(ans) < k: 
            if l < 0 or abs(x - arr[l]) > abs(x - arr[r]): 
                # If l is invalid but queue is not full, then by problem statement r has to be valid. 
                ans.append(arr[r])
                r += 1
            else:
                # Same thing here; if r is invalid but queue not full, l must be valid. 
                ans.appendleft(arr[l])
                l -= 1
        return list(ans)


Dove in without thinking about this part:
    l is last element <= x
    r is first element > x

    bisect left returns i of first element >=
    bisect right returns i of first element greater
"""
from bisect import bisect_left, bisect_right
from collections import deque
from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if len(arr) == k:
            return arr

        r = bisect_right(arr, x)
        if r <= 1:  # x is <= arr[0]
            return arr[:k]
        elif r == len(arr)-1:  # x is >= arr[0]
            return arr[-k:]
        else:
            l = r - 1
            ans = deque([])
            while len(ans) < k:
                if r > len(arr)-1 or abs(x - arr[l]) <= abs(x - arr[r]):
                    # If l is invalid but queue is not full, then by problem statement r has to be valid.
                    ans.appendleft(arr[l])
                    l -= 1
                else:
                    # Same thing here; if r is invalid but queue not full, l must be valid.
                    ans.append(arr[r])
                    r += 1
            return list(ans)


s = Solution()
cases = [
    ([1, 2, 3, 4, 5], 4, 3, [1, 2, 3, 4]),  # Given 1; x in arr
    ([1, 2, 3, 4, 5], 4, -1, [1, 2, 3, 4]),  # given 2; x not in arr
    ([1, 2, 3, 4, 5], 3, 6, [3, 4, 5]),  # x > largest
    ([1, 2, 3, 4, 5], 3, 0, [1, 2, 3]),  # x < smallest
    ([1], 1, 5, [1]),  # singleton
    ([0, 0, 1, 2, 3, 3, 4, 7, 7, 8], 3, 5, [3, 3, 4])
]
for arr, k, x, expected in cases:
    actual = None
    try:
        actual = s.findClosestElements(arr, k, x)
        assert actual == expected
    except:
        print(f"{arr,k,x}: {expected} != {actual}")
        raise
    # print("--"*10)
