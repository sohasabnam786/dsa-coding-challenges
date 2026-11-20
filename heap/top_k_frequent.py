"""
🟡 Top K Frequent Elements
Find the k most frequent elements in an array.

Time:  O(n log k) with heap, O(n) with bucket sort
Space: O(n)
"""
import heapq
from collections import Counter


def top_k_frequent_heap(nums: list[int], k: int) -> list[int]:
    """Heap approach - O(n log k)."""
    count = Counter(nums)
    return heapq.nlargest(k, count.keys(), key=count.get)


def top_k_frequent_bucket(nums: list[int], k: int) -> list[int]:
    """Bucket sort approach - O(n)."""
    count = Counter(nums)
    buckets = [[] for _ in range(len(nums) + 1)]

    for num, freq in count.items():
        buckets[freq].append(num)

    result = []
    for i in range(len(buckets) - 1, -1, -1):
        for num in buckets[i]:
            result.append(num)
            if len(result) == k:
                return result
    return result


if __name__ == "__main__":
    print(top_k_frequent_heap([1,1,1,2,2,3], 2))     # [1, 2]
    print(top_k_frequent_bucket([1,1,1,2,2,3], 2))   # [1, 2]
