import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as seabornInstance
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

data2013 = pd.read_csv("data/QB Stats/2013_QBPassing_stats.csv")
data2014 = pd.read_csv("data/QB Stats/2014_QBPassing_stats.csv")
data2015 = pd.read_csv("data/QB Stats/2015_QBPassing_stats.csv")
data2016 = pd.read_csv("data/QB Stats/2016_QBPassing_stats.csv")
data2017 = pd.read_csv("data/QB Stats/2017_QBPassing_stats.csv")
data2018 = pd.read_csv("data/QB Stats/2018_QBPassing_stats.csv")
