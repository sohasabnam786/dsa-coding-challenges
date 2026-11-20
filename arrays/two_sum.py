"""
🟢 Two Sum
Given an array of integers and a target, return indices of two numbers that add up to the target.

Time:  O(n)
Space: O(n)
"""


def two_sum(nums: list[int], target: int) -> list[int]:
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


def two_sum_brute_force(nums: list[int], target: int) -> list[int]:
    """Brute force approach - O(n^2) time, O(1) space."""
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))   # [0, 1]
    print(two_sum([3, 2, 4], 6))         # [1, 2]
    print(two_sum([3, 3], 6))            # [0, 1]
