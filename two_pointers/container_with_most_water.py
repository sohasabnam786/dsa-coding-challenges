"""
🟡 Container With Most Water
Find two lines that form a container holding the most water.

Time:  O(n)
Space: O(1)
"""


def max_area(height: list[int]) -> int:
    left, right = 0, len(height) - 1
    max_water = 0
    while left < right:
        width = right - left
        h = min(height[left], height[right])
        max_water = max(max_water, width * h)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_water


if __name__ == "__main__":
    print(max_area([1,8,6,2,5,4,8,3,7]))  # 49
    print(max_area([1,1]))                  # 1
