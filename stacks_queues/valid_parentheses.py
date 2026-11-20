"""
🟢 Valid Parentheses
Determine if the input string has valid bracket matching.

Time:  O(n)
Space: O(n)
"""


def is_valid(s: str) -> bool:
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    for char in s:
        if char in mapping:
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
        else:
            stack.append(char)
    return len(stack) == 0


if __name__ == "__main__":
    print(is_valid("()"))        # True
    print(is_valid("()[]{}"))    # True
    print(is_valid("(]"))        # False
    print(is_valid("{[]}"))      # True
