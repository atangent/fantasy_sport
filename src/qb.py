import pandas as pd
import numpy as np

qb_2013 = pd.read_csv("../data/QB Stats/2013_QBPassing_stats.csv")
qb_2014 = pd.read_csv("../data/QB Stats/2014_QBPassing_stats.csv")
qb_2015 = pd.read_csv("../data/QB Stats/2015_QBPassing_stats.csv")
qb_2016 = pd.read_csv("../data/QB Stats/2016_QBPassing_stats.csv")
qb_2017 = pd.read_csv("../data/QB Stats/2017_QBPassing_stats.csv")
qb_2018 = pd.read_csv("../data/QB Stats/2018_QBPassing_stats.csv")

# Join dataframes based on unique player id
qb_2013_2014 = pd.merge(qb_2013, qb_2014, how="left", on=["Player", "Player"])
qb_2014_2015 = pd.merge(qb_2014, qb_2015, how="left", on=["Player", "Player"])
qb_2015_2016 = pd.merge(qb_2015, qb_2016, how="left", on=["Player", "Player"])
qb_2016_2017 = pd.merge(qb_2016, qb_2017, how="left", on=["Player", "Player"])
qb_2017_2018 = pd.merge(qb_2017, qb_2018, how="left", on=["Player", "Player"])

# Concatenate all frames below one another
qb_dfs = [qb_2013_2014, qb_2014_2015, qb_2015_2016, qb_2016_2017, qb_2017_2018]
qb_df = pd.concat(dfs)


