def majority_element(nums: list[int]) -> int:
    count, cand = 0, None
    for n in nums:
        if count == 0:
            cand = n
        count += 1 if n == cand else -1
    return cand
