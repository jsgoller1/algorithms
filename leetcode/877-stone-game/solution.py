"""
Alex and Lee play a game with piles of stones.  There are an even number of piles
arranged in a row, and each pile has a positive integer number of stones piles[i].

The objective of the game is to end with the most stones.  The total number of
stones is odd, so there are no ties.

Alex and Lee take turns, with Alex starting first.  Each turn, a player takes
the entire pile of stones from either the beginning or the end of the row.
This continues until there are no more piles left, at which point the person
with the most stones wins.

Assuming Alex and Lee play optimally, return True if and only if Alex
wins the game.

Example 1:
Input: [5,3,4,5]
Output: true

Explanation:
Alex starts first, and can only take the first 5 or the last 5.
Say he takes the first 5, so that the row becomes [3, 4, 5].
If Lee takes 3, then the board is [4, 5], and Alex takes 5 to win with 10 points.
If Lee takes the last 5, then the board is [3, 4], and Alex takes 4 to win with 9 points.
This demonstrated that taking the first 5 was a winning move for Alex, so we return true.

Input: Array of ints, representing piles of stones
Output: bool, can Alex win the game.

Constraints
- 2 <= piles.length <= 500
- piles.length is even.
- 1 <= piles[i] <= 500
- sum(piles) is odd.
----------------
- Alex always goes first; he wins every 2-pile game.
- always even number of piles between 2 and 500;
- always at least one stone per pile
- always an odd number of stones
- Players can never tie; there are an odd number of stones split
across an even number of pies so there is no splitting of the piles
that makes them equal
- There are some configurations wherein selecting the max corner pile
is suboptimal:
[1, 4, 10, 4, 1, 1]
Alex: right 1. Lee: left 1.
[4, 10, 4, 1]
Alex: right 1. Lee: either 4.
[4, 10] or [4, 10]
Lee loses.

- When does Lee win? What conditions make the game unwinnable for Alex?
Other than by making suboptimal moves, can Alex ever lose?
  - [1, 2, 1, 1] <- alex wins
  - [2, 1, 1, 1] <- alex wins
  - [2, 2, 2, 1] <- alex wins
  - [2, 3, 3, 1] <- alex wins
  - [2, 3, 1, 3] <- alex wins
  - [1, 1, 4, 3, 1, 1]
    - [1, 4, 3, 1] <- Alex wins

- Alex can never lose; the correct solution is to return True
------------------------------------------------------------
I am furious.
"""


class Solution:
    def stoneGame(self, piles):
        return True


if __name__ == '__main__':
    s = Solution()
    assert s.stoneGame([5, 3, 4, 5]) == True
