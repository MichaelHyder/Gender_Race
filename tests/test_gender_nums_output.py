import pytest
import pandas as pd
import numpy

from . import gender_nums
from . import utils

# Test case 1: Test the function with sample data
def test_gen_gender_output():
    """
    Test the gen_gender_output function.

    This function tests the gen_gender_output function by creating a DataFrame and passing it 
    into the function we are testing, then manually creating what the function should return,
    and asserting if the expected output matches the actual output.
    """

    data = {
        'Gender': ['M', 'F', 'M', 'O', 'F', 'F', 'M', 'M', 'M']
    }
    df = pd.DataFrame(data)
    
    # Call the function to be tested
    output = gender_nums.gen_gender_output(df)
    
    # Define the expected output DataFrame
    expected_output = pd.DataFrame(
        [
            [3, utils.percentage(3, 9)],
            [5, utils.percentage(5, 9)],
            [1, utils.percentage(1, 9)],
        ],
        columns=["Overall = 9", "Percentage of Total (%)"],
        index=[["Gender", "Gender", "Gender"], ["FEMALE", "MALE", "OTHER"]]
    ).round(2)
    
    # Compare the function's output with the expected output
    pd.testing.assert_frame_equal(output, expected_output)