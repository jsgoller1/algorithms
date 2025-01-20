from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once_reversed(prices: List[float]) -> float:
    highest = prices[-1]
    profit = 0.0
    for price in prices[::-1]:
        highest = max(highest, price)
        profit = max(profit, highest-price)
    return profit


def buy_and_sell_stock_once_explicit_min_price(prices: List[float]) -> float:
    lowest_price = float('inf')
    best_profit = 0
    for price in prices:
        lowest_price = min(price, lowest_price)
        best_profit = max(best_profit, price-lowest_price)
    return best_profit


def buy_and_sell_stock_once(prices: List[float]) -> float:
    """
    On every day given the stock price, we can do one of 3 things:
    3) Sell 1st share. Profit: price - lowest price so far. 
    4) Buy 1st share. Profit: -price.
    5) Nothing so far. Profit: 0.

    To get the best possible sale for each, use the max function. 
    """
    first_buy = -float('inf')
    first_sell = 0

    for price in prices:
        first_buy = max(first_buy, -price)
        first_sell = max(first_sell, price + first_buy)

    return first_sell


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
