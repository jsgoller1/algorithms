"""
You are given coins of different denominations and a total amount of money amount.
Write a function to compute the fewest number of coins that you need to make up
that amount. If that amount of money cannot be made up by any combination of the
coins, return -1.

Example 1:
Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:
Input: coins = [2], amount = 3
Output: -1
------------------------------
In: list[int], amount
Out: amount

- Brute force: use backtracking to try each possible combination of coins, starting with the biggest denominations
- Is there a DP solution to this?
  - the fewest coins for N is fewest(N-coin1, N-coin2, N-coin3); we definitely have overlapping subproblems

Cases:
  coins = [1,5,10], N = 15
  fewest = 2 (10 and 5)

  coins = [1,5,10], N = 10
  fewest = 1 (10)

  coins = [1,5,10], N = 14
  fewest = 5 (10,1,1,1,1)

  coins = [5,10], N = 14
  fewest = -1

- 14
  - 9
    - 4
    - X
  - 4
    - X
    - X

- 15
  - 10
    - 5
    - 0
  - 5
    - X
    - 0

 f(N) = min(f(N-c1), f(N-c2), f(N-c3))
-----------------------------------------------------
fewest(coins, N):
  if N <= 0:
    return 0
  return min([f(N-coin)+1 for coin in coins])

- Works, except if no possible coins can be made; maybe we want to say if N < 0, return -1,
but if N == 0, return 1?
- Have to be careful with our min then


- If N < 0, return -1
- If N = 0, return 0
- Otherwise, return the minimum of f(N-coin)+1 for each coin, assuming the result is positive
- If there's nothing in the above, return -1

"""


class Solution:
    def coinChange(self, coins, amount):
        """
        I saw something like this bottom-up approach in the LC discussions
        and it seems like the quickest way to solve the problem.
        """
        cache = [0] + [float('inf')] * amount
        for val in range(1, amount + 1):
            cache[val] = min([cache[val - coin] if val - coin >= 0
                              else float('inf') for coin in coins]) + 1

        if cache[amount] == float('inf'):
            return - 1
        return cache[amount]


class WorkingSolution:
    """
    Despite being nearly identical to TopDownSolution below,
    this solution tends to pass without TLE, whereas the other one
    doesn't
    """

    def coinChange(self, coins, amount):
        self.cache = {}
        self.getWays(coins, amount)
        return self.cache[amount]

    def getWays(self, coins, amount):
        if amount in self.cache:
            return self.cache[amount]
        if amount <= 0:
            self.cache[amount] = amount
            return self.cache[amount]

        ways = []
        for coin in coins:
            way = self.getWays(coins, amount - coin) + 1
            if 0 < way:
                ways.append(way)

        if not ways:
            self.cache[amount] = -1
        else:
            self.cache[amount] = min(ways)
        return self.cache[amount]


class TopDownSolution:
    """
    This would work in an interview but fails due to timeouts,
    and I'm not entirely sure why since the above one uses list concatenation
    """

    def coinChange(self, coins, amount):
        self.cache = {}
        self.getWays(coins, amount)
        return self.cache[amount]

    def getWays(self, coins, amount, spaces=0):
        if amount in self.cache:
            return self.cache[amount]
        if amount <= 0:
            self.cache[amount] = amount
        else:
            fewest = float('inf')
            for coin in coins:
                count = self.getWays(coins, amount - coin)
                if count >= 0:
                    fewest = min(fewest, count)

            if fewest == float('inf'):
                self.cache[amount] = -1
            else:
                self.cache[amount] = fewest + 1

        return self.cache[amount]


if __name__ == '__main__':
    s = Solution()
    assert s.coinChange([1, 2, 5], 11) == 3
    assert s.coinChange([2], 3) == -1
    assert s.coinChange([1], 0) == 0
    assert s.coinChange([1, 2, 5], 100) == 20
    print(s.coinChange([70, 177, 394, 428, 427, 437,
                        176, 145, 83, 370], 7582))
