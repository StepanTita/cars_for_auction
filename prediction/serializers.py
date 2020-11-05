from rest_framework import serializers
import numpy as np

import choices

choices.init()

class PredictionSerializer(serializers.Serializer):
    engine_capacity = serializers.FloatField(default=np.nan)
    car_type = serializers.ChoiceField(choices=choices.CatTypeChoices())
    registration_year = serializers.IntegerField(default=0)
    gearbox = serializers.ChoiceField(choices=choices.GearBoxChoices())
    power = serializers.IntegerField(default=0)
    model = serializers.ChoiceField(choices=choices.ModelChoices())
    mileage = serializers.IntegerField(default=0)
    fuel = serializers.ChoiceField(choices=choices.FuelChoices())
    brand = serializers.ChoiceField(choices=choices.BrandChoices())
    damage = serializers.BooleanField(default=False)
    zipcode = serializers.IntegerField(default=0)
    insurance_price = serializers.FloatField(default=np.nan)


class PriceSerializer(serializers.Serializer):
    price = serializers.FloatField()
