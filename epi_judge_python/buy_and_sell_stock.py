from test_framework import generic_test


def buy_and_sell_stock_once(prices):
    # TODO - you fill in here.

    mini = prices[0]
    maxp = 0
    for cur in prices:
        if cur < mini:
            mini = cur
        else:
            profit = cur - mini
            maxp = max(maxp, profit)

    return maxp
    # return 0.0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock.py",
                                       "buy_and_sell_stock.tsv",
                                       buy_and_sell_stock_once))
