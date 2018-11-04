"""
Statement:

We have two types of tiles: a 2x1 domino shape, and an "L" tromino shape.
These shapes may be rotated.

XX  <- domino

XX  <- "L" tromino
X

Given N, how many ways are there to tile a 2 x N board? Return
your answer modulo 10^9 + 7.

(In a tiling, every square must be covered by a tile. Two tilings
are different if and only if there are two adjacent (U/D/L/R)
cells on the board such that exactly one of the tilings has both
squares occupied by a tile.)

Example:
Input: 3
Output: 5

Explanation:
The five different ways are listed below, different letters indicates different tiles:
XYZ XXZ XYY XXY XYY
XYZ YYZ XZZ XYY XXY
Note:

N  will be in range [1, 1000].

(I am still learning how to solve DP problems,
so I looked at this answer after about 40 minutes:
https://leetcode.com/problems/domino-and-tromino-tiling/discuss/116581/Detail-and-explanation-of-O(n)-solution-why-dpn2*dn-1%2Bdpn-3)

------
Understand / Plan

Input: N, (for size of board, 2 x N)
Output: int N, number of ways to tile the board

This feels like it's going to be a DP problem:
 - Only need to return N, not every combinaion
 - Once we know N-1, we know N.

Thinking about some base cases:
2 x 1: 1 way:
X
X

2 x 2: 2 ways
XX  XY
YY, XY

2 x 3: 5, shown above.
XYZ XXZ XYY XXY XYY
XYZ YYZ XZZ XYY XXY

2 x 4 can be found by:
- all of 2 x 3, with a single vertical block added (1 choice of new tile, 5 tilings)
- all of 2 x 2, with two horizontal blocks added (1 choice of new tile, 2 tilings; we don't count the 4 verticals because it is handled in all of 2x3 plus a vertical)
- all of 2 x 1, with one of two combinations of triominos (2 choices for new tiles; 2 tilings)
- all of 2 x 0 (assumed zero), with two combinations of two triominos and a domino (2 choices for new tiles; 2 tilings)
total: 11 tilings

Per ZhengkaWei's solution, if we say count(n) is the number of ways to tile a 2 x n grid,
then there is only one way for count(n-1) and count(n-2) to have tiles added to it to become
count(n) - for n-1, only a vertical tile may be added; for n-2, the vertical tile is covered
by a different case so only a horizontal tile may be added, which necessitates using a second
horizontal tile. n-3 can support a triomino and therefore has 2 separate ways that new tilings can occur.

Also from the solution:
dp[n] = dp[n-1] + dp[n-2] + 2*(dp[n-3]+...+d[0])
dp[n-1] = dp[n-2] + dp[n-3]+ 2*(dp[n-4]+…+d[0])
so,
// factor out two dp[n-3]
dp[n] = dp[n-1] + dp[n-2] + dp[n-3] + dp[n-3] + 2*(dp[n-4]+...+d[0])

// re-arrange operands
dp[n] = dp[n-1] + dp[n-3] + (dp[n-2]+dp[n-3]+2*(dp[n-4]+...+d[0]))

// change last terms to dp[n-1]
dp[n] = dp[n-1] + dp[n-3] + dp[n-1]

// simplify by grouping like terms
dp[n] = 2*dp[n-1] + dp[n-3]

---
Execute

See code below.
----
Review
"""


class Solution(object):
    def __init__(self):
        self.cache = {0: 0, 1: 1, 2: 2, 3: 5}

    # top-down approach; at the time of writing, this beats 43% of solutions
    """
    def numTilings(self, n):
        if n in self.cache:
            return self.cache[n]
        else:
            self.cache[n] = (2 * self.numTilings(n-1) +
                             self.numTilings(n - 3)) % ((10**9)+7)
            return self.cache[n]
    """

    # bottom up approach; at time of writing, this beats 83% of solutions
    def numTilings(self, n):
        if n in self.cache:
            return self.cache[n]
        i = 4
        while (i <= n):
            self.cache[i] = (2 * self.numTilings(i-1) +
                             self.numTilings(i - 3)) % ((10 ** 9) + 7)
            i += 1
        return self.cache[n]


if __name__ == '__main__':
    s = Solution()
    assert s.numTilings(3) == 5
    assert s.numTilings(4) == 11
    assert s.numTilings(5) == 24
    assert s.numTilings(30) == 312342182
