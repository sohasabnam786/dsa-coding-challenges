"""
🟢 Binary Search & Variants
Classic binary search and its common variations.

Time:  O(log n)
Space: O(1)
"""


def binary_search(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def lower_bound(nums: list[int], target: int) -> int:
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left


def upper_bound(nums: list[int], target: int) -> int:
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return left


def search_range(nums: list[int], target: int) -> list[int]:
    lo = lower_bound(nums, target)
    hi = upper_bound(nums, target)
    if lo < len(nums) and nums[lo] == target:
        return [lo, hi - 1]
    return [-1, -1]


def search_rotated(nums: list[int], target: int) -> int:
    """Search in a rotated sorted array."""
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1


if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 11, 13]
    print(binary_search(arr, 7))                    # 3
    print(search_range([5,7,7,8,8,10], 8))          # [3, 4]
    print(search_rotated([4,5,6,7,0,1,2], 0))       # 4
