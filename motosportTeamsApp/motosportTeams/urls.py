from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('cars',views.cars,name="cars"),
    path('cars/addcar',views.add_car,name='addcar'),
    path('cars/editcar/<int:car_id>',views.edit_car,name='editcar'),
    path('cars/deletecar/<int:car_id>',views.delete_car,name="deletecar"),
    path('drivers',views.drivers,name="drivers"),
]