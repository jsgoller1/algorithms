from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    if not prices:
        return 0.0
    max_so_far = min_so_far = prices[-1]
    best_so_far = 0.0

    for price in prices[::-1]:
        min_so_far = min(min_so_far, price)
        best_so_far = max(best_so_far, max_so_far-min_so_far)
        if price > max_so_far:
            min_so_far = max_so_far = price 

    return best_so_far


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
