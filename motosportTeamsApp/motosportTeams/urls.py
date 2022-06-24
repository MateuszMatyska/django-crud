from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('cars',views.cars,name="cars"),
    path('cars/addcar',views.add_car, name='addcar'),
    # path('cars/editcar',,name='editcar'),
    path('drivers',views.drivers,name="drivers"),
]