"""
🔴 Find Median from Data Stream
Design a data structure that supports adding numbers and finding the median.

Time:  O(log n) for addNum, O(1) for findMedian
Space: O(n)
"""
import heapq


class MedianFinder:
    def __init__(self):
        self.small = []  # Max-heap (negated values)
        self.large = []  # Min-heap

    def add_num(self, num: int) -> None:
        # Always add to max-heap first
        heapq.heappush(self.small, -num)

        # Ensure max of small <= min of large
        if self.small and self.large and (-self.small[0]) > self.large[0]:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # Balance sizes (small can have at most 1 more element)
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        elif len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def find_median(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2.0


if __name__ == "__main__":
    mf = MedianFinder()
    mf.add_num(1)
    print(mf.find_median())  # 1.0
    mf.add_num(2)
    print(mf.find_median())  # 1.5
    mf.add_num(3)
    print(mf.find_median())  # 2.0
