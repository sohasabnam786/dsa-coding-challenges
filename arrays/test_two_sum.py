from arrays.two_sum import two_sum, two_sum_brute_force


def test_basic():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]


def test_middle_elements():
    assert two_sum([3, 2, 4], 6) == [1, 2]


def test_duplicates():
    assert two_sum([3, 3], 6) == [0, 1]


def test_negative_numbers():
    assert two_sum([-1, -2, -3, -4, -5], -8) == [2, 4]


def test_brute_force():
    assert two_sum_brute_force([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum_brute_force([3, 2, 4], 6) == [1, 2]
