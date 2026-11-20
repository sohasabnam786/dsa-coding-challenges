"""
🟡 Letter Combinations of a Phone Number
Generate all letter combinations from phone digits.

Time:  O(4^n)
Space: O(n)
"""


PHONE_MAP = {
    "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
    "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz",
}


def letter_combinations(digits: str) -> list[str]:
    if not digits:
        return []

    result = []

    def backtrack(index, current):
        if index == len(digits):
            result.append("".join(current))
            return

        for letter in PHONE_MAP[digits[index]]:
            current.append(letter)
            backtrack(index + 1, current)
            current.pop()

    backtrack(0, [])
    return result


def letter_combinations_iterative(digits: str) -> list[str]:
    """Iterative BFS approach."""
    if not digits:
        return []

    result = [""]
    for digit in digits:
        new_result = []
        for combo in result:
            for letter in PHONE_MAP[digit]:
                new_result.append(combo + letter)
        result = new_result

    return result


if __name__ == "__main__":
    print(letter_combinations("23"))
    # ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    print(letter_combinations_iterative("23"))
