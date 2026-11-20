"""
🟢 Maximum Sum Subarray of Size K
Find the maximum sum of a subarray of size k.

Time:  O(n)
Space: O(1)
"""


def max_sum_subarray(nums: list[int], k: int) -> int:
    if len(nums) < k:
        return 0
    window_sum = sum(nums[:k])
    max_sum = window_sum
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, window_sum)
    return max_sum


def min_size_subarray_sum(target: int, nums: list[int]) -> int:
    """Find the minimal length subarray with sum >= target."""
    min_len = float("inf")
    window_sum = 0
    left = 0
    for right in range(len(nums)):
        window_sum += nums[right]
        while window_sum >= target:
            min_len = min(min_len, right - left + 1)
            window_sum -= nums[left]
            left += 1
    return min_len if min_len != float("inf") else 0


if __name__ == "__main__":
    print(max_sum_subarray([2, 1, 5, 1, 3, 2], 3))  # 9
    print(min_size_subarray_sum(7, [2,3,1,2,4,3]))   # 2
