"""
🟡 Z Algorithm
Compute Z-array for string matching and other applications.

Z[i] = length of the longest substring starting at i that matches a prefix of s.

Time:  O(n)
Space: O(n)
"""


def z_function(s: str) -> list[int]:
    n = len(s)
    z = [0] * n
    z[0] = n
    l, r = 0, 0

    for i in range(1, n):
        if i < r:
            z[i] = min(r - i, z[i - l])

        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1

        if i + z[i] > r:
            l, r = i, i + z[i]

    return z


def z_search(text: str, pattern: str) -> list[int]:
    """Find all occurrences of pattern in text using Z-algorithm."""
    combined = pattern + "$" + text
    z = z_function(combined)
    m = len(pattern)

    return [i - m - 1 for i in range(m + 1, len(combined)) if z[i] == m]


if __name__ == "__main__":
    s = "aabxaabxcaabxaabxay"
    z = z_function(s)
    print(f"Z-array: {z}")

    text = "ABABDABACDABABCABAB"
    pattern = "ABABCABAB"
    print(f"Pattern found at: {z_search(text, pattern)}")
