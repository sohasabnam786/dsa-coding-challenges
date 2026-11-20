"""
🟢 Contains Duplicate
Given an integer array, return True if any value appears at least twice.

Time:  O(n)
Space: O(n)
"""


def contains_duplicate(nums: list[int]) -> bool:
    return len(nums) != len(set(nums))


def contains_duplicate_sort(nums: list[int]) -> bool:
    """Sorting approach - O(n log n) time, O(1) space."""
    nums = sorted(nums)
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return True
    return False


if __name__ == "__main__":
    print(contains_duplicate([1, 2, 3, 1]))     # True
    print(contains_duplicate([1, 2, 3, 4]))     # False
