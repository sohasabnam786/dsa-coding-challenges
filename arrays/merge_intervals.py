"""
🟡 Merge Intervals
Given an array of intervals, merge all overlapping intervals.

Time:  O(n log n)
Space: O(n)
"""


def merge(intervals: list[list[int]]) -> list[list[int]]:
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    for start, end in intervals[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])

    return merged


if __name__ == "__main__":
    print(merge([[1,3],[2,6],[8,10],[15,18]]))  # [[1,6],[8,10],[15,18]]
    print(merge([[1,4],[4,5]]))                  # [[1,5]]
