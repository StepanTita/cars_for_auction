import numpy as np


def transform_year(d):
    d = d.copy()
    year = d['registration_year']

    d.loc[(year < 1900) & (year <= 20), 'registration_year'] += 2000
    d.loc[(year < 1900) & (year > 20), 'registration_year'] += 1900
    return d


def transform_power(d):
    d = d.copy()
    power = d['power']
    car_type = d['car_type']

    d.loc[power >= 500, 'power'] = np.nan
    d.loc[power < 25, 'power'] = np.nan
    return d


def transform_capacity(d):
    d = d.copy()
    engine = d['engine_capacity']
    d.loc[engine > 3.3, 'engine_capacity'] = np.nan
    d.loc[engine < 0.8, 'engine_capacity'] = np.nan
    return d


def transform_price(d):
    d = d.copy()
    d.loc[:, 'insurance_price'] = np.log(d['insurance_price'])
    if 'price' in d:
        d.loc[:, 'price'] = np.log(d['price'])
    return d


def prepare_data(data):
    transformers = [transform_year, transform_power, transform_capacity, transform_price]
    new_data = data
    for t in transformers:
        new_data = t(new_data)
    return new_data
