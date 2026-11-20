"""
🟢 Best Time to Buy and Sell Stock
Find the maximum profit from buying and selling a stock once.

Time:  O(n)
Space: O(1)
"""


def max_profit(prices: list[int]) -> int:
    if not prices:
        return 0

    min_price = float("inf")
    max_profit_val = 0

    for price in prices:
        min_price = min(min_price, price)
        max_profit_val = max(max_profit_val, price - min_price)

    return max_profit_val


if __name__ == "__main__":
    print(max_profit([7, 1, 5, 3, 6, 4]))  # 5
    print(max_profit([7, 6, 4, 3, 1]))      # 0
