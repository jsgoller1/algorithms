"""
Statement: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions
as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
on is done, i.e. max profit = 0.

----
Understand

Note that the question is purely asking about the maximum amount, not the
best action to take each day. This is possibly a clue that we don't need to
store information about every previous day (also, I've gotten a shoddy
linear-space, constant time solution to this before, but I have seen
a constant-time sketched out). What can we do to remove the need to
know _every_ previous possible day's action?

We can think of this as a state machine:
Bought -> Sold, Held
Sold -> Bought, Held
Held -> Bought, Sold, Held

Some cases:
[1,2] -> 1 (buy, sell)
[4,3,2] -> 0 (hold, hold, hold)
[1,2,7] -> 6 (buy, hold, sell)
[1,0,4] -> 4 (hold, buy, sell)
[4,1,6,1,7] 11 -> (hold, buy, sell, buy, sell)
[1,2,2,2] -> 1 (buy, hold, hold, sell)

Does knowing what the best thing to do yesterday was
help us know what the best thing to do today is? At any
intermediary step, we should NOT need to look back through
every element of the array. Can we come up with a situation
where an intermediary (or a solved array with a new element added)
forces us to change any more than a contant number of previous decisions?

- Suppose we have a solution for an n-element array that
involves selling on the last day; adding another element
will not affect what day we should buy on.
    - If we add an element lower than the last, do nothing.
    - If we add an element higher than the last, sell on that day instead.

Example: [4,2,5] vs [4,2,5,7]
- Instead of selling on 5, we sell on 7
Example: [4,2,5] vs [4,2,5,1]
- Still sell on 5

- Suppose we have a solution for an n-element
array where we sell before the last day, and we add another element.
    - If the new element is higher than the last one, old hold becomes
    a buy, new element is a sell.
    - Otherwise, new element is a hold as well
[2,7,4] vs [2,7,4,9]
    - Instead of holding on 4, buy on 4 and sell on 9. Still buy on 2 and sell on 7
[2,7,4] vs [2,7,4,1]
    - Still buy on 7, sell on 2, hold on 4, and now hold on 1 as well.

- Can we come up with a situation that forces non-constant amount of backtracking?
[2,4,5] -> [2,4,5,6] only backtrack one (sell on 6 instead of 5)
        -> [2,4,5,4] no backtracking

[2,4,3] -> [2,4,3,4] only backtrack one (buy on 3 instead of holding, sell on second 4)
        -> [2,4,3,2] no backtracking

[4,3,2] -> [4,3,2,3] backtack once (buy on 2 instead of hold, sell on 3)
        -> [4,3,2,1] no backtracking

[2,4,3,4] -> [2,4,3,4,5] backtrack once
          -> [2,4,3,4,2] no backtracking

What about thinking about it from the perspective of the n, n-1, and n-2 days (since we have 3 possible states)?
    - Asking this led me to the pseudocode in the Plan section.

----
Plan

Initialize with B, ?

if S, ?:
    S > ?:
        ? -> B
    S <= ?:
        S -> H
        ? -> S
if B, ?:
    if B > ?:
        B -> H
        ? -> B
    if B <= ?:
        ? -> S
if H, ?:
    if H >= ?:
        ? -> H
    if H < ?
        ? -> S

if last item is B, swap to H

----
Execute

See below
----
Review

O(n) for time, O(c) for space, beats 60% of other submissions.
"""


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0

        total = 0 - prices[0]
        prev = 'b'
        for i in range(1, len(prices)):
            if prev == 's':
                if prices[i - 1] > prices[i]:
                    total -= prices[i]
                    prev = 'b'
                else:
                    total -= prices[i - 1]
                    total += prices[i]
            else:
                if prices[i - 1] > prices[i]:
                    total += prices[i - 1]
                    total -= prices[i]
                else:
                    total += prices[i]
                    prev = 's'

        # Don't buy on the last day.
        if prev == 'b':
            total += prices[-1]

        print("{0}: {1}".format(prices, total))
        return total


if __name__ == '__main__':
    s = Solution()
    assert s.maxProfit([]) == 0
    assert s.maxProfit([1]) == 0
    assert s.maxProfit([1, 0]) == 0
    assert s.maxProfit([1, 5]) == 4
    assert s.maxProfit([1, 5, 4]) == 4
    assert s.maxProfit([5, 4, 1]) == 0
    assert s.maxProfit([1, 1, 1]) == 0
    assert s.maxProfit([1, 3, 3, 7]) == 6
    assert s.maxProfit([7, 1, 5, 3, 6, 4]) == 7
