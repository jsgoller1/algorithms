"""
You are given coins of different denominations and a total amount of money.
Write a function to compute the number of combinations that make up that amount.
You may assume that you have infinite number of each kind of coin.

Note: You can assume that
- 0 <= amount <= 5000
- 1 <= coin <= 5000
- the number of coins is less than 500
- the answer is guaranteed to fit into signed 32-bit integer

Example 1:
Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1

Example 2:
Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.

Example 3:
Input: amount = 10, coins = [10]
Output: 1
-----------------------------------------------------------------------
In: list[int], int
Out: int

- Hello darkness, my old friend. This problem took me 3 days last time I tried it, and
couldn't do it without help from @robot-dreams
- This problem can be solved with dynamic programming.
- We are looking for the number of ways we can make change, not THE ways we
can make change. Ideally, we shouldn't need to store a set / list / etc
of the ways we can make change
- Can we find the solution by solutions to subproblems? Is the number of ways we make
change for amount a with coins c is the a-c_1 + a-c_2 + a-c_3... for each c_n
< a? For example, to make change for 15 with 1, 5, 10:
- 15 - 1 + coinChange(14)
- 15 - 5 + coinChange(10)
- 15 - 10 + coinChange(5)

- How do we prevent the case where 15-5 picks a dime and 15-10 picks a nickle
so that both end up counting 10 + 5?

- What if we look at subproblems along two axes:
  - ways to make change if we commit to using a given coin
  - ways to make change if we don't use that particular coin
- So with this, say we make change for 15 with 10, 5, 1:
  - make change for 15 with 5, 1
    - make change for 15 with 1
      - 1 way
    - make change for 10 with 5, 1
      - make change for 10 with 1
        - 1 way
      - make change for 5 with 5, 1
        - make change for 5 with 1
          - 1 way
        - make change for 0 with 5,1
          - 1 way (assumed)
  - make change for 5 with 10, 5, 1
    - make change for 5 with 5,1 (it looks like we are possible repeating an already-examined case here, but what we are doing is decomposing the nickle when we started by using a dime; we SHOULD cache this though)
      - make change for 5 with 1
        - 1 way
      - make change for 0 with 5,1
        - 1 way (assumed)
    - can't make change with 10

Brute force answer to 15 with 10, 5, 1:
d + n
n + n + n
n + n + 5p
n + 5p + 5p
5p + 5p + 5p
d + 5p
---------------------------------------------------------------------------
- base cases are:
  - making change for 0 cents; assuming there is only 1 way
  - making change for negative cents; 0 ways
  - making change with only 1 coin; 1 way if coin divides amount, 0 if not

No caching:
coinchange(coins, amount):
  if amount == 0:
    return 1
  if amount < 0:
    return 0
  return coinchange(coins[1:], amount) + coinchange(coins, amount-coins[0])

Caching:
solve(coins, amount, cache):
  if (coins, amount) in cache:
    return cache[(coins,amount)]
  if amount == 0:
    return 1
  if amount < 0:
    return 0
  cache[(coins,amount)] = coinchange(coins[1:], amount) + \
         coinchange(coins, amount-coins[0])
  return cache[(coins,amount)]

coinchange(coins, amount):
  cache = {}
  coins.convert_to_tuple()
  return coinchange(coins, amount, cache)
"""


class Solution:
    def solve(self, coins, amount, spaces=0):
        spaces += 2
        #print(" "*spaces+"Evaluating {0},{1}".format(coins, amount))
        if (coins, amount) in self.cache:
            return self.cache[(coins, amount)]
        if amount == 0:
            return 1
        if len(coins) == 1:
            return not amount % coins[0]  # python hack; True + 0 == 1
        if amount < 0:
            return 0
        self.cache[(coins, amount)] = self.solve(
            coins[1:], amount, spaces) + self.solve(coins, amount-coins[0], spaces)
        return self.cache[(coins, amount)]

    def change(self, coins, amount):
        self.cache = {}
        coins = tuple(coins)
        return self.solve(coins, amount)


if __name__ == '__main__':
    s = Solution()
    assert s.change([1, 2, 5], 5) == 4
    assert s.change([1, 5, 10], 15) == 6
    assert s.change([5, 10], 7) == 0
    assert s.change([3], 3) == 1
