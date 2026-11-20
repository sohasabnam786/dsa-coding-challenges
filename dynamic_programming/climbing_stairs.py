"""
🟢 Climbing Stairs
You can climb 1 or 2 steps. How many distinct ways to reach the top?

Time:  O(n)
Space: O(1)
"""


def climb_stairs(n: int) -> int:
    if n <= 2:
        return n
    prev2, prev1 = 1, 2
    for _ in range(3, n + 1):
        curr = prev1 + prev2
        prev2 = prev1
        prev1 = curr
    return prev1


def climb_stairs_memo(n: int) -> int:
    memo = {}
    def dp(i):
        if i <= 2:
            return i
        if i in memo:
            return memo[i]
        memo[i] = dp(i - 1) + dp(i - 2)
        return memo[i]
    return dp(n)


if __name__ == "__main__":
    for i in range(1, 11):
        print(f"n={i}: {climb_stairs(i)} ways")
