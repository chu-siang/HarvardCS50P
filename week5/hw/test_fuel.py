from fuel import convert,gauge
import pytest

def test_convert():
    assert convert("3/4") == 75
    assert convert("1/3") == 33
    assert convert("2/3") == 67
    assert convert("0/100") == 0
    assert convert("1/100") == 1
    assert convert("100/100") == 100
    assert convert("99/100") == 99
    with pytest.raises(ZeroDivisionError):
        convert("100/0")
        convert("4/0")
        convert("1/0")
    with pytest.raises(ValueError):
        convert("three/four")
    with pytest.raises(ValueError):
        convert("cat/dog")
    with pytest.raises(ValueError):
        convert("10/3")
    with pytest.raises(ValueError):
        convert("1.5/3")
    with pytest.raises(ValueError):
        convert("1.5/4")
    with pytest.raises(ValueError):
        convert("3/5.5")
    with pytest.raises(ValueError):
        convert("5-10")
    with pytest.raises(ValueError):
        convert("x/y")
def test_gauge():
    assert gauge(75) == "75%"
    assert gauge(33) == "33%"
    assert gauge(67) == "67%"
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(100) == "F"
    assert gauge(99) == "F"
