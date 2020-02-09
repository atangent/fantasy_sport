import pandas as pd

# Import regular stats
wr_2013 = pd.read_csv("../data/Receiving Stats/2013_Receiving_stats.csv")
wr_2014 = pd.read_csv("../data/Receiving Stats/2014_Receiving_stats.csv")
wr_2015 = pd.read_csv("../data/Receiving Stats/2015_Receiving_stats.csv")
wr_2016 = pd.read_csv("../data/Receiving Stats/2016_Receiving_stats.csv")
wr_2017 = pd.read_csv("../data/Receiving Stats/2017_Receiving_stats.csv")
wr_2018 = pd.read_csv("../data/Receiving Stats/2018_Receiving_stats.csv")

# Import fantasy stats
wr_fantasy_2013 = pd.read_csv("../data/Fantasy Stats/2013_fantasy_stats.csv")
wr_fantasy_2014 = pd.read_csv("../data/Fantasy Stats/2014_fantasy_stats.csv")
wr_fantasy_2015 = pd.read_csv("../data/Fantasy Stats/2015_fantasy_stats.csv")
wr_fantasy_2016 = pd.read_csv("../data/Fantasy Stats/2016_fantasy_stats.csv")
wr_fantasy_2017 = pd.read_csv("../data/Fantasy Stats/2017_fantasy_stats.csv")
wr_fantasy_2018 = pd.read_csv("../data/Fantasy Stats/2018_fantasy_stats.csv")

# Join stats w fantasy ranks and points
wr_all_2013 = pd.merge(wr_2013, wr_fantasy_2013, how="left", on=["Player", "Player"])
wr_all_2014 = pd.merge(wr_2014, wr_fantasy_2014, how="left", on=["Player", "Player"])
wr_all_2015 = pd.merge(wr_2015, wr_fantasy_2015, how="left", on=["Player", "Player"])
wr_all_2016 = pd.merge(wr_2016, wr_fantasy_2016, how="left", on=["Player", "Player"])
wr_all_2017 = pd.merge(wr_2017, wr_fantasy_2017, how="left", on=["Player", "Player"])
wr_all_2018 = pd.merge(wr_2018, wr_fantasy_2018, how="left", on=["Player", "Player"])

# Join dataframes based on unique player id
wr_2013_2014 = pd.merge(wr_all_2013, wr_all_2014, how="left", on=["Player", "Player"])
wr_2014_2015 = pd.merge(wr_all_2014, wr_all_2015, how="left", on=["Player", "Player"])
wr_2015_2016 = pd.merge(wr_all_2015, wr_all_2016, how="left", on=["Player", "Player"])
wr_2016_2017 = pd.merge(wr_all_2016, wr_all_2017, how="left", on=["Player", "Player"])
wr_2017_2018 = pd.merge(wr_all_2017, wr_all_2018, how="left", on=["Player", "Player"])

# Concatenate all frames below one another
wr_dfs = [wr_2013_2014, wr_2014_2015, wr_2015_2016, wr_2016_2017, wr_2017_2018]
wr_df = pd.concat(wr_dfs, sort=False)
wr_df_csv = wr_df.to_csv('../data/Dataframes/wr_df.csv')
