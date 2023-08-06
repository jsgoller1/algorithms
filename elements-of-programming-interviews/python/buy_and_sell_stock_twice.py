from typing import List

from test_framework import generic_test


def buy_and_sell_stock_twice(prices: List[float]) -> float:
    """
    On every day given the stock price, we can do one of 5 things:
    1) Sell 2nd share. Profit: profit from 2nd buy + price. 
    2) Buy 2nd share. Profit: profit from first sale - price.
    3) Sell 1st share. Profit: price - lowest price so far. 
    4) Buy 1st share. Profit: -price.
    5) Nothing so far. Profit: 0.

    To get the best possible sale for each, use the max function. The ordering we do the updates in actually doesn't
    matter and still produces the correct result for the tests; however, the since the best second sell day depends
    on the best second buy day, which in turn depends on the best first sell day, the order should be first_buy -> first_sell ->
    second_buy -> second_sell.
    """
    first_buy = -float('inf')
    first_sell = 0
    second_buy = -float('inf')
    second_sell = 0

    for price in prices:
        first_buy = max(first_buy, -price)
        first_sell = max(first_sell, price + first_buy)
        second_buy = max(second_buy, first_sell - price)
        second_sell = max(second_sell, second_buy + price)

    return second_sell


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock_twice.py',
                                       'buy_and_sell_stock_twice.tsv',
                                       buy_and_sell_stock_twice))
