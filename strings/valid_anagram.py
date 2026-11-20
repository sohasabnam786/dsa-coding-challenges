"""
🟢 Valid Anagram
Determine if two strings are anagrams of each other.

Time:  O(n)
Space: O(1) - at most 26 characters
"""
from collections import Counter


def is_anagram(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)


def is_anagram_sort(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)


def is_anagram_manual(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    count = {}
    for c in s:
        count[c] = count.get(c, 0) + 1
    for c in t:
        count[c] = count.get(c, 0) - 1
        if count[c] < 0:
            return False
    return True


if __name__ == "__main__":
    print(is_anagram("anagram", "nagaram"))  # True
    print(is_anagram("rat", "car"))           # False
