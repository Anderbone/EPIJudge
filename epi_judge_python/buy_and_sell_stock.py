from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    max_profit = 0
    buy_min = prices[0]
    for i in range(1, len(prices)):
        if prices[i] < buy_min:
            buy_min = prices[i]
        elif prices[i] > buy_min:
            if prices[i] - buy_min > max_profit:
                max_profit = prices[i] - buy_min
    return max_profit


# def buy_and_sell_stock_once(prices: List[float]) -> float:
#     # this is infinite times
#     profit = 0
#     for i in range(len(prices)-1):
#         first = prices[i]
#         second = prices[i+1]
#         if second > first:
#             profit += second - first
#     return profit

# def buy_and_sell_stock_once(prices: List[float]) -> float:
#     # TODO - you fill in here.
#
#     mini = prices[0]
#     maxp = 0
#     for cur in prices:
#         if cur < mini:
#             mini = cur
#         else:
#             profit = cur - mini
#             maxp = max(maxp, profit)
#
#     return maxp
#     # return 0.0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
