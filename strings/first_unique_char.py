from collections import Counter
def first_uniq_char(s: str) -> int:
    cnt = Counter(s)
    for i, ch in enumerate(s):
        if cnt[ch] == 1:
            return i
    return -1
