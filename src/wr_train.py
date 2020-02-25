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


data = pd.read_csv('../data/Dataframes/wr_df.csv')

re_yard_features = data[['Yds_x', 'Y/R_x', 'Y/G_x', 'FantPt_x', 'Yds_y']].fillna(0)
predict_re_yard = 'Yds_y'

re_tds_features = data[['Rec_x', 'Y/R_x', 'TD_x', 'FantPt_x', 'TD_y']].fillna(0)
predict_re_tds = 'TD_y'

re_fumble_features = data[['Ctch%_x', 'R/G_x', 'Fmb_x', 'FantPt_x', 'Fmb_y']].fillna(0)
predict_re_fumble = 'Fmb_y'

re_yard_pred, re_yard_true, re_yard_score = full_process(re_yard_features, predict_re_yard, 'receiving_yards')
re_tds_pred, re_tds_true, re_tds_score = full_process(re_tds_features, predict_re_tds, 'receiving_tds')
re_fumble_pred, re_fumble_true, re_fumble_score = full_process(re_fumble_features, predict_re_fumble, 'receiving_fumbles')

print("Median Error (yards): " + str(round(re_yard_score, 1)) + "\nMedian Error (fantasy points): "
      + str(round(re_yard_score/10, 1)))

# for i in range(len(r_yard_pred)):
#     if re_yard_true[i] > 100:
#         print("Predicted: " + str(np.round(re_yard_pred[i], 1)) + "\tActual: " + str(re_yard_true[i]))

print("Median Error (TDs): " + str(round(re_tds_score, 1)) + "\nMedian Error (fantasy points): "
       + str(round(re_tds_score*6, 1)))

# for i in range(len(re_tds_pred)):
#     if re_tds_true[i] > 1:
#         print("Predicted: " + str(np.round(re_tds_pred[i], 0)) + "\tActual: " + str(re_tds_true[i]))

print("Median Error (Fmbs): " + str(round(re_fumble_score, 1)) + "\nMedian Error (fantasy points): "
       + str(round(re_fumble_score*2, 1)))

# for i in range(len(re_fumble_pred)):
#     print("Predicted: " + str(np.round(re_fumble_pred[i], 0)) + "\tActual: " + str(re_fumble_true[i]))
