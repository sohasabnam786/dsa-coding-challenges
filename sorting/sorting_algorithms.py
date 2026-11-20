"""
🟢🟡 Classic Sorting Algorithms
Implementation of common sorting algorithms with complexity analysis.
"""


def bubble_sort(arr: list[int]) -> list[int]:
    """Bubble Sort - O(n^2) time, O(1) space."""
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


def selection_sort(arr: list[int]) -> list[int]:
    """Selection Sort - O(n^2) time, O(1) space."""
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def insertion_sort(arr: list[int]) -> list[int]:
    """Insertion Sort - O(n^2) time, O(1) space."""
    arr = arr.copy()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def merge_sort(arr: list[int]) -> list[int]:
    """Merge Sort - O(n log n) time, O(n) space."""
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return _merge(left, right)


def _merge(left: list[int], right: list[int]) -> list[int]:
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


def quick_sort(arr: list[int]) -> list[int]:
    """Quick Sort - O(n log n) average, O(n^2) worst time."""
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def heap_sort(arr: list[int]) -> list[int]:
    """Heap Sort - O(n log n) time, O(1) space."""
    arr = arr.copy()
    n = len(arr)
    def heapify(size, root):
        largest = root
        left = 2 * root + 1
        right = 2 * root + 2
        if left < size and arr[left] > arr[largest]:
            largest = left
        if right < size and arr[right] > arr[largest]:
            largest = right
        if largest != root:
            arr[root], arr[largest] = arr[largest], arr[root]
            heapify(size, largest)
    for i in range(n // 2 - 1, -1, -1):
        heapify(n, i)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(i, 0)
    return arr


if __name__ == "__main__":
    test_arr = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original:  {test_arr}")
    print(f"Bubble:    {bubble_sort(test_arr)}")
    print(f"Selection: {selection_sort(test_arr)}")
    print(f"Insertion: {insertion_sort(test_arr)}")
    print(f"Merge:     {merge_sort(test_arr)}")
    print(f"Quick:     {quick_sort(test_arr)}")
    print(f"Heap:      {heap_sort(test_arr)}")
