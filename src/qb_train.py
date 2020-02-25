import pandas as pd
import numpy as np
import sklearn
import pickle
from sklearn import linear_model
from sklearn.metrics import median_absolute_error
from sklearn.feature_selection import f_regression


# HOW TO CALCULATE FANTASY POINTS
# passing yards - 1 point /25 yards
# passing touchdowns - 4 points
# passing interceptions - -2 points
# rushing yards - 1 point / 10 yards
# rushing touchdowns - 6 points
# receptions *only PPR scoring [points per reception] - 1 point
# receiving yards - 1 point / 10 yards
# receiving touchdowns - 6 points
# 2-point conversions - 2 points
# fumbles lost - -2 points
# fumble recovered before touchdown - 6 points

def get_model(pickle_path):
    pickle_in = open(pickle_path, "rb")
    m = pickle.load(pickle_in)
    return m


def feature_selection(X, Y):
    F, pval = f_regression(X, Y, center=True)
    return F, pval


def score_model(test_outputs, true_outputs):
    score = median_absolute_error(true_outputs, test_outputs)
    return score


def create_model(independent, dependent, pickle_path):
    best_score = 100000
    for _ in range(3000):
        x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(independent, dependent, test_size=0.2)
        linear = linear_model.LinearRegression()
        linear.fit(x_train, y_train)
        predict = linear.predict(x_test)
        median = score_model(predict, y_test)
        if median < best_score:
            best_score = median
            best_x_test = x_test
            best_y_test = y_test
            with open(pickle_path, "wb") as f:
                pickle.dump(linear, f)
    return best_x_test, best_y_test


def full_process(stat_features, predict_stat, stat_name):
    x = np.array(stat_features.drop(columns=predict_stat))
    y = np.array(stat_features[predict_stat].fillna(0))
    file_path = '../data/pickle/' + stat_name + '.pickle'

    x_true, y_true = create_model(x, y, file_path)
    stat_model = get_model(file_path)
    y_pred = stat_model.predict(x_true)
    score = score_model(y_pred, y_true)
    return y_pred, y_true, score


data = pd.read_csv('../data/Dataframes/qb_df.csv')

p_yard_features = data[['Cmp_x', 'Yds_x', 'Y/G_x', 'Rate_x', 'FantPt_x', 'Yds_y']].fillna(0)
predict_p_yard = 'Yds_y'

p_tds_features = data[['Cmp%_x', 'TD_x', 'TD%_x', 'Int_x', 'Int%_x', 'Rate_x', 'FantPt_x', 'TD_y']].fillna(0)
predict_p_tds = 'TD_y'

p_ints_features = data[['Cmp%_x', 'Int_x', 'Int%_x', 'Rate_x', 'ANY/A_x', 'FantPt_x', 'Int_y']].fillna(0)
predict_p_ints = 'Int_y'

p_yard_pred, p_yard_true, p_yard_score = full_process(p_yard_features, predict_p_yard, 'passing_yards')
p_tds_pred, p_tds_true, p_tds_score = full_process(p_tds_features, predict_p_tds, 'passing_tds')
p_ints_pred, p_ints_true, p_ints_score = full_process(p_ints_features, predict_p_ints, 'passing_ints')


print("Median Error (yards): " + str(round(p_yard_score, 1)) + "\nMedian Error (fantasy points): "
      + str(round(p_yard_score/25, 1)))

# for i in range(len(p_yard_pred)):
#     if p_yard_true[i] > 100:
#         print("Predicted: " + str(np.round(p_yard_pred[i], 1)) + "\tActual: " + str(p_yard_true[i]))

print("Median Error (TDs): " + str(round(p_tds_score, 1)) + "\nMedian Error (fantasy points): "
       + str(round(p_tds_score*4, 1)))

# for i in range(len(p_tds_pred)):
#     if p_yard_true[i] > 3:
#         print("Predicted: " + str(np.round(p_tds_pred[i], 0)) + "\tActual: " + str(p_tds_true[i]))

print("Median Error (Ints): " + str(round(p_ints_score, 1)) + "\nMedian Error (fantasy points): "
      + str(round(p_ints_score*2, 1)))

# for i in range(len(p_tds_pred)):
#     if p_yard_true[i] > 3:
#         print("Predicted: " + str(np.round(p_tds_pred[i], 0)) + "\tActual: " + str(p_tds_true[i]))
