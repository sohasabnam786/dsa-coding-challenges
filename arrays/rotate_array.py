def rotate(nums: list[int], k: int) -> None:
    k %= len(nums)
    def rev(l, r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1
    rev(0, len(nums) - 1)
    rev(0, k - 1)
    rev(k, len(nums) - 1)

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    rotate(arr, 3)
    print("Rotated:", arr)
