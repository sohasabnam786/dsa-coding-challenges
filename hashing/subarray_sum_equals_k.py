"""
🟡 Subarray Sum Equals K
Find the total number of subarrays whose sum equals k.

Time:  O(n)
Space: O(n)
"""
from collections import defaultdict


def subarray_sum(nums: list[int], k: int) -> int:
    count = 0
    prefix_sum = 0
    prefix_counts = defaultdict(int)
    prefix_counts[0] = 1
    for num in nums:
        prefix_sum += num
        count += prefix_counts[prefix_sum - k]
        prefix_counts[prefix_sum] += 1
    return count


if __name__ == "__main__":
    print(subarray_sum([1, 1, 1], 2))   # 2
    print(subarray_sum([1, 2, 3], 3))   # 2
    print(subarray_sum([1, -1, 0], 0))  # 3
