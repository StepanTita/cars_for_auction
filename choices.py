import pandas as pd

_car_type_choices = None
_gear_box_choices = None
_model_choices = None
_fuel_choices = None
_brand_choices = None


def CatTypeChoices():
    return _car_type_choices


def GearBoxChoices():
    return _gear_box_choices


def ModelChoices():
    return _model_choices


def FuelChoices():
    return _fuel_choices


def BrandChoices():
    return _brand_choices


def init():
    global _car_type_choices, _gear_box_choices, _model_choices, _fuel_choices, _brand_choices
    data_path = 'data/'
    data_file = 'train.csv'
    data = pd.read_csv(data_path + data_file, index_col=0)
    data = data.dropna()
    _car_type_choices = data['type'].unique()
    _gear_box_choices = data['gearbox'].unique()
    _model_choices = data['model'].unique()
    _fuel_choices = data['fuel'].unique()
    _brand_choices = data['brand'].unique()

