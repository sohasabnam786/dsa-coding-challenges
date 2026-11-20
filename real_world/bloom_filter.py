"""
Bloom Filter
Probabilistic data structure for set membership testing.
False positives possible, false negatives impossible.

Time:  O(k) per operation where k = number of hash functions
Space: O(m) bits
"""
import hashlib
import math


class BloomFilter:
    def __init__(self, expected_items: int, false_positive_rate: float = 0.01):
        self.size = self._optimal_size(expected_items, false_positive_rate)
        self.num_hashes = self._optimal_hashes(self.size, expected_items)
        self.bit_array = [False] * self.size
        self.items_added = 0

    def add(self, item: str) -> None:
        for i in range(self.num_hashes):
            index = self._hash(item, i)
            self.bit_array[index] = True
        self.items_added += 1

    def might_contain(self, item: str) -> bool:
        return all(self.bit_array[self._hash(item, i)] for i in range(self.num_hashes))

    def _hash(self, item: str, seed: int) -> int:
        h = hashlib.sha256(f"{item}{seed}".encode()).hexdigest()
        return int(h, 16) % self.size

    @staticmethod
    def _optimal_size(n: int, p: float) -> int:
        m = -(n * math.log(p)) / (math.log(2) ** 2)
        return int(m)

    @staticmethod
    def _optimal_hashes(m: int, n: int) -> int:
        k = (m / n) * math.log(2)
        return max(1, int(k))

    @property
    def fill_ratio(self) -> float:
        return sum(self.bit_array) / self.size


if __name__ == "__main__":
    bf = BloomFilter(1000, 0.01)
    words = ["apple", "banana", "cherry", "date", "elderberry"]
    for w in words:
        bf.add(w)

    print(f"Size: {bf.size} bits, Hashes: {bf.num_hashes}")

    for w in words:
        print(f"  '{w}' in filter: {bf.might_contain(w)}")  # All True

    test_words = ["fig", "grape", "kiwi"]
    for w in test_words:
        print(f"  '{w}' in filter: {bf.might_contain(w)}")  # Likely False

    print(f"Fill ratio: {bf.fill_ratio:.4f}")
