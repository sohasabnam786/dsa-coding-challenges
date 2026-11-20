"""
🟡 Maximum Subarray (Kadane's Algorithm)
Find the contiguous subarray with the largest sum.

Time:  O(n)
Space: O(1)
"""


def max_subarray(nums: list[int]) -> int:
    max_sum = nums[0]
    current_sum = nums[0]

    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)

    return max_sum


def max_subarray_with_indices(nums: list[int]) -> tuple:
    """Returns (max_sum, start_index, end_index)."""
    max_sum = nums[0]
    current_sum = nums[0]
    start = end = temp_start = 0

    for i in range(1, len(nums)):
        if nums[i] > current_sum + nums[i]:
            current_sum = nums[i]
            temp_start = i
        else:
            current_sum += nums[i]

        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i

    return max_sum, start, end


if __name__ == "__main__":
    print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
    print(max_subarray_with_indices([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
