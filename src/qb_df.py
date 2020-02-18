import pandas as pd
import re


def player_name_clean(player_id):  # Separates the Player's name from the weird ID tag
    clean_id = re.split(r'\+|\*|\\', player_id, 1)  # Splits the string at the first instance of a +, *, or \
    return clean_id[0]  # Returns just the player's name


qb_2013 = pd.read_csv("../data/QB Stats/2013_QBPassing_stats.csv")
qb_2013['Player'] = qb_2013['Player'].apply(player_name_clean)  # Cleans the Player's name column
qb_2014 = pd.read_csv("../data/QB Stats/2014_QBPassing_stats.csv")
qb_2014['Player'] = qb_2014['Player'].apply(player_name_clean)
qb_2015 = pd.read_csv("../data/QB Stats/2015_QBPassing_stats.csv")
qb_2015['Player'] = qb_2015['Player'].apply(player_name_clean)
qb_2016 = pd.read_csv("../data/QB Stats/2016_QBPassing_stats.csv")
qb_2016['Player'] = qb_2016['Player'].apply(player_name_clean)
qb_2017 = pd.read_csv("../data/QB Stats/2017_QBPassing_stats.csv")
qb_2017['Player'] = qb_2017['Player'].apply(player_name_clean)
qb_2018 = pd.read_csv("../data/QB Stats/2018_QBPassing_stats.csv")
qb_2018['Player'] = qb_2018['Player'].apply(player_name_clean)

# Join dataframes based on unique player id
qb_2013_2014 = pd.merge(qb_2013, qb_2014, how="left", on=["Player", "Player"])
qb_2014_2015 = pd.merge(qb_2014, qb_2015, how="left", on=["Player", "Player"])
qb_2015_2016 = pd.merge(qb_2015, qb_2016, how="left", on=["Player", "Player"])
qb_2016_2017 = pd.merge(qb_2016, qb_2017, how="left", on=["Player", "Player"])
qb_2017_2018 = pd.merge(qb_2017, qb_2018, how="left", on=["Player", "Player"])

# Concatenate all frames below one another
qb_dfs = [qb_2013_2014, qb_2014_2015, qb_2015_2016, qb_2016_2017, qb_2017_2018]
qb_df = pd.concat(qb_dfs)
qb_df_csv = qb_df.to_csv('../data/Dataframes/qb_df.csv', index=None, header=True)

print(qb_2013_2014)

