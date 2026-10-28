def test_div_zero_raises():
    import calc
    import pytest
    with pytest.raises(ValueError):
        calc.div(1, 0)