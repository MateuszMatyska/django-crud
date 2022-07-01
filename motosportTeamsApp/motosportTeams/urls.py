from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('cars',views.cars,name="cars"),
    path('cars/addcar',views.add_car,name='addcar'),
    path('cars/editcar/<int:car_id>',views.edit_car,name='editcar'),
    path('cars/deletecar/<int:car_id>',views.delete_car,name="deletecar"),
    path('drivers',views.drivers,name="drivers"),
    path('drivers/adddriver',views.add_driver,name='adddriver'),
    path('drivers/editdriver/<int:driver_id>',views.edit_driver,name="editdriver"),
    path('drivers/deletedriver/<int:driver_id>',views.delete_driver,name="deletedriver"),
]