"""
Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it can trap after raining.

In: List of ints
    - can be up to 30,000 in len
    - 0 <= individual height <= 100,000
Out:
    - int
----------------------------------------
Possible cases:
    - Empty (n=0) -> 0
    - All equal (n!=0, all heights equal) -> 0
    - Most possible rainwater -> height[0] = height[len-1] = 100,000, all other 0
    - Average case will be varying heights; some rainwater caught between
    - all decreasing / increasing -> 0

When is rainwater caught:
    - if two heights > 0 in sequence with at least one lower in between
Not caught:
    - two consecutive of equal height (without nesting in above case)
    - continuous increasing or decreasing heights

Need to be able to detect "pockets"; height[n], height[m] > 0 with n < k < m, height[k] < height[n], height[m]
When don't previous values matter?
    - we found a new max
When they do matter:
    - found "pocket" but not a new max

Forward pass
value, max, rainwater, stack
 X      0       0       []
 1      1       0       [1]
 0      1       0       [1,0]
 2      2       1       [2]
 1      2       1       [2,1]
 0      2       1       [2,1,0]
 1      2       1       [2,1,0,1]
 3      3       5       [3]
 2      3       5       [3,2]
 1      3       5       [3,2,1]
 2      3       5       [3,2,1,2]
 1      3       5       [3,2,1,2,1]

Backward pass
value, max, rainwater, stack
 X      0       5       []
 1      1       5       [1]
 2      2       5       [2]
 1      2       5       [2,1]
 2      2       6       [2]
 3      3       6       [3,2]

 Return 6


------------------------------------------
Two pass approach with stack
- Start at beginning of array with empty stack, max = 0, water = 0
    for each value in heights:
        if value >= max:
            unwind stack to previous max
            compute how much rainwater would be caught and save; must have pocket
            empty stack
            value becomes new max
        stack.push(value)
    heights = stack.reversed()
    empty stack, max = 0
    repeat above procedure
    return rainwater
"""
from typing import List


def evaluate(height):
    stack = []
    max_height = 0
    collected = 0
    for current_height in height:
        if current_height >= max_height:
            bounding_height = min(current_height, max_height)
            pocket_collected = 0
            while stack and stack[-1] < bounding_height:
                pocket_height = stack.pop()
                pocket_collected += bounding_height - pocket_height
            collected += pocket_collected if stack else 0
            max_height = current_height
            stack = [max_height]
        else:
            stack.append(current_height)
    stack.reverse()
    return stack, collected


class Solution:
    def trap(self, height: List[int]) -> int:
        stack, forward_collected = evaluate(height)
        _, backwards_collected = evaluate(stack)
        return forward_collected + backwards_collected


s = Solution()
cases = [
    ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
    ([4, 2, 0, 3, 2, 5], 9),
    ([1, 1, 1, 1, 1], 0),
    ([1, 2, 3, 4, 5], 0),
    ([5, 4, 3, 2, 1], 0),
    ([5, 4, 3, 2, 5], 6),
    ([5, 2, 3, 4, 5], 6)
]
for input_args, expected in cases:
    actual = s.trap(input_args)
    assert expected == actual, f"{input_args}, {expected} != {actual}"
