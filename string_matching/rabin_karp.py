"""
🟡 Rabin-Karp String Matching
Rolling hash based pattern matching.

Time:  O(n + m) average, O(n * m) worst case
Space: O(1)
"""


def rabin_karp(text: str, pattern: str) -> list[int]:
    n, m = len(text), len(pattern)
    if m > n:
        return []

    base = 256
    mod = 101  # Prime number
    matches = []

    # Calculate hash of pattern and first window
    p_hash = 0
    t_hash = 0
    h = pow(base, m - 1, mod)

    for i in range(m):
        p_hash = (base * p_hash + ord(pattern[i])) % mod
        t_hash = (base * t_hash + ord(text[i])) % mod

    for i in range(n - m + 1):
        if p_hash == t_hash:
            if text[i:i + m] == pattern:
                matches.append(i)

        if i < n - m:
            t_hash = (base * (t_hash - ord(text[i]) * h) + ord(text[i + m])) % mod
            if t_hash < 0:
                t_hash += mod

    return matches


if __name__ == "__main__":
    text = "ABABDABACDABABCABAB"
    pattern = "ABABCABAB"
    print(f"Matches at: {rabin_karp(text, pattern)}")

    # Multiple pattern search
    text2 = "the quick brown fox jumps over the lazy fox"
    print(f"'fox' found at: {rabin_karp(text2, 'fox')}")
