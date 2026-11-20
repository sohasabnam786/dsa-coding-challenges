"""
🟡 Product of Array Except Self
Return an array where each element is the product of all elements except itself.
Solve it WITHOUT using division.

Time:  O(n)
Space: O(1) extra (output array doesn't count)
"""


def product_except_self(nums: list[int]) -> list[int]:
    n = len(nums)
    result = [1] * n

    left_product = 1
    for i in range(n):
        result[i] = left_product
        left_product *= nums[i]

    right_product = 1
    for i in range(n - 1, -1, -1):
        result[i] *= right_product
        right_product *= nums[i]

    return result


if __name__ == "__main__":
    print(product_except_self([1, 2, 3, 4]))          # [24, 12, 8, 6]
    print(product_except_self([-1, 1, 0, -3, 3]))     # [0, 0, 9, 0, 0]
