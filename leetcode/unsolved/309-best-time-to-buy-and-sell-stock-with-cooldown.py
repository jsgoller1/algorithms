"""
Statement:

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions
as you like (i.e., buy one and sell one share of the stock multiple times) with the
following restrictions:

- You may not engage in multiple transactions at the same time (ie, you must sell the
stock before you buy again).
- After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)

Example:
Input: [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]
----
Understand

This problem calls for finding the maximum value we can obtain
by starting with a zero total and walking an array by either adding the value
we see (selling) or subtracting it from the total (buying).
- We cannot add it to the total unless we have previously subtracted it (not explicitly stated, but we cannot sell stock we don't have)
- We cannot subtract immediately after we add (buy right after a sell).
- We cannot own more than one share of stock at once (consecutive buy not allowed)

Regardless of the fact that this is presented as a DP problem for Bradfield,
I feel like there is probably some DP-like recursive algorithm for this -
the maximum value for an n-array can probably be derived from an n-1 array.

How can we frame the problem such that we only need to know the outcome of the previous step (or a fixed number
of previous state)?

Base cases:
  [1] -> 0 (cannot sell)
  [2,3] -> 1 (buy and then sell iff array[0] < aray[1])
  [4,3] -> 0 (buy and then sell iff array[0] < aray[1])

Recursive solution for element n:
  if n-1 is a sell:
    if n > n-1:
      change n-1 to hold
      sell on n
    else:
      hold on n
  if n-1 is a buy:
    if n < n-1:
      hold on n
    if n = n-1:
      hold on n
    if n > n-1:
      sell on n
  if n-1 is a hold:
    if not last in array:
      buy on n
    else:
      hold on n

Except,

- "Buy and hold out for the best sell" fails some cases
[1,2,3,0,2] -> 3
Correct: B S H B S -> 1 + 2 = 3
Actual:  B H S H H -> 2 = 2

- "Buy and sell immediately" fails some cases
        [1,2,7,0,2] ->
Correct: B H S H H  -> 6 = 6
Actual:  B S H B S  -> 1 + 2 = 3
----------
P
E
R
"""
