from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from . import models
from . import forms

def index(request):
    return HttpResponse("MotoSportTeams app")

def cars(request):
    cars = models.Car.objects.all()
    context = {'cars_list': cars}
    return render(request, 'cars/index.html', context)

def add_car(request):
    if request.method == 'POST':
        form = forms.CarForm(request.POST)
        if form.is_valid:
            car = models.Car()
            car.mark = request.POST['mark']
            car.model = request.POST['model']
            car.car_type = request.POST['car_type']
            car.save()
            return HttpResponseRedirect('/cars')   
    else:
        return render(request, 'cars/add_car.html')    

def edit_car(request):
    return HttpResponse("Car edit")


def drivers(request):
    return HttpResponse("Drivers view")