"""
There are N gas stations along a circular route, where the amount of gas at station i is gas[i]. You have
a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station
(i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once in the clockwise direction,
otherwise return -1.

Note:
- If there exists a solution, it is guaranteed to be unique.
- Both input arrays are non-empty and have the same length.
- Each element in the input arrays is a non-negative integer.

Example 1:
Input:
gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]
Output: 3

Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.

Example 2:
Input:
gas  = [2,3,4]
cost = [3,4,3]
Output: -1
Explanation:
You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 0. Your tank = 4 - 3 + 2 = 3
Travel to station 1. Your tank = 3 - 3 + 3 = 3
You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
Therefore, you can't travel around the circuit once no matter where you start.

-------
- In: list[int], list[int]
- Out: int

- Brute force: try every possible starting station; O(n^2)
- Is there some way we can examine each station once, and
find some pattern / fact about the circuit that makes it impossible?
- What if we subtract the cost of the station from its gas cost? This
should allow us to produce a weighted graph, O(n):
gas   = [2,  3,  4]
cost  = [3,  4,  3]
edges = [-1, -1, 1]

gas   = [1,   2,  3, 4, 5, 2]
cost  = [3,   4,  5, 1, 1, 1]
edges = [-2, -2, -2, 3, 4, -1]

- With this, we can start seeing where the optimal starting point would be
- if the sum of all edges in the array is negative, it is unsolvable.
  - is this always true? Can we permute the 5 element array to make it unsolvable?
  - [-2,  3, -2, -2, 3]
  - Can't think of an obvious counterexample
- We always drive from left to right til we return to our index (use mod)
- The sum of the array, if solvable, is zero no matter where we start in it.
- do a left to right and right to left walk summing total gas; pick index where total is highest?
  - [-2, -2, -2, 3, 4, -1], highest r to l at 3
    - as long as they're in the same order with each other, doesn't matter what actual order they're in
    - [-3, 7,-3, 2, -3]
    - [2, 4, -2, -2, 1, -1]
    - [2,-2,2,-2]
- is there ever a reason why picking the index with the highest current gas is wrong?
- what are we trying to do here?
  - pick index where visiting every other stop back to it is maximized? (well, nonzero, but should only be one)
  - what if we thought of it as a ring; leftmost/rightmost heuristics shouldn't have to apply.
----------------------------------------
Not super sure if this is the best way, but:

- generate edges list by subtracting cost from gas
- if sum(edges) < 0, return -1
- otherwise, walk from right to left and keeping track of max current gas
- return index with highest current gas
"""


class Solution:
    def canCompleteCircuit(self, gas, cost):
        edges = [gas - cost[i] for i, gas in enumerate(gas)]
        if sum(edges) < 0:
            return - 1

        max_gas = -float('inf')
        curr_gas = 0
        max_gas_i = 0
        for i in range(len(edges) - 1, -1, -1):
            curr_gas += edges[i]
            if curr_gas > max_gas:
                max_gas_i = i
                max_gas = curr_gas
        return max_gas_i


if __name__ == '__main__':
    s = Solution()
    assert s.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]) == 3
    assert s.canCompleteCircuit([2, 3, 4], [3, 4, 3]) == -1
