import os

import pandas as pd

from prediction import prepare
import lightgbm as lgb

import joblib
from datetime import datetime

print(os.getcwd())

def train():
    data_path = 'data/'
    data_file = 'train.csv'
    data = pd.read_csv(data_path + data_file, index_col=0)
    data = prepare.prepare_data(data)
    cdata = data
    for c in cdata.select_dtypes(include='object'):
        cdata[c] = cdata[c].astype('category')

    X, y = cdata.drop(['price'], axis=1), cdata['price']

    best = {
        'objective': 'regression_l2',
        'num_leaves': 98,
        'num_iterations': 1200,
        'min_data_in_leaf': 36,
        'log_target': True,
        'learning_rate': 0.018000000000000002,
        'feature_fraction': 0.85,
        'bagging_freq': 10,
        'bagging_fraction': 0.75
    }

    reg = lgb.LGBMRegressor(metric='mape', n_estimators=500, **best)
    reg.fit(X, y)

    model_path = 'models/'
    v = len(os.listdir(model_path))
    model_file = f'lgbm-v{v}-{datetime.now()}.model'.replace(' ', '_')

    joblib.dump(reg, model_path + model_file)


if __name__ == "__main__":
    train()
