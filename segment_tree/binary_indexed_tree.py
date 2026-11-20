"""
🟡 Binary Indexed Tree (Fenwick Tree)
Efficient data structure for prefix sums and point updates.

Time:  O(log n) per query/update
Space: O(n)
"""


class BIT:
    def __init__(self, n: int):
        self.n = n
        self.tree = [0] * (n + 1)

    @classmethod
    def from_array(cls, nums: list[int]):
        bit = cls(len(nums))
        for i, num in enumerate(nums):
            bit.update(i, num)
        return bit

    def update(self, index: int, delta: int) -> None:
        """Add delta to element at index."""
        i = index + 1
        while i <= self.n:
            self.tree[i] += delta
            i += i & (-i)

    def prefix_sum(self, index: int) -> int:
        """Sum of elements from 0 to index (inclusive)."""
        total = 0
        i = index + 1
        while i > 0:
            total += self.tree[i]
            i -= i & (-i)
        return total

    def range_sum(self, left: int, right: int) -> int:
        """Sum of elements from left to right (inclusive)."""
        result = self.prefix_sum(right)
        if left > 0:
            result -= self.prefix_sum(left - 1)
        return result


class BIT2D:
    """2D Binary Indexed Tree for 2D prefix sums."""
    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols
        self.tree = [[0] * (cols + 1) for _ in range(rows + 1)]

    def update(self, row: int, col: int, delta: int):
        i = row + 1
        while i <= self.rows:
            j = col + 1
            while j <= self.cols:
                self.tree[i][j] += delta
                j += j & (-j)
            i += i & (-i)

    def prefix_sum(self, row: int, col: int) -> int:
        total = 0
        i = row + 1
        while i > 0:
            j = col + 1
            while j > 0:
                total += self.tree[i][j]
                j -= j & (-j)
            i -= i & (-i)
        return total

    def region_sum(self, r1: int, c1: int, r2: int, c2: int) -> int:
        result = self.prefix_sum(r2, c2)
        if r1 > 0:
            result -= self.prefix_sum(r1 - 1, c2)
        if c1 > 0:
            result -= self.prefix_sum(r2, c1 - 1)
        if r1 > 0 and c1 > 0:
            result += self.prefix_sum(r1 - 1, c1 - 1)
        return result


if __name__ == "__main__":
    nums = [1, 7, 3, 0, 5, 8, 3, 2, 6, 2, 1, 1, 4, 13]
    bit = BIT.from_array(nums)

    print(f"Prefix sum [0..5]: {bit.prefix_sum(5)}")   # 24
    print(f"Range sum [2..6]: {bit.range_sum(2, 6)}")  # 19

    bit.update(3, 6)  # Add 6 to index 3
    print(f"After update, range sum [2..6]: {bit.range_sum(2, 6)}")  # 25
