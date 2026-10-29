def test_mean_basic():
    from stats import mean
    assert mean([1, 2, 3, 4]) == 2.5

def test_median_odd_length():
    from stats import median
    assert median([3, 1, 2]) == 2
