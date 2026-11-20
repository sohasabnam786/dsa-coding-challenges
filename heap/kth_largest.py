"""
🟡 Kth Largest Element in an Array
Find the kth largest element using a heap.

Time:  O(n log k) with min-heap, O(n) average with quickselect
Space: O(k) with heap
"""
import heapq
import random


def find_kth_largest_heap(nums: list[int], k: int) -> int:
    """Min-heap approach - maintains k largest elements."""
    heap = nums[:k]
    heapq.heapify(heap)

    for num in nums[k:]:
        if num > heap[0]:
            heapq.heapreplace(heap, num)

    return heap[0]


def find_kth_largest_quickselect(nums: list[int], k: int) -> int:
    """Quickselect approach - O(n) average time."""
    target = len(nums) - k

    def quickselect(left, right):
        pivot_idx = random.randint(left, right)
        nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]
        pivot = nums[right]

        store = left
        for i in range(left, right):
            if nums[i] < pivot:
                nums[i], nums[store] = nums[store], nums[i]
                store += 1
        nums[store], nums[right] = nums[right], nums[store]

        if store == target:
            return nums[store]
        elif store < target:
            return quickselect(store + 1, right)
        else:
            return quickselect(left, store - 1)

    return quickselect(0, len(nums) - 1)


if __name__ == "__main__":
    print(find_kth_largest_heap([3,2,1,5,6,4], 2))          # 5
    print(find_kth_largest_quickselect([3,2,3,1,2,4,5,5,6], 4))  # 4
