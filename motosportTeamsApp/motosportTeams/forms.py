from django import forms

class CarForm(forms.Form):
    mark = forms.CharField(label='mark', max_length=200)
    model = forms.CharField(label='model', max_length=250)
    car_type = forms.CharField(label='Car Type', max_length=200)
