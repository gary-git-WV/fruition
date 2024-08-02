import pytest
from fuel import convert, gauge


def test_one_half():
    assert convert("1/2") == 50
def test_one_third():
    assert convert("1/3") == 33
def test_99():
    assert convert("99/100") == 99
def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
def test_cat_num():
    with pytest.raises(ValueError):
        convert("cat/4")
def test_cat_denom():
    with pytest.raises(ValueError):
        convert("1/cat")
def test_float_num():
    with pytest.raises(ValueError):
        convert("1.2/4")
def test_float_denom():
    with pytest.raises(ValueError):
        convert("1/4.2")
def test_gauge1():
    assert gauge(1) == 'E'
def test_99ga():
    assert gauge(99) == "F"
def test_gauge_50():
    assert gauge(50) == "50%"
