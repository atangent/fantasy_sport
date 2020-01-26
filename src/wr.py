import pandas as pd
import numpy as np
from numpy import genfromtxt

# Import csv files
csv2013 = pd.read_csv("../data/Receiving "
                       "Stats/2013_Receiving_stats.csv",
                      keep_default_na=False, na_values=[""])

csv2014 = pd.read_csv("../data/Receiving "
                       "Stats/2014_Receiving_stats.csv")

csv2015 = pd.read_csv("../data/Receiving "
                       "Stats/2015_Receiving_stats.csv")

csv2016 = pd.read_csv("../data/Receiving "
                       "Stats/2016_Receiving_stats.csv")

csv2017 = pd.read_csv("../data/Receiving "
                       "Stats/2017_Receiving_stats.csv")

csv2018 = pd.read_csv("../data/Receiving "
                       "Stats/2018_Receiving_stats.csv")

# Join dataframes based on unique player id
df1314 = pd.merge(csv2013, csv2014, how="left", on=["Player", "Player"])