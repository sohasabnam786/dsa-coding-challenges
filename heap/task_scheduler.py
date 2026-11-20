"""
🟡 Task Scheduler
Given tasks with cooldown period, find minimum intervals to finish all tasks.

Time:  O(n)
Space: O(1) - at most 26 distinct tasks
"""
from collections import Counter


def least_interval(tasks: list[str], n: int) -> int:
    counts = Counter(tasks)
    max_count = max(counts.values())
    max_count_tasks = sum(1 for c in counts.values() if c == max_count)

    # Formula: (max_count - 1) * (n + 1) + max_count_tasks
    result = (max_count - 1) * (n + 1) + max_count_tasks

    # At minimum, we need len(tasks) intervals
    return max(result, len(tasks))


if __name__ == "__main__":
    print(least_interval(["A","A","A","B","B","B"], 2))     # 8
    print(least_interval(["A","A","A","B","B","B"], 0))     # 6
    print(least_interval(["A","A","A","A","A","A","B","C","D","E","F","G"], 2))  # 16
