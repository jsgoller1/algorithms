"""
Statement: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

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
----
Understand

See cooldown version.
----
Plan

actions = [H] * len(input)
For first two elements:
  - if 0 > 1:
    Begin with [H, B]
  if 1 > 0:
    Begin with [B, S]

Then starting at n=1 until end:
  if N < N+1:
    if actions[N] == S:
      swap(actions[N], actions[N+1])
    if actions[N] == B:
      actions[N+1] = S
  if N > N+1:
    if actions[N] == B:
      swap(actions[N], actions[N+1])
    if N == S:
      actions[N+1] = B
if actions[-1] == B, set to H

----
Execute
----
Review
"""


def solver_actions(prices):
    actions = ['B'] + (['H'] * (len(prices)-1))
    for i in range(len(prices) - 1):
        if prices[i] < prices[i + 1]:
            if actions[i] == 'S':
                actions[i], actions[i+1] = actions[i+1], actions[i]
            elif actions[i] == 'B':
                actions[i + 1] = 'S'
        if prices[i] > prices[i + 1]:
            if actions[i] == 'B':
                actions[i], actions[i+1] = actions[i+1], actions[i]
            if actions[i] == 'S':
                actions[i + 1] = 'B'
    if actions[-1] == 'B':
        actions[-1] = 'H'
    return actions


def solver(prices):
    total = 0
    for i in range(len(prices) - 1):
        if prices[i] < prices[i + 1]:
            if actions[i] == 'S':
                actions[i], actions[i+1] = actions[i+1], actions[i]
            elif actions[i] == 'B':
                actions[i + 1] = 'S'
        if prices[i] > prices[i + 1]:
            if actions[i] == 'B':
                actions[i], actions[i+1] = actions[i+1], actions[i]
            if actions[i] == 'S':
                actions[i + 1] = 'B'
    if actions[-1] == 'B':
        actions[-1] = 'H'
    return actions


if __name__ == '__main__':
    print(solver([7, 1, 5, 3, 6, 4]))
    print(solver([7, 6, 4, 3, 1]))
