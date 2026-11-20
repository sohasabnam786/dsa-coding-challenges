"""
🟡 Group Anagrams
Group strings that are anagrams of each other.

Time:  O(n * k log k) where k is max string length
Space: O(n * k)
"""
from collections import defaultdict


def group_anagrams(strs: list[str]) -> list[list[str]]:
    groups = defaultdict(list)
    for s in strs:
        key = tuple(sorted(s))
        groups[key].append(s)
    return list(groups.values())


def group_anagrams_count(strs: list[str]) -> list[list[str]]:
    """Using character count as key - O(n * k) time."""
    groups = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord("a")] += 1
        groups[tuple(count)].append(s)
    return list(groups.values())


if __name__ == "__main__":
    result = group_anagrams(["eat","tea","tan","ate","nat","bat"])
    for group in result:
        print(group)
