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


rb_2013 = merge_w_fantasy("../data/Rushing Stats/2013_Rushing_stats.csv", "../data/Fantasy Stats/2013_fantasy_stats.csv")
rb_2014 = merge_w_fantasy("../data/Rushing Stats/2014_Rushing_stats.csv", "../data/Fantasy Stats/2014_fantasy_stats.csv")
rb_2015 = merge_w_fantasy("../data/Rushing Stats/2015_Rushing_stats.csv", "../data/Fantasy Stats/2015_fantasy_stats.csv")
rb_2016 = merge_w_fantasy("../data/Rushing Stats/2016_Rushing_stats.csv", "../data/Fantasy Stats/2016_fantasy_stats.csv")
rb_2017 = merge_w_fantasy("../data/Rushing Stats/2017_Rushing_stats.csv", "../data/Fantasy Stats/2017_fantasy_stats.csv")
rb_2018 = merge_w_fantasy("../data/Rushing Stats/2018_Rushing_stats.csv", "../data/Fantasy Stats/2018_fantasy_stats.csv")

rb_2019 = merge_w_fantasy("../data/Rushing Stats/2019_Rushing_stats.csv", "../data/Fantasy Stats/2019_fantasy_stats.csv")
rb_df_csv = rb_2019.to_csv('../data/Dataframes/rb_2019_df.csv', index=None, header=True)

# Join dataframes based on unique player id
rb_2013_2014 = pd.merge(rb_2013, rb_2014, how="left", on=["Player", "Player"])
rb_2014_2015 = pd.merge(rb_2014, rb_2015, how="left", on=["Player", "Player"])
rb_2015_2016 = pd.merge(rb_2015, rb_2016, how="left", on=["Player", "Player"])
rb_2016_2017 = pd.merge(rb_2016, rb_2017, how="left", on=["Player", "Player"])
rb_2017_2018 = pd.merge(rb_2017, rb_2018, how="left", on=["Player", "Player"])

# Concatenate all frames below one another
rb_dfs = [rb_2013_2014, rb_2014_2015, rb_2015_2016, rb_2016_2017, rb_2017_2018]
rb_df = pd.concat(rb_dfs, sort=False)
rb_df_csv = rb_df.to_csv('../data/Dataframes/rb_df.csv', index=None, header=True)
