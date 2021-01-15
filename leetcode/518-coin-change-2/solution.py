"""
You are given coins of different denominations and a total amount of money. Write
a function to compute the number of combinations that make up that amount. You may
assume that you have infinite number of each kind of coin.

Constraints:
    - Amount between 0 and 5000, coins between 1 and 5000
    - less than 500 coins
    - answer will be smaller than 2**32-1
 -----------------------------------------------------------
Solved this problem with DP before; need to remember how.
Does the problem have optimal substructure (optimal solutions can be obtained from optimal subsolutions)
or overlapping substructure (different answers will reuse the same subproblems)?

Strategy of "all the ways to make 10 minus 1 penny, minus 1 dime, and minus 1 nickle" fails because
of overlapping subproblems:
    10: all for 9 plus penny (2), all for 5 plus nickle (2), all for 0 plus dime (1)
        0: d
        5: n + n, 5p + n
        9: [n 4p + p], [9p + p]
    Strategy breaks at 10 with two cases of 5p + n; overlapping subproblems 


How do we rule out overlapping subcases? Need to ensure that if we already have 5p + 1d that 1d + 5p doesn't get counted.
When elliott and I did this, didn't we eliminate coins instead of committing to using them?
Ways to make 10 using d,n,p = ways to make 5 using d,np + ways to make 10 using n,p?

Left subtree: make new amount minus largest denomination
Right subtree: make same amount without largest denomination 
Caching - can occur for amount/coin pairs. 

Why does this work? Eliminates overlapping subproblems - how? In above example,
coin elimination means we only find "get to 5 via a nickle" in one path.
------------------------
base case: amount is 0 (found a valid way), or we have no coins (not valid). 
(sort and order coins, greatest-to-least)

def change(amt, coins):
    if not coins or amt < 0:
        return 0
    if amt == 0:
        return 1
    return change(amt - coins[0], coins) + change(amt, coins[1:])

(above is going to do a ton of extra work; let's make sure strategy works first tho)

"""

from collections import namedtuple
from typing import List, Tuple

TestCase = namedtuple('TestCase', ['name', 'amount', 'coins', 'expected'])


class Solution:
    def recurse(self, amt: int, coins: Tuple[int]) -> int:
        if (amt, coins) in self.cache:
            return self.cache[(amt, coins)]
        if not coins or amt < 0:
            return 0
        if amt == 0:
            return 1

        self.cache[(amt, coins)] = self.recurse(amt - coins[0], coins) + self.recurse(amt, coins[1:])
        return self.cache[(amt, coins)]

    def change(self, amt: int, coins: List[int]) -> int:
        self.cache = {(0, ()): 1}
        return self.recurse(amt, tuple(coins))


if __name__ == '__main__':
    s = Solution()
    test_cases = [
        TestCase('Ex 1', 5, [1, 2, 5], 4),
        TestCase('Ex 2', 3, [2], 0),
        TestCase('Ex 3', 10, [10], 1),
        TestCase('Failed 1', 0, [], 1),

    ]
    for case in test_cases:
        actual = s.change(case.amount, case.coins)
        assert actual == case.expected, f"{case.name} - {case.amount}, {case.coins}: {case.expected} != {actual}"
