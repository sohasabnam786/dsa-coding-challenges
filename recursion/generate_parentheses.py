"""
🟡 Generate Parentheses
Generate all combinations of n pairs of well-formed parentheses.

Time:  O(4^n / sqrt(n)) - Catalan number
Space: O(n)
"""


def generate_parenthesis(n: int) -> list[str]:
    result = []
    def backtrack(current: str, open_count: int, close_count: int):
        if len(current) == 2 * n:
            result.append(current)
            return
        if open_count < n:
            backtrack(current + "(", open_count + 1, close_count)
        if close_count < open_count:
            backtrack(current + ")", open_count, close_count + 1)
    backtrack("", 0, 0)
    return result


if __name__ == "__main__":
    for n in range(1, 5):
        combos = generate_parenthesis(n)
        print(f"n={n}: {len(combos)} combinations")
        for c in combos:
            print(f"  {c}")
