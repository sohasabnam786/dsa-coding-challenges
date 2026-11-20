"""
🟡 Palindrome Partitioning
Partition a string such that every substring is a palindrome.

Time:  O(n * 2^n)
Space: O(n)
"""


def partition(s: str) -> list[list[str]]:
    result = []

    def is_palindrome(sub):
        return sub == sub[::-1]

    def backtrack(start, current):
        if start == len(s):
            result.append(current[:])
            return

        for end in range(start + 1, len(s) + 1):
            substring = s[start:end]
            if is_palindrome(substring):
                current.append(substring)
                backtrack(end, current)
                current.pop()

    backtrack(0, [])
    return result


if __name__ == "__main__":
    print(partition("aab"))    # [["a","a","b"], ["aa","b"]]
    print(partition("a"))      # [["a"]]
