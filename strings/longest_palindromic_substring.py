"""
🟡 Longest Palindromic Substring
Find the longest palindromic substring in s.

Approach: Expand around center.
Time:  O(n^2)
Space: O(1)
"""


def longest_palindrome(s: str) -> str:
    if len(s) < 2:
        return s

    start = 0
    max_len = 1

    def expand(left: int, right: int):
        nonlocal start, max_len
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if right - left + 1 > max_len:
                start = left
                max_len = right - left + 1
            left -= 1
            right += 1

    for i in range(len(s)):
        expand(i, i)       # Odd length
        expand(i, i + 1)   # Even length

    return s[start:start + max_len]


if __name__ == "__main__":
    print(longest_palindrome("babad"))   # "bab" or "aba"
    print(longest_palindrome("cbbd"))    # "bb"
    print(longest_palindrome("racecar")) # "racecar"
