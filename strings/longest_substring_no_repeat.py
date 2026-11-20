"""
🟡 Longest Substring Without Repeating Characters
Find the length of the longest substring without repeating characters.

Time:  O(n)
Space: O(min(n, m)) where m is the charset size
"""


def length_of_longest_substring(s: str) -> int:
    char_index = {}
    max_len = 0
    start = 0

    for end, char in enumerate(s):
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1
        char_index[char] = end
        max_len = max(max_len, end - start + 1)

    return max_len


if __name__ == "__main__":
    print(length_of_longest_substring("abcabcbb"))  # 3
    print(length_of_longest_substring("bbbbb"))      # 1
    print(length_of_longest_substring("pwwkew"))     # 3
