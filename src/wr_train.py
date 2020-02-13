import pandas as pd
import numpy as np
from sklearn import datasets, linear_model
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt
import sklearn
from sklearn.utils import shuffle
import pickle
from matplotlib import style
"""
HOW TO CALCULATE FANTASY POINTS
passing yards - 1 point /25 yards
passing touchdowns - 4 points
passing interceptions - -2 points
rushing yards - 1 point / 10 yards
rushing touchdowns - 6 points
receptions *only PPR scoring [points per reception] - 1 point
receiving yards - 1 point / 10 yards
receiving touchdowns - 6 points
2-point conversions - 2 points
fumbles lost - -2 points
fumble recovered before touchdown - 6 points
"""
# Link to csv
data = pd.read_csv('../data/Dataframes/wr_df.csv', sep=",")
# Trim data with only inputs needed
data = data[["Age_x", "G_x", "Gs_x", "Tgt_x", "Rec_x", "Ctch%_x", "Yds_x", "Y/R_x", "TD_x", "1D_x",
             "Lng_x", "Y/Tgt_x", "R/G_x", "Y/G_x", "Fmb_x", "FanPt_x", "FanPosRank_x", "FanOvRank_x"]]
# Separate data
predict = "FanPt_y"
# Features
x = np.array(data[drop([predict], 1)])
# Label
y = np.array(data[predict])
# Split into training testing
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size = 0.2)

# Fun part. Train multiple models. Linear regression on steroids
best = 0
for _ in range(50):
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size = 0.2)
    linear = linear_model.LinearRegression()
    linear.fit(x_train, y_train)
    accuracy = linear.score(x_test, y_test)
    print("Accuracy of model: " + str(accuracy))
    # If current model has better score than max, save as max
    if accuracy > best:
        best = accuracy
        with open("../data/pickle/wr.pickle", "wb") as f:
            pickle.dump(linear, f)

# Load model
pickle_in = open("../data/pickle/wr.pickle", "rb")
linear = pickle.load(pickle_in)

print("Coefficient: ", linear.coef_)
print("Intercept: ", linear.intercept_)

predictions = linear.predict(x_test)
for x in range(len(predictions)):
    print(predictions[x], x_test[x], y_test[x])

# Plot model
plot = "failures"
plt.scatter(data[plot], data["G3"])
plt.legend(loc=4)
plt.xlabel(plot)
plt.ylabel("Fantasy points")
plt.show()

