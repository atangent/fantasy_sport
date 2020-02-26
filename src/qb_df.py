import pandas as pd
import re


def merge_w_fantasy(statsFilePath, fantasyStatsFilePath):
    stats = df_setup(statsFilePath)
    fant_stats = df_setup(fantasyStatsFilePath)
    merged_df = pd.merge(stats, fant_stats, how="left", on=["Player", "Player"])
    return merged_df


def df_setup(filePath):
    df = pd.read_csv(filePath)
    df['Player'] = df['Player'].apply(player_name_clean)
    return df


def player_name_clean(player_id):  # Separates the Player's name from the weird ID tag
    clean_id = re.split(r'\+|\*|\\', player_id, 1)  # Splits the string at the first instance of a +, *, or \
    return clean_id[0]  # Returns just the player's name


qb_2013 = merge_w_fantasy("../data/QB Stats/2013_QBPassing_stats.csv", "../data/Fantasy Stats/2013_fantasy_stats.csv")
qb_2014 = merge_w_fantasy("../data/QB Stats/2014_QBPassing_stats.csv", "../data/Fantasy Stats/2014_fantasy_stats.csv")
qb_2015 = merge_w_fantasy("../data/QB Stats/2015_QBPassing_stats.csv", "../data/Fantasy Stats/2015_fantasy_stats.csv")
qb_2016 = merge_w_fantasy("../data/QB Stats/2016_QBPassing_stats.csv", "../data/Fantasy Stats/2016_fantasy_stats.csv")
qb_2017 = merge_w_fantasy("../data/QB Stats/2017_QBPassing_stats.csv", "../data/Fantasy Stats/2017_fantasy_stats.csv")
qb_2018 = merge_w_fantasy("../data/QB Stats/2018_QBPassing_stats.csv", "../data/Fantasy Stats/2018_fantasy_stats.csv")

# Join dataframes based on unique player id
qb_2013_2014 = pd.merge(qb_2013, qb_2014, how="left", on=["Player", "Player"])
qb_2014_2015 = pd.merge(qb_2014, qb_2015, how="left", on=["Player", "Player"])
qb_2015_2016 = pd.merge(qb_2015, qb_2016, how="left", on=["Player", "Player"])
qb_2016_2017 = pd.merge(qb_2016, qb_2017, how="left", on=["Player", "Player"])
qb_2017_2018 = pd.merge(qb_2017, qb_2018, how="left", on=["Player", "Player"])

# Concatenate all frames below one another
qb_dfs = [qb_2013_2014, qb_2014_2015, qb_2015_2016, qb_2016_2017, qb_2017_2018]
qb_df = pd.concat(qb_dfs, sort=False)
qb_df_csv = qb_df.to_csv('../data/Dataframes/qb_df.csv', index=None, header=True)

print(qb_df)

