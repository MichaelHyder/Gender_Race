import numpy as np
import pandas as pd
from . import utils

def gen_race_output(df):   
    """
    Make final output table from DataFrame.
    
    This function takes a DataFrame and returns a new DataFrame with the count and percent of total
    for each subset of the Race data. It finds the different names of the data points and groups 
    them together to find the subset of the data set that each one makes up. Then it maps each group 
    to its appropriate name for the output and creates the arrays that will label the data in the final
    table. It then creates the final DataFrame that will be outputted and rouns the results to 2 
    decimals.
    
    Parameters
    ----------
    df : DataFrame
        DataFrame of the original data we are inputting.
    

    Returns
    -------
    DataFrame
        DataFrame containing the desired output of the count of each gender as well as the percent
        of the total that each makes up.
    """

    # Step 1: Group the data based on the "Race" column and calculate count and percentage
    df_clean = df.fillna(0)
    df_clean["Race"] = df_clean["Race"].apply(lambda x: 'UNKNOWN' if x == 0 else x)
    grouped_data = df_clean.groupby("Race").size()
    total_data_entries = len(df_clean)
    counts = grouped_data.values
    percentages = [utils.percentage(count, total_data_entries) for count in counts]

    arrays = [np.array(["Race" for x in grouped_data.index]),
              np.array(grouped_data.index)
              ]

    # Step 2: Create a new DataFrame to display the results
    results_df = pd.DataFrame({
    "Overall = " + str(len(df_clean)): counts,
    "Percentage of Total (%)": percentages
    }, index=arrays)

    return results_df.round(2)








