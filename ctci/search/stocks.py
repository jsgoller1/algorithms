import random

"""
Assume that an array stores the various stock prices of FooBar Inc over n days
at market open, where array[m] is the openingprice of FooBar Inc. on day m.
Write a program that finds the maximum posssible profit from buying and
selling a single share of FooBar Inc stock. You must buy before you sell.
(Elements of Programming Interviews, Introduction)

Solution: Brute forcing would require us to compare every price in the array to
every other price, which is O(n^2) and therefore unsatisfactory. A O(n) solution
(implemented) can be obtained by walking through the array once, keeping track
of the minimum possible price and best revenue so far, updating the revenue when
the current price minus current min exceeds the previous maximum profit, and the
minimum when new minimums are found.

(Code adapted from InterviewCake.com, with some additions)
"""

def get_best_profit(prices):
    print prices
    min_price = prices[0]
    max_profit = best_sell = best_buy = 0
    for current_price in prices:
        min_price = min(min_price, current_price)
        if (max(max_profit, current_price - min_price) != max_profit):
            max_profit = current_price - min_price
            best_buy = min_price
            best_sell = current_price
    print "Maximum profit: " + str(max_profit)
    print "Best buying price: " + str(best_buy)
    print "Best selling price:" + str(best_sell)

get_best_profit([random.randint(0,200) for x in range(0,40)])
