"""
🔴 Trapping Rain Water
Compute how much water can be trapped after raining.

Time:  O(n)
Space: O(1)
"""


def trap(height: list[int]) -> int:
    """Two-pointer approach."""
    if not height:
        return 0
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]
    water = 0
    while left < right:
        if left_max < right_max:
            left += 1
            left_max = max(left_max, height[left])
            water += left_max - height[left]
        else:
            right -= 1
            right_max = max(right_max, height[right])
            water += right_max - height[right]
    return water


def trap_dp(height: list[int]) -> int:
    """DP approach - easier to understand."""
    if not height:
        return 0
    n = len(height)
    left_max = [0] * n
    right_max = [0] * n
    left_max[0] = height[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i-1], height[i])
    right_max[n-1] = height[n-1]
    for i in range(n-2, -1, -1):
        right_max[i] = max(right_max[i+1], height[i])
    water = 0
    for i in range(n):
        water += min(left_max[i], right_max[i]) - height[i]
    return water


if __name__ == "__main__":
    print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))  # 6
    print(trap([4,2,0,3,2,5]))                # 9
