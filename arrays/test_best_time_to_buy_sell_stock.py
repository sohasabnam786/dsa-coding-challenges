from arrays.best_time_to_buy_sell_stock import max_profit


def test_normal_case():
    assert max_profit([7, 1, 5, 3, 6, 4]) == 5


def test_decreasing():
    assert max_profit([7, 6, 4, 3, 1]) == 0


def test_empty():
    assert max_profit([]) == 0


def test_single():
    assert max_profit([5]) == 0
