import pytest

from src.grades import average, letter_grade


def test_average():
    assert average([80, 90, 100]) == 90


def test_average_empty_list():
    with pytest.raises(ValueError):
        average([])


def test_letter_grade():
    assert letter_grade(95) == "A"
    assert letter_grade(80) == "B"
    assert letter_grade(65) == "C"
    assert letter_grade(30) == "F"


def test_letter_grade_out_of_range():
    with pytest.raises(ValueError):
        letter_grade(150)
