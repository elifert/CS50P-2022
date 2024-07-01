from fuel2 import convert, gauge
import pytest

def test_gauge():
    assert gauge(99) == "F"
    assert gauge(98) == "98%"
    assert gauge(1) == "E"

def test_convert():
    assert convert("1/2") == 50
    assert convert("2/5") == 40
    assert convert("1/10") == 10

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_value_error():
    with pytest.raises(ValueError):
        convert("2/1")
