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
df_2013_2014 = pd.merge(csv2013, csv2014, how="left", on=["Player", "Player"])
df_2014_2015 = pd.merge(csv2014, csv2015, how="left", on=["Player", "Player"])
df_2015_2016 = pd.merge(csv2015, csv2016, how="left", on=["Player", "Player"])
df_2016_2017 = pd.merge(csv2016, csv2017, how="left", on=["Player", "Player"])
df_2017_2018 = pd.merge(csv2017, csv2018, how="left", on=["Player", "Player"])

# Concatenate all frames below one another
dfs = [df_2013_2014, df_2014_2015, df_2015_2016, df_2016_2017, df_2017_2018]
entire_df = pd.concat(dfs)
