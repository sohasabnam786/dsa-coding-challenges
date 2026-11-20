"""
🟡 Jump Game
Determine if you can reach the last index.

Time:  O(n)
Space: O(1)
"""


def can_jump(nums: list[int]) -> bool:
    max_reach = 0
    for i, jump in enumerate(nums):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i + jump)
    return True


def min_jumps(nums: list[int]) -> int:
    """Jump Game II - minimum number of jumps to reach the end."""
    jumps = 0
    current_end = 0
    farthest = 0
    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])
        if i == current_end:
            jumps += 1
            current_end = farthest
    return jumps


if __name__ == "__main__":
    print(can_jump([2, 3, 1, 1, 4]))   # True
    print(can_jump([3, 2, 1, 0, 4]))   # False
    print(min_jumps([2, 3, 1, 1, 4]))  # 2
