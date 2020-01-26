import pandas as pd

# Import csv files
wr_2013 = pd.read_csv("../data/Receiving "
                       "Stats/2013_Receiving_stats.csv")

wr_2014 = pd.read_csv("../data/Receiving "
                       "Stats/2014_Receiving_stats.csv")

wr_2015 = pd.read_csv("../data/Receiving "
                       "Stats/2015_Receiving_stats.csv")

wr_2016 = pd.read_csv("../data/Receiving "
                       "Stats/2016_Receiving_stats.csv")

wr_2017 = pd.read_csv("../data/Receiving "
                       "Stats/2017_Receiving_stats.csv")

wr_2018 = pd.read_csv("../data/Receiving "
                       "Stats/2018_Receiving_stats.csv")

# Join dataframes based on unique player id
wr_2013_2014 = pd.merge(wr_2013, wr_2014, how="left", on=["Player", "Player"])
wr_2014_2015 = pd.merge(wr_2014, wr_2015, how="left", on=["Player", "Player"])
wr_2015_2016 = pd.merge(wr_2015, wr_2016, how="left", on=["Player", "Player"])
wr_2016_2017 = pd.merge(wr_2016, wr_2017, how="left", on=["Player", "Player"])
wr_2017_2018 = pd.merge(wr_2017, wr_2018, how="left", on=["Player", "Player"])

# Concatenate all frames below one another
wr_dfs = [wr_2013_2014, wr_2014_2015, wr_2015_2016, wr_2016_2017, wr_2017_2018]
wr_df = pd.concat(wr_dfs)
