"""
🟡 Longest Increasing Subsequence
Find the length of the longest strictly increasing subsequence.

Approach 1: DP - O(n^2)
Approach 2: Binary Search - O(n log n)
"""
import bisect


def lis_dp(nums: list[int]) -> int:
    if not nums:
        return 0
    n = len(nums)
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


def lis_binary_search(nums: list[int]) -> int:
    tails = []
    for num in nums:
        pos = bisect.bisect_left(tails, num)
        if pos == len(tails):
            tails.append(num)
        else:
            tails[pos] = num
    return len(tails)


if __name__ == "__main__":
    print(lis_dp([10, 9, 2, 5, 3, 7, 101, 18]))            # 4
    print(lis_binary_search([10, 9, 2, 5, 3, 7, 101, 18]))  # 4
