"""
🟡 Activity Selection / Interval Scheduling
Select the maximum number of non-overlapping activities.

Time:  O(n log n)
Space: O(1)
"""


def max_activities(activities: list[tuple[int, int]]) -> list[tuple[int, int]]:
    sorted_acts = sorted(activities, key=lambda x: x[1])
    selected = [sorted_acts[0]]
    for start, end in sorted_acts[1:]:
        if start >= selected[-1][1]:
            selected.append((start, end))
    return selected


def min_meeting_rooms(intervals: list[list[int]]) -> int:
    """Find minimum number of meeting rooms required."""
    if not intervals:
        return 0
    events = []
    for start, end in intervals:
        events.append((start, 1))
        events.append((end, -1))
    events.sort()
    max_rooms = current_rooms = 0
    for _, delta in events:
        current_rooms += delta
        max_rooms = max(max_rooms, current_rooms)
    return max_rooms


if __name__ == "__main__":
    activities = [(1,4),(3,5),(0,6),(5,7),(3,9),(5,9),(6,10),(8,11),(8,12),(2,14),(12,16)]
    selected = max_activities(activities)
    print(f"Selected {len(selected)} activities: {selected}")
    print(f"Min rooms needed: {min_meeting_rooms([[0,30],[5,10],[15,20]])}")
