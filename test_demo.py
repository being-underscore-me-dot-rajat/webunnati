import pytest
import demo


def test_add():
    assert demo.add(2, 3) == 5


def test_sub():
    assert demo.sub(10, 4) == 6


def test_mul():
    assert demo.mul(3, 4) == 12


def test_div():
    assert demo.div(8, 2) == 4


def test_power():
    assert demo.power(2, 3) == 8


def test_bad_calc_raises_runtime_errors():
    with pytest.raises(TypeError):
        demo.add("7", 8)

    with pytest.raises(ZeroDivisionError):
        demo.div(10, 0)

    with pytest.raises(NameError):
        print(unknown_value)
