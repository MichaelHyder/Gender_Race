import pandas as pd

#Import Data file where filename is a string of the files name
def read_file(filename):
    """
    Read file and make DataFrame.
    This functions reads in a file and turns it into a DataFrame.

    Parameters
    ----------
    filename : string
        Name of the file as a string.
    

    Returns
    -------
    DataFrame
        DataFrame containing the data from the csv file.
    """
    return pd.read_csv(filename)


def percentage(data, total):
    """
    Make percentage of a subet.
    This function takes in a subset of data points and the total number of data points and 
    finds the percentage that the subset makes up of the total. 

    Parameters
    ----------
    data : integer
        The number of data points we want to find the percentage of.
    
    total : integer
        The total number of data points in the dataset.

    Returns
    -------
    Float
        The percentage of the total number of data points that the subset represents. 
    """
    if total == 0:
        raise ValueError("The 'whole' value cannot be zero.")
    
    return data/total * 100





