import pytest
from . import utils

def test_percentage_positive_values():
    """
    Test the Percentage function.

    This function tests the percentage function to ensure that when it takes 2 positive values,
    it returns a result that is within +- 1*10^7 of the expected answer.
    """
    percent = utils.percentage(25, 100)
    result = percent - 25.0
    assert 0.0001 >= result >= -0.0001

    percent = utils.percentage(30, 50)
    result = percent - 60.0
    assert 0.0001 >= result >= -0.0001

    percent = utils.percentage(3, 10)
    result = percent - 30.0
    assert 0.0001 >= result >= -0.0001

# Test case 2: Test the percentage calculation with zero values.
def test_percentage_with_zero_values():
    """
    Test the Percentage function.

    This function tests the percentage function to ensure that when it takes a value of 0 as the
    total number of data points it returns an error because it cannot divide by 0.
    """

    percent = utils.percentage(0, 1000)
    result = percent - 0.0
    assert 0.0001 >= result >= -0.0001

    with pytest.raises(ValueError):
        utils.percentage(100, 0)

# Test case 3: Test the percentage calculation with negative values.
def test_percentage_with_negative_values():
    """
    Test the Percentage function.

    This function tests the percentage function to ensure that when it takes 2 negative values 
    or 1 negative and 1 positive value it returns a result that is within +- 1*10^7 of the 
    expected answer.
    """
    percent = utils.percentage(-20, 200)
    result = percent + 10.0
    assert 0.0001 >= result >= -0.0001

    percent = utils.percentage(50, -100)
    result = percent + 50.0
    assert 0.0001 >= result >= -0.0001

    percent = utils.percentage(-5, -50)
    result = percent - 10.0
    assert 0.0001 >= result >= -0.0001
    