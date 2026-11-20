from sorting.sorting_algorithms import (
    bubble_sort, selection_sort, insertion_sort,
    merge_sort, quick_sort, heap_sort
)
import random

ALGORITHMS = [bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort, heap_sort]


def test_sorted():
    arr = [1, 2, 3, 4, 5]
    for algo in ALGORITHMS:
        assert algo(arr) == [1, 2, 3, 4, 5], f"{algo.__name__} failed"


def test_reverse():
    arr = [5, 4, 3, 2, 1]
    for algo in ALGORITHMS:
        assert algo(arr) == [1, 2, 3, 4, 5], f"{algo.__name__} failed"


def test_duplicates():
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    expected = sorted(arr)
    for algo in ALGORITHMS:
        assert algo(arr) == expected, f"{algo.__name__} failed"


def test_single():
    for algo in ALGORITHMS:
        assert algo([42]) == [42]


def test_empty():
    for algo in ALGORITHMS:
        assert algo([]) == []


def test_negative():
    arr = [-3, -1, -4, -1, -5]
    expected = sorted(arr)
    for algo in ALGORITHMS:
        assert algo(arr) == expected


def test_random():
    arr = [random.randint(-100, 100) for _ in range(50)]
    expected = sorted(arr)
    for algo in ALGORITHMS:
        assert algo(arr) == expected
