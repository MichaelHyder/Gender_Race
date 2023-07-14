#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 12:05:38 2023

@author: Michael Hyder Jr
Take Gender and Race data and create a dataframe with the counts of each type of entry as well as the 
percentage of the total that it represents.
"""

import numpy as np
import pandas as pd

#Import Data file where filename is a string of the files name

def read_file(filename):
    """ Read file and make DataFrame
    
    This functions reads in a file and turns it into a DataFrame.

"""
    return pd.read_csv(filename)


def percentage(data, total):
    """Make percentage of a subet.
    
    This function takes in a subset of data points  and the total number of data points and 
    finds the percentage that the subset makes up of the total. 

"""
    return data/len(total) * 100

def gen_race_output(df):   
    """Make final output table from DataFrame
    
    This function takes a DataFrame and returns a new DataFrame with the count and percent of total
    for each subset of the Race data. It finds the different names of the data points and groups 
    them together to find the subset of the data set that each one makes up. Then it maps each group 
    to its appropriate name for the output and creates the arrays that will label the data in the final
    table. It then creates the final DataFrame that will be outputted and rouns the results to 2 
    decimals.
    
    Args:
        df: DataFrame of the original data that we are inputting
        
    Returns:
        DataFrame with percentage and count of each data type.

"""

    df_clean = df.fillna(0)
    genders = df_clean["Race"].unique()
    counts = np.array([])
    grouped_race = df_clean.groupby(df_clean.Race)
    
    for i in genders:
        counts = np.append(counts, (len(grouped_race.get_group(i))))
        
    labels = lambda:["UNKNOWN" if (x == 0) else str(x) for x in genders]
    arrays = [np.array(["Race" for x in counts]),
              np.array(labels())
              ]
    
    df_final = pd.DataFrame([[counts[0], percentage(counts[0], df_clean)], [counts[1], percentage(counts[1], df_clean)],
               [counts[2], percentage(counts[2], df_clean)],[counts[3], percentage(counts[3], df_clean)],
               [counts[4], percentage(counts[4], df_clean)],[counts[5], percentage(counts[5], df_clean)]],
                           
        columns=["Overall = " + str(len(df_clean)), "Percent of Total (%)"],index=arrays)
    return df_final.round(2)
    
    
df = read_file("gender_race.csv")
print(gen_race_output(df))














