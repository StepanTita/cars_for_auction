import os

import joblib

from cars_from_auction import settings


class Context:
    def __init__(self):
        self._model = None

    # load the latest model
    def get_model(self):
        if self._model is None:
            model_path = 'models/'
            model_name = settings.MODEL
            model_file = f'{model_name}'

            reg = joblib.load(model_path + model_file)
            self._model = reg
        return self._model
