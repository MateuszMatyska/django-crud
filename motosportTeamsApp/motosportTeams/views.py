from multiprocessing import context
from statistics import mode
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

def edit_car(request, car_id):
    if request.method == 'POST':
        form = forms.CarForm(request.POST)
        if form.is_valid:
            car = models.Car.objects.get(id = car_id)
            car.mark = request.POST['mark']
            car.model = request.POST['model']
            car.car_type = request.POST['car_type']
            car.save()
            return HttpResponseRedirect('/cars')   
    else:
        car = models.Car.objects.get(id = car_id)
        context = {'car': car}
        return render(request, 'cars/edit_car.html', context)    
        
def delete_car(request, car_id):
    if car_id > 0:
        car = models.Car.objects.get(id = car_id)
        car.delete()
        return HttpResponseRedirect('/cars')
    else: 
        return HttpResponseRedirect('/cars')

def drivers(request):
    drivers = models.Driver.objects.all()
    context = {'drivers_list': drivers}
    return render(request, 'drivers/index.html', context)

def add_driver(request):
    if request.method == 'POST':
        form = forms.DriverForm(request.POST)
        if form.is_valid:
            driver = models.Driver()
            driver.first_name = request.POST['first_name']
            driver.last_name = request.POST['last_name']
            car_id = request.POST['car_id']
            car = models.Car.objects.get(id = car_id)
            driver.car = car
            driver.save()
            return HttpResponseRedirect('/drivers')   
    else:
        cars = models.Car.objects.all()
        context = {'cars': cars}
        return render(request, 'drivers/add_driver.html', context)  

def edit_driver(request, driver_id):
    if request.method == 'POST':
        form = forms.DriverForm(request.POST)
        if form.is_valid:
            driver = models.Driver.objects.get(id = driver_id)
            driver.first_name = request.POST['first_name']
            driver.last_name = request.POST['last_name']
            car_id = request.POST['car_id']
            car = models.Car.objects.get(id = car_id)
            driver.car = car
            driver.save()
            return HttpResponseRedirect('/drivers')   
    else:
        cars = models.Car.objects.all()
        driver = models.Driver.objects.get(id = driver_id)
        context = {'cars': cars, 'driver': driver}
        return render(request, 'drivers/edit_driver.html', context) 

def delete_driver(request, driver_id):
    if driver_id > 0:
        driver = models.Driver.objects.get(id = driver_id)
        driver.delete()
        return HttpResponseRedirect('/drivers')
    else: 
        return HttpResponseRedirect('/drivers')