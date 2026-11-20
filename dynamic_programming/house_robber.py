"""
🟡 House Robber
Maximize the amount of money you can rob without robbing adjacent houses.

Time:  O(n)
Space: O(1)
"""


def rob(nums: list[int]) -> int:
    if not nums:
        return 0
    if len(nums) <= 2:
        return max(nums)
    prev2, prev1 = nums[0], max(nums[0], nums[1])
    for i in range(2, len(nums)):
        curr = max(prev1, prev2 + nums[i])
        prev2 = prev1
        prev1 = curr
    return prev1


def rob_circular(nums: list[int]) -> int:
    """House Robber II - houses are in a circle."""
    if len(nums) <= 2:
        return max(nums) if nums else 0
    return max(rob(nums[:-1]), rob(nums[1:]))


if __name__ == "__main__":
    print(rob([1, 2, 3, 1]))       # 4
    print(rob([2, 7, 9, 3, 1]))    # 12
    print(rob_circular([2, 3, 2]))  # 3
