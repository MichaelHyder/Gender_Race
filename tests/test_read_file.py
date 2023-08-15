import pandas as pd
import pytest
from . import utils

def sample_csv(tmp_path):
    """
        Create a sample csv file.

        This function creates a sample csv file that will be used to test our read_file 
        function.
         """

    # Create a sample CSV file
    csv_file = tmp_path / 'sample.csv'
    data = {'Name': ['John', 'Alice', 'Bob'],
            'Age': [25, 32, 41],
            'City': ['New York', 'Paris', 'London']}
    df = pd.DataFrame(data)
    df.to_csv(csv_file, index=False)
    return csv_file

def test_read_csv_to_dataframe():
    """ 
        Test the read_file function.

        This function tests the read_file function by using it to read the sample csv file
        that was created in the function above, then creating a DataFrame that the csv file
        should match ones its been read. Then, it compares the actual DataFrame to the expected
        one.
        """
        
    # Call the function to read the CSV file
    df_actual = utils.read_file("sample.csv")

    # Prepare the expected DataFrame
    data = {'Name': ['John', 'Alice', 'Bob'],
            'Age': [25, 32, 41],
            'City': ['New York', 'Paris', 'London']}
    df_expected = pd.DataFrame(data)

    # Assert that the DataFrames are equal
    pd.testing.assert_frame_equal(df_actual,df_expected)



