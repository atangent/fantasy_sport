import pickle
import pandas as pd
import re

def player_name_clean(player_id):  # Separates the Player's name from the weird ID tag
    clean_id = re.split(r'\+|\*|\\', player_id, 1)  # Splits the string at the first instance of a +, *, or \
    return clean_id[0]  # Returns just the player's name

# Loading Models
passing_ints = pickle.load(open('../data/pickle/passing_ints.csv', "rb"))
passing_tds = pickle.load(open('../data/pickle/passing_tds.csv', "rb"))
passing_yards = pickle.load(open('../data/pickle/passing_yards.csv', "rb"))
receiving_fumbles = pickle.load(open('../data/pickle/receiving_fumbles.csv', "rb"))
receiving_tds = pickle.load(open('../data/pickle/receiving_tds.csv', "rb"))
receiving_yards = pickle.load(open('../data/pickle/receiving_yards.csv', "rb"))
rushing_fumbles = pickle.load(open('../data/pickle/rushing_fumbles.csv', "rb"))
rushing_tds = pickle.load(open('../data/pickle/rushing_tds.csv', "rb"))
rushing_yards = pickle.load(open('../data/pickle/rushing_yards.csv', "rb"))

passing_data = pd.read_csv('../data/Dataframes/qb_2019_df.csv')
rushing_data = pd.read_csv('../data/Dataframes/rb_2019_df.csv')
receiving_data = pd.read_csv('../data/Dataframes/wr_2019_df.csv')



