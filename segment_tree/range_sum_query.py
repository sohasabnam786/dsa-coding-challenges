"""
🟡 Range Sum Query - Mutable
Handle multiple range sum queries with updates.

Time:  O(log n) per query/update
Space: O(n)
"""


class NumArray:
    def __init__(self, nums: list[int]):
        self.n = len(nums)
        self.tree = [0] * (self.n + 1)
        self.nums = [0] * self.n

        for i, num in enumerate(nums):
            self.update(i, num)

    def update(self, index: int, val: int) -> None:
        diff = val - self.nums[index]
        self.nums[index] = val
        i = index + 1
        while i <= self.n:
            self.tree[i] += diff
            i += i & (-i)

    def _prefix_sum(self, index: int) -> int:
        total = 0
        i = index + 1
        while i > 0:
            total += self.tree[i]
            i -= i & (-i)
        return total

    def sum_range(self, left: int, right: int) -> int:
        result = self._prefix_sum(right)
        if left > 0:
            result -= self._prefix_sum(left - 1)
        return result


if __name__ == "__main__":
    arr = NumArray([1, 3, 5])
    print(arr.sum_range(0, 2))  # 9
    arr.update(1, 2)
    print(arr.sum_range(0, 2))  # 8
