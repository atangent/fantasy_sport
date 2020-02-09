import pandas as pd
from sklearn import datasets, linear_model
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt
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
# Code to train model for best from article 
data = pd.read_csv("student-mat.csv", sep=";")
data = data[["G1", "G2", "G3", "studytime", "failures", "absences"]]
predict = "G3"
X = np.array(data.drop([predict], 1))
y = np.array(data[predict])
best = 0
for _ in range(30):
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.1)
    linear = linear_model.LinearRegression()
    linear.fit(x_train, y_train)
    acc = linear.score(x_test, y_test)
    if acc > best:
        best = acc
        with open("studentmodel.pickle", "wb") as f:
            pickle.dump(linear, f)

print(best)
