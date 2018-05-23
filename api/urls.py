from django.contrib import admin
from django.urls import path, include
from django.conf.urls import  url



# from django.core.urlresolvers import resolve
from django.urls import resolve
from . import views



app_name = 'api'

urlpatterns = [
    path('booking/list',                              views.booking_list,            name='booking_list'),
    path('vehicle/list',                              views.vehicle_list,            name='vehicle_list'),
]

