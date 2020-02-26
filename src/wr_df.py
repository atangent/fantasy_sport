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


wr_2013 = merge_w_fantasy("../data/Receiving Stats/2013_Receiving_stats.csv", "../data/Fantasy Stats/2013_fantasy_stats.csv")
wr_2014 = merge_w_fantasy("../data/Receiving Stats/2014_Receiving_stats.csv", "../data/Fantasy Stats/2014_fantasy_stats.csv")
wr_2015 = merge_w_fantasy("../data/Receiving Stats/2015_Receiving_stats.csv", "../data/Fantasy Stats/2015_fantasy_stats.csv")
wr_2016 = merge_w_fantasy("../data/Receiving Stats/2016_Receiving_stats.csv", "../data/Fantasy Stats/2016_fantasy_stats.csv")
wr_2017 = merge_w_fantasy("../data/Receiving Stats/2017_Receiving_stats.csv", "../data/Fantasy Stats/2017_fantasy_stats.csv")
wr_2018 = merge_w_fantasy("../data/Receiving Stats/2018_Receiving_stats.csv", "../data/Fantasy Stats/2018_fantasy_stats.csv")

# Concatenate all frames below one another
wr_dfs = [wr_2013_2014, wr_2014_2015, wr_2015_2016, wr_2016_2017, wr_2017_2018]
wr_df = pd.concat(wr_dfs, sort=False)
wr_df_csv = wr_df.to_csv('../data/Dataframes/wr_df.csv', index=None, header=True)

