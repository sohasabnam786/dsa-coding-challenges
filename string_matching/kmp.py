"""
🟡 KMP (Knuth-Morris-Pratt) String Matching
Efficient pattern matching using failure function.

Time:  O(n + m)
Space: O(m) for failure table
"""


def build_failure_table(pattern: str) -> list[int]:
    m = len(pattern)
    failure = [0] * m
    j = 0

    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = failure[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        failure[i] = j

    return failure


def kmp_search(text: str, pattern: str) -> list[int]:
    if not pattern:
        return []

    failure = build_failure_table(pattern)
    matches = []
    j = 0

    for i in range(len(text)):
        while j > 0 and text[i] != pattern[j]:
            j = failure[j - 1]
        if text[i] == pattern[j]:
            j += 1
        if j == len(pattern):
            matches.append(i - len(pattern) + 1)
            j = failure[j - 1]

    return matches


if __name__ == "__main__":
    text = "ABABDABACDABABCABAB"
    pattern = "ABABCABAB"
    matches = kmp_search(text, pattern)
    print(f"Pattern found at indices: {matches}")

    text2 = "aaaaaa"
    pattern2 = "aaa"
    print(f"Overlapping matches: {kmp_search(text2, pattern2)}")
