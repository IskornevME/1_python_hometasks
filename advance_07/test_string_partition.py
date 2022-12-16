import pytest


@pytest.mark.parametrize(
    "data, separator, expected",
    [
        (
            "simple example for separation",
            "example",
            ("simple ", "example", " for separation")
         ),
        (
            "no data from left of sep",
            "no",
            ("", "no", " data from left of sep")
        ),
        (
            "no data from right of sep",
            "sep",
            ("no data from right of ", "sep", "")
        )

    ],
)
def test_base_partition(data, separator, expected):
    assert data.partition(separator) == expected


def test_no_separator():
    string = "By the order of peaky blinders"
    separator = "Shelby"
    expected = ("By the order of peaky blinders", "", "")
    assert string.partition(separator) == expected


def test_register():
    string = "this text HaS strange separator"
    separator = "has"
    expected = ("this text HaS strange separator", "", "")
    assert string.partition(separator) == expected

    string = "this text has usual separator"
    separator = "HaS"
    expected = ("this text has usual separator", "", "")
    assert string.partition(separator) == expected


def test_many_separator():
    string = "and at once I know"
    separator = " "
    expected = ("and", " ", "at once I know")
    assert string.partition(separator) == expected

    string = "   three spaces from left"
    separator = " "
    expected = ("", " ", "  three spaces from left")
    assert string.partition(separator) == expected

    string = "three spaces from right from   "
    separator = "from "
    expected = ("three spaces ", "from ", "right from   ")
    assert string.partition(separator) == expected


def test_no_args():
    string = "One ring to rule them all"
    with pytest.raises(TypeError) as err:
        string.partition()
    assert str(err.value) == "str.partition() takes exactly one argument (0 given)"


def test_empty_sep():
    string = "One ring to rule them all"
    separator = ""
    with pytest.raises(ValueError) as err:
        string.partition(separator)
    assert str(err.value) == "empty separator"
