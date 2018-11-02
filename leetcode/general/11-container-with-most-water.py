"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai),
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).

Translation: in the given array, the values are the heights of the lines. (see picture)

Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

Example:
Input: [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: There are 6 partitions in between in[1] (8) and in[-1] (7); as such, there are 7 columns that could be filled with water. Because
7 is lower of the two, we can fill 7 columns with 7 units of water (imagine the intermediary lines are very porous and take up no space themselves)
resulting in 49.

Constraints:
  - You cannot "slant" the container (i.e. have a diagonal water surface maybe?)
  - n >= 2
----------------------------
Cases:
  1: [1, 8, 6, 2, 5, 4, 8, 3, 7]          (pick arr[1] and arr[-1])
  2: [2, 1, 8, 6, 2, 5, 4, 8, 3, 7, 1, 2] (pick arr[2] and arr[-3])
  3: [1, ..., 99, 1, 1, 99, ..., 1]       (pick 8s)
  4: [1, 1, 1, 1, 1]                      (pick first and last)
  5: [1,1,1,1,1,1,2,2]                    (pick first and last)
  6: [5,1,10,1,10,1,5]                    (pick outermost 5s)
  7: [4,1,10,1,10,1,4]                    (pick outermost 4s - 24)

- Brute force:
  - count the amount of water for every possible combination O(n^2)
- Trapping Rainwater can be done in O(N) time by using a stack, but that catches _all_ rainwater.
  - Also, doing the two-passes with the stacks would give us the two 8-height lines, which is wrong
- Do we need to examine every pair?
  - Probably not; we should be able to reach a point where "this could never be greater"
  - Can't sort
- We do need to look at every line at least once
- If we pick two lines, there is no way to catch more water by picking any lines in between that are shorter; could by picking greater.
  - if we pick the two maxes, we don't need to look any further inwards for better lines
  - what do we need to do so we know we don't need to look outwards? Is there a way to quickly disqualify remaining elements
- Suppose we've picked the maxes in [...,20,...21,10,7,8,9], which are 10 and 11. If we want to pick the correct rightmost line, there is no reason to pick any line
with a taller/equal line to its right; 7 and 8 cannot be the correct answer. Same logic applies to other side as well. Cases:


"Two pointers" approaches:
- What if starting at outermost, we determine if moving either inwards results in a better solution?
  - Would fail on case #2

- Start in the middle and work outwards
  - [1, 8, 6, 2, 5, 4, 8, 3, 7]
                 5, 4
                   [4, 10,12,16]  right edge given left is 5
    [5  16 12 4  4]               left edge given right is 4

  - correct on case #1
  - Would break on case #3
- Start with the array maxes and work outwards
  - correctly does cases 1-5
  - Could this strategy be tricked into picking the wrong elements?
    - Fails #7
       max is 24 with outermost 4s, but strategy picks 20 with two 10s.
- Start with outermost and look no further inwards than maxes; only replace if we find a boundary that is better than the outermost
    - passes 1,4-7, fails 2 and 3
- Obtain maxes, and then return the highest amount of water from four passes
  - leftmost element, inwards from rightmost
  - left max, inwards from rightmost
  - rightmost element, inmost from leftmost
  - right max, inward from leftmost
  - passes
"""
