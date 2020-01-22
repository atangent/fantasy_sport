import pandas as pd
import numpy as np
from numpy import genfromtxt

# Import csv files
csv2013 = pd.read_csv("/Users/amytang/OneDrive - Queen\'s University/QMIND/data/Receiving "
                       "Stats/2013_Receiving_stats.csv",
                      keep_default_na=False, na_values=[""])

csv2014 = pd.read_csv("/Users/amytang/OneDrive - Queen\'s University/QMIND/data/Receiving "
                       "Stats/2014_Receiving_stats.csv")

csv2015 = pd.read_csv("/Users/amytang/OneDrive - Queen\'s University/QMIND/data/Receiving "
                       "Stats/2015_Receiving_stats.csv")

csv2016 = pd.read_csv("/Users/amytang/OneDrive - Queen\'s University/QMIND/data/Receiving "
                       "Stats/2016_Receiving_stats.csv")

csv2017 = pd.read_csv("/Users/amytang/OneDrive - Queen\'s University/QMIND/data/Receiving "
                       "Stats/2017_Receiving_stats.csv")

csv2018 = pd.read_csv("/Users/amytang/OneDrive - Queen\'s University/QMIND/data/Receiving "
                       "Stats/2018_Receiving_stats.csv")

# Concatenate arrays side by side
df1314 = pd.concat([csv2013, csv2014], axis=1)

# Join dataframes based on unique player id
