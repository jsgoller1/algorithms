"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell
one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:
Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.

Example 2:
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

Constraints:
    - None given

Cases:
    - Top price before lowest
    - Every day is a loss (given case 2)
-------------------
On each day, the highest day after it minus that day is the best possible transaction (or 0):
Day:          [7, 1, 5, 3, 6, 4]
Best after:   [X, 6, 6, 6, X, X]
Best profit:  [0, 5, 1, 3, 0, 0]
Answer: 5

Can we go r-to-l, keeping track of maxes and best sales?

best_profit = 0
best_price = 0
for price in prices[::-1]:
    best_price = max(price, best_price)
    best_profit = max(best_profit, best_price-price)
return best_profit 
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_profit = 0
        best_price = 0
        for price in prices[::-1]:
            best_price = max(price, best_price)
            best_profit = max(best_profit, best_price-price)
        return best_profit


if __name__ == '__main__':
    cases = [
        ([7, 1, 5, 3, 6, 4], 5),  # buy on 1, sell on 6
        ([7, 6, 4, 3, 1], 0)  # No possible day to make a profit
    ]

    sol = Solution()
    for prices, expected in cases:
        actual = sol.maxProfit(prices)
        assert expected == actual, f"{expected} != {actual}"
