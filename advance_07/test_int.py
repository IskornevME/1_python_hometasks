import pytest


@pytest.mark.parametrize(
    "data, expected",
    [
        (2.5, 2),
        (1.6, 1),
        (3.4, 3),
        ('4', 4),
        (7.8, 7),
        (6453.3901, 6453),
        (float('473.23'), 473)
    ],
)
def test_base_int(data, expected):
    assert int(data) == expected


def test_int_letter_number():
    with pytest.raises(ValueError) as err:
        int('e2')
    assert str(err.value) == "invalid literal for int() with base 10: 'e2'"


def test_int_float_string():
    with pytest.raises(ValueError) as err:
        int('30321.345')
    assert str(err.value) == "invalid literal for int() with base 10: '30321.345'"


@pytest.mark.parametrize(
    "data, system, expected",
    [
        ('12', 8,  10),
        ('111001', 2, 57),
        ('20', 16, 32),
        ('210', 3, 21),
        ('31042', 5, 2022)
    ],
)
def test_convert_numeral_system(data, system, expected):
    assert int(data, system) == expected


def test_wrong_first_arg_for_convert():
    with pytest.raises(TypeError) as err:
        int(48, 16)
    assert str(err.value) == "int() can't convert non-string with explicit base"


@pytest.mark.parametrize(
    "data, expected",
    [
        (0b11, 3),
        (0o25, 21),
        (0xA5, 165)
    ],
)
def test_convert_with_prefix(data, expected):
    assert int(data) == expected


def test_wrong_prefix_for_convert():
    with pytest.raises(ValueError) as err:
        int('0b11')
    assert str(err.value) == "invalid literal for int() with base 10: '0b11'"
