from rest_framework import serializers
from django.core.exceptions import ObjectDoesNotExist
from .models import Manufacturer, CarModel, Car
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned


class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = ['manufacturing_date']
       

class CarModelSerializer(serializers.ModelSerializer):
    car_set = CarSerializer(many=True)
    
    class Meta:
        model = CarModel
        fields = ['name', 'production_year', 'car_set']
        read_only_fields = ['car_set']


class ManufacturerSerializer(serializers.ModelSerializer):
    carmodel_set = CarModelSerializer(many=True)
    
    class Meta:
        model = Manufacturer
        fields = ['name', 'carmodel_set']

    
    def create(self, validated_data):
        models_data = validated_data.pop('carmodel_set')
        manufacturer, _ = Manufacturer.objects.get_or_create(**validated_data)
        for model_data in models_data:
            cars = model_data.pop('car_set')
            model_var, _ = CarModel.objects.get_or_create(
                manufacturer=manufacturer, **model_data)
            for car in cars:
                Car.objects.create(car_model=model_var, **car)
        return manufacturer

    def update(self, instance, validated_data):
        models_data = validated_data.pop('carmodel_set')
        for model_data in models_data:
            cars = model_data.pop('car_set')
            model_var, _ = CarModel.objects.get_or_create(manufacturer=instance, **model_data)
            for car in cars:
                Car.objects.create(car_model=model_var, **car)
        return instance

    
    def is_valid(self, raise_exception=False):
        if hasattr(self, 'initial_data'):
            try:
                obj = Manufacturer.objects.get(name=self.initial_data["name"])

            except (ObjectDoesNotExist, MultipleObjectsReturned):
                return super().is_valid(raise_exception)
            else:
                self.instance = obj
                return super().is_valid(raise_exception)
        else:
            return super().is_valid(raise_exception)