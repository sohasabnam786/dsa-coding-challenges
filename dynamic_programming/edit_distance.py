"""
🔴 Edit Distance (Levenshtein Distance)
Find the minimum number of operations to convert word1 to word2.
Operations: insert, delete, replace.

Time:  O(m * n)
Space: O(m * n), can be optimized to O(min(m, n))
"""


def min_distance(word1: str, word2: str) -> int:
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    return dp[m][n]


def min_distance_optimized(word1: str, word2: str) -> int:
    """Space-optimized version using two rows."""
    m, n = len(word1), len(word2)
    if m < n:
        return min_distance_optimized(word2, word1)
    prev = list(range(n + 1))
    for i in range(1, m + 1):
        curr = [i] + [0] * n
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                curr[j] = prev[j - 1]
            else:
                curr[j] = 1 + min(prev[j], curr[j - 1], prev[j - 1])
        prev = curr
    return prev[n]


if __name__ == "__main__":
    print(min_distance("horse", "ros"))            # 3
    print(min_distance("intention", "execution"))  # 5
