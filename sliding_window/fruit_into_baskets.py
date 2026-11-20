"""
🟡 Fruit Into Baskets (Longest Subarray with at most K distinct elements)

Time:  O(n)
Space: O(1)
"""
from collections import defaultdict


def total_fruit(fruits: list[int]) -> int:
    basket = defaultdict(int)
    left = 0
    max_fruits = 0
    for right in range(len(fruits)):
        basket[fruits[right]] += 1
        while len(basket) > 2:
            basket[fruits[left]] -= 1
            if basket[fruits[left]] == 0:
                del basket[fruits[left]]
            left += 1
        max_fruits = max(max_fruits, right - left + 1)
    return max_fruits


def longest_k_distinct(s: str, k: int) -> int:
    """Longest substring with at most k distinct characters."""
    char_count = defaultdict(int)
    left = 0
    max_len = 0
    for right in range(len(s)):
        char_count[s[right]] += 1
        while len(char_count) > k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len


if __name__ == "__main__":
    print(total_fruit([1, 2, 1]))           # 3
    print(total_fruit([0, 1, 2, 2]))        # 3
    print(longest_k_distinct("araaci", 2))   # 4
