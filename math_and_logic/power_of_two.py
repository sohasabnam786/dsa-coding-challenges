"""
🟢 Power of Two & Bit Manipulation
Check if a number is a power of two, count bits, etc.

Time:  O(1)
Space: O(1)
"""


def is_power_of_two(n: int) -> bool:
    return n > 0 and (n & (n - 1)) == 0


def count_bits(n: int) -> int:
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count


def count_bits_trick(n: int) -> int:
    """Brian Kernighan's trick - O(number of set bits)."""
    count = 0
    while n:
        n &= n - 1
        count += 1
    return count


def single_number(nums: list[int]) -> int:
    """Find the element that appears only once (others appear twice)."""
    result = 0
    for num in nums:
        result ^= num
    return result


if __name__ == "__main__":
    for i in range(17):
        print(f"{i}: power_of_two={is_power_of_two(i)}, bits={count_bits(i)}")
    print(single_number([4, 1, 2, 1, 2]))  # 4
