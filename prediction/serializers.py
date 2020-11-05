from rest_framework import serializers

class PredictionSerializer(serializers.Serializer):
    engine_capacity = serializers.FloatField()
    car_type = serializers.CharField()
    registration_year = serializers.IntegerField()
    gearbox = serializers.CharField()
    power = serializers.IntegerField()
    model = serializers.CharField()
    mileage = serializers.IntegerField()
    fuel = serializers.CharField()
    brand = serializers.CharField()
    damage = serializers.BooleanField()
    zipcode = serializers.IntegerField()
    insurance_price = serializers.FloatField()


class PriceSerializer(serializers.Serializer):
    price = serializers.FloatField()
