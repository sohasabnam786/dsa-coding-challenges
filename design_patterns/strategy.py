"""
Strategy Pattern
Define a family of algorithms, encapsulate each one, and make them interchangeable.

Use cases: Sorting strategies, payment methods, compression algorithms.
"""
from abc import ABC, abstractmethod


class SortStrategy(ABC):
    @abstractmethod
    def sort(self, data: list) -> list:
        pass

    @abstractmethod
    def name(self) -> str:
        pass


class BubbleSortStrategy(SortStrategy):
    def sort(self, data: list) -> list:
        arr = data[:]
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

    def name(self) -> str:
        return "Bubble Sort"


class QuickSortStrategy(SortStrategy):
    def sort(self, data: list) -> list:
        if len(data) <= 1:
            return data
        pivot = data[len(data) // 2]
        left = [x for x in data if x < pivot]
        middle = [x for x in data if x == pivot]
        right = [x for x in data if x > pivot]
        return self.sort(left) + middle + self.sort(right)

    def name(self) -> str:
        return "Quick Sort"


class MergeSortStrategy(SortStrategy):
    def sort(self, data: list) -> list:
        if len(data) <= 1:
            return data
        mid = len(data) // 2
        left = self.sort(data[:mid])
        right = self.sort(data[mid:])
        return self._merge(left, right)

    def _merge(self, left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def name(self) -> str:
        return "Merge Sort"


class Sorter:
    def __init__(self, strategy: SortStrategy = None):
        self._strategy = strategy or QuickSortStrategy()

    def set_strategy(self, strategy: SortStrategy):
        self._strategy = strategy

    def sort(self, data: list) -> list:
        print(f"Sorting with {self._strategy.name()}")
        return self._strategy.sort(data)


if __name__ == "__main__":
    data = [64, 34, 25, 12, 22, 11, 90]
    sorter = Sorter()

    for strategy in [BubbleSortStrategy(), QuickSortStrategy(), MergeSortStrategy()]:
        sorter.set_strategy(strategy)
        result = sorter.sort(data)
        print(f"  Result: {result}")
