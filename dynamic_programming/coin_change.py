"""
🟡 Coin Change
Find the minimum number of coins to make up a given amount.

Time:  O(amount * len(coins))
Space: O(amount)
"""


def coin_change(coins: list[int], amount: int) -> int:
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[amount] if dp[amount] != float("inf") else -1


def coin_change_ways(coins: list[int], amount: int) -> int:
    """Count the number of ways to make change."""
    dp = [0] * (amount + 1)
    dp[0] = 1
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]
    return dp[amount]


if __name__ == "__main__":
    print(coin_change([1, 5, 10, 25], 36))     # 3
    print(coin_change([2], 3))                   # -1
    print(coin_change_ways([1, 5, 10, 25], 36))
