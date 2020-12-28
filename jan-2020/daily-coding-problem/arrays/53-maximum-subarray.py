"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

Constraints:
    - 1 <= nums.length <= 2 * 10^4 (up to 20,000 numbers)
    - -231 <= nums[i] <= 231 - 1 (small number range)
------
Brute force won't work; there are possibly 20,000 numbers - up to 1 + 2 + 3 + 4 + 5 ... + 20,000 possible subarrays, can't test them all.

What cases exist?
    - All positive, pick entire array
        - [1,2,3]
    - All negative, pick singleton with greatest
        - [-1,-2,-3] -> -1
    - Mix where we can pick a positive-valued contiguous subarray
        - [10,9,-1,8] -> entire array
        - [10,9,-1,8,-2] -> all but last

Some sort of overlapping subproblem here:
    - [10,-9,8] is [10], [10,-9,8,7] is entire array; is there a way we can re-use knowledge?
    - We can do an L->R pass and keep track of overall gain loss, then an R->L pass with the same
    - Can also keep track of min and max values for each pass

Arr: [-10,  1,  2, -4,  -5,    1,   2 ]
L-R: [-10, -9, -7, -11, -16, -15, -13 ]
R-L: [-13  -3  -4  -6   -2     3    2 ]
3 is best, pick last 2 elements

If we pick the idx of the max on the L-R cumsum pass, then we do an R-L cumsum pass up to the L-R max's index,
will we get the best subarray from those two indexes in the regular arr?

Arr: [-10,  1,   2,  -4,   -5,    1,   2  -9 ]

L-R  [-10, -9,  -7,  -11,  -16, -15, -13, -21]
                 ^
                 best in L-R pass
R-L  [-22  -12  -13  -15   -11   -6   -7   -9]
       |----------|
            ^
           get max from here for R-L pass

So max subarr is these two
            V    V
Arr: [-10,  1,   2,  -4,   -5,    1,   2  -9 ]


Doesn't work. Breaks on:
Arr: [-3, -2,  1]
LR   [-3, -5, -4] (-3 is max here, idx of -4 is actual answer)
RL   [-4  -1   1] 

Left-to-right vs right to left sums appears to break if we have only one value that should be included

What if instead of cumsum, each pass did something smarter, like "would it be better to add this, or start here?"
or maybe "where is it best for us to start?"
Then L-R pass would start at final index 


"""
from typing import List


def idx_of_cmax(arr):
    sums = []
    cmax = -float('inf')
    csum = 0
    idx = None
    for i, val in enumerate(arr):
        csum += val
        sums.append(csum)
        if csum > cmax:
            cmax = csum
            idx = i
    print(f"{sums}, i: {idx}, max: {sums[idx]}")
    return idx


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        print(nums)
        lr_i = idx_of_cmax(nums)
        rl_i = idx_of_cmax(reversed(nums))
        rl_i = len(nums) - rl_i
        return sum(nums[rl_i:lr_i+1])


if __name__ == '__main__':
    s = Solution()
    cases = [
        #([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
        #([1], 1),
        #([0], 0),
        #([-1], -1),
        #([-2147483647], -2147483647),
        #([-3, -2, -1], -1),
        ([-3, -2, 1], 1)

    ]
    for input_args, expected in cases:
        actual = s.maxSubArray(input_args)
        assert expected == actual, f"{input_args}, {expected} != {actual}"
