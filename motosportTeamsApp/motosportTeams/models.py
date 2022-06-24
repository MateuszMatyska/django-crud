from django.db import models

class Car(models.Model):
    mark = models.CharField(max_length=200)
    model = models.CharField(max_length=250)
    car_type = models.CharField(max_length=200)


class Driver(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, null=True)