import collections

"""
Statement (https://leetcode.com/problems/trapping-rain-water/description/):

Given n non-negative integers representing an elevation map where the width
of each bar is 1, compute how much water it is able to trap after raining.
(see leetcode for a diagram)

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
---
Understand

- The middle value must be less than the adjacent values
for the water to be trapped:

      X
X     X
X X   X   X
2 1 0 3 0 1
(4 units trapped)

    X X
X X X X
X X X X X X
2 2 3 3 1 1
(0 units trapped)

X
X
X   X
X   X X   X
4 0 2 1 0 3
(3 units trapped)


- Could we go through the array L-to-R until we find a value that is followed by a lower value and
can thus serve as a legitimate left-edge of a trap?

- Heuristics:
  - DP?
    - Unlikely? We don't really have obvious "overlapping subproblems" - what we find out in a different
    part of the problem could change the outcome of what we found in an earlier part.
  - Divide and conquer?
---
Plan

- A brute force approach - O(n*m) for an n element array with second-highest element m:
  - Total rainwater = 0
  - loop through the array until one or less elements are positive:
    - add 1 to total rainwater for each zero or negative value observed
    - decrement each element

- Graph search - O(n*m) for an n element array with max element m:
  - Find the maximum element in the array, called m
  - Initialize an m-by-n matrix
  - Draw the above histogram in the Understand section within the matrix
  - Starting from the top-most, left-most cell, BFS the matrix, halting at any cell with an X
  - Count the number of nodes visited

- Linear time approach - O(n) for n element array
  - total = 0
  - Perform a first pass of the following algorithm, traversing the array left to right
    - max element = 0
    - initialize an empty stack
    - for each element in the array:
      - if current < max element so far:
        - stack.push(current)
      - else (we saw a height >= our current max)
        - calculate all of the space between the new height and our previous max that would be filled by water:
          - distance from each column * height of smaller column
          - remove space occupied by blocks in between
          - total += (number of items popped * min(previous max, current) - (sum items popped))
        - Set max element to current height
    - return total and the stack, prepending our max element back to it if it is nonempty
      - the prepending is necessary for the following pass to work correctly.
  - If the stack is empty after the pass, return total
    - otherwise, repeat the algorithm using the unexamined contents of our stack in reverse order
    - add new total to previous total and return

-------
Execution

See below.

----
Review

Forthcoming.
"""


def print_grid(array):
    """
    Print heights as a histogram for
    enhanced eyeballing.
    """
    height = 1
    levels = []
    for _ in range(max(array)):
        level = ""
        for each in array:
            if each < height:
                level += "  "
            else:
                level += "X "
        levels.append(level)
        height += 1
    for level in levels[::-1]:
        print(level)


class Solution:
    def array_pass(self, heights):
        """
        Walk over array in one pass, performing the procedure described above.
        """
        max_height = 0
        total = 0
        stack = collections.deque()
        for height in heights:
            if height < max_height:
                stack.append(height)
            else:
                total += (max_height * len(stack)) - sum(stack)
                stack.clear()
                max_height = height

        # If our stack is nonempty, we will have to
        # go over it in reverse, so we need to add
        # our previously seen max height back to it.
        if stack:
            stack.appendleft(max_height)
        return total, stack

    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int

        Entrypoint for solution.
        """
        total, stack = self.array_pass(height)
        if stack:
            remaining, _ = self.array_pass(reversed(stack))
            total += remaining
        return total


if __name__ == '__main__':
    s = Solution()
    assert s.trap([4, 2, 3]) == 1
    assert s.trap([4, 0, 4]) == 4
    assert s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
    assert s.trap([5, 5, 1, 7, 1, 1, 5, 2, 7, 6]) == 23
