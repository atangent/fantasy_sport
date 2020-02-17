import pandas as pd
import numpy as np
from sklearn import datasets, linear_model
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt
import sklearn
from sklearn.utils import shuffle
import pickle
from matplotlib import style
import os

data = pd.read_csv('qb_df.csv')



print(data)
