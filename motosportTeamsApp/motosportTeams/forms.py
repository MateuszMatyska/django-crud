from django import forms

from motosportTeams.models import Car

class CarForm(forms.Form):
    mark = forms.CharField(label='mark', max_length=200)
    model = forms.CharField(label='model', max_length=250)
    car_type = forms.CharField(label='Car Type', max_length=200)

class DriverForm(forms.Form):
    first_name = forms.CharField(label='first_name', max_length=200)
    last_name = forms.CharField(label='last_name', max_length=200)
    car = forms.ModelChoiceField(queryset=Car.objects.all())
