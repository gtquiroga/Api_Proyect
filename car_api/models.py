from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CarModel(models.Model):
    manufacturer = models.ForeignKey(
        Manufacturer, 
        on_delete=models.CASCADE,
        related_name='car_models')
    name = models.CharField(max_length=100)
    production_year = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta: 
        unique_together = [["manufacturer", "name", "production_year"]]

class Car(models.Model):
    car_model = models.ForeignKey(
        CarModel, 
        on_delete=models.CASCADE,
        related_name='cars')
    manufacturing_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)