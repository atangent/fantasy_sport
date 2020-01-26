import pandas as pd

# Import csv files
rb_2013 = pd.read_csv("../data/Rushing "
                       "Stats/2013_Rushing_stats.csv")

rb_2014 = pd.read_csv("../data/Rushing "
                       "Stats/2014_Rushing_stats.csv")

rb_2015 = pd.read_csv("../data/Rushing "
                       "Stats/2015_Rushing_stats.csv")

rb_2016 = pd.read_csv("../data/Rushing "
                       "Stats/2016_Rushing_stats.csv")

rb_2017 = pd.read_csv("../data/Rushing "
                       "Stats/2017_Rushing_stats.csv")

rb_2018 = pd.read_csv("../data/Rushing "
                       "Stats/2018_Rushing_stats.csv")

# Join dataframes based on unique player id
rb_2013_2014 = pd.merge(rb_2013, rb_2014, how="left", on=["Player", "Player"])
df_2014_2015 = pd.merge(csv2014, csv2015, how="left", on=["Player", "Player"])
df_2015_2016 = pd.merge(csv2015, csv2016, how="left", on=["Player", "Player"])
df_2016_2017 = pd.merge(csv2016, csv2017, how="left", on=["Player", "Player"])
df_2017_2018 = pd.merge(csv2017, csv2018, how="left", on=["Player", "Player"])

# Concatenate all frames below one another
dfs = [df_2013_2014, df_2014_2015, df_2015_2016, df_2016_2017, df_2017_2018]
rb_df = pd.concat(dfs)
