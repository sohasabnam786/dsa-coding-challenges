"""
🟡 Permutations & Combinations
Generate all permutations and combinations of a list.
"""


def permutations(nums: list[int]) -> list[list[int]]:
    result = []
    def backtrack(current, remaining):
        if not remaining:
            result.append(current[:])
            return
        for i in range(len(remaining)):
            current.append(remaining[i])
            backtrack(current, remaining[:i] + remaining[i+1:])
            current.pop()
    backtrack([], nums)
    return result


def combinations(nums: list[int], k: int) -> list[list[int]]:
    result = []
    def backtrack(start, current):
        if len(current) == k:
            result.append(current[:])
            return
        for i in range(start, len(nums)):
            current.append(nums[i])
            backtrack(i + 1, current)
            current.pop()
    backtrack(0, [])
    return result


def subsets(nums: list[int]) -> list[list[int]]:
    result = []
    def backtrack(start, current):
        result.append(current[:])
        for i in range(start, len(nums)):
            current.append(nums[i])
            backtrack(i + 1, current)
            current.pop()
    backtrack(0, [])
    return result


if __name__ == "__main__":
    print("Permutations of [1,2,3]:")
    for p in permutations([1, 2, 3]):
        print(f"  {p}")
    print("\nCombinations of [1,2,3,4] choose 2:")
    for c in combinations([1, 2, 3, 4], 2):
        print(f"  {c}")
    print("\nSubsets of [1,2,3]:")
    for s in subsets([1, 2, 3]):
        print(f"  {s}")
