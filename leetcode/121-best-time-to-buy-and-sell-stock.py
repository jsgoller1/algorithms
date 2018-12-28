"""
Say you have an array for which the ith element is the price of a
given stock on day i. If you were only permitted to complete at
most one transaction (i.e., buy one and sell one share of the stock),
design an algorithm to find the maximum profit. Note that you cannot
sell a stock before you buy one.

Example 1:
Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.

Example 2:
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

Ex. 3:
Input: [7,2,7,3,1,9]
Out: 8
Exp: Best idea is buy at 1, sell at 9
--------------------------------------------------------------------------
In: list[int]
Out: int

- I picked this from list of DP questions, so I already know that's the right approach.
- What is the recurrence here?
  - best(7 days) = best(6 days) + if we can sell on day 7
  - best(6 days) = best(5 days) + if we can sell on day 6

- for 2 days: buy on first, sell on second
- for 3 days, buy on first, sell second or buy on first, sell third, or buy second, sell third

- What if at every step, we either use it as the sell day, or as the new buying day.
- in example 1 above: [7,1,5,3,6,4]
  - initial buy is day[0]
  - initial sell is day[1]
  - initial best is day[1] - day[0]
  - evaluate arr[2]:
    - move buy to 1 (1)
    - move sell to 2 (5)
  - evaluate arr[3]:
    if sell is higher, move sell
    if buy is lower, we only want to move it if we can be certain there's
    a better sell coming
      - actually, we only need to update best if that happens.
-----------------------------
profit(prices):
  buy = 0
  sell = 1
  best = prices[sell] - prices[buy]
  for i in range(1, len(prices)-1):
    if prices[i] > sell:
      sell = i
    if prices[i] < buy:
      buy = i
      sell = i+1
    best = max(best, prices[sell] - prices[buy])

"""


class Solution:
    def maxProfitFirst(self, prices):
        if len(prices) < 2:
            return 0
        buy = 0
        sell = 1
        best = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[sell]:
                sell = i
            if prices[i] < prices[buy] and i < len(prices)-1:
                buy = i
                sell = i+1
            best = max(best, prices[sell] - prices[buy])
        return best

    def maxProfit(self, prices):
        profit = 0
        if prices:
            buy = prices[0]
            for i, price in enumerate(prices):
                buy = price if price < buy else buy
                profit = price-buy if price - buy > profit else profit
        return profit


if __name__ == '__main__':
    s = Solution()
    assert s.maxProfit([7, 1, 5, 3, 6, 4]) == 5
    assert s.maxProfit([7, 6, 4, 3, 1]) == 0
    assert s.maxProfit([7, 2, 7, 3, 1, 9]) == 8
    assert s.maxProfit([1, 2, 4]) == 3
    assert s.maxProfit([]) == 0
