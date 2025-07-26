import pytest
from testing import calculate_age
from datetime import date

CURRENT_YEAR = date.today().year

@pytest.mark.parametrize(
    "birth_year, expected", [
        (2000, CURRENT_YEAR - 2000),
        (1990, CURRENT_YEAR - 1990),
        (CURRENT_YEAR, 0),
        (0, CURRENT_YEAR),
    ])
def test_calculate_age_valid_cases(birth_year, expected):
    assert calculate_age(birth_year) == expected


@pytest.mark.parametrize(
    "birth_year", [
        CURRENT_YEAR + 1,
        CURRENT_YEAR + 100,
    ])
def test_calculate_age_invalid_cases(birth_year):
    with pytest.raises(ValueError):
        calculate_age(birth_year)
