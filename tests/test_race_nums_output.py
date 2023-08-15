import pytest
import pandas as pd
import numpy
from . import race_nums
from . import utils

def test_gen_race_output():
    """
    Test the gen_race_output function.

    This function tests the gen_race_output function by creating a DataFrame and passing it 
    into the function we are testing, then manually creating what the function should return,
    and asserting if the expected output matches the actual output.
    """

    data = {
        'Race': ['2106-3', '2054-5', '1002-5', '2028-9', '2076-8',0],
    }
    df = pd.DataFrame(data)
    
    # Call the function to be tested
    output = race_nums.gen_race_output(df)
    
    # Define the expected output DataFrame
    expected_output = pd.DataFrame(
        [
            [1, utils.percentage(1, 6)],
            [1, utils.percentage(1, 6)],
            [1, utils.percentage(1, 6)],
            [1, utils.percentage(1, 6)],
            [1, utils.percentage(1, 6)],
            [1, utils.percentage(1, 6)],
        ],
        columns=["Overall = 6", "Percentage of Total (%)"],
        index=[["Race", "Race", "Race", "Race","Race", "Race"], ['1002-5', '2028-9', '2054-5', '2076-8', '2106-3','UNKNOWN']]
    ).round(2)

    # Compare the function's output with the expected output
    pd.testing.assert_frame_equal(output, expected_output)

