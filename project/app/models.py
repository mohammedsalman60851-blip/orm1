from django.db import models
from django.contrib import admin
class Car(models.Model):
    car_id = models.AutoField(primary_key=True)   # Primary Key
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    fuel_type = models.CharField(max_length=20)

class CarAdmin(admin.ModelAdmin):
    list_display = ('car_id', 'brand', 'model', 'year', 'price','fuel_type')
