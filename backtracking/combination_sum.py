"""
🟡 Combination Sum
Find all unique combinations that sum to a target.

Time:  O(2^t) where t = target / min(candidates)
Space: O(t)
"""


def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    """Candidates can be reused."""
    result = []
    candidates.sort()

    def backtrack(remaining, combo, start):
        if remaining == 0:
            result.append(combo[:])
            return
        for i in range(start, len(candidates)):
            if candidates[i] > remaining:
                break
            combo.append(candidates[i])
            backtrack(remaining - candidates[i], combo, i)
            combo.pop()

    backtrack(target, [], 0)
    return result


def combination_sum_2(candidates: list[int], target: int) -> list[list[int]]:
    """Each candidate can only be used once."""
    result = []
    candidates.sort()

    def backtrack(remaining, combo, start):
        if remaining == 0:
            result.append(combo[:])
            return
        for i in range(start, len(candidates)):
            if candidates[i] > remaining:
                break
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            combo.append(candidates[i])
            backtrack(remaining - candidates[i], combo, i + 1)
            combo.pop()

    backtrack(target, [], 0)
    return result


if __name__ == "__main__":
    print(combination_sum([2, 3, 6, 7], 7))      # [[2,2,3], [7]]
    print(combination_sum_2([10,1,2,7,6,1,5], 8)) # [[1,1,6], [1,2,5], [1,7], [2,6]]
